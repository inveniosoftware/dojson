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
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'linkage': '6',
        'form_subheading': 'k',
        'relator_code': '4',
        'numeration': 'b',
        'personal_name': 'a',
        'international_standard_serial_number': 'x',
        'dates_associated_with_a_name': 'd',
        'affiliation': 'u',
        'title_of_a_work': 't',
        'name_of_part_section_of_a_work': 'p',
        'miscellaneous_information': 'g',
        'relator_term': 'e',
        'titles_and_other_words_associated_with_a_name': 'c',
        'date_of_a_work': 'f',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'number_of_part_section_of_a_work': 'n',
        'volume_sequential_designation': 'v',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'b': value.get('numeration'),
        'a': value.get('personal_name'),
        'x': value.get('international_standard_serial_number'),
        'd': value.get('dates_associated_with_a_name'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'g': value.get('miscellaneous_information'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'f': value.get('date_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'v': value.get('volume_sequential_designation'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), '_'),
    }


@to_marc21.over('410', '^series_statement_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_corporate_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'linkage': '6',
        'form_subheading': 'k',
        'relator_code': '4',
        'subordinate_unit': 'b',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'international_standard_serial_number': 'x',
        'date_of_meeting_or_treaty_signing': 'd',
        'affiliation': 'u',
        'title_of_a_work': 't',
        'name_of_part_section_of_a_work': 'p',
        'miscellaneous_information': 'g',
        'relator_term': 'e',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'volume_sequential_designation': 'v',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'x': value.get('international_standard_serial_number'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'g': value.get('miscellaneous_information'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'c': value.get('location_of_meeting'),
        'f': value.get('date_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'v': value.get('volume_sequential_designation'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), '_'),
    }


@to_marc21.over('411', '^series_statement_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_meeting_name(self, key, value):
    """Reverse - Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'linkage': '6',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'form_subheading': 'k',
        'relator_code': '4',
        'volume_sequential_designation': 'v',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_meeting': 'd',
        'affiliation': 'u',
        'title_of_a_work': 't',
        'name_of_part_section_of_a_work': 'p',
        'miscellaneous_information': 'g',
        'subordinate_unit': 'e',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'international_standard_serial_number': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': value.get('volume_sequential_designation'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'd': value.get('date_of_meeting'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'g': value.get('miscellaneous_information'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'c': value.get('location_of_meeting'),
        'f': value.get('date_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'x': value.get('international_standard_serial_number'),
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
        'bibliographic_record_control_number': 'w',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'volume_sequential_designation': 'v',
        'title': 'a',
        'authority_record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'international_standard_serial_number': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': value.get('volume_sequential_designation'),
        'a': value.get('title'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'x': value.get('international_standard_serial_number'),
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
        'linkage': '6',
        'volume_sequential_designation': 'v',
        'series_statement': 'a',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'library_of_congress_call_number': 'l',
        'international_standard_serial_number': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('volume_sequential_designation')
        ),
        'a': utils.reverse_force_list(
            value.get('series_statement')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('library_of_congress_call_number'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        '$ind1': indicator_map1.get(value.get('series_tracing_policy'), '_'),
        '$ind2': '_',
    }
