# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21


@marc21.over('main_entry_personal_name', '^100[0_31].')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    """Main Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'k': 'form_subheading',
        'u': 'affiliation',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'c': 'titles_and_words_associated_with_a_name',
        'e': 'relator_term',
        '6': 'linkage',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'j': 'attribution_qualifier',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'a': 'personal_name',
        'l': 'language_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'd': 'dates_associated_with_a_name',
        'b': 'numeration',
        'q': 'fuller_form_of_name',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'affiliation': value.get('u'),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'titles_and_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'linkage': value.get('6'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'personal_name': value.get('a'),
        'language_of_a_work': value.get('l'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'numeration': value.get('b'),
        'fuller_form_of_name': value.get('q'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_corporate_name', '^110[0_21].')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    """Main Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    field_map = {
        'k': 'form_subheading',
        'u': 'affiliation',
        'f': 'date_of_a_work',
        'c': 'location_of_meeting',
        'e': 'relator_term',
        '6': 'linkage',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'n': 'number_of_part_section_meeting',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'd': 'date_of_meeting_or_treaty_signing',
        'b': 'subordinate_unit',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'affiliation': value.get('u'),
        'date_of_a_work': value.get('f'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'linkage': value.get('6'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_meeting_name', '^111[0_21].')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    """Main Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    field_map = {
        'k': 'form_subheading',
        'u': 'affiliation',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_meeting',
        'c': 'location_of_meeting',
        'e': 'subordinate_unit',
        '6': 'linkage',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'j': 'relator_term',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'd': 'date_of_meeting',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'affiliation': value.get('u'),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'linkage': value.get('6'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'date_of_meeting': value.get('d'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_uniform_title', '^130[096348725_1].')
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    """Main Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    field_map = {
        'k': 'form_subheading',
        'f': 'date_of_a_work',
        's': 'version',
        '6': 'linkage',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'h': 'medium',
        'a': 'uniform_title',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'd': 'date_of_treaty_signing',
        'r': 'key_for_music',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'linkage': value.get('6'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium': value.get('h'),
        'uniform_title': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'key_for_music': value.get('r'),
        'nonfiling_characters': indicator_map1.get(key[3]),
    }
