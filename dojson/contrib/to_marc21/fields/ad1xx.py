# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_authority


@to_marc21_authority.over('100', '^heading_personal_name$')
@utils.filter_values
def reverse_heading_personal_name(self, key, value):
    """Reverse - Heading-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'form_subheading': 'k',
        'fuller_form_of_name': 'q',
        'general_subdivision': 'x',
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'numeration': 'b',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'personal_name': 'a',
        'chronological_subdivision': 'y',
        'medium_of_performance_for_music': 'm',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'key_for_music': 'r',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'dates_associated_with_a_name': 'd',
        'language_of_a_work': 'l',
        'title_of_a_work': 't',
        'attribution_qualifier': 'j',
        'form_subdivision': 'v',
        'titles_and_other_words_associated_with_a_name': 'c',
        'version': 's',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'q': value.get('fuller_form_of_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'b': value.get('numeration'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('personal_name'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'r': value.get('key_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': value.get('dates_associated_with_a_name'),
        'l': value.get('language_of_a_work'),
        't': value.get('title_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        's': value.get('version'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('110', '^heading_corporate_name$')
@utils.filter_values
def reverse_heading_corporate_name(self, key, value):
    """Reverse - Heading-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'form_subheading': 'k',
        'general_subdivision': 'x',
        'medium': 'h',
        'number_of_part_section_meeting': 'n',
        'subordinate_unit': 'b',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'chronological_subdivision': 'y',
        'medium_of_performance_for_music': 'm',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'key_for_music': 'r',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'date_of_meeting_or_treaty_signing': 'd',
        'language_of_a_work': 'l',
        'title_of_a_work': 't',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'location_of_meeting': 'c',
        'version': 's',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'r': value.get('key_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'l': value.get('language_of_a_work'),
        't': value.get('title_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        's': value.get('version'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('111', '^heading_meeting_name$')
@utils.filter_values
def reverse_heading_meeting_name(self, key, value):
    """Reverse - Heading-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'e',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'number_of_part_section_meeting': 'n',
        'version': 's',
        'date_of_meeting': 'd',
        'geographic_subdivision': 'z',
        'language_of_a_work': 'l',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'relator_term': 'j',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'chronological_subdivision': 'y',
        'location_of_meeting': 'c',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        's': value.get('version'),
        'd': value.get('date_of_meeting'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('130', '^heading_uniform_title$')
@utils.filter_values
def reverse_heading_uniform_title(self, key, value):
    """Reverse - Heading-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'version': 's',
        'date_of_treaty_signing': 'd',
        'key_for_music': 'r',
        'language_of_a_work': 'l',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'geographic_subdivision': 'z',
        'uniform_title': 'a',
        'chronological_subdivision': 'y',
        'medium_of_performance_for_music': 'm',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        's': value.get('version'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'r': value.get('key_for_music'),
        'l': value.get('language_of_a_work'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('uniform_title'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('148', '^heading_chronological_term$')
@utils.filter_values
def reverse_heading_chronological_term(self, key, value):
    """Reverse - Heading-Chronological Term."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_term': 'a',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('chronological_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('150', '^heading_topical_term$')
@utils.filter_values
def reverse_heading_topical_term(self, key, value):
    """Reverse - Heading-Topical Term."""
    field_map = {
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'topical_term_or_geographic_name_entry_element': 'a',
        'topical_term_following_geographic_name_entry_element': 'b',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('151', '^heading_geographic_name$')
@utils.filter_values
def reverse_heading_geographic_name(self, key, value):
    """Reverse - Heading-Geographic Name."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'geographic_name': 'a',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('geographic_name'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('155', '^heading_genre_form_term$')
@utils.filter_values
def reverse_heading_genre_form_term(self, key, value):
    """Reverse - Heading-Genre/Form Term."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'genre_form_term': 'a',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('genre_form_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('162', '^heading_medium_of_performance_term$')
@utils.filter_values
def reverse_heading_medium_of_performance_term(self, key, value):
    """Reverse - Heading-Medium of Performance Term."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'medium_of_performance_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('medium_of_performance_term'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('180', '^heading_general_subdivision$')
@utils.filter_values
def reverse_heading_general_subdivision(self, key, value):
    """Reverse - Heading-General Subdivision."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('181', '^heading_geographic_subdivision$')
@utils.filter_values
def reverse_heading_geographic_subdivision(self, key, value):
    """Reverse - Heading-Geographic Subdivision."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('182', '^heading_chronological_subdivision$')
@utils.filter_values
def reverse_heading_chronological_subdivision(self, key, value):
    """Reverse - Heading-Chronological Subdivision."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('185', '^heading_form_subdivision$')
@utils.filter_values
def reverse_heading_form_subdivision(self, key, value):
    """Reverse - Heading-Form Subdivision."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
