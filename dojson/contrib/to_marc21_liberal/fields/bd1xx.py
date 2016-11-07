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
        'titles_and_words_associated_with_a_name': 'c',
        'relator_term': 'e',
        'form_subheading': 'k',
        'dates_associated_with_a_name': 'd',
        'linkage': '6',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'numeration': 'b',
        'relator_code': '4',
        'attribution_qualifier': 'j',
        'fuller_form_of_name': 'q',
        'number_of_part_section_of_a_work': 'n',
        'personal_name': 'a',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'd': value.get('dates_associated_with_a_name'),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('numeration'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'q': value.get('fuller_form_of_name'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('personal_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
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
        'location_of_meeting': 'c',
        'relator_term': 'e',
        'form_subheading': 'k',
        'date_of_meeting_or_treaty_signing': 'd',
        'linkage': '6',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'subordinate_unit': 'b',
        'relator_code': '4',
        'number_of_part_section_meeting': 'n',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
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
        'location_of_meeting': 'c',
        'subordinate_unit': 'e',
        'form_subheading': 'k',
        'date_of_meeting': 'd',
        'linkage': '6',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'relator_code': '4',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'number_of_part_section_meeting': 'n',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'relator_term': 'j',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'd': value.get('date_of_meeting'),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
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
        'date_of_treaty_signing': 'd',
        'miscellaneous_information': 'g',
        'form_subheading': 'k',
        'title_of_a_work': 't',
        'key_for_music': 'r',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'date_of_a_work': 'f',
        'uniform_title': 'a',
        'version': 's',
        'language_of_a_work': 'l',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'medium_of_performance_for_music': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'f': value.get('date_of_a_work'),
        'a': value.get('uniform_title'),
        's': value.get('version'),
        'l': value.get('language_of_a_work'),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
