# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Do JSON translation."""

from sre_parse import Pattern, SubPattern, parse
from sre_compile import compile as sre_compile
from sre_constants import BRANCH, SUBPATTERN

from pkg_resources import iter_entry_points

from six import iteritems
from six.moves import zip_longest
from .utils import IgnoreKey


class Index(object):
    """Index implementation based on build-in Python SRE module."""

    def __init__(self, rules=None, flags=0, branch_size=99):
        """Initialize index structures.

        :param rules: list of tuples (regular expression, data)
        :param flags: additional flags passed to SRE parser
        :param branch_size: number of groups in a branch (max. 99)
        """
        self._patterns = []
        self.flags = flags
        self.rules = rules or []
        self.branch_size = branch_size

        def make_pattern(rules, flags=0):
            """Compile a rules to single branch with groups."""
            pattern = Pattern()
            pattern.flags = flags
            pattern.subpatterns = [None] * (len(rules) + 1)

            return sre_compile(SubPattern(pattern, [
                (BRANCH, (None, [SubPattern(pattern, [
                    (SUBPATTERN, (group, parse(regex, flags, pattern))),
                ]) for group, (regex, _) in enumerate(rules, 1)]))
            ]))

        for rules in zip_longest(*[iter(self.rules)] * self.branch_size):
            self._patterns.append(make_pattern([
                rule for rule in rules if rule is not None
            ]))

    def query(self, key):
        """Yield data matching the key."""
        for section, pattern in enumerate(self._patterns):
            match = pattern.match(key)
            if match:
                return self.rules[
                    section * self.branch_size + match.lastindex - 1
                ][1]


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

    def do(self, blob):
        """Translate blob values and instantiate new model instance."""
        output = {}

        if self.index is None:
            self.build()

        for key, value in iteritems(blob):
            result = self.index.query(key)
            if result:
                name, creator = result
                try:
                    data = creator(output, key, value)
                    if getattr(creator, '__extend__', False):
                        existing = output.get(name, [])
                        existing.extend(data)
                        output[name] = existing
                    else:
                        output[name] = data
                except IgnoreKey:
                    pass

        return output

    def missing(self, blob):
        """Return keys with missing rules."""
        if self.index is None:
            self.build()
        return [key for key in blob.keys() if self.index.query(key) is None]
