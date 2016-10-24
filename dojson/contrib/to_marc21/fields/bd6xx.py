# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('600', '^subject_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_personal_name(self, key, value):
    """Reverse - Subject Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'title_of_a_work': 't',
        'personal_name': 'a',
        'version': 's',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'relator_term': 'e',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'medium_of_performance_for_music': 'm',
        'numeration': 'b',
        'attribution_qualifier': 'j',
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'number_of_part_section_of_a_work': 'n',
        'source_of_heading_or_term': '2',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'fuller_form_of_name': 'q',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'titles_and_other_words_associated_with_a_name': 'c',
        'linkage': '6',
        'date_of_a_work': 'f',
        'key_for_music': 'r',
        'dates_associated_with_a_name': 'd',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_personal_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_personal_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('personal_name'),
        's': value.get('version'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': value.get('numeration'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '2': value.get('source_of_heading_or_term'),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'q': value.get('fuller_form_of_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'r': value.get('key_for_music'),
        'd': value.get('dates_associated_with_a_name'),
        'o': value.get('arranged_statement_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('610', '^subject_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_corporate_name(self, key, value):
    """Reverse - Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'title_of_a_work': 't',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'relator_term': 'e',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'medium_of_performance_for_music': 'm',
        'subordinate_unit': 'b',
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'number_of_part_section_meeting': 'n',
        'source_of_heading_or_term': '2',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
        'linkage': '6',
        'date_of_a_work': 'f',
        'key_for_music': 'r',
        'date_of_meeting_or_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_corporate_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_corporate_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '2': value.get('source_of_heading_or_term'),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'r': value.get('key_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('611', '^subject_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_meeting_name(self, key, value):
    """Reverse - Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'title_of_a_work': 't',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'subordinate_unit': 'e',
        'affiliation': 'u',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'relator_term': 'j',
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'number_of_part_section_meeting': 'n',
        'source_of_heading_or_term': '2',
        'version': 's',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
        'linkage': '6',
        'date_of_a_work': 'f',
        'date_of_meeting': 'd',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_meeting_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_meeting_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'u': value.get('affiliation'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '2': value.get('source_of_heading_or_term'),
        's': value.get('version'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'd': value.get('date_of_meeting'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('630', '^subject_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_uniform_title(self, key, value):
    """Reverse - Subject Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'title_of_a_work': 't',
        'uniform_title': 'a',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'medium_of_performance_for_music': 'm',
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'number_of_part_section_of_a_work': 'n',
        'source_of_heading_or_term': '2',
        'version': 's',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'linkage': '6',
        'date_of_a_work': 'f',
        'key_for_music': 'r',
        'date_of_treaty_signing': 'd',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        't': value.get('title_of_a_work'),
        'a': value.get('uniform_title'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '2': value.get('source_of_heading_or_term'),
        's': value.get('version'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '6': value.get('linkage'),
        'f': value.get('date_of_a_work'),
        'r': value.get('key_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'o': value.get('arranged_statement_for_music'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('648', '^subject_added_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_chronological_term(self, key, value):
    """Reverse - Subject Added Entry-Chronological Term."""
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'chronological_term': 'a',
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'source_of_heading_or_term': '2',
        'linkage': '6',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('650', '^subject_added_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_topical_term(self, key, value):
    """Reverse - Subject Added Entry-Topical Term."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'form_subdivision': 'v',
        'topical_term_or_geographic_name_entry_element': 'a',
        'source_of_heading_or_term': '2',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'location_of_event': 'c',
        'linkage': '6',
        'topical_term_following_geographic_name_entry_element': 'b',
        'active_dates': 'd',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('level_of_subject'), '7') != '7':
        try:
            order.remove(field_map.get('level_of_subject'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        '2': value.get('source_of_heading_or_term'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        'c': value.get('location_of_event'),
        '6': value.get('linkage'),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'd': value.get('active_dates'),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('651', '^subject_added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_geographic_name(self, key, value):
    """Reverse - Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'form_subdivision': 'v',
        'geographic_name': 'a',
        'source_of_heading_or_term': '2',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'miscellaneous_information': 'g',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('geographic_name'),
        '2': value.get('source_of_heading_or_term'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('653', '^index_term_uncontrolled$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_uncontrolled(self, key, value):
    """Reverse - Index Term-Uncontrolled."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    indicator_map2 = {
        "Chronological term": "4",
        "Corporate name": "2",
        "Genre/form term": "6",
        "Geographic name": "5",
        "Meeting name": "3",
        "No information provided": "_",
        "Personal name": "1",
        "Topical term": "0"}
    field_map = {
        'uncontrolled_term': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('level_of_index_term'), '7') != '7':
        try:
            order.remove(field_map.get('level_of_index_term'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_term_or_name'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_term_or_name'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('uncontrolled_term')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_index_term'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_term_or_name'), '_'),
    }


@to_marc21.over('654', '^subject_added_entry_faceted_topical_terms$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_faceted_topical_terms(self, key, value):
    """Reverse - Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    field_map = {
        'chronological_subdivision': 'y',
        'relator_code': '4',
        'form_subdivision': 'v',
        'focus_term': 'a',
        'source_of_heading_or_term': '2',
        'relator_term': 'e',
        'authority_record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
        'materials_specified': '3',
        'facet_hierarchy_designation': 'c',
        'linkage': '6',
        'non_focus_term': 'b',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('level_of_subject'), '7') != '7':
        try:
            order.remove(field_map.get('level_of_subject'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': utils.reverse_force_list(
            value.get('focus_term')
        ),
        '2': value.get('source_of_heading_or_term'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('655', '^index_term_genre_form$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {"Basic": "_", "Faceted": "0"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'genre_form_data_or_focus_term': 'a',
        'source_of_term': '2',
        'geographic_subdivision': 'z',
        'authority_record_control_number': '0',
        'general_subdivision': 'x',
        'materials_specified': '3',
        'facet_hierarchy_designation': 'c',
        'linkage': '6',
        'non_focus_term': 'b',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_heading'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_heading'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove(field_map.get('thesaurus'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '5': value.get('institution_to_which_field_applies'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('genre_form_data_or_focus_term'),
        '2': value.get('source_of_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '3': value.get('materials_specified'),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_heading'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('656', '^index_term_occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_occupation(self, key, value):
    """Reverse - Index Term-Occupation."""
    indicator_map2 = {"Source specified in subfield $2": "7"}
    field_map = {
        'occupation': 'a',
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'form': 'k',
        'authority_record_control_number': '0',
        'geographic_subdivision': 'z',
        'source_of_term': '2',
        'linkage': '6',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_term'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_term'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('occupation'),
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'k': value.get('form'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'source_of_term' in value and
        not indicator_map2.get(value.get('source_of_term')) and
        value.get('source_of_term') == value.get('source_of_term')
        else indicator_map2.get(value.get('source_of_term'), '_'),
    }


@to_marc21.over('657', '^index_term_function$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_function(self, key, value):
    """Reverse - Index Term-Function."""
    indicator_map2 = {"Source specified in subfield $2": "7"}
    field_map = {
        'function': 'a',
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'authority_record_control_number': '0',
        'geographic_subdivision': 'z',
        'source_of_term': '2',
        'linkage': '6',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_term'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_term'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('function'),
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'source_of_term' in value and
        not indicator_map2.get(value.get('source_of_term')) and
        value.get('source_of_term') == value.get('source_of_term')
        else indicator_map2.get(value.get('source_of_term'), '_'),
    }


@to_marc21.over('658', '^index_term_curriculum_objective$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_curriculum_objective(self, key, value):
    """Reverse - Index Term-Curriculum Objective."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'main_curriculum_objective': 'a',
        'curriculum_code': 'c',
        'source_of_term_or_code': '2',
        'linkage': '6',
        'subordinate_curriculum_objective': 'b',
        'correlation_factor': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('main_curriculum_objective'),
        'c': value.get('curriculum_code'),
        '2': value.get('source_of_term_or_code'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('subordinate_curriculum_objective')
        ),
        'd': value.get('correlation_factor'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('662', '^subject_added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'relator_code': '4',
        'country_or_larger_entity': 'a',
        'first_order_political_jurisdiction': 'b',
        'source_of_heading_or_term': '2',
        'extraterrestrial_area': 'h',
        'relator_term': 'e',
        'authority_record_control_number': '0',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'intermediate_political_jurisdiction': 'c',
        'linkage': '6',
        'city_subsection': 'f',
        'city': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        '2': value.get('source_of_heading_or_term'),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        '6': value.get('linkage'),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'd': value.get('city'),
        '$ind1': '_',
        '$ind2': '_',
    }
