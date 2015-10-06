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


@marc21.over('main_entry_personal_name', '^100[103_].')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    """Main Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    return {
        'personal_name': value.get('a'),
        'titles_and_words_associated_with_a_name': utils.force_list(
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
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'fuller_form_of_name': value.get('q'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
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
    }


@tomarc21.over('100', '^main_entry_personal_name$')
@utils.filter_values
def reverse_main_entry_personal_name(self, key, value):
    """Reverse - Main Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    return {
        'a': utils.reverse_force_list(value.get('personal_name')),
        'c': utils.reverse_force_list(value.get('titles_and_words_associated_with_a_name')),
        'b': utils.reverse_force_list(value.get('numeration')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('dates_associated_with_a_name')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('attribution_qualifier')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'q': utils.reverse_force_list(value.get('fuller_form_of_name')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element')),
        '$ind2': '_',
    }


@marc21.over('main_entry_corporate_name', '^110[10_2].')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    """Main Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
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
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@tomarc21.over('110', '^main_entry_corporate_name$')
@utils.filter_values
def reverse_main_entry_corporate_name(self, key, value):
    """Reverse - Main Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    return {
        'a': utils.reverse_force_list(value.get('corporate_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'b': utils.reverse_force_list(value.get('subordinate_unit')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('date_of_meeting_or_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number_r')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element')),
        '$ind2': '_',
    }


@marc21.over('main_entry_meeting_name', '^111[10_2].')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    """Main Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
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
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
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
    }


@tomarc21.over('111', '^main_entry_meeting_name$')
@utils.filter_values
def reverse_main_entry_meeting_name(self, key, value):
    """Reverse - Main Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    return {
        'a': utils.reverse_force_list(value.get('meeting_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'e': utils.reverse_force_list(value.get('subordinate_unit')),
        'd': utils.reverse_force_list(value.get('date_of_meeting')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('relator_term')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'q': utils.reverse_force_list(value.get('name_of_meeting_following_jurisdiction_name_entry_element')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element')),
        '$ind2': '_',
    }


@marc21.over('main_entry_uniform_title', '^130[_1032547698].')
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    """Main Entry-Uniform Title."""
    indicator_map1 = {"0": "Number of nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
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
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
    }


@tomarc21.over('130', '^main_entry_uniform_title$')
@utils.filter_values
def reverse_main_entry_uniform_title(self, key, value):
    """Reverse - Main Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
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
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters')),
        '$ind2': '_',
    }
