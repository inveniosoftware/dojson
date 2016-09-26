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


@marc21_authority.over('leader', '^leader')
@utils.filter_values
def leader(self, key, value):
    """Leader."""
    record_status = {
        'a': 'increase_in_encoding_level',
        'c': 'corrected_or_revised',
        'd': 'deleted',
        'n': 'new',
        'o': 'obsolete',
        's': 'deleted_heading_split_into_two_or_more_headings',
        'x': 'deleted_heading_replaced_by_another_heading',
    }
    type_of_record = {
        'z': 'authority_data',
    }
    character_coding_scheme = {
        '#': 'marc-8',
        'a': 'ucs_unicode'
    }
    indicator_count = {
        '2': 'number_of_character_positions_used_for_a_subfield_code',
    }
    subfield_code_length = {
        '2': 'number_of_character_positions_used_for_indicators',
    }
    encoding_level = {
        'n': 'complete_authority_record',
        'o': 'incomplete_authority_record',
    }

    length_of_the_length_of_field_portion = {
        '4': 4,
    }
    length_of_the_starting_character_position_portion = {
        '5': 5,
    }
    length_of_the_implementation_defined_portion = {
        '0': 0,
    }
    undefined = {
        '0': 0,
    }

    return {
        'record_length': int(value[:5]),
        'record_status': record_status.get(value[5]),
        'type_of_record': type_of_record.get(value[6]),
        'character_coding_scheme': character_coding_scheme.get(value[9]),
        'indicator_count': int(value[10]),
        'subfield_code_length': int(value[11]),
        'base_address_of_data': int(value[12:17]),
        'encoding_level': encoding_level.get(value[17]),
        'length_of_the_length_of_field_portion':
            length_of_the_length_of_field_portion.get(value[20]),
        'length_of_the_starting_character_position_portion':
            length_of_the_starting_character_position_portion.get(value[21]),
        'length_of_the_implementation_defined_portion':
            length_of_the_implementation_defined_portion.get(value[22]),
        'undefined': undefined.get(value[23])
    }
