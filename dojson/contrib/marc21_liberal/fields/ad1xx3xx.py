# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_authority


@marc21_authority.over('heading_personal_name', '^100[103_].')
@utils.filter_values
def heading_personal_name(self, key, value):
    """Heading-Personal Name."""
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

    indicator_map1 = {'0': 'Forename', '1': 'Surname', '3': 'Family name'}

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_corporate_name', '^110[10_2].')
@utils.filter_values
def heading_corporate_name(self, key, value):
    """Heading-Corporate Name."""
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

    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order'}

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
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
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
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
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('heading_meeting_name', '^111[10_2].')
@utils.filter_values
def heading_meeting_name(self, key, value):
    """Heading-Meeting Name."""
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

    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order'}

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')),
        'location_of_meeting': utils.force_list(
            value.get('c')),
        'form_subdivision': utils.force_list(
            value.get('v')),
        'subordinate_unit': utils.force_list(
            value.get('e')),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')),
        'relator_term': utils.force_list(
            value.get('j')),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'geographic_subdivision': utils.force_list(
            value.get('z')),
        'type_of_meeting_name_entry_element': indicator_map1.get(
            key[3]),
    }


@marc21_authority.over('heading_uniform_title', '^130.[_1032547698]')
@utils.filter_values
def heading_uniform_title(self, key, value):
    """Heading-Uniform Title."""
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

    indicator_map2 = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'}

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
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
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
    }


@marc21_authority.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        'a': 'content_type_term',
        'b': 'content_type_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        'a': 'format_of_notated_music_term',
        'b': 'format_of_notated_music_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('complex_see_also_reference_subject', '^360..')
@utils.for_each_value
@utils.filter_values
def complex_see_also_reference_subject(self, key, value):
    """Complex See Also Reference-Subject."""
    field_map = {
        'a': 'heading_referred_to',
        'i': 'explanatory_text',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over(
    'other_attributes_of_person_or_corporate_body',
    '^368..')
@utils.for_each_value
@utils.filter_values
def other_attributes_of_person_or_corporate_body(self, key, value):
    """Other Attributes of Person or Corporate Body."""
    field_map = {
        'a': 'type_of_corporate_body',
        'b': 'type_of_jurisdiction',
        'c': 'other_designation',
        'd': 'title_of_person',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_corporate_body': utils.force_list(
            value.get('a')
        ),
        'other_designation': utils.force_list(
            value.get('c')
        ),
        'type_of_jurisdiction': utils.force_list(
            value.get('b')
        ),
        'title_of_person': utils.force_list(
            value.get('d')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'a': 'place_of_birth',
        'b': 'place_of_death',
        'c': 'associated_country',
        'e': 'place_of_residence_headquarters',
        'f': 'other_associated_place',
        'g': 'place_of_origin_of_work',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_birth': value.get('a'),
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'place_of_death': value.get('b'),
        'place_of_residence_headquarters': utils.force_list(
            value.get('e')
        ),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('address', '^371..')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    field_map = {
        'a': 'address',
        'b': 'city',
        'c': 'intermediate_jurisdiction',
        'd': 'country',
        'e': 'postal_code',
        'm': 'electronic_mail_address',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        'z': 'public_note',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'address': utils.force_list(
            value.get('a')
        ),
        'intermediate_jurisdiction': value.get('c'),
        'city': value.get('b'),
        'postal_code': value.get('e'),
        'country': value.get('d'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'start_period': value.get('s'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'end_period': value.get('t'),
    }


@marc21_authority.over('field_of_activity', '^372..')
@utils.for_each_value
@utils.filter_values
def field_of_activity(self, key, value):
    """Field of Activity."""
    field_map = {
        'a': 'field_of_activity',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_of_activity': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_group', '^373..')
@utils.for_each_value
@utils.filter_values
def associated_group(self, key, value):
    """Associated Group."""
    field_map = {
        'a': 'associated_group',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'associated_group': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('occupation', '^374..')
@utils.for_each_value
@utils.filter_values
def occupation(self, key, value):
    """Occupation."""
    field_map = {
        'a': 'occupation',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'occupation': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('gender', '^375..')
@utils.for_each_value
@utils.filter_values
def gender(self, key, value):
    """Gender."""
    field_map = {
        'a': 'gender',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'gender': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('family_information', '^376..')
@utils.for_each_value
@utils.filter_values
def family_information(self, key, value):
    """Family Information."""
    field_map = {
        'a': 'type_of_family',
        'b': 'name_of_prominent_member',
        'c': 'hereditary_title',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_family': utils.force_list(
            value.get('a')
        ),
        'hereditary_title': utils.force_list(
            value.get('c')
        ),
        'name_of_prominent_member': utils.force_list(
            value.get('b')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    field_map = {
        'a': 'language_code',
        'l': 'language_term',
        '2': 'source_of_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'linkage': value.get('6'),
        'source_of_code': value.get('2', 'MARC language code')
    }


@marc21_authority.over('fuller_form_of_personal_name', '^378..')
@utils.filter_values
def fuller_form_of_personal_name(self, key, value):
    """Fuller Form of Personal Name."""
    field_map = {
        'q': 'fuller_form_of_personal_name',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'fuller_form_of_personal_name': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        'a': 'form_of_work',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over(
    'other_distinguishing_characteristics_of_work_or_expression',
    '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(
        self,
        key,
        value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'a': 'other_distinguishing_characteristic',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('medium_of_performance', '^382[10_].')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    field_map = {
        'a': 'medium_of_performance',
        'b': 'soloist',
        'd': 'doubling_instrument',
        'e': 'number_of_ensembles',
        'n': 'number_of_performers_of_the_same_medium',
        'p': 'alternative_medium_of_performance',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        's': 'total_number_of_performers',
        'v': 'note',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Medium of performance',
        '1': 'Partial medium of performance'}

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'number_of_ensembles': utils.force_list(
            value.get('e')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': utils.force_list(
            value.get('r')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'total_number_of_performers': value.get('s'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21_authority.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'a': 'serial_number',
        'b': 'opus_number',
        'c': 'thematic_index_number',
        'd': 'thematic_index_code',
        'e': 'publisher_associated_with_opus_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'publisher_associated_with_opus_number': value.get('e'),
        'thematic_index_code': value.get('d'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('key', '^384..')
@utils.filter_values
def key(self, key, value):
    """Key."""
    field_map = {
        'a': 'key',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        '_': 'Relationship to original unknown',
        '0': 'Original key',
        '1': 'Transposed key'
    }

    if key[3] in indicator_map1:
        order.append('key_type')

    return {
        '__order__': tuple(order) if len(order) else None,
        'key': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'key_type': indicator_map1.get(key[3])
    }


@marc21_authority.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'a': 'audience_term',
        'b': 'audience_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'a': 'creator_contributor_term',
        'b': 'creator_contributor_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('time_period_of_creation', '^388[1_2].')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    field_map = {
        'a': 'time_period_of_creation_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        '_': 'No information provided',
        '1': 'Creation of work',
        '2': 'Creation of aggregate work'}

    if key[3] in indicator_map1:
        order.append('type_of_time_period')

    return {
        '__order__': tuple(order) if len(order) else None,
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_time_period': indicator_map1.get(key[3]),
    }
