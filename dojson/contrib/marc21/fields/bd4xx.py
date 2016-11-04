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

from ..model import marc21


@marc21.over('series_statement_added_entry_personal_name', '^400[03_1][0_1]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    """Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {
        "0": "Main entry not represented by pronoun",
        "1": "Main entry represented by pronoun"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        '6': 'linkage',
        'u': 'affiliation',
        'b': 'numeration',
        '4': 'relator_code',
        'x': 'international_standard_serial_number',
        'n': 'number_of_part_section_of_a_work',
        'a': 'personal_name',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        't': 'title_of_a_work',
        'e': 'relator_term',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'g': 'miscellaneous_information',
        'f': 'date_of_a_work',
        'd': 'dates_associated_with_a_name',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'affiliation': value.get('u'),
        'numeration': value.get('b'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'international_standard_serial_number': value.get('x'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'personal_name': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'title_of_a_work': value.get('t'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'dates_associated_with_a_name': value.get('d'),
        'volume_sequential_designation': value.get('v'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_corporate_name', '^410[0_21][0_1]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    """Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Main entry not represented by pronoun",
        "1": "Main entry represented by pronoun"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        '6': 'linkage',
        'u': 'affiliation',
        'b': 'subordinate_unit',
        '4': 'relator_code',
        'x': 'international_standard_serial_number',
        'n': 'number_of_part_section_meeting',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        't': 'title_of_a_work',
        'e': 'relator_term',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'g': 'miscellaneous_information',
        'f': 'date_of_a_work',
        'd': 'date_of_meeting_or_treaty_signing',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'affiliation': value.get('u'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'international_standard_serial_number': value.get('x'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'title_of_a_work': value.get('t'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': value.get('c'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'volume_sequential_designation': value.get('v'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_meeting_name', '^411[0_21][0_1]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    """Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Main entry not represented by pronoun",
        "1": "Main entry represented by pronoun"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        '6': 'linkage',
        'u': 'affiliation',
        '4': 'relator_code',
        'd': 'date_of_meeting',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'n': 'number_of_part_section_meeting',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        't': 'title_of_a_work',
        'e': 'subordinate_unit',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'g': 'miscellaneous_information',
        'f': 'date_of_a_work',
        'x': 'international_standard_serial_number',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'date_of_meeting': value.get('d'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'title_of_a_work': value.get('t'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': value.get('c'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'international_standard_serial_number': value.get('x'),
        'volume_sequential_designation': value.get('v'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_title', '^440.[06413278_95]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    """Series Statement/Added Entry-Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'n': 'number_of_part_section_of_a_work',
        'a': 'title',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'title': value.get('a'),
        'volume_sequential_designation': value.get('v'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement', '^490[0_1].')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    """Series Statement."""
    indicator_map1 = {"0": "Series not traced", "1": "Series traced"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'l': 'library_of_congress_call_number',
        'x': 'international_standard_serial_number',
        '3': 'materials_specified',
        'a': 'series_statement',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('series_tracing_policy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'library_of_congress_call_number': value.get('l'),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'materials_specified': value.get('3'),
        'series_statement': utils.force_list(
            value.get('a')
        ),
        'volume_sequential_designation': utils.force_list(
            value.get('v')
        ),
        'series_tracing_policy': indicator_map1.get(key[3]),
    }
