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


@to_marc21.over('210', '^abbreviated_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_abbreviated_title(self, key, value):
    """Reverse - Abbreviated Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Abbreviated key title": "_", "Other abbreviated title": "0"}
    field_map = {
        'abbreviated_title': 'a',
        'qualifying_information': 'b',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('abbreviated_title'),
        'b': value.get('qualifying_information'),
        '2': utils.reverse_force_list(
            value.get('source')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('type'), '_'),
    }


@to_marc21.over('222', '^key_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_key_title(self, key, value):
    """Reverse - Key Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'key_title': 'a',
        'qualifying_information': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('key_title'),
        'b': value.get('qualifying_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('240', '^uniform_title$')
@utils.filter_values
def reverse_uniform_title(self, key, value):
    """Reverse - Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'uniform_title': 'a',
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'version': 's',
        'key_for_music': 'r',
        'language_of_a_work': 'l',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'date_of_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'authority_record_control_number_or_standard_number': '0',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'l': value.get('language_of_a_work'),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('242', '^translation_of_title_by_cataloging_agency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_of_title_by_cataloging_agency(self, key, value):
    """Reverse - Translation of Title by Cataloging Agency."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'title': 'a',
        'remainder_of_title': 'b',
        'statement_of_responsibility': 'c',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'language_code_of_translated_title': 'y',
        'medium': 'h',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'c': value.get('statement_of_responsibility'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'y': value.get('language_code_of_translated_title'),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('243', '^collective_uniform_title$')
@utils.filter_values
def reverse_collective_uniform_title(self, key, value):
    """Reverse - Collective Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'uniform_title': 'a',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'version': 's',
        'key_for_music': 'r',
        'language_of_a_work': 'l',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'date_of_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'l': value.get('language_of_a_work'),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('245', '^title_statement$')
@utils.filter_values
def reverse_title_statement(self, key, value):
    """Reverse - Title Statement."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'title': 'a',
        'remainder_of_title': 'b',
        'form': 'k',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'medium': 'h',
        'statement_of_responsibility': 'c',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'inclusive_dates': 'f',
        'bulk_dates': 'g',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'k': utils.reverse_force_list(
            value.get('form')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'h': value.get('medium'),
        'c': value.get('statement_of_responsibility'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'f': value.get('inclusive_dates'),
        'g': value.get('bulk_dates'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('246', '^varying_form_of_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_varying_form_of_title(self, key, value):
    """Reverse - Varying Form of Title."""
    indicator_map1 = {"No note, added entry": "3", "No note, no added entry": "2", "Note, added entry": "1", "Note, no added entry": "0"}
    indicator_map2 = {"Added title page title": "5", "Caption title": "6", "Cover title": "4", "Distinctive title": "2", "No type specified": "_", "Other title": "3", "Parallel title": "1", "Portion of title": "0", "Running title": "7", "Spine title": "8"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'title_proper_short_title': 'a',
        'display_text': 'i',
        'date_or_sequential_designation': 'f',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'remainder_of_title': 'b',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        'a': value.get('title_proper_short_title'),
        'i': value.get('display_text'),
        'f': value.get('date_or_sequential_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'b': value.get('remainder_of_title'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_added_entry_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_title'), '_'),
    }


@to_marc21.over('247', '^former_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title(self, key, value):
    """Reverse - Former Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Display note": "0", "Do not display note": "1"}
    field_map = {
        'title': 'a',
        'remainder_of_title': 'b',
        'date_or_sequential_designation': 'f',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'f': value.get('date_or_sequential_designation'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('note_controller'), '_'),
    }
