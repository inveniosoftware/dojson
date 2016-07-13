# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

import warnings
from collections import MutableMapping, MutableSequence
from operator import itemgetter

from dojson import Overdo
from dojson._compat import iteritems
from dojson.errors import IgnoreKey, MissingRule
from dojson.utils import GroupableOrderedDict

warnings.warn('MARC21 undo feature is experimental')


class Underdo(Overdo):
    """Translation index specification for reverse marc21 translation."""

    def do(self, blob, ignore_missing=True, exception_handlers=None):
        """Translate blob values and instantiate new model instance.

        Takes out the indicators, if any, from the returned dictionary and puts
        them into the key.

        :param blob: ``dict``-like object on which the matching rules are
                     going to be applied.
        :param ignore_missing: Set to ``False`` if you prefer to raise
                               an exception ``MissingRule`` for the first
                               key that it is not matching any rule.
        :param exception_handlers: Give custom exception handlers to take care
                                   of non-standard names that are installation
                                   specific.

        .. versionadded:: 1.0.0

           ``ignore_missing`` allows to specify if the function should raise
           an exception.

        .. versionadded:: 1.1.0

           ``exception_handlers`` allows unknown keys to treated in a custom
           fashion.
        """
        handlers = {IgnoreKey: None}
        handlers.update(exception_handlers or {})

        if ignore_missing:
            handlers.setdefault(MissingRule, None)

        output = []

        if self.index is None:
            self.build()

        if '__order__' in blob and not isinstance(blob, GroupableOrderedDict):
            blob = GroupableOrderedDict(blob)

        if '__order__' in blob:
            items = blob.iteritems(repeated=True)
        else:
            items = iteritems(blob)

        for key, value in items:
            try:
                result = self.index.query(key)
                if not result:
                    raise MissingRule(key)

                name, creator = result
                item = creator(output, key, value)
                if isinstance(item, MutableMapping):
                    field = '{0}{1}{2}'.format(
                        name, item.pop('$ind1', '_'),
                        item.pop('$ind2', '_'))
                    if '__order__' in item:
                        item = GroupableOrderedDict(item)
                    output.append((field, item))
                elif isinstance(item, MutableSequence):
                    for v in item:
                        try:
                            field = '{0}{1}{2}'.format(
                                name, v.pop('$ind1', '_'),
                                v.pop('$ind2', '_'))
                        except AttributeError:
                            field = name
                        output.append((field, v))
                else:
                    output.append((name, item))
            except Exception as exc:
                if exc.__class__ in handlers:
                    handler = handlers[exc.__class__]
                    if handler is not None:
                        handler(exc, output, key, value)
                else:
                    raise

        return GroupableOrderedDict(output)


to_marc21 = Underdo(entry_point_group='dojson.contrib.to_marc21')

to_marc21_authority = Underdo(
    entry_point_group='dojson.contrib.to_marc21_authority')
"""MARC 21 Format for Authority Data."""
