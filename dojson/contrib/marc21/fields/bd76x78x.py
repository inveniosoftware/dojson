# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from dojson import utils

from ..model import marc21


@marc21.over('main_series_entry', '^760[10_][8_]')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Main series'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('subseries_entry', '^762[10_][8_]')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Has subseries'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('original_language_entry', '^765[10_][8_]')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Translation of'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('translation_entry', '^767[10_][8_]')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Translated as'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_special_issue_entry', '^770[10_][8_]')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Has supplement'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('supplement_parent_entry', '^772[10_][0_8]')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'0': u'Parent', u'#': u'Supplement to',
                      u'8': u'No display constant generated'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('host_item_entry', '^773[10_][8_]')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'In'}
    return {
        'materials_specified': value.get('3'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'enumeration_and_first_page': value.get('q'),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('constituent_unit_entry', '^774[10_][8_]')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Constituent unit'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_edition_entry', '^775[10_][8_]')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Other edition available'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'language_code': value.get('e'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'country_code': value.get('f'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('additional_physical_form_entry', '^776[10_][8_]')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Available in another form'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('issued_with_entry', '^777[10_][8_]')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Issued with'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('preceding_entry', '^780[10_][10325476_]')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'1': u'Continues in part', u'0': u'Continues', u'3': u'Supersedes in part', u'2': u'Supersedes',
                      u'5': u'Absorbed', u'4': u'Formed by the union of ... and ...', u'7': u'Separated from', u'6': u'Absorbed in part'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('succeeding_entry', '^785[10_][103254768_]')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'1': u'Continued in part by', u'0': u'Continued by', u'3': u'Superseded in part by', u'2': u'Superseded by', u'5':
                      u'Absorbed in part by', u'4': u'Absorbed by', u'7': u'Merged with ... to form ...', u'6': u'Split into ... and ...', u'8': u'Changed back to'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }


@marc21.over('data_source_entry', '^786[10_][8_]')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Data source'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'period_of_content': value.get('j'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'source_contribution': value.get('v'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('other_relationship_entry', '^787[10_][8_]')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {
        u'8': u'No display constant generated', u'#': u'Related item'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }
