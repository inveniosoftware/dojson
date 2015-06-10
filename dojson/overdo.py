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
        self.index = esmre.Index()

    def over(self, name, *source_tags):
        """Register creator rule."""
        def decorator(creator):
            for field in source_tags:
                self.index.enter(field, (name, creator))
            return creator
        return decorator

    def do(self, blob):
        """Translate blob values and instantiate new model instance."""
        output = {}

        for key, value in iteritems(blob):
            for name, creator in self.index.query(key):
                output[name] = creator(output, key, value)

        return output
