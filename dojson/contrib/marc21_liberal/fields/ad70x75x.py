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

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('established_heading_linking_entry_personal_name', '^700..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_personal_name(self, key, value):
    """Established Heading Linking Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'j': 'attribution_qualifier',
        'x': 'general_subdivision',
        '4': 'relationship_code',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        '2': 'source_of_heading_or_term',
        'k': 'form_subheading',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        's': 'version',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'personal_name',
        'q': 'fuller_form_of_name',
        '8': 'field_link_and_sequence_number',
        'y': 'chronological_subdivision',
        'c': 'titles_and_other_words_associated_with_a_name',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'd': 'dates_associated_with_a_name',
        'r': 'key_for_music',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'b': 'numeration',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'source_of_heading_or_term': value.get('2'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'personal_name': value.get('a'),
        'fuller_form_of_name': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'arranged_statement_for_music': value.get('o'),
        'dates_associated_with_a_name': value.get('d'),
        'key_for_music': value.get('r'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'numeration': value.get('b'),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
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
        'x': 'general_subdivision',
        '4': 'relationship_code',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        '2': 'source_of_heading_or_term',
        'k': 'form_subheading',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        's': 'version',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'r': 'key_for_music',
        '8': 'field_link_and_sequence_number',
        'y': 'chronological_subdivision',
        'c': 'location_of_meeting',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'd': 'date_of_meeting_or_treaty_signing',
        'n': 'number_of_part_section_meeting',
        '6': 'linkage',
        'b': 'subordinate_unit',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'source_of_heading_or_term': value.get('2'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'key_for_music': value.get('r'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'arranged_statement_for_music': value.get('o'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
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
        'j': 'relator_term',
        'x': 'general_subdivision',
        '4': 'relationship_code',
        'i': 'relationship_information',
        'l': 'language_of_a_work',
        '2': 'source_of_heading_or_term',
        'k': 'form_subheading',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        's': 'version',
        'z': 'geographic_subdivision',
        'n': 'number_of_part_section_meeting',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        '8': 'field_link_and_sequence_number',
        'y': 'chronological_subdivision',
        'c': 'location_of_meeting',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'd': 'date_of_meeting',
        '6': 'linkage',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'language_of_a_work': value.get('l'),
        'source_of_heading_or_term': value.get('2'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_meeting': value.get('d'),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
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
        'x': 'general_subdivision',
        '4': 'relationship_code',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
        '2': 'source_of_heading_or_term',
        'k': 'form_subheading',
        'f': 'date_of_a_work',
        's': 'version',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        'v': 'form_subdivision',
        'g': 'miscellaneous_information',
        'a': 'uniform_title',
        'r': 'key_for_music',
        '8': 'field_link_and_sequence_number',
        'y': 'chronological_subdivision',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'd': 'date_of_treaty_signing',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'source_of_heading_or_term': value.get('2'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'date_of_a_work': value.get('f'),
        'version': value.get('s'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'uniform_title': value.get('a'),
        'key_for_music': value.get('r'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'arranged_statement_for_music': value.get('o'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
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
        'y': 'chronological_subdivision',
        'a': 'chronological_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'x': 'general_subdivision',
        '2': 'source_of_heading_or_term',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '6': 'linkage',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'chronological_term': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'source_of_heading_or_term': value.get('2'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
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
        'y': 'chronological_subdivision',
        'w': 'control_subfield',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '2': 'source_of_heading_or_term',
        'x': 'general_subdivision',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'b': 'topical_term_following_geographic_name_entry_element',
        'a': 'topical_term_or_geographic_name_entry_element',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'source_of_heading_or_term': value.get('2'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
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
        'y': 'chronological_subdivision',
        'a': 'geographic_name',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '2': 'source_of_heading_or_term',
        'x': 'general_subdivision',
        '6': 'linkage',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_name': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'source_of_heading_or_term': value.get('2'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
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
        'y': 'chronological_subdivision',
        'a': 'genre_form_term_as_entry_element',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'x': 'general_subdivision',
        '2': 'source_of_heading_or_term',
        'z': 'geographic_subdivision',
        'i': 'relationship_information',
        '6': 'linkage',
        'v': 'form_subdivision',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'genre_form_term_as_entry_element': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'source_of_heading_or_term': value.get('2'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
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
