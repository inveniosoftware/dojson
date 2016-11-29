# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 liberal utils."""

import re

from dojson.errors import MissingRule
from dojson.utils import GroupableOrderedDict


def to_marc21_liberal_handler(exc, output, key, value):
    """When a key cannot be translated, simply use the number instead."""
    if exc.__class__ is MissingRule:

        datafield_pattern = re.compile('^\d{3}$')
        if datafield_pattern.match(key):

            # All custom datafields are by default lists
            if not isinstance(value, (tuple, list)):
                value = [value]
            for element in value:
                # Is it a datafield (i.e. do we have subfields)?
                if isinstance(element, (GroupableOrderedDict, dict)):
                    # Convert value from GroupableOrderedDict for mutability
                    element = dict(element)

                    field = '{0}{1}{2}'.format(
                        key, element.pop('$ind1', ['_'])[0],
                        element.pop('$ind2', ['_'])[0])

                    # If there's no order, add one
                    if '__order__' not in element:
                        element['__order__'] = list(element.keys())

                    # Convert '__order__' to list for mutability
                    element['__order__'] = list(element['__order__'])

                    # Remove indicators from order
                    try:
                        element['__order__'].remove('$ind1')
                    except ValueError:
                        pass
                    try:
                        element['__order__'].remove('$ind2')
                    except ValueError:
                        pass

                    element = GroupableOrderedDict(element)

                # Else, we have a controlfield, without indicators
                else:
                    field = '{0}'.format(key)

                output.append((field, element))
        else:
            pass
    else:
        raise exc
