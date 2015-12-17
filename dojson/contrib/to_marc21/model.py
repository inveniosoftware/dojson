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
from collections import MutableMapping, MutableSequence

from six import iteritems

from dojson import Overdo, utils

warnings.warn('MARC21 undo feature is experimental')


class Underdo(Overdo):
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
            result = self.index.query(key)
            if result:
                name, creator = result
                try:
                    value = creator(output, key, value)
                    if isinstance(value, MutableMapping):
                        output['{0}{1}{2}'.format(
                            name, value.pop('$ind1', '_'),
                            value.pop('$ind2', '_'))] = value
                    elif isinstance(value, MutableSequence):
                        for v in value:
                            try:
                                key = '{0}{1}{2}'.format(
                                    name, v.pop('$ind1', '_'),
                                    v.pop('$ind2', '_'))
                            except AttributeError:
                                key = name
                            if key in output:
                                output[key].append(v)
                            else:
                                output[key] = [v]
                    else:
                        output[name] = value
                except utils.IgnoreKey:
                    pass

        return output


to_marc21 = Underdo(entry_point_group='dojson.contrib.to_marc21')
