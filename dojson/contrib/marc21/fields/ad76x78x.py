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


@marc21_authority.over('established_heading_linking_entry_medium_of_performance_term', '^762.[4210_6735]')
@utils.for_each_value
@utils.filter_values
def established_heading_linking_entry_medium_of_performance_term(self, key, value):
    """Established Heading Linking Entry-Medium of Performance Term."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'w': 'control_subfield',
        'i': 'relationship_information',
        'a': 'medium_of_performance_term_as_entry_element',
        '6': 'linkage',
        '4': 'relationship_code',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium_of_performance_term_as_entry_element': value.get('a'),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('subdivision_linking_entry_general_subdivision', '^780.[4210_6735]')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_general_subdivision(self, key, value):
    """Subdivision Linking Entry-General Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'w': 'control_subfield',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '6': 'linkage',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('subdivision_linking_entry_geographic_subdivision', '^781.[4210_6735]')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_geographic_subdivision(self, key, value):
    """Subdivision Linking Entry-Geographic Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'w': 'control_subfield',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '6': 'linkage',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('subdivision_linking_entry_chronological_subdivision', '^782.[4210_6735]')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_chronological_subdivision(self, key, value):
    """Subdivision Linking Entry-Chronological Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'w': 'control_subfield',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '6': 'linkage',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('subdivision_linking_entry_form_subdivision', '^785.[4210_6735]')
@utils.for_each_value
@utils.filter_values
def subdivision_linking_entry_form_subdivision(self, key, value):
    """Subdivision Linking Entry-Form Subdivision."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'w': 'control_subfield',
        'i': 'relationship_information',
        'z': 'geographic_subdivision',
        '4': 'relationship_code',
        'v': 'form_subdivision',
        '2': 'source_of_heading_or_term',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
        'x': 'general_subdivision',
        '6': 'linkage',
        'y': 'chronological_subdivision',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_subfield': value.get('w'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'source_of_heading_or_term': value.get('2'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('complex_linking_entry_data', '^788.[4210_6735]')
@utils.filter_values
def complex_linking_entry_data(self, key, value):
    """Complex Linking Entry Data."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re", "7": "Source specified in subfield $2"}
    field_map = {
        'i': 'explanatory_text',
        'a': 'heading_referred_to',
        '6': 'linkage',
        '4': 'relationship_code',
        '2': 'source_of_heading_or_term',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('thesaurus')

    return {
        '__order__': tuple(order) if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'source_of_heading_or_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'thesaurus': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }
