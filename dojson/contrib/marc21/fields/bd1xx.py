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


@marc21.over('main_entry_personal_name', '^100[103_].')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    indicator_map1 = {
        u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    return {
        'personal_name': value.get('a'),
        'titles_and_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'attribution_qualifier': value.get('j'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_of_a_work': value.get('n'),
        'fuller_form_of_name': value.get('q'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_corporate_name', '^110[102_].')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name',
                      u'0': u'Inverted name', u'2': u'Name in direct order'}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_meeting': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number_r': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_meeting_name', '^111[102_].')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name',
                      u'0': u'Inverted name', u'2': u'Name in direct order'}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'relator_term': value.get('j'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }


@marc21.over('main_entry_uniform_title', '^130..')
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    return {
        'uniform_title': value.get('a'),
        'name_of_part_section_of_a_work': value.get('p'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }
