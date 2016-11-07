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

from ..model import marc21_liberal


@marc21_liberal.over('series_added_entry_personal_name', '^800..')
@utils.for_each_value
@utils.filter_values
def series_added_entry_personal_name(self, key, value):
    """Series Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'r': 'key_for_music',
        'd': 'dates_associated_with_a_name',
        'b': 'numeration',
        'f': 'date_of_a_work',
        'j': 'attribution_qualifier',
        'q': 'fuller_form_of_name',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relator_code',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'e': 'relator_term',
        '7': 'control_subfield',
        'a': 'personal_name',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        '3': 'materials_specified',
        'k': 'form_subheading',
        '6': 'linkage',
        'v': 'volume_sequential_designation',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        't': 'title_of_a_work',
        'x': 'international_standard_serial_number',
        'o': 'arranged_statement_for_music',
        'w': 'bibliographic_record_control_number',
        'u': 'affiliation',
        's': 'version',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'key_for_music': value.get('r'),
        'dates_associated_with_a_name': value.get('d'),
        'numeration': value.get('b'),
        'date_of_a_work': value.get('f'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'fuller_form_of_name': value.get('q'),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'control_subfield': value.get('7'),
        'personal_name': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'volume_sequential_designation': value.get('v'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'arranged_statement_for_music': value.get('o'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_added_entry_corporate_name', '^810..')
@utils.for_each_value
@utils.filter_values
def series_added_entry_corporate_name(self, key, value):
    """Series Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'r': 'key_for_music',
        'd': 'date_of_meeting_or_treaty_signing',
        'b': 'subordinate_unit',
        'f': 'date_of_a_work',
        'o': 'arranged_statement_for_music',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relator_code',
        'h': 'medium',
        'n': 'number_of_part_section_meeting',
        'e': 'relator_term',
        '7': 'control_subfield',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        '3': 'materials_specified',
        'k': 'form_subheading',
        '6': 'linkage',
        'v': 'volume_sequential_designation',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        't': 'title_of_a_work',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'u': 'affiliation',
        's': 'version',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'key_for_music': value.get('r'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'date_of_a_work': value.get('f'),
        'arranged_statement_for_music': value.get('o'),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'medium': value.get('h'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'control_subfield': value.get('7'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'volume_sequential_designation': value.get('v'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_added_entry_meeting_name', '^811..')
@utils.for_each_value
@utils.filter_values
def series_added_entry_meeting_name(self, key, value):
    """Series Added Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'd': 'date_of_meeting',
        'f': 'date_of_a_work',
        'j': 'relator_term',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relator_code',
        'h': 'medium',
        'n': 'number_of_part_section_meeting',
        'e': 'subordinate_unit',
        '7': 'control_subfield',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'g': 'miscellaneous_information',
        '3': 'materials_specified',
        'k': 'form_subheading',
        '6': 'linkage',
        'v': 'volume_sequential_designation',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        't': 'title_of_a_work',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'u': 'affiliation',
        's': 'version',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'date_of_meeting': value.get('d'),
        'date_of_a_work': value.get('f'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'medium': value.get('h'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'control_subfield': value.get('7'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'volume_sequential_designation': value.get('v'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_added_entry_uniform_title', '^830..')
@utils.for_each_value
@utils.filter_values
def series_added_entry_uniform_title(self, key, value):
    """Series Added Entry-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'r': 'key_for_music',
        '7': 'control_subfield',
        'f': 'date_of_a_work',
        'o': 'arranged_statement_for_music',
        'l': 'language_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'd': 'date_of_treaty_signing',
        'a': 'uniform_title',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        '6': 'linkage',
        'k': 'form_subheading',
        '3': 'materials_specified',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        't': 'title_of_a_work',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'v': 'volume_sequential_designation',
        's': 'version',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'key_for_music': value.get('r'),
        'control_subfield': value.get('7'),
        'date_of_a_work': value.get('f'),
        'arranged_statement_for_music': value.get('o'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'uniform_title': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'volume_sequential_designation': value.get('v'),
        'version': value.get('s'),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
