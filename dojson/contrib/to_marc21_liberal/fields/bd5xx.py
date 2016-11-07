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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('500', '^general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_general_note(self, key, value):
    """Reverse - General Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'materials_specified': '3',
        'general_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '3': value.get('materials_specified'),
        'a': value.get('general_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('501', '^with_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_with_note(self, key, value):
    """Reverse - With Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'with_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('with_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('502', '^dissertation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dissertation_note(self, key, value):
    """Reverse - Dissertation Note."""
    field_map = {
        'linkage': '6',
        'year_degree_granted': 'd',
        'name_of_granting_institution': 'c',
        'dissertation_note': 'a',
        'field_link_and_sequence_number': '8',
        'degree_type': 'b',
        'dissertation_identifier': 'o',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('year_degree_granted'),
        'c': value.get('name_of_granting_institution'),
        'a': value.get('dissertation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('degree_type'),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('504', '^bibliography_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_bibliography_note(self, key, value):
    """Reverse - Bibliography, Etc. Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'number_of_references': 'b',
        'bibliography_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_references'),
        'a': value.get('bibliography_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('505', '^formatted_contents_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_formatted_contents_note(self, key, value):
    """Reverse - Formatted Contents Note."""
    indicator_map1 = {"Contents": "0", "Incomplete contents": "1", "No display constant generated": "8", "Partial contents": "2"}
    indicator_map2 = {"Basic": "_", "Enhanced": "0"}
    field_map = {
        'linkage': '6',
        'title': 't',
        'uniform_resource_identifier': 'u',
        'formatted_contents_note': 'a',
        'field_link_and_sequence_number': '8',
        'statement_of_responsibility': 'r',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'level_of_content_designation'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        't': utils.reverse_force_list(
            value.get('title')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': value.get('formatted_contents_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': indicator_map2.get(value.get('level_of_content_designation'), value.get('level_of_content_designation', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('506', '^restrictions_on_access_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_restrictions_on_access_note(self, key, value):
    """Reverse - Restrictions on Access Note."""
    indicator_map1 = {"No information provided": "_", "No restrictions": "0", "Restrictions apply": "1"}
    field_map = {
        'linkage': '6',
        'authorized_users': 'd',
        'materials_specified': '3',
        'physical_access_provisions': 'c',
        'authorization': 'e',
        'jurisdiction': 'b',
        'terms_governing_access': 'a',
        'standardized_terminology_for_access_restriction': 'f',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['restriction', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'a': value.get('terms_governing_access'),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('restriction'), value.get('restriction', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('507', '^scale_note_for_graphic_material$')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'remainder_of_scale_note': 'b',
        'representative_fraction_of_scale_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('remainder_of_scale_note'),
        'a': value.get('representative_fraction_of_scale_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('508', '^creation_production_credits_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creation_production_credits_note(self, key, value):
    """Reverse - Creation/Production Credits Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'creation_production_credits_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('creation_production_credits_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('510', '^citation_references_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_citation_references_note(self, key, value):
    """Reverse - Citation/References Note."""
    indicator_map1 = {"Coverage complete": "1", "Coverage is selective": "2", "Coverage unknown": "0", "Location in source given": "4", "Location in source not given": "3"}
    field_map = {
        'linkage': '6',
        'international_standard_serial_number': 'x',
        'materials_specified': '3',
        'location_within_source': 'c',
        'name_of_source': 'a',
        'field_link_and_sequence_number': '8',
        'coverage_of_source': 'b',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['coverage_location_in_source', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': value.get('international_standard_serial_number'),
        '3': value.get('materials_specified'),
        'c': value.get('location_within_source'),
        'a': value.get('name_of_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('coverage_of_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('coverage_location_in_source'), value.get('coverage_location_in_source', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('511', '^participant_or_performer_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_participant_or_performer_note(self, key, value):
    """Reverse - Participant or Performer Note."""
    indicator_map1 = {"Cast": "1", "No display constant generated": "0"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'participant_or_performer_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('participant_or_performer_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('513', '^type_of_report_and_period_covered_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'period_covered': 'b',
        'type_of_report': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('period_covered'),
        'a': value.get('type_of_report'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('514', '^data_quality_note$')
@utils.filter_values
def reverse_data_quality_note(self, key, value):
    """Reverse - Data Quality Note."""
    field_map = {
        'linkage': '6',
        'vertical_positional_accuracy_value': 'j',
        'logical_consistency_report': 'd',
        'uniform_resource_identifier': 'u',
        'attribute_accuracy_explanation': 'c',
        'display_note': 'z',
        'completeness_report': 'e',
        'attribute_accuracy_value': 'b',
        'attribute_accuracy_report': 'a',
        'horizontal_position_accuracy_explanation': 'h',
        'horizontal_position_accuracy_report': 'f',
        'cloud_cover': 'm',
        'field_link_and_sequence_number': '8',
        'vertical_positional_accuracy_explanation': 'k',
        'vertical_positional_accuracy_report': 'i',
        'horizontal_position_accuracy_value': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'd': value.get('logical_consistency_report'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'e': value.get('completeness_report'),
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'a': value.get('attribute_accuracy_report'),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        'f': value.get('horizontal_position_accuracy_report'),
        'm': value.get('cloud_cover'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'i': value.get('vertical_positional_accuracy_report'),
        'g': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_value')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('515', '^numbering_peculiarities_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numbering_peculiarities_note(self, key, value):
    """Reverse - Numbering Peculiarities Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'numbering_peculiarities_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('numbering_peculiarities_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('516', '^type_of_computer_file_or_data_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_computer_file_or_data_note(self, key, value):
    """Reverse - Type of Computer File or Data Note."""
    indicator_map1 = {"No display constant generated": "8", "Type of file": "_"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'type_of_computer_file_or_data_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('type_of_computer_file_or_data_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('518', '^date_time_and_place_of_an_event_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    field_map = {
        'linkage': '6',
        'date_of_event': 'd',
        'source_of_term': '2',
        'materials_specified': '3',
        'date_time_and_place_of_an_event_note': 'a',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'place_of_event': 'p',
        'other_event_information': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('date_time_and_place_of_an_event_note'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('520', '^summary$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {"Abstract": "3", "Content advice": "4", "No display constant generated": "8", "Review": "1", "Scope and content": "2", "Subject": "0", "Summary": "_"}
    field_map = {
        'linkage': '6',
        'source': '2',
        'materials_specified': '3',
        'assigning_source': 'c',
        'summary': 'a',
        'field_link_and_sequence_number': '8',
        'expansion_of_summary_note': 'b',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source'),
        '3': value.get('materials_specified'),
        'c': value.get('assigning_source'),
        'a': value.get('summary'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('expansion_of_summary_note'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('521', '^target_audience_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {"Audience": "_", "Interest age level": "1", "Interest grade level": "2", "Motivation/interest level": "4", "No display constant generated": "8", "Reading grade level": "0", "Special audience characteristics": "3"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source': 'b',
        'materials_specified': '3',
        'target_audience_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source'),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('target_audience_note')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('522', '^geographic_coverage_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {"Geographic coverage": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_coverage_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('geographic_coverage_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('524', '^preferred_citation_of_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preferred_citation_of_described_materials_note(self, key, value):
    """Reverse - Preferred Citation of Described Materials Note."""
    indicator_map1 = {"Cite as": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source_of_schema_used': '2',
        'materials_specified': '3',
        'preferred_citation_of_described_materials_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_schema_used'),
        '3': value.get('materials_specified'),
        'a': value.get('preferred_citation_of_described_materials_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('525', '^supplement_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'supplement_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('supplement_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('526', '^study_program_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_study_program_information_note(self, key, value):
    """Reverse - Study Program Information Note."""
    indicator_map1 = {"No display constant generated": "8", "Reading program": "0"}
    field_map = {
        'linkage': '6',
        'public_note': 'z',
        'title_point_value': 'd',
        'nonpublic_note': 'x',
        'reading_level': 'c',
        'program_name': 'a',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'interest_level': 'b',
        'display_text': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'd': value.get('title_point_value'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'c': value.get('reading_level'),
        'a': value.get('program_name'),
        '5': value.get('institution_to_which_field_applies'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('interest_level'),
        'i': value.get('display_text'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('530', '^additional_physical_form_available_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    field_map = {
        'linkage': '6',
        'order_number': 'd',
        'materials_specified': '3',
        'availability_conditions': 'c',
        'additional_physical_form_available_note': 'a',
        'field_link_and_sequence_number': '8',
        'availability_source': 'b',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('order_number'),
        '3': value.get('materials_specified'),
        'c': value.get('availability_conditions'),
        'a': value.get('additional_physical_form_available_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('availability_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('533', '^reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_reproduction_note(self, key, value):
    """Reverse - Reproduction Note."""
    field_map = {
        'linkage': '6',
        'date_of_reproduction': 'd',
        'materials_specified': '3',
        'agency_responsible_for_reproduction': 'c',
        'physical_description_of_reproduction': 'e',
        'place_of_reproduction': 'b',
        'type_of_reproduction': 'a',
        'series_statement_of_reproduction': 'f',
        'fixed_length_data_elements_of_reproduction': '7',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'note_about_reproduction': 'n',
        'dates_and_or_sequential_designation_of_issues_reproduced': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('date_of_reproduction'),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'e': value.get('physical_description_of_reproduction'),
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        'a': value.get('type_of_reproduction'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
        ),
        'm': utils.reverse_force_list(
            value.get('dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('534', '^original_version_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_version_note(self, key, value):
    """Reverse - Original Version Note."""
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'publication_distribution_of_original': 'c',
        'location_of_original': 'l',
        'international_standard_book_number': 'z',
        'physical_description_of_original': 'e',
        'edition_statement_of_original': 'b',
        'other_resource_identifier': 'o',
        'international_standard_serial_number': 'x',
        'main_entry_of_original': 'a',
        'series_statement_of_original': 'f',
        'title_statement_of_original': 't',
        'introductory_phrase': 'p',
        'field_link_and_sequence_number': '8',
        'key_title_of_original': 'k',
        'note_about_original': 'n',
        'material_specific_details': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'c': value.get('publication_distribution_of_original'),
        'l': value.get('location_of_original'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'e': value.get('physical_description_of_original'),
        'b': value.get('edition_statement_of_original'),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        'a': value.get('main_entry_of_original'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        't': value.get('title_statement_of_original'),
        'p': value.get('introductory_phrase'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
        'm': value.get('material_specific_details'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('535', '^location_of_originals_duplicates_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_originals_duplicates_note(self, key, value):
    """Reverse - Location of Originals/Duplicates Note."""
    indicator_map1 = {"Holder of duplicates": "2", "Holder of originals": "1"}
    field_map = {
        'linkage': '6',
        'telecommunications_address': 'd',
        'materials_specified': '3',
        'country': 'c',
        'custodian': 'a',
        'field_link_and_sequence_number': '8',
        'postal_address': 'b',
        'repository_location_code': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['custodial_role', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'a': value.get('custodian'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        'g': value.get('repository_location_code'),
        '$ind1': indicator_map1.get(value.get('custodial_role'), value.get('custodial_role', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('536', '^funding_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_funding_information_note(self, key, value):
    """Reverse - Funding Information Note."""
    field_map = {
        'linkage': '6',
        'work_unit_number': 'h',
        'undifferentiated_number': 'd',
        'project_number': 'f',
        'grant_number': 'c',
        'text_of_note': 'a',
        'field_link_and_sequence_number': '8',
        'program_element_number': 'e',
        'contract_number': 'b',
        'task_number': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'c': utils.reverse_force_list(
            value.get('grant_number')
        ),
        'a': value.get('text_of_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        'g': utils.reverse_force_list(
            value.get('task_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('538', '^system_details_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_note(self, key, value):
    """Reverse - System Details Note."""
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'system_details_note': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'display_text': 'i',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('system_details_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': value.get('display_text'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('540', '^terms_governing_use_and_reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_terms_governing_use_and_reproduction_note(self, key, value):
    """Reverse - Terms Governing Use and Reproduction Note."""
    field_map = {
        'linkage': '6',
        'authorized_users': 'd',
        'materials_specified': '3',
        'authorization': 'c',
        'terms_governing_use_and_reproduction': 'a',
        'jurisdiction': 'b',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('authorized_users'),
        '3': value.get('materials_specified'),
        'c': value.get('authorization'),
        'a': value.get('terms_governing_use_and_reproduction'),
        'b': value.get('jurisdiction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('541', '^immediate_source_of_acquisition_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_immediate_source_of_acquisition_note(self, key, value):
    """Reverse - Immediate Source of Acquisition Note."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'linkage': '6',
        'date_of_acquisition': 'd',
        'materials_specified': '3',
        'method_of_acquisition': 'c',
        'accession_number': 'e',
        'address': 'b',
        'type_of_unit': 'o',
        'source_of_acquisition': 'a',
        'purchase_price': 'h',
        'owner': 'f',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'extent': 'n',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('date_of_acquisition'),
        '3': value.get('materials_specified'),
        'c': value.get('method_of_acquisition'),
        'e': value.get('accession_number'),
        'b': value.get('address'),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'a': value.get('source_of_acquisition'),
        'h': value.get('purchase_price'),
        'f': value.get('owner'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), value.get('privacy', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('542', '^information_relating_to_copyright_status$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_relating_to_copyright_status(self, key, value):
    """Reverse - Information Relating to Copyright Status."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'linkage': '6',
        'creation_date': 'j',
        'copyright_holder': 'd',
        'materials_specified': '3',
        'corporate_creator': 'c',
        'source_of_information': 's',
        'supplying_agency': 'q',
        'personal_creator': 'a',
        'copyright_statement': 'f',
        'country_of_publication_or_creation': 'p',
        'field_link_and_sequence_number': '8',
        'publisher': 'k',
        'copyright_status': 'l',
        'uniform_resource_identifier': 'u',
        'copyright_holder_contact_information': 'e',
        'personal_creator_death_date': 'b',
        'research_date': 'o',
        'jurisdiction_of_copyright_assessment': 'r',
        'publication_date': 'i',
        'copyright_renewal_date': 'h',
        'copyright_date': 'g',
        'note': 'n',
        'publication_status': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'j': value.get('creation_date'),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        '3': value.get('materials_specified'),
        'c': value.get('corporate_creator'),
        's': value.get('source_of_information'),
        'q': value.get('supplying_agency'),
        'a': value.get('personal_creator'),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'l': value.get('copyright_status'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'b': value.get('personal_creator_death_date'),
        'o': value.get('research_date'),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        'i': value.get('publication_date'),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        'g': value.get('copyright_date'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'm': value.get('publication_status'),
        '$ind1': indicator_map1.get(value.get('privacy'), value.get('privacy', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('544', '^location_of_other_archival_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {"Associated materials": "0", "No information provided": "_", "Related materials": "1"}
    field_map = {
        'linkage': '6',
        'title': 'd',
        'materials_specified': '3',
        'country': 'c',
        'custodian': 'a',
        'field_link_and_sequence_number': '8',
        'provenance': 'e',
        'address': 'b',
        'note': 'n',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['relationship', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('country')
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
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '$ind1': indicator_map1.get(value.get('relationship'), value.get('relationship', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('545', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {"Administrative history": "1", "Biographical sketch": "0", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'expansion': 'b',
        'uniform_resource_identifier': 'u',
        'biographical_or_historical_data': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_data', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('expansion'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': value.get('biographical_or_historical_data'),
        '$ind1': indicator_map1.get(value.get('type_of_data'), value.get('type_of_data', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('546', '^language_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_note(self, key, value):
    """Reverse - Language Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'information_code_or_alphabet': 'b',
        'materials_specified': '3',
        'language_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('language_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('547', '^former_title_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title_complexity_note(self, key, value):
    """Reverse - Former Title Complexity Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'former_title_complexity_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('former_title_complexity_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('550', '^issuing_body_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issuing_body_note(self, key, value):
    """Reverse - Issuing Body Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'issuing_body_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('issuing_body_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('552', '^entity_and_attribute_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_entity_and_attribute_information_note(self, key, value):
    """Reverse - Entity and Attribute Information Note."""
    field_map = {
        'linkage': '6',
        'attribute_units_of_measurement_and_resolution': 'j',
        'attribute_definition_and_source': 'd',
        'uniform_resource_identifier': 'u',
        'attribute_label': 'c',
        'attribute_value_accuracy': 'l',
        'display_note': 'z',
        'enumerated_domain_value': 'e',
        'entity_type_definition_and_source': 'b',
        'entity_and_attribute_overview': 'o',
        'attribute_measurement_frequency': 'n',
        'entity_type_label': 'a',
        'codeset_name_and_source': 'h',
        'enumerated_domain_value_definition_and_source': 'f',
        'entity_and_attribute_detail_citation': 'p',
        'attribute_value_accuracy_explanation': 'm',
        'field_link_and_sequence_number': '8',
        'beginning_and_ending_date_of_attribute_values': 'k',
        'unrepresentable_domain': 'i',
        'range_domain_minimum_and_maximum': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'd': value.get('attribute_definition_and_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('attribute_label'),
        'l': value.get('attribute_value_accuracy'),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'b': value.get('entity_type_definition_and_source'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        'n': value.get('attribute_measurement_frequency'),
        'a': value.get('entity_type_label'),
        'h': value.get('codeset_name_and_source'),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        'm': value.get('attribute_value_accuracy_explanation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'i': value.get('unrepresentable_domain'),
        'g': value.get('range_domain_minimum_and_maximum'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('555', '^cumulative_index_finding_aids_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {"Finding aids": "0", "Indexes": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'bibliographic_reference': 'd',
        'materials_specified': '3',
        'degree_of_control': 'c',
        'cumulative_index_finding_aids_note': 'a',
        'field_link_and_sequence_number': '8',
        'availability_source': 'b',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('bibliographic_reference'),
        '3': value.get('materials_specified'),
        'c': value.get('degree_of_control'),
        'a': value.get('cumulative_index_finding_aids_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('availability_source')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('556', '^information_about_documentation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {"Documentation": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'international_standard_book_number': 'z',
        'information_about_documentation_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('information_about_documentation_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('561', '^ownership_and_custodial_history$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'history': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('history'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), value.get('privacy', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('562', '^copy_and_version_identification_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copy_and_version_identification_note(self, key, value):
    """Reverse - Copy and Version Identification Note."""
    field_map = {
        'linkage': '6',
        'presentation_format': 'd',
        'materials_specified': '3',
        'version_identification': 'c',
        'identifying_markings': 'a',
        'copy_identification': 'b',
        'field_link_and_sequence_number': '8',
        'number_of_copies': 'e',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        'a': utils.reverse_force_list(
            value.get('identifying_markings')
        ),
        'b': utils.reverse_force_list(
            value.get('copy_identification')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('563', '^binding_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_binding_information(self, key, value):
    """Reverse - Binding Information."""
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'binding_note': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': value.get('binding_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('565', '^case_file_characteristics_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_case_file_characteristics_note(self, key, value):
    """Reverse - Case File Characteristics Note."""
    indicator_map1 = {"Case file characteristics": "0", "File size": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'universe_of_data': 'd',
        'materials_specified': '3',
        'unit_of_analysis': 'c',
        'number_of_cases_variables': 'a',
        'field_link_and_sequence_number': '8',
        'filing_scheme_or_code': 'e',
        'name_of_variable': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')
        ),
        'a': value.get('number_of_cases_variables'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_variable')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('567', '^methodology_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_methodology_note(self, key, value):
    """Reverse - Methodology Note."""
    indicator_map1 = {"Methodology": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'methodology_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('methodology_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('580', '^linking_entry_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'linking_entry_complexity_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('linking_entry_complexity_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('581', '^publications_about_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publications_about_described_materials_note(self, key, value):
    """Reverse - Publications About Described Materials Note."""
    indicator_map1 = {"No display constant generated": "8", "Publications": "_"}
    field_map = {
        'international_standard_book_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'publications_about_described_materials_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
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
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('583', '^action_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {"No information provided": "_", "Not private": "1", "Private": "0"}
    field_map = {
        'linkage': '6',
        'site_of_action': 'j',
        'action_interval': 'd',
        'nonpublic_note': 'x',
        'materials_specified': '3',
        'time_date_of_action': 'c',
        'status': 'l',
        'public_note': 'z',
        'contingency_for_action': 'e',
        'action_identification': 'b',
        'type_of_unit': 'o',
        'extent': 'n',
        'action': 'a',
        'jurisdiction': 'h',
        'authorization': 'f',
        'source_of_term': '2',
        'uniform_resource_identifier': 'u',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'method_of_action': 'i',
        'action_agent': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'a': value.get('action'),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), value.get('privacy', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('584', '^accumulation_and_frequency_of_use_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_accumulation_and_frequency_of_use_note(self, key, value):
    """Reverse - Accumulation and Frequency of Use Note."""
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'accumulation': 'a',
        'frequency_of_use': 'b',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('585', '^exhibitions_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_exhibitions_note(self, key, value):
    """Reverse - Exhibitions Note."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'materials_specified': '3',
        'exhibitions_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '3': value.get('materials_specified'),
        'a': value.get('exhibitions_note'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('586', '^awards_note$')
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

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('awards_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('588', '^source_of_description_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    indicator_map1 = {"Latest issue consulted": "1", "No information provided": "_", "Source of description": "0"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'source_of_description_note': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('source_of_description_note'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
