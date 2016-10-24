# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_authority


@to_marc21_authority.over(
    '700', '^established_heading_linking_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_personal_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Personal Name."""
    field_map = {
        'personal_name': 'a',
        'numeration': 'b',
        'titles_and_other_words_associated_with_a_name': 'c',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relationship_information': 'i',
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
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Family name': '3', 'Forename': '0', 'Surname': '1'}
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('personal_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'b': value.get('numeration'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '710', '^established_heading_linking_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_corporate_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Corporate Name."""
    field_map = {
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'b',
        'location_of_meeting': 'c',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relationship_information': 'i',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_meeting': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Inverted name': '0',
                      'Jurisdiction name': '1', 'Name in direct order': '2'}
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '711', '^established_heading_linking_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_meeting_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Meeting Name."""
    field_map = {
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'location_of_meeting': 'c',
        'date_of_meeting': 'd',
        'subordinate_unit': 'e',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relationship_information': 'i',
        'relator_term': 'j',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'version': 's',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Inverted name': '0',
                      'Jurisdiction name': '1', 'Name in direct order': '2'}
    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '730', '^established_heading_linking_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_uniform_title(self, key, value):
    """Reverse - Established Heading Linking Entry-Uniform Title."""
    field_map = {
        'uniform_title': 'a',
        'date_of_treaty_signing': 'd',
        'date_of_a_work': 'f',
        'miscellaneous_information': 'g',
        'medium': 'h',
        'relationship_information': 'i',
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
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '748', '^established_heading_linking_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_chronological_term(
        self, key, value):
    """Reverse - Established Heading Linking Entry-Chronological Term."""
    field_map = {
        'chronological_term': 'a',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '750', '^established_heading_linking_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_topical_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Topical Term."""
    field_map = {
        'topical_term_or_geographic_name_entry_element': 'a',
        'topical_term_following_geographic_name_entry_element': 'b',
        'miscellaneous_information': 'g',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '751', '^established_heading_linking_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_geographic_name(
        self, key, value):
    """Reverse - Established Heading Linking Entry-Geographic Name."""
    field_map = {
        'geographic_name': 'a',
        'miscellaneous_information': 'g',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over(
    '755', '^established_heading_linking_entry_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_genre_form_term(
        self, key, value):
    """Reverse - Established Heading Linking Entry-Genre/Form Term."""
    field_map = {
        'genre_form_term_as_entry_element': 'a',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'Library of Congress Subject Headings': '0',
        'LC subject headings for children\'s literature': '1',
        'Medical Subject Headings': '2',
        'National Agricultural Library subject authority file': '3',
        'Source not specified': '4',
        'Canadian Subject Headings': '5',
        'Répertoire de vedettes-matière': '6',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('genre_form_term_as_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if value.get('thesaurus') and value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }
