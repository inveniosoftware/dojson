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


@marc21.over('subject_added_entry_personal_name', '^600[_013][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    """Subject Added Entry-Personal Name."""
    indicator_map1 = {
        '0': 'Forename',
        '1': 'Surname',
        '3': 'Family name',
    }

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

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
        'u': 'affiliation',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

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
        'miscellaneous_information': value.get('g'),
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
        'affiliation': value.get('u'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_corporate_name', '^610[_0-2][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    """Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

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
        'u': 'affiliation',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'location_of_meeting': value.get('c'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
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
        'affiliation': value.get('u'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_meeting_name', '^611[_0-2][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    """Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

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
        'u': 'affiliation',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'date_of_meeting': value.get('d'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
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
        'affiliation': value.get('u'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over(
    'subject_added_entry_uniform_title', '^630[_0-9][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    """Subject Added Entry-Uniform Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'e': 'relator_term',
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
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in valid_nonfiling_characters:
        order.append('nonfiling_characters')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': utils.int_with_default(key[3], None),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_chronological_term', '^648[_01][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    """Subject Added Entry-Chronological Term."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Date or time period covered or depicted',
        '1': 'Date or time period of creation or origin',
    }

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'chronological_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_date_or_time_period': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_topical_term', '^650[_0-2][_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    """Subject Added Entry-Topical Term."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'No level specified',
        '1': 'Primary',
        '2': 'Secondary',
    }

    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'topical_term_or_geographic_name_entry_element',
        'b': 'topical_term_following_geographic_name_entry_element',
        'c': 'location_of_event',
        'd': 'active_dates',
        'e': 'relator_term',
        'g': 'miscellaneous_information',
        '4': 'relator_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_subject')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'location_of_event': value.get('c'),
        'active_dates': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_geographic_name', '^651_[_0-7]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    """Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'geographic_name',
        'e': 'relator_term',
        'g': 'miscellaneous_information',
        '4': 'relator_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_heading_or_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('index_term_uncontrolled', '^653[_0-2][_0-6]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    """Index Term-Uncontrolled."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'No level specified',
        '1': 'Primary',
        '2': 'Secondary',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Topical term',
        '1': 'Personal name',
        '2': 'Corporate name',
        '3': 'Meeting name',
        '4': 'Chronological term',
        '5': 'Geographic name',
        '6': 'Genre/form term',
    }

    field_map = {
        'a': 'uncontrolled_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'level_of_index_term': indicator_map1.get(key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_faceted_topical_terms', '^654[_0-2]_')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    """Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'No level specified',
        '1': 'Primary',
        '2': 'Secondary',
    }

    field_map = {
        'a': 'focus_term',
        'b': 'non_focus_term',
        'c': 'facet_hierarchy_designation',
        'e': 'relator_term',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_subject')

    return {
        '__order__': tuple(order) if len(order) else None,
        'focus_term': utils.force_list(
            value.get('a')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
    }


@marc21.over('index_term_genre_form', '^655[_0][_0-7]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    """Index Term-Genre/Form."""
    indicator_map1 = {
        '_': 'Basic',
        '0': 'Faceted',
    }
    indicator_map2 = {
        '0': 'Library of Congress Subject Headings',
        '1': "LC subject headings for children's literature",
        '2': 'Medical Subject Headings',
        '3': 'National Agricultural Library subject authority file',
        '4': 'Source not specified',
        '5': 'Canadian Subject Headings',
        '6': 'Répertoire de vedettes-matière',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'genre_form_data_or_focus_term',
        'b': 'non_focus_term',
        'c': 'facet_hierarchy_designation',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_heading')
    if key[4] in indicator_map2:
        order.append('thesaurus')

    if key[4] != '7':
        try:
            order.remove('source_of_term')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'genre_form_data_or_focus_term': value.get('a'),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_heading': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('index_term_occupation', '^656_7')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    """Index Term-Occupation."""
    field_map = {
        'a': 'occupation',
        'k': 'form',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'occupation': value.get('a'),
        'form': value.get('k'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('index_term_function', '^657_7')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    """Index Term-Function."""
    field_map = {
        'a': 'function',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'function': value.get('a'),
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
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('index_term_curriculum_objective', '^658__')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    """Index Term-Curriculum Objective."""
    field_map = {
        'a': 'main_curriculum_objective',
        'b': 'subordinate_curriculum_objective',
        'c': 'curriculum_code',
        'd': 'correlation_factor',
        '2': 'source_of_term_or_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_curriculum_objective': value.get('a'),
        'subordinate_curriculum_objective': utils.force_list(
            value.get('b')
        ),
        'curriculum_code': value.get('c'),
        'correlation_factor': value.get('d'),
        'source_of_term_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('subject_added_entry_hierarchical_place_name', '^662__')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    """Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        'a': 'country_or_larger_entity',
        'b': 'first_order_political_jurisdiction',
        'c': 'intermediate_political_jurisdiction',
        'd': 'city',
        'e': 'relator_term',
        'f': 'city_subsection',
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
        'h': 'extraterrestrial_area',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'city': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }
