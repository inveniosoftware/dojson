# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils
from dojson.contrib.marc21_liberal.utils import liberal_map_order

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('260', '^complex_see_reference_subject$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_complex_see_reference_subject(self, key, value):
    """Reverse - Complex See Reference-Subject."""

    field_map = {
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
        'authority_record_control_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
