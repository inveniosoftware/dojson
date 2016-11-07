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
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'volume_sequential_designation': 'v',
        'medium': 'h',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'medium_of_performance_for_music': 'm',
        'bibliographic_record_control_number': 'w',
        'key_for_music': 'r',
        'authority_record_control_number_or_standard_number': '0',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'control_subfield': '7',
        'date_of_a_work': 'f',
        'number_of_part_section_of_a_work': 'n',
        'affiliation': 'u',
        'relator_code': '4',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'personal_name': 'a',
        'fuller_form_of_name': 'q',
        'numeration': 'b',
        'attribution_qualifier': 'j',
        'version': 's',
        'dates_associated_with_a_name': 'd',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'linkage': '6',
        'form_subheading': 'k',
        'titles_and_other_words_associated_with_a_name': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        'h': value.get('medium'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'r': value.get('key_for_music'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '7': value.get('control_subfield'),
        'f': value.get('date_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('personal_name'),
        'q': value.get('fuller_form_of_name'),
        'b': value.get('numeration'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        's': value.get('version'),
        'd': value.get('dates_associated_with_a_name'),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
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
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'volume_sequential_designation': 'v',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'medium_of_performance_for_music': 'm',
        'bibliographic_record_control_number': 'w',
        'key_for_music': 'r',
        'authority_record_control_number_or_standard_number': '0',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'control_subfield': '7',
        'date_of_a_work': 'f',
        'number_of_part_section_meeting': 'n',
        'affiliation': 'u',
        'relator_code': '4',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'b',
        'medium': 'h',
        'version': 's',
        'date_of_meeting_or_treaty_signing': 'd',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'linkage': '6',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'r': value.get('key_for_music'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '7': value.get('control_subfield'),
        'f': value.get('date_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'h': value.get('medium'),
        's': value.get('version'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
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
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'volume_sequential_designation': 'v',
        'subordinate_unit': 'e',
        'medium': 'h',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'bibliographic_record_control_number': 'w',
        'authority_record_control_number_or_standard_number': '0',
        'control_subfield': '7',
        'miscellaneous_information': 'g',
        'date_of_meeting': 'd',
        'version': 's',
        'number_of_part_section_meeting': 'n',
        'affiliation': 'u',
        'relator_code': '4',
        'name_of_part_section_of_a_work': 'p',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'title_of_a_work': 't',
        'relator_term': 'j',
        'date_of_a_work': 'f',
        'materials_specified': '3',
        'linkage': '6',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'h': value.get('medium'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '7': value.get('control_subfield'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': value.get('date_of_meeting'),
        's': value.get('version'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        't': value.get('title_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
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
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'volume_sequential_designation': 'v',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'medium_of_performance_for_music': 'm',
        'bibliographic_record_control_number': 'w',
        'key_for_music': 'r',
        'authority_record_control_number_or_standard_number': '0',
        'number_of_part_section_of_a_work': 'n',
        'miscellaneous_information': 'g',
        'control_subfield': '7',
        'version': 's',
        'materials_specified': '3',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'uniform_title': 'a',
        'title_of_a_work': 't',
        'medium': 'h',
        'date_of_a_work': 'f',
        'linkage': '6',
        'form_subheading': 'k',
        'date_of_treaty_signing': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'r': value.get('key_for_music'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '7': value.get('control_subfield'),
        's': value.get('version'),
        '3': value.get('materials_specified'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('uniform_title'),
        't': value.get('title_of_a_work'),
        'h': value.get('medium'),
        'f': value.get('date_of_a_work'),
        '6': value.get('linkage'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
