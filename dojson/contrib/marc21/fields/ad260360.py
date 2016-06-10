# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_authority


@marc21_authority.over('complex_see_reference_subject', '^260..')
@utils.for_each_value
@utils.filter_values
def complex_see_reference_subject(self, key, value):
    """Complex See Reference-Subject."""
    field_map = {
        'a': 'heading_referred_to',
        'i': 'explanatory_text',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('complex_see_also_reference_subject', '^360..')
@utils.for_each_value
@utils.filter_values
def complex_see_also_reference_subject(self, key, value):
    """Complex See Also Reference-Subject."""
    field_map = {
        'a': 'heading_referred_to',
        'i': 'explanatory_text',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }
