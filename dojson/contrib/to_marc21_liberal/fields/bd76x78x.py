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


@to_marc21_liberal.over('760', '^main_series_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_main_series_entry(self, key, value):
    """Reverse - Main Series Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Main series": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'uniform_title': 's',
        'title': 't',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('762', '^subseries_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subseries_entry(self, key, value):
    """Reverse - Subseries Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has subseries": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'uniform_title': 's',
        'title': 't',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('765', '^original_language_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_language_entry(self, key, value):
    """Reverse - Original Language Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translation of": "_"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('767', '^translation_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_entry(self, key, value):
    """Reverse - Translation Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translated as": "_"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('770', '^supplement_special_issue_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_special_issue_entry(self, key, value):
    """Reverse - Supplement/Special Issue Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has supplement": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('772', '^supplement_parent_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_parent_entry(self, key, value):
    """Reverse - Supplement Parent Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Parent": "0", "Supplement to": "_"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('773', '^host_item_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_host_item_entry(self, key, value):
    """Reverse - Host Item Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"In": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'abbreviated_title': 'p',
        'enumeration_and_first_page': 'q',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'materials_specified': '3',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'p': value.get('abbreviated_title'),
        'q': value.get('enumeration_and_first_page'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('774', '^constituent_unit_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_constituent_unit_entry(self, key, value):
    """Reverse - Constituent Unit Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Constituent unit": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('775', '^other_edition_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_edition_entry(self, key, value):
    """Reverse - Other Edition Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Other edition available": "_"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'language_code': 'e',
        'country_code': 'f',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'e': value.get('language_code'),
        'f': value.get('country_code'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('776', '^additional_physical_form_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_entry(self, key, value):
    """Reverse - Additional Physical Form Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Available in another form": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('777', '^issued_with_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issued_with_entry(self, key, value):
    """Reverse - Issued With Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Issued with": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'uniform_title': 's',
        'title': 't',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('780', '^preceding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preceding_entry(self, key, value):
    """Reverse - Preceding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed": "5", "Absorbed in part": "6", "Continues": "0", "Continues in part": "1", "Formed by the union of ... and ...": "4", "Separated from": "7", "Supersedes": "2", "Supersedes in part": "3"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'type_of_relationship'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), value.get('type_of_relationship', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('785', '^succeeding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_succeeding_entry(self, key, value):
    """Reverse - Succeeding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed by": "4", "Absorbed in part by": "5", "Changed back to": "8", "Continued by": "0", "Continued in part by": "1", "Merged with ... to form ...": "7", "Split into ... and ...": "6", "Superseded by": "2", "Superseded in part by": "3"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'type_of_relationship'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), value.get('type_of_relationship', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('786', '^data_source_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_data_source_entry(self, key, value):
    """Reverse - Data Source Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Data source": "_", "No display constant generated": "8"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'period_of_content': 'j',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'abbreviated_title': 'p',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'source_contribution': 'v',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'j': value.get('period_of_content'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'p': value.get('abbreviated_title'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'v': value.get('source_contribution'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('787', '^other_relationship_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_relationship_entry(self, key, value):
    """Reverse - Other Relationship Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Related item": "_"}

    field_map = {
        'main_entry_heading': 'a',
        'edition': 'b',
        'qualifying_information': 'c',
        'place_publisher_and_date_of_publication': 'd',
        'related_parts': 'g',
        'physical_description': 'h',
        'relationship_information': 'i',
        'series_data_for_related_item': 'k',
        'material_specific_details': 'm',
        'note': 'n',
        'other_item_identifier': 'o',
        'report_number': 'r',
        'uniform_title': 's',
        'title': 't',
        'standard_technical_report_number': 'u',
        'record_control_number': 'w',
        'international_standard_serial_number': 'x',
        'coden_designation': 'y',
        'international_standard_book_number': 'z',
        'relationship_code': '4',
        'linkage': '6',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'b': value.get('edition'),
        'c': value.get('qualifying_information'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'h': value.get('physical_description'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'm': value.get('material_specific_details'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        's': value.get('uniform_title'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'y': value.get('coden_designation'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
