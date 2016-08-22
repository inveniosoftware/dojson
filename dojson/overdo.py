# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Do JSON translation."""

import re

from pkg_resources import iter_entry_points

from ._compat import iteritems, zip_longest
from .errors import IgnoreKey, MissingRule
from .utils import GroupableOrderedDict

try:
    from _sre import MAXGROUPS
except ImportError:
    MAXGROUPS = 100


class Index(object):
    """Index implementation based on build-in Python SRE module."""

    def __init__(self, rules=None, flags=0, branch_size=MAXGROUPS - 1):
        """Initialize index structures.

        :param rules: list of tuples (regular expression, data)
        :param flags: additional flags passed to SRE parser
        :param branch_size: number of groups in a branch (max. 99)
        """
        self._patterns = []
        self.flags = flags
        self.rules = rules or []
        self.branch_size = min(branch_size, len(self.rules))

        def make_pattern(rules, flags=0):
            """Compile a rules to single branch with groups."""
            return re.compile('|'.join('(?P<I{name}>{regex})'.format(
                name=name, regex=regex
            ) for name, (regex, _) in enumerate(rules)), flags=flags)

        for rules in zip_longest(*[iter(self.rules)] * self.branch_size):
            self._patterns.append(make_pattern([
                rule for rule in rules if rule is not None
            ]))

    def query(self, key):
        """Return data matching the key."""
        for section, pattern in enumerate(self._patterns):
            match = pattern.match(key)
            if match:
                return self.rules[section * self.branch_size + int(
                    match.lastgroup[1:]
                )][1]


class Overdo(object):
    """Translation index."""

    def __init__(self, bases=None, entry_point_group=None):
        """Constructor."""
        self.rules = []
        if bases:
            for base in bases:
                base._collect_entry_points()
                self.rules.extend(base.rules)
        self.entry_point_group = entry_point_group
        self.index = None

    def _collect_entry_points(self):
        """Collect entry points."""
        if self.entry_point_group is not None:
            for entry_point in iter_entry_points(
                    group=self.entry_point_group, name=None):
                entry_point.load()

    def build(self):
        """Build."""
        self._collect_entry_points()
        self.index = Index(self.rules)

    def over(self, name, *source_tags):
        """Register creator rule."""
        def decorator(creator):
            self.index = None
            for field in source_tags:
                self.rules.append((field, (name, creator)))
            return creator
        return decorator

    def do(self, blob, ignore_missing=True, exception_handlers=None):
        """Translate blob values and instantiate new model instance.

        Raises ``MissingRule`` when no rule matched and ``ignore_missing``
        is ``False``.

        :param blob: ``dict``-like object on which the matching rules are
                     going to be applied.
        :param ignore_missing: Set to ``False`` if you prefer to raise
                               an exception ``MissingRule`` for the first
                               key that it is not matching any rule.
        :param exception_handlers: Give custom exception handlers to take care
                                   of non-standard codes that are installation
                                   specific.

        .. versionchanged:: 1.0.0

           ``ignore_missing`` allows to specify if the function should raise
           an exception.

        .. versionchanged:: 1.1.0

           ``exception_handlers`` allows to set custom handlers for
           non-standard MARC codes.
        """
        handlers = {IgnoreKey: None}
        handlers.update(exception_handlers or {})

        def clean_missing(exc, output, key, value):
            order = output.get('__order__')
            if order:
                order.remove(key)

        if ignore_missing:
            handlers.setdefault(MissingRule, clean_missing)

        output = {}

        if self.index is None:
            self.build()

        if isinstance(blob, GroupableOrderedDict):
            items = blob.iteritems(repeated=True)
        else:
            items = iteritems(blob)

        for key, value in items:
            try:
                result = self.index.query(key)
                if not result:
                    raise MissingRule(key)

                name, creator = result
                data = creator(output, key, value)
                if getattr(creator, '__extend__', False):
                    existing = output.get(name, [])
                    existing.extend(data)
                    output[name] = existing
                else:
                    output[name] = data
            except Exception as exc:
                if exc.__class__ in handlers:
                    handler = handlers[exc.__class__]
                    if handler is not None:
                        handler(exc, output, key, value)
                else:
                    raise

        return output

    def missing(self, blob):
        """Return keys with missing rules."""
        if self.index is None:
            self.build()
        return [key for key in blob.keys() if self.index.query(key) is None]
