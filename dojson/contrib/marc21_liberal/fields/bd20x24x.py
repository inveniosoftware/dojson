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

from ..model import marc21_liberal


@marc21_liberal.over('abbreviated_title', '^210..')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "Other abbreviated title", "_": "Abbreviated key title"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'qualifying_information',
        '6': 'linkage',
        'a': 'abbreviated_title',
        '2': 'source',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('type')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'abbreviated_title': value.get('a'),
        'source': utils.force_list(
            value.get('2')
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
        '8': 'field_link_and_sequence_number',
        'b': 'qualifying_information',
        'a': 'key_title',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': value.get('b'),
        'key_title': value.get('a'),
        'linkage': value.get('6'),
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
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'a': 'uniform_title',
        'h': 'medium',
        's': 'version',
        'g': 'miscellaneous_information',
        'p': 'name_of_part_section_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'r': 'key_for_music',
        'd': 'date_of_treaty_signing',
        'k': 'form_subheading',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'o': 'arranged_statement_for_music',
        'm': 'medium_of_performance_for_music',
        'l': 'language_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('uniform_title_printed_or_displayed')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_a_work': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('a'),
        'medium': value.get('h'),
        'version': value.get('s'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'key_for_music': value.get('r'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'arranged_statement_for_music': value.get('o'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
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
        'n': 'number_of_part_section_of_a_work',
        'h': 'medium',
        'b': 'remainder_of_title',
        'a': 'title',
        'c': 'statement_of_responsibility',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'p': 'name_of_part_section_of_a_work',
        'y': 'language_code_of_translated_title',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'medium': value.get('h'),
        'remainder_of_title': value.get('b'),
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'language_code_of_translated_title': value.get('y'),
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
        'f': 'date_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        'a': 'uniform_title',
        'h': 'medium',
        's': 'version',
        'g': 'miscellaneous_information',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'o': 'arranged_statement_for_music',
        'm': 'medium_of_performance_for_music',
        'k': 'form_subheading',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('uniform_title_printed_or_displayed')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_a_work': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'uniform_title': value.get('a'),
        'medium': value.get('h'),
        'version': value.get('s'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'key_for_music': value.get('r'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'arranged_statement_for_music': value.get('o'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
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
        'f': 'inclusive_dates',
        'n': 'number_of_part_section_of_a_work',
        'b': 'remainder_of_title',
        'a': 'title',
        'c': 'statement_of_responsibility',
        'h': 'medium',
        's': 'version',
        'g': 'bulk_dates',
        'p': 'name_of_part_section_of_a_work',
        'k': 'form',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'inclusive_dates': value.get('f'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'remainder_of_title': value.get('b'),
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'medium': value.get('h'),
        'version': value.get('s'),
        'bulk_dates': value.get('g'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'form': utils.force_list(
            value.get('k')
        ),
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
        'f': 'date_or_sequential_designation',
        'h': 'medium',
        'b': 'remainder_of_title',
        'a': 'title_proper_short_title',
        'i': 'display_text',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_added_entry_controller')

    if key[4] != '_':
        order.append('type_of_title')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_or_sequential_designation': value.get('f'),
        'medium': value.get('h'),
        'remainder_of_title': value.get('b'),
        'title_proper_short_title': value.get('a'),
        'display_text': value.get('i'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
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
        'f': 'date_or_sequential_designation',
        'h': 'medium',
        'b': 'remainder_of_title',
        'x': 'international_standard_serial_number',
        'a': 'title',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'g': 'miscellaneous_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('title_added_entry')

    if key[4] != '_':
        order.append('note_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_or_sequential_designation': value.get('f'),
        'medium': value.get('h'),
        'remainder_of_title': value.get('b'),
        'international_standard_serial_number': value.get('x'),
        'title': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'title_added_entry': indicator_map1.get(key[3], key[3]),
        'note_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
