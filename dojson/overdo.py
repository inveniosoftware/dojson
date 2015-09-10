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
from .utils import IgnoreKey


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
                try:
                    output[name] = creator(output, key, value)
                except IgnoreKey:
                    pass

        return output

    def missing(self, blob):
        """Return keys with missing rules."""
        if self.index is None:
            self.build()
        return [key for key in blob.keys() if not len(list(self._query(key)))]
