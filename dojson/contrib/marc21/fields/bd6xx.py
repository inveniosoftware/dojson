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


@marc21.over('subject_added_entry_personal_name', '^600[03_1][341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    """Subject Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'q': 'fuller_form_of_name',
        'c': 'titles_and_other_words_associated_with_a_name',
        'y': 'chronological_subdivision',
        '4': 'relator_code',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'n': 'number_of_part_section_of_a_work',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        'r': 'key_for_music',
        'u': 'affiliation',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'd': 'dates_associated_with_a_name',
        'f': 'date_of_a_work',
        'l': 'language_of_a_work',
        'h': 'medium',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'relator_term',
        'j': 'attribution_qualifier',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'personal_name',
        'b': 'numeration',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'fuller_form_of_name': value.get('q'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'dates_associated_with_a_name': value.get('d'),
        'date_of_a_work': value.get('f'),
        'language_of_a_work': value.get('l'),
        'medium': value.get('h'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'personal_name': value.get('a'),
        'numeration': value.get('b'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_corporate_name', '^610[0_12][341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    """Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'c': 'location_of_meeting',
        'y': 'chronological_subdivision',
        '4': 'relator_code',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'n': 'number_of_part_section_meeting',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        'r': 'key_for_music',
        'u': 'affiliation',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'd': 'date_of_meeting_or_treaty_signing',
        'f': 'date_of_a_work',
        'l': 'language_of_a_work',
        'h': 'medium',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'relator_term',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'b': 'subordinate_unit',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'language_of_a_work': value.get('l'),
        'medium': value.get('h'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_meeting_name', '^611[0_12][341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    """Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'c': 'location_of_meeting',
        'y': 'chronological_subdivision',
        '4': 'relator_code',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'k': 'form_subheading',
        'u': 'affiliation',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'p': 'name_of_part_section_of_a_work',
        't': 'title_of_a_work',
        'd': 'date_of_meeting',
        'f': 'date_of_a_work',
        'l': 'language_of_a_work',
        'h': 'medium',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'subordinate_unit',
        'j': 'relator_term',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        'n': 'number_of_part_section_meeting',
        'v': 'form_subdivision',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'affiliation': value.get('u'),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title_of_a_work': value.get('t'),
        'date_of_meeting': value.get('d'),
        'date_of_a_work': value.get('f'),
        'language_of_a_work': value.get('l'),
        'medium': value.get('h'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_uniform_title',
             '^630[9341750_268][341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    """Subject Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        'y': 'chronological_subdivision',
        '4': 'relator_code',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'n': 'number_of_part_section_of_a_work',
        'x': 'general_subdivision',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
        'r': 'key_for_music',
        's': 'version',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        't': 'title_of_a_work',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'l': 'language_of_a_work',
        'h': 'medium',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'relator_term',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        'a': 'uniform_title',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('nonfiling_characters')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'title_of_a_work': value.get('t'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'language_of_a_work': value.get('l'),
        'medium': value.get('h'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'uniform_title': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_chronological_term', '^648.[341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    """Subject Added Entry-Chronological Term."""
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'y': 'chronological_subdivision',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        '3': 'materials_specified',
        'a': 'chronological_term',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'materials_specified': value.get('3'),
        'chronological_term': value.get('a'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_topical_term', '^650[_120][341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    """Subject Added Entry-Topical Term."""
    indicator_map1 = {
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary",
        "_": "No information provided"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'y': 'chronological_subdivision',
        'd': 'active_dates',
        'c': 'location_of_event',
        '3': 'materials_specified',
        '4': 'relator_code',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'x': 'general_subdivision',
        'e': 'relator_term',
        'b': 'topical_term_following_geographic_name_entry_element',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'v': 'form_subdivision',
        'a': 'topical_term_or_geographic_name_entry_element',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_subject')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'active_dates': value.get('d'),
        'location_of_event': value.get('c'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_geographic_name', '^651.[341750_26]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    """Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'y': 'chronological_subdivision',
        'a': 'geographic_name',
        '3': 'materials_specified',
        'x': 'general_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'relator_term',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        '4': 'relator_code',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_name': value.get('a'),
        'materials_specified': value.get('3'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('index_term_uncontrolled', '^653[_120][3415_026]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    """Index Term-Uncontrolled."""
    indicator_map1 = {
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary",
        "_": "No information provided"}
    indicator_map2 = {
        "0": "Topical term",
        "1": "Personal name",
        "2": "Corporate name",
        "3": "Meeting name",
        "4": "Chronological term",
        "5": "Geographic name",
        "6": "Genre/form term",
        "_": "No information provided"}
    field_map = {
        'a': 'uncontrolled_term',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_index_term')

    if key[4] in indicator_map2:
        order.append('type_of_term_or_name')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uncontrolled_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'level_of_index_term': indicator_map1.get(key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_faceted_topical_terms', '^654[_120].')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    """Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary",
        "_": "No information provided"}
    field_map = {
        'y': 'chronological_subdivision',
        'c': 'facet_hierarchy_designation',
        '3': 'materials_specified',
        '4': 'relator_code',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number',
        'e': 'relator_term',
        'b': 'non_focus_term',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'a': 'focus_term',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_subject')

    return {
        '__order__': tuple(order) if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'focus_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
    }


@marc21.over('index_term_genre_form', '^655[_0][341750_26]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    """Index Term-Genre/Form."""
    indicator_map1 = {"0": "Faceted", "_": "Basic"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    field_map = {
        'y': 'chronological_subdivision',
        'c': 'facet_hierarchy_designation',
        '3': 'materials_specified',
        'a': 'genre_form_data_or_focus_term',
        '5': 'institution_to_which_field_applies',
        '0': 'authority_record_control_number',
        'b': 'non_focus_term',
        '2': 'source_of_term',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_heading')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'genre_form_data_or_focus_term': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'type_of_heading': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('index_term_occupation', '^656.[_7]')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    """Index Term-Occupation."""
    indicator_map2 = {"7": "Source specified in subfield $2"}
    field_map = {
        '0': 'authority_record_control_number',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '2': 'source_of_term',
        '6': 'linkage',
        '3': 'materials_specified',
        'a': 'occupation',
        'k': 'form',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_term')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'materials_specified': value.get('3'),
        'occupation': value.get('a'),
        'form': value.get('k'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_term': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('index_term_function', '^657.[_7]')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    """Index Term-Function."""
    indicator_map2 = {"7": "Source specified in subfield $2"}
    field_map = {
        '0': 'authority_record_control_number',
        'y': 'chronological_subdivision',
        '2': 'source_of_term',
        '6': 'linkage',
        '3': 'materials_specified',
        'a': 'function',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_term')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'linkage': value.get('6'),
        'materials_specified': value.get('3'),
        'function': value.get('a'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_term': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('index_term_curriculum_objective', '^658..')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    """Index Term-Curriculum Objective."""
    field_map = {
        'd': 'correlation_factor',
        'b': 'subordinate_curriculum_objective',
        '2': 'source_of_term_or_code',
        '6': 'linkage',
        'a': 'main_curriculum_objective',
        '8': 'field_link_and_sequence_number',
        'c': 'curriculum_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'correlation_factor': value.get('d'),
        'subordinate_curriculum_objective': utils.force_list(
            value.get('b')
        ),
        'source_of_term_or_code': value.get('2'),
        'linkage': value.get('6'),
        'main_curriculum_objective': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'curriculum_code': value.get('c'),
    }


@marc21.over('subject_added_entry_hierarchical_place_name', '^662..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    """Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        'd': 'city',
        'f': 'city_subsection',
        'c': 'intermediate_political_jurisdiction',
        'h': 'extraterrestrial_area',
        '4': 'relator_code',
        '0': 'authority_record_control_number',
        'e': 'relator_term',
        'b': 'first_order_political_jurisdiction',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'a': 'country_or_larger_entity',
        '8': 'field_link_and_sequence_number',
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'city': value.get('d'),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
    }
