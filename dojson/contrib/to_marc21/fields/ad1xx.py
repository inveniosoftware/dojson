# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
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
    field_map = {
        'personal_name': 'a',
        'numeration': 'b',
        'titles_and_other_words_associated_with_a_name': 'c',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'fuller_form_of_name': 'q',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Family name': '3', 'Forename': '0', 'Surname': '1'}
    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('personal_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'b': value.get('numeration'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
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
    field_map = {
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'b',
        'location_of_meeting': 'c',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_meeting': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Inverted name': '0',
                      'Jurisdiction name': '1', 'Name in direct order': '2'}
    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('111', '^heading_meeting_name$')
@utils.filter_values
def reverse_heading_meeting_name(self, key, value):
    """Reverse - Heading-Meeting Name."""
    field_map = {
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'location_of_meeting': 'c',
        'date_of_meeting': 'd',
        'subordinate_unit': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relator_term': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Inverted name': '0',
                      'Jurisdiction name': '1', 'Name in direct order': '2'}
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('130', '^heading_uniform_title$')
@utils.filter_values
def reverse_heading_uniform_title(self, key, value):
    """Reverse - Heading-Uniform Title."""
    field_map = {
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
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
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('148', '^heading_chronological_term$')
@utils.filter_values
def reverse_heading_chronological_term(self, key, value):
    """Reverse - Heading-Chronological Term."""
    field_map = {
        'chronological_term': 'a',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'topical_term_or_geographic_name_entry_element': 'a',
        'topical_term_following_geographic_name_entry_element': 'b',
        'miscellaneous_information': 'g',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'geographic_name': 'a',
        'miscellaneous_information': 'g',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'genre_form_term': 'a',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('genre_form_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'medium_of_performance_term': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('medium_of_performance_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('180', '^heading_general_subdivision$')
@utils.filter_values
def reverse_heading_general_subdivision(self, key, value):
    """Reverse - Heading-General Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
