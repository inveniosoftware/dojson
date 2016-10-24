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


@to_marc21.over('760', '^main_series_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_main_series_entry(self, key, value):
    """Reverse - Main Series Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Main series": "_", "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'title': 't',
        'relationship_code': '4',
        'control_subfield': '7',
        'edition': 'b',
        'place_publisher_and_date_of_publication': 'd',
        'material_specific_details': 'm',
        'international_standard_serial_number': 'x',
        'physical_description': 'h',
        'related_parts': 'g',
        'relationship_information': 'i',
        'other_item_identifier': 'o',
        'main_entry_heading': 'a',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        't': value.get('title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '7': value.get('control_subfield'),
        'b': value.get('edition'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'm': value.get('material_specific_details'),
        'x': value.get('international_standard_serial_number'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'a': value.get('main_entry_heading'),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('762', '^subseries_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subseries_entry(self, key, value):
    """Reverse - Subseries Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Has subseries": "_",
        "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'title': 't',
        'relationship_code': '4',
        'control_subfield': '7',
        'edition': 'b',
        'place_publisher_and_date_of_publication': 'd',
        'material_specific_details': 'm',
        'international_standard_serial_number': 'x',
        'physical_description': 'h',
        'related_parts': 'g',
        'relationship_information': 'i',
        'other_item_identifier': 'o',
        'main_entry_heading': 'a',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        't': value.get('title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '7': value.get('control_subfield'),
        'b': value.get('edition'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'm': value.get('material_specific_details'),
        'x': value.get('international_standard_serial_number'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'a': value.get('main_entry_heading'),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('765', '^original_language_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_language_entry(self, key, value):
    """Reverse - Original Language Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "No display constant generated": "8",
        "Translation of": "_"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('767', '^translation_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_entry(self, key, value):
    """Reverse - Translation Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "No display constant generated": "8",
        "Translated as": "_"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('770', '^supplement_special_issue_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_special_issue_entry(self, key, value):
    """Reverse - Supplement/Special Issue Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Has supplement": "_",
        "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('772', '^supplement_parent_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_parent_entry(self, key, value):
    """Reverse - Supplement Parent Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "No display constant generated": "8",
        "Parent": "0",
        "Supplement to": "_"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('773', '^host_item_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_host_item_entry(self, key, value):
    """Reverse - Host Item Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"In": "_", "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'enumeration_and_first_page': 'q',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'materials_specified': '3',
        'title': 't',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'abbreviated_title': 'p',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'q': value.get('enumeration_and_first_page'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        '3': value.get('materials_specified'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        'p': value.get('abbreviated_title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('774', '^constituent_unit_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_constituent_unit_entry(self, key, value):
    """Reverse - Constituent Unit Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Constituent unit": "_",
        "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('775', '^other_edition_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_edition_entry(self, key, value):
    """Reverse - Other Edition Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "No display constant generated": "8",
        "Other edition available": "_"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'main_entry_heading': 'a',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'language_code': 'e',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'country_code': 'f',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'a': value.get('main_entry_heading'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        'e': value.get('language_code'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'f': value.get('country_code'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('776', '^additional_physical_form_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_entry(self, key, value):
    """Reverse - Additional Physical Form Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Available in another form": "_",
        "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('777', '^issued_with_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issued_with_entry(self, key, value):
    """Reverse - Issued With Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Issued with": "_", "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'title': 't',
        'relationship_code': '4',
        'control_subfield': '7',
        'edition': 'b',
        'place_publisher_and_date_of_publication': 'd',
        'material_specific_details': 'm',
        'series_data_for_related_item': 'k',
        'physical_description': 'h',
        'related_parts': 'g',
        'relationship_information': 'i',
        'other_item_identifier': 'o',
        'main_entry_heading': 'a',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        't': value.get('title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '7': value.get('control_subfield'),
        'b': value.get('edition'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'm': value.get('material_specific_details'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'a': value.get('main_entry_heading'),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('780', '^preceding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preceding_entry(self, key, value):
    """Reverse - Preceding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Absorbed": "5",
        "Absorbed in part": "6",
        "Continues": "0",
        "Continues in part": "1",
        "Formed by the union of ... and ...": "4",
        "Separated from": "7",
        "Supersedes": "2",
        "Supersedes in part": "3"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_relationship'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_relationship'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), '_'),
    }


@to_marc21.over('785', '^succeeding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_succeeding_entry(self, key, value):
    """Reverse - Succeeding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "Absorbed by": "4",
        "Absorbed in part by": "5",
        "Changed back to": "8",
        "Continued by": "0",
        "Continued in part by": "1",
        "Merged with ... to form ...": "7",
        "Split into ... and ...": "6",
        "Superseded by": "2",
        "Superseded in part by": "3"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_relationship'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_relationship'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), '_'),
    }


@to_marc21.over('786', '^data_source_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_data_source_entry(self, key, value):
    """Reverse - Data Source Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Data source": "_", "No display constant generated": "8"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'title': 't',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'abbreviated_title': 'p',
        'control_subfield': '7',
        'source_contribution': 'v',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'period_of_content': 'j',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        'p': value.get('abbreviated_title'),
        '7': value.get('control_subfield'),
        'v': value.get('source_contribution'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'j': value.get('period_of_content'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('787', '^other_relationship_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_relationship_entry(self, key, value):
    """Reverse - Other Relationship Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {
        "No display constant generated": "8",
        "Related item": "_"}
    field_map = {
        'uniform_title': 's',
        'relationship_code': '4',
        'international_standard_book_number': 'z',
        'edition': 'b',
        'main_entry_heading': 'a',
        'material_specific_details': 'm',
        'physical_description': 'h',
        'related_parts': 'g',
        'other_item_identifier': 'o',
        'standard_technical_report_number': 'u',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'note': 'n',
        'coden_designation': 'y',
        'title': 't',
        'control_subfield': '7',
        'record_control_number': 'w',
        'report_number': 'r',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'b': value.get('edition'),
        'a': value.get('main_entry_heading'),
        'm': value.get('material_specific_details'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'u': value.get('standard_technical_report_number'),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        't': value.get('title'),
        '7': value.get('control_subfield'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }
