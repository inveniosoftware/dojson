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


@to_marc21.over('100', '^main_entry_personal_name$')
@utils.filter_values
def reverse_main_entry_personal_name(self, key, value):
    """Reverse - Main Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'numeration': 'b',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'number_of_part_section_of_a_work': 'n',
        'titles_and_words_associated_with_a_name': 'c',
        'title_of_a_work': 't',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'fuller_form_of_name': 'q',
        'attribution_qualifier': 'j',
        'linkage': '6',
        'affiliation': 'u',
        'personal_name': 'a',
        'date_of_a_work': 'f',
        'dates_associated_with_a_name': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('numeration'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        't': value.get('title_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'q': value.get('fuller_form_of_name'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        'a': value.get('personal_name'),
        'f': value.get('date_of_a_work'),
        'd': value.get('dates_associated_with_a_name'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('110', '^main_entry_corporate_name$')
@utils.filter_values
def reverse_main_entry_corporate_name(self, key, value):
    """Reverse - Main Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'b',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'location_of_meeting': 'c',
        'title_of_a_work': 't',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'affiliation': 'u',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_a_work': 'f',
        'date_of_meeting_or_treaty_signing': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        't': value.get('title_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'f': value.get('date_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('111', '^main_entry_meeting_name$')
@utils.filter_values
def reverse_main_entry_meeting_name(self, key, value):
    """Reverse - Main Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'location_of_meeting': 'c',
        'title_of_a_work': 't',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'subordinate_unit': 'e',
        'miscellaneous_information': 'g',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'date_of_meeting': 'd',
        'linkage': '6',
        'affiliation': 'u',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_a_work': 'f',
        'relator_term': 'j',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        't': value.get('title_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'd': value.get('date_of_meeting'),
        '6': value.get('linkage'),
        'u': value.get('affiliation'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'f': value.get('date_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('130', '^main_entry_uniform_title$')
@utils.filter_values
def reverse_main_entry_uniform_title(self, key, value):
    """Reverse - Main Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    field_map = {
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'uniform_title': 'a',
        'language_of_a_work': 'l',
        'key_for_music': 'r',
        'number_of_part_section_of_a_work': 'n',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'title_of_a_work': 't',
        'arranged_statement_for_music': 'o',
        'version': 's',
        'date_of_treaty_signing': 'd',
        'medium_of_performance_for_music': 'm',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('uniform_title'),
        'l': value.get('language_of_a_work'),
        'r': value.get('key_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        's': value.get('version'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': '_',
    }
