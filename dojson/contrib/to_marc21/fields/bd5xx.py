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
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'general_note': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('general_note'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('501', '^with_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_with_note(self, key, value):
    """Reverse - With Note."""
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'with_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('with_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('502', '^dissertation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dissertation_note(self, key, value):
    """Reverse - Dissertation Note."""
    field_map = {
        'degree_type': 'b',
        'dissertation_identifier': 'o',
        'year_degree_granted': 'd',
        'dissertation_note': 'a',
        'field_link_and_sequence_number': '8',
        'name_of_granting_institution': 'c',
        'linkage': '6',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('degree_type'),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        'd': value.get('year_degree_granted'),
        'a': value.get('dissertation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('name_of_granting_institution'),
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
        'number_of_references': 'b',
        'linkage': '6',
        'bibliography_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('number_of_references'),
        '6': value.get('linkage'),
        'a': value.get('bibliography_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('505', '^formatted_contents_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_formatted_contents_note(self, key, value):
    """Reverse - Formatted Contents Note."""
    indicator_map1 = {
        "Contents": "0",
        "Incomplete contents": "1",
        "No display constant generated": "8",
        "Partial contents": "2"}
    indicator_map2 = {"Basic": "_", "Enhanced": "0"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'formatted_contents_note': 'a',
        'statement_of_responsibility': 'r',
        'title': 't',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('level_of_content_designation'), '7') != '7':
        try:
            order.remove(field_map.get('level_of_content_designation'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('formatted_contents_note'),
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')
        ),
        't': utils.reverse_force_list(
            value.get('title')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
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
    indicator_map1 = {
        "No information provided": "_",
        "No restrictions": "0",
        "Restrictions apply": "1"}
    field_map = {
        'jurisdiction': 'b',
        'source_of_term': '2',
        'authorized_users': 'd',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'terms_governing_access': 'a',
        'physical_access_provisions': 'c',
        'standardized_terminology_for_access_restriction': 'f',
        'linkage': '6',
        'authorization': 'e',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('restriction'), '7') != '7':
        try:
            order.remove(field_map.get('restriction'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        '2': value.get('source_of_term'),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': value.get('terms_governing_access'),
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('restriction'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('507', '^scale_note_for_graphic_material$')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    field_map = {
        'remainder_of_scale_note': 'b',
        'linkage': '6',
        'representative_fraction_of_scale_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('remainder_of_scale_note'),
        '6': value.get('linkage'),
        'a': value.get('representative_fraction_of_scale_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('508', '^creation_production_credits_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creation_production_credits_note(self, key, value):
    """Reverse - Creation/Production Credits Note."""
    field_map = {
        'linkage': '6',
        'creation_production_credits_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('creation_production_credits_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('510', '^citation_references_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_citation_references_note(self, key, value):
    """Reverse - Citation/References Note."""
    indicator_map1 = {
        "Coverage complete": "1",
        "Coverage is selective": "2",
        "Coverage unknown": "0",
        "Location in source given": "4",
        "Location in source not given": "3"}
    field_map = {
        'coverage_of_source': 'b',
        'international_standard_serial_number': 'x',
        'name_of_source': 'a',
        'field_link_and_sequence_number': '8',
        'location_within_source': 'c',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('coverage_location_in_source'), '7') != '7':
        try:
            order.remove(field_map.get('coverage_location_in_source'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('coverage_of_source'),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('name_of_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('location_within_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'linkage': '6',
        'participant_or_performer_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('participant_or_performer_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('513', '^type_of_report_and_period_covered_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    field_map = {
        'period_covered': 'b',
        'linkage': '6',
        'type_of_report': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('period_covered'),
        '6': value.get('linkage'),
        'a': value.get('type_of_report'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('514', '^data_quality_note$')
@utils.filter_values
def reverse_data_quality_note(self, key, value):
    """Reverse - Data Quality Note."""
    field_map = {
        'attribute_accuracy_value': 'b',
        'vertical_positional_accuracy_explanation': 'k',
        'display_note': 'z',
        'logical_consistency_report': 'd',
        'field_link_and_sequence_number': '8',
        'horizontal_position_accuracy_explanation': 'h',
        'linkage': '6',
        'cloud_cover': 'm',
        'vertical_positional_accuracy_value': 'j',
        'vertical_positional_accuracy_report': 'i',
        'attribute_accuracy_report': 'a',
        'attribute_accuracy_explanation': 'c',
        'horizontal_position_accuracy_report': 'f',
        'uniform_resource_identifier': 'u',
        'completeness_report': 'e',
        'horizontal_position_accuracy_value': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'd': value.get('logical_consistency_report'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        '6': value.get('linkage'),
        'm': value.get('cloud_cover'),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'i': value.get('vertical_positional_accuracy_report'),
        'a': value.get('attribute_accuracy_report'),
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        'f': value.get('horizontal_position_accuracy_report'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'e': value.get('completeness_report'),
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
        'linkage': '6',
        'numbering_peculiarities_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('numbering_peculiarities_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('516', '^type_of_computer_file_or_data_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_computer_file_or_data_note(self, key, value):
    """Reverse - Type of Computer File or Data Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Type of file": "_"}
    field_map = {
        'linkage': '6',
        'type_of_computer_file_or_data_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('type_of_computer_file_or_data_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('518', '^date_time_and_place_of_an_event_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    field_map = {
        'other_event_information': 'o',
        'source_of_term': '2',
        'date_of_event': 'd',
        'date_time_and_place_of_an_event_note': 'a',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'linkage': '6',
        'place_of_event': 'p',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        'a': value.get('date_time_and_place_of_an_event_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('520', '^summary$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {
        "Abstract": "3",
        "Content advice": "4",
        "No display constant generated": "8",
        "Review": "1",
        "Scope and content": "2",
        "Subject": "0",
        "Summary": "_"}
    field_map = {
        'expansion_of_summary_note': 'b',
        'source': '2',
        'summary': 'a',
        'field_link_and_sequence_number': '8',
        'assigning_source': 'c',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('expansion_of_summary_note'),
        '2': value.get('source'),
        'a': value.get('summary'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('assigning_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('521', '^target_audience_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {
        "Audience": "_",
        "Interest age level": "1",
        "Interest grade level": "2",
        "Motivation/interest level": "4",
        "No display constant generated": "8",
        "Reading grade level": "0",
        "Special audience characteristics": "3"}
    field_map = {
        'source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'target_audience_note': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('target_audience_note')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('522', '^geographic_coverage_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {
        "Geographic coverage": "_",
        "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'geographic_coverage_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('geographic_coverage_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'source_of_schema_used': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'preferred_citation_of_described_materials_note': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_schema_used'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('preferred_citation_of_described_materials_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('525', '^supplement_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    field_map = {
        'linkage': '6',
        'supplement_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('supplement_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('526', '^study_program_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_study_program_information_note(self, key, value):
    """Reverse - Study Program Information Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Reading program": "0"}
    field_map = {
        'interest_level': 'b',
        'display_text': 'i',
        'nonpublic_note': 'x',
        'title_point_value': 'd',
        'program_name': 'a',
        'field_link_and_sequence_number': '8',
        'reading_level': 'c',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'public_note': 'z',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('interest_level'),
        'i': value.get('display_text'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'd': value.get('title_point_value'),
        'a': value.get('program_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('reading_level'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('530', '^additional_physical_form_available_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    field_map = {
        'availability_source': 'b',
        'order_number': 'd',
        'additional_physical_form_available_note': 'a',
        'field_link_and_sequence_number': '8',
        'availability_conditions': 'c',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('availability_source'),
        'd': value.get('order_number'),
        'a': value.get('additional_physical_form_available_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('availability_conditions'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('533', '^reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_reproduction_note(self, key, value):
    """Reverse - Reproduction Note."""
    field_map = {
        'place_of_reproduction': 'b',
        'dates_and_or_sequential_designation_of_issues_reproduced': 'm',
        'date_of_reproduction': 'd',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'fixed_length_data_elements_of_reproduction': '7',
        'type_of_reproduction': 'a',
        'agency_responsible_for_reproduction': 'c',
        'series_statement_of_reproduction': 'f',
        'linkage': '6',
        'physical_description_of_reproduction': 'e',
        'materials_specified': '3',
        'note_about_reproduction': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        'm': utils.reverse_force_list(
            value.get('dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        'd': value.get('date_of_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        'a': value.get('type_of_reproduction'),
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        '6': value.get('linkage'),
        'e': value.get('physical_description_of_reproduction'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
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
        'edition_statement_of_original': 'b',
        'key_title_of_original': 'k',
        'international_standard_serial_number': 'x',
        'location_of_original': 'l',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'introductory_phrase': 'p',
        'material_specific_details': 'm',
        'other_resource_identifier': 'o',
        'title_statement_of_original': 't',
        'main_entry_of_original': 'a',
        'international_standard_book_number': 'z',
        'publication_distribution_of_original': 'c',
        'series_statement_of_original': 'f',
        'physical_description_of_original': 'e',
        'materials_specified': '3',
        'note_about_original': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('edition_statement_of_original'),
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        'l': value.get('location_of_original'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'p': value.get('introductory_phrase'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        't': value.get('title_statement_of_original'),
        'a': value.get('main_entry_of_original'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'c': value.get('publication_distribution_of_original'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        'e': value.get('physical_description_of_original'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
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
        'postal_address': 'b',
        'telecommunications_address': 'd',
        'custodian': 'a',
        'field_link_and_sequence_number': '8',
        'country': 'c',
        'linkage': '6',
        'materials_specified': '3',
        'repository_location_code': 'g',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('custodial_role'), '7') != '7':
        try:
            order.remove(field_map.get('custodial_role'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        'a': value.get('custodian'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'contract_number': 'b',
        'undifferentiated_number': 'd',
        'text_of_note': 'a',
        'field_link_and_sequence_number': '8',
        'program_element_number': 'e',
        'grant_number': 'c',
        'project_number': 'f',
        'work_unit_number': 'h',
        'linkage': '6',
        'task_number': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'a': value.get('text_of_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'c': utils.reverse_force_list(
            value.get('grant_number')
        ),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        '6': value.get('linkage'),
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
        'display_text': 'i',
        'system_details_note': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': value.get('display_text'),
        'a': value.get('system_details_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('540', '^terms_governing_use_and_reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_terms_governing_use_and_reproduction_note(self, key, value):
    """Reverse - Terms Governing Use and Reproduction Note."""
    field_map = {
        'jurisdiction': 'b',
        'authorized_users': 'd',
        'terms_governing_use_and_reproduction': 'a',
        'field_link_and_sequence_number': '8',
        'authorization': 'c',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('jurisdiction'),
        'd': value.get('authorized_users'),
        'a': value.get('terms_governing_use_and_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('authorization'),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('541', '^immediate_source_of_acquisition_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_immediate_source_of_acquisition_note(self, key, value):
    """Reverse - Immediate Source of Acquisition Note."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    field_map = {
        'address': 'b',
        'date_of_acquisition': 'd',
        'field_link_and_sequence_number': '8',
        'purchase_price': 'h',
        'institution_to_which_field_applies': '5',
        'type_of_unit': 'o',
        'source_of_acquisition': 'a',
        'method_of_acquisition': 'c',
        'owner': 'f',
        'linkage': '6',
        'accession_number': 'e',
        'materials_specified': '3',
        'extent': 'n',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('privacy'), '7') != '7':
        try:
            order.remove(field_map.get('privacy'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('address'),
        'd': value.get('date_of_acquisition'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('purchase_price'),
        '5': value.get('institution_to_which_field_applies'),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'a': value.get('source_of_acquisition'),
        'c': value.get('method_of_acquisition'),
        'f': value.get('owner'),
        '6': value.get('linkage'),
        'e': value.get('accession_number'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('542', '^information_relating_to_copyright_status$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_relating_to_copyright_status(self, key, value):
    """Reverse - Information Relating to Copyright Status."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    field_map = {
        'personal_creator_death_date': 'b',
        'publication_status': 'm',
        'copyright_status': 'l',
        'field_link_and_sequence_number': '8',
        'publication_date': 'i',
        'research_date': 'o',
        'supplying_agency': 'q',
        'copyright_date': 'g',
        'source_of_information': 's',
        'publisher': 'k',
        'uniform_resource_identifier': 'u',
        'copyright_holder': 'd',
        'copyright_renewal_date': 'h',
        'copyright_holder_contact_information': 'e',
        'country_of_publication_or_creation': 'p',
        'creation_date': 'j',
        'personal_creator': 'a',
        'jurisdiction_of_copyright_assessment': 'r',
        'corporate_creator': 'c',
        'copyright_statement': 'f',
        'linkage': '6',
        'materials_specified': '3',
        'note': 'n',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('privacy'), '7') != '7':
        try:
            order.remove(field_map.get('privacy'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('personal_creator_death_date'),
        'm': value.get('publication_status'),
        'l': value.get('copyright_status'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': value.get('publication_date'),
        'o': value.get('research_date'),
        'q': value.get('supplying_agency'),
        'g': value.get('copyright_date'),
        's': value.get('source_of_information'),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        'j': value.get('creation_date'),
        'a': value.get('personal_creator'),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        'c': value.get('corporate_creator'),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('544', '^location_of_other_archival_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {
        "Associated materials": "0",
        "No information provided": "_",
        "Related materials": "1"}
    field_map = {
        'address': 'b',
        'title': 'd',
        'custodian': 'a',
        'field_link_and_sequence_number': '8',
        'provenance': 'e',
        'country': 'c',
        'linkage': '6',
        'materials_specified': '3',
        'note': 'n',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('relationship'), '7') != '7':
        try:
            order.remove(field_map.get('relationship'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        'a': utils.reverse_force_list(
            value.get('custodian')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('provenance')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '$ind1': indicator_map1.get(value.get('relationship'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('545', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {
        "Administrative history": "1",
        "Biographical sketch": "0",
        "No information provided": "_"}
    field_map = {
        'expansion': 'b',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'biographical_or_historical_data': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_data'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_data'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('expansion'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'a': value.get('biographical_or_historical_data'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'information_code_or_alphabet': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'language_note': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('language_note'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('547', '^former_title_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title_complexity_note(self, key, value):
    """Reverse - Former Title Complexity Note."""
    field_map = {
        'linkage': '6',
        'former_title_complexity_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('former_title_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('550', '^issuing_body_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issuing_body_note(self, key, value):
    """Reverse - Issuing Body Note."""
    field_map = {
        'linkage': '6',
        'issuing_body_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('issuing_body_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('552', '^entity_and_attribute_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_entity_and_attribute_information_note(self, key, value):
    """Reverse - Entity and Attribute Information Note."""
    field_map = {
        'entity_type_definition_and_source': 'b',
        'beginning_and_ending_date_of_attribute_values': 'k',
        'display_note': 'z',
        'uniform_resource_identifier': 'u',
        'attribute_definition_and_source': 'd',
        'attribute_value_accuracy': 'l',
        'field_link_and_sequence_number': '8',
        'codeset_name_and_source': 'h',
        'linkage': '6',
        'attribute_value_accuracy_explanation': 'm',
        'attribute_units_of_measurement_and_resolution': 'j',
        'unrepresentable_domain': 'i',
        'entity_and_attribute_overview': 'o',
        'entity_type_label': 'a',
        'attribute_label': 'c',
        'enumerated_domain_value_definition_and_source': 'f',
        'attribute_measurement_frequency': 'n',
        'enumerated_domain_value': 'e',
        'entity_and_attribute_detail_citation': 'p',
        'range_domain_minimum_and_maximum': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('entity_type_definition_and_source'),
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'd': value.get('attribute_definition_and_source'),
        'l': value.get('attribute_value_accuracy'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('codeset_name_and_source'),
        '6': value.get('linkage'),
        'm': value.get('attribute_value_accuracy_explanation'),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'i': value.get('unrepresentable_domain'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        'a': value.get('entity_type_label'),
        'c': value.get('attribute_label'),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'n': value.get('attribute_measurement_frequency'),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        'g': value.get('range_domain_minimum_and_maximum'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('555', '^cumulative_index_finding_aids_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        "Finding aids": "0",
        "Indexes": "_",
        "No display constant generated": "8"}
    field_map = {
        'availability_source': 'b',
        'bibliographic_reference': 'd',
        'cumulative_index_finding_aids_note': 'a',
        'field_link_and_sequence_number': '8',
        'degree_of_control': 'c',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('availability_source')
        ),
        'd': value.get('bibliographic_reference'),
        'a': value.get('cumulative_index_finding_aids_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('degree_of_control'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('556', '^information_about_documentation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {
        "Documentation": "_",
        "No display constant generated": "8"}
    field_map = {
        'international_standard_book_number': 'z',
        'linkage': '6',
        'information_about_documentation_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('information_about_documentation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('561', '^ownership_and_custodial_history$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    field_map = {
        'history': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('privacy'), '7') != '7':
        try:
            order.remove(field_map.get('privacy'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('history'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('562', '^copy_and_version_identification_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copy_and_version_identification_note(self, key, value):
    """Reverse - Copy and Version Identification Note."""
    field_map = {
        'copy_identification': 'b',
        'number_of_copies': 'e',
        'presentation_format': 'd',
        'identifying_markings': 'a',
        'field_link_and_sequence_number': '8',
        'version_identification': 'c',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('copy_identification')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        'd': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        'a': utils.reverse_force_list(
            value.get('identifying_markings')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('binding_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('565', '^case_file_characteristics_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_case_file_characteristics_note(self, key, value):
    """Reverse - Case File Characteristics Note."""
    indicator_map1 = {
        "Case file characteristics": "0",
        "File size": "_",
        "No display constant generated": "8"}
    field_map = {
        'name_of_variable': 'b',
        'universe_of_data': 'd',
        'number_of_cases_variables': 'a',
        'field_link_and_sequence_number': '8',
        'filing_scheme_or_code': 'e',
        'unit_of_analysis': 'c',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('name_of_variable')
        ),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')
        ),
        'a': value.get('number_of_cases_variables'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')
        ),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'linkage': '6',
        'methodology_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('methodology_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('580', '^linking_entry_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    field_map = {
        'linkage': '6',
        'linking_entry_complexity_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('linking_entry_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('581', '^publications_about_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publications_about_described_materials_note(self, key, value):
    """Reverse - Publications About Described Materials Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Publications": "_"}
    field_map = {
        'international_standard_book_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'publications_about_described_materials_note': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('publications_about_described_materials_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('583', '^action_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    field_map = {
        'action_identification': 'b',
        'action_agent': 'k',
        'nonpublic_note': 'x',
        'source_of_term': '2',
        'action_interval': 'd',
        'status': 'l',
        'field_link_and_sequence_number': '8',
        'jurisdiction': 'h',
        'institution_to_which_field_applies': '5',
        'public_note': 'z',
        'site_of_action': 'j',
        'method_of_action': 'i',
        'type_of_unit': 'o',
        'action': 'a',
        'uniform_resource_identifier': 'u',
        'time_date_of_action': 'c',
        'authorization': 'f',
        'linkage': '6',
        'contingency_for_action': 'e',
        'materials_specified': '3',
        'extent': 'n',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('privacy'), '7') != '7':
        try:
            order.remove(field_map.get('privacy'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        '2': value.get('source_of_term'),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'a': value.get('action'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('extent')
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
        'frequency_of_use': 'b',
        'accumulation': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('585', '^exhibitions_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_exhibitions_note(self, key, value):
    """Reverse - Exhibitions Note."""
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'exhibitions_note': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('exhibitions_note'),
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
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'awards_note': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('awards_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('588', '^source_of_description_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    indicator_map1 = {
        "Latest issue consulted": "1",
        "No information provided": "_",
        "Source of description": "0"}
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'source_of_description_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('source_of_description_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }
