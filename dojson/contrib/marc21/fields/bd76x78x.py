# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21, tomarc21


@marc21.over('main_series_entry', '^760[10_][8_]')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    """Main Series Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Main series", "8": "No display constant generated"}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'uniform_title': value.get('s'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^760[10_][8_]', 'main_series_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_main_series_entry(self, key, value):
    """Reverse - Main Series Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title')),
    }


@marc21.over('subseries_entry', '^762[10_][8_]')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    """Subseries Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Has subseries", "8": "No display constant generated"}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'uniform_title': value.get('s'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^762[10_][8_]', 'subseries_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subseries_entry(self, key, value):
    """Reverse - Subseries Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title')),
    }


@marc21.over('original_language_entry', '^765[10_][8_]')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    """Original Language Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Translation of", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^765[10_][8_]', 'original_language_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_language_entry(self, key, value):
    """Reverse - Original Language Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('translation_entry', '^767[10_][8_]')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    """Translation Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Translated as", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^767[10_][8_]', 'translation_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_entry(self, key, value):
    """Reverse - Translation Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('supplement_special_issue_entry', '^770[10_][8_]')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    """Supplement/Special Issue Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Has supplement", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^770[10_][8_]', 'supplement_special_issue_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_special_issue_entry(self, key, value):
    """Reverse - Supplement/Special Issue Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('supplement_parent_entry', '^772[10_][0_8]')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    """Supplement Parent Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Supplement to", "0": "Parent", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^772[10_][0_8]', 'supplement_parent_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_parent_entry(self, key, value):
    """Reverse - Supplement Parent Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('host_item_entry', '^773[10_][8_]')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    """Host Item Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "In", "8": "No display constant generated"}
    return {
        'materials_specified': value.get('3'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'enumeration_and_first_page': value.get('q'),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^773[10_][8_]', 'host_item_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_host_item_entry(self, key, value):
    """Reverse - Host Item Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        'q': utils.reverse_force_list(value.get('enumeration_and_first_page')),
        'p': utils.reverse_force_list(value.get('abbreviated_title')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('constituent_unit_entry', '^774[10_][8_]')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    """Constituent Unit Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Constituent unit", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^774[10_][8_]', 'constituent_unit_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_constituent_unit_entry(self, key, value):
    """Reverse - Constituent Unit Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('other_edition_entry', '^775[10_][8_]')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    """Other Edition Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Other edition available", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'language_code': value.get('e'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'country_code': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^775[10_][8_]', 'other_edition_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_edition_entry(self, key, value):
    """Reverse - Other Edition Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'e': utils.reverse_force_list(value.get('language_code')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'f': utils.reverse_force_list(value.get('country_code')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('additional_physical_form_entry', '^776[10_][8_]')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    """Additional Physical Form Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Available in another form", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^776[10_][8_]', 'additional_physical_form_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_entry(self, key, value):
    """Reverse - Additional Physical Form Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('issued_with_entry', '^777[10_][8_]')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    """Issued With Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Issued with", "8": "No display constant generated"}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'uniform_title': value.get('s'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^777[10_][8_]', 'issued_with_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issued_with_entry(self, key, value):
    """Reverse - Issued With Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title')),
    }


@marc21.over('preceding_entry', '^780[10_][_10325476]')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    """Preceding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"0": "Continues", "1": "Continues in part", "2": "Supersedes", "3": "Supersedes in part", "4": "Formed by the union of ... and ...", "5": "Absorbed", "6": "Absorbed in part", "7": "Separated from"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@tomarc21.over('^780[10_][_10325476]', 'preceding_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preceding_entry(self, key, value):
    """Reverse - Preceding Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('succeeding_entry', '^785[10_][_103254768]')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    """Succeeding Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"0": "Continued by", "1": "Continued in part by", "2": "Superseded by", "3": "Superseded in part by", "4": "Absorbed by", "5": "Absorbed in part by", "6": "Split into ... and ...", "7": "Merged with ... to form ...", "8": "Changed back to"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@tomarc21.over('^785[10_][_103254768]', 'succeeding_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_succeeding_entry(self, key, value):
    """Reverse - Succeeding Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('data_source_entry', '^786[10_][8_]')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    """Data Source Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Data source", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'period_of_content': value.get('j'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'source_contribution': value.get('v'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^786[10_][8_]', 'data_source_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_data_source_entry(self, key, value):
    """Reverse - Data Source Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'j': utils.reverse_force_list(value.get('period_of_content')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        'p': utils.reverse_force_list(value.get('abbreviated_title')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'v': utils.reverse_force_list(value.get('source_contribution')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('other_relationship_entry', '^787[10_][8_]')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    """Other Relationship Entry."""
    indicator_map1 = {"0": "Display note", "1": "Do not display note"}
    indicator_map2 = {"#": "Related item", "8": "No display constant generated"}
    return {
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'physical_description': value.get('h'),
        'series_data_for_related_item': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'other_item_identifier': utils.force_list(
            value.get('o')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('s'),
        'report_number': utils.force_list(
            value.get('r')
        ),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('^787[10_][8_]', 'other_relationship_entry')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_relationship_entry(self, key, value):
    """Reverse - Other Relationship Entry."""
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    indicator_map1 = {
            # TODO
            # TODO
            # TODO
    }
    return {
        '4': utils.reverse_force_list(value.get('relationship_code')),
        '7': utils.reverse_force_list(value.get('control_subfield')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('main_entry_heading')),
        'c': utils.reverse_force_list(value.get('qualifying_information')),
        'b': utils.reverse_force_list(value.get('edition')),
        'd': utils.reverse_force_list(value.get('place_publisher_and_date_of_publication')),
        'g': utils.reverse_force_list(value.get('related_parts')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('physical_description')),
        'k': utils.reverse_force_list(value.get('series_data_for_related_item')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'o': utils.reverse_force_list(value.get('other_item_identifier')),
        'n': utils.reverse_force_list(value.get('note')),
        's': utils.reverse_force_list(value.get('uniform_title')),
        'r': utils.reverse_force_list(value.get('report_number')),
        'u': utils.reverse_force_list(value.get('standard_technical_report_number')),
        't': utils.reverse_force_list(value.get('title')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'y': utils.reverse_force_list(value.get('coden_designation')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }
