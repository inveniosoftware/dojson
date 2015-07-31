# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Do JSON translation."""

import re

import esmre

from six import iteritems


class Overdo(object):

    """Translation index."""

    def __init__(self):
        """Constructor."""
        self.rules = []
        self.index = None

    def build(self):
        """Build."""
        self.index = esmre.Index()
        for rule in self.rules:
            self.index.enter(*rule)

    def over(self, name, *source_tags):
        """Register creator rule."""
        def decorator(creator):
            self.index = None
            for field in source_tags:
                self.rules.append((field, (name, creator, re.compile(field))))
            return creator
        return decorator

    def _query(self, key):
        """Query."""
        for name, creator, field in self.index.query(key):
            if field.match(key):
                yield name, creator, field

    def do(self, blob):
        """Translate blob values and instantiate new model instance."""
        output = {}

        if self.index is None:
            self.build()

        for key, value in iteritems(blob):
            for name, creator, field in self._query(key):
                output[name] = creator(output, key, value)

        return output

    def undo(self, blob):
        """Translate blob values from json to marc21 and instantiate new model instance.

        This does the same what 'do' does, but takes into
        account indicator which might change key when
        translating from json to marc21
        """
        output = {}

        if self.index is None:
            self.build()

        for key, value in iteritems(blob):
            for name, creator, field in self._query(key):
                translation_result = creator(output, key, value)

                repr_result = translation_result
                if isinstance(translation_result, list):
                    repr_result = translation_result[0]
                    if isinstance(translation_result[0], dict):
                        for element in translation_result[1:]:
                            element.pop('_indicator1', '_')
                            element.pop('_indicator2', '_')

                if isinstance(repr_result, dict):
                    indicator_1 = repr_result.pop('_indicator1', '_')
                    indicator_2 = repr_result.pop('_indicator2', '_')
                else:
                    indicator_1 = None
                    indicator_2 = None

                altered_name = self._change_name(name, indicator_1, indicator_2)

                output[altered_name] = translation_result

        return output

    def _change_name(self, name, indicator_1, indicator_2):
        if name.startswith('^'):
            name = name[1:]

        key = name[:3]

        if not indicator_1 and not indicator_2:
            return key

        return key + indicator_1 + indicator_2


    def missing(self, blob):
        """Return keys with missing rules."""
        if self.index is None:
            self.build()
        return [key for key in blob.keys() if not len(list(self._query(key)))]
