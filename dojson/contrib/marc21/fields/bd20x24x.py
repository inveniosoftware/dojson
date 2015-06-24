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

@marc21.over('abbreviated_title', '^210[10][0.]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'Other abbreviated title', u'#': u'Abbreviated key title'}
    return {
        'abbreviated_title': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'title_added_entry': indicator_map1.get(key[3]),
        'type': indicator_map2.get(key[4]),
    }

@marc21.over('key_title', '^222.[0]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'key_title': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('uniform_title', '^240[10].')
@utils.filter_values
def uniform_title(self, key, value):
    indicator_map1 = {u'1': u'Printed or displayed', u'0': u'Not printed or displayed'}
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
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
    }

@marc21.over('translation_of_title_by_cataloging_agency', '^242[10][0]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'remainder_of_title': value.get('b'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'linkage': value.get('6'),
        'language_code_of_translated_title': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('collective_uniform_title', '^243[10].')
@utils.filter_values
def collective_uniform_title(self, key, value):
    indicator_map1 = {u'1': u'Printed or displayed', u'0': u'Not printed or displayed'}
    return {
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
    }

@marc21.over('title_statement', '^245[10][0]')
@utils.filter_values
def title_statement(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'statement_of_responsibility': value.get('c'),
        'remainder_of_title': value.get('b'),
        'bulk_dates': value.get('g'),
        'inclusive_dates': value.get('f'),
        'medium': value.get('h'),
        'form': value.get('k'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('varying_form_of_title', '^246[1032][.103254768]')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    indicator_map1 = {u'1': u'Note, added entry', u'0': u'Note, no added entry', u'3': u'No note, added entry', u'2': u'No note, no added entry'}
    indicator_map2 = {u'#': u'No type specified', u'1': u'Parallel title', u'0': u'Portion of title', u'3': u'Other title', u'2': u'Distinctive title', u'5': u'Added title page title', u'4': u'Cover title', u'7': u'Running title', u'6': u'Caption title', u'8': u'Spine title'}
    return {
        'title_proper_short_title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'display_text': value.get('i'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'note_added_entry_controller': indicator_map1.get(key[3]),
        'type_of_title': indicator_map2.get(key[4]),
    }

@marc21.over('former_title', '^247[10][10]')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'1': u'Do not display note', u'0': u'Display note'}
    return {
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'note_controller': indicator_map2.get(key[4]),
    }
