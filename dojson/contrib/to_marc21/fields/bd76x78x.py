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
        'record_control_number': 'w',
        'linkage': '6',
        'uniform_title': 's',
        'control_subfield': '7',
        'relationship_information': 'i',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'title': 't',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'main_entry_heading': 'a',
        'note': 'n',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        's': value.get('uniform_title'),
        '7': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        't': value.get('title'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        'a': value.get('main_entry_heading'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('762', '^subseries_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subseries_entry(self, key, value):
    """Reverse - Subseries Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has subseries": "_", "No display constant generated": "8"}
    field_map = {
        'record_control_number': 'w',
        'linkage': '6',
        'uniform_title': 's',
        'control_subfield': '7',
        'relationship_information': 'i',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'title': 't',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'main_entry_heading': 'a',
        'note': 'n',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        's': value.get('uniform_title'),
        '7': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        't': value.get('title'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        'a': value.get('main_entry_heading'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('765', '^original_language_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_language_entry(self, key, value):
    """Reverse - Original Language Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translation of": "_"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('767', '^translation_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_entry(self, key, value):
    """Reverse - Translation Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translated as": "_"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('770', '^supplement_special_issue_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_special_issue_entry(self, key, value):
    """Reverse - Supplement/Special Issue Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has supplement": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('772', '^supplement_parent_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_parent_entry(self, key, value):
    """Reverse - Supplement Parent Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Parent": "0", "Supplement to": "_"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
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
        'linkage': '6',
        'coden_designation': 'y',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'enumeration_and_first_page': 'q',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'note': 'n',
        'title': 't',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'uniform_title': 's',
        'abbreviated_title': 'p',
        'relationship_information': 'i',
        'international_standard_serial_number': 'x',
        'report_number': 'r',
        'materials_specified': '3',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'y': value.get('coden_designation'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('enumeration_and_first_page'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        's': value.get('uniform_title'),
        'p': value.get('abbreviated_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': value.get('international_standard_serial_number'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '3': value.get('materials_specified'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('774', '^constituent_unit_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_constituent_unit_entry(self, key, value):
    """Reverse - Constituent Unit Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Constituent unit": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('775', '^other_edition_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_edition_entry(self, key, value):
    """Reverse - Other Edition Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Other edition available": "_"}
    field_map = {
        'linkage': '6',
        'coden_designation': 'y',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'country_code': 'f',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'note': 'n',
        'title': 't',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'uniform_title': 's',
        'relationship_information': 'i',
        'international_standard_serial_number': 'x',
        'language_code': 'e',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'y': value.get('coden_designation'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'f': value.get('country_code'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': value.get('international_standard_serial_number'),
        'e': value.get('language_code'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('776', '^additional_physical_form_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_entry(self, key, value):
    """Reverse - Additional Physical Form Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Available in another form": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
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
        'record_control_number': 'w',
        'linkage': '6',
        'uniform_title': 's',
        'control_subfield': '7',
        'relationship_information': 'i',
        'international_standard_serial_number': 'x',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'other_item_identifier': 'o',
        'title': 't',
        'material_specific_details': 'm',
        'series_data_for_related_item': 'k',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'main_entry_heading': 'a',
        'note': 'n',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        's': value.get('uniform_title'),
        '7': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'm': value.get('material_specific_details'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        'a': value.get('main_entry_heading'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('780', '^preceding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preceding_entry(self, key, value):
    """Reverse - Preceding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed": "5", "Absorbed in part": "6", "Continues": "0", "Continues in part": "1", "Formed by the union of ... and ...": "4", "Separated from": "7", "Supersedes": "2", "Supersedes in part": "3"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), '_'),
    }


@to_marc21.over('785', '^succeeding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_succeeding_entry(self, key, value):
    """Reverse - Succeeding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed by": "4", "Absorbed in part by": "5", "Changed back to": "8", "Continued by": "0", "Continued in part by": "1", "Merged with ... to form ...": "7", "Split into ... and ...": "6", "Superseded by": "2", "Superseded in part by": "3"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
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
        'linkage': '6',
        'coden_designation': 'y',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'international_standard_serial_number': 'x',
        'title': 't',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'period_of_content': 'j',
        'abbreviated_title': 'p',
        'relationship_information': 'i',
        'report_number': 'r',
        'series_data_for_related_item': 'k',
        'record_control_number': 'w',
        'uniform_title': 's',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'note': 'n',
        'source_contribution': 'v',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'y': value.get('coden_designation'),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'x': value.get('international_standard_serial_number'),
        't': value.get('title'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'j': value.get('period_of_content'),
        'p': value.get('abbreviated_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('uniform_title'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'v': value.get('source_contribution'),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('787', '^other_relationship_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_relationship_entry(self, key, value):
    """Reverse - Other Relationship Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Related item": "_"}
    field_map = {
        'linkage': '6',
        'note': 'n',
        'control_subfield': '7',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'edition': 'b',
        'physical_description': 'h',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
        'title': 't',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'place_publisher_and_date_of_publication': 'd',
        'coden_designation': 'y',
        'uniform_title': 's',
        'relationship_information': 'i',
        'report_number': 'r',
        'record_control_number': 'w',
        'international_standard_book_number': 'z',
        'main_entry_heading': 'a',
        'series_data_for_related_item': 'k',
        'qualifying_information': 'c',
        'related_parts': 'g',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '7': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'b': value.get('edition'),
        'h': value.get('physical_description'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'y': value.get('coden_designation'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'a': value.get('main_entry_heading'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'c': value.get('qualifying_information'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }
