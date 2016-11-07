# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Define DoJSON handlers."""

from dojson.errors import MissingRule
from dojson.utils import GroupableOrderedDict


def marc21_liberal_handler(exc, output, key, value):
    """When a key cannot be translated, simply use the number instead."""
    if exc.__class__ is MissingRule:
        if key != '__order__':
            field = key[:3]

            # Convert value from GroupableOrderedDict for mutability
            value = dict(value)

            # Convert '__order__' to list for mutability
            value['__order__'] = list(value['__order__'])
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

            output[field] = value
        else:
            pass
    else:
        raise exc


def to_marc21_liberal_handler(exc, output, key, value):
    """When a key cannot be translated, simply use the number instead."""
    if exc.__class__ is MissingRule:
        if key != '__order__':
            # Convert value from GroupableOrderedDict for mutability
            value = dict(value)

            field = '{0}{1}{2}'.format(
                key, value.pop('$ind1', ['_'])[0],
                value.pop('$ind2', ['_'])[0])

            # Convert '__order__' to list for mutability
            value['__order__'] = list(value['__order__'])
            try:
                value['__order__'].remove('$ind1')
            except ValueError:
                pass
            try:
                value['__order__'].remove('$ind2')
            except ValueError:
                pass

            value = GroupableOrderedDict(value)
            output.append((field, value))
        else:
            pass
    else:
        raise exc
