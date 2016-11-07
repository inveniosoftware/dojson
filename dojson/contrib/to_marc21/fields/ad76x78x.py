# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_authority


@to_marc21_authority.over('762', '^established_heading_linking_entry_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_medium_of_performance_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Medium of Performance Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'control_subfield': 'w',
        'linkage': '6',
        'medium_of_performance_term_as_entry_element': 'a',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'a': value.get('medium_of_performance_term_as_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('780', '^subdivision_linking_entry_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_general_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-General Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('781', '^subdivision_linking_entry_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_geographic_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Geographic Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('782', '^subdivision_linking_entry_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_chronological_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Chronological Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('785', '^subdivision_linking_entry_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_form_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Form Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('788', '^complex_linking_entry_data$')
@utils.filter_values
def reverse_complex_linking_entry_data(self, key, value):
    """Reverse - Complex Linking Entry Data."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'heading_referred_to': 'a',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'explanatory_text': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }
