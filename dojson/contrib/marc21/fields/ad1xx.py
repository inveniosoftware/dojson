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


@marc21_authority.over('heading_personal_name', '^100[0_31].')
@utils.filter_values
def heading_personal_name(self, key, value):
    """Heading-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
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
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_name': value.get('a'),
        'numeration': value.get('b'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'fuller_form_of_name': value.get('q'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_corporate_name', '^110[02_1].')
@utils.filter_values
def heading_corporate_name(self, key, value):
    """Heading-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
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
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_meeting_name', '^111[02_1].')
@utils.filter_values
def heading_meeting_name(self, key, value):
    """Heading-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
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
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        's': 'version',
        't': 'title_of_a_work',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
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
        'date_of_meeting': value.get('d'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_uniform_title', '^130.[059874132_6]')
@utils.filter_values
def heading_uniform_title(self, key, value):
    """Heading-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
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
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('heading_chronological_term', '^148..')
@utils.filter_values
def heading_chronological_term(self, key, value):
    """Heading-Chronological Term."""
    field_map = {
        'a': 'chronological_term',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'chronological_term': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_topical_term', '^150..')
@utils.filter_values
def heading_topical_term(self, key, value):
    """Heading-Topical Term."""
    field_map = {
        'a': 'topical_term_or_geographic_name_entry_element',
        'b': 'topical_term_following_geographic_name_entry_element',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_geographic_name', '^151..')
@utils.filter_values
def heading_geographic_name(self, key, value):
    """Heading-Geographic Name."""
    field_map = {
        'a': 'geographic_name',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_name': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_genre_form_term', '^155..')
@utils.filter_values
def heading_genre_form_term(self, key, value):
    """Heading-Genre/Form Term."""
    field_map = {
        'a': 'genre_form_term',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'genre_form_term': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_medium_of_performance_term', '^162..')
@utils.filter_values
def heading_medium_of_performance_term(self, key, value):
    """Heading-Medium of Performance Term."""
    field_map = {
        'a': 'medium_of_performance_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'medium_of_performance_term': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_general_subdivision', '^180..')
@utils.filter_values
def heading_general_subdivision(self, key, value):
    """Heading-General Subdivision."""
    field_map = {
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_geographic_subdivision', '^181..')
@utils.filter_values
def heading_geographic_subdivision(self, key, value):
    """Heading-Geographic Subdivision."""
    field_map = {
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_chronological_subdivision', '^182..')
@utils.filter_values
def heading_chronological_subdivision(self, key, value):
    """Heading-Chronological Subdivision."""
    field_map = {
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('heading_form_subdivision', '^185..')
@utils.filter_values
def heading_form_subdivision(self, key, value):
    """Heading-Form Subdivision."""
    field_map = {
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }
