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
    indicator_map1 = {
        'Forename': '0',
        'Surname': '1',
        'Family name': '3',
    }

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'personal_name': 'a',
        'numeration': 'b',
        'titles_and_other_words_associated_with_a_name': 'c',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'fuller_form_of_name': 'q',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('personal_name'),
        'b': value.get('numeration'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': value.get('miscellaneous_information'),
        'h': value.get('medium'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('610', '^subject_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_corporate_name(self, key, value):
    """Reverse - Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        'Inverted name': '0',
        'Jurisdiction name': '1',
        'Name in direct order': '2',
    }
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'b',
        'location_of_meeting': 'c',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_meeting': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'c': value.get('location_of_meeting'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': value.get('miscellaneous_information'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('611', '^subject_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_meeting_name(self, key, value):
    """Reverse - Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        'Inverted name': '0',
        'Jurisdiction name': '1',
        'Name in direct order': '2',
    }
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'location_of_meeting': 'c',
        'date_of_meeting': 'd',
        'subordinate_unit': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relator_term': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'version': 's',
        'title_of_a_work': 't',
        'affiliation': 'u',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'd': value.get('date_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'f': value.get('date_of_a_work'),
        'g': value.get('miscellaneous_information'),
        'h': value.get('medium'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'u': value.get('affiliation'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('630', '^subject_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_uniform_title(self, key, value):
    """Reverse - Subject Added Entry-Uniform Title."""
    valid_nonfiling_characters = [x for x in range(10)]

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7'
    }

    field_map = {
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': value.get('miscellaneous_information'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('nonfiling_characters') if value.get('nonfiling_characters') in valid_nonfiling_characters else '_',
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('648', '^subject_added_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_chronological_term(self, key, value):
    """Reverse - Subject Added Entry-Chronological Term."""
    indicator_map1 = {
        'No information provided': '_',
        'Date or time period covered or depicted': '0',
        'Date or time period of creation or origin': '1',
    }

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7'
    }

    field_map = {
        'chronological_term': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_date_or_time_period'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('thesaurus'),
            '_'),
    }


@to_marc21.over('650', '^subject_added_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_topical_term(self, key, value):
    """Reverse - Subject Added Entry-Topical Term."""
    indicator_map1 = {
        'No information provided': '_',
        'No level specified': '0',
        'Primary': '1',
        'Secondary': '2',
    }

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'topical_term_or_geographic_name_entry_element': 'a',
        'topical_term_following_geographic_name_entry_element': 'b',
        'location_of_event': 'c',
        'active_dates': 'd',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'c': value.get('location_of_event'),
        'd': value.get('active_dates'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('651', '^subject_added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_geographic_name(self, key, value):
    """Reverse - Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's' literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7'
    }

    field_map = {
        'geographic_name': 'a',
        'relator_term': 'e',
        'miscellaneous_information': 'g',
        'relator_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('653', '^index_term_uncontrolled$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_uncontrolled(self, key, value):
    """Reverse - Index Term-Uncontrolled."""
    indicator_map1 = {
        'No information provided': '_',
        'No level specified': '0',
        'Primary': '1',
        'Secondary': '2',
    }

    indicator_map2 = {
        'No information provided': '_',
        'Topical term': '0',
        'Personal name': '1',
        'Corporate name': '2',
        'Meeting name': '3',
        'Chronological term': '4',
        'Geographic name': '5',
        'Genre/form term': '6',
    }

    field_map = {
        'uncontrolled_term': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

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
        'No information provided': '_',
        'No level specified': '0',
        'Primary': '1',
        'Secondary': '2',
    }

    field_map = {
        'focus_term': 'a',
        'non_focus_term': 'b',
        'facet_hierarchy_designation': 'c',
        'relator_term': 'e',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'materials_specified': '3',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('focus_term')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('655', '^index_term_genre_form$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {
        'Basic': '_',
        'Faceted': '0',
    }

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        "LC subject headings for children's literature": '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
        'Source specified in subfield $2': '7'
    }

    field_map = {
        'genre_form_data_or_focus_term': 'a',
        'non_focus_term': 'b',
        'facet_hierarchy_designation': 'c',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('thesaurus'), '7') != '7':
        try:
            order.remove('2')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('genre_form_data_or_focus_term'),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_term'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_heading'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('656', '^index_term_occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_occupation(self, key, value):
    """Reverse - Index Term-Occupation."""
    field_map = {
        'occupation': 'a',
        'form': 'k',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('occupation'),
        'k': value.get('form'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '7',
    }


@to_marc21.over('657', '^index_term_function$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_function(self, key, value):
    """Reverse - Index Term-Function."""
    field_map = {
        'function': 'a',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('function'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_term'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '7',
    }


@to_marc21.over('658', '^index_term_curriculum_objective$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_curriculum_objective(self, key, value):
    """Reverse - Index Term-Curriculum Objective."""
    field_map = {
        'main_curriculum_objective': 'a',
        'subordinate_curriculum_objective': 'b',
        'curriculum_code': 'c',
        'correlation_factor': 'd',
        'source_of_term_or_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_curriculum_objective'),
        'b': utils.reverse_force_list(
            value.get('subordinate_curriculum_objective')
        ),
        'c': value.get('curriculum_code'),
        'd': value.get('correlation_factor'),
        '2': value.get('source_of_term_or_code'),
        '6': value.get('linkage'),
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
        'country_or_larger_entity': 'a',
        'first_order_political_jurisdiction': 'b',
        'intermediate_political_jurisdiction': 'c',
        'city': 'd',
        'relator_term': 'e',
        'city_subsection': 'f',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'extraterrestrial_area': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'd': value.get('city'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
