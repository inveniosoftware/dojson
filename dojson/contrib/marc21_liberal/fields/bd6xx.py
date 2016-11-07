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

from ..model import marc21_liberal


@marc21_liberal.over('subject_added_entry_personal_name', '^600..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    """Subject Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'd': 'dates_associated_with_a_name',
        'a': 'personal_name',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_of_a_work',
        'f': 'date_of_a_work',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'fuller_form_of_name',
        'k': 'form_subheading',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        'c': 'titles_and_other_words_associated_with_a_name',
        's': 'version',
        't': 'title_of_a_work',
        'b': 'numeration',
        'm': 'medium_of_performance_for_music',
        'u': 'affiliation',
        'j': 'attribution_qualifier',
        'v': 'form_subdivision',
        'r': 'key_for_music',
        '2': 'source_of_heading_or_term',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'dates_associated_with_a_name': value.get('d'),
        'personal_name': value.get('a'),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'date_of_a_work': value.get('f'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'fuller_form_of_name': value.get('q'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'numeration': value.get('b'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'affiliation': value.get('u'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'key_for_music': value.get('r'),
        'source_of_heading_or_term': value.get('2'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_corporate_name', '^610..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    """Subject Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'd': 'date_of_meeting_or_treaty_signing',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_meeting',
        'f': 'date_of_a_work',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        'c': 'location_of_meeting',
        's': 'version',
        't': 'title_of_a_work',
        'b': 'subordinate_unit',
        'm': 'medium_of_performance_for_music',
        'u': 'affiliation',
        'v': 'form_subdivision',
        'r': 'key_for_music',
        '2': 'source_of_heading_or_term',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'date_of_a_work': value.get('f'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'affiliation': value.get('u'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'key_for_music': value.get('r'),
        'source_of_heading_or_term': value.get('2'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_meeting_name', '^611..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    """Subject Added Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'd': 'date_of_meeting',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_meeting',
        'f': 'date_of_a_work',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'k': 'form_subheading',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'z': 'geographic_subdivision',
        'e': 'subordinate_unit',
        'c': 'location_of_meeting',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'j': 'relator_term',
        'v': 'form_subdivision',
        '2': 'source_of_heading_or_term',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'date_of_meeting': value.get('d'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'date_of_a_work': value.get('f'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_heading_or_term': value.get('2'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_uniform_title', '^630..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    """Subject Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'd': 'date_of_treaty_signing',
        'a': 'uniform_title',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_of_a_work',
        'f': 'date_of_a_work',
        'o': 'arranged_statement_for_music',
        'y': 'chronological_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        's': 'version',
        't': 'title_of_a_work',
        'm': 'medium_of_performance_for_music',
        'v': 'form_subdivision',
        'r': 'key_for_music',
        '2': 'source_of_heading_or_term',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('nonfiling_characters')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'uniform_title': value.get('a'),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'date_of_a_work': value.get('f'),
        'arranged_statement_for_music': value.get('o'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'key_for_music': value.get('r'),
        'source_of_heading_or_term': value.get('2'),
        'nonfiling_characters': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_chronological_term', '^648..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    """Subject Added Entry-Chronological Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        '3': 'materials_specified',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'chronological_term',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'materials_specified': value.get('3'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'chronological_term': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_topical_term', '^650..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    """Subject Added Entry-Topical Term."""
    indicator_map1 = {"0": "No level specified", "1": "Primary", "2": "Secondary", "_": "No information provided"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'd': 'active_dates',
        'e': 'relator_term',
        'c': 'location_of_event',
        'a': 'topical_term_or_geographic_name_entry_element',
        'b': 'topical_term_following_geographic_name_entry_element',
        '2': 'source_of_heading_or_term',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('level_of_subject')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'active_dates': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'location_of_event': value.get('c'),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'source_of_heading_or_term': value.get('2'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'level_of_subject': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_geographic_name', '^651..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    """Subject Added Entry-Geographic Name."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
    field_map = {
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'miscellaneous_information',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        '2': 'source_of_heading_or_term',
        'a': 'geographic_name',
        'x': 'general_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'source_of_heading_or_term': value.get('2'),
        'geographic_name': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('index_term_uncontrolled', '^653..')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    """Index Term-Uncontrolled."""
    indicator_map1 = {"0": "No level specified", "1": "Primary", "2": "Secondary", "_": "No information provided"}
    indicator_map2 = {"0": "Topical term", "1": "Personal name", "2": "Corporate name", "3": "Meeting name", "4": "Chronological term", "5": "Geographic name", "6": "Genre/form term", "_": "No information provided"}
    field_map = {
        '6': 'linkage',
        'a': 'uncontrolled_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('level_of_index_term')

    if key[4] != '_':
        order.append('type_of_term_or_name')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'uncontrolled_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'level_of_index_term': indicator_map1.get(key[3], key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_faceted_topical_terms', '^654..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    """Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {"0": "No level specified", "1": "Primary", "2": "Secondary", "_": "No information provided"}
    field_map = {
        '6': 'linkage',
        '4': 'relator_code',
        'z': 'geographic_subdivision',
        'e': 'relator_term',
        'c': 'facet_hierarchy_designation',
        'a': 'focus_term',
        'b': 'non_focus_term',
        '2': 'source_of_heading_or_term',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('level_of_subject')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'focus_term': utils.force_list(
            value.get('a')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'source_of_heading_or_term': value.get('2'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'level_of_subject': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('index_term_genre_form', '^655..')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    """Index Term-Genre/Form."""
    indicator_map1 = {"0": "Faceted", "_": "Basic"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
    field_map = {
        '6': 'linkage',
        'z': 'geographic_subdivision',
        '2': 'source_of_term',
        'c': 'facet_hierarchy_designation',
        'a': 'genre_form_data_or_focus_term',
        'b': 'non_focus_term',
        '5': 'institution_to_which_field_applies',
        'x': 'general_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_heading')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'source_of_term': value.get('2'),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'genre_form_data_or_focus_term': value.get('a'),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'type_of_heading': indicator_map1.get(key[3], key[3]),
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('index_term_occupation', '^656..')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    """Index Term-Occupation."""
    indicator_map2 = {"7": "Source specified in subfield $2"}
    field_map = {
        '3': 'materials_specified',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'source_of_term',
        '0': 'authority_record_control_number',
        'a': 'occupation',
        'k': 'form',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_term')

    record_dict = {
        '__order__': order if len(order) else None,
        'materials_specified': value.get('3'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'occupation': value.get('a'),
        'form': value.get('k'),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_term': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('index_term_function', '^657..')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    """Index Term-Function."""
    indicator_map2 = {"7": "Source specified in subfield $2"}
    field_map = {
        '3': 'materials_specified',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'source_of_term',
        '0': 'authority_record_control_number',
        'a': 'function',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_term')

    record_dict = {
        '__order__': order if len(order) else None,
        'materials_specified': value.get('3'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'function': value.get('a'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_term': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('index_term_curriculum_objective', '^658..')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    """Index Term-Curriculum Objective."""
    field_map = {
        '6': 'linkage',
        'd': 'correlation_factor',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_term_or_code',
        'c': 'curriculum_code',
        'a': 'main_curriculum_objective',
        'b': 'subordinate_curriculum_objective',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'correlation_factor': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_term_or_code': value.get('2'),
        'curriculum_code': value.get('c'),
        'main_curriculum_objective': value.get('a'),
        'subordinate_curriculum_objective': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_added_entry_hierarchical_place_name', '^662..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    """Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        '6': 'linkage',
        '4': 'relator_code',
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
        'd': 'city',
        'e': 'relator_term',
        'c': 'intermediate_political_jurisdiction',
        'a': 'country_or_larger_entity',
        'b': 'first_order_political_jurisdiction',
        'h': 'extraterrestrial_area',
        'f': 'city_subsection',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'city': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
