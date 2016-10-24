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


@marc21.over('series_added_entry_personal_name', '^800[0_13].')
@utils.for_each_value
@utils.filter_values
def series_added_entry_personal_name(self, key, value):
    """Series Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'c': 'titles_and_other_words_associated_with_a_name',
        'a': 'personal_name',
        '5': 'institution_to_which_field_applies',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        'e': 'relator_term',
        '4': 'relator_code',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'h': 'medium',
        '7': 'control_subfield',
        'x': 'international_standard_serial_number',
        'b': 'numeration',
        'j': 'attribution_qualifier',
        'f': 'date_of_a_work',
        's': 'version',
        'd': 'dates_associated_with_a_name',
        'l': 'language_of_a_work',
        'q': 'fuller_form_of_name',
        '3': 'materials_specified',
        'u': 'affiliation',
        'o': 'arranged_statement_for_music',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_of_a_work',
        'g': 'miscellaneous_information',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'personal_name': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium': value.get('h'),
        'control_subfield': value.get('7'),
        'international_standard_serial_number': value.get('x'),
        'numeration': value.get('b'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'dates_associated_with_a_name': value.get('d'),
        'language_of_a_work': value.get('l'),
        'fuller_form_of_name': value.get('q'),
        'materials_specified': value.get('3'),
        'affiliation': value.get('u'),
        'arranged_statement_for_music': value.get('o'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'volume_sequential_designation': value.get('v'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_corporate_name', '^810[021_].')
@utils.for_each_value
@utils.filter_values
def series_added_entry_corporate_name(self, key, value):
    """Series Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    field_map = {
        'c': 'location_of_meeting',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        '5': 'institution_to_which_field_applies',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        'e': 'relator_term',
        '4': 'relator_code',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'h': 'medium',
        '7': 'control_subfield',
        'x': 'international_standard_serial_number',
        'b': 'subordinate_unit',
        'f': 'date_of_a_work',
        's': 'version',
        'd': 'date_of_meeting_or_treaty_signing',
        'l': 'language_of_a_work',
        'w': 'bibliographic_record_control_number',
        '3': 'materials_specified',
        'u': 'affiliation',
        'o': 'arranged_statement_for_music',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_meeting',
        'g': 'miscellaneous_information',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium': value.get('h'),
        'control_subfield': value.get('7'),
        'international_standard_serial_number': value.get('x'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'materials_specified': value.get('3'),
        'affiliation': value.get('u'),
        'arranged_statement_for_music': value.get('o'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'volume_sequential_designation': value.get('v'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_meeting_name', '^811[021_].')
@utils.for_each_value
@utils.filter_values
def series_added_entry_meeting_name(self, key, value):
    """Series Added Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    field_map = {
        'c': 'location_of_meeting',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '5': 'institution_to_which_field_applies',
        'k': 'form_subheading',
        'e': 'subordinate_unit',
        '4': 'relator_code',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'h': 'medium',
        '7': 'control_subfield',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'j': 'relator_term',
        'f': 'date_of_a_work',
        's': 'version',
        'd': 'date_of_meeting',
        'l': 'language_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        '3': 'materials_specified',
        'u': 'affiliation',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_meeting',
        'g': 'miscellaneous_information',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium': value.get('h'),
        'control_subfield': value.get('7'),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'date_of_meeting': value.get('d'),
        'language_of_a_work': value.get('l'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'materials_specified': value.get('3'),
        'affiliation': value.get('u'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'volume_sequential_designation': value.get('v'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_uniform_title', '^830.[2_579683041]')
@utils.for_each_value
@utils.filter_values
def series_added_entry_uniform_title(self, key, value):
    """Series Added Entry-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'uniform_title',
        '7': 'control_subfield',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        'x': 'international_standard_serial_number',
        'w': 'bibliographic_record_control_number',
        'f': 'date_of_a_work',
        's': 'version',
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_of_a_work',
        'g': 'miscellaneous_information',
        'v': 'volume_sequential_designation',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'control_subfield': value.get('7'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'international_standard_serial_number': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'volume_sequential_designation': value.get('v'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }
