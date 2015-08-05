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


@marc21.over('subject_added_entry_personal_name', '^600[103_][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    """Subject Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('600', 'subject_added_entry_personal_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_personal_name(self, key, value):
    """Reverse - Subject Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('personal_name')),
        'c': utils.reverse_force_list(value.get('titles_and_other_words_associated_with_a_name')),
        'b': utils.reverse_force_list(value.get('numeration')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('dates_associated_with_a_name')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('attribution_qualifier')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'q': utils.reverse_force_list(value.get('fuller_form_of_name')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_corporate_name', '^610[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    """Subject Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('610', 'subject_added_entry_corporate_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_corporate_name(self, key, value):
    """Reverse - Subject Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('corporate_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'b': utils.reverse_force_list(value.get('subordinate_unit')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('date_of_meeting_or_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_meeting_name', '^611[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    """Subject Added Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('611', 'subject_added_entry_meeting_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_meeting_name(self, key, value):
    """Reverse - Subject Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('meeting_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'e': utils.reverse_force_list(value.get('subordinate_unit')),
        'd': utils.reverse_force_list(value.get('date_of_meeting')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('relator_term')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'q': utils.reverse_force_list(value.get('name_of_meeting_following_jurisdiction_name_entry_element')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_uniform_title', '^630[_1032547698][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    """Subject Added Entry-Uniform Title."""
    indicator_map1 = {"0": "Number of nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('630', 'subject_added_entry_uniform_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_uniform_title(self, key, value):
    """Reverse - Subject Added Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('uniform_title')),
        'e': utils.reverse_force_list(value.get('relator_term')),
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
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_chronological_term', '^648[10_][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    """Subject Added Entry-Chronological Term."""
    indicator_map1 = {"#": "No information provided", "0": "Date or time period covered or depicted", "1": "Date or time period of creation or origin"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('648', 'subject_added_entry_chronological_term')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_chronological_term(self, key, value):
    """Reverse - Subject Added Entry-Chronological Term."""
    indicator_map1 = {"Date or time period covered or depicted": "0", "Date or time period of creation or origin": "1", "No information provided": "_"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('chronological_term')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('type_of_date_or_time_period')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_topical_term', '^650[10_2][_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    """Subject Added Entry-Topical Term."""
    indicator_map1 = {"#": "No information provided", "0": "No level specified", "1": "Primary", "2": "Secondary"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('650', 'subject_added_entry_topical_term')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_topical_term(self, key, value):
    """Reverse - Subject Added Entry-Topical Term."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('topical_term_or_geographic_name_entry_element')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'c': utils.reverse_force_list(value.get('location_of_event')),
        'b': utils.reverse_force_list(value.get('topical_term_following_geographic_name_entry_element')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('active_dates')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('level_of_subject')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('subject_added_entry_geographic_name', '^651.[_10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    """Subject Added Entry-Geographic Name."""
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('651', 'subject_added_entry_geographic_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_geographic_name(self, key, value):
    """Reverse - Subject Added Entry-Geographic Name."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('geographic_name')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('thesaurus')),
    }


@marc21.over('index_term_uncontrolled', '^653[10_2][_1032546]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    """Index Term-Uncontrolled."""
    indicator_map1 = {"#": "No information provided", "0": "No level specified", "1": "Primary", "2": "Secondary"}
    indicator_map2 = {"#": "No information provided", "0": "Topical term", "1": "Personal name", "2": "Corporate name", "3": "Meeting name", "4": "Chronological term", "5": "Geographic name", "6": "Genre/form term"}
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


@tomarc21.over('653', 'index_term_uncontrolled')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_uncontrolled(self, key, value):
    """Reverse - Index Term-Uncontrolled."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Chronological term": "4", "Corporate name": "2", "Genre/form term": "6", "Geographic name": "5", "Meeting name": "3", "No information provided": "_", "Personal name": "1", "Topical term": "0"}
    return {
        'a': utils.reverse_force_list(value.get('uncontrolled_term')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('level_of_index_term')),
        '$ind2': indicator_map2.get(value.get('type_of_term_or_name')),
    }


@marc21.over('subject_added_entry_faceted_topical_terms', '^654[10_2].')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    """Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {"#": "No information provided", "0": "No level specified", "1": "Primary", "2": "Secondary"}
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


@tomarc21.over('654', 'subject_added_entry_faceted_topical_terms')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_faceted_topical_terms(self, key, value):
    """Reverse - Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    return {
        'a': utils.reverse_force_list(value.get('focus_term')),
        'c': utils.reverse_force_list(value.get('facet_hierarchy_designation')),
        'b': utils.reverse_force_list(value.get('non_focus_term')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('level_of_subject')),
        '$ind2': '_',
    }


@marc21.over('index_term_genre_form', '^655[0_][_10325476]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    """Index Term-Genre/Form."""
    indicator_map1 = {"#": "Basic", "0": "Faceted"}
    indicator_map2 = {"0": "Library of Congress Subject Headings", "1": "LC subject headings for children\u0027s literature", "2": "Medical Subject Headings", "3": "National Agricultural Library subject authority file", "4": "Source not specified", "5": "Canadian Subject Headings", "6": "R\u00e9pertoire de vedettes-mati\u00e8re", "7": "Source specified in subfield $2"}
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


@tomarc21.over('655', 'index_term_genre_form')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {"Basic": "_", "Faceted": "0"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('genre_form_data_or_focus_term')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'c': utils.reverse_force_list(value.get('facet_hierarchy_designation')),
        'b': utils.reverse_force_list(value.get('non_focus_term')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(value.get('type_of_heading')),
        '$ind2': indicator_map2.get(value.get('thesaurus')),
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


@tomarc21.over('656', 'index_term_occupation')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_occupation(self, key, value):
    """Reverse - Index Term-Occupation."""
    return {
        'a': utils.reverse_force_list(value.get('occupation')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'k': utils.reverse_force_list(value.get('form')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': '_',
        '$ind2': '_',
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


@tomarc21.over('657', 'index_term_function')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_function(self, key, value):
    """Reverse - Index Term-Function."""
    return {
        'a': utils.reverse_force_list(value.get('function')),
        'x': utils.reverse_force_list(value.get('general_subdivision')),
        'v': utils.reverse_force_list(value.get('form_subdivision')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('geographic_subdivision')),
        '$ind1': '_',
        '$ind2': '_',
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


@tomarc21.over('658', 'index_term_curriculum_objective')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_curriculum_objective(self, key, value):
    """Reverse - Index Term-Curriculum Objective."""
    return {
        'a': utils.reverse_force_list(value.get('main_curriculum_objective')),
        'c': utils.reverse_force_list(value.get('curriculum_code')),
        'b': utils.reverse_force_list(value.get('subordinate_curriculum_objective')),
        'd': utils.reverse_force_list(value.get('correlation_factor')),
        '2': utils.reverse_force_list(value.get('source_of_term_or_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
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


@tomarc21.over('662', 'subject_added_entry_hierarchical_place_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Subject Added Entry-Hierarchical Place Name."""
    return {
        'a': utils.reverse_force_list(value.get('country_or_larger_entity')),
        'c': utils.reverse_force_list(value.get('intermediate_political_jurisdiction')),
        'b': utils.reverse_force_list(value.get('first_order_political_jurisdiction')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('city')),
        'g': utils.reverse_force_list(value.get('other_nonjurisdictional_geographic_region_and_feature')),
        'f': utils.reverse_force_list(value.get('city_subsection')),
        'h': utils.reverse_force_list(value.get('extraterrestrial_area')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }
