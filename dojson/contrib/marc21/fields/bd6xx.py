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

@marc21.over('subject_added_entry_personal_name', '^600[103][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'attribution_qualifier': value.get('j'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_corporate_name', '^610[102][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_meeting_name', '^611[102][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'relator_term': value.get('j'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_uniform_title', '^630.[10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title': value.get('a'),
        'relator_term': value.get('e'),
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
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_chronological_term', '^648[10.][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    indicator_map1 = {u'1': u'Date or time period of creation or origin', u'0': u'Date or time period covered or depicted', u'#': u'No information provided'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xc3\xa9pertoire de vedettes-mati\xc3\xa8re'}
    return {
        'chronological_term': value.get('a'),
        'general_subdivision': value.get('x'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'type_of_date_or_time_period': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_topical_term', '^650[10.2][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'general_subdivision': value.get('x'),
        'location_of_event': value.get('c'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'relator_term': value.get('e'),
        'active_dates': value.get('d'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'level_of_subject': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_geographic_name', '^651.[10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'geographic_name': value.get('a'),
        'general_subdivision': value.get('x'),
        'relator_term': value.get('e'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('index_term_uncontrolled', '^653[10.2][.1032546]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    indicator_map2 = {u'#': u'No information provided', u'1': u'Personal name', u'0': u'Topical term', u'3': u'Meeting name', u'2': u'Corporate name', u'5': u'Geographic name', u'4': u'Chronological term', u'6': u'Genre/form term'}
    return {
        'uncontrolled_term': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'level_of_index_term': indicator_map1.get(key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_faceted_topical_terms', '^654[10.2].')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    return {
        'focus_term': value.get('a'),
        'facet_hierarchy_designation': value.get('c'),
        'non_focus_term': value.get('b'),
        'relator_term': value.get('e'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'level_of_subject': indicator_map1.get(key[3]),
    }

@marc21.over('index_term_genre_form', '^655[0.][10325476]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    indicator_map1 = {u'0': u'Faceted', u'#': u'Basic'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'genre_form_data_or_focus_term': value.get('a'),
        'general_subdivision': value.get('x'),
        'facet_hierarchy_designation': value.get('c'),
        'non_focus_term': value.get('b'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'type_of_heading': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('index_term_occupation', '^656..')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    return {
        'occupation': value.get('a'),
        'general_subdivision': value.get('x'),
        'form': value.get('k'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
    }

@marc21.over('index_term_function', '^657..')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    return {
        'function': value.get('a'),
        'general_subdivision': value.get('x'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
    }

@marc21.over('index_term_curriculum_objective', '^658..')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    return {
        'main_curriculum_objective': value.get('a'),
        'curriculum_code': value.get('c'),
        'subordinate_curriculum_objective': value.get('b'),
        'correlation_factor': value.get('d'),
        'source_of_term_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('subject_added_entry_hierarchical_place_name', '^662..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    return {
        'country_or_larger_entity': value.get('a'),
        'intermediate_political_jurisdiction': value.get('c'),
        'first_order_political_jurisdiction': value.get('b'),
        'relator_term': value.get('e'),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': value.get('g'),
        'city_subsection': value.get('f'),
        'extraterrestrial_area': value.get('h'),
        'authority_record_control_number': value.get('0'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }
