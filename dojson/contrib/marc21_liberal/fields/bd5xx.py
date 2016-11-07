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

from ..model import marc21_liberal


@marc21_liberal.over('general_note', '^500..')
@utils.for_each_value
@utils.filter_values
def general_note(self, key, value):
    """General Note."""
    field_map = {
        '5': 'institution_to_which_field_applies',
        'a': 'general_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': value.get('5'),
        'general_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('with_note', '^501..')
@utils.for_each_value
@utils.filter_values
def with_note(self, key, value):
    """With Note."""
    field_map = {
        '5': 'institution_to_which_field_applies',
        'a': 'with_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': value.get('5'),
        'with_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('dissertation_note', '^502..')
@utils.for_each_value
@utils.filter_values
def dissertation_note(self, key, value):
    """Dissertation Note."""
    field_map = {
        'b': 'degree_type',
        '8': 'field_link_and_sequence_number',
        'o': 'dissertation_identifier',
        'a': 'dissertation_note',
        'd': 'year_degree_granted',
        'g': 'miscellaneous_information',
        '6': 'linkage',
        'c': 'name_of_granting_institution',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'degree_type': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'dissertation_identifier': utils.force_list(
            value.get('o')
        ),
        'dissertation_note': value.get('a'),
        'year_degree_granted': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'name_of_granting_institution': value.get('c'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('bibliography_note', '^504..')
@utils.for_each_value
@utils.filter_values
def bibliography_note(self, key, value):
    """Bibliography, Etc. Note."""
    field_map = {
        'a': 'bibliography_note',
        'b': 'number_of_references',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'bibliography_note': value.get('a'),
        'number_of_references': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('formatted_contents_note', '^505..')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    """Formatted Contents Note."""
    indicator_map1 = {"0": "Contents", "1": "Incomplete contents", "2": "Partial contents", "8": "No display constant generated"}
    indicator_map2 = {"0": "Enhanced", "_": "Basic"}
    field_map = {
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'r': 'statement_of_responsibility',
        't': 'title',
        'a': 'formatted_contents_note',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('level_of_content_designation')

    record_dict = {
        '__order__': order if len(order) else None,
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'statement_of_responsibility': utils.force_list(
            value.get('r')
        ),
        'title': utils.force_list(
            value.get('t')
        ),
        'formatted_contents_note': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        'level_of_content_designation': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('restrictions_on_access_note', '^506..')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    indicator_map1 = {"0": "No restrictions", "1": "Restrictions apply", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'jurisdiction',
        '8': 'field_link_and_sequence_number',
        'e': 'authorization',
        'a': 'terms_governing_access',
        'd': 'authorized_users',
        '3': 'materials_specified',
        '6': 'linkage',
        '2': 'source_of_term',
        'f': 'standardized_terminology_for_access_restriction',
        '5': 'institution_to_which_field_applies',
        'c': 'physical_access_provisions',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('restriction')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'jurisdiction': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authorization': utils.force_list(
            value.get('e')
        ),
        'terms_governing_access': value.get('a'),
        'authorized_users': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'standardized_terminology_for_access_restriction': utils.force_list(
            value.get('f')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'physical_access_provisions': utils.force_list(
            value.get('c')
        ),
        'restriction': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('scale_note_for_graphic_material', '^507..')
@utils.filter_values
def scale_note_for_graphic_material(self, key, value):
    """Scale Note for Graphic Material."""
    field_map = {
        'a': 'representative_fraction_of_scale_note',
        'b': 'remainder_of_scale_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'representative_fraction_of_scale_note': value.get('a'),
        'remainder_of_scale_note': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('creation_production_credits_note', '^508..')
@utils.for_each_value
@utils.filter_values
def creation_production_credits_note(self, key, value):
    """Creation/Production Credits Note."""
    field_map = {
        'a': 'creation_production_credits_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'creation_production_credits_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('citation_references_note', '^510..')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    """Citation/References Note."""
    indicator_map1 = {"0": "Coverage unknown", "1": "Coverage complete", "2": "Coverage is selective", "3": "Location in source not given", "4": "Location in source given"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'coverage_of_source',
        '8': 'field_link_and_sequence_number',
        'x': 'international_standard_serial_number',
        'a': 'name_of_source',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'location_within_source',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('coverage_location_in_source')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'coverage_of_source': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_serial_number': value.get('x'),
        'name_of_source': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'location_within_source': value.get('c'),
        'coverage_location_in_source': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('participant_or_performer_note', '^511..')
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'participant_or_performer_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('type_of_report_and_period_covered_note', '^513..')
@utils.for_each_value
@utils.filter_values
def type_of_report_and_period_covered_note(self, key, value):
    """Type of Report and Period Covered Note."""
    field_map = {
        'a': 'type_of_report',
        'b': 'period_covered',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'type_of_report': value.get('a'),
        'period_covered': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('data_quality_note', '^514..')
@utils.filter_values
def data_quality_note(self, key, value):
    """Data Quality Note."""
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'attribute_accuracy_value',
        '8': 'field_link_and_sequence_number',
        'e': 'completeness_report',
        'a': 'attribute_accuracy_report',
        'd': 'logical_consistency_report',
        'g': 'horizontal_position_accuracy_value',
        'h': 'horizontal_position_accuracy_explanation',
        'j': 'vertical_positional_accuracy_value',
        'f': 'horizontal_position_accuracy_report',
        'k': 'vertical_positional_accuracy_explanation',
        'm': 'cloud_cover',
        'z': 'display_note',
        'c': 'attribute_accuracy_explanation',
        'i': 'vertical_positional_accuracy_report',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'attribute_accuracy_value': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'completeness_report': value.get('e'),
        'attribute_accuracy_report': value.get('a'),
        'logical_consistency_report': value.get('d'),
        'horizontal_position_accuracy_value': utils.force_list(
            value.get('g')
        ),
        'horizontal_position_accuracy_explanation': utils.force_list(
            value.get('h')
        ),
        'vertical_positional_accuracy_value': utils.force_list(
            value.get('j')
        ),
        'horizontal_position_accuracy_report': value.get('f'),
        'vertical_positional_accuracy_explanation': utils.force_list(
            value.get('k')
        ),
        'cloud_cover': value.get('m'),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'attribute_accuracy_explanation': utils.force_list(
            value.get('c')
        ),
        'vertical_positional_accuracy_report': value.get('i'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('numbering_peculiarities_note', '^515..')
@utils.for_each_value
@utils.filter_values
def numbering_peculiarities_note(self, key, value):
    """Numbering Peculiarities Note."""
    field_map = {
        'a': 'numbering_peculiarities_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'numbering_peculiarities_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('type_of_computer_file_or_data_note', '^516..')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    """Type of Computer File or Data Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Type of file"}
    field_map = {
        'a': 'type_of_computer_file_or_data_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'type_of_computer_file_or_data_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('date_time_and_place_of_an_event_note', '^518..')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event_note(self, key, value):
    """Date/Time and Place of an Event Note."""
    field_map = {
        '2': 'source_of_term',
        'p': 'place_of_event',
        '0': 'record_control_number',
        'o': 'other_event_information',
        'd': 'date_of_event',
        '8': 'field_link_and_sequence_number',
        'a': 'date_time_and_place_of_an_event_note',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'other_event_information': utils.force_list(
            value.get('o')
        ),
        'date_of_event': utils.force_list(
            value.get('d')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_time_and_place_of_an_event_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('summary', '^520..')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    """Summary, Etc.."""
    indicator_map1 = {"0": "Subject", "1": "Review", "2": "Scope and content", "3": "Abstract", "4": "Content advice", "8": "No display constant generated", "_": "Summary"}
    field_map = {
        '2': 'source',
        'u': 'uniform_resource_identifier',
        'b': 'expansion_of_summary_note',
        '8': 'field_link_and_sequence_number',
        'a': 'summary',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'assigning_source',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'expansion_of_summary_note': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'summary': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'assigning_source': value.get('c'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('target_audience_note', '^521..')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    """Target Audience Note."""
    indicator_map1 = {"0": "Reading grade level", "1": "Interest age level", "2": "Interest grade level", "3": "Special audience characteristics", "4": "Motivation/interest level", "8": "No display constant generated", "_": "Audience"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'target_audience_note',
        'b': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'target_audience_note': utils.force_list(
            value.get('a')
        ),
        'source': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('geographic_coverage_note', '^522..')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    """Geographic Coverage Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Geographic coverage"}
    field_map = {
        'a': 'geographic_coverage_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_coverage_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('preferred_citation_of_described_materials_note', '^524..')
@utils.for_each_value
@utils.filter_values
def preferred_citation_of_described_materials_note(self, key, value):
    """Preferred Citation of Described Materials Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Cite as"}
    field_map = {
        '2': 'source_of_schema_used',
        'a': 'preferred_citation_of_described_materials_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_schema_used': value.get('2'),
        'preferred_citation_of_described_materials_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('supplement_note', '^525..')
@utils.for_each_value
@utils.filter_values
def supplement_note(self, key, value):
    """Supplement Note."""
    field_map = {
        'a': 'supplement_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'supplement_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('study_program_information_note', '^526..')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    """Study Program Information Note."""
    indicator_map1 = {"0": "Reading program", "8": "No display constant generated"}
    field_map = {
        'a': 'program_name',
        'b': 'interest_level',
        '8': 'field_link_and_sequence_number',
        'z': 'public_note',
        'x': 'nonpublic_note',
        '5': 'institution_to_which_field_applies',
        'd': 'title_point_value',
        '6': 'linkage',
        'i': 'display_text',
        'c': 'reading_level',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'program_name': value.get('a'),
        'interest_level': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'title_point_value': value.get('d'),
        'linkage': value.get('6'),
        'display_text': value.get('i'),
        'reading_level': value.get('c'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('additional_physical_form_available_note', '^530..')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_available_note(self, key, value):
    """Additional Physical Form Available Note."""
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'availability_source',
        '8': 'field_link_and_sequence_number',
        'd': 'order_number',
        'a': 'additional_physical_form_available_note',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'availability_conditions',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'availability_source': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'order_number': value.get('d'),
        'additional_physical_form_available_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'availability_conditions': value.get('c'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('reproduction_note', '^533..')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    """Reproduction Note."""
    field_map = {
        'b': 'place_of_reproduction',
        '8': 'field_link_and_sequence_number',
        'e': 'physical_description_of_reproduction',
        'a': 'type_of_reproduction',
        'd': 'date_of_reproduction',
        '3': 'materials_specified',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'f': 'series_statement_of_reproduction',
        'n': 'note_about_reproduction',
        'm': 'dates_and_or_sequential_designation_of_issues_reproduced',
        '7': 'fixed_length_data_elements_of_reproduction',
        'c': 'agency_responsible_for_reproduction',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_of_reproduction': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'physical_description_of_reproduction': value.get('e'),
        'type_of_reproduction': value.get('a'),
        'date_of_reproduction': value.get('d'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': value.get('5'),
        'series_statement_of_reproduction': utils.force_list(
            value.get('f')
        ),
        'note_about_reproduction': utils.force_list(
            value.get('n')
        ),
        'dates_and_or_sequential_designation_of_issues_reproduced': utils.force_list(
            value.get('m')
        ),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'agency_responsible_for_reproduction': utils.force_list(
            value.get('c')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('original_version_note', '^534..')
@utils.for_each_value
@utils.filter_values
def original_version_note(self, key, value):
    """Original Version Note."""
    field_map = {
        'p': 'introductory_phrase',
        'b': 'edition_statement_of_original',
        '8': 'field_link_and_sequence_number',
        'z': 'international_standard_book_number',
        'e': 'physical_description_of_original',
        'l': 'location_of_original',
        'a': 'main_entry_of_original',
        '3': 'materials_specified',
        '6': 'linkage',
        't': 'title_statement_of_original',
        'f': 'series_statement_of_original',
        'k': 'key_title_of_original',
        'm': 'material_specific_details',
        'x': 'international_standard_serial_number',
        'o': 'other_resource_identifier',
        'c': 'publication_distribution_of_original',
        'n': 'note_about_original',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'introductory_phrase': value.get('p'),
        'edition_statement_of_original': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'physical_description_of_original': value.get('e'),
        'location_of_original': value.get('l'),
        'main_entry_of_original': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'title_statement_of_original': value.get('t'),
        'series_statement_of_original': utils.force_list(
            value.get('f')
        ),
        'key_title_of_original': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'other_resource_identifier': utils.force_list(
            value.get('o')
        ),
        'publication_distribution_of_original': value.get('c'),
        'note_about_original': utils.force_list(
            value.get('n')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('location_of_originals_duplicates_note', '^535..')
@utils.for_each_value
@utils.filter_values
def location_of_originals_duplicates_note(self, key, value):
    """Location of Originals/Duplicates Note."""
    indicator_map1 = {"1": "Holder of originals", "2": "Holder of duplicates"}
    field_map = {
        'b': 'postal_address',
        '8': 'field_link_and_sequence_number',
        'd': 'telecommunications_address',
        'a': 'custodian',
        '3': 'materials_specified',
        'g': 'repository_location_code',
        '6': 'linkage',
        'c': 'country',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('custodial_role')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'postal_address': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'telecommunications_address': utils.force_list(
            value.get('d')
        ),
        'custodian': value.get('a'),
        'materials_specified': value.get('3'),
        'repository_location_code': value.get('g'),
        'linkage': value.get('6'),
        'country': utils.force_list(
            value.get('c')
        ),
        'custodial_role': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('funding_information_note', '^536..')
@utils.for_each_value
@utils.filter_values
def funding_information_note(self, key, value):
    """Funding Information Note."""
    field_map = {
        'h': 'work_unit_number',
        'b': 'contract_number',
        '8': 'field_link_and_sequence_number',
        'f': 'project_number',
        'e': 'program_element_number',
        'a': 'text_of_note',
        'd': 'undifferentiated_number',
        'g': 'task_number',
        '6': 'linkage',
        'c': 'grant_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'work_unit_number': utils.force_list(
            value.get('h')
        ),
        'contract_number': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'project_number': utils.force_list(
            value.get('f')
        ),
        'program_element_number': utils.force_list(
            value.get('e')
        ),
        'text_of_note': value.get('a'),
        'undifferentiated_number': utils.force_list(
            value.get('d')
        ),
        'task_number': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'grant_number': utils.force_list(
            value.get('c')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('system_details_note', '^538..')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    """System Details Note."""
    field_map = {
        'a': 'system_details_note',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        'i': 'display_text',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'system_details_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_text': value.get('i'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('terms_governing_use_and_reproduction_note', '^540..')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    field_map = {
        'a': 'terms_governing_use_and_reproduction',
        'b': 'jurisdiction',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'd': 'authorized_users',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'authorization',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'terms_governing_use_and_reproduction': value.get('a'),
        'jurisdiction': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'authorized_users': value.get('d'),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'authorization': value.get('c'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('immediate_source_of_acquisition_note', '^541..')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    indicator_map1 = {"0": "Private", "1": "Not private", "_": "No information provided"}
    field_map = {
        'b': 'address',
        '8': 'field_link_and_sequence_number',
        'e': 'accession_number',
        'a': 'source_of_acquisition',
        'd': 'date_of_acquisition',
        '3': 'materials_specified',
        'h': 'purchase_price',
        'f': 'owner',
        'n': 'extent',
        'o': 'type_of_unit',
        '5': 'institution_to_which_field_applies',
        'c': 'method_of_acquisition',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('privacy')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'address': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'accession_number': value.get('e'),
        'source_of_acquisition': value.get('a'),
        'date_of_acquisition': value.get('d'),
        'materials_specified': value.get('3'),
        'purchase_price': value.get('h'),
        'owner': value.get('f'),
        'extent': utils.force_list(
            value.get('n')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'method_of_acquisition': value.get('c'),
        'linkage': value.get('6'),
        'privacy': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('information_relating_to_copyright_status', '^542..')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    """Information Relating to Copyright Status."""
    indicator_map1 = {"0": "Private", "1": "Not private", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'g': 'copyright_date',
        '8': 'field_link_and_sequence_number',
        's': 'source_of_information',
        'o': 'research_date',
        'l': 'copyright_status',
        'a': 'personal_creator',
        'd': 'copyright_holder',
        'j': 'creation_date',
        'f': 'copyright_statement',
        'n': 'note',
        'm': 'publication_status',
        'p': 'country_of_publication_or_creation',
        'b': 'personal_creator_death_date',
        'e': 'copyright_holder_contact_information',
        'q': 'supplying_agency',
        '3': 'materials_specified',
        '6': 'linkage',
        'h': 'copyright_renewal_date',
        'k': 'publisher',
        'r': 'jurisdiction_of_copyright_assessment',
        'c': 'corporate_creator',
        'i': 'publication_date',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('privacy')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'copyright_date': value.get('g'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': value.get('s'),
        'research_date': value.get('o'),
        'copyright_status': value.get('l'),
        'personal_creator': value.get('a'),
        'copyright_holder': utils.force_list(
            value.get('d')
        ),
        'creation_date': value.get('j'),
        'copyright_statement': utils.force_list(
            value.get('f')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'publication_status': value.get('m'),
        'country_of_publication_or_creation': utils.force_list(
            value.get('p')
        ),
        'personal_creator_death_date': value.get('b'),
        'copyright_holder_contact_information': utils.force_list(
            value.get('e')
        ),
        'supplying_agency': value.get('q'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'copyright_renewal_date': utils.force_list(
            value.get('h')
        ),
        'publisher': utils.force_list(
            value.get('k')
        ),
        'jurisdiction_of_copyright_assessment': value.get('r'),
        'corporate_creator': value.get('c'),
        'publication_date': value.get('i'),
        'privacy': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('location_of_other_archival_materials_note', '^544..')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    """Location of Other Archival Materials Note."""
    indicator_map1 = {"0": "Associated materials", "1": "Related materials", "_": "No information provided"}
    field_map = {
        'b': 'address',
        '8': 'field_link_and_sequence_number',
        'e': 'provenance',
        'd': 'title',
        'a': 'custodian',
        '3': 'materials_specified',
        'n': 'note',
        '6': 'linkage',
        'c': 'country',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('relationship')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'address': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'provenance': utils.force_list(
            value.get('e')
        ),
        'title': utils.force_list(
            value.get('d')
        ),
        'custodian': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'note': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'country': utils.force_list(
            value.get('c')
        ),
        'relationship': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('biographical_or_historical_data', '^545..')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {"0": "Biographical sketch", "1": "Administrative history", "_": "No information provided"}
    field_map = {
        'a': 'biographical_or_historical_data',
        'u': 'uniform_resource_identifier',
        'b': 'expansion',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_data')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'biographical_or_historical_data': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'expansion': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'type_of_data': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('language_note', '^546..')
@utils.for_each_value
@utils.filter_values
def language_note(self, key, value):
    """Language Note."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'language_note',
        'b': 'information_code_or_alphabet',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_note': value.get('a'),
        'information_code_or_alphabet': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('former_title_complexity_note', '^547..')
@utils.for_each_value
@utils.filter_values
def former_title_complexity_note(self, key, value):
    """Former Title Complexity Note."""
    field_map = {
        'a': 'former_title_complexity_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'former_title_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('issuing_body_note', '^550..')
@utils.for_each_value
@utils.filter_values
def issuing_body_note(self, key, value):
    """Issuing Body Note."""
    field_map = {
        'a': 'issuing_body_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'issuing_body_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('entity_and_attribute_information_note', '^552..')
@utils.for_each_value
@utils.filter_values
def entity_and_attribute_information_note(self, key, value):
    """Entity and Attribute Information Note."""
    field_map = {
        'p': 'entity_and_attribute_detail_citation',
        'u': 'uniform_resource_identifier',
        'b': 'entity_type_definition_and_source',
        '8': 'field_link_and_sequence_number',
        'z': 'display_note',
        'e': 'enumerated_domain_value',
        'l': 'attribute_value_accuracy',
        'a': 'entity_type_label',
        'd': 'attribute_definition_and_source',
        'n': 'attribute_measurement_frequency',
        'g': 'range_domain_minimum_and_maximum',
        'h': 'codeset_name_and_source',
        'j': 'attribute_units_of_measurement_and_resolution',
        'f': 'enumerated_domain_value_definition_and_source',
        'k': 'beginning_and_ending_date_of_attribute_values',
        'm': 'attribute_value_accuracy_explanation',
        'o': 'entity_and_attribute_overview',
        'c': 'attribute_label',
        'i': 'unrepresentable_domain',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'entity_and_attribute_detail_citation': utils.force_list(
            value.get('p')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'entity_type_definition_and_source': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_note': utils.force_list(
            value.get('z')
        ),
        'enumerated_domain_value': utils.force_list(
            value.get('e')
        ),
        'attribute_value_accuracy': value.get('l'),
        'entity_type_label': value.get('a'),
        'attribute_definition_and_source': value.get('d'),
        'attribute_measurement_frequency': value.get('n'),
        'range_domain_minimum_and_maximum': value.get('g'),
        'codeset_name_and_source': value.get('h'),
        'attribute_units_of_measurement_and_resolution': value.get('j'),
        'enumerated_domain_value_definition_and_source': utils.force_list(
            value.get('f')
        ),
        'beginning_and_ending_date_of_attribute_values': value.get('k'),
        'attribute_value_accuracy_explanation': value.get('m'),
        'entity_and_attribute_overview': utils.force_list(
            value.get('o')
        ),
        'attribute_label': value.get('c'),
        'unrepresentable_domain': value.get('i'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('cumulative_index_finding_aids_note', '^555..')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    """Cumulative Index/Finding Aids Note."""
    indicator_map1 = {"0": "Finding aids", "8": "No display constant generated", "_": "Indexes"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'availability_source',
        '8': 'field_link_and_sequence_number',
        'd': 'bibliographic_reference',
        'a': 'cumulative_index_finding_aids_note',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'degree_of_control',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'availability_source': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'bibliographic_reference': value.get('d'),
        'cumulative_index_finding_aids_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'degree_of_control': value.get('c'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('information_about_documentation_note', '^556..')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    """Information About Documentation Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Documentation"}
    field_map = {
        'a': 'information_about_documentation_note',
        '8': 'field_link_and_sequence_number',
        'z': 'international_standard_book_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'information_about_documentation_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('ownership_and_custodial_history', '^561..')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {"0": "Private", "1": "Not private", "_": "No information provided"}
    field_map = {
        'a': 'history',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('privacy')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'history': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('copy_and_version_identification_note', '^562..')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    """Copy and Version Identification Note."""
    field_map = {
        'a': 'identifying_markings',
        'b': 'copy_identification',
        '8': 'field_link_and_sequence_number',
        'e': 'number_of_copies',
        'd': 'presentation_format',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'version_identification',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'identifying_markings': utils.force_list(
            value.get('a')
        ),
        'copy_identification': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_copies': utils.force_list(
            value.get('e')
        ),
        'presentation_format': utils.force_list(
            value.get('d')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'version_identification': utils.force_list(
            value.get('c')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('binding_information', '^563..')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    """Binding Information."""
    field_map = {
        'a': 'binding_note',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'binding_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('case_file_characteristics_note', '^565..')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    """Case File Characteristics Note."""
    indicator_map1 = {"0": "Case file characteristics", "8": "No display constant generated", "_": "File size"}
    field_map = {
        'b': 'name_of_variable',
        '8': 'field_link_and_sequence_number',
        'e': 'filing_scheme_or_code',
        'd': 'universe_of_data',
        'a': 'number_of_cases_variables',
        '3': 'materials_specified',
        '6': 'linkage',
        'c': 'unit_of_analysis',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'name_of_variable': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'filing_scheme_or_code': utils.force_list(
            value.get('e')
        ),
        'universe_of_data': utils.force_list(
            value.get('d')
        ),
        'number_of_cases_variables': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'unit_of_analysis': utils.force_list(
            value.get('c')
        ),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('methodology_note', '^567..')
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

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'methodology_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('linking_entry_complexity_note', '^580..')
@utils.for_each_value
@utils.filter_values
def linking_entry_complexity_note(self, key, value):
    """Linking Entry Complexity Note."""
    field_map = {
        'a': 'linking_entry_complexity_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linking_entry_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('publications_about_described_materials_note', '^581..')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    """Publications About Described Materials Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Publications"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'publications_about_described_materials_note',
        '3': 'materials_specified',
        'z': 'international_standard_book_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'publications_about_described_materials_note': value.get('a'),
        'materials_specified': value.get('3'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('action_note', '^583..')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    indicator_map1 = {"0": "Private", "1": "Not private", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'action_identification',
        '8': 'field_link_and_sequence_number',
        'z': 'public_note',
        'e': 'contingency_for_action',
        'l': 'status',
        'a': 'action',
        'd': 'action_interval',
        '3': 'materials_specified',
        '6': 'linkage',
        '2': 'source_of_term',
        'j': 'site_of_action',
        'f': 'authorization',
        'k': 'action_agent',
        'o': 'type_of_unit',
        'x': 'nonpublic_note',
        '5': 'institution_to_which_field_applies',
        'h': 'jurisdiction',
        'c': 'time_date_of_action',
        'i': 'method_of_action',
        'n': 'extent',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('privacy')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'action_identification': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'contingency_for_action': utils.force_list(
            value.get('e')
        ),
        'status': utils.force_list(
            value.get('l')
        ),
        'action': value.get('a'),
        'action_interval': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'site_of_action': utils.force_list(
            value.get('j')
        ),
        'authorization': utils.force_list(
            value.get('f')
        ),
        'action_agent': utils.force_list(
            value.get('k')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'jurisdiction': utils.force_list(
            value.get('h')
        ),
        'time_date_of_action': utils.force_list(
            value.get('c')
        ),
        'method_of_action': utils.force_list(
            value.get('i')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'privacy': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('accumulation_and_frequency_of_use_note', '^584..')
@utils.for_each_value
@utils.filter_values
def accumulation_and_frequency_of_use_note(self, key, value):
    """Accumulation and Frequency of Use Note."""
    field_map = {
        'a': 'accumulation',
        'b': 'frequency_of_use',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'accumulation': utils.force_list(
            value.get('a')
        ),
        'frequency_of_use': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('exhibitions_note', '^585..')
@utils.for_each_value
@utils.filter_values
def exhibitions_note(self, key, value):
    """Exhibitions Note."""
    field_map = {
        '5': 'institution_to_which_field_applies',
        'a': 'exhibitions_note',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': value.get('5'),
        'exhibitions_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('awards_note', '^586..')
@utils.for_each_value
@utils.filter_values
def awards_note(self, key, value):
    """Awards Note."""
    indicator_map1 = {"8": "No display constant generated", "_": "Awards"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'awards_note',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'awards_note': value.get('a'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('source_of_description_note', '^588..')
@utils.for_each_value
@utils.filter_values
def source_of_description_note(self, key, value):
    """Source of Description Note."""
    indicator_map1 = {"0": "Source of description", "1": "Latest issue consulted", "_": "No information provided"}
    field_map = {
        '5': 'institution_to_which_field_applies',
        'a': 'source_of_description_note',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'institution_to_which_field_applies': value.get('5'),
        'source_of_description_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
