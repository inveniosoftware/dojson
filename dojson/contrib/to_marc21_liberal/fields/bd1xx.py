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
from dojson.contrib.marc21_liberal.utils import liberal_map_order

from ..model import to_marc21_liberal


@to_marc21_liberal.over('100', '^main_entry_personal_name$')
@utils.filter_values
def reverse_main_entry_personal_name(self, key, value):
    """Reverse - Main Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}

    field_map = {
        'personal_name': 'a',
        'numeration': 'b',
        'titles_and_words_associated_with_a_name': 'c',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'fuller_form_of_name': 'q',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_personal_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('personal_name'),
        'b': value.get('numeration'),
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'b',
        'location_of_meeting': 'c',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'location_of_meeting': 'c',
        'date_of_meeting': 'd',
        'subordinate_unit': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'relator_term': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'd': value.get('date_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['nonfiling_characters', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
