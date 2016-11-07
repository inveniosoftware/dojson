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


@marc21_liberal_authority.over('established_heading_linking_entry_medium_of_performance_term', '^762..')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_medium_of_performance_term(self, key, value):
    """Established Heading Linking Entry-Medium of Performance Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'a': 'medium_of_performance_term_as_entry_element',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        'i': 'relationship_information',
        'w': 'control_subfield',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'medium_of_performance_term_as_entry_element': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'control_subfield': value.get('w'),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('subdivision_linking_entry_general_subdivision', '^780..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_general_subdivision(self, key, value):
    """Subdivision Linking Entry-General Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'v': 'form_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        '2': 'source_of_heading_or_term',
        'y': 'chronological_subdivision',
        'i': 'relationship_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'source_of_heading_or_term': value.get('2'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('subdivision_linking_entry_geographic_subdivision', '^781..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_geographic_subdivision(self, key, value):
    """Subdivision Linking Entry-Geographic Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'v': 'form_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        '2': 'source_of_heading_or_term',
        'y': 'chronological_subdivision',
        'i': 'relationship_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'source_of_heading_or_term': value.get('2'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('subdivision_linking_entry_chronological_subdivision', '^782..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_chronological_subdivision(self, key, value):
    """Subdivision Linking Entry-Chronological Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'v': 'form_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        '2': 'source_of_heading_or_term',
        'y': 'chronological_subdivision',
        'i': 'relationship_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'source_of_heading_or_term': value.get('2'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('subdivision_linking_entry_form_subdivision', '^785..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_form_subdivision(self, key, value):
    """Subdivision Linking Entry-Form Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'v': 'form_subdivision',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        'z': 'geographic_subdivision',
        '2': 'source_of_heading_or_term',
        'y': 'chronological_subdivision',
        'i': 'relationship_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'source_of_heading_or_term': value.get('2'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('complex_linking_entry_data', '^788..')
@utils.filter_values
def complex_linking_entry_data(self, key, value):
    """Complex Linking Entry Data."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        '4': 'relationship_code',
        'a': 'heading_referred_to',
        '6': 'linkage',
        '2': 'source_of_heading_or_term',
        '8': 'field_link_and_sequence_number',
        'i': 'explanatory_text',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'source_of_heading_or_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'thesaurus': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
