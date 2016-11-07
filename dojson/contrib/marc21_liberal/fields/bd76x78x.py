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


@marc21_liberal.over('main_series_entry', '^760..')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    """Main Series Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Main series"}
    field_map = {
        'm': 'material_specific_details',
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        's': 'uniform_title',
        'a': 'main_entry_heading',
        'h': 'physical_description',
        'i': 'relationship_information',
        'b': 'edition',
        'y': 'coden_designation',
        't': 'title',
        'x': 'international_standard_serial_number',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'material_specific_details': value.get('m'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'uniform_title': value.get('s'),
        'main_entry_heading': value.get('a'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'edition': value.get('b'),
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subseries_entry', '^762..')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    """Subseries Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Has subseries"}
    field_map = {
        'm': 'material_specific_details',
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        's': 'uniform_title',
        'a': 'main_entry_heading',
        'h': 'physical_description',
        'i': 'relationship_information',
        'b': 'edition',
        'y': 'coden_designation',
        't': 'title',
        'x': 'international_standard_serial_number',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'material_specific_details': value.get('m'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'uniform_title': value.get('s'),
        'main_entry_heading': value.get('a'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'edition': value.get('b'),
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('original_language_entry', '^765..')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    """Original Language Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Translation of"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('translation_entry', '^767..')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    """Translation Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Translated as"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('supplement_special_issue_entry', '^770..')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    """Supplement/Special Issue Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Has supplement"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('supplement_parent_entry', '^772..')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    """Supplement Parent Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"0": "Parent", "8": "No display constant generated", "_": "Supplement to"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('host_item_entry', '^773..')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    """Host Item Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "In"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        '4': 'relationship_code',
        'g': 'related_parts',
        '3': 'materials_specified',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'q': 'enumeration_and_first_page',
        'p': 'abbreviated_title',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'enumeration_and_first_page': value.get('q'),
        'abbreviated_title': value.get('p'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('constituent_unit_entry', '^774..')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    """Constituent Unit Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Constituent unit"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('other_edition_entry', '^775..')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    """Other Edition Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Other edition available"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'e': 'language_code',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'a': 'main_entry_heading',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        'f': 'country_code',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'language_code': value.get('e'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'main_entry_heading': value.get('a'),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'country_code': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('additional_physical_form_entry', '^776..')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    """Additional Physical Form Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Available in another form"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('issued_with_entry', '^777..')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    """Issued With Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Issued with"}
    field_map = {
        'm': 'material_specific_details',
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        's': 'uniform_title',
        'a': 'main_entry_heading',
        'h': 'physical_description',
        'i': 'relationship_information',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        't': 'title',
        'x': 'international_standard_serial_number',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'material_specific_details': value.get('m'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'uniform_title': value.get('s'),
        'main_entry_heading': value.get('a'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('preceding_entry', '^780..')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    """Preceding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"0": "Continues", "1": "Continues in part", "2": "Supersedes", "3": "Supersedes in part", "4": "Formed by the union of ... and ...", "5": "Absorbed", "6": "Absorbed in part", "7": "Separated from"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('type_of_relationship')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'type_of_relationship': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('succeeding_entry', '^785..')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    """Succeeding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"0": "Continued by", "1": "Continued in part by", "2": "Superseded by", "3": "Superseded in part by", "4": "Absorbed by", "5": "Absorbed in part by", "6": "Split into ... and ...", "7": "Merged with ... to form ...", "8": "Changed back to"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('type_of_relationship')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'type_of_relationship': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('data_source_entry', '^786..')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    """Data Source Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Data source"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'j': 'period_of_content',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'p': 'abbreviated_title',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        'v': 'source_contribution',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'period_of_content': value.get('j'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'abbreviated_title': value.get('p'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'source_contribution': value.get('v'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('other_relationship_entry', '^787..')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    """Other Relationship Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Related item"}
    field_map = {
        'd': 'place_publisher_and_date_of_publication',
        'n': 'note',
        'c': 'qualifying_information',
        '4': 'relationship_code',
        'g': 'related_parts',
        'r': 'report_number',
        'a': 'main_entry_heading',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        't': 'title',
        'x': 'international_standard_serial_number',
        'm': 'material_specific_details',
        'u': 'standard_technical_report_number',
        'o': 'other_item_identifier',
        '7': 'control_subfield',
        'h': 'physical_description',
        's': 'uniform_title',
        'b': 'edition',
        'k': 'series_data_for_related_item',
        'y': 'coden_designation',
        '6': 'linkage',
        'w': 'record_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_controller')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_publisher_and_date_of_publication': value.get('d'),
        'note': utils.force_list(
            value.get('n')
        ),
        'qualifying_information': value.get('c'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'main_entry_heading': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'title': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'material_specific_details': value.get('m'),
        'standard_technical_report_number': value.get('u'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'uniform_title': value.get('s'),
        'edition': value.get('b'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'coden_designation': value.get('y'),
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_controller': indicator_map1.get(key[3], key[3]),
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
