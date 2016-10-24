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


@marc21.over('abbreviated_title', '^210[01_][0_]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {
        "0": "Other abbreviated title",
        "_": "Abbreviated key title"}
    field_map = {
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'abbreviated_title',
        'b': 'qualifying_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')

    if key[4] in indicator_map2:
        order.append('type')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'abbreviated_title': value.get('a'),
        'qualifying_information': value.get('b'),
        'title_added_entry': indicator_map1.get(key[3]),
        'type': indicator_map2.get(key[4]),
    }


@marc21.over('key_title', '^222.[2589610743_]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    """Key Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '6': 'linkage',
        'b': 'qualifying_information',
        '8': 'field_link_and_sequence_number',
        'a': 'key_title',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'qualifying_information': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key_title': value.get('a'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('uniform_title', '^240[01_][2589610743_]')
@utils.filter_values
def uniform_title(self, key, value):
    """Uniform Title."""
    indicator_map1 = {
        "0": "Not printed or displayed",
        "1": "Printed or displayed"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'f': 'date_of_a_work',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        'a': 'uniform_title',
        'r': 'key_for_music',
        's': 'version',
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'form_subheading',
        'g': 'miscellaneous_information',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'o': 'arranged_statement_for_music',
        'm': 'medium_of_performance_for_music',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('uniform_title_printed_or_displayed')

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_of_a_work': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'uniform_title': value.get('a'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'arranged_statement_for_music': value.get('o'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('translation_of_title_by_cataloging_agency',
             '^242[01_][2589610743_]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    """Translation of Title by Cataloging Agency."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'b': 'remainder_of_title',
        '8': 'field_link_and_sequence_number',
        'y': 'language_code_of_translated_title',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'c': 'statement_of_responsibility',
        'p': 'name_of_part_section_of_a_work',
        'a': 'title',
        'h': 'medium',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'remainder_of_title': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_code_of_translated_title': value.get('y'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'statement_of_responsibility': value.get('c'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'title': value.get('a'),
        'medium': value.get('h'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('collective_uniform_title', '^243[01_][2589610743_]')
@utils.filter_values
def collective_uniform_title(self, key, value):
    """Collective Uniform Title."""
    indicator_map1 = {
        "0": "Not printed or displayed",
        "1": "Printed or displayed"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'f': 'date_of_a_work',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        'a': 'uniform_title',
        'r': 'key_for_music',
        's': 'version',
        'k': 'form_subheading',
        'g': 'miscellaneous_information',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'o': 'arranged_statement_for_music',
        'm': 'medium_of_performance_for_music',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('uniform_title_printed_or_displayed')

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_of_a_work': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'uniform_title': value.get('a'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'arranged_statement_for_music': value.get('o'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('title_statement', '^245[01_][2589610743_]')
@utils.filter_values
def title_statement(self, key, value):
    """Title Statement."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'f': 'inclusive_dates',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'k': 'form',
        'c': 'statement_of_responsibility',
        's': 'version',
        'b': 'remainder_of_title',
        'h': 'medium',
        'a': 'title',
        'g': 'bulk_dates',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'inclusive_dates': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form': utils.force_list(
            value.get('k')
        ),
        'statement_of_responsibility': value.get('c'),
        'version': value.get('s'),
        'remainder_of_title': value.get('b'),
        'medium': value.get('h'),
        'title': value.get('a'),
        'bulk_dates': value.get('g'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('varying_form_of_title', '^246[2031_][258610743_]')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    """Varying Form of Title."""
    indicator_map1 = {
        "0": "Note, no added entry",
        "1": "Note, added entry",
        "2": "No note, no added entry",
        "3": "No note, added entry"}
    indicator_map2 = {
        "0": "Portion of title",
        "1": "Parallel title",
        "2": "Distinctive title",
        "3": "Other title",
        "4": "Cover title",
        "5": "Added title page title",
        "6": "Caption title",
        "7": "Running title",
        "8": "Spine title",
        "_": "No type specified"}
    field_map = {
        'b': 'remainder_of_title',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        'f': 'date_or_sequential_designation',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'i': 'display_text',
        'n': 'number_of_part_section_of_a_work',
        'a': 'title_proper_short_title',
        'g': 'miscellaneous_information',
        'h': 'medium',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_added_entry_controller')

    if key[4] in indicator_map2:
        order.append('type_of_title')

    return {
        '__order__': tuple(order) if len(order) else None,
        'remainder_of_title': value.get('b'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_or_sequential_designation': value.get('f'),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'display_text': value.get('i'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'title_proper_short_title': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'note_added_entry_controller': indicator_map1.get(key[3]),
        'type_of_title': indicator_map2.get(key[4]),
    }


@marc21.over('former_title', '^247[01_][01_]')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    """Former Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "Display note", "1": "Do not display note"}
    field_map = {
        'b': 'remainder_of_title',
        '8': 'field_link_and_sequence_number',
        'x': 'international_standard_serial_number',
        'f': 'date_or_sequential_designation',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'a': 'title',
        'g': 'miscellaneous_information',
        'h': 'medium',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')

    if key[4] in indicator_map2:
        order.append('note_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'remainder_of_title': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_serial_number': value.get('x'),
        'date_or_sequential_designation': value.get('f'),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'title': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'title_added_entry': indicator_map1.get(key[3]),
        'note_controller': indicator_map2.get(key[4]),
    }
