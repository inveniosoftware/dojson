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
        'institution_to_which_field_applies': '5',
        'general_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('general_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'institution_to_which_field_applies': '5',
        'with_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('with_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'dissertation_identifier': 'o',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'degree_type': 'b',
        'year_degree_granted': 'd',
        'dissertation_note': 'a',
        'name_of_granting_institution': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'b': value.get('degree_type'),
        'd': value.get('year_degree_granted'),
        'a': value.get('dissertation_note'),
        'c': value.get('name_of_granting_institution'),
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
        'number_of_references': 'b',
        'field_link_and_sequence_number': '8',
        'bibliography_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('number_of_references'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('bibliography_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'miscellaneous_information': 'g',
        'title': 't',
        'formatted_contents_note': 'a',
        'statement_of_responsibility': 'r',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'level_of_content_designation'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': utils.reverse_force_list(
            value.get('title')
        ),
        'a': value.get('formatted_contents_note'),
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'jurisdiction': 'b',
        'terms_governing_access': 'a',
        'standardized_terminology_for_access_restriction': 'f',
        'source_of_term': '2',
        'authorized_users': 'd',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'physical_access_provisions': 'c',
        'authorization': 'e',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['restriction', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'a': value.get('terms_governing_access'),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        '2': value.get('source_of_term'),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
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
        'remainder_of_scale_note': 'b',
        'field_link_and_sequence_number': '8',
        'representative_fraction_of_scale_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('remainder_of_scale_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('representative_fraction_of_scale_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'creation_production_credits_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('creation_production_credits_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'coverage_of_source': 'b',
        'name_of_source': 'a',
        'location_within_source': 'c',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['coverage_location_in_source', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': value.get('international_standard_serial_number'),
        '6': value.get('linkage'),
        'b': value.get('coverage_of_source'),
        'a': value.get('name_of_source'),
        'c': value.get('location_within_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'participant_or_performer_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('participant_or_performer_note'),
        '6': value.get('linkage'),
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
        'period_covered': 'b',
        'field_link_and_sequence_number': '8',
        'type_of_report': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('period_covered'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('type_of_report'),
        '6': value.get('linkage'),
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
        'vertical_positional_accuracy_explanation': 'k',
        'horizontal_position_accuracy_explanation': 'h',
        'linkage': '6',
        'attribute_accuracy_value': 'b',
        'attribute_accuracy_report': 'a',
        'horizontal_position_accuracy_report': 'f',
        'vertical_positional_accuracy_value': 'j',
        'logical_consistency_report': 'd',
        'attribute_accuracy_explanation': 'c',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'horizontal_position_accuracy_value': 'g',
        'completeness_report': 'e',
        'cloud_cover': 'm',
        'vertical_positional_accuracy_report': 'i',
        'display_note': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'a': value.get('attribute_accuracy_report'),
        'f': value.get('horizontal_position_accuracy_report'),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'd': value.get('logical_consistency_report'),
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'g': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_value')
        ),
        'e': value.get('completeness_report'),
        'm': value.get('cloud_cover'),
        'i': value.get('vertical_positional_accuracy_report'),
        'z': utils.reverse_force_list(
            value.get('display_note')
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
        'field_link_and_sequence_number': '8',
        'numbering_peculiarities_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('numbering_peculiarities_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'type_of_computer_file_or_data_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('type_of_computer_file_or_data_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'other_event_information': 'o',
        'linkage': '6',
        'record_control_number': '0',
        'date_of_event': 'd',
        'source_of_term': '2',
        'date_time_and_place_of_an_event_note': 'a',
        'place_of_event': 'p',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        'a': value.get('date_time_and_place_of_an_event_note'),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'expansion_of_summary_note': 'b',
        'source': '2',
        'summary': 'a',
        'assigning_source': 'c',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('expansion_of_summary_note'),
        '2': value.get('source'),
        'a': value.get('summary'),
        'c': value.get('assigning_source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'source': 'b',
        'field_link_and_sequence_number': '8',
        'target_audience_note': 'a',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('target_audience_note')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'geographic_coverage_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('geographic_coverage_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'source_of_schema_used': '2',
        'preferred_citation_of_described_materials_note': 'a',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_schema_used'),
        'a': value.get('preferred_citation_of_described_materials_note'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'supplement_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('supplement_note'),
        '6': value.get('linkage'),
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
        'reading_level': 'c',
        'institution_to_which_field_applies': '5',
        'nonpublic_note': 'x',
        'linkage': '6',
        'interest_level': 'b',
        'title_point_value': 'd',
        'program_name': 'a',
        'field_link_and_sequence_number': '8',
        'display_text': 'i',
        'public_note': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('reading_level'),
        '5': value.get('institution_to_which_field_applies'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        '6': value.get('linkage'),
        'b': value.get('interest_level'),
        'd': value.get('title_point_value'),
        'a': value.get('program_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': value.get('display_text'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'availability_source': 'b',
        'order_number': 'd',
        'additional_physical_form_available_note': 'a',
        'availability_conditions': 'c',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('availability_source'),
        'd': value.get('order_number'),
        'a': value.get('additional_physical_form_available_note'),
        'c': value.get('availability_conditions'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'dates_and_or_sequential_designation_of_issues_reproduced': 'm',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'place_of_reproduction': 'b',
        'type_of_reproduction': 'a',
        'series_statement_of_reproduction': 'f',
        'date_of_reproduction': 'd',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'agency_responsible_for_reproduction': 'c',
        'note_about_reproduction': 'n',
        'fixed_length_data_elements_of_reproduction': '7',
        'physical_description_of_reproduction': 'e',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'm': utils.reverse_force_list(
            value.get('dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        'a': value.get('type_of_reproduction'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        'd': value.get('date_of_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
        ),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        'e': value.get('physical_description_of_reproduction'),
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
        'key_title_of_original': 'k',
        'material_specific_details': 'm',
        'linkage': '6',
        'location_of_original': 'l',
        'other_resource_identifier': 'o',
        'series_statement_of_original': 'f',
        'title_statement_of_original': 't',
        'main_entry_of_original': 'a',
        'publication_distribution_of_original': 'c',
        'materials_specified': '3',
        'edition_statement_of_original': 'b',
        'field_link_and_sequence_number': '8',
        'note_about_original': 'n',
        'physical_description_of_original': 'e',
        'international_standard_serial_number': 'x',
        'introductory_phrase': 'p',
        'international_standard_book_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'm': value.get('material_specific_details'),
        '6': value.get('linkage'),
        'l': value.get('location_of_original'),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        't': value.get('title_statement_of_original'),
        'a': value.get('main_entry_of_original'),
        'c': value.get('publication_distribution_of_original'),
        '3': value.get('materials_specified'),
        'b': value.get('edition_statement_of_original'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
        'e': value.get('physical_description_of_original'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        'p': value.get('introductory_phrase'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
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
        'field_link_and_sequence_number': '8',
        'repository_location_code': 'g',
        'linkage': '6',
        'postal_address': 'b',
        'telecommunications_address': 'd',
        'custodian': 'a',
        'country': 'c',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['custodial_role', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': value.get('repository_location_code'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        'a': value.get('custodian'),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        '3': value.get('materials_specified'),
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
        'work_unit_number': 'h',
        'field_link_and_sequence_number': '8',
        'task_number': 'g',
        'linkage': '6',
        'program_element_number': 'e',
        'contract_number': 'b',
        'undifferentiated_number': 'd',
        'project_number': 'f',
        'text_of_note': 'a',
        'grant_number': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('task_number')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'a': value.get('text_of_note'),
        'c': utils.reverse_force_list(
            value.get('grant_number')
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
        'institution_to_which_field_applies': '5',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'system_details_note': 'a',
        'field_link_and_sequence_number': '8',
        'display_text': 'i',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'a': value.get('system_details_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': value.get('display_text'),
        '3': value.get('materials_specified'),
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
        'authorization': 'c',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'jurisdiction': 'b',
        'authorized_users': 'd',
        'terms_governing_use_and_reproduction': 'a',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('authorization'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'b': value.get('jurisdiction'),
        'd': value.get('authorized_users'),
        'a': value.get('terms_governing_use_and_reproduction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'type_of_unit': 'o',
        'purchase_price': 'h',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'address': 'b',
        'source_of_acquisition': 'a',
        'owner': 'f',
        'date_of_acquisition': 'd',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'method_of_acquisition': 'c',
        'extent': 'n',
        'accession_number': 'e',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'h': value.get('purchase_price'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'b': value.get('address'),
        'a': value.get('source_of_acquisition'),
        'f': value.get('owner'),
        'd': value.get('date_of_acquisition'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'c': value.get('method_of_acquisition'),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'e': value.get('accession_number'),
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
        'publication_status': 'm',
        'copyright_renewal_date': 'h',
        'source_of_information': 's',
        'linkage': '6',
        'personal_creator_death_date': 'b',
        'copyright_holder': 'd',
        'copyright_holder_contact_information': 'e',
        'jurisdiction_of_copyright_assessment': 'r',
        'research_date': 'o',
        'copyright_date': 'g',
        'creation_date': 'j',
        'country_of_publication_or_creation': 'p',
        'publication_date': 'i',
        'publisher': 'k',
        'copyright_status': 'l',
        'copyright_statement': 'f',
        'personal_creator': 'a',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'supplying_agency': 'q',
        'corporate_creator': 'c',
        'note': 'n',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'm': value.get('publication_status'),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        's': value.get('source_of_information'),
        '6': value.get('linkage'),
        'b': value.get('personal_creator_death_date'),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        'o': value.get('research_date'),
        'g': value.get('copyright_date'),
        'j': value.get('creation_date'),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        'i': value.get('publication_date'),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'l': value.get('copyright_status'),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        'a': value.get('personal_creator'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'q': value.get('supplying_agency'),
        'c': value.get('corporate_creator'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
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


@to_marc21_liberal.over('544', '^location_of_other_archival_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {"Associated materials": "0", "No information provided": "_", "Related materials": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'linkage': '6',
        'provenance': 'e',
        'address': 'b',
        'title': 'd',
        'custodian': 'a',
        'country': 'c',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['relationship', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('provenance')
        ),
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        'a': utils.reverse_force_list(
            value.get('custodian')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        '3': value.get('materials_specified'),
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
        'expansion': 'b',
        'field_link_and_sequence_number': '8',
        'biographical_or_historical_data': 'a',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_data', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('expansion'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('biographical_or_historical_data'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
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
        'information_code_or_alphabet': 'b',
        'field_link_and_sequence_number': '8',
        'language_note': 'a',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('language_note'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'former_title_complexity_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('former_title_complexity_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'issuing_body_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('issuing_body_note'),
        '6': value.get('linkage'),
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
        'beginning_and_ending_date_of_attribute_values': 'k',
        'codeset_name_and_source': 'h',
        'entity_and_attribute_overview': 'o',
        'linkage': '6',
        'entity_type_definition_and_source': 'b',
        'entity_type_label': 'a',
        'enumerated_domain_value_definition_and_source': 'f',
        'attribute_units_of_measurement_and_resolution': 'j',
        'attribute_definition_and_source': 'd',
        'attribute_label': 'c',
        'attribute_value_accuracy': 'l',
        'field_link_and_sequence_number': '8',
        'attribute_measurement_frequency': 'n',
        'uniform_resource_identifier': 'u',
        'range_domain_minimum_and_maximum': 'g',
        'enumerated_domain_value': 'e',
        'entity_and_attribute_detail_citation': 'p',
        'attribute_value_accuracy_explanation': 'm',
        'unrepresentable_domain': 'i',
        'display_note': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'h': value.get('codeset_name_and_source'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        '6': value.get('linkage'),
        'b': value.get('entity_type_definition_and_source'),
        'a': value.get('entity_type_label'),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'd': value.get('attribute_definition_and_source'),
        'c': value.get('attribute_label'),
        'l': value.get('attribute_value_accuracy'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': value.get('attribute_measurement_frequency'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'g': value.get('range_domain_minimum_and_maximum'),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        'm': value.get('attribute_value_accuracy_explanation'),
        'i': value.get('unrepresentable_domain'),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'availability_source': 'b',
        'bibliographic_reference': 'd',
        'cumulative_index_finding_aids_note': 'a',
        'degree_of_control': 'c',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('availability_source')
        ),
        'd': value.get('bibliographic_reference'),
        'a': value.get('cumulative_index_finding_aids_note'),
        'c': value.get('degree_of_control'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'information_about_documentation_note': 'a',
        'linkage': '6',
        'international_standard_book_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('information_about_documentation_note'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'history': 'a',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'a': value.get('history'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'version_identification': 'c',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'number_of_copies': 'e',
        'copy_identification': 'b',
        'presentation_format': 'd',
        'identifying_markings': 'a',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        'b': utils.reverse_force_list(
            value.get('copy_identification')
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
        '3': value.get('materials_specified'),
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'binding_note': 'a',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'a': value.get('binding_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'filing_scheme_or_code': 'e',
        'name_of_variable': 'b',
        'universe_of_data': 'd',
        'number_of_cases_variables': 'a',
        'unit_of_analysis': 'c',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_variable')
        ),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')
        ),
        'a': value.get('number_of_cases_variables'),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')
        ),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'methodology_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('methodology_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'linking_entry_complexity_note': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('linking_entry_complexity_note'),
        '6': value.get('linkage'),
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
        'field_link_and_sequence_number': '8',
        'international_standard_book_number': 'z',
        'publications_about_described_materials_note': 'a',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('publications_about_described_materials_note'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'action_agent': 'k',
        'jurisdiction': 'h',
        'institution_to_which_field_applies': '5',
        'type_of_unit': 'o',
        'linkage': '6',
        'nonpublic_note': 'x',
        'action_identification': 'b',
        'action': 'a',
        'authorization': 'f',
        'source_of_term': '2',
        'action_interval': 'd',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'status': 'l',
        'time_date_of_action': 'c',
        'extent': 'n',
        'uniform_resource_identifier': 'u',
        'contingency_for_action': 'e',
        'site_of_action': 'j',
        'method_of_action': 'i',
        'public_note': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['privacy', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'a': value.get('action'),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        '2': value.get('source_of_term'),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
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
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'frequency_of_use': 'b',
        'accumulation': 'a',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
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
        'institution_to_which_field_applies': '5',
        'exhibitions_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('exhibitions_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'field_link_and_sequence_number': '8',
        'awards_note': 'a',
        'linkage': '6',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('awards_note'),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
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
        'institution_to_which_field_applies': '5',
        'source_of_description_note': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('source_of_description_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
