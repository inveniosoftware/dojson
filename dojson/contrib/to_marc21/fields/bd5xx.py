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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('general_note'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('with_note'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
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
        'dissertation_note': 'a',
        'degree_type': 'b',
        'name_of_granting_institution': 'c',
        'year_degree_granted': 'd',
        'miscellaneous_information': 'g',
        'dissertation_identifier': 'o',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('dissertation_note'),
        'b': value.get('degree_type'),
        'c': value.get('name_of_granting_institution'),
        'd': value.get('year_degree_granted'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'number_of_references': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('bibliography_note'),
        'b': value.get('number_of_references'),
        '6': value.get('linkage'),
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
        'Contents': '0',
        'Incomplete contents': '1',
        'Partial contents': '2',
        'No display constant generated': '8',
    }

    indicator_map2 = {
        'Basic': '_',
        'Enhanced': '0',
    }

    field_map = {
        'formatted_contents_note': 'a',
        'miscellaneous_information': 'g',
        'statement_of_responsibility': 'r',
        'title': 't',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('formatted_contents_note'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')),
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')),
        't': utils.reverse_force_list(
            value.get('title')),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('level_of_content_designation'),
            '_'),
    }


@to_marc21.over('506', '^restrictions_on_access_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_restrictions_on_access_note(self, key, value):
    """Reverse - Restrictions on Access Note."""
    indicator_map1 = {
        'No information provided': '_',
        'No restrictions': '0',
        'Restrictions apply': '1',
    }

    field_map = {
        'terms_governing_access': 'a',
        'jurisdiction': 'b',
        'physical_access_provisions': 'c',
        'authorized_users': 'd',
        'authorization': 'e',
        'standardized_terminology_for_access_restriction': 'f',
        'uniform_resource_identifier': 'u',
        'source_of_term': '2',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('terms_governing_access'),
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '2': value.get('source_of_term'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('restriction'), '_'),
    }


@to_marc21.over('507', '^scale_note_for_graphic_material$')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    field_map = {
        'representative_fraction_of_scale_note': 'a',
        'remainder_of_scale_note': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('representative_fraction_of_scale_note'),
        'b': value.get('remainder_of_scale_note'),
        '6': value.get('linkage'),
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
        'creation_production_credits_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('creation_production_credits_note'),
        '6': value.get('linkage'),
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
        'Coverage unknown': '0',
        'Coverage complete': '1',
        'Coverage is selective': '2',
        'Location in source not given': '3',
        'Location in source given': '4',
    }

    field_map = {
        'name_of_source': 'a',
        'coverage_of_source': 'b',
        'location_within_source': 'c',
        'uniform_resource_identifier': 'u',
        'international_standard_serial_number': 'x',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('name_of_source'),
        'b': value.get('coverage_of_source'),
        'c': value.get('location_within_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        'x': value.get('international_standard_serial_number'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('coverage_location_in_source'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('511', '^participant_or_performer_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_participant_or_performer_note(self, key, value):
    """Reverse - Participant or Performer Note."""
    indicator_map1 = {
        'Cast': '1',
        'No display constant generated': '0',
    }

    field_map = {
        'participant_or_performer_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('participant_or_performer_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('513', '^type_of_report_and_period_covered_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    field_map = {
        'type_of_report': 'a',
        'period_covered': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_report'),
        'b': value.get('period_covered'),
        '6': value.get('linkage'),
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
        'attribute_accuracy_report': 'a',
        'attribute_accuracy_value': 'b',
        'attribute_accuracy_explanation': 'c',
        'logical_consistency_report': 'd',
        'completeness_report': 'e',
        'horizontal_position_accuracy_report': 'f',
        'horizontal_position_accuracy_value': 'g',
        'horizontal_position_accuracy_explanation': 'h',
        'vertical_positional_accuracy_report': 'i',
        'vertical_positional_accuracy_value': 'j',
        'vertical_positional_accuracy_explanation': 'k',
        'cloud_cover': 'm',
        'uniform_resource_identifier': 'u',
        'display_note': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('attribute_accuracy_report'),
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        'd': value.get('logical_consistency_report'),
        'e': value.get('completeness_report'),
        'f': value.get('horizontal_position_accuracy_report'),
        'g': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_value')
        ),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        'i': value.get('vertical_positional_accuracy_report'),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'm': value.get('cloud_cover'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'linkage': '6',
        'field_link_and_sequence_number': '8',
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
    indicator_map1 = {
        'Type of file': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'type_of_computer_file_or_data_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_computer_file_or_data_note'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('518', '^date_time_and_place_of_an_event_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    field_map = {
        'date_time_and_place_of_an_event_note': 'a',
        'date_of_event': 'd',
        'other_event_information': 'o',
        'place_of_event': 'p',
        'record_control_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('date_time_and_place_of_an_event_note'),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('520', '^summary$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {
        'Summary': '_',
        'Subject': '0',
        'Review': '1',
        'Scope and content': '2',
        'Abstract': '3',
        'Content advice': '4',
        'No display constant generated': '8',
    }

    field_map = {
        'summary': 'a',
        'expansion_of_summary_note': 'b',
        'assigning_source': 'c',
        'uniform_resource_identifier': 'u',
        'source': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('summary'),
        'b': value.get('expansion_of_summary_note'),
        'c': value.get('assigning_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '2': value.get('source'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('521', '^target_audience_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {
        'Audience': '_',
        'Interest age level': '1',
        'Interest grade level': '2',
        'Motivation/interest level': '4',
        'No display constant generated': '8',
        'Reading grade level': '0',
        'Special audience characteristics': '3',
    }

    field_map = {
        'target_audience_note': 'a',
        'source': 'b',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('target_audience_note')),
        'b': value.get('source'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('522', '^geographic_coverage_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {
        'Geographic coverage': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'geographic_coverage_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_coverage_note'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('524', '^preferred_citation_of_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preferred_citation_of_described_materials_note(self, key, value):
    """Reverse - Preferred Citation of Described Materials Note."""
    indicator_map1 = {
        'Cite as': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'preferred_citation_of_described_materials_note': 'a',
        'source_of_schema_used': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('preferred_citation_of_described_materials_note'),
        '2': value.get('source_of_schema_used'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('525', '^supplement_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    field_map = {
        'supplement_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('supplement_note'),
        '6': value.get('linkage'),
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
        'Reading program': '0',
        'No display constant generated': '8',
    }

    field_map = {
        'program_name': 'a',
        'interest_level': 'b',
        'reading_level': 'c',
        'title_point_value': 'd',
        'display_text': 'i',
        'nonpublic_note': 'x',
        'public_note': 'z',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('program_name'),
        'b': value.get('interest_level'),
        'c': value.get('reading_level'),
        'd': value.get('title_point_value'),
        'i': value.get('display_text'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')),
        'z': utils.reverse_force_list(
            value.get('public_note')),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('530', '^additional_physical_form_available_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    field_map = {
        'additional_physical_form_available_note': 'a',
        'availability_source': 'b',
        'availability_conditions': 'c',
        'order_number': 'd',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('additional_physical_form_available_note'),
        'b': value.get('availability_source'),
        'c': value.get('availability_conditions'),
        'd': value.get('order_number'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'type_of_reproduction': 'a',
        'place_of_reproduction': 'b',
        'agency_responsible_for_reproduction': 'c',
        'date_of_reproduction': 'd',
        'physical_description_of_reproduction': 'e',
        'series_statement_of_reproduction': 'f',
        'dates_and_or_sequential_designation_of_issues_reproduced': 'm',
        'note_about_reproduction': 'n',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'fixed_length_data_elements_of_reproduction': '7',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_reproduction'),
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'd': value.get('date_of_reproduction'),
        'e': value.get('physical_description_of_reproduction'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        'm': utils.reverse_force_list(
            value.get(
                'dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'main_entry_of_original': 'a',
        'edition_statement_of_original': 'b',
        'publication_distribution_of_original': 'c',
        'physical_description_of_original': 'e',
        'series_statement_of_original': 'f',
        'key_title_of_original': 'k',
        'location_of_original': 'l',
        'material_specific_details': 'm',
        'note_about_original': 'n',
        'other_resource_identifier': 'o',
        'introductory_phrase': 'p',
        'title_statement_of_original': 't',
        'international_standard_serial_number': 'x',
        'international_standard_book_number': 'z',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_of_original'),
        'b': value.get('edition_statement_of_original'),
        'c': value.get('publication_distribution_of_original'),
        'e': value.get('physical_description_of_original'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'l': value.get('location_of_original'),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        'p': value.get('introductory_phrase'),
        't': value.get('title_statement_of_original'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('535', '^location_of_originals_duplicates_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_originals_duplicates_note(self, key, value):
    """Reverse - Location of Originals/Duplicates Note."""
    indicator_map1 = {
        'Holder of originals': '1',
        'Holder of duplicates': '2',
    }

    field_map = {
        'custodian': 'a',
        'postal_address': 'b',
        'country': 'c',
        'telecommunications_address': 'd',
        'repository_location_code': 'g',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('custodian'),
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        'g': value.get('repository_location_code'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'contract_number': 'b',
        'grant_number': 'c',
        'undifferentiated_number': 'd',
        'program_element_number': 'e',
        'project_number': 'f',
        'task_number': 'g',
        'work_unit_number': 'h',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('text_of_note'),
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        'c': utils.reverse_force_list(
            value.get('grant_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'g': utils.reverse_force_list(
            value.get('task_number')
        ),
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'display_text': 'i',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('system_details_note'),
        'i': value.get('display_text'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
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
        'jurisdiction': 'b',
        'authorization': 'c',
        'authorized_users': 'd',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('terms_governing_use_and_reproduction'),
        'b': value.get('jurisdiction'),
        'c': value.get('authorization'),
        'd': value.get('authorized_users'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
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
    indicator_map1 = {
        'No information provided': '_',
        'Private': '0',
        'Not private': '1',
    }

    field_map = {
        'source_of_acquisition': 'a',
        'address': 'b',
        'method_of_acquisition': 'c',
        'date_of_acquisition': 'd',
        'accession_number': 'e',
        'owner': 'f',
        'purchase_price': 'h',
        'extent': 'n',
        'type_of_unit': 'o',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('source_of_acquisition'),
        'b': value.get('address'),
        'c': value.get('method_of_acquisition'),
        'd': value.get('date_of_acquisition'),
        'e': value.get('accession_number'),
        'f': value.get('owner'),
        'h': value.get('purchase_price'),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'No information provided': '_',
        'Private': '0',
        'Not private': '1',
    }

    field_map = {
        'personal_creator': 'a',
        'personal_creator_death_date': 'b',
        'corporate_creator': 'c',
        'copyright_holder': 'd',
        'copyright_holder_contact_information': 'e',
        'copyright_statement': 'f',
        'copyright_date': 'g',
        'copyright_renewal_date': 'h',
        'publication_date': 'i',
        'creation_date': 'j',
        'publisher': 'k',
        'copyright_status': 'l',
        'publication_status': 'm',
        'note': 'n',
        'research_date': 'o',
        'country_of_publication_or_creation': 'p',
        'supplying_agency': 'q',
        'jurisdiction_of_copyright_assessment': 'r',
        'source_of_information': 's',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('personal_creator'),
        'b': value.get('personal_creator_death_date'),
        'c': value.get('corporate_creator'),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        'g': value.get('copyright_date'),
        'i': value.get('publication_date'),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        'j': value.get('creation_date'),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'l': value.get('copyright_status'),
        'm': value.get('publication_status'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': value.get('research_date'),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        'q': value.get('supplying_agency'),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        's': value.get('source_of_information'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'No information provided': '_',
        'Associated materials': '0',
        'Related materials': '1',
    }

    field_map = {
        'custodian': 'a',
        'address': 'b',
        'country': 'c',
        'title': 'd',
        'provenance': 'e',
        'note': 'n',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('custodian')
        ),
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        'e': utils.reverse_force_list(
            value.get('provenance')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '3': value.get('materials_specified'),
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
    indicator_map1 = {
        'No information provided': '_',
        'Biographical sketch': '0',
        'Administrative history': '1',
    }

    field_map = {
        'biographical_or_historical_data': 'a',
        'expansion': 'b',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('biographical_or_historical_data'),
        'b': value.get('expansion'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
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
        'language_note': 'a',
        'information_code_or_alphabet': 'b',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('language_note'),
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '3': value.get('materials_specified'),
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
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('former_title_complexity_note'),
        '6': value.get('linkage'),
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
        'issuing_body_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('issuing_body_note'),
        '6': value.get('linkage'),
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
        'entity_type_label': 'a',
        'entity_type_definition_and_source': 'b',
        'attribute_label': 'c',
        'attribute_definition_and_source': 'd',
        'enumerated_domain_value': 'e',
        'enumerated_domain_value_definition_and_source': 'f',
        'range_domain_minimum_and_maximum': 'g',
        'codeset_name_and_source': 'h',
        'unrepresentable_domain': 'i',
        'attribute_units_of_measurement_and_resolution': 'j',
        'beginning_and_ending_date_of_attribute_values': 'k',
        'attribute_value_accuracy': 'l',
        'attribute_value_accuracy_explanation': 'm',
        'attribute_measurement_frequency': 'n',
        'entity_and_attribute_overview': 'o',
        'entity_and_attribute_detail_citation': 'p',
        'uniform_resource_identifier': 'u',
        'display_note': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('entity_type_label'),
        'b': value.get('entity_type_definition_and_source'),
        'c': value.get('attribute_label'),
        'd': value.get('attribute_definition_and_source'),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'g': value.get('range_domain_minimum_and_maximum'),
        'h': value.get('codeset_name_and_source'),
        'i': value.get('unrepresentable_domain'),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'l': value.get('attribute_value_accuracy'),
        'm': value.get('attribute_value_accuracy_explanation'),
        'n': value.get('attribute_measurement_frequency'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('555', '^cumulative_index_finding_aids_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        'Indexes': '_',
        'Finding aids': '0',
        'No display constant generated': '8',
    }

    field_map = {
        'cumulative_index_finding_aids_note': 'a',
        'availability_source': 'b',
        'degree_of_control': 'c',
        'bibliographic_reference': 'd',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('cumulative_index_finding_aids_note'),
        'b': utils.reverse_force_list(
            value.get('availability_source')),
        'c': value.get('degree_of_control'),
        'd': value.get('bibliographic_reference'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('556', '^information_about_documentation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {
        'Documentation': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'information_about_documentation_note': 'a',
        'international_standard_book_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('information_about_documentation_note'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('561', '^ownership_and_custodial_history$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {
        'No information provided': '_',
        'Private': '0',
        'Not private': '1',
    }

    field_map = {
        'history': 'a',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('history'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'copy_identification': 'b',
        'version_identification': 'c',
        'presentation_format': 'd',
        'number_of_copies': 'e',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('identifying_markings')
        ),
        'b': utils.reverse_force_list(
            value.get('copy_identification')
        ),
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        'd': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
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
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('binding_note'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
    indicator_map1 = {
        'File size': '_',
        'Case file characteristics': '0',
        'No display constant generated': '8',
    }

    field_map = {
        'number_of_cases_variables': 'a',
        'name_of_variable': 'b',
        'unit_of_analysis': 'c',
        'universe_of_data': 'd',
        'filing_scheme_or_code': 'e',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number_of_cases_variables'),
        'b': utils.reverse_force_list(
            value.get('name_of_variable')),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('567', '^methodology_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_methodology_note(self, key, value):
    """Reverse - Methodology Note."""
    indicator_map1 = {
        'Methodology': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'methodology_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('methodology_note'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('580', '^linking_entry_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    field_map = {
        'linking_entry_complexity_note': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('linking_entry_complexity_note'),
        '6': value.get('linkage'),
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
        'Publications': '_',
        'No display constant generated': '8',
    }

    field_map = {
        'publications_about_described_materials_note': 'a',
        'international_standard_book_number': 'z',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('publications_about_described_materials_note'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('583', '^action_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {
        'No information provided': '_',
        'Private': '0',
        'Not private': '1',
    }

    field_map = {
        'action': 'a',
        'action_identification': 'b',
        'time_date_of_action': 'c',
        'action_interval': 'd',
        'contingency_for_action': 'e',
        'authorization': 'f',
        'jurisdiction': 'h',
        'method_of_action': 'i',
        'site_of_action': 'j',
        'action_agent': 'k',
        'status': 'l',
        'extent': 'n',
        'type_of_unit': 'o',
        'uniform_resource_identifier': 'u',
        'nonpublic_note': 'x',
        'public_note': 'z',
        'source_of_term': '2',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('action'),
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('source_of_term'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'frequency_of_use': 'b',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('exhibitions_note'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('586', '^awards_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_awards_note(self, key, value):
    """Reverse - Awards Note."""
    indicator_map1 = {
        'Awards': '_',
        'No display constant generated': '8',
    }

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
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('588', '^source_of_description_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    indicator_map1 = {
        'No information provided': '_',
        'Source of description': '0',
        'Latest issue consulted': '1',
    }

    field_map = {
        'source_of_description_note': 'a',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('source_of_description_note'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }
