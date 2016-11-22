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
        'a': 'medium_of_performance_term_as_entry_element',
        'i': 'relationship_information',
        'w': 'control_subfield',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'medium_of_performance_term_as_entry_element': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'control_subfield': value.get('w'),
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


@marc21_liberal_authority.over('subdivision_linking_entry_general_subdivision', '^780..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_general_subdivision(self, key, value):
    """Subdivision Linking Entry-General Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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


@marc21_liberal_authority.over('subdivision_linking_entry_geographic_subdivision', '^781..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_geographic_subdivision(self, key, value):
    """Subdivision Linking Entry-Geographic Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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


@marc21_liberal_authority.over('subdivision_linking_entry_chronological_subdivision', '^782..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_chronological_subdivision(self, key, value):
    """Subdivision Linking Entry-Chronological Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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


@marc21_liberal_authority.over('subdivision_linking_entry_form_subdivision', '^785..')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_form_subdivision(self, key, value):
    """Subdivision Linking Entry-Form Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
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


@marc21_liberal_authority.over('complex_linking_entry_data', '^788..')
@utils.filter_values
def complex_linking_entry_data(self, key, value):
    """Complex Linking Entry Data."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'a': 'heading_referred_to',
        'i': 'explanatory_text',
        '2': 'source_of_heading_or_term',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('thesaurus')

    record_dict = {
        '__order__': order if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
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
