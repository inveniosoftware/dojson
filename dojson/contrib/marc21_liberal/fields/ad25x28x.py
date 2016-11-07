# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('complex_see_reference_subject', '^260..')
@utils.for_each_value
@utils.filter_values
def complex_see_reference_subject(self, key, value):
    """Complex See Reference-Subject."""
    field_map = {
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'i': 'explanatory_text',
        '0': 'authority_record_control_number',
        'a': 'heading_referred_to',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
