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

from dojson import Overdo
from dojson.errors import IgnoreKey
from dojson.utils import GroupableOrderedDict


warnings.warn('MARC21 undo feature is experimental')


class Underdo(Overdo):
    """Translation index specification for reverse marc21 translation."""

    def do(self, blob):
        """Translate blob values and instantiate new model instance.

        Takes out the indicators, if any, from the returned dictionary and puts
        them into the key.
        """
        output = []

        if self.index is None:
            self.build()

        if '__order__' in blob and not isinstance(blob, GroupableOrderedDict):
            blob = GroupableOrderedDict(blob)

        if '__order__' in blob:
            items = blob.iteritems(repeated=True)
        else:
            items = iteritems(blob)

        for key, item in items:
            result = self.index.query(key)
            if result:
                name, creator = result
                try:
                    value = creator(output, key, item)

                    if isinstance(value, MutableMapping):
                        k = ''.join((name,
                                     value.pop('$ind1', '_'),
                                     value.pop('$ind2', '_')))
                        if '__order__' in value or isinstance(value, dict):
                            value = GroupableOrderedDict(value)
                        output.append((k, value))
                    elif isinstance(value, MutableSequence):
                        for v in value:
                            try:
                                k = ''.join((name,
                                             v.pop('$ind1', '_'),
                                             v.pop('$ind2', '_')))
                            except AttributeError:
                                k = name

                            if '__order__' in v or isinstance(v, dict):
                                v = GroupableOrderedDict(v)
                            output.append((k, v))
                    else:
                        k = ''.join((name,
                                     value.pop('$ind1', '_'),
                                     value.pop('$ind2', '_')))
                        output.append((k, value))
                except IgnoreKey:
                    warnings.warn('{} was ignored in to_marc21.do'.format(key))

        return GroupableOrderedDict(output)


to_marc21 = Underdo(entry_point_group='dojson.contrib.to_marc21')
