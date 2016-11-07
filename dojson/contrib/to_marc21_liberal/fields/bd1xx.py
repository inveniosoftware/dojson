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


@to_marc21_liberal.over('100', '^main_entry_personal_name$')
@utils.filter_values
def reverse_main_entry_personal_name(self, key, value):
    """Reverse - Main Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'fuller_form_of_name': 'q',
        'titles_and_words_associated_with_a_name': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'number_of_part_section_of_a_work': 'n',
        'personal_name': 'a',
        'field_link_and_sequence_number': '8',
        'dates_associated_with_a_name': 'd',
        'numeration': 'b',
        'attribution_qualifier': 'j',
        'linkage': '6',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'q': value.get('fuller_form_of_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('personal_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'b': value.get('numeration'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('110', '^main_entry_corporate_name$')
@utils.filter_values
def reverse_main_entry_corporate_name(self, key, value):
    """Reverse - Main Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'location_of_meeting': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'number_of_part_section_meeting': 'n',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'field_link_and_sequence_number': '8',
        'date_of_meeting_or_treaty_signing': 'd',
        'subordinate_unit': 'b',
        'linkage': '6',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('111', '^main_entry_meeting_name$')
@utils.filter_values
def reverse_main_entry_meeting_name(self, key, value):
    """Reverse - Main Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'authority_record_control_number_or_standard_number': '0',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'number_of_part_section_meeting': 'n',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'field_link_and_sequence_number': '8',
        'date_of_meeting': 'd',
        'location_of_meeting': 'c',
        'relator_term': 'j',
        'linkage': '6',
        'subordinate_unit': 'e',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('date_of_meeting'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('130', '^main_entry_uniform_title$')
@utils.filter_values
def reverse_main_entry_uniform_title(self, key, value):
    """Reverse - Main Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    field_map = {
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_of_a_work': 'n',
        'title_of_a_work': 't',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'uniform_title': 'a',
        'key_for_music': 'r',
        'field_link_and_sequence_number': '8',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'arranged_statement_for_music': 'o',
        'linkage': '6',
        'name_of_part_section_of_a_work': 'p',
        'date_of_a_work': 'f',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'a': value.get('uniform_title'),
        'r': value.get('key_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'o': value.get('arranged_statement_for_music'),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
