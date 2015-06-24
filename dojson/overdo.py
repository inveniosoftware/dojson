# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Do JSON translation."""

import esmre

from six import iteritems


class Overdo(object):

    """Translation index."""

    def __init__(self):
        self.rules = []
        self.index = None

    def build(self):
        self.index = esmre.Index()
        for rule in self.rules:
            self.index.enter(*rule)

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
            for name, creator in self.index.query(key):
                output[name] = creator(output, key, value)

        return output

    def missing(self, blob):
        """Return keys with missing rules."""
        return [key for key in blob.keys() if not len(self.index.query(key))]
