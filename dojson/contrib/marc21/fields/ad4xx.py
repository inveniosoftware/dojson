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

from ..model import marc21_authority


@marc21_authority.over('see_from_tracing_personal_name', '^400[1_03].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_personal_name(self, key, value):
    """See From Tracing-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'q': 'fuller_form_of_name',
        'j': 'attribution_qualifier',
        '5': 'institution_to_which_field_applies',
        'h': 'medium',
        'c': 'titles_and_other_words_associated_with_a_name',
        't': 'title_of_a_work',
        'y': 'chronological_subdivision',
        'a': 'personal_name',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'w': 'control_subfield',
        'f': 'date_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relationship_code',
        'o': 'arranged_statement_for_music',
        'e': 'relator_term',
        'k': 'form_subheading',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        'b': 'numeration',
        '6': 'linkage',
        'd': 'dates_associated_with_a_name',
        'g': 'miscellaneous_information',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'fuller_form_of_name': value.get('q'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium': value.get('h'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'title_of_a_work': value.get('t'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'personal_name': value.get('a'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'control_subfield': value.get('w'),
        'date_of_a_work': value.get('f'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'arranged_statement_for_music': value.get('o'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'numeration': value.get('b'),
        'linkage': value.get('6'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'type_of_personal_name_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_from_tracing_corporate_name', '^410[21_0].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_corporate_name(self, key, value):
    """See From Tracing-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '5': 'institution_to_which_field_applies',
        'h': 'medium',
        'c': 'location_of_meeting',
        't': 'title_of_a_work',
        'y': 'chronological_subdivision',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        'o': 'arranged_statement_for_music',
        'n': 'number_of_part_section_meeting',
        'w': 'control_subfield',
        'k': 'form_subheading',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relationship_code',
        's': 'version',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        'b': 'subordinate_unit',
        '6': 'linkage',
        'd': 'date_of_meeting_or_treaty_signing',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium': value.get('h'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'title_of_a_work': value.get('t'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'control_subfield': value.get('w'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'version': value.get('s'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_from_tracing_meeting_name', '^411[21_0].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_meeting_name(self, key, value):
    """See From Tracing-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'i': 'relationship_information',
        'j': 'relator_term',
        '5': 'institution_to_which_field_applies',
        'h': 'medium',
        'c': 'location_of_meeting',
        'g': 'miscellaneous_information',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'n': 'number_of_part_section_meeting',
        'w': 'control_subfield',
        'f': 'date_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relationship_code',
        's': 'version',
        'e': 'subordinate_unit',
        'k': 'form_subheading',
        'x': 'general_subdivision',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '6': 'linkage',
        'd': 'date_of_meeting',
        'l': 'language_of_a_work',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium': value.get('h'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'control_subfield': value.get('w'),
        'date_of_a_work': value.get('f'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'version': value.get('s'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'linkage': value.get('6'),
        'date_of_meeting': value.get('d'),
        'language_of_a_work': value.get('l'),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_from_tracing_uniform_title', '^430.[_2435169807]')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_uniform_title(self, key, value):
    """See From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '5': 'institution_to_which_field_applies',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'y': 'chronological_subdivision',
        'a': 'uniform_title',
        'l': 'language_of_a_work',
        'o': 'arranged_statement_for_music',
        'n': 'number_of_part_section_of_a_work',
        'w': 'control_subfield',
        'k': 'form_subheading',
        'p': 'name_of_part_section_of_a_work',
        '4': 'relationship_code',
        's': 'version',
        'f': 'date_of_a_work',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        '6': 'linkage',
        'd': 'date_of_treaty_signing',
        't': 'title_of_a_work',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'uniform_title': value.get('a'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'control_subfield': value.get('w'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'version': value.get('s'),
        'date_of_a_work': value.get('f'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'title_of_a_work': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('see_from_tracing_chronological_term', '^448..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_term(self, key, value):
    """See From Tracing-Chronological Term."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'a': 'chronological_term',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_topical_term', '^450..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_topical_term(self, key, value):
    """See From Tracing-Topical Term."""
    field_map = {
        'i': 'relationship_information',
        'a': 'topical_term_or_geographic_name_entry_element',
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'g': 'miscellaneous_information',
        'b': 'topical_term_following_geographic_name_entry_element',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_geographic_name', '^451..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_name(self, key, value):
    """See From Tracing-Geographic Name."""
    field_map = {
        'i': 'relationship_information',
        'a': 'geographic_name',
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'g': 'miscellaneous_information',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_name': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_genre_form_term', '^455..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_genre_form_term(self, key, value):
    """See From Tracing-Genre/Form Term."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'a': 'genre_form_term',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'genre_form_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_medium_of_performance_term', '^462..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_medium_of_performance_term(self, key, value):
    """See From Tracing-Medium of Performance Term."""
    field_map = {
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'a': 'medium_of_performance_term',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'medium_of_performance_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_general_subdivision', '^480..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_general_subdivision(self, key, value):
    """See From Tracing-General Subdivision."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_geographic_subdivision', '^481..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_subdivision(self, key, value):
    """See From Tracing-Geographic Subdivision."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_chronological_subdivision', '^482..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_subdivision(self, key, value):
    """See From Tracing-Chronological Subdivision."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_from_tracing_form_subdivision', '^485..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_form_subdivision(self, key, value):
    """See From Tracing-Form Subdivision."""
    field_map = {
        'x': 'general_subdivision',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        'y': 'chronological_subdivision',
        'w': 'control_subfield',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'control_subfield': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }
