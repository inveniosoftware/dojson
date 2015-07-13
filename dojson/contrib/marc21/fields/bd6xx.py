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


@marc21.over('subject_added_entry_personal_name', '^600[103_][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    """Subject Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'personal_name': value.get('a'),
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
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_corporate_name', '^610[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    """Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
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
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_meeting_name', '^611[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    """Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over(
    'subject_added_entry_uniform_title', '^630[_1032547698][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    """Subject Added Entry-Uniform Title."""
    indicator_map1 = {
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
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
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
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_chronological_term', '^648[10_][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    """Subject Added Entry-Chronological Term."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Date or time period covered or depicted",
        "1": "Date or time period of creation or origin"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re",
        "7": "Source specified in subfield $2"}
    return {
        'chronological_term': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_date_or_time_period': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_topical_term', '^650[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    """Subject Added Entry-Topical Term."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'location_of_event': value.get('c'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'active_dates': value.get('d'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_geographic_name', '^651.[_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    """Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'geographic_name': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('index_term_uncontrolled', '^653[10_2][_1032546]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    """Index Term-Uncontrolled."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary"}
    indicator_map2 = {
        "#": "No information provided",
        "0": "Topical term",
        "1": "Personal name",
        "2": "Corporate name",
        "3": "Meeting name",
        "4": "Chronological term",
        "5": "Geographic name",
        "6": "Genre/form term"}
    return {
        'uncontrolled_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'level_of_index_term': indicator_map1.get(key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4]),
    }


@marc21.over('subject_added_entry_faceted_topical_terms', '^654[10_2].')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    """Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "No level specified",
        "1": "Primary",
        "2": "Secondary"}
    return {
        'focus_term': utils.force_list(
            value.get('a')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'level_of_subject': indicator_map1.get(key[3]),
    }


@marc21.over('index_term_genre_form', '^655[0_][_10325476]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    """Index Term-Genre/Form."""
    indicator_map1 = {"#": "Basic", "0": "Faceted"}
    indicator_map2 = {
        "0": "Library of Congress Subject Headings",
        "1": "LC subject headings for children\u0027s literature",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "R\u00e9pertoire de vedettes-mati\u00e8re",
        "7": "Source specified in subfield $2"}
    return {
        'genre_form_data_or_focus_term': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'facet_hierarchy_designation': utils.force_list(
            value.get('c')
        ),
        'non_focus_term': utils.force_list(
            value.get('b')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'type_of_heading': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }


@marc21.over('index_term_occupation', '^656..')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    """Index Term-Occupation."""
    return {
        'occupation': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form': value.get('k'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('index_term_function', '^657..')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    """Index Term-Function."""
    return {
        'function': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('index_term_curriculum_objective', '^658..')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    """Index Term-Curriculum Objective."""
    return {
        'main_curriculum_objective': value.get('a'),
        'curriculum_code': value.get('c'),
        'subordinate_curriculum_objective': utils.force_list(
            value.get('b')
        ),
        'correlation_factor': value.get('d'),
        'source_of_term_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('subject_added_entry_hierarchical_place_name', '^662..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    """Subject Added Entry-Hierarchical Place Name."""
    return {
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }
