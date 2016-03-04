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


@marc21.over('general_note', '^500__')
@utils.for_each_value
@utils.filter_values
def general_note(self, key, value):
    """General Note."""
    field_map = {
        'a': 'general_note',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_note': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('with_note', '^501__')
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


@marc21.over('dissertation_note', '^502__')
@utils.for_each_value
@utils.filter_values
def dissertation_note(self, key, value):
    """Dissertation Note."""
    field_map = {
        'a': 'dissertation_note',
        'b': 'degree_type',
        'c': 'name_of_granting_institution',
        'd': 'year_degree_granted',
        'g': 'miscellaneous_information',
        'o': 'dissertation_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'dissertation_note': value.get('a'),
        'degree_type': value.get('b'),
        'name_of_granting_institution': value.get('c'),
        'year_degree_granted': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'dissertation_identifier': utils.force_list(
            value.get('o')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('bibliography_note', '^504__')
@utils.for_each_value
@utils.filter_values
def bibliography_note(self, key, value):
    """Bibliography, Etc. Note."""
    field_map = {
        'a': 'bibliography_note',
        'b': 'number_of_references',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'bibliography_note': value.get('a'),
        'number_of_references': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('formatted_contents_note', '^505[_0128][_0]')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    """Formatted Contents Note."""
    indicator_map1 = {
        '0': 'Contents',
        '1': 'Incomplete contents',
        '2': 'Partial contents',
        '8': 'No display constant generated',
    }

    indicator_map2 = {
        '_': 'Basic',
        '0': 'Enhanced',
    }

    field_map = {
        'a': 'formatted_contents_note',
        'g': 'miscellaneous_information',
        'r': 'statement_of_responsibility',
        't': 'title',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')
    if key[4] in indicator_map2:
        order.append('level_of_content_designation')

    return {
        '__order__': tuple(order) if len(order) else None,
        'formatted_contents_note': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'statement_of_responsibility': utils.force_list(
            value.get('r')
        ),
        'title': utils.force_list(
            value.get('t')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
        'level_of_content_designation': indicator_map2.get(key[4]),
    }


@marc21.over('restrictions_on_access_note', '^506[_01]_')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'No restrictions',
        '1': 'Restrictions apply',
    }

    field_map = {
        'a': 'terms_governing_access',
        'b': 'jurisdiction',
        'c': 'physical_access_provisions',
        'd': 'authorized_users',
        'e': 'authorization',
        'f': 'standardized_terminology_for_access_restriction',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number'
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('restriction')

    return {
        '__order__': tuple(order) if len(order) else None,
        'terms_governing_access': value.get('a'),
        'jurisdiction': utils.force_list(
            value.get('b')
        ),
        'physical_access_provisions': utils.force_list(
            value.get('c')
        ),
        'authorized_users': utils.force_list(
            value.get('d')
        ),
        'authorization': utils.force_list(
            value.get('e')
        ),
        'standardized_terminology_for_access_restriction': utils.force_list(
            value.get('f')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'restriction': indicator_map1.get(key[3], '_'),
    }


@marc21.over('scale_note_for_graphic_material', '^507__')
@utils.filter_values
def scale_note_for_graphic_material(self, key, value):
    """Scale Note for Graphic Material."""
    field_map = {
        'a': 'representative_fraction_of_scale_note',
        'b': 'remainder_of_scale_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'representative_fraction_of_scale_note': value.get('a'),
        'remainder_of_scale_note': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('creation_production_credits_note', '^508__')
@utils.for_each_value
@utils.filter_values
def creation_production_credits_note(self, key, value):
    """Creation/Production Credits Note."""
    field_map = {
        'a': 'creation_production_credits_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'creation_production_credits_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('citation_references_note', '^510[_01234]_')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    """Citation/References Note."""
    indicator_map1 = {
        '0': 'Coverage unknown',
        '1': 'Coverage complete',
        '2': 'Coverage is selective',
        '3': 'Location in source not given',
        '4': 'Location in source given',
    }

    field_map = {
        'a': 'name_of_source',
        'b': 'coverage_of_source',
        'c': 'location_within_source',
        'u': 'uniform_resource_identifier',
        'x': 'international_standard_serial_number',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('coverage_location_in_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_source': value.get('a'),
        'coverage_of_source': value.get('b'),
        'location_within_source': value.get('c'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'international_standard_serial_number': value.get('x'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'coverage_location_in_source': indicator_map1.get(key[3]),
    }


@marc21.over('participant_or_performer_note', '^511[_01]_')
@utils.for_each_value
@utils.filter_values
def participant_or_performer_note(self, key, value):
    """Participant or Performer Note."""
    indicator_map1 = {
        '0': 'No display constant generated',
        '1': 'Cast',
    }

    field_map = {
        'a': 'participant_or_performer_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'participant_or_performer_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('type_of_report_and_period_covered_note', '^513__')
@utils.for_each_value
@utils.filter_values
def type_of_report_and_period_covered_note(self, key, value):
    """Type of Report and Period Covered Note."""
    field_map = {
        'a': 'type_of_report',
        'b': 'period_covered',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_report': value.get('a'),
        'period_covered': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('data_quality_note', '^514__')
@utils.filter_values
def data_quality_note(self, key, value):
    """Data Quality Note."""
    field_map = {
        'a': 'attribute_accuracy_report',
        'b': 'attribute_accuracy_value',
        'c': 'attribute_accuracy_explanation',
        'd': 'logical_consistency_report',
        'e': 'completeness_report',
        'f': 'horizontal_position_accuracy_report',
        'g': 'horizontal_position_accuracy_value',
        'h': 'horizontal_position_accuracy_explanation',
        'i': 'vertical_positional_accuracy_report',
        'j': 'vertical_positional_accuracy_value',
        'k': 'vertical_positional_accuracy_explanation',
        'm': 'cloud_cover',
        'u': 'uniform_resource_identifier',
        'z': 'display_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'attribute_accuracy_report': value.get('a'),
        'attribute_accuracy_value': utils.force_list(
            value.get('b')
        ),
        'attribute_accuracy_explanation': utils.force_list(
            value.get('c')
        ),
        'logical_consistency_report': value.get('d'),
        'completeness_report': value.get('e'),
        'horizontal_position_accuracy_report': value.get('f'),
        'horizontal_position_accuracy_value': utils.force_list(
            value.get('g')
        ),
        'horizontal_position_accuracy_explanation': utils.force_list(
            value.get('h')
        ),
        'vertical_positional_accuracy_report': value.get('i'),
        'vertical_positional_accuracy_value': utils.force_list(
            value.get('j')
        ),
        'vertical_positional_accuracy_explanation': utils.force_list(
            value.get('k')
        ),
        'cloud_cover': value.get('m'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('numbering_peculiarities_note', '^515__')
@utils.for_each_value
@utils.filter_values
def numbering_peculiarities_note(self, key, value):
    """Numbering Peculiarities Note."""
    field_map = {
        'a': 'numbering_peculiarities_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
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


@marc21.over('type_of_computer_file_or_data_note', '^516[_8]_')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    """Type of Computer File or Data Note."""
    indicator_map1 = {
        '_': 'Type of file',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'type_of_computer_file_or_data_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_computer_file_or_data_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('date_time_and_place_of_an_event_note', '^518__')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event_note(self, key, value):
    """Date/Time and Place of an Event Note."""
    field_map = {
        'a': 'date_time_and_place_of_an_event_note',
        'd': 'date_of_event',
        'o': 'other_event_information',
        'p': 'place_of_event',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_time_and_place_of_an_event_note': value.get('a'),
        'date_of_event': utils.force_list(
            value.get('d')
        ),
        'other_event_information': utils.force_list(
            value.get('o')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('summary', '^520[_012348]_')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    """Summary, Etc.."""
    indicator_map1 = {
        '_': 'Summary',
        '0': 'Subject',
        '1': 'Review',
        '2': 'Scope and content',
        '3': 'Abstract',
        '4': 'Content advice',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'summary',
        'b': 'expansion_of_summary_note',
        'c': 'assigning_source',
        'u': 'uniform_resource_identifier',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'summary': value.get('a'),
        'expansion_of_summary_note': value.get('b'),
        'assigning_source': value.get('c'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('target_audience_note', '^521[_012348]_')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    """Target Audience Note."""
    indicator_map1 = {
        '_': 'Audience',
        '0': 'Reading grade level',
        '1': 'Interest age level',
        '2': 'Interest grade level',
        '3': 'Special audience characteristics',
        '4': 'Motivation/interest level',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'target_audience_note',
        'b': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'target_audience_note': utils.force_list(
            value.get('a')
        ),
        'source': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('geographic_coverage_note', '^522[_8]_')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    """Geographic Coverage Note."""
    indicator_map1 = {
        '_': 'Geographic coverage',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'geographic_coverage_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_coverage_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('preferred_citation_of_described_materials_note', '^524[_8]_')
@utils.for_each_value
@utils.filter_values
def preferred_citation_of_described_materials_note(self, key, value):
    """Preferred Citation of Described Materials Note."""
    indicator_map1 = {
        '_': 'Cite as',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'preferred_citation_of_described_materials_note',
        '2': 'source_of_schema_used',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'preferred_citation_of_described_materials_note': value.get('a'),
        'source_of_schema_used': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('supplement_note', '^525__')
@utils.for_each_value
@utils.filter_values
def supplement_note(self, key, value):
    """Supplement Note."""
    field_map = {
        'a': 'supplement_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'supplement_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('study_program_information_note', '^526[_08]_')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    """Study Program Information Note."""
    indicator_map1 = {
        '0': 'Reading program',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'program_name',
        'b': 'interest_level',
        'c': 'reading_level',
        'd': 'title_point_value',
        'i': 'display_text',
        'x': 'nonpublic_note',
        'z': 'public_note',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'program_name': value.get('a'),
        'interest_level': value.get('b'),
        'reading_level': value.get('c'),
        'title_point_value': value.get('d'),
        'display_text': value.get('i'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('additional_physical_form_available_note', '^530__')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_available_note(self, key, value):
    """Additional Physical Form Available Note."""
    field_map = {
        'a': 'additional_physical_form_available_note',
        'b': 'availability_source',
        'c': 'availability_conditions',
        'd': 'order_number',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'additional_physical_form_available_note': value.get('a'),
        'availability_source': value.get('b'),
        'availability_conditions': value.get('c'),
        'order_number': value.get('d'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('reproduction_note', '^533__')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    """Reproduction Note."""
    field_map = {
        'a': 'type_of_reproduction',
        'b': 'place_of_reproduction',
        'c': 'agency_responsible_for_reproduction',
        'd': 'date_of_reproduction',
        'e': 'physical_description_of_reproduction',
        'f': 'series_statement_of_reproduction',
        'm': 'dates_and_or_sequential_designation_of_issues_reproduced',
        'n': 'note_about_reproduction',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '7': 'fixed_length_data_elements_of_reproduction',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_reproduction': value.get('a'),
        'place_of_reproduction': utils.force_list(
            value.get('b')
        ),
        'agency_responsible_for_reproduction': utils.force_list(
            value.get('c')
        ),
        'date_of_reproduction': value.get('d'),
        'physical_description_of_reproduction': value.get('e'),
        'series_statement_of_reproduction': utils.force_list(
            value.get('f')
        ),
        'dates_and_or_sequential_designation_of_issues_reproduced': utils.force_list(
            value.get('m')
        ),
        'note_about_reproduction': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('original_version_note', '^534__')
@utils.for_each_value
@utils.filter_values
def original_version_note(self, key, value):
    """Original Version Note."""
    field_map = {
        'a': 'main_entry_of_original',
        'b': 'edition_statement_of_original',
        'c': 'publication_distribution_of_original',
        'e': 'physical_description_of_original',
        'f': 'series_statement_of_original',
        'k': 'key_title_of_original',
        'l': 'location_of_original',
        'm': 'material_specific_details',
        'n': 'note_about_original',
        'o': 'other_resource_identifier',
        'p': 'introductory_phrase',
        't': 'title_statement_of_original',
        'x': 'international_standard_serial_number',
        'z': 'international_standard_book_number',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_of_original': value.get('a'),
        'edition_statement_of_original': value.get('b'),
        'publication_distribution_of_original': value.get('c'),
        'physical_description_of_original': value.get('e'),
        'series_statement_of_original': utils.force_list(
            value.get('f')
        ),
        'key_title_of_original': utils.force_list(
            value.get('k')
        ),
        'location_of_original': value.get('l'),
        'material_specific_details': value.get('m'),
        'note_about_original': utils.force_list(
            value.get('n')
        ),
        'other_resource_identifier': utils.force_list(
            value.get('o')
        ),
        'introductory_phrase': value.get('p'),
        'materials_specified': value.get('3'),
        'title_statement_of_original': value.get('t'),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('location_of_originals_duplicates_note', '^535[_12]_')
@utils.for_each_value
@utils.filter_values
def location_of_originals_duplicates_note(self, key, value):
    """Location of Originals/Duplicates Note."""
    indicator_map1 = {
        '1': 'Holder of originals',
        '2': 'Holder of duplicates',
    }

    field_map = {
        'a': 'custodian',
        'b': 'postal_address',
        'c': 'country',
        'd': 'telecommunications_address',
        'g': 'repository_location_code',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('custodial_role')

    return {
        '__order__': tuple(order) if len(order) else None,
        'custodian': value.get('a'),
        'postal_address': utils.force_list(
            value.get('b')
        ),
        'country': utils.force_list(
            value.get('c')
        ),
        'telecommunications_address': utils.force_list(
            value.get('d')
        ),
        'repository_location_code': value.get('g'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'custodial_role': indicator_map1.get(key[3]),
    }


@marc21.over('funding_information_note', '^536__')
@utils.for_each_value
@utils.filter_values
def funding_information_note(self, key, value):
    """Funding Information Note."""
    field_map = {
        'a': 'text_of_note',
        'b': 'contract_number',
        'c': 'grant_number',
        'd': 'undifferentiated_number',
        'e': 'program_element_number',
        'f': 'project_number',
        'g': 'task_number',
        'h': 'work_unit_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'text_of_note': value.get('a'),
        'contract_number': utils.force_list(
            value.get('b')
        ),
        'grant_number': utils.force_list(
            value.get('c')
        ),
        'undifferentiated_number': utils.force_list(
            value.get('d')
        ),
        'program_element_number': utils.force_list(
            value.get('e')
        ),
        'project_number': utils.force_list(
            value.get('f')
        ),
        'task_number': utils.force_list(
            value.get('g')
        ),
        'work_unit_number': utils.force_list(
            value.get('h')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('system_details_note', '^538__')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    """System Details Note."""
    field_map = {
        'a': 'system_details_note',
        'i': 'display_text',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'system_details_note': value.get('a'),
        'display_text': value.get('i'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('terms_governing_use_and_reproduction_note', '^540__')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    field_map = {
        'a': 'terms_governing_use_and_reproduction',
        'b': 'jurisdiction',
        'c': 'authorization',
        'd': 'authorized_users',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'terms_governing_use_and_reproduction': value.get('a'),
        'jurisdiction': value.get('b'),
        'authorization': value.get('c'),
        'authorized_users': value.get('d'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('immediate_source_of_acquisition_note', '^541[_01]_')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Private',
        '1': 'Not private',
    }

    field_map = {
        'a': 'source_of_acquisition',
        'b': 'address',
        'c': 'method_of_acquisition',
        'd': 'date_of_acquisition',
        'e': 'accession_number',
        'f': 'owner',
        'h': 'purchase_price',
        'n': 'extent',
        'o': 'type_of_unit',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_acquisition': value.get('a'),
        'address': value.get('b'),
        'method_of_acquisition': value.get('c'),
        'date_of_acquisition': value.get('d'),
        'accession_number': value.get('e'),
        'owner': value.get('f'),
        'purchase_price': value.get('h'),
        'extent': utils.force_list(
            value.get('n')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('information_relating_to_copyright_status', '^542[_01]_')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    """Information Relating to Copyright Status."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Private',
        '1': 'Not private',
    }

    field_map = {
        'a': 'personal_creator',
        'b': 'personal_creator_death_date',
        'c': 'corporate_creator',
        'd': 'copyright_holder',
        'e': 'copyright_holder_contact_information',
        'f': 'copyright_statement',
        'g': 'copyright_date',
        'h': 'copyright_renewal_date',
        'i': 'publication_date',
        'j': 'creation_date',
        'k': 'publisher',
        'l': 'copyright_status',
        'm': 'publication_status',
        'n': 'note',
        'o': 'research_date',
        'p': 'country_of_publication_or_creation',
        'q': 'supplying_agency',
        'r': 'jurisdiction_of_copyright_assessment',
        's': 'source_of_information',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_creator': value.get('a'),
        'personal_creator_death_date': value.get('b'),
        'corporate_creator': value.get('c'),
        'copyright_holder': utils.force_list(
            value.get('d')
        ),
        'copyright_holder_contact_information': utils.force_list(
            value.get('e')
        ),
        'copyright_statement': utils.force_list(
            value.get('f')
        ),
        'copyright_date': value.get('g'),
        'copyright_renewal_date': utils.force_list(
            value.get('h')
        ),
        'publication_date': value.get('i'),
        'creation_date': value.get('j'),
        'publisher': utils.force_list(
            value.get('k')
        ),
        'copyright_status': value.get('l'),
        'publication_status': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'research_date': value.get('o'),
        'country_of_publication_or_creation': utils.force_list(
            value.get('p')
        ),
        'supplying_agency': value.get('q'),
        'jurisdiction_of_copyright_assessment': value.get('r'),
        'source_of_information': value.get('s'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('location_of_other_archival_materials_note', '^544[_01]_')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    """Location of Other Archival Materials Note."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Associated materials',
        '1': 'Related materials',
    }

    field_map = {
        'a': 'custodian',
        'b': 'address',
        'c': 'country',
        'd': 'title',
        'e': 'provenance',
        'n': 'note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'custodian': utils.force_list(
            value.get('a')
        ),
        'address': utils.force_list(
            value.get('b')
        ),
        'country': utils.force_list(
            value.get('c')
        ),
        'title': utils.force_list(
            value.get('d')
        ),
        'provenance': utils.force_list(
            value.get('e')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relationship': indicator_map1.get(key[3]),
    }


@marc21.over('biographical_or_historical_data', '^545[_01]_')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Biographical sketch',
        '1': 'Administrative history',
    }

    field_map = {
        'a': 'biographical_or_historical_data',
        'b': 'expansion',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_data')

    return {
        '__order__': tuple(order) if len(order) else None,
        'biographical_or_historical_data': value.get('a'),
        'expansion': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_data': indicator_map1.get(key[3]),
    }


@marc21.over('language_note', '^546__')
@utils.for_each_value
@utils.filter_values
def language_note(self, key, value):
    """Language Note."""
    field_map = {
        'a': 'language_note',
        'b': 'information_code_or_alphabet',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_note': value.get('a'),
        'information_code_or_alphabet': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('former_title_complexity_note', '^547__')
@utils.for_each_value
@utils.filter_values
def former_title_complexity_note(self, key, value):
    """Former Title Complexity Note."""
    field_map = {
        'a': 'former_title_complexity_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'former_title_complexity_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('issuing_body_note', '^550__')
@utils.for_each_value
@utils.filter_values
def issuing_body_note(self, key, value):
    """Issuing Body Note."""
    field_map = {
        'a': 'issuing_body_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'issuing_body_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('entity_and_attribute_information_note', '^552__')
@utils.for_each_value
@utils.filter_values
def entity_and_attribute_information_note(self, key, value):
    """Entity and Attribute Information Note."""
    field_map = {
        'a': 'entity_type_label',
        'b': 'entity_type_definition_and_source',
        'c': 'attribute_label',
        'd': 'attribute_definition_and_source',
        'e': 'enumerated_domain_value',
        'f': 'enumerated_domain_value_definition_and_source',
        'g': 'range_domain_minimum_and_maximum',
        'h': 'codeset_name_and_source',
        'i': 'unrepresentable_domain',
        'j': 'attribute_units_of_measurement_and_resolution',
        'k': 'beginning_and_ending_date_of_attribute_values',
        'l': 'attribute_value_accuracy',
        'm': 'attribute_value_accuracy_explanation',
        'n': 'attribute_measurement_frequency',
        'o': 'entity_and_attribute_overview',
        'p': 'entity_and_attribute_detail_citation',
        'u': 'uniform_resource_identifier',
        'z': 'display_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'entity_type_label': value.get('a'),
        'entity_type_definition_and_source': value.get('b'),
        'attribute_label': value.get('c'),
        'attribute_definition_and_source': value.get('d'),
        'enumerated_domain_value': utils.force_list(
            value.get('e')
        ),
        'enumerated_domain_value_definition_and_source': utils.force_list(
            value.get('f')
        ),
        'range_domain_minimum_and_maximum': value.get('g'),
        'codeset_name_and_source': value.get('h'),
        'unrepresentable_domain': value.get('i'),
        'attribute_units_of_measurement_and_resolution': value.get('j'),
        'beginning_and_ending_date_of_attribute_values': value.get('k'),
        'attribute_value_accuracy': value.get('l'),
        'attribute_value_accuracy_explanation': value.get('m'),
        'attribute_measurement_frequency': value.get('n'),
        'entity_and_attribute_overview': utils.force_list(
            value.get('o')
        ),
        'entity_and_attribute_detail_citation': utils.force_list(
            value.get('p')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('cumulative_index_finding_aids_note', '^555[_08]_')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    """Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        '_': 'Indexes',
        '0': 'Finding aids',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'cumulative_index_finding_aids_note',
        'b': 'availability_source',
        'c': 'degree_of_control',
        'd': 'bibliographic_reference',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'cumulative_index_finding_aids_note': value.get('a'),
        'availability_source': utils.force_list(
            value.get('b')
        ),
        'degree_of_control': value.get('c'),
        'bibliographic_reference': value.get('d'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('information_about_documentation_note', '^556[_8]_')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    """Information About Documentation Note."""
    indicator_map1 = {
        '_': 'Documentation',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'information_about_documentation_note',
        'z': 'international_standard_book_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'information_about_documentation_note': value.get('a'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('ownership_and_custodial_history', '^561[_01]_')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Private',
        '1': 'Not private',
    }

    field_map = {
        'a': 'history',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'history': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('copy_and_version_identification_note', '^562__')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    """Copy and Version Identification Note."""
    field_map = {
        'a': 'identifying_markings',
        'b': 'copy_identification',
        'c': 'version_identification',
        'd': 'presentation_format',
        'e': 'number_of_copies',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'identifying_markings': utils.force_list(
            value.get('a')
        ),
        'copy_identification': utils.force_list(
            value.get('b')
        ),
        'version_identification': utils.force_list(
            value.get('c')
        ),
        'presentation_format': utils.force_list(
            value.get('d')
        ),
        'number_of_copies': utils.force_list(
            value.get('e')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('binding_information', '^563__')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    """Binding Information."""
    field_map = {
        'a': 'binding_note',
        'u': 'uniform_resource_identifier',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'binding_note': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('case_file_characteristics_note', '^565[_08]_')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    """Case File Characteristics Note."""
    indicator_map1 = {
        '_': 'File size',
        '0': 'Case file characteristics',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'number_of_cases_variables',
        'b': 'name_of_variable',
        'c': 'unit_of_analysis',
        'd': 'universe_of_data',
        'e': 'filing_scheme_or_code',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_of_cases_variables': value.get('a'),
        'name_of_variable': utils.force_list(
            value.get('b')
        ),
        'unit_of_analysis': utils.force_list(
            value.get('c')
        ),
        'universe_of_data': utils.force_list(
            value.get('d')
        ),
        'filing_scheme_or_code': utils.force_list(
            value.get('e')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('methodology_note', '^567[_8]_')
@utils.for_each_value
@utils.filter_values
def methodology_note(self, key, value):
    """Methodology Note."""
    indicator_map1 = {
        '_': 'Methodology',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'methodology_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'methodology_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('linking_entry_complexity_note', '^580__')
@utils.for_each_value
@utils.filter_values
def linking_entry_complexity_note(self, key, value):
    """Linking Entry Complexity Note."""
    field_map = {
        'a': 'linking_entry_complexity_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linking_entry_complexity_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('publications_about_described_materials_note', '^581[_8]_')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    """Publications About Described Materials Note."""
    indicator_map1 = {
        '_': 'Publications',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'publications_about_described_materials_note',
        'z': 'international_standard_book_number',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'publications_about_described_materials_note': value.get('a'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('action_note', '^583[_01]_')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Private',
        '1': 'Not private',
    }

    field_map = {
        'a': 'action',
        'b': 'action_identification',
        'c': 'time_date_of_action',
        'd': 'action_interval',
        'e': 'contingency_for_action',
        'f': 'authorization',
        'h': 'jurisdiction',
        'i': 'method_of_action',
        'j': 'site_of_action',
        'k': 'action_agent',
        'l': 'status',
        'n': 'extent',
        'o': 'type_of_unit',
        'u': 'uniform_resource_identifier',
        'x': 'nonpublic_note',
        'z': 'public_note',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('privacy')

    return {
        '__order__': tuple(order) if len(order) else None,
        'action': value.get('a'),
        'action_identification': utils.force_list(
            value.get('b')
        ),
        'time_date_of_action': utils.force_list(
            value.get('c')
        ),
        'action_interval': utils.force_list(
            value.get('d')
        ),
        'contingency_for_action': utils.force_list(
            value.get('e')
        ),
        'authorization': utils.force_list(
            value.get('f')
        ),
        'jurisdiction': utils.force_list(
            value.get('h')
        ),
        'method_of_action': utils.force_list(
            value.get('i')
        ),
        'site_of_action': utils.force_list(
            value.get('j')
        ),
        'action_agent': utils.force_list(
            value.get('k')
        ),
        'status': utils.force_list(
            value.get('l')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21.over('accumulation_and_frequency_of_use_note', '^584__')
@utils.for_each_value
@utils.filter_values
def accumulation_and_frequency_of_use_note(self, key, value):
    """Accumulation and Frequency of Use Note."""
    field_map = {
        'a': 'accumulation',
        'b': 'frequency_of_use',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'accumulation': utils.force_list(
            value.get('a')
        ),
        'frequency_of_use': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('exhibitions_note', '^585__')
@utils.for_each_value
@utils.filter_values
def exhibitions_note(self, key, value):
    """Exhibitions Note."""
    field_map = {
        'a': 'exhibitions_note',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'exhibitions_note': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('awards_note', '^586[_8]_')
@utils.for_each_value
@utils.filter_values
def awards_note(self, key, value):
    """Awards Note."""
    indicator_map1 = {
        '_': 'Awards',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'awards_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'awards_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('source_of_description_note', '^588[_01]_')
@utils.for_each_value
@utils.filter_values
def source_of_description_note(self, key, value):
    """Source of Description Note."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Source of description',
        '1': 'Latest issue consulted',
    }

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
        'display_constant_controller': indicator_map1.get(key[3])
    }
