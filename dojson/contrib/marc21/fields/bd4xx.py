# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from dojson import utils

from ..model import marc21

@marc21.over('series_statement_added_entry_personal_name', '^400[103][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'personal_name': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'titles_and_other_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_corporate_name', '^410[102][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_meeting_name', '^411[102][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_title', '^440.[0]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': value.get('p'),
        'volume_sequential_designation': value.get('v'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'bibliographic_record_control_number': value.get('w'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement', '^490[10].')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    indicator_map1 = {u'1': u'Series traced', u'0': u'Series not traced'}
    return {
        'series_statement': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'library_of_congress_call_number': value.get('l'),
        'materials_specified': value.get('3'),
        'volume_sequential_designation': value.get('v'),
        'field_link_and_sequence_number': value.get('8'),
        'series_tracing_policy': indicator_map1.get(key[3]),
    }
