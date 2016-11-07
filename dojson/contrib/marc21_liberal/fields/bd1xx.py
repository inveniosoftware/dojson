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

from ..model import marc21_liberal


@marc21_liberal.over('main_entry_personal_name', '^100..')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    """Main Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'd': 'dates_associated_with_a_name',
        'l': 'language_of_a_work',
        'e': 'relator_term',
        'g': 'miscellaneous_information',
        '6': 'linkage',
        'j': 'attribution_qualifier',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'a': 'personal_name',
        '0': 'authority_record_control_number_or_standard_number',
        'p': 'name_of_part_section_of_a_work',
        'q': 'fuller_form_of_name',
        '8': 'field_link_and_sequence_number',
        'c': 'titles_and_words_associated_with_a_name',
        't': 'title_of_a_work',
        'u': 'affiliation',
        '4': 'relator_code',
        'k': 'form_subheading',
        'b': 'numeration',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'dates_associated_with_a_name': value.get('d'),
        'language_of_a_work': value.get('l'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'personal_name': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'fuller_form_of_name': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'titles_and_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'numeration': value.get('b'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('main_entry_corporate_name', '^110..')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    """Main Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'd': 'date_of_meeting_or_treaty_signing',
        'l': 'language_of_a_work',
        'e': 'relator_term',
        'g': 'miscellaneous_information',
        '6': 'linkage',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_meeting',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        '0': 'authority_record_control_number_or_standard_number',
        'p': 'name_of_part_section_of_a_work',
        '8': 'field_link_and_sequence_number',
        'c': 'location_of_meeting',
        't': 'title_of_a_work',
        'u': 'affiliation',
        '4': 'relator_code',
        'k': 'form_subheading',
        'b': 'subordinate_unit',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('main_entry_meeting_name', '^111..')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    """Main Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'd': 'date_of_meeting',
        'l': 'language_of_a_work',
        'e': 'subordinate_unit',
        'g': 'miscellaneous_information',
        '6': 'linkage',
        'j': 'relator_term',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_meeting',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '0': 'authority_record_control_number_or_standard_number',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        '8': 'field_link_and_sequence_number',
        'c': 'location_of_meeting',
        't': 'title_of_a_work',
        '4': 'relator_code',
        'k': 'form_subheading',
        'u': 'affiliation',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_meeting': value.get('d'),
        'language_of_a_work': value.get('l'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'title_of_a_work': value.get('t'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'affiliation': value.get('u'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('main_entry_uniform_title', '^130..')
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    """Main Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    field_map = {
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        'g': 'miscellaneous_information',
        's': 'version',
        'o': 'arranged_statement_for_music',
        'r': 'key_for_music',
        'h': 'medium',
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'a': 'uniform_title',
        '0': 'authority_record_control_number_or_standard_number',
        'p': 'name_of_part_section_of_a_work',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        't': 'title_of_a_work',
        '6': 'linkage',
        'm': 'medium_of_performance_for_music',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('nonfiling_characters')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'version': value.get('s'),
        'arranged_statement_for_music': value.get('o'),
        'key_for_music': value.get('r'),
        'medium': value.get('h'),
        'date_of_a_work': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'nonfiling_characters': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
