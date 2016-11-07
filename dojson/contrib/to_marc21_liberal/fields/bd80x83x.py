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


@to_marc21_liberal.over('800', '^series_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_personal_name(self, key, value):
    """Reverse - Series Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'fuller_form_of_name': 'q',
        'personal_name': 'a',
        'volume_sequential_designation': 'v',
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'affiliation': 'u',
        'number_of_part_section_of_a_work': 'n',
        'control_subfield': '7',
        'institution_to_which_field_applies': '5',
        'form_subheading': 'k',
        'international_standard_serial_number': 'x',
        'dates_associated_with_a_name': 'd',
        'medium_of_performance_for_music': 'm',
        'attribution_qualifier': 'j',
        'relator_term': 'e',
        'numeration': 'b',
        'materials_specified': '3',
        'relator_code': '4',
        'titles_and_other_words_associated_with_a_name': 'c',
        'bibliographic_record_control_number': 'w',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
        'version': 's',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'q': value.get('fuller_form_of_name'),
        'a': value.get('personal_name'),
        'v': value.get('volume_sequential_designation'),
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '7': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': value.get('international_standard_serial_number'),
        'd': value.get('dates_associated_with_a_name'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'b': value.get('numeration'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('810', '^series_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_corporate_name(self, key, value):
    """Reverse - Series Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'affiliation': 'u',
        'volume_sequential_designation': 'v',
        'control_subfield': '7',
        'institution_to_which_field_applies': '5',
        'form_subheading': 'k',
        'international_standard_serial_number': 'x',
        'date_of_meeting_or_treaty_signing': 'd',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_meeting': 'n',
        'relator_term': 'e',
        'subordinate_unit': 'b',
        'materials_specified': '3',
        'relator_code': '4',
        'location_of_meeting': 'c',
        'bibliographic_record_control_number': 'w',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
        'version': 's',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        'v': value.get('volume_sequential_designation'),
        '7': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': value.get('international_standard_serial_number'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('811', '^series_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_meeting_name(self, key, value):
    """Reverse - Series Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'volume_sequential_designation': 'v',
        'date_of_meeting': 'd',
        'affiliation': 'u',
        'number_of_part_section_meeting': 'n',
        'control_subfield': '7',
        'institution_to_which_field_applies': '5',
        'form_subheading': 'k',
        'international_standard_serial_number': 'x',
        'relator_term': 'j',
        'subordinate_unit': 'e',
        'materials_specified': '3',
        'relator_code': '4',
        'location_of_meeting': 'c',
        'bibliographic_record_control_number': 'w',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
        'version': 's',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'v': value.get('volume_sequential_designation'),
        'd': value.get('date_of_meeting'),
        'u': value.get('affiliation'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '7': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': value.get('international_standard_serial_number'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('830', '^series_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_uniform_title(self, key, value):
    """Reverse - Series Added Entry-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'uniform_title': 'a',
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'volume_sequential_designation': 'v',
        'control_subfield': '7',
        'date_of_a_work': 'f',
        'form_subheading': 'k',
        'international_standard_serial_number': 'x',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'materials_specified': '3',
        'date_of_treaty_signing': 'd',
        'bibliographic_record_control_number': 'w',
        'title_of_a_work': 't',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'a': value.get('uniform_title'),
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'v': value.get('volume_sequential_designation'),
        '7': value.get('control_subfield'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '3': value.get('materials_specified'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        't': value.get('title_of_a_work'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        'h': value.get('medium'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
