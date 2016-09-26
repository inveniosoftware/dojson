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


@marc21.over('main_series_entry', '^760[_01][_8]')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    """Main Series Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Main series',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        's': 'uniform_title',
        't': 'title',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('subseries_entry', '^762[_01][_8]')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    """Subseries Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }
    indicator_map2 = {
        '_': 'Has subseries',
        '8': 'No display constant generated'
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        's': 'uniform_title',
        't': 'title',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('original_language_entry', '^765[_01][_8]')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    """Original Language Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Translation of',
        '8': 'No display constant generated'
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('translation_entry', '^767[_01][_8]')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    """Translation Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Translated as',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_special_issue_entry', '^770[_01][_8]')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    """Supplement/Special Issue Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Has supplement',
        '8': 'No display constant generated'
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_parent_entry', '^772[_01][_08]')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    """Supplement Parent Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Supplement to',
        '0': 'Parent',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('host_item_entry', '^773[_01][_8]')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    """Host Item Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'In',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'p': 'abbreviated_title',
        'q': 'enumeration_and_first_page',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '3': 'materials_specified',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'abbreviated_title': value.get('p'),
        'report_number': utils.force_list(value.get('r')),
        'enumeration_and_first_page': value.get('q'),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'materials_specified': value.get('3'),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('constituent_unit_entry', '^774[_01][_8]')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    """Constituent Unit Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Constituent unit',
        '8': 'No display constant generated'
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_edition_entry', '^775[_01][_8]')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    """Other Edition Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Other edition available',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'e': 'language_code',
        'f': 'country_code',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'language_code': value.get('e'),
        'country_code': value.get('f'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('additional_physical_form_entry', '^776[_01][_8]')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    """Additional Physical Form Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Available in another form',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('issued_with_entry', '^777[_01][_8]')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    """Issued With Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Issued with',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        's': 'uniform_title',
        't': 'title',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('preceding_entry', '^780[_01][_0-7]')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    """Preceding Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '0': 'Continues',
        '1': 'Continues in part',
        '2': 'Supersedes',
        '3': 'Supersedes in part',
        '4': 'Formed by the union of ... and ...',
        '5': 'Absorbed',
        '6': 'Absorbed in part',
        '7': 'Separated from',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('type_of_relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('succeeding_entry', '^785[_01][_0-8]')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    """Succeeding Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '0': 'Continued by',
        '1': 'Continued in part by',
        '2': 'Superseded by',
        '3': 'Superseded in part by',
        '4': 'Absorbed by',
        '5': 'Absorbed in part by',
        '6': 'Split into ... and ...',
        '7': 'Merged with ... to form ...',
        '8': 'Changed back to',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number'
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('type_of_relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('data_source_entry', '^786[_01][_8]')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    """Data Source Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Data source',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'j': 'period_of_content',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'p': 'abbreviated_title',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'v': 'source_contribution',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'period_of_content': value.get('j'),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'abbreviated_title': value.get('p'),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'source_contribution': value.get('v'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_relationship_entry', '^787[_01][_8]')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    """Other Relationship Entry."""
    indicator_map1 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    indicator_map2 = {
        '_': 'Related item',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'main_entry_heading',
        'b': 'edition',
        'c': 'qualifying_information',
        'd': 'place_publisher_and_date_of_publication',
        'g': 'related_parts',
        'h': 'physical_description',
        'i': 'relationship_information',
        'k': 'series_data_for_related_item',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'r': 'report_number',
        's': 'uniform_title',
        't': 'title',
        'u': 'standard_technical_report_number',
        'w': 'record_control_number',
        'x': 'international_standard_serial_number',
        'y': 'coden_designation',
        'z': 'international_standard_book_number',
        '4': 'relationship_code',
        '6': 'linkage',
        '7': 'control_subfield',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')
    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'qualifying_information': value.get('c'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(value.get('g')),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'series_data_for_related_item': utils.force_list(value.get('k')),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(value.get('n')),
        'other_item_identifier': utils.force_list(value.get('o')),
        'report_number': utils.force_list(value.get('r')),
        'uniform_title': value.get('s'),
        'title': value.get('t'),
        'standard_technical_report_number': value.get('u'),
        'record_control_number': utils.force_list(value.get('w')),
        'international_standard_serial_number': value.get('x'),
        'coden_designation': value.get('y'),
        'international_standard_book_number': utils.force_list(value.get('z')),
        'relationship_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'control_subfield': value.get('7'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }
