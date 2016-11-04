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
    indicator_map2 = {
        "Abbreviated key title": "_",
        "Other abbreviated title": "0"}
    field_map = {
        'linkage': '6',
        'abbreviated_title': 'a',
        'qualifying_information': 'b',
        'source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('title_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('title_added_entry'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type'), '7') != '7':
        try:
            order.remove(field_map.get('type'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('abbreviated_title'),
        'b': value.get('qualifying_information'),
        '2': utils.reverse_force_list(
            value.get('source')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'linkage': '6',
        'key_title': 'a',
        'qualifying_information': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('key_title'),
        'b': value.get('qualifying_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('240', '^uniform_title$')
@utils.filter_values
def reverse_uniform_title(self, key, value):
    """Reverse - Uniform Title."""
    indicator_map1 = {
        "Not printed or displayed": "0",
        "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'linkage': '6',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'language_of_a_work': 'l',
        'key_for_music': 'r',
        'authority_record_control_number_or_standard_number': '0',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'uniform_title': 'a',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('uniform_title_printed_or_displayed'), '7') != '7':
        try:
            order.remove(field_map.get('uniform_title_printed_or_displayed'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'l': value.get('language_of_a_work'),
        'r': value.get('key_for_music'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('uniform_title'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
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
        'linkage': '6',
        'statement_of_responsibility': 'c',
        'language_code_of_translated_title': 'y',
        'number_of_part_section_of_a_work': 'n',
        'remainder_of_title': 'b',
        'field_link_and_sequence_number': '8',
        'medium': 'h',
        'title': 'a',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('title_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('title_added_entry'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('statement_of_responsibility'),
        'y': value.get('language_code_of_translated_title'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'b': value.get('remainder_of_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('medium'),
        'a': value.get('title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('243', '^collective_uniform_title$')
@utils.filter_values
def reverse_collective_uniform_title(self, key, value):
    """Reverse - Collective Uniform Title."""
    indicator_map1 = {
        "Not printed or displayed": "0",
        "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'linkage': '6',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'language_of_a_work': 'l',
        'key_for_music': 'r',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'uniform_title': 'a',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('uniform_title_printed_or_displayed'), '7') != '7':
        try:
            order.remove(field_map.get('uniform_title_printed_or_displayed'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'l': value.get('language_of_a_work'),
        'r': value.get('key_for_music'),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('uniform_title'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
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
        'linkage': '6',
        'remainder_of_title': 'b',
        'medium': 'h',
        'bulk_dates': 'g',
        'name_of_part_section_of_a_work': 'p',
        'statement_of_responsibility': 'c',
        'inclusive_dates': 'f',
        'version': 's',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'title': 'a',
        'form': 'k',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('title_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('title_added_entry'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('remainder_of_title'),
        'h': value.get('medium'),
        'g': value.get('bulk_dates'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': value.get('statement_of_responsibility'),
        'f': value.get('inclusive_dates'),
        's': value.get('version'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('title'),
        'k': utils.reverse_force_list(
            value.get('form')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('246', '^varying_form_of_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_varying_form_of_title(self, key, value):
    """Reverse - Varying Form of Title."""
    indicator_map1 = {
        "No note, added entry": "3",
        "No note, no added entry": "2",
        "Note, added entry": "1",
        "Note, no added entry": "0"}
    indicator_map2 = {
        "Added title page title": "5",
        "Caption title": "6",
        "Cover title": "4",
        "Distinctive title": "2",
        "No type specified": "_",
        "Other title": "3",
        "Parallel title": "1",
        "Portion of title": "0",
        "Running title": "7",
        "Spine title": "8"}
    field_map = {
        'linkage': '6',
        'miscellaneous_information': 'g',
        'date_or_sequential_designation': 'f',
        'remainder_of_title': 'b',
        'display_text': 'i',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'number_of_part_section_of_a_work': 'n',
        'medium': 'h',
        'title_proper_short_title': 'a',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('note_added_entry_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_added_entry_controller'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_title'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_title'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_or_sequential_designation'),
        'b': value.get('remainder_of_title'),
        'i': value.get('display_text'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'a': value.get('title_proper_short_title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
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
        'linkage': '6',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'date_or_sequential_designation': 'f',
        'remainder_of_title': 'b',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'medium': 'h',
        'title': 'a',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('title_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('title_added_entry'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('note_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_or_sequential_designation'),
        'b': value.get('remainder_of_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'a': value.get('title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('note_controller'), '_'),
    }
