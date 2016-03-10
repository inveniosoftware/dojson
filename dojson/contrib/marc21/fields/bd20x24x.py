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


@marc21.over('abbreviated_title', '^210[10_][0_]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {
        '0': 'No added entry',
        '1': 'Added entry',
    }

    indicator_map2 = {
        '_': 'Abbreviated key title',
        '0': 'Other abbreviated title',
    }

    field_map = {
        'a': 'abbreviated_title',
        'b': 'qualifying_information',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')
    if key[4] in indicator_map2:
        order.append('type')

    return {
        '__order__': tuple(order) if len(order) else None,
        'abbreviated_title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': utils.force_list(
            value.get('2')
        ),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'title_added_entry': indicator_map1.get(key[3]),
        'type': indicator_map2.get(key[4]),
    }


@marc21.over('key_title', '^222_[_0-9]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    """Key Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    field_map = {
        'a': 'key_title',
        'b': 'qualifying_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'key_title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over('uniform_title', '^240[_01][_0-9]')
@utils.filter_values
def uniform_title(self, key, value):
    """Uniform Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map1 = {
        '0': 'Not printed or displayed',
        '1': 'Printed or displayed',
    }

    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('uniform_title_printed_or_displayed')
    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over(
    'translation_of_title_by_cataloging_agency', '^242[_01][_0-9]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    """Translation of Title by Cataloging Agency."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map1 = {
        '0': 'No added entry',
        '1': 'Added entry',
    }

    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'c': 'statement_of_responsibility_etc.',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'y': 'language_code_of_translated_title',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')
    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'remainder_of_title': value.get('b'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'language_code_of_translated_title': value.get('y'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over('collective_uniform_title', '^243[_01][_0-9]')
@utils.filter_values
def collective_uniform_title(self, key, value):
    """Collective Uniform Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map1 = {
        '0': 'Not printed or displayed',
        '1': 'Printed or displayed',
    }

    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('uniform_title_printed_or_displayed')
    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over('title_statement', '^245[_01][_0-9]')
@utils.filter_values
def title_statement(self, key, value):
    """Title Statement."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map1 = {
        '0': 'No added entry',
        '1': 'Added entry',
    }

    field_map = {
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'title',
        'b': 'remainder_of_title',
        'c': 'statement_of_responsibility',
        'f': 'inclusive_dates',
        'g': 'bulk_dates',
        'h': 'medium',
        'k': 'form',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        's': 'version'
    }

    order = utils.map_order(field_map, value)
    if key[3] in indicator_map1:
        order.append('title_added_entry')
    if key[4] in valid_nonfiling_characters:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'remainder_of_title': value.get('b'),
        'bulk_dates': value.get('g'),
        'inclusive_dates': value.get('f'),
        'medium': value.get('h'),
        'form': utils.force_list(
            value.get('k')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': utils.int_with_default(key[4], None),
    }


@marc21.over('varying_form_of_title', '^246[1032_][_103254768]')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    """Varying Form of Title."""
    indicator_map1 = {
        '0': 'Note, no added entry',
        '1': 'Note, added entry',
        '2': 'No note, no added entry',
        '3': 'No note, added entry',
    }

    indicator_map2 = {
        '_': 'No type specified',
        '0': 'Portion of title',
        '1': 'Parallel title',
        '2': 'Distinctive title',
        '3': 'Other title',
        '4': 'Cover title',
        '5': 'Added title page title',
        '6': 'Caption title',
        '7': 'Running title',
        '8': 'Spine title',
    }

    field_map = {
        'a': 'title_proper_short_title',
        'b': 'remainder_of_title',
        'f': 'date_or_sequential_designation',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'display_text',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_added_entry_controller')

    if key[4] in indicator_map2:
        order.append('type_of_title')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title_proper_short_title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'display_text': value.get('i'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_added_entry_controller': indicator_map1.get(key[3]),
        'type_of_title': indicator_map2.get(key[4]),
    }


@marc21.over('former_title', '^247[10_][10_]')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    """Former Title."""
    indicator_map1 = {
        '0': 'No added entry',
        '1': 'Added entry',
    }
    indicator_map2 = {
        '0': 'Display note',
        '1': 'Do not display note',
    }

    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'f': 'date_or_sequential_designation',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'x': 'international_standard_serial_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('title_added_entry')
    if key[4] in indicator_map2:
        order.append('note_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3]),
        'note_controller': indicator_map2.get(key[4]),
    }
