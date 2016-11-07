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


@marc21_liberal.over('series_statement_added_entry_personal_name', '^400..')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    """Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    field_map = {
        'k': 'form_subheading',
        'n': 'number_of_part_section_of_a_work',
        '8': 'field_link_and_sequence_number',
        'v': 'volume_sequential_designation',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'u': 'affiliation',
        'd': 'dates_associated_with_a_name',
        'a': 'personal_name',
        'e': 'relator_term',
        'l': 'language_of_a_work',
        'x': 'international_standard_serial_number',
        't': 'title_of_a_work',
        'f': 'date_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'b': 'numeration',
        'p': 'name_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('pronoun_represents_main_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volume_sequential_designation': value.get('v'),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': value.get('g'),
        'affiliation': value.get('u'),
        'dates_associated_with_a_name': value.get('d'),
        'personal_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'international_standard_serial_number': value.get('x'),
        'title_of_a_work': value.get('t'),
        'date_of_a_work': value.get('f'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_statement_added_entry_corporate_name', '^410..')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    """Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    field_map = {
        'k': 'form_subheading',
        'n': 'number_of_part_section_meeting',
        '8': 'field_link_and_sequence_number',
        'v': 'volume_sequential_designation',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'u': 'affiliation',
        'd': 'date_of_meeting_or_treaty_signing',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'e': 'relator_term',
        'l': 'language_of_a_work',
        'x': 'international_standard_serial_number',
        't': 'title_of_a_work',
        'f': 'date_of_a_work',
        'c': 'location_of_meeting',
        'b': 'subordinate_unit',
        'p': 'name_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('pronoun_represents_main_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volume_sequential_designation': value.get('v'),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': value.get('g'),
        'affiliation': value.get('u'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'international_standard_serial_number': value.get('x'),
        'title_of_a_work': value.get('t'),
        'date_of_a_work': value.get('f'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_statement_added_entry_meeting_name', '^411..')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    """Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    field_map = {
        'k': 'form_subheading',
        'n': 'number_of_part_section_meeting',
        '8': 'field_link_and_sequence_number',
        'v': 'volume_sequential_designation',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'u': 'affiliation',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'e': 'subordinate_unit',
        'l': 'language_of_a_work',
        'x': 'international_standard_serial_number',
        't': 'title_of_a_work',
        'f': 'date_of_a_work',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'p': 'name_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('pronoun_represents_main_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volume_sequential_designation': value.get('v'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': value.get('g'),
        'affiliation': value.get('u'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'international_standard_serial_number': value.get('x'),
        'title_of_a_work': value.get('t'),
        'date_of_a_work': value.get('f'),
        'location_of_meeting': value.get('c'),
        'date_of_meeting': value.get('d'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_statement_added_entry_title', '^440..')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    """Series Statement/Added Entry-Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'w': 'bibliographic_record_control_number',
        'n': 'number_of_part_section_of_a_work',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        'v': 'volume_sequential_designation',
        '6': 'linkage',
        'a': 'title',
        'x': 'international_standard_serial_number',
        'p': 'name_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'volume_sequential_designation': value.get('v'),
        'linkage': value.get('6'),
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('series_statement', '^490..')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    """Series Statement."""
    indicator_map1 = {"0": "Series not traced", "1": "Series traced"}
    field_map = {
        'x': 'international_standard_serial_number',
        'l': 'library_of_congress_call_number',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'v': 'volume_sequential_designation',
        '6': 'linkage',
        'a': 'series_statement',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('series_tracing_policy')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'library_of_congress_call_number': value.get('l'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'volume_sequential_designation': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'series_statement': utils.force_list(
            value.get('a')
        ),
        'series_tracing_policy': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
