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


@marc21.over('series_added_entry_personal_name', '^800[_103]_')
@utils.for_each_value
@utils.filter_values
def series_added_entry_personal_name(self, key, value):
    """Series Added Entry-Personal Name."""
    indicator_map1 = {
        '0': 'Forename',
        '1': 'Surname',
        '3': 'Family name',
    }

    field_map = {
        'a': 'personal_name',
        'b': 'numeration',
        'c': 'titles_and_other_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'j': 'attribution_qualifier',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'q': 'fuller_form_of_name',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'w': 'bibliographic_record_control_number',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(value.get('c')),
        'numeration': value.get('b'),
        'dates_associated_with_a_name': value.get('d'),
        'relator_term': utils.force_list(value.get('e')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'attribution_qualifier': utils.force_list(value.get('j')),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(value.get('m')),
        'number_of_part_section_of_a_work': utils.force_list(value.get('n')),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'fuller_form_of_name': value.get('q'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'bibliographic_record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(value.get('0')),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': utils.force_list(value.get('5')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_corporate_name', '^810[_0-2]_')
@utils.for_each_value
@utils.filter_values
def series_added_entry_corporate_name(self, key, value):
    """Series Added Entry-Corporate Name."""
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
        'h': 'medium',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_meeting',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'w': 'bibliographic_record_control_number',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(value.get('b')),
        'location_of_meeting': value.get('c'),
        'date_of_meeting_or_treaty_signing': utils.force_list(value.get('d')),
        'relator_term': utils.force_list(value.get('e')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(value.get('m')),
        'number_of_part_section_meeting': utils.force_list(value.get('n')),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'bibliographic_record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(value.get('0')),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': utils.force_list(value.get('5')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_meeting_name', '^811[_0-2]_')
@utils.for_each_value
@utils.filter_values
def series_added_entry_meeting_name(self, key, value):
    """Series Added Entry-Meeting Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    field_map = {
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'j': 'relator_term',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'v': 'volume_sequential_designation',
        'w': 'bibliographic_record_control_number',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'date_of_meeting': value.get('d'),
        'subordinate_unit': utils.force_list(value.get('e')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'relator_term': utils.force_list(value.get('j')),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(value.get('n')),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'volume_sequential_designation': value.get('v'),
        'bibliographic_record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(value.get('0')),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': utils.force_list(value.get('5')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('series_added_entry_uniform_title', '^830_[_0-9]')
@utils.for_each_value
@utils.filter_values
def series_added_entry_uniform_title(self, key, value):
    """Series Added Entry-Uniform Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

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
        'v': 'volume_sequential_designation',
        'w': 'bibliographic_record_control_number',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(value.get('d')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(value.get('m')),
        'number_of_part_section_of_a_work': utils.force_list(value.get('n')),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'volume_sequential_designation': value.get('v'),
        'bibliographic_record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(value.get('0')),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': utils.force_list(value.get('5')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }
