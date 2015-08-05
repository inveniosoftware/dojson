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


@marc21.over('abbreviated_title', '^210[10_][0_]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"#": "Abbreviated key title", "0": "Other abbreviated title"}
    return {
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


@tomarc21.over('210', 'abbreviated_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_abbreviated_title(self, key, value):
    """Reverse - Abbreviated Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Abbreviated key title": "_", "Other abbreviated title": "0"}
    return {
        'a': utils.reverse_force_list(value.get('abbreviated_title')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source')),
        'b': utils.reverse_force_list(value.get('qualifying_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('title_added_entry')),
        '$ind2': indicator_map2.get(value.get('type')),
    }


@marc21.over('key_title', '^222.[_1032547698]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    """Key Title."""
    indicator_map2 = {"0": "No nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
        'key_title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('222', 'key_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_key_title(self, key, value):
    """Reverse - Key Title."""
    indicator_map2 = {"No nonfiling characters": "0", "Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('key_title')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('qualifying_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('uniform_title', '^240[10_][_1032547698]')
@utils.filter_values
def uniform_title(self, key, value):
    """Uniform Title."""
    indicator_map1 = {"0": "Not printed or displayed", "1": "Printed or displayed"}
    indicator_map2 = {"0": "Number of nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
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
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('240', 'uniform_title')
@utils.filter_values
def reverse_uniform_title(self, key, value):
    """Reverse - Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {"Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('uniform_title')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'd': utils.reverse_force_list(value.get('date_of_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('translation_of_title_by_cataloging_agency', '^242[10_][_1032547698]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    """Translation of Title by Cataloging Agency."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "No nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
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
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('242', 'translation_of_title_by_cataloging_agency')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_of_title_by_cataloging_agency(self, key, value):
    """Reverse - Translation of Title by Cataloging Agency."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"No nonfiling characters": "0", "Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('title')),
        'c': utils.reverse_force_list(value.get('statement_of_responsibility')),
        'b': utils.reverse_force_list(value.get('remainder_of_title')),
        'h': utils.reverse_force_list(value.get('medium')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('language_code_of_translated_title')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('title_added_entry')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('collective_uniform_title', '^243[10_][_1032547698]')
@utils.filter_values
def collective_uniform_title(self, key, value):
    """Collective Uniform Title."""
    indicator_map1 = {"0": "Not printed or displayed", "1": "Printed or displayed"}
    indicator_map2 = {"0": "Number of nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
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
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('243', 'collective_uniform_title')
@utils.filter_values
def reverse_collective_uniform_title(self, key, value):
    """Reverse - Collective Uniform Title."""
    indicator_map1 = {"Not printed or displayed": "0", "Printed or displayed": "1"}
    indicator_map2 = {"Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('uniform_title')),
        'd': utils.reverse_force_list(value.get('date_of_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('uniform_title_printed_or_displayed')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('title_statement', '^245[10_][_1032547698]')
@utils.filter_values
def title_statement(self, key, value):
    """Title Statement."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "No nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
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
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('245', 'title_statement')
@utils.filter_values
def reverse_title_statement(self, key, value):
    """Reverse - Title Statement."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"No nonfiling characters": "0", "Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('title')),
        'c': utils.reverse_force_list(value.get('statement_of_responsibility')),
        'b': utils.reverse_force_list(value.get('remainder_of_title')),
        'g': utils.reverse_force_list(value.get('bulk_dates')),
        'f': utils.reverse_force_list(value.get('inclusive_dates')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('title_added_entry')),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('varying_form_of_title', '^246[1032_][_103254768]')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    """Varying Form of Title."""
    indicator_map1 = {"0": "Note, no added entry", "1": "Note, added entry", "2": "No note, no added entry", "3": "No note, added entry"}
    indicator_map2 = {"#": "No type specified", "0": "Portion of title", "1": "Parallel title", "2": "Distinctive title", "3": "Other title", "4": "Cover title", "5": "Added title page title", "6": "Caption title", "7": "Running title", "8": "Spine title"}
    return {
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


@tomarc21.over('246', 'varying_form_of_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_varying_form_of_title(self, key, value):
    """Reverse - Varying Form of Title."""
    indicator_map1 = {"No note, added entry": "3", "No note, no added entry": "2", "Note, added entry": "1", "Note, no added entry": "0"}
    indicator_map2 = {"Added title page title": "5", "Caption title": "6", "Cover title": "4", "Distinctive title": "2", "No type specified": "_", "Other title": "3", "Parallel title": "1", "Portion of title": "0", "Running title": "7", "Spine title": "8"}
    return {
        'a': utils.reverse_force_list(value.get('title_proper_short_title')),
        'b': utils.reverse_force_list(value.get('remainder_of_title')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_or_sequential_designation')),
        'i': utils.reverse_force_list(value.get('display_text')),
        'h': utils.reverse_force_list(value.get('medium')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('note_added_entry_controller')),
        '$ind2': indicator_map2.get(value.get('type_of_title')),
    }


@marc21.over('former_title', '^247[10_][10_]')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    """Former Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {"0": "Display note", "1": "Do not display note"}
    return {
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


@tomarc21.over('247', 'former_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title(self, key, value):
    """Reverse - Former Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Display note": "0", "Do not display note": "1"}
    return {
        'a': utils.reverse_force_list(value.get('title')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'b': utils.reverse_force_list(value.get('remainder_of_title')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_or_sequential_designation')),
        'h': utils.reverse_force_list(value.get('medium')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('title_added_entry')),
        '$ind2': indicator_map2.get(value.get('note_controller')),
    }
