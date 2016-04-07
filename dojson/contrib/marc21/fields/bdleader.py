# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21


@marc21.over('leader', '^leader')
@utils.filter_values
def leader(self, key, value):
    """Leader."""
    record_status = {
        'a': 'increase_in_encoding_level',
        'c': 'corrected_or_revised',
        'd': 'deleted',
        'n': 'new',
        'p': 'increase_in_encoding_level_from_prepublication'
    }
    type_of_record = {
        'a': 'language_material',
        'c': 'notated_music',
        'd': 'manuscript_notated_music',
        'e': 'cartographic_material',
        'f': 'manuscript_cartographic_material',
        'g': 'projected_medium',
        'i': 'nonmusical_sound_recording',
        'j': 'musical_sound_recording',
        'k': 'two-dimensional_nonprojectable_graphic',
        'm': 'computer_file',
        'o': 'kit',
        'p': 'mixed_materials',
        'r': 'three-dimensional_artifact_or_naturally_occuring_object',
        't': 'manuscript_language_material',
    }
    bibliographic_level = {
        'a': 'monographic_component_part',
        'b': 'serial_component_part',
        'c': 'collection',
        'd': 'subunit',
        'i': 'integrating_resource',
        'm': 'monograph_item',
        's': 'serial',
    }
    type_of_control = {
        '#': 'no_specified_type',
        'a': 'archival',
    }
    character_coding_scheme = {
        '#': 'marc-8',
        'a': 'ucs_unicode'
    }
    encoding_level = {
        '#': 'full_level',
        '1': 'full_level_material_not_examined',
        '2': 'less-than-full_level_material_not_examined',
        '3': 'abbreviated_level',
        '4': 'core_level',
        '5': 'partial_preliminary_level',
        '7': 'minimal_level',
        '8': 'prepublication_level',
        'u': 'unknown',
        'z': 'not_applicable',
    }
    descriptive_cataloging_form = {
        '#': 'non-isbd',
        'a': 'aacr_2',
        'c': 'isbd_punctuation_omitteed',
        'i': 'isbd_punctuation_included',
        'u': 'unknown',
    }
    multipart_resource_record_level = {
        '#': 'not_specified_or_not_applicable',
        'a': 'set',
        'b': 'part_with_independent_title',
        'c': 'part_with_dependent_title',
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
        'bibliographic_level': bibliographic_level.get(value[7]),
        'type_of_control': type_of_control.get(value[8]),
        'character_coding_scheme': character_coding_scheme.get(value[9]),
        'indicator_count': int(value[10]),
        'subfield_code_count': int(value[11]),
        'base_address_of_data': int(value[12:17]),
        'encoding_level': encoding_level.get(value[17]),
        'descriptive_cataloging_form': descriptive_cataloging_form.get(value[18]),
        'multipart_resource_record_level': multipart_resource_record_level.get(value[19]),
        'length_of_the_length_of_field_portion':
            length_of_the_length_of_field_portion.get(value[20]),
        'length_of_the_starting_character_position_portion':
            length_of_the_starting_character_position_portion.get(value[21]),
        'length_of_the_implementation_defined_portion':
            length_of_the_implementation_defined_portion.get(value[22]),
        'undefined': undefined.get(value[23])
    }
