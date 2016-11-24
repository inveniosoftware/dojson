# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 liberal utils."""

from dojson.errors import MissingRule
from dojson.utils import GroupableOrderedDict


def to_marc21_liberal_handler(exc, output, key, value):
    """When a key cannot be translated, simply use the number instead."""
    if exc.__class__ is MissingRule:
        if key != '__order__':

            # Is it a datafield (i.e. do we have subfields)?
            if isinstance(value, GroupableOrderedDict):
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

            # Else, we have a controlfield, without indicators
            else:
                field = '{0}'.format(key)

            output.append((field, value))
        else:
            pass
    else:
        raise exc
