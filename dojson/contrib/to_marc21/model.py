# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

import warnings

from dojson import Overdo
from dojson import utils

from six import iteritems

warnings.warn('MARC21 undo feature is experimental')


class OverUndo(Overdo):

    """Translation index specification for reverse marc21 translation."""

    def do(self, blob):
        """Translate blob values and instantiate new model instance.

        Takes out the indicators, if any, from the returned dictionary and puts
        them into the key.
        """
        output = {}

        if self.index is None:
            self.build()

        for key, value in iteritems(blob):
            for name, creator, field in self._query(key):
                try:
                    value = creator(output, key, value)
                    try:
                        name = '{0}{1}{2}'.format(name, value.pop('$ind1', ''),
                                                  value.pop('$ind2', ''))
                    except TypeError:
                        # It is not a dictionary, there are indicators.
                        name = name
                    output[name] = value
                except utils.IgnoreKey:
                    pass

        return output


to_marc21 = OverUndo(entry_point_group='dojson.contrib.to_marc21')
