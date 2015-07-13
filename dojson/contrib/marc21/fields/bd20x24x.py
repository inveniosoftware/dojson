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

from ..model import marc21


@marc21.over('abbreviated_title', '^210[10_][0_]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    """Abbreviated Title."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {
        "#": "Abbreviated key title",
        "0": "Other abbreviated title"}
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


@marc21.over('key_title', '^222.[_1032547698]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    """Key Title."""
    indicator_map2 = {
        "0": "No nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
    return {
        'key_title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21.over('uniform_title', '^240[10_][_1032547698]')
@utils.filter_values
def uniform_title(self, key, value):
    """Uniform Title."""
    indicator_map1 = {
        "0": "Not printed or displayed",
        "1": "Printed or displayed"}
    indicator_map2 = {
        "0": "Number of nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
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


@marc21.over(
    'translation_of_title_by_cataloging_agency', '^242[10_][_1032547698]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    """Translation of Title by Cataloging Agency."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {
        "0": "No nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
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


@marc21.over('collective_uniform_title', '^243[10_][_1032547698]')
@utils.filter_values
def collective_uniform_title(self, key, value):
    """Collective Uniform Title."""
    indicator_map1 = {
        "0": "Not printed or displayed",
        "1": "Printed or displayed"}
    indicator_map2 = {
        "0": "Number of nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
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


@marc21.over('title_statement', '^245[10_][_1032547698]')
@utils.filter_values
def title_statement(self, key, value):
    """Title Statement."""
    indicator_map1 = {"0": "No added entry", "1": "Added entry"}
    indicator_map2 = {
        "0": "No nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
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


@marc21.over('varying_form_of_title', '^246[1032_][_103254768]')
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
        "#": "No type specified",
        "0": "Portion of title",
        "1": "Parallel title",
        "2": "Distinctive title",
        "3": "Other title",
        "4": "Cover title",
        "5": "Added title page title",
        "6": "Caption title",
        "7": "Running title",
        "8": "Spine title"}
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
