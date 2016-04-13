# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('leader', '^leader')
def to_leader(self, key, value):
    """To Leader."""
    record_status = {
        'increase_in_encoding_level': 'a',
        'corrected_or_revised': 'c',
        'deleted': 'd',
        'new': 'n',
        'increase_in_encoding_level_from_prepublication': 'p'
    }
    type_of_record = {
        'language_material': 'a',
        'notated_music': 'c',
        'manuscript_notated_music': 'd',
        'cartographic_material': 'e',
        'manuscript_cartographic_material': 'f',
        'projected_medium': 'g',
        'nonmusical_sound_recording': 'i',
        'musical_sound_recording': 'j',
        'two-dimensional_nonprojectable_graphic': 'k',
        'computer_file': 'm',
        'kit': 'o',
        'mixed_materials': 'p',
        'three-dimensional_artifact_or_naturally_occuring_object': 'r',
        'manuscript_language_material': 't',
    }
    bibliographic_level = {
        'monographic_component_part': 'a',
        'serial_component_part': 'b',
        'collection': 'c',
        'subunit': 'd',
        'integrating_resource': 'i',
        'monograph_item': 'm',
        'serial': 's',
    }
    type_of_control = {
        'no_specified_type': '#',
        'archival': 'a',
    }
    character_coding_scheme = {
        'marc-8': '#',
        'ucs_unicode': 'a'
    }
    encoding_level = {
        'full_level': '#',
        'full_level_material_not_examined': '1',
        'less-than-full_level_material_not_examined': '2',
        'abbreviated_level': '3',
        'core_level': '4',
        'partial_preliminary_level': '5',
        'minimal_level': '7',
        'prepublication_level': '8',
        'unknown': 'u',
        'not_applicable': 'z',
    }
    descriptive_cataloging_form = {
        'non-isbd': '#',
        'aacr_2': 'a',
        'isbd_punctuation_omitteed': 'c',
        'isbd_punctuation_included': 'i',
        'unknown': 'u',
    }
    multipart_resource_record_level = {
        'not_specified_or_not_applicable': '#',
        'set': 'a',
        'part_with_independent_title': 'b',
        'part_with_dependent_title': 'c',
    }

    length_of_field_portion = {
        4: '4',
    }
    starting_character_position_portion = {
        5: '5',
    }
    implementation_defined_portion = {
        0: '0',
    }
    undefined = {
        0: '0',
    }

    leader_string = (
        '{record_length!s:0>5}{record_status}{type_of_record}'
        '{bibliographic_level}{type_of_control}{character_coding_scheme}'
        '{indicator_count!s}{subfield_code_count!s}{base_address_of_data!s:0>5}'
        '{encoding_level}{descriptive_cataloging_form}'
        '{multipart_resource_record_level}'
        '{length_of_the_length_of_field_portion}'
        '{length_of_the_starting_character_position_portion}'
        '{length_of_the_implementation_defined_portion}'
        '{undefined}'
    ).format(
        record_length=value.get('record_length', '     '),
        record_status=record_status.get(value.get('record_status'), ' '),
        type_of_record=type_of_record.get(value.get('type_of_record'), ' '),
        bibliographic_level=bibliographic_level.get(value.get(
            'bibliographic_level'), ' '),
        type_of_control=type_of_control.get(value.get('type_of_control'), ' '),
        character_coding_scheme=character_coding_scheme.get(
            value.get('character_coding_scheme'), ' '),
        indicator_count=value.get('indicator_count', ' '),
        subfield_code_count=value.get('subfield_code_count', ' '),
        base_address_of_data=value.get('base_address_of_data', '     '),
        encoding_level=encoding_level.get(value.get('encoding_level'), ' '),
        descriptive_cataloging_form=descriptive_cataloging_form.get(
            value.get('descriptive_cataloging_form'), ' '),
        multipart_resource_record_level=multipart_resource_record_level.get(
            value.get('multipart_resource_record_level'), ' '),
        length_of_the_length_of_field_portion=length_of_field_portion.get(
            value.get('length_of_the_length_of_field_portion'), ' '),
        length_of_the_starting_character_position_portion=starting_character_position_portion.get(
            value.get('length_of_the_starting_character_position_portion'), ' '),
        length_of_the_implementation_defined_portion=implementation_defined_portion.get(
            value.get('length_of_the_implementation_defined_portion'), ' '),
        undefined=undefined.get(value.get('undefined'), ' '),
    )

    assert len(leader_string) == 24

    return leader_string
