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


@marc21_authority.over('heading_personal_name', '^100[1_30].')
@utils.filter_values
def heading_personal_name(self, key, value):
    """Heading-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'e': 'relator_term',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'm': 'medium_of_performance_for_music',
        'j': 'attribution_qualifier',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'c': 'titles_and_other_words_associated_with_a_name',
        'b': 'numeration',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        'f': 'date_of_a_work',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'o': 'arranged_statement_for_music',
        'r': 'key_for_music',
        'q': 'fuller_form_of_name',
        'a': 'personal_name',
        'h': 'medium',
        'l': 'language_of_a_work',
        'd': 'dates_associated_with_a_name',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'date_of_a_work': value.get('f'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'arranged_statement_for_music': value.get('o'),
        'key_for_music': value.get('r'),
        'fuller_form_of_name': value.get('q'),
        'personal_name': value.get('a'),
        'medium': value.get('h'),
        'language_of_a_work': value.get('l'),
        'dates_associated_with_a_name': value.get('d'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_corporate_name', '^110[21_0].')
@utils.filter_values
def heading_corporate_name(self, key, value):
    """Heading-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'e': 'relator_term',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_meeting',
        '6': 'linkage',
        'c': 'location_of_meeting',
        'b': 'subordinate_unit',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
        'f': 'date_of_a_work',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'k': 'form_subheading',
        'o': 'arranged_statement_for_music',
        'r': 'key_for_music',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'h': 'medium',
        'l': 'language_of_a_work',
        'd': 'date_of_meeting_or_treaty_signing',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'arranged_statement_for_music': value.get('o'),
        'key_for_music': value.get('r'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'medium': value.get('h'),
        'language_of_a_work': value.get('l'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_meeting_name', '^111[21_0].')
@utils.filter_values
def heading_meeting_name(self, key, value):
    """Heading-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'f': 'date_of_a_work',
        'l': 'language_of_a_work',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'e': 'subordinate_unit',
        'p': 'name_of_part_section_of_a_work',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        't': 'title_of_a_work',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'j': 'relator_term',
        's': 'version',
        'n': 'number_of_part_section_meeting',
        '6': 'linkage',
        'c': 'location_of_meeting',
        'y': 'chronological_subdivision',
        'h': 'medium',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        'd': 'date_of_meeting',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_of_a_work': value.get('f'),
        'language_of_a_work': value.get('l'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'title_of_a_work': value.get('t'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'version': value.get('s'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'medium': value.get('h'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'date_of_meeting': value.get('d'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_uniform_title', '^130.[54123_68907]')
@utils.filter_values
def heading_uniform_title(self, key, value):
    """Heading-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'f': 'date_of_a_work',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'k': 'form_subheading',
        'o': 'arranged_statement_for_music',
        'x': 'general_subdivision',
        'p': 'name_of_part_section_of_a_work',
        'a': 'uniform_title',
        't': 'title_of_a_work',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        'g': 'miscellaneous_information',
        's': 'version',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'y': 'chronological_subdivision',
        'h': 'medium',
        '8': 'field_link_and_sequence_number',
        'l': 'language_of_a_work',
        'd': 'date_of_treaty_signing',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_of_a_work': value.get('f'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'arranged_statement_for_music': value.get('o'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'uniform_title': value.get('a'),
        'title_of_a_work': value.get('t'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'version': value.get('s'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'medium': value.get('h'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_of_a_work': value.get('l'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('heading_chronological_term', '^148..')
@utils.filter_values
def heading_chronological_term(self, key, value):
    """Heading-Chronological Term."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '6': 'linkage',
        'a': 'chronological_term',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'chronological_term': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_topical_term', '^150..')
@utils.filter_values
def heading_topical_term(self, key, value):
    """Heading-Topical Term."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '6': 'linkage',
        'b': 'topical_term_following_geographic_name_entry_element',
        'a': 'topical_term_or_geographic_name_entry_element',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_geographic_name', '^151..')
@utils.filter_values
def heading_geographic_name(self, key, value):
    """Heading-Geographic Name."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '6': 'linkage',
        'a': 'geographic_name',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'geographic_name': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_genre_form_term', '^155..')
@utils.filter_values
def heading_genre_form_term(self, key, value):
    """Heading-Genre/Form Term."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '6': 'linkage',
        'a': 'genre_form_term',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'genre_form_term': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_medium_of_performance_term', '^162..')
@utils.filter_values
def heading_medium_of_performance_term(self, key, value):
    """Heading-Medium of Performance Term."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'medium_of_performance_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'medium_of_performance_term': value.get('a'),
    }


@marc21_authority.over('heading_general_subdivision', '^180..')
@utils.filter_values
def heading_general_subdivision(self, key, value):
    """Heading-General Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_geographic_subdivision', '^181..')
@utils.filter_values
def heading_geographic_subdivision(self, key, value):
    """Heading-Geographic Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_chronological_subdivision', '^182..')
@utils.filter_values
def heading_chronological_subdivision(self, key, value):
    """Heading-Chronological Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }


@marc21_authority.over('heading_form_subdivision', '^185..')
@utils.filter_values
def heading_form_subdivision(self, key, value):
    """Heading-Form Subdivision."""
    field_map = {
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
    }
