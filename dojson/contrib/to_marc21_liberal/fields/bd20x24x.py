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


@to_marc21_liberal.over('210', '^abbreviated_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_abbreviated_title(self, key, value):
    """Reverse - Abbreviated Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Abbreviated key title": "_", "Other abbreviated title": "0"}
    field_map = {
        'linkage': '6',
        'abbreviated_title': 'a',
        'field_link_and_sequence_number': '8',
        'source': '2',
        'qualifying_information': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'type'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('abbreviated_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source')
        ),
        'b': value.get('qualifying_information'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), value.get('title_added_entry', '_')),
        '$ind2': indicator_map2.get(value.get('type'), value.get('type', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('222', '^key_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_key_title(self, key, value):
    """Reverse - Key Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'linkage': '6',
        'key_title': 'a',
        'field_link_and_sequence_number': '8',
        'qualifying_information': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('key_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('qualifying_information'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('240', '^uniform_title$')
@utils.filter_values
def reverse_uniform_title(self, key, value):
    """Reverse - Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'medium': 'h',
        'key_for_music': 'r',
        'authority_record_control_number_or_standard_number': '0',
        'date_of_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
        'language_of_a_work': 'l',
        'form_subheading': 'k',
        'linkage': '6',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'date_of_a_work': 'f',
        'uniform_title': 'a',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['uniform_title_printed_or_displayed', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        'r': value.get('key_for_music'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        'l': value.get('language_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('uniform_title'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed'), value.get('uniform_title_printed_or_displayed', '_')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('242', '^translation_of_title_by_cataloging_agency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_of_title_by_cataloging_agency(self, key, value):
    """Reverse - Translation of Title by Cataloging Agency."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'medium': 'h',
        'linkage': '6',
        'title': 'a',
        'statement_of_responsibility': 'c',
        'language_code_of_translated_title': 'y',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'remainder_of_title': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('title'),
        'c': value.get('statement_of_responsibility'),
        'y': value.get('language_code_of_translated_title'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'b': value.get('remainder_of_title'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), value.get('title_added_entry', '_')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('243', '^collective_uniform_title$')
@utils.filter_values
def reverse_collective_uniform_title(self, key, value):
    """Reverse - Collective Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'medium': 'h',
        'key_for_music': 'r',
        'linkage': '6',
        'date_of_treaty_signing': 'd',
        'language_of_a_work': 'l',
        'form_subheading': 'k',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'date_of_a_work': 'f',
        'uniform_title': 'a',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['uniform_title_printed_or_displayed', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        'r': value.get('key_for_music'),
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'l': value.get('language_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('uniform_title'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed'), value.get('uniform_title_printed_or_displayed', '_')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('245', '^title_statement$')
@utils.filter_values
def reverse_title_statement(self, key, value):
    """Reverse - Title Statement."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'medium': 'h',
        'linkage': '6',
        'title': 'a',
        'statement_of_responsibility': 'c',
        'form': 'k',
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'inclusive_dates': 'f',
        'bulk_dates': 'g',
        'remainder_of_title': 'b',
        'number_of_part_section_of_a_work': 'n',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('title'),
        'c': value.get('statement_of_responsibility'),
        'k': utils.reverse_force_list(
            value.get('form')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('inclusive_dates'),
        'g': value.get('bulk_dates'),
        'b': value.get('remainder_of_title'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), value.get('title_added_entry', '_')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('246', '^varying_form_of_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_varying_form_of_title(self, key, value):
    """Reverse - Varying Form of Title."""
    indicator_map1 = {"No note, added entry": "3", "No note, no added entry": "2", "Note, added entry": "1", "Note, no added entry": "0"}
    indicator_map2 = {"Added title page title": "5", "Caption title": "6", "Cover title": "4", "Distinctive title": "2", "No type specified": "_", "Other title": "3", "Parallel title": "1", "Portion of title": "0", "Running title": "7", "Spine title": "8"}
    field_map = {
        'date_or_sequential_designation': 'f',
        'medium': 'h',
        'linkage': '6',
        'title_proper_short_title': 'a',
        'display_text': 'i',
        'number_of_part_section_of_a_work': 'n',
        'miscellaneous_information': 'g',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'remainder_of_title': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_added_entry_controller', 'type_of_title'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'f': value.get('date_or_sequential_designation'),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('title_proper_short_title'),
        'i': value.get('display_text'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'b': value.get('remainder_of_title'),
        '$ind1': indicator_map1.get(value.get('note_added_entry_controller'), value.get('note_added_entry_controller', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_title'), value.get('type_of_title', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('247', '^former_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title(self, key, value):
    """Reverse - Former Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Display note": "0", "Do not display note": "1"}
    field_map = {
        'date_or_sequential_designation': 'f',
        'medium': 'h',
        'linkage': '6',
        'title': 'a',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'remainder_of_title': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'note_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'f': value.get('date_or_sequential_designation'),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'b': value.get('remainder_of_title'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), value.get('title_added_entry', '_')),
        '$ind2': indicator_map2.get(value.get('note_controller'), value.get('note_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
