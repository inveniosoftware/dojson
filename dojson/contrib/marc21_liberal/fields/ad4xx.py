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

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('see_from_tracing_personal_name', '^400..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_personal_name(self, key, value):
    """See From Tracing-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'q': 'fuller_form_of_name',
        '8': 'field_link_and_sequence_number',
        'b': 'numeration',
        'a': 'personal_name',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        'n': 'number_of_part_section_of_a_work',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        's': 'version',
        'k': 'form_subheading',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'j': 'attribution_qualifier',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'x': 'general_subdivision',
        'r': 'key_for_music',
        'd': 'dates_associated_with_a_name',
        'w': 'control_subfield',
        'i': 'relationship_information',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'm': 'medium_of_performance_for_music',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'fuller_form_of_name': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'numeration': value.get('b'),
        'personal_name': value.get('a'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'version': value.get('s'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'key_for_music': value.get('r'),
        'dates_associated_with_a_name': value.get('d'),
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'type_of_personal_name_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_corporate_name', '^410..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_corporate_name(self, key, value):
    """See From Tracing-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'subordinate_unit',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        'n': 'number_of_part_section_meeting',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'd': 'date_of_meeting_or_treaty_signing',
        'k': 'form_subheading',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'r': 'key_for_music',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'x': 'general_subdivision',
        's': 'version',
        'w': 'control_subfield',
        'i': 'relationship_information',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'm': 'medium_of_performance_for_music',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'version': value.get('s'),
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_meeting_name', '^411..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_meeting_name(self, key, value):
    """See From Tracing-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        '8': 'field_link_and_sequence_number',
        't': 'title_of_a_work',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'y': 'chronological_subdivision',
        'n': 'number_of_part_section_meeting',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'd': 'date_of_meeting',
        'k': 'form_subheading',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'j': 'relator_term',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'x': 'general_subdivision',
        's': 'version',
        'w': 'control_subfield',
        'i': 'relationship_information',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'date_of_meeting': value.get('d'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'version': value.get('s'),
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_uniform_title', '^430..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_uniform_title(self, key, value):
    """See From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '8': 'field_link_and_sequence_number',
        't': 'title_of_a_work',
        'a': 'uniform_title',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        'n': 'number_of_part_section_of_a_work',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'd': 'date_of_treaty_signing',
        'k': 'form_subheading',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'f': 'date_of_a_work',
        'r': 'key_for_music',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'x': 'general_subdivision',
        's': 'version',
        'w': 'control_subfield',
        'i': 'relationship_information',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'uniform_title': value.get('a'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'date_of_a_work': value.get('f'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'version': value.get('s'),
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_chronological_term', '^448..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_term(self, key, value):
    """See From Tracing-Chronological Term."""
    field_map = {
        'w': 'control_subfield',
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'a': 'chronological_term',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_topical_term', '^450..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_topical_term(self, key, value):
    """See From Tracing-Topical Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'topical_term_following_geographic_name_entry_element',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'a': 'topical_term_or_geographic_name_entry_element',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_geographic_name', '^451..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_name(self, key, value):
    """See From Tracing-Geographic Name."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'a': 'geographic_name',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'geographic_name': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_genre_form_term', '^455..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_genre_form_term(self, key, value):
    """See From Tracing-Genre/Form Term."""
    field_map = {
        'w': 'control_subfield',
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'a': 'genre_form_term',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'genre_form_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_medium_of_performance_term', '^462..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_medium_of_performance_term(self, key, value):
    """See From Tracing-Medium of Performance Term."""
    field_map = {
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'i': 'relationship_information',
        'a': 'medium_of_performance_term',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium_of_performance_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_general_subdivision', '^480..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_general_subdivision(self, key, value):
    """See From Tracing-General Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_geographic_subdivision', '^481..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_subdivision(self, key, value):
    """See From Tracing-Geographic Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_chronological_subdivision', '^482..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_subdivision(self, key, value):
    """See From Tracing-Chronological Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_from_tracing_form_subdivision', '^485..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_form_subdivision(self, key, value):
    """See From Tracing-Form Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
