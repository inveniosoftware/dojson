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

from ..model import to_marc21


@to_marc21.over('400', '^series_statement_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_personal_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {
        "Main entry not represented by pronoun": "0",
        "Main entry represented by pronoun": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'date_of_a_work': 'f',
        'numeration': 'b',
        'personal_name': 'a',
        'number_of_part_section_of_a_work': 'n',
        'affiliation': 'u',
        'titles_and_other_words_associated_with_a_name': 'c',
        'language_of_a_work': 'l',
        'international_standard_serial_number': 'x',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'relator_code': '4',
        'volume_sequential_designation': 'v',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_personal_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_personal_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('pronoun_represents_main_entry'), '7') != '7':
        try:
            order.remove(field_map.get('pronoun_represents_main_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'b': value.get('numeration'),
        'a': value.get('personal_name'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'u': value.get('affiliation'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'l': value.get('language_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'd': value.get('dates_associated_with_a_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': value.get('volume_sequential_designation'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': value.get('miscellaneous_information'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), '_'),
    }


@to_marc21.over('410', '^series_statement_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_corporate_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Main entry not represented by pronoun": "0",
        "Main entry represented by pronoun": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'date_of_a_work': 'f',
        'subordinate_unit': 'b',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'number_of_part_section_meeting': 'n',
        'affiliation': 'u',
        'location_of_meeting': 'c',
        'language_of_a_work': 'l',
        'international_standard_serial_number': 'x',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'relator_code': '4',
        'volume_sequential_designation': 'v',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_corporate_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_corporate_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('pronoun_represents_main_entry'), '7') != '7':
        try:
            order.remove(field_map.get('pronoun_represents_main_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'u': value.get('affiliation'),
        'c': value.get('location_of_meeting'),
        'l': value.get('language_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': value.get('volume_sequential_designation'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': value.get('miscellaneous_information'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), '_'),
    }


@to_marc21.over('411', '^series_statement_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_meeting_name(self, key, value):
    """Reverse - Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Main entry not represented by pronoun": "0",
        "Main entry represented by pronoun": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'linkage': '6',
        'date_of_a_work': 'f',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'number_of_part_section_meeting': 'n',
        'affiliation': 'u',
        'location_of_meeting': 'c',
        'international_standard_serial_number': 'x',
        'volume_sequential_designation': 'v',
        'date_of_meeting': 'd',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'relator_code': '4',
        'subordinate_unit': 'e',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_meeting_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_meeting_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('pronoun_represents_main_entry'), '7') != '7':
        try:
            order.remove(field_map.get('pronoun_represents_main_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'u': value.get('affiliation'),
        'c': value.get('location_of_meeting'),
        'x': value.get('international_standard_serial_number'),
        'v': value.get('volume_sequential_designation'),
        'd': value.get('date_of_meeting'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': value.get('miscellaneous_information'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), '_'),
    }


@to_marc21.over('440', '^series_statement_added_entry_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_title(self, key, value):
    """Reverse - Series Statement/Added Entry-Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'field_link_and_sequence_number': '8',
        'international_standard_serial_number': 'x',
        'bibliographic_record_control_number': 'w',
        'authority_record_control_number': '0',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'title': 'a',
        'volume_sequential_designation': 'v',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'a': value.get('title'),
        'v': value.get('volume_sequential_designation'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('490', '^series_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement(self, key, value):
    """Reverse - Series Statement."""
    indicator_map1 = {"Series not traced": "0", "Series traced": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'library_of_congress_call_number': 'l',
        'linkage': '6',
        'international_standard_serial_number': 'x',
        'series_statement': 'a',
        'volume_sequential_designation': 'v',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('series_tracing_policy'), '7') != '7':
        try:
            order.remove(field_map.get('series_tracing_policy'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('library_of_congress_call_number'),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        'a': utils.reverse_force_list(
            value.get('series_statement')
        ),
        'v': utils.reverse_force_list(
            value.get('volume_sequential_designation')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('series_tracing_policy'), '_'),
        '$ind2': '_',
    }
