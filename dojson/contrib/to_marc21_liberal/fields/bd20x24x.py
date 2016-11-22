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
        'abbreviated_title': 'a',
        'qualifying_information': 'b',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'type'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('abbreviated_title'),
        'b': value.get('qualifying_information'),
        '2': utils.reverse_force_list(
            value.get('source')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'key_title': 'a',
        'qualifying_information': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('key_title'),
        'b': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['uniform_title_printed_or_displayed', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'title': 'a',
        'remainder_of_title': 'b',
        'statement_of_responsibility': 'c',
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'language_code_of_translated_title': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'c': value.get('statement_of_responsibility'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'y': value.get('language_code_of_translated_title'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['uniform_title_printed_or_displayed', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'title': 'a',
        'remainder_of_title': 'b',
        'statement_of_responsibility': 'c',
        'inclusive_dates': 'f',
        'bulk_dates': 'g',
        'medium': 'h',
        'form': 'k',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'version': 's',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'c': value.get('statement_of_responsibility'),
        'f': value.get('inclusive_dates'),
        'g': value.get('bulk_dates'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'title_proper_short_title': 'a',
        'remainder_of_title': 'b',
        'date_or_sequential_designation': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'display_text': 'i',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_added_entry_controller', 'type_of_title'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title_proper_short_title'),
        'b': value.get('remainder_of_title'),
        'f': value.get('date_or_sequential_designation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'i': value.get('display_text'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'title': 'a',
        'remainder_of_title': 'b',
        'date_or_sequential_designation': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'international_standard_serial_number': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['title_added_entry', 'note_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'f': value.get('date_or_sequential_designation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'x': value.get('international_standard_serial_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), value.get('title_added_entry', '_')),
        '$ind2': indicator_map2.get(value.get('note_controller'), value.get('note_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
