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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('600', '^subject_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_personal_name(self, key, value):
    """Reverse - Subject Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'general_subdivision': 'x',
        'language_of_a_work': 'l',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'attribution_qualifier': 'j',
        'dates_associated_with_a_name': 'd',
        'numeration': 'b',
        'date_of_a_work': 'f',
        'source_of_heading_or_term': '2',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'version': 's',
        'geographic_subdivision': 'z',
        'materials_specified': '3',
        'personal_name': 'a',
        'key_for_music': 'r',
        'title_of_a_work': 't',
        'number_of_part_section_of_a_work': 'n',
        'chronological_subdivision': 'y',
        'name_of_part_section_of_a_work': 'p',
        'titles_and_other_words_associated_with_a_name': 'c',
        'relator_code': '4',
        'fuller_form_of_name': 'q',
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance_for_music': 'm',
        'field_link_and_sequence_number': '8',
        'medium': 'h',
        'relator_term': 'e',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'b': value.get('numeration'),
        'f': value.get('date_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        's': value.get('version'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('personal_name'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'q': value.get('fuller_form_of_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('610', '^subject_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_corporate_name(self, key, value):
    """Reverse - Subject Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'general_subdivision': 'x',
        'language_of_a_work': 'l',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'date_of_meeting_or_treaty_signing': 'd',
        'subordinate_unit': 'b',
        'date_of_a_work': 'f',
        'source_of_heading_or_term': '2',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'version': 's',
        'geographic_subdivision': 'z',
        'materials_specified': '3',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'key_for_music': 'r',
        'title_of_a_work': 't',
        'number_of_part_section_meeting': 'n',
        'chronological_subdivision': 'y',
        'name_of_part_section_of_a_work': 'p',
        'location_of_meeting': 'c',
        'relator_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance_for_music': 'm',
        'field_link_and_sequence_number': '8',
        'medium': 'h',
        'relator_term': 'e',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'f': value.get('date_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        's': value.get('version'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('611', '^subject_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_meeting_name(self, key, value):
    """Reverse - Subject Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'general_subdivision': 'x',
        'language_of_a_work': 'l',
        'miscellaneous_information': 'g',
        'authority_record_control_number_or_standard_number': '0',
        'relator_term': 'j',
        'date_of_meeting': 'd',
        'date_of_a_work': 'f',
        'source_of_heading_or_term': '2',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'version': 's',
        'geographic_subdivision': 'z',
        'materials_specified': '3',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'title_of_a_work': 't',
        'number_of_part_section_meeting': 'n',
        'chronological_subdivision': 'y',
        'name_of_part_section_of_a_work': 'p',
        'location_of_meeting': 'c',
        'relator_code': '4',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'field_link_and_sequence_number': '8',
        'medium': 'h',
        'subordinate_unit': 'e',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('date_of_meeting'),
        'f': value.get('date_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        's': value.get('version'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('630', '^subject_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_uniform_title(self, key, value):
    """Reverse - Subject Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'general_subdivision': 'x',
        'language_of_a_work': 'l',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'source_of_heading_or_term': '2',
        'geographic_subdivision': 'z',
        'version': 's',
        'materials_specified': '3',
        'uniform_title': 'a',
        'key_for_music': 'r',
        'title_of_a_work': 't',
        'number_of_part_section_of_a_work': 'n',
        'chronological_subdivision': 'y',
        'name_of_part_section_of_a_work': 'p',
        'form_subdivision': 'v',
        'relator_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance_for_music': 'm',
        'field_link_and_sequence_number': '8',
        'medium': 'h',
        'relator_term': 'e',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'f': value.get('date_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        's': value.get('version'),
        '3': value.get('materials_specified'),
        'a': value.get('uniform_title'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': value.get('medium'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('648', '^subject_added_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_chronological_term(self, key, value):
    """Reverse - Subject Added Entry-Chronological Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'chronological_term': 'a',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('650', '^subject_added_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_topical_term(self, key, value):
    """Reverse - Subject Added Entry-Topical Term."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'topical_term_or_geographic_name_entry_element': 'a',
        'general_subdivision': 'x',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'location_of_event': 'c',
        'relator_code': '4',
        'active_dates': 'd',
        'chronological_subdivision': 'y',
        'topical_term_following_geographic_name_entry_element': 'b',
        'source_of_heading_or_term': '2',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level_of_subject', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'c': value.get('location_of_event'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'd': value.get('active_dates'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        '2': value.get('source_of_heading_or_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), value.get('level_of_subject', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('651', '^subject_added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_geographic_name(self, key, value):
    """Reverse - Subject Added Entry-Geographic Name."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'geographic_name': 'a',
        'general_subdivision': 'x',
        'authority_record_control_number_or_standard_number': '0',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'form_subdivision': 'v',
        'relator_code': '4',
        'chronological_subdivision': 'y',
        'source_of_heading_or_term': '2',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': value.get('geographic_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('653', '^index_term_uncontrolled$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_uncontrolled(self, key, value):
    """Reverse - Index Term-Uncontrolled."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Chronological term": "4", "Corporate name": "2", "Genre/form term": "6", "Geographic name": "5", "Meeting name": "3", "No information provided": "_", "Personal name": "1", "Topical term": "0"}
    field_map = {
        'uncontrolled_term': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level_of_index_term', 'type_of_term_or_name'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('uncontrolled_term')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_index_term'), value.get('level_of_index_term', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_term_or_name'), value.get('type_of_term_or_name', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('654', '^subject_added_entry_faceted_topical_terms$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_faceted_topical_terms(self, key, value):
    """Reverse - Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {"No information provided": "_", "No level specified": "0", "Primary": "1", "Secondary": "2"}
    field_map = {
        'materials_specified': '3',
        'focus_term': 'a',
        'authority_record_control_number': '0',
        'linkage': '6',
        'form_subdivision': 'v',
        'relator_code': '4',
        'chronological_subdivision': 'y',
        'non_focus_term': 'b',
        'source_of_heading_or_term': '2',
        'geographic_subdivision': 'z',
        'facet_hierarchy_designation': 'c',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level_of_subject', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('focus_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        '2': value.get('source_of_heading_or_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), value.get('level_of_subject', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('655', '^index_term_genre_form$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {"Basic": "_", "Faceted": "0"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\u00e9pertoire de vedettes-mati\u00e8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'genre_form_data_or_focus_term': 'a',
        'general_subdivision': 'x',
        'authority_record_control_number': '0',
        'linkage': '6',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'non_focus_term': 'b',
        'source_of_term': '2',
        'geographic_subdivision': 'z',
        'facet_hierarchy_designation': 'c',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_heading', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': value.get('genre_form_data_or_focus_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        '2': value.get('source_of_term'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_heading'), value.get('type_of_heading', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('656', '^index_term_occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_occupation(self, key, value):
    """Reverse - Index Term-Occupation."""
    indicator_map2 = {"Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'occupation': 'a',
        'general_subdivision': 'x',
        'source_of_term': '2',
        'authority_record_control_number': '0',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_term'])

    if (indicator_map2.get(value.get('source_of_term'), '7') != '7' or len(value.get('source_of_term', '')) == 1) and\
            field_map.get('source_of_term'):
        order.remove(field_map.get('source_of_term'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('occupation'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'k': value.get('form'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_term' in value and
        not indicator_map2.get(value.get('source_of_term')) and
        value.get('source_of_term') == value.get('source_of_term') and
        field_map.get('source_of_term') in order
        else indicator_map2.get(value.get('source_of_term'), value.get('source_of_term', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('657', '^index_term_function$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_function(self, key, value):
    """Reverse - Index Term-Function."""
    indicator_map2 = {"Source specified in subfield $2": "7"}
    field_map = {
        'materials_specified': '3',
        'chronological_subdivision': 'y',
        'function': 'a',
        'general_subdivision': 'x',
        'source_of_term': '2',
        'authority_record_control_number': '0',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_term'])

    if (indicator_map2.get(value.get('source_of_term'), '7') != '7' or len(value.get('source_of_term', '')) == 1) and\
            field_map.get('source_of_term'):
        order.remove(field_map.get('source_of_term'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('function'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_term' in value and
        not indicator_map2.get(value.get('source_of_term')) and
        value.get('source_of_term') == value.get('source_of_term') and
        field_map.get('source_of_term') in order
        else indicator_map2.get(value.get('source_of_term'), value.get('source_of_term', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('658', '^index_term_curriculum_objective$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_curriculum_objective(self, key, value):
    """Reverse - Index Term-Curriculum Objective."""
    field_map = {
        'linkage': '6',
        'main_curriculum_objective': 'a',
        'subordinate_curriculum_objective': 'b',
        'source_of_term_or_code': '2',
        'field_link_and_sequence_number': '8',
        'correlation_factor': 'd',
        'curriculum_code': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('main_curriculum_objective'),
        'b': utils.reverse_force_list(
            value.get('subordinate_curriculum_objective')
        ),
        '2': value.get('source_of_term_or_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('correlation_factor'),
        'c': value.get('curriculum_code'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('662', '^subject_added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Subject Added Entry-Hierarchical Place Name."""
    field_map = {
        'linkage': '6',
        'country_or_larger_entity': 'a',
        'authority_record_control_number': '0',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'intermediate_political_jurisdiction': 'c',
        'relator_code': '4',
        'city': 'd',
        'first_order_political_jurisdiction': 'b',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'extraterrestrial_area': 'h',
        'relator_term': 'e',
        'city_subsection': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
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
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'd': value.get('city'),
        'b': value.get('first_order_political_jurisdiction'),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
