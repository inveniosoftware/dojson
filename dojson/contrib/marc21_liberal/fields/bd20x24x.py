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

from ..utils import liberal_map_order
from ..model import marc21_liberal


@marc21_liberal.over('abbreviated_title', '^210..')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "Other abbreviated title", "_": "Abbreviated key title"}
    field_map = {
        'a': 'abbreviated_title',
        'b': 'qualifying_information',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('type')

    record_dict = {
        '__order__': order if len(order) else None,
        'abbreviated_title': value.get('a'),
        'qualifying_information': value.get('b'),
        'source': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3], key[3]),
        'type': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('key_title', '^222..')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    """Key Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'key_title',
        'b': 'qualifying_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'key_title': value.get('a'),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('uniform_title', '^240..')
@utils.filter_values
def uniform_title(self, key, value):
    """Uniform Title."""
    indicator_map1 = {"0": "Not printed or displayed", "1": "Printed or displayed"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('uniform_title_printed_or_displayed')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3], key[3]),
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('translation_of_title_by_cataloging_agency', '^242..')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    """Translation of Title by Cataloging Agency."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'c': 'statement_of_responsibility',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'y': 'language_code_of_translated_title',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'statement_of_responsibility': value.get('c'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'language_code_of_translated_title': value.get('y'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3], key[3]),
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('collective_uniform_title', '^243..')
@utils.filter_values
def collective_uniform_title(self, key, value):
    """Collective Uniform Title."""
    indicator_map1 = {"0": "Not printed or displayed", "1": "Printed or displayed"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('uniform_title_printed_or_displayed')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3], key[3]),
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('title_statement', '^245..')
@utils.filter_values
def title_statement(self, key, value):
    """Title Statement."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'c': 'statement_of_responsibility',
        'f': 'inclusive_dates',
        'g': 'bulk_dates',
        'h': 'medium',
        'k': 'form',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        's': 'version',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'statement_of_responsibility': value.get('c'),
        'inclusive_dates': value.get('f'),
        'bulk_dates': value.get('g'),
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
        'title_added_entry': indicator_map1.get(key[3], key[3]),
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('varying_form_of_title', '^246..')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    """Varying Form of Title."""
    indicator_map1 = {"0": "Note, no added entry", "1": "Note, added entry", "2": "No note, no added entry", "3": "No note, added entry"}
    indicator_map2 = {"0": "Portion of title", "1": "Parallel title", "2": "Distinctive title", "3": "Other title", "4": "Cover title", "5": "Added title page title", "6": "Caption title", "7": "Running title", "8": "Spine title", "_": "No type specified"}
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('note_added_entry_controller')

    if key[4] != '_':
        order.append('type_of_title')

    record_dict = {
        '__order__': order if len(order) else None,
        'title_proper_short_title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date_or_sequential_designation': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'display_text': value.get('i'),
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
        'note_added_entry_controller': indicator_map1.get(key[3], key[3]),
        'type_of_title': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('former_title', '^247..')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    """Former Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "Display note", "1": "Do not display note"}
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('note_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date_or_sequential_designation': value.get('f'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_added_entry': indicator_map1.get(key[3], key[3]),
        'note_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
