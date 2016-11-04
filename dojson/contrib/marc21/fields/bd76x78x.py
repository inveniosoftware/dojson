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


@marc21.over('main_series_entry', '^760[_10][_8]')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    """Main Series Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Main series"}
    field_map = {
        'g': 'related_parts',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        's': 'uniform_title',
        '7': 'control_subfield',
        'h': 'physical_description',
        'c': 'qualifying_information',
        'y': 'coden_designation',
        'i': 'relationship_information',
        'a': 'main_entry_heading',
        'w': 'record_control_number',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'b': 'edition',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'uniform_title': value.get('s'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'qualifying_information': value.get('c'),
        'coden_designation': value.get('y'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'main_entry_heading': value.get('a'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'edition': value.get('b'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('subseries_entry', '^762[_10][_8]')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    """Subseries Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Has subseries"}
    field_map = {
        'g': 'related_parts',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        's': 'uniform_title',
        '7': 'control_subfield',
        'h': 'physical_description',
        'c': 'qualifying_information',
        'y': 'coden_designation',
        'i': 'relationship_information',
        'a': 'main_entry_heading',
        'w': 'record_control_number',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'b': 'edition',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'uniform_title': value.get('s'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'qualifying_information': value.get('c'),
        'coden_designation': value.get('y'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'main_entry_heading': value.get('a'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'edition': value.get('b'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('original_language_entry', '^765[_10][_8]')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    """Original Language Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Translation of"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('translation_entry', '^767[_10][_8]')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    """Translation Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Translated as"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_special_issue_entry', '^770[_10][_8]')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    """Supplement/Special Issue Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Has supplement"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_parent_entry', '^772[_10][_08]')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    """Supplement Parent Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "0": "Parent",
        "8": "No display constant generated",
        "_": "Supplement to"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('host_item_entry', '^773[_10][_8]')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    """Host Item Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "In"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'p': 'abbreviated_title',
        '3': 'materials_specified',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
        'q': 'enumeration_and_first_page',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'abbreviated_title': value.get('p'),
        'materials_specified': value.get('3'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'enumeration_and_first_page': value.get('q'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('constituent_unit_entry', '^774[_10][_8]')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    """Constituent Unit Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Constituent unit"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_edition_entry', '^775[_10][_8]')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    """Other Edition Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Other edition available"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'e': 'language_code',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'f': 'country_code',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'language_code': value.get('e'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'country_code': value.get('f'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('additional_physical_form_entry', '^776[_10][_8]')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    """Additional Physical Form Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Available in another form"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('issued_with_entry', '^777[_10][_8]')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    """Issued With Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Issued with"}
    field_map = {
        'g': 'related_parts',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        's': 'uniform_title',
        'k': 'series_data_for_related_item',
        '7': 'control_subfield',
        'h': 'physical_description',
        'c': 'qualifying_information',
        'y': 'coden_designation',
        'i': 'relationship_information',
        'a': 'main_entry_heading',
        'w': 'record_control_number',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'b': 'edition',
        '6': 'linkage',
        'x': 'international_standard_serial_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'uniform_title': value.get('s'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'qualifying_information': value.get('c'),
        'coden_designation': value.get('y'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'main_entry_heading': value.get('a'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'edition': value.get('b'),
        'linkage': value.get('6'),
        'international_standard_serial_number': value.get('x'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('preceding_entry', '^780[_10][_13750426]')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    """Preceding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "0": "Continues",
        "1": "Continues in part",
        "2": "Supersedes",
        "3": "Supersedes in part",
        "4": "Formed by the union of ... and ...",
        "5": "Absorbed",
        "6": "Absorbed in part",
        "7": "Separated from"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('type_of_relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('succeeding_entry', '^785[_10][_153704826]')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    """Succeeding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "0": "Continued by",
        "1": "Continued in part by",
        "2": "Superseded by",
        "3": "Superseded in part by",
        "4": "Absorbed by",
        "5": "Absorbed in part by",
        "6": "Split into ... and ...",
        "7": "Merged with ... to form ...",
        "8": "Changed back to"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('type_of_relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('data_source_entry', '^786[_10][_8]')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    """Data Source Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"8": "No display constant generated", "_": "Data source"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'j': 'period_of_content',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'v': 'source_contribution',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'p': 'abbreviated_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'period_of_content': value.get('j'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'source_contribution': value.get('v'),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'abbreviated_title': value.get('p'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_relationship_entry', '^787[_10][_8]')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    """Other Relationship Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Related item"}
    field_map = {
        'y': 'coden_designation',
        't': 'title',
        'm': 'material_specific_details',
        'n': 'note',
        'o': 'other_item_identifier',
        'x': 'international_standard_serial_number',
        '7': 'control_subfield',
        'h': 'physical_description',
        'i': 'relationship_information',
        'z': 'international_standard_book_number',
        'b': 'edition',
        'g': 'related_parts',
        'w': 'record_control_number',
        'r': 'report_number',
        'k': 'series_data_for_related_item',
        's': 'uniform_title',
        'c': 'qualifying_information',
        'a': 'main_entry_heading',
        '4': 'relationship_code',
        '8': 'field_link_and_sequence_number',
        'd': 'place_publisher_and_date_of_publication',
        'u': 'standard_technical_report_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_controller')

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden_designation': value.get('y'),
        'title': value.get('t'),
        'material_specific_details': value.get('m'),
        'note': utils.force_list(
            value.get('n')
        ),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'international_standard_serial_number': value.get('x'),
        'control_subfield': value.get('7'),
        'physical_description': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'edition': value.get('b'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'uniform_title': value.get('s'),
        'qualifying_information': value.get('c'),
        'main_entry_heading': value.get('a'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_publisher_and_date_of_publication': value.get('d'),
        'standard_technical_report_number': value.get('u'),
        'linkage': value.get('6'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }
