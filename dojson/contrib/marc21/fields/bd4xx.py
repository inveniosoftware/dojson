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


@marc21.over('series_statement_added_entry_personal_name', '^400[_013][_01]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    """Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {
        '0': 'Forename',
        '1': 'Surname',
        '3': 'Family name',
    }
    indicator_map2 = {
        '0': 'Main entry not represented by pronoun',
        '1': 'Main entry represented by pronoun',
    }

    field_map = {
        'a': 'personal_name',
        'b': 'numeration',
        'c': 'titles_and_other_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_name': value.get('a'),
        'numeration': value.get('b'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_corporate_name', '^410[_012][_01]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    """Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '0': 'Main entry not represented by pronoun',
        '1': 'Main entry represented by pronoun',
    }

    field_map = {
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'b': 'subordinate_unit',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting_or_treaty_signing',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')
    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'location_of_meeting': value.get('c'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_meeting_name', '^411[_012][_01]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    """Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '0': 'Main entry not represented by pronoun',
        '1': 'Main entry represented by pronoun',
    }

    field_map = {
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')
    if key[4] in indicator_map2:
        order.append('pronoun_represents_main_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'date_of_meeting': value.get('d'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@marc21.over('series_statement_added_entry_title', '^440_[_0-9]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    """Series Statement/Added Entry-Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    field_map = {
        'a': 'title',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'v': 'volume_sequential_designation',
        'w': 'bibliographic_record_control_number',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'volume_sequential_designation': value.get('v'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over('series_statement', '^490[01_]_')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    """Series Statement."""
    indicator_map1 = {
        '0': 'Series not traced',
        '1': 'Series traced',
    }

    field_map = {
        'a': 'series_statement',
        'l': 'library_of_congress_call_number',
        'v': 'volume_sequential_designation',
        'x': 'international_standard_serial_number',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('series_tracing_policy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'series_statement': utils.force_list(
            value.get('a')
        ),
        'library_of_congress_call_number': value.get('l'),
        'volume_sequential_designation': utils.force_list(
            value.get('v')
        ),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'series_tracing_policy': indicator_map1.get(key[3]),
    }
