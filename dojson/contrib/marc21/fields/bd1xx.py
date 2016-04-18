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


@marc21.over('main_entry_personal_name', '^100[013_]_')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    """Main Entry-Personal Name."""
    indicator_map1 = {
        '0': 'Forename',
        '1': 'Surname',
        '3': 'Family name',
    }

    field_map = {
        'a': 'personal_name',
        'b': 'numeration',
        'c': 'titles_and_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'j': 'attribution_qualifier',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'q': 'fuller_form_of_name',
        't': 'title_of_a_work',
        'u': 'affiliation',
        '0': 'authority_record_control_number_or_standard_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_name': value.get('a'),
        'titles_and_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'fuller_form_of_name': value.get('q'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_corporate_name', '^110[10_2].')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    """Main Entry-Corporate Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    field_map = {
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'b': 'subordinate_unit',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting_or_treaty_signing',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'u': 'affiliation',
        '0': 'authority_record_control_number_or_standard_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_meeting_name', '^111[10_2].')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    """Main Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    }

    field_map = {
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'j': 'relator_term',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        't': 'title_of_a_work',
        'u': 'affiliation',
        '0': 'authority_record_control_number_or_standard_number',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_uniform_title', '^130[_0-9]_')
@utils.for_each_value
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    """Main Entry-Uniform Title."""
    nonfiling_characters = [str(x) for x in range(10)]

    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': utils.int_with_default(key[3], None),
    }
