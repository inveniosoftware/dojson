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
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'title_of_a_work': 't',
        'source_of_heading_or_term': '2',
        'number_of_part_section_of_a_work': 'n',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'attribution_qualifier': 'j',
        'chronological_subdivision': 'y',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'fuller_form_of_name': 'q',
        'titles_and_other_words_associated_with_a_name': 'c',
        'miscellaneous_information': 'g',
        'affiliation': 'u',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'materials_specified': '3',
        'numeration': 'b',
        'arranged_statement_for_music': 'o',
        'personal_name': 'a',
        'version': 's',
        'form_subdivision': 'v',
        'language_of_a_work': 'l',
        'date_of_a_work': 'f',
        'linkage': '6',
        'dates_associated_with_a_name': 'd',
        'general_subdivision': 'x',
        'relator_code': '4',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'q': value.get('fuller_form_of_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'u': value.get('affiliation'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '3': value.get('materials_specified'),
        'b': value.get('numeration'),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('personal_name'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'f': value.get('date_of_a_work'),
        '6': value.get('linkage'),
        'd': value.get('dates_associated_with_a_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'h': value.get('medium'),
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
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'title_of_a_work': 't',
        'source_of_heading_or_term': '2',
        'number_of_part_section_meeting': 'n',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'chronological_subdivision': 'y',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'affiliation': 'u',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'materials_specified': '3',
        'subordinate_unit': 'b',
        'arranged_statement_for_music': 'o',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'form_subdivision': 'v',
        'language_of_a_work': 'l',
        'date_of_a_work': 'f',
        'linkage': '6',
        'date_of_meeting_or_treaty_signing': 'd',
        'general_subdivision': 'x',
        'relator_code': '4',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'u': value.get('affiliation'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'f': value.get('date_of_a_work'),
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'h': value.get('medium'),
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
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'date_of_a_work': 'f',
        'source_of_heading_or_term': '2',
        'number_of_part_section_meeting': 'n',
        'date_of_meeting': 'd',
        'relator_term': 'j',
        'subordinate_unit': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'affiliation': 'u',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'form_subdivision': 'v',
        'language_of_a_work': 'l',
        'relator_code': '4',
        'linkage': '6',
        'title_of_a_work': 't',
        'materials_specified': '3',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'f': value.get('date_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'd': value.get('date_of_meeting'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'u': value.get('affiliation'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        '3': value.get('materials_specified'),
        'h': value.get('medium'),
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
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'date_of_treaty_signing': 'd',
        'source_of_heading_or_term': '2',
        'number_of_part_section_of_a_work': 'n',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'chronological_subdivision': 'y',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'general_subdivision': 'x',
        'arranged_statement_for_music': 'o',
        'uniform_title': 'a',
        'version': 's',
        'form_subdivision': 'v',
        'language_of_a_work': 'l',
        'relator_code': '4',
        'linkage': '6',
        'title_of_a_work': 't',
        'date_of_a_work': 'f',
        'materials_specified': '3',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '2': value.get('source_of_heading_or_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('uniform_title'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        'f': value.get('date_of_a_work'),
        '3': value.get('materials_specified'),
        'h': value.get('medium'),
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
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'chronological_term': 'a',
        'geographic_subdivision': 'z',
        'source_of_heading_or_term': '2',
        'linkage': '6',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('chronological_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
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
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'general_subdivision': 'x',
        'topical_term_following_geographic_name_entry_element': 'b',
        'chronological_subdivision': 'y',
        'topical_term_or_geographic_name_entry_element': 'a',
        'geographic_subdivision': 'z',
        'source_of_heading_or_term': '2',
        'form_subdivision': 'v',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'location_of_event': 'c',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'linkage': '6',
        'active_dates': 'd',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'c': value.get('location_of_event'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        'd': value.get('active_dates'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
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
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'chronological_subdivision': 'y',
        'geographic_name': 'a',
        'geographic_subdivision': 'z',
        'source_of_heading_or_term': '2',
        'form_subdivision': 'v',
        'relator_term': 'e',
        'general_subdivision': 'x',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('geographic_name'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
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
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Chronological term": "4", "Corporate name": "2", "Genre/form term": "6", "Geographic name": "5", "Meeting name": "3", "No information provided": "_", "Personal name": "1", "Topical term": "0"}
    field_map = {
        'uncontrolled_term': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('uncontrolled_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('level_of_index_term'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_term_or_name'), '_'),
    }


@to_marc21.over('654', '^subject_added_entry_faceted_topical_terms$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_faceted_topical_terms(self, key, value):
    """Reverse - Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    field_map = {
        'non_focus_term': 'b',
        'chronological_subdivision': 'y',
        'focus_term': 'a',
        'geographic_subdivision': 'z',
        'source_of_heading_or_term': '2',
        'form_subdivision': 'v',
        'relator_term': 'e',
        'authority_record_control_number': '0',
        'facet_hierarchy_designation': 'c',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': utils.reverse_force_list(
            value.get('focus_term')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('655', '^index_term_genre_form$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {"Basic": "_", "Faceted": "0"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number': '0',
        'non_focus_term': 'b',
        'chronological_subdivision': 'y',
        'genre_form_data_or_focus_term': 'a',
        'geographic_subdivision': 'z',
        'source_of_term': '2',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'facet_hierarchy_designation': 'c',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('genre_form_data_or_focus_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_term'),
        '5': value.get('institution_to_which_field_applies'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
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
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'occupation': 'a',
        'geographic_subdivision': 'z',
        'source_of_term': '2',
        'linkage': '6',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'form': 'k',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('occupation'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'k': value.get('form'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
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
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'function': 'a',
        'geographic_subdivision': 'z',
        'source_of_term': '2',
        'linkage': '6',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('function'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
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
        'subordinate_curriculum_objective': 'b',
        'main_curriculum_objective': 'a',
        'curriculum_code': 'c',
        'source_of_term_or_code': '2',
        'linkage': '6',
        'correlation_factor': 'd',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('subordinate_curriculum_objective')
        ),
        'a': value.get('main_curriculum_objective'),
        'c': value.get('curriculum_code'),
        '2': value.get('source_of_term_or_code'),
        '6': value.get('linkage'),
        'd': value.get('correlation_factor'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('662', '^subject_added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        'authority_record_control_number': '0',
        'first_order_political_jurisdiction': 'b',
        'country_or_larger_entity': 'a',
        'source_of_heading_or_term': '2',
        'relator_term': 'e',
        'relator_code': '4',
        'intermediate_political_jurisdiction': 'c',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'linkage': '6',
        'city': 'd',
        'field_link_and_sequence_number': '8',
        'city_subsection': 'f',
        'extraterrestrial_area': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        '2': value.get('source_of_heading_or_term'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        '6': value.get('linkage'),
        'd': value.get('city'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
