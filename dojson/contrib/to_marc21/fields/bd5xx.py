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

from ..model import to_marc21


@to_marc21.over('500', '^general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_general_note(self, key, value):
    """Reverse - General Note."""
    field_map = {
        'general_note': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('general_note'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('501', '^with_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_with_note(self, key, value):
    """Reverse - With Note."""
    field_map = {
        'with_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('with_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('502', '^dissertation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dissertation_note(self, key, value):
    """Reverse - Dissertation Note."""
    field_map = {
        'dissertation_note': 'a',
        'field_link_and_sequence_number': '8',
        'name_of_granting_institution': 'c',
        'year_degree_granted': 'd',
        'dissertation_identifier': 'o',
        'degree_type': 'b',
        'linkage': '6',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('dissertation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('name_of_granting_institution'),
        'd': value.get('year_degree_granted'),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        'b': value.get('degree_type'),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('504', '^bibliography_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_bibliography_note(self, key, value):
    """Reverse - Bibliography, Etc. Note."""
    field_map = {
        'bibliography_note': 'a',
        'field_link_and_sequence_number': '8',
        'number_of_references': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('bibliography_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_references'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('505', '^formatted_contents_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_formatted_contents_note(self, key, value):
    """Reverse - Formatted Contents Note."""
    indicator_map1 = {"Contents": "0", "Incomplete contents": "1", "No display constant generated": "8", "Partial contents": "2"}
    indicator_map2 = {"Basic": "_", "Enhanced": "0"}
    field_map = {
        'statement_of_responsibility': 'r',
        'formatted_contents_note': 'a',
        'field_link_and_sequence_number': '8',
        'title': 't',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')
        ),
        'a': value.get('formatted_contents_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': utils.reverse_force_list(
            value.get('title')
        ),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('level_of_content_designation'), '_'),
    }


@to_marc21.over('506', '^restrictions_on_access_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_restrictions_on_access_note(self, key, value):
    """Reverse - Restrictions on Access Note."""
    indicator_map1 = {"No information provided": "_", "No restrictions": "0", "Restrictions apply": "1"}
    field_map = {
        'physical_access_provisions': 'c',
        'standardized_terminology_for_access_restriction': 'f',
        'uniform_resource_identifier': 'u',
        'authorized_users': 'd',
        'linkage': '6',
        'materials_specified': '3',
        'terms_governing_access': 'a',
        'field_link_and_sequence_number': '8',
        'source_of_term': '2',
        'authorization': 'e',
        'institution_to_which_field_applies': '5',
        'jurisdiction': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('terms_governing_access'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_term'),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        '$ind1': indicator_map1.get(value.get('restriction'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('507', '^scale_note_for_graphic_material$')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    field_map = {
        'representative_fraction_of_scale_note': 'a',
        'field_link_and_sequence_number': '8',
        'remainder_of_scale_note': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('representative_fraction_of_scale_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('remainder_of_scale_note'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('508', '^creation_production_credits_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creation_production_credits_note(self, key, value):
    """Reverse - Creation/Production Credits Note."""
    field_map = {
        'creation_production_credits_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('creation_production_credits_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('510', '^citation_references_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_citation_references_note(self, key, value):
    """Reverse - Citation/References Note."""
    indicator_map1 = {"Coverage complete": "1", "Coverage is selective": "2", "Coverage unknown": "0", "Location in source given": "4", "Location in source not given": "3"}
    field_map = {
        'name_of_source': 'a',
        'materials_specified': '3',
        'international_standard_serial_number': 'x',
        'uniform_resource_identifier': 'u',
        'location_within_source': 'c',
        'coverage_of_source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('name_of_source'),
        '3': value.get('materials_specified'),
        'x': value.get('international_standard_serial_number'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('location_within_source'),
        'b': value.get('coverage_of_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('coverage_location_in_source'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('511', '^participant_or_performer_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_participant_or_performer_note(self, key, value):
    """Reverse - Participant or Performer Note."""
    indicator_map1 = {"Cast": "1", "No display constant generated": "0"}
    field_map = {
        'participant_or_performer_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('participant_or_performer_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('513', '^type_of_report_and_period_covered_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    field_map = {
        'type_of_report': 'a',
        'field_link_and_sequence_number': '8',
        'period_covered': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_report'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('period_covered'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('514', '^data_quality_note$')
@utils.filter_values
def reverse_data_quality_note(self, key, value):
    """Reverse - Data Quality Note."""
    field_map = {
        'attribute_accuracy_explanation': 'c',
        'horizontal_position_accuracy_report': 'f',
        'horizontal_position_accuracy_explanation': 'h',
        'logical_consistency_report': 'd',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'display_note': 'z',
        'attribute_accuracy_report': 'a',
        'field_link_and_sequence_number': '8',
        'completeness_report': 'e',
        'vertical_positional_accuracy_explanation': 'k',
        'cloud_cover': 'm',
        'vertical_positional_accuracy_value': 'j',
        'vertical_positional_accuracy_report': 'i',
        'attribute_accuracy_value': 'b',
        'horizontal_position_accuracy_value': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        'f': value.get('horizontal_position_accuracy_report'),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        'd': value.get('logical_consistency_report'),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'a': value.get('attribute_accuracy_report'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': value.get('completeness_report'),
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'm': value.get('cloud_cover'),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'i': value.get('vertical_positional_accuracy_report'),
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'g': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_value')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('515', '^numbering_peculiarities_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numbering_peculiarities_note(self, key, value):
    """Reverse - Numbering Peculiarities Note."""
    field_map = {
        'numbering_peculiarities_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('numbering_peculiarities_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('516', '^type_of_computer_file_or_data_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_computer_file_or_data_note(self, key, value):
    """Reverse - Type of Computer File or Data Note."""
    indicator_map1 = {"No display constant generated": "8", "Type of file": "_"}
    field_map = {
        'type_of_computer_file_or_data_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_computer_file_or_data_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('518', '^date_time_and_place_of_an_event_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    field_map = {
        'date_time_and_place_of_an_event_note': 'a',
        'materials_specified': '3',
        'source_of_term': '2',
        'date_of_event': 'd',
        'other_event_information': 'o',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'record_control_number': '0',
        'place_of_event': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('date_time_and_place_of_an_event_note'),
        '3': value.get('materials_specified'),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('520', '^summary$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {"Abstract": "3", "Content advice": "4", "No display constant generated": "8", "Review": "1", "Scope and content": "2", "Subject": "0", "Summary": "_"}
    field_map = {
        'summary': 'a',
        'materials_specified': '3',
        'source': '2',
        'uniform_resource_identifier': 'u',
        'assigning_source': 'c',
        'expansion_of_summary_note': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('summary'),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('assigning_source'),
        'b': value.get('expansion_of_summary_note'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('521', '^target_audience_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {"Audience": "_", "Interest age level": "1", "Interest grade level": "2", "Motivation/interest level": "4", "No display constant generated": "8", "Reading grade level": "0", "Special audience characteristics": "3"}
    field_map = {
        'target_audience_note': 'a',
        'materials_specified': '3',
        'source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('target_audience_note')
        ),
        '3': value.get('materials_specified'),
        'b': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('522', '^geographic_coverage_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {"Geographic coverage": "_", "No display constant generated": "8"}
    field_map = {
        'geographic_coverage_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_coverage_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('524', '^preferred_citation_of_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preferred_citation_of_described_materials_note(self, key, value):
    """Reverse - Preferred Citation of Described Materials Note."""
    indicator_map1 = {"Cite as": "_", "No display constant generated": "8"}
    field_map = {
        'preferred_citation_of_described_materials_note': 'a',
        'materials_specified': '3',
        'source_of_schema_used': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('preferred_citation_of_described_materials_note'),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_schema_used'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('525', '^supplement_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    field_map = {
        'supplement_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('supplement_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('526', '^study_program_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_study_program_information_note(self, key, value):
    """Reverse - Study Program Information Note."""
    indicator_map1 = {"No display constant generated": "8", "Reading program": "0"}
    field_map = {
        'public_note': 'z',
        'program_name': 'a',
        'field_link_and_sequence_number': '8',
        'nonpublic_note': 'x',
        'reading_level': 'c',
        'institution_to_which_field_applies': '5',
        'title_point_value': 'd',
        'display_text': 'i',
        'interest_level': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'a': value.get('program_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'c': value.get('reading_level'),
        '5': value.get('institution_to_which_field_applies'),
        'd': value.get('title_point_value'),
        'i': value.get('display_text'),
        'b': value.get('interest_level'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('530', '^additional_physical_form_available_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    field_map = {
        'additional_physical_form_available_note': 'a',
        'materials_specified': '3',
        'uniform_resource_identifier': 'u',
        'availability_conditions': 'c',
        'order_number': 'd',
        'availability_source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('additional_physical_form_available_note'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('availability_conditions'),
        'd': value.get('order_number'),
        'b': value.get('availability_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('533', '^reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_reproduction_note(self, key, value):
    """Reverse - Reproduction Note."""
    field_map = {
        'agency_responsible_for_reproduction': 'c',
        'series_statement_of_reproduction': 'f',
        'fixed_length_data_elements_of_reproduction': '7',
        'date_of_reproduction': 'd',
        'linkage': '6',
        'materials_specified': '3',
        'type_of_reproduction': 'a',
        'field_link_and_sequence_number': '8',
        'note_about_reproduction': 'n',
        'physical_description_of_reproduction': 'e',
        'institution_to_which_field_applies': '5',
        'dates_and_or_sequential_designation_of_issues_reproduced': 'm',
        'place_of_reproduction': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        'd': value.get('date_of_reproduction'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('type_of_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
        ),
        'e': value.get('physical_description_of_reproduction'),
        '5': value.get('institution_to_which_field_applies'),
        'm': utils.reverse_force_list(
            value.get('dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('534', '^original_version_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_version_note(self, key, value):
    """Reverse - Original Version Note."""
    field_map = {
        'publication_distribution_of_original': 'c',
        'materials_specified': '3',
        'international_standard_serial_number': 'x',
        'title_statement_of_original': 't',
        'international_standard_book_number': 'z',
        'linkage': '6',
        'series_statement_of_original': 'f',
        'location_of_original': 'l',
        'main_entry_of_original': 'a',
        'field_link_and_sequence_number': '8',
        'note_about_original': 'n',
        'physical_description_of_original': 'e',
        'material_specific_details': 'm',
        'key_title_of_original': 'k',
        'edition_statement_of_original': 'b',
        'other_resource_identifier': 'o',
        'introductory_phrase': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('publication_distribution_of_original'),
        '3': value.get('materials_specified'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        't': value.get('title_statement_of_original'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        'l': value.get('location_of_original'),
        'a': value.get('main_entry_of_original'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
        'e': value.get('physical_description_of_original'),
        'm': value.get('material_specific_details'),
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'b': value.get('edition_statement_of_original'),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        'p': value.get('introductory_phrase'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('535', '^location_of_originals_duplicates_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_originals_duplicates_note(self, key, value):
    """Reverse - Location of Originals/Duplicates Note."""
    indicator_map1 = {"Holder of duplicates": "2", "Holder of originals": "1"}
    field_map = {
        'custodian': 'a',
        'materials_specified': '3',
        'country': 'c',
        'telecommunications_address': 'd',
        'postal_address': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'repository_location_code': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('custodian'),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': value.get('repository_location_code'),
        '$ind1': indicator_map1.get(value.get('custodial_role'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('536', '^funding_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_funding_information_note(self, key, value):
    """Reverse - Funding Information Note."""
    field_map = {
        'text_of_note': 'a',
        'field_link_and_sequence_number': '8',
        'program_element_number': 'e',
        'work_unit_number': 'h',
        'grant_number': 'c',
        'undifferentiated_number': 'd',
        'contract_number': 'b',
        'linkage': '6',
        'project_number': 'f',
        'task_number': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('text_of_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        'c': utils.reverse_force_list(
            value.get('grant_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        '6': value.get('linkage'),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'g': utils.reverse_force_list(
            value.get('task_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('538', '^system_details_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_note(self, key, value):
    """Reverse - System Details Note."""
    field_map = {
        'system_details_note': 'a',
        'materials_specified': '3',
        'uniform_resource_identifier': 'u',
        'institution_to_which_field_applies': '5',
        'display_text': 'i',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('system_details_note'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': value.get('display_text'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('540', '^terms_governing_use_and_reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_terms_governing_use_and_reproduction_note(self, key, value):
    """Reverse - Terms Governing Use and Reproduction Note."""
    field_map = {
        'terms_governing_use_and_reproduction': 'a',
        'materials_specified': '3',
        'authorization': 'c',
        'uniform_resource_identifier': 'u',
        'institution_to_which_field_applies': '5',
        'authorized_users': 'd',
        'jurisdiction': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('terms_governing_use_and_reproduction'),
        '3': value.get('materials_specified'),
        'c': value.get('authorization'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'd': value.get('authorized_users'),
        'b': value.get('jurisdiction'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('541', '^immediate_source_of_acquisition_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_immediate_source_of_acquisition_note(self, key, value):
    """Reverse - Immediate Source of Acquisition Note."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'method_of_acquisition': 'c',
        'owner': 'f',
        'purchase_price': 'h',
        'date_of_acquisition': 'd',
        'linkage': '6',
        'materials_specified': '3',
        'source_of_acquisition': 'a',
        'field_link_and_sequence_number': '8',
        'extent': 'n',
        'accession_number': 'e',
        'institution_to_which_field_applies': '5',
        'address': 'b',
        'type_of_unit': 'o',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('method_of_acquisition'),
        'f': value.get('owner'),
        'h': value.get('purchase_price'),
        'd': value.get('date_of_acquisition'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('source_of_acquisition'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'e': value.get('accession_number'),
        '5': value.get('institution_to_which_field_applies'),
        'b': value.get('address'),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('542', '^information_relating_to_copyright_status$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_relating_to_copyright_status(self, key, value):
    """Reverse - Information Relating to Copyright Status."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'corporate_creator': 'c',
        'copyright_statement': 'f',
        'copyright_renewal_date': 'h',
        'uniform_resource_identifier': 'u',
        'copyright_holder': 'd',
        'linkage': '6',
        'materials_specified': '3',
        'copyright_status': 'l',
        'source_of_information': 's',
        'personal_creator': 'a',
        'field_link_and_sequence_number': '8',
        'publication_status': 'm',
        'personal_creator_death_date': 'b',
        'copyright_date': 'g',
        'jurisdiction_of_copyright_assessment': 'r',
        'creation_date': 'j',
        'supplying_agency': 'q',
        'note': 'n',
        'copyright_holder_contact_information': 'e',
        'publisher': 'k',
        'publication_date': 'i',
        'research_date': 'o',
        'country_of_publication_or_creation': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('corporate_creator'),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'l': value.get('copyright_status'),
        's': value.get('source_of_information'),
        'a': value.get('personal_creator'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('publication_status'),
        'b': value.get('personal_creator_death_date'),
        'g': value.get('copyright_date'),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        'j': value.get('creation_date'),
        'q': value.get('supplying_agency'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'i': value.get('publication_date'),
        'o': value.get('research_date'),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('544', '^location_of_other_archival_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {"Associated materials": "0", "No information provided": "_", "Related materials": "1"}
    field_map = {
        'custodian': 'a',
        'materials_specified': '3',
        'note': 'n',
        'provenance': 'e',
        'country': 'c',
        'title': 'd',
        'address': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('custodian')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'e': utils.reverse_force_list(
            value.get('provenance')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('relationship'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('545', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {"Administrative history": "1", "Biographical sketch": "0", "No information provided": "_"}
    field_map = {
        'biographical_or_historical_data': 'a',
        'field_link_and_sequence_number': '8',
        'expansion': 'b',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('biographical_or_historical_data'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('expansion'),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_data'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('546', '^language_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_note(self, key, value):
    """Reverse - Language Note."""
    field_map = {
        'language_note': 'a',
        'materials_specified': '3',
        'information_code_or_alphabet': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('language_note'),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('547', '^former_title_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title_complexity_note(self, key, value):
    """Reverse - Former Title Complexity Note."""
    field_map = {
        'former_title_complexity_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('former_title_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('550', '^issuing_body_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issuing_body_note(self, key, value):
    """Reverse - Issuing Body Note."""
    field_map = {
        'issuing_body_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('issuing_body_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('552', '^entity_and_attribute_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_entity_and_attribute_information_note(self, key, value):
    """Reverse - Entity and Attribute Information Note."""
    field_map = {
        'attribute_label': 'c',
        'enumerated_domain_value_definition_and_source': 'f',
        'codeset_name_and_source': 'h',
        'attribute_definition_and_source': 'd',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'attribute_value_accuracy': 'l',
        'display_note': 'z',
        'entity_type_label': 'a',
        'field_link_and_sequence_number': '8',
        'attribute_measurement_frequency': 'n',
        'enumerated_domain_value': 'e',
        'beginning_and_ending_date_of_attribute_values': 'k',
        'attribute_value_accuracy_explanation': 'm',
        'attribute_units_of_measurement_and_resolution': 'j',
        'unrepresentable_domain': 'i',
        'entity_type_definition_and_source': 'b',
        'entity_and_attribute_overview': 'o',
        'range_domain_minimum_and_maximum': 'g',
        'entity_and_attribute_detail_citation': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('attribute_label'),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'h': value.get('codeset_name_and_source'),
        'd': value.get('attribute_definition_and_source'),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'l': value.get('attribute_value_accuracy'),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'a': value.get('entity_type_label'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': value.get('attribute_measurement_frequency'),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'm': value.get('attribute_value_accuracy_explanation'),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'i': value.get('unrepresentable_domain'),
        'b': value.get('entity_type_definition_and_source'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        'g': value.get('range_domain_minimum_and_maximum'),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('555', '^cumulative_index_finding_aids_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {"Finding aids": "0", "Indexes": "_", "No display constant generated": "8"}
    field_map = {
        'cumulative_index_finding_aids_note': 'a',
        'materials_specified': '3',
        'uniform_resource_identifier': 'u',
        'degree_of_control': 'c',
        'bibliographic_reference': 'd',
        'availability_source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('cumulative_index_finding_aids_note'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('degree_of_control'),
        'd': value.get('bibliographic_reference'),
        'b': utils.reverse_force_list(
            value.get('availability_source')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('556', '^information_about_documentation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {"Documentation": "_", "No display constant generated": "8"}
    field_map = {
        'international_standard_book_number': 'z',
        'information_about_documentation_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('information_about_documentation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('561', '^ownership_and_custodial_history$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'history': 'a',
        'materials_specified': '3',
        'uniform_resource_identifier': 'u',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('history'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('562', '^copy_and_version_identification_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copy_and_version_identification_note(self, key, value):
    """Reverse - Copy and Version Identification Note."""
    field_map = {
        'identifying_markings': 'a',
        'materials_specified': '3',
        'number_of_copies': 'e',
        'version_identification': 'c',
        'institution_to_which_field_applies': '5',
        'presentation_format': 'd',
        'copy_identification': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('identifying_markings')
        ),
        '3': value.get('materials_specified'),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'd': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        'b': utils.reverse_force_list(
            value.get('copy_identification')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('563', '^binding_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_binding_information(self, key, value):
    """Reverse - Binding Information."""
    field_map = {
        'binding_note': 'a',
        'materials_specified': '3',
        'uniform_resource_identifier': 'u',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('binding_note'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('565', '^case_file_characteristics_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_case_file_characteristics_note(self, key, value):
    """Reverse - Case File Characteristics Note."""
    indicator_map1 = {"Case file characteristics": "0", "File size": "_", "No display constant generated": "8"}
    field_map = {
        'number_of_cases_variables': 'a',
        'materials_specified': '3',
        'filing_scheme_or_code': 'e',
        'unit_of_analysis': 'c',
        'universe_of_data': 'd',
        'name_of_variable': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number_of_cases_variables'),
        '3': value.get('materials_specified'),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')
        ),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')
        ),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_variable')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('567', '^methodology_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_methodology_note(self, key, value):
    """Reverse - Methodology Note."""
    indicator_map1 = {"Methodology": "_", "No display constant generated": "8"}
    field_map = {
        'methodology_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('methodology_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('580', '^linking_entry_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    field_map = {
        'linking_entry_complexity_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('linking_entry_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('581', '^publications_about_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publications_about_described_materials_note(self, key, value):
    """Reverse - Publications About Described Materials Note."""
    indicator_map1 = {"No display constant generated": "8", "Publications": "_"}
    field_map = {
        'international_standard_book_number': 'z',
        'publications_about_described_materials_note': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('publications_about_described_materials_note'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('583', '^action_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'time_date_of_action': 'c',
        'authorization': 'f',
        'jurisdiction': 'h',
        'uniform_resource_identifier': 'u',
        'action_interval': 'd',
        'extent': 'n',
        'linkage': '6',
        'materials_specified': '3',
        'nonpublic_note': 'x',
        'status': 'l',
        'public_note': 'z',
        'action': 'a',
        'field_link_and_sequence_number': '8',
        'source_of_term': '2',
        'contingency_for_action': 'e',
        'institution_to_which_field_applies': '5',
        'site_of_action': 'j',
        'method_of_action': 'i',
        'action_identification': 'b',
        'type_of_unit': 'o',
        'action_agent': 'k',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'a': value.get('action'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_term'),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('584', '^accumulation_and_frequency_of_use_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_accumulation_and_frequency_of_use_note(self, key, value):
    """Reverse - Accumulation and Frequency of Use Note."""
    field_map = {
        'accumulation': 'a',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'frequency_of_use': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('585', '^exhibitions_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_exhibitions_note(self, key, value):
    """Reverse - Exhibitions Note."""
    field_map = {
        'exhibitions_note': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('exhibitions_note'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('586', '^awards_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_awards_note(self, key, value):
    """Reverse - Awards Note."""
    indicator_map1 = {"Awards": "_", "No display constant generated": "8"}
    field_map = {
        'awards_note': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('awards_note'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('588', '^source_of_description_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    indicator_map1 = {"Latest issue consulted": "1", "No information provided": "_", "Source of description": "0"}
    field_map = {
        'source_of_description_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('source_of_description_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }
