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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('400', '^series_statement_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_personal_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'numeration': 'b',
        'field_link_and_sequence_number': '8',
        'dates_associated_with_a_name': 'd',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'titles_and_other_words_associated_with_a_name': 'c',
        'form_subheading': 'k',
        'affiliation': 'u',
        'name_of_part_section_of_a_work': 'p',
        'volume_sequential_designation': 'v',
        'relator_term': 'e',
        'number_of_part_section_of_a_work': 'n',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'personal_name': 'a',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'pronoun_represents_main_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('numeration'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'x': value.get('international_standard_serial_number'),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'u': value.get('affiliation'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': value.get('volume_sequential_designation'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('personal_name'),
        'g': value.get('miscellaneous_information'),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), value.get('pronoun_represents_main_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('410', '^series_statement_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_corporate_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'subordinate_unit': 'b',
        'field_link_and_sequence_number': '8',
        'date_of_meeting_or_treaty_signing': 'd',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'location_of_meeting': 'c',
        'form_subheading': 'k',
        'affiliation': 'u',
        'name_of_part_section_of_a_work': 'p',
        'volume_sequential_designation': 'v',
        'relator_term': 'e',
        'number_of_part_section_meeting': 'n',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'pronoun_represents_main_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'x': value.get('international_standard_serial_number'),
        '6': value.get('linkage'),
        'c': value.get('location_of_meeting'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'u': value.get('affiliation'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': value.get('volume_sequential_designation'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'g': value.get('miscellaneous_information'),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), value.get('pronoun_represents_main_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('411', '^series_statement_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_meeting_name(self, key, value):
    """Reverse - Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'date_of_meeting': 'd',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'location_of_meeting': 'c',
        'form_subheading': 'k',
        'affiliation': 'u',
        'volume_sequential_designation': 'v',
        'subordinate_unit': 'e',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'number_of_part_section_meeting': 'n',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'pronoun_represents_main_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('date_of_meeting'),
        'x': value.get('international_standard_serial_number'),
        '6': value.get('linkage'),
        'c': value.get('location_of_meeting'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'u': value.get('affiliation'),
        'v': value.get('volume_sequential_designation'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'g': value.get('miscellaneous_information'),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry'), value.get('pronoun_represents_main_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('440', '^series_statement_added_entry_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_title(self, key, value):
    """Reverse - Series Statement/Added Entry-Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'bibliographic_record_control_number': 'w',
        'volume_sequential_designation': 'v',
        'field_link_and_sequence_number': '8',
        'international_standard_serial_number': 'x',
        'number_of_part_section_of_a_work': 'n',
        'linkage': '6',
        'authority_record_control_number': '0',
        'name_of_part_section_of_a_work': 'p',
        'title': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'v': value.get('volume_sequential_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'a': value.get('title'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('490', '^series_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement(self, key, value):
    """Reverse - Series Statement."""
    indicator_map1 = {"Series not traced": "0", "Series traced": "1"}
    field_map = {
        'volume_sequential_designation': 'v',
        'field_link_and_sequence_number': '8',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'library_of_congress_call_number': 'l',
        'materials_specified': '3',
        'series_statement': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['series_tracing_policy', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('volume_sequential_designation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        '6': value.get('linkage'),
        'l': value.get('library_of_congress_call_number'),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('series_statement')
        ),
        '$ind1': indicator_map1.get(value.get('series_tracing_policy'), value.get('series_tracing_policy', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
