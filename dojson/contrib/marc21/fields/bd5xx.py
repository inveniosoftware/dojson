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

from ..model import marc21


@marc21.over('general_note', '^500..')
@utils.for_each_value
@utils.filter_values
def general_note(self, key, value):
    """General Note."""
    field_map = {
        'a': 'general_note',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_note': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('with_note', '^501..')
@utils.for_each_value
@utils.filter_values
def with_note(self, key, value):
    """With Note."""
    field_map = {
        'a': 'with_note',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'with_note': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('dissertation_note', '^502..')
@utils.for_each_value
@utils.filter_values
def dissertation_note(self, key, value):
    """Dissertation Note."""
    field_map = {
        'a': 'dissertation_note',
        'o': 'dissertation_identifier',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        'c': 'name_of_granting_institution',
        '8': 'field_link_and_sequence_number',
        'b': 'degree_type',
        'd': 'year_degree_granted',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'dissertation_note': value.get('a'),
        'dissertation_identifier': utils.force_list(
            value.get('o')
        ),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'name_of_granting_institution': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'degree_type': value.get('b'),
        'year_degree_granted': value.get('d'),
    }


@marc21.over('bibliography_note', '^504..')
@utils.for_each_value
@utils.filter_values
def bibliography_note(self, key, value):
    """Bibliography, Etc. Note."""
    field_map = {
        'a': 'bibliography_note',
        '8': 'field_link_and_sequence_number',
        'b': 'number_of_references',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'bibliography_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_references': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('formatted_contents_note', '^505[0812_][0_]')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    """Formatted Contents Note."""
    indicator_map1 = {
        "0": "Contents",
        "1": "Incomplete contents",
        "2": "Partial contents",
        "8": "No display constant generated"}
    indicator_map2 = {"0": "Enhanced", "_": "Basic"}
    field_map = {
        'a': 'formatted_contents_note',
        't': 'title',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'r': 'statement_of_responsibility',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    if key[4] in indicator_map2:
        order.append('level_of_content_designation')

    return {
        '__order__': tuple(order) if len(order) else None,
        'formatted_contents_note': value.get('a'),
        'title': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'statement_of_responsibility': utils.force_list(
            value.get('r')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
        'level_of_content_designation': indicator_map2.get(key[4]),
    }


@marc21.over('restrictions_on_access_note', '^506[01_].')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    indicator_map1 = {
        "0": "No restrictions",
        "1": "Restrictions apply",
        "_": "No information provided"}
    field_map = {
        'a': 'terms_governing_access',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        'e': 'authorization',
        '5': 'institution_to_which_field_applies',
        'c': 'physical_access_provisions',
        'f': 'standardized_terminology_for_access_restriction',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'b': 'jurisdiction',
        'd': 'authorized_users',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('restriction')

    return {
        '__order__': tuple(order) if len(order) else None,
        'terms_governing_access': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'authorization': utils.force_list(
            value.get('e')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'physical_access_provisions': utils.force_list(
            value.get('c')
        ),
        'standardized_terminology_for_access_restriction': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'jurisdiction': utils.force_list(
            value.get('b')
        ),
        'authorized_users': utils.force_list(
            value.get('d')
        ),
        'restriction': indicator_map1.get(key[3]),
    }


@marc21.over('scale_note_for_graphic_material', '^507..')
@utils.filter_values
def scale_note_for_graphic_material(self, key, value):
    """Scale Note for Graphic Material."""
    field_map = {
        'a': 'representative_fraction_of_scale_note',
        '8': 'field_link_and_sequence_number',
        'b': 'remainder_of_scale_note',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'representative_fraction_of_scale_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'remainder_of_scale_note': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('creation_production_credits_note', '^508..')
@utils.for_each_value
@utils.filter_values
def creation_production_credits_note(self, key, value):
    """Creation/Production Credits Note."""
    field_map = {
        'a': 'creation_production_credits_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'creation_production_credits_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('citation_references_note', '^510[04231_].')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    """Citation/References Note."""
    indicator_map1 = {
        "0": "Coverage unknown",
        "1": "Coverage complete",
        "2": "Coverage is selective",
        "3": "Location in source not given",
        "4": "Location in source given"}
    field_map = {
        'a': 'name_of_source',
        'x': 'international_standard_serial_number',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'location_within_source',
        '8': 'field_link_and_sequence_number',
        'b': 'coverage_of_source',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('coverage_location_in_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_source': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'location_within_source': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'coverage_of_source': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'coverage_location_in_source': indicator_map1.get(key[3]),
    }


@marc21.over('participant_or_performer_note', '^511[01_].')
@utils.for_each_value
@utils.filter_values
def participant_or_performer_note(self, key, value):
    """Participant or Performer Note."""
    indicator_map1 = {"0": "No display constant generated", "1": "Cast"}
    field_map = {
        'a': 'participant_or_performer_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'participant_or_performer_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('type_of_report_and_period_covered_note', '^513..')
@utils.for_each_value
@utils.filter_values
def type_of_report_and_period_covered_note(self, key, value):
    """Type of Report and Period Covered Note."""
    field_map = {
        'a': 'type_of_report',
        '8': 'field_link_and_sequence_number',
        'b': 'period_covered',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_report': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'period_covered': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('data_quality_note', '^514..')
@utils.filter_values
def data_quality_note(self, key, value):
    """Data Quality Note."""
    field_map = {
        'a': 'attribute_accuracy_report',
        'z': 'display_note',
        'u': 'uniform_resource_identifier',
        'm': 'cloud_cover',
        'g': 'horizontal_position_accuracy_value',
        'e': 'completeness_report',
        '8': 'field_link_and_sequence_number',
        'i': 'vertical_positional_accuracy_report',
        'c': 'attribute_accuracy_explanation',
        'f': 'horizontal_position_accuracy_report',
        '6': 'linkage',
        'b': 'attribute_accuracy_value',
        'd': 'logical_consistency_report',
        'h': 'horizontal_position_accuracy_explanation',
        'j': 'vertical_positional_accuracy_value',
        'k': 'vertical_positional_accuracy_explanation',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'attribute_accuracy_report': value.get('a'),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'cloud_cover': value.get('m'),
        'horizontal_position_accuracy_value': utils.force_list(
            value.get('g')
        ),
        'completeness_report': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'vertical_positional_accuracy_report': value.get('i'),
        'attribute_accuracy_explanation': utils.force_list(
            value.get('c')
        ),
        'horizontal_position_accuracy_report': value.get('f'),
        'linkage': value.get('6'),
        'attribute_accuracy_value': utils.force_list(
            value.get('b')
        ),
        'logical_consistency_report': value.get('d'),
        'horizontal_position_accuracy_explanation': utils.force_list(
            value.get('h')
        ),
        'vertical_positional_accuracy_value': utils.force_list(
            value.get('j')
        ),
        'vertical_positional_accuracy_explanation': utils.force_list(
            value.get('k')
        ),
    }


@marc21.over('numbering_peculiarities_note', '^515..')
@utils.for_each_value
@utils.filter_values
def numbering_peculiarities_note(self, key, value):
    """Numbering Peculiarities Note."""
    field_map = {
        'a': 'numbering_peculiarities_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'numbering_peculiarities_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('type_of_computer_file_or_data_note', '^516[8_].')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    """Type of Computer File or Data Note."""
    indicator_map1 = {
        "8": "No display constant generated",
        "_": "Type of file"}
    field_map = {
        'a': 'type_of_computer_file_or_data_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_computer_file_or_data_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('date_time_and_place_of_an_event_note', '^518..')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event_note(self, key, value):
    """Date/Time and Place of an Event Note."""
    field_map = {
        '0': 'record_control_number',
        'a': 'date_time_and_place_of_an_event_note',
        'p': 'place_of_event',
        'o': 'other_event_information',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_term',
        'd': 'date_of_event',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'date_time_and_place_of_an_event_note': value.get('a'),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'other_event_information': utils.force_list(
            value.get('o')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'date_of_event': utils.force_list(
            value.get('d')
        ),
    }


@marc21.over('summary', '^520[042381_].')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    """Summary, Etc.."""
    indicator_map1 = {
        "0": "Subject",
        "1": "Review",
        "2": "Scope and content",
        "3": "Abstract",
        "4": "Content advice",
        "8": "No display constant generated",
        "_": "Summary"}
    field_map = {
        'a': 'summary',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'c': 'assigning_source',
        '2': 'source',
        'b': 'expansion_of_summary_note',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'summary': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'assigning_source': value.get('c'),
        'source': value.get('2'),
        'expansion_of_summary_note': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('target_audience_note', '^521[042381_].')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    """Target Audience Note."""
    indicator_map1 = {
        "0": "Reading grade level",
        "1": "Interest age level",
        "2": "Interest grade level",
        "3": "Special audience characteristics",
        "4": "Motivation/interest level",
        "8": "No display constant generated",
        "_": "Audience"}
    field_map = {
        'a': 'target_audience_note',
        '8': 'field_link_and_sequence_number',
        'b': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'target_audience_note': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('geographic_coverage_note', '^522[8_].')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    """Geographic Coverage Note."""
    indicator_map1 = {
        "8": "No display constant generated",
        "_": "Geographic coverage"}
    field_map = {
        'a': 'geographic_coverage_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_coverage_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('preferred_citation_of_described_materials_note', '^524[8_].')
@utils.for_each_value
@utils.filter_values
def preferred_citation_of_described_materials_note(self, key, value):
    """Preferred Citation of Described Materials Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Cite as"}
    field_map = {
        'a': 'preferred_citation_of_described_materials_note',
        '3': 'materials_specified',
        '2': 'source_of_schema_used',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'preferred_citation_of_described_materials_note': value.get('a'),
        'materials_specified': value.get('3'),
        'source_of_schema_used': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('supplement_note', '^525..')
@utils.for_each_value
@utils.filter_values
def supplement_note(self, key, value):
    """Supplement Note."""
    field_map = {
        'a': 'supplement_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'supplement_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('study_program_information_note', '^526[08_].')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    """Study Program Information Note."""
    indicator_map1 = {
        "0": "Reading program",
        "8": "No display constant generated"}
    field_map = {
        'a': 'program_name',
        'z': 'public_note',
        'x': 'nonpublic_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'c': 'reading_level',
        '5': 'institution_to_which_field_applies',
        'b': 'interest_level',
        'd': 'title_point_value',
        'i': 'display_text',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'program_name': value.get('a'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'reading_level': value.get('c'),
        'institution_to_which_field_applies': value.get('5'),
        'interest_level': value.get('b'),
        'title_point_value': value.get('d'),
        'display_text': value.get('i'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('additional_physical_form_available_note', '^530..')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_available_note(self, key, value):
    """Additional Physical Form Available Note."""
    field_map = {
        'a': 'additional_physical_form_available_note',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'availability_conditions',
        '8': 'field_link_and_sequence_number',
        'b': 'availability_source',
        'd': 'order_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'additional_physical_form_available_note': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'availability_conditions': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'availability_source': value.get('b'),
        'order_number': value.get('d'),
    }


@marc21.over('reproduction_note', '^533..')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    """Reproduction Note."""
    field_map = {
        'a': 'type_of_reproduction',
        '3': 'materials_specified',
        'e': 'physical_description_of_reproduction',
        '8': 'field_link_and_sequence_number',
        '7': 'fixed_length_data_elements_of_reproduction',
        'n': 'note_about_reproduction',
        'c': 'agency_responsible_for_reproduction',
        'f': 'series_statement_of_reproduction',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'm': 'dates_and_or_sequential_designation_of_issues_reproduced',
        'b': 'place_of_reproduction',
        'd': 'date_of_reproduction',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_reproduction': value.get('a'),
        'materials_specified': value.get('3'),
        'physical_description_of_reproduction': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'note_about_reproduction': utils.force_list(
            value.get('n')
        ),
        'agency_responsible_for_reproduction': utils.force_list(
            value.get('c')
        ),
        'series_statement_of_reproduction': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': value.get('5'),
        'dates_and_or_sequential_designation_of_issues_reproduced': utils.force_list(
            value.get('m')
        ),
        'place_of_reproduction': utils.force_list(
            value.get('b')
        ),
        'date_of_reproduction': value.get('d'),
    }


@marc21.over('original_version_note', '^534..')
@utils.for_each_value
@utils.filter_values
def original_version_note(self, key, value):
    """Original Version Note."""
    field_map = {
        'a': 'main_entry_of_original',
        'l': 'location_of_original',
        'p': 'introductory_phrase',
        'o': 'other_resource_identifier',
        '3': 'materials_specified',
        'x': 'international_standard_serial_number',
        'e': 'physical_description_of_original',
        '8': 'field_link_and_sequence_number',
        'n': 'note_about_original',
        't': 'title_statement_of_original',
        'c': 'publication_distribution_of_original',
        'f': 'series_statement_of_original',
        '6': 'linkage',
        'z': 'international_standard_book_number',
        'm': 'material_specific_details',
        'b': 'edition_statement_of_original',
        'k': 'key_title_of_original',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_of_original': value.get('a'),
        'location_of_original': value.get('l'),
        'introductory_phrase': value.get('p'),
        'other_resource_identifier': utils.force_list(
            value.get('o')
        ),
        'materials_specified': value.get('3'),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'physical_description_of_original': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_about_original': utils.force_list(
            value.get('n')
        ),
        'title_statement_of_original': value.get('t'),
        'publication_distribution_of_original': value.get('c'),
        'series_statement_of_original': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'material_specific_details': value.get('m'),
        'edition_statement_of_original': value.get('b'),
        'key_title_of_original': utils.force_list(
            value.get('k')
        ),
    }


@marc21.over('location_of_originals_duplicates_note', '^535[12_].')
@utils.for_each_value
@utils.filter_values
def location_of_originals_duplicates_note(self, key, value):
    """Location of Originals/Duplicates Note."""
    indicator_map1 = {"1": "Holder of originals", "2": "Holder of duplicates"}
    field_map = {
        'a': 'custodian',
        '3': 'materials_specified',
        '6': 'linkage',
        'g': 'repository_location_code',
        'c': 'country',
        '8': 'field_link_and_sequence_number',
        'b': 'postal_address',
        'd': 'telecommunications_address',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('custodial_role')

    return {
        '__order__': tuple(order) if len(order) else None,
        'custodian': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'repository_location_code': value.get('g'),
        'country': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'postal_address': utils.force_list(
            value.get('b')
        ),
        'telecommunications_address': utils.force_list(
            value.get('d')
        ),
        'custodial_role': indicator_map1.get(key[3]),
    }


@marc21.over('funding_information_note', '^536..')
@utils.for_each_value
@utils.filter_values
def funding_information_note(self, key, value):
    """Funding Information Note."""
    field_map = {
        'a': 'text_of_note',
        'e': 'program_element_number',
        'f': 'project_number',
        '6': 'linkage',
        'g': 'task_number',
        'c': 'grant_number',
        '8': 'field_link_and_sequence_number',
        'b': 'contract_number',
        'd': 'undifferentiated_number',
        'h': 'work_unit_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'text_of_note': value.get('a'),
        'program_element_number': utils.force_list(
            value.get('e')
        ),
        'project_number': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'task_number': utils.force_list(
            value.get('g')
        ),
        'grant_number': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'contract_number': utils.force_list(
            value.get('b')
        ),
        'undifferentiated_number': utils.force_list(
            value.get('d')
        ),
        'work_unit_number': utils.force_list(
            value.get('h')
        ),
    }


@marc21.over('system_details_note', '^538..')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    """System Details Note."""
    field_map = {
        'a': 'system_details_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'u': 'uniform_resource_identifier',
        'i': 'display_text',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'system_details_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'display_text': value.get('i'),
    }


@marc21.over('terms_governing_use_and_reproduction_note', '^540..')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    field_map = {
        'a': 'terms_governing_use_and_reproduction',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'c': 'authorization',
        '5': 'institution_to_which_field_applies',
        'b': 'jurisdiction',
        'd': 'authorized_users',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'terms_governing_use_and_reproduction': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authorization': value.get('c'),
        'institution_to_which_field_applies': value.get('5'),
        'jurisdiction': value.get('b'),
        'authorized_users': value.get('d'),
    }


@marc21.over('immediate_source_of_acquisition_note', '^541[01_].')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    indicator_map1 = {
        "0": "Private",
        "1": "Not private",
        "_": "No information provided"}
    field_map = {
        'a': 'source_of_acquisition',
        'o': 'type_of_unit',
        '3': 'materials_specified',
        'e': 'accession_number',
        '8': 'field_link_and_sequence_number',
        'n': 'extent',
        'c': 'method_of_acquisition',
        'f': 'owner',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'b': 'address',
        'd': 'date_of_acquisition',
        'h': 'purchase_price',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_acquisition': value.get('a'),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'materials_specified': value.get('3'),
        'accession_number': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'method_of_acquisition': value.get('c'),
        'owner': value.get('f'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': value.get('5'),
        'address': value.get('b'),
        'date_of_acquisition': value.get('d'),
        'purchase_price': value.get('h'),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('information_relating_to_copyright_status', '^542[01_].')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    """Information Relating to Copyright Status."""
    indicator_map1 = {
        "0": "Private",
        "1": "Not private",
        "_": "No information provided"}
    field_map = {
        'a': 'personal_creator',
        'l': 'copyright_status',
        'p': 'country_of_publication_or_creation',
        'o': 'research_date',
        '3': 'materials_specified',
        'e': 'copyright_holder_contact_information',
        '8': 'field_link_and_sequence_number',
        'q': 'supplying_agency',
        'i': 'publication_date',
        'b': 'personal_creator_death_date',
        'd': 'copyright_holder',
        'r': 'jurisdiction_of_copyright_assessment',
        'h': 'copyright_renewal_date',
        'u': 'uniform_resource_identifier',
        'm': 'publication_status',
        'g': 'copyright_date',
        'n': 'note',
        'c': 'corporate_creator',
        'f': 'copyright_statement',
        '6': 'linkage',
        's': 'source_of_information',
        'j': 'creation_date',
        'k': 'publisher',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_creator': value.get('a'),
        'copyright_status': value.get('l'),
        'country_of_publication_or_creation': utils.force_list(
            value.get('p')
        ),
        'research_date': value.get('o'),
        'materials_specified': value.get('3'),
        'copyright_holder_contact_information': utils.force_list(
            value.get('e')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'supplying_agency': value.get('q'),
        'publication_date': value.get('i'),
        'personal_creator_death_date': value.get('b'),
        'copyright_holder': utils.force_list(
            value.get('d')
        ),
        'jurisdiction_of_copyright_assessment': value.get('r'),
        'copyright_renewal_date': utils.force_list(
            value.get('h')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'publication_status': value.get('m'),
        'copyright_date': value.get('g'),
        'note': utils.force_list(
            value.get('n')
        ),
        'corporate_creator': value.get('c'),
        'copyright_statement': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'source_of_information': value.get('s'),
        'creation_date': value.get('j'),
        'publisher': utils.force_list(
            value.get('k')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('location_of_other_archival_materials_note', '^544[01_].')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    """Location of Other Archival Materials Note."""
    indicator_map1 = {
        "0": "Associated materials",
        "1": "Related materials",
        "_": "No information provided"}
    field_map = {
        'a': 'custodian',
        'e': 'provenance',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'country',
        '8': 'field_link_and_sequence_number',
        'b': 'address',
        'd': 'title',
        'n': 'note',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'custodian': utils.force_list(
            value.get('a')
        ),
        'provenance': utils.force_list(
            value.get('e')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'country': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'address': utils.force_list(
            value.get('b')
        ),
        'title': utils.force_list(
            value.get('d')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'relationship': indicator_map1.get(key[3]),
    }


@marc21.over('biographical_or_historical_data', '^545[01_].')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {
        "0": "Biographical sketch",
        "1": "Administrative history",
        "_": "No information provided"}
    field_map = {
        'a': 'biographical_or_historical_data',
        '8': 'field_link_and_sequence_number',
        'b': 'expansion',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_data')

    return {
        '__order__': tuple(order) if len(order) else None,
        'biographical_or_historical_data': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'expansion': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'type_of_data': indicator_map1.get(key[3]),
    }


@marc21.over('language_note', '^546..')
@utils.for_each_value
@utils.filter_values
def language_note(self, key, value):
    """Language Note."""
    field_map = {
        'a': 'language_note',
        '8': 'field_link_and_sequence_number',
        'b': 'information_code_or_alphabet',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'information_code_or_alphabet': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
    }


@marc21.over('former_title_complexity_note', '^547..')
@utils.for_each_value
@utils.filter_values
def former_title_complexity_note(self, key, value):
    """Former Title Complexity Note."""
    field_map = {
        'a': 'former_title_complexity_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'former_title_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('issuing_body_note', '^550..')
@utils.for_each_value
@utils.filter_values
def issuing_body_note(self, key, value):
    """Issuing Body Note."""
    field_map = {
        'a': 'issuing_body_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'issuing_body_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('entity_and_attribute_information_note', '^552..')
@utils.for_each_value
@utils.filter_values
def entity_and_attribute_information_note(self, key, value):
    """Entity and Attribute Information Note."""
    field_map = {
        'a': 'entity_type_label',
        'l': 'attribute_value_accuracy',
        'p': 'entity_and_attribute_detail_citation',
        'o': 'entity_and_attribute_overview',
        'm': 'attribute_value_accuracy_explanation',
        'g': 'range_domain_minimum_and_maximum',
        'e': 'enumerated_domain_value',
        '8': 'field_link_and_sequence_number',
        'n': 'attribute_measurement_frequency',
        'i': 'unrepresentable_domain',
        'c': 'attribute_label',
        'f': 'enumerated_domain_value_definition_and_source',
        '6': 'linkage',
        'z': 'display_note',
        'u': 'uniform_resource_identifier',
        'b': 'entity_type_definition_and_source',
        'd': 'attribute_definition_and_source',
        'h': 'codeset_name_and_source',
        'j': 'attribute_units_of_measurement_and_resolution',
        'k': 'beginning_and_ending_date_of_attribute_values',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'entity_type_label': value.get('a'),
        'attribute_value_accuracy': value.get('l'),
        'entity_and_attribute_detail_citation': utils.force_list(
            value.get('p')
        ),
        'entity_and_attribute_overview': utils.force_list(
            value.get('o')
        ),
        'attribute_value_accuracy_explanation': value.get('m'),
        'range_domain_minimum_and_maximum': value.get('g'),
        'enumerated_domain_value': utils.force_list(
            value.get('e')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'attribute_measurement_frequency': value.get('n'),
        'unrepresentable_domain': value.get('i'),
        'attribute_label': value.get('c'),
        'enumerated_domain_value_definition_and_source': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'entity_type_definition_and_source': value.get('b'),
        'attribute_definition_and_source': value.get('d'),
        'codeset_name_and_source': value.get('h'),
        'attribute_units_of_measurement_and_resolution': value.get('j'),
        'beginning_and_ending_date_of_attribute_values': value.get('k'),
    }


@marc21.over('cumulative_index_finding_aids_note', '^555[08_].')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    """Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        "0": "Finding aids",
        "8": "No display constant generated",
        "_": "Indexes"}
    field_map = {
        'a': 'cumulative_index_finding_aids_note',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'degree_of_control',
        '8': 'field_link_and_sequence_number',
        'b': 'availability_source',
        'd': 'bibliographic_reference',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'cumulative_index_finding_aids_note': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'degree_of_control': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'availability_source': utils.force_list(
            value.get('b')
        ),
        'bibliographic_reference': value.get('d'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('information_about_documentation_note', '^556[8_].')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    """Information About Documentation Note."""
    indicator_map1 = {
        "8": "No display constant generated",
        "_": "Documentation"}
    field_map = {
        'a': 'information_about_documentation_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'z': 'international_standard_book_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'information_about_documentation_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('ownership_and_custodial_history', '^561[01_].')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {
        "0": "Private",
        "1": "Not private",
        "_": "No information provided"}
    field_map = {
        'a': 'history',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'history': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('copy_and_version_identification_note', '^562..')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    """Copy and Version Identification Note."""
    field_map = {
        'a': 'identifying_markings',
        'e': 'number_of_copies',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'c': 'version_identification',
        '5': 'institution_to_which_field_applies',
        'b': 'copy_identification',
        'd': 'presentation_format',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'identifying_markings': utils.force_list(
            value.get('a')
        ),
        'number_of_copies': utils.force_list(
            value.get('e')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'version_identification': utils.force_list(
            value.get('c')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'copy_identification': utils.force_list(
            value.get('b')
        ),
        'presentation_format': utils.force_list(
            value.get('d')
        ),
    }


@marc21.over('binding_information', '^563..')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    """Binding Information."""
    field_map = {
        'a': 'binding_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'binding_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21.over('case_file_characteristics_note', '^565[08_].')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    """Case File Characteristics Note."""
    indicator_map1 = {
        "0": "Case file characteristics",
        "8": "No display constant generated",
        "_": "File size"}
    field_map = {
        'a': 'number_of_cases_variables',
        'e': 'filing_scheme_or_code',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'unit_of_analysis',
        '8': 'field_link_and_sequence_number',
        'b': 'name_of_variable',
        'd': 'universe_of_data',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_of_cases_variables': value.get('a'),
        'filing_scheme_or_code': utils.force_list(
            value.get('e')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'unit_of_analysis': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_variable': utils.force_list(
            value.get('b')
        ),
        'universe_of_data': utils.force_list(
            value.get('d')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('methodology_note', '^567[8_].')
@utils.for_each_value
@utils.filter_values
def methodology_note(self, key, value):
    """Methodology Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Methodology"}
    field_map = {
        'a': 'methodology_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'methodology_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('linking_entry_complexity_note', '^580..')
@utils.for_each_value
@utils.filter_values
def linking_entry_complexity_note(self, key, value):
    """Linking Entry Complexity Note."""
    field_map = {
        'a': 'linking_entry_complexity_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linking_entry_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('publications_about_described_materials_note', '^581[8_].')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    """Publications About Described Materials Note."""
    indicator_map1 = {
        "8": "No display constant generated",
        "_": "Publications"}
    field_map = {
        'a': 'publications_about_described_materials_note',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '6': 'linkage',
        'z': 'international_standard_book_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'publications_about_described_materials_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('action_note', '^583[01_].')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    indicator_map1 = {
        "0": "Private",
        "1": "Not private",
        "_": "No information provided"}
    field_map = {
        'a': 'action',
        'l': 'status',
        'z': 'public_note',
        'o': 'type_of_unit',
        '2': 'source_of_term',
        'x': 'nonpublic_note',
        'e': 'contingency_for_action',
        '5': 'institution_to_which_field_applies',
        'n': 'extent',
        'i': 'method_of_action',
        'c': 'time_date_of_action',
        'f': 'authorization',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        'b': 'action_identification',
        'd': 'action_interval',
        'h': 'jurisdiction',
        'j': 'site_of_action',
        'k': 'action_agent',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'action': value.get('a'),
        'status': utils.force_list(
            value.get('l')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'source_of_term': value.get('2'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'contingency_for_action': utils.force_list(
            value.get('e')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'extent': utils.force_list(
            value.get('n')
        ),
        'method_of_action': utils.force_list(
            value.get('i')
        ),
        'time_date_of_action': utils.force_list(
            value.get('c')
        ),
        'authorization': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'action_identification': utils.force_list(
            value.get('b')
        ),
        'action_interval': utils.force_list(
            value.get('d')
        ),
        'jurisdiction': utils.force_list(
            value.get('h')
        ),
        'site_of_action': utils.force_list(
            value.get('j')
        ),
        'action_agent': utils.force_list(
            value.get('k')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('accumulation_and_frequency_of_use_note', '^584..')
@utils.for_each_value
@utils.filter_values
def accumulation_and_frequency_of_use_note(self, key, value):
    """Accumulation and Frequency of Use Note."""
    field_map = {
        'a': 'accumulation',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'b': 'frequency_of_use',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'accumulation': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'frequency_of_use': utils.force_list(
            value.get('b')
        ),
    }


@marc21.over('exhibitions_note', '^585..')
@utils.for_each_value
@utils.filter_values
def exhibitions_note(self, key, value):
    """Exhibitions Note."""
    field_map = {
        'a': 'exhibitions_note',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'exhibitions_note': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('awards_note', '^586[8_].')
@utils.for_each_value
@utils.filter_values
def awards_note(self, key, value):
    """Awards Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Awards"}
    field_map = {
        'a': 'awards_note',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'awards_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('source_of_description_note', '^588[01_].')
@utils.for_each_value
@utils.filter_values
def source_of_description_note(self, key, value):
    """Source of Description Note."""
    indicator_map1 = {
        "0": "Source of description",
        "1": "Latest issue consulted",
        "_": "No information provided"}
    field_map = {
        'a': 'source_of_description_note',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_description_note': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }
