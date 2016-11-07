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


@marc21_authority.over('see_also_from_tracing_personal_name', '^500[_013].')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_personal_name(self, key, value):
    """See Also From Tracing-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        'x': 'general_subdivision',
        'f': 'date_of_a_work',
        'a': 'personal_name',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        'b': 'numeration',
        'o': 'arranged_statement_for_music',
        'q': 'fuller_form_of_name',
        'd': 'dates_associated_with_a_name',
        'k': 'form_subheading',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'e': 'relator_term',
        'h': 'medium',
        'r': 'key_for_music',
        'y': 'chronological_subdivision',
        'c': 'titles_and_other_words_associated_with_a_name',
        'n': 'number_of_part_section_of_a_work',
        'j': 'attribution_qualifier',
        '5': 'institution_to_which_field_applies',
        'p': 'name_of_part_section_of_a_work',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'version',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'date_of_a_work': value.get('f'),
        'personal_name': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'numeration': value.get('b'),
        'arranged_statement_for_music': value.get('o'),
        'fuller_form_of_name': value.get('q'),
        'dates_associated_with_a_name': value.get('d'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'medium': value.get('h'),
        'key_for_music': value.get('r'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_also_from_tracing_corporate_name', '^510[_021].')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_corporate_name(self, key, value):
    """See Also From Tracing-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        'x': 'general_subdivision',
        'f': 'date_of_a_work',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        'b': 'subordinate_unit',
        'o': 'arranged_statement_for_music',
        'd': 'date_of_meeting_or_treaty_signing',
        'k': 'form_subheading',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'e': 'relator_term',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'y': 'chronological_subdivision',
        'c': 'location_of_meeting',
        'n': 'number_of_part_section_meeting',
        '5': 'institution_to_which_field_applies',
        'p': 'name_of_part_section_of_a_work',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'version',
        'r': 'key_for_music',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'date_of_a_work': value.get('f'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'arranged_statement_for_music': value.get('o'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_also_from_tracing_meeting_name', '^511[_021].')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_meeting_name(self, key, value):
    """See Also From Tracing-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        'f': 'date_of_a_work',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'd': 'date_of_meeting',
        'k': 'form_subheading',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'e': 'subordinate_unit',
        'h': 'medium',
        'y': 'chronological_subdivision',
        'c': 'location_of_meeting',
        'n': 'number_of_part_section_meeting',
        'j': 'relator_term',
        '5': 'institution_to_which_field_applies',
        'p': 'name_of_part_section_of_a_work',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'version',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'date_of_a_work': value.get('f'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'date_of_meeting': value.get('d'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'medium': value.get('h'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_also_from_tracing_uniform_title', '^530.[8162593_047]')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_uniform_title(self, key, value):
    """See Also From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        'f': 'date_of_a_work',
        'a': 'uniform_title',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'o': 'arranged_statement_for_music',
        'd': 'date_of_treaty_signing',
        'k': 'form_subheading',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'y': 'chronological_subdivision',
        'n': 'number_of_part_section_of_a_work',
        '5': 'institution_to_which_field_applies',
        'p': 'name_of_part_section_of_a_work',
        'v': 'form_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'version',
        'r': 'key_for_music',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'date_of_a_work': value.get('f'),
        'uniform_title': value.get('a'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'arranged_statement_for_music': value.get('o'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('see_also_from_tracing_chronological_term', '^548..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_chronological_term(self, key, value):
    """See Also From Tracing-Chronological Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'a': 'chronological_term',
        'w': 'control_subfield',
        'v': 'form_subdivision',
        '0': 'record_control_number',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'chronological_term': value.get('a'),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_also_from_tracing_topical_term', '^550..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_topical_term(self, key, value):
    """See Also From Tracing-Topical Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'a': 'topical_term_or_geographic_name_entry_element',
        'b': 'topical_term_following_geographic_name_entry_element',
        'v': 'form_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
    }


@marc21_authority.over('see_also_from_tracing_geographic_name', '^551..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_geographic_name(self, key, value):
    """See Also From Tracing-Geographic Name."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'a': 'geographic_name',
        'w': 'control_subfield',
        'v': 'form_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'geographic_name': value.get('a'),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
    }


@marc21_authority.over('see_also_from_tracing_genre_form_term', '^555..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_genre_form_term(self, key, value):
    """See Also From Tracing-Genre/Form Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'a': 'genre_form_term',
        'w': 'control_subfield',
        'v': 'form_subdivision',
        '0': 'record_control_number',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'genre_form_term': value.get('a'),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
    }


@marc21_authority.over('see_also_from_tracing_medium_of_performance_term', '^562..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_medium_of_performance_term(self, key, value):
    """See Also From Tracing-Medium of Performance Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'medium_of_performance_term',
        'i': 'relationship_information',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'w': 'control_subfield',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'medium_of_performance_term': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'control_subfield': value.get('w'),
    }


@marc21_authority.over('see_also_from_tracing_general_subdivision', '^580..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_general_subdivision(self, key, value):
    """See Also From Tracing-General Subdivision."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'w': 'control_subfield',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
    }


@marc21_authority.over('see_also_from_tracing_geographic_subdivision', '^581..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_geographic_subdivision(self, key, value):
    """See Also From Tracing-Geographic Subdivision."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'w': 'control_subfield',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
    }


@marc21_authority.over('see_also_from_tracing_chronological_subdivision', '^582..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_chronological_subdivision(self, key, value):
    """See Also From Tracing-Chronological Subdivision."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'w': 'control_subfield',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
    }


@marc21_authority.over('see_also_from_tracing_form_subdivision', '^585..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_form_subdivision(self, key, value):
    """See Also From Tracing-Form Subdivision."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '4': 'relationship_code',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'w': 'control_subfield',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
    }
