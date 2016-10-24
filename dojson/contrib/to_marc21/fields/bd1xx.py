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
        'fuller_form_of_name': 'q',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'dates_associated_with_a_name': 'd',
        'number_of_part_section_of_a_work': 'n',
        'language_of_a_work': 'l',
        'linkage': '6',
        'titles_and_words_associated_with_a_name': 'c',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'relator_term': 'e',
        'attribution_qualifier': 'j',
        'numeration': 'b',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'personal_name': 'a',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_personal_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_personal_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('fuller_form_of_name'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'b': value.get('numeration'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('personal_name'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('110', '^main_entry_corporate_name$')
@utils.filter_values
def reverse_main_entry_corporate_name(self, key, value):
    """Reverse - Main Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'date_of_meeting_or_treaty_signing': 'd',
        'number_of_part_section_meeting': 'n',
        'language_of_a_work': 'l',
        'linkage': '6',
        'location_of_meeting': 'c',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'relator_term': 'e',
        'form_subheading': 'k',
        'subordinate_unit': 'b',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'affiliation': 'u',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_corporate_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_corporate_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'l': value.get('language_of_a_work'),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'u': value.get('affiliation'),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('111', '^main_entry_meeting_name$')
@utils.filter_values
def reverse_main_entry_meeting_name(self, key, value):
    """Reverse - Main Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    field_map = {
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'affiliation': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'date_of_meeting': 'd',
        'number_of_part_section_meeting': 'n',
        'language_of_a_work': 'l',
        'linkage': '6',
        'location_of_meeting': 'c',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'subordinate_unit': 'e',
        'relator_term': 'j',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_meeting_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_meeting_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'u': value.get('affiliation'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'd': value.get('date_of_meeting'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'l': value.get('language_of_a_work'),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('130', '^main_entry_uniform_title$')
@utils.filter_values
def reverse_main_entry_uniform_title(self, key, value):
    """Reverse - Main Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'version': 's',
        'medium_of_performance_for_music': 'm',
        'form_subheading': 'k',
        'number_of_part_section_of_a_work': 'n',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'title_of_a_work': 't',
        'key_for_music': 'r',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'date_of_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
        'linkage': '6',
        'uniform_title': 'a',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        's': value.get('version'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        '6': value.get('linkage'),
        'a': value.get('uniform_title'),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': '_',
    }
