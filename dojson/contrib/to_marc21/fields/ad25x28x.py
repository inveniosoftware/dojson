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

from ..model import to_marc21_authority


@to_marc21_authority.over('260', '^complex_see_reference_subject$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_complex_see_reference_subject(self, key, value):
    """Reverse - Complex See Reference-Subject."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
        'linkage': '6',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
