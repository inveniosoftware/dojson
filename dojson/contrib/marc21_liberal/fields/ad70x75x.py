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

from ..utils import liberal_map_order
from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('established_heading_linking_entry_personal_name', '^700..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_personal_name(self, key, value):
    """Established Heading Linking Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'personal_name',
        'b': 'numeration',
        'c': 'titles_and_other_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
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
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_corporate_name', '^710..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_corporate_name(self, key, value):
    """Established Heading Linking Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'b': 'subordinate_unit',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting_or_treaty_signing',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
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
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_meeting_name', '^711..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_meeting_name(self, key, value):
    """Established Heading Linking Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
        'j': 'relator_term',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        's': 'version',
        't': 'title_of_a_work',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_uniform_title', '^730..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_uniform_title(self, key, value):
    """Established Heading Linking Entry-Uniform Title."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
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
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
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
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_chronological_term', '^748..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_chronological_term(self, key, value):
    """Established Heading Linking Entry-Chronological Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'chronological_term',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'chronological_term': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_topical_term', '^750..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_topical_term(self, key, value):
    """Established Heading Linking Entry-Topical Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'topical_term_or_geographic_name_entry_element',
        'b': 'topical_term_following_geographic_name_entry_element',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_geographic_name(self, key, value):
    """Established Heading Linking Entry-Geographic Name."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'geographic_name',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_name': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('established_heading_linking_entry_genre_form_term', '^755..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_genre_form_term(self, key, value):
    """Established Heading Linking Entry-Genre/Form Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'genre_form_term_as_entry_element',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'genre_form_term_as_entry_element': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
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
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
