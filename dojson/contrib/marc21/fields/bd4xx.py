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


@marc21.over('series_statement_added_entry_personal_name', '^400[103_][10_]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    """Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    return {
        'personal_name': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('400', '^series_statement_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_personal_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    return {
        'a': utils.reverse_force_list(value.get('personal_name')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('titles_and_other_words_associated_with_a_name')),
        'b': utils.reverse_force_list(value.get('numeration')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('dates_associated_with_a_name')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'v': utils.reverse_force_list(value.get('volume_sequential_designation')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry')),
    }


@marc21.over('series_statement_added_entry_corporate_name', '^410[10_2][10_]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    """Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('410', '^series_statement_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_corporate_name(self, key, value):
    """Reverse - Series Statement/Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    return {
        'a': utils.reverse_force_list(value.get('corporate_name_or_jurisdiction_name_as_entry_element')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'b': utils.reverse_force_list(value.get('subordinate_unit')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('date_of_meeting_or_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'v': utils.reverse_force_list(value.get('volume_sequential_designation')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry')),
    }


@marc21.over('series_statement_added_entry_meeting_name', '^411[10_2][10_]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    """Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Main entry not represented by pronoun", "1": "Main entry represented by pronoun"}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('411', '^series_statement_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_meeting_name(self, key, value):
    """Reverse - Series Statement/Added Entry Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Main entry not represented by pronoun": "0", "Main entry represented by pronoun": "1"}
    return {
        'a': utils.reverse_force_list(value.get('meeting_name_or_jurisdiction_name_as_entry_element')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'e': utils.reverse_force_list(value.get('subordinate_unit')),
        'd': utils.reverse_force_list(value.get('date_of_meeting')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'v': utils.reverse_force_list(value.get('volume_sequential_designation')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'q': utils.reverse_force_list(value.get('name_of_meeting_following_jurisdiction_name_entry_element')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('pronoun_represents_main_entry')),
    }


@marc21.over('series_statement_added_entry_title', '^440.[_1032547698]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    """Series Statement/Added Entry-Title."""
    indicator_map2 = {"0": "No nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    return {
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'volume_sequential_designation': value.get('v'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@tomarc21.over('440', '^series_statement_added_entry_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement_added_entry_title(self, key, value):
    """Reverse - Series Statement/Added Entry-Title."""
    indicator_map2 = {"No nonfiling characters": "0", "Number of nonfiling characters": "8"}
    return {
        'a': utils.reverse_force_list(value.get('title')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'v': utils.reverse_force_list(value.get('volume_sequential_designation')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        'w': utils.reverse_force_list(value.get('bibliographic_record_control_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters')),
    }


@marc21.over('series_statement', '^490[10_].')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    """Series Statement."""
    indicator_map1 = {"0": "Series not traced", "1": "Series traced"}
    return {
        'series_statement': utils.force_list(
            value.get('a')
        ),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'library_of_congress_call_number': value.get('l'),
        'materials_specified': value.get('3'),
        'volume_sequential_designation': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'series_tracing_policy': indicator_map1.get(key[3]),
    }


@tomarc21.over('490', '^series_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_statement(self, key, value):
    """Reverse - Series Statement."""
    indicator_map1 = {"Series not traced": "0", "Series traced": "1"}
    return {
        'a': utils.reverse_force_list(value.get('series_statement')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'l': utils.reverse_force_list(value.get('library_of_congress_call_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'v': utils.reverse_force_list(value.get('volume_sequential_designation')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('series_tracing_policy')),
        '$ind2': '_',
    }
