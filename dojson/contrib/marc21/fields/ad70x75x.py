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


@marc21_authority.over('established_heading_linking_entry_personal_name', '^700[_013][5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_personal_name(self, key, value):
    """Established Heading Linking Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'q': 'fuller_form_of_name',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
        'j': 'attribution_qualifier',
        'b': 'numeration',
        'x': 'general_subdivision',
        'a': 'personal_name',
        'e': 'relator_term',
        's': 'version',
        '2': 'source_of_heading_or_term',
        'w': 'control_subfield',
        'l': 'language_of_a_work',
        'i': 'relationship_information',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'r': 'key_for_music',
        '4': 'relationship_code',
        'c': 'titles_and_other_words_associated_with_a_name',
        'z': 'geographic_subdivision',
        'p': 'name_of_part_section_of_a_work',
        'm': 'medium_of_performance_for_music',
        'o': 'arranged_statement_for_music',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'd': 'dates_associated_with_a_name',
        'v': 'form_subdivision',
        'f': 'date_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'fuller_form_of_name': value.get('q'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'numeration': value.get('b'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'personal_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'version': value.get('s'),
        'source_of_heading_or_term': value.get('2'),
        'control_subfield': value.get('w'),
        'language_of_a_work': value.get('l'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'key_for_music': value.get('r'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'arranged_statement_for_music': value.get('o'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'date_of_a_work': value.get('f'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_corporate_name', '^710[_201][5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_corporate_name(self, key, value):
    """Established Heading Linking Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
        'b': 'subordinate_unit',
        'x': 'general_subdivision',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'e': 'relator_term',
        's': 'version',
        '2': 'source_of_heading_or_term',
        'w': 'control_subfield',
        'l': 'language_of_a_work',
        'i': 'relationship_information',
        'h': 'medium',
        'n': 'number_of_part_section_meeting',
        '6': 'linkage',
        'r': 'key_for_music',
        '4': 'relationship_code',
        'c': 'location_of_meeting',
        'z': 'geographic_subdivision',
        'p': 'name_of_part_section_of_a_work',
        'm': 'medium_of_performance_for_music',
        'o': 'arranged_statement_for_music',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'd': 'date_of_meeting_or_treaty_signing',
        'v': 'form_subdivision',
        'f': 'date_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'version': value.get('s'),
        'source_of_heading_or_term': value.get('2'),
        'control_subfield': value.get('w'),
        'language_of_a_work': value.get('l'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'key_for_music': value.get('r'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'arranged_statement_for_music': value.get('o'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'date_of_a_work': value.get('f'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_meeting_name', '^711[_201][5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_meeting_name(self, key, value):
    """Established Heading Linking Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
        'j': 'relator_term',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'e': 'subordinate_unit',
        'i': 'relationship_information',
        '2': 'source_of_heading_or_term',
        'l': 'language_of_a_work',
        's': 'version',
        'h': 'medium',
        'n': 'number_of_part_section_meeting',
        '6': 'linkage',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'c': 'location_of_meeting',
        'z': 'geographic_subdivision',
        'p': 'name_of_part_section_of_a_work',
        'f': 'date_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'd': 'date_of_meeting',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'source_of_heading_or_term': value.get('2'),
        'language_of_a_work': value.get('l'),
        'version': value.get('s'),
        'medium': value.get('h'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_a_work': value.get('f'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_of_meeting': value.get('d'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_uniform_title', '^730.[5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_uniform_title(self, key, value):
    """Established Heading Linking Entry-Uniform Title."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'y': 'chronological_subdivision',
        'g': 'miscellaneous_information',
        't': 'title_of_a_work',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'a': 'uniform_title',
        'i': 'relationship_information',
        '2': 'source_of_heading_or_term',
        'l': 'language_of_a_work',
        's': 'version',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'w': 'control_subfield',
        '4': 'relationship_code',
        'z': 'geographic_subdivision',
        'd': 'date_of_treaty_signing',
        'p': 'name_of_part_section_of_a_work',
        'm': 'medium_of_performance_for_music',
        'o': 'arranged_statement_for_music',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'r': 'key_for_music',
        'f': 'date_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'uniform_title': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'source_of_heading_or_term': value.get('2'),
        'language_of_a_work': value.get('l'),
        'version': value.get('s'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'arranged_statement_for_music': value.get('o'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key_for_music': value.get('r'),
        'date_of_a_work': value.get('f'),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_chronological_term', '^748.[5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_chronological_term(self, key, value):
    """Established Heading Linking Entry-Chronological Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'i': 'relationship_information',
        'a': 'chronological_term',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'chronological_term': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_topical_term', '^750.[5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_topical_term(self, key, value):
    """Established Heading Linking Entry-Topical Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'w': 'control_subfield',
        'g': 'miscellaneous_information',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'a': 'topical_term_or_geographic_name_entry_element',
        'i': 'relationship_information',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'b': 'topical_term_following_geographic_name_entry_element',
        '8': 'field_link_and_sequence_number',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_geographic_name', '^751.[5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_geographic_name(self, key, value):
    """Established Heading Linking Entry-Geographic Name."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'i': 'relationship_information',
        'a': 'geographic_name',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_name': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('established_heading_linking_entry_genre_form_term', '^755.[5674_2031]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_genre_form_term(self, key, value):
    """Established Heading Linking Entry-Genre/Form Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        'x': 'general_subdivision',
        'i': 'relationship_information',
        'a': 'genre_form_term_as_entry_element',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'genre_form_term_as_entry_element': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }
