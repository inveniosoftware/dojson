# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 liberal utils."""

import re

from dojson.errors import MissingRule
from dojson.utils import GroupableOrderedDict


def marc21_liberal_handler(exc, output, key, value):
    """When a key cannot be translated, simply use the number instead."""
    if exc.__class__ is MissingRule:

        datafield_pattern = re.compile('^\d{3}[\d\w_]{0,2}$')
        if datafield_pattern.match(key):

            key = "{0:_<5}".format(key)
            field = key[:3]

            # Is it a datafield (i.e. do we have subfields)?
            if isinstance(value, GroupableOrderedDict):
                # Convert value from GroupableOrderedDict for mutability
                value = dict(value)
                # Convert '__order__' to list for mutability
                value['__order__'] = list(value['__order__'])

                # Do we have indicators?
                if key[3] != '_':
                    value['$ind1'] = key[3]
                    value['__order__'].append('$ind1')
                if key[4] != '_':
                    value['$ind2'] = key[4]
                    value['__order__'].append('$ind2')

                value = GroupableOrderedDict(value)

                # Rewrite the record's '__order__' to remove indicators
                output['__order__'] = [field if elem == key else elem
                                       for elem in output['__order__']]

            # Treat all custom fields as repeatable
            if field in output:
                output[field].append(value)
            else:
                output[field] = [value]
        else:
            pass
    else:
        raise exc


def liberal_map_order(field_map, value, indicators=None):
    """Ordered list of fields to be able to pass the order along.

    .. note:: It returns a list as you may want to alter it based on the
       indicators. The final structure should use a tuple for immutability.

    Returns an empty list if no `__order__' is found in the value.

    .. versionadded:: 1.1.0
    """
    if '__order__'in value:
        order = value['__order__']
    else:
        order = value.keys()

    if not indicators:
        indicators = []
    returnlist = []
    for k in order:
        if k in field_map:
            returnlist.append(field_map[k])
        elif len(k) == 1:
            returnlist.append(k)
    return returnlist
