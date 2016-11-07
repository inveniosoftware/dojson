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

from ..model import to_marc21_authority


@to_marc21_authority.over('700', '^established_heading_linking_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_personal_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
        'geographic_subdivision': 'z',
        'key_for_music': 'r',
        'personal_name': 'a',
        'medium_of_performance_for_music': 'm',
        'title_of_a_work': 't',
        'attribution_qualifier': 'j',
        'chronological_subdivision': 'y',
        'language_of_a_work': 'l',
        'fuller_form_of_name': 'q',
        'relator_term': 'e',
        'titles_and_other_words_associated_with_a_name': 'c',
        'date_of_a_work': 'f',
        'numeration': 'b',
        'dates_associated_with_a_name': 'd',
        'medium': 'h',
        'version': 's',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'number_of_part_section_of_a_work': 'n',
        'source_of_heading_or_term': '2',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'r': value.get('key_for_music'),
        'a': value.get('personal_name'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        't': value.get('title_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'q': value.get('fuller_form_of_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'f': value.get('date_of_a_work'),
        'b': value.get('numeration'),
        'd': value.get('dates_associated_with_a_name'),
        'h': value.get('medium'),
        's': value.get('version'),
        'o': value.get('arranged_statement_for_music'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '2': value.get('source_of_heading_or_term'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('710', '^established_heading_linking_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_corporate_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
        'geographic_subdivision': 'z',
        'key_for_music': 'r',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'medium_of_performance_for_music': 'm',
        'title_of_a_work': 't',
        'chronological_subdivision': 'y',
        'language_of_a_work': 'l',
        'relator_term': 'e',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'subordinate_unit': 'b',
        'date_of_meeting_or_treaty_signing': 'd',
        'medium': 'h',
        'version': 's',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'number_of_part_section_meeting': 'n',
        'source_of_heading_or_term': '2',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'r': value.get('key_for_music'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        't': value.get('title_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'f': value.get('date_of_a_work'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'h': value.get('medium'),
        's': value.get('version'),
        'o': value.get('arranged_statement_for_music'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '2': value.get('source_of_heading_or_term'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('711', '^established_heading_linking_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_meeting_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'geographic_subdivision': 'z',
        'title_of_a_work': 't',
        'relator_term': 'j',
        'chronological_subdivision': 'y',
        'language_of_a_work': 'l',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'subordinate_unit': 'e',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'name_of_part_section_of_a_work': 'p',
        'date_of_meeting': 'd',
        'control_subfield': 'w',
        'version': 's',
        'medium': 'h',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'number_of_part_section_meeting': 'n',
        'source_of_heading_or_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        't': value.get('title_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'f': value.get('date_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'd': value.get('date_of_meeting'),
        'w': value.get('control_subfield'),
        's': value.get('version'),
        'h': value.get('medium'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '2': value.get('source_of_heading_or_term'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('730', '^established_heading_linking_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_uniform_title(self, key, value):
    """Reverse - Established Heading Linking Entry-Uniform Title."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'uniform_title': 'a',
        'linkage': '6',
        'general_subdivision': 'x',
        'form_subheading': 'k',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
        'geographic_subdivision': 'z',
        'key_for_music': 'r',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'title_of_a_work': 't',
        'chronological_subdivision': 'y',
        'language_of_a_work': 'l',
        'date_of_a_work': 'f',
        'name_of_part_section_of_a_work': 'p',
        'date_of_treaty_signing': 'd',
        'medium': 'h',
        'version': 's',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'number_of_part_section_of_a_work': 'n',
        'source_of_heading_or_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('uniform_title'),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'r': value.get('key_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        't': value.get('title_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'f': value.get('date_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'h': value.get('medium'),
        's': value.get('version'),
        'o': value.get('arranged_statement_for_music'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '2': value.get('source_of_heading_or_term'),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('748', '^established_heading_linking_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_chronological_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Chronological Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'linkage': '6',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'chronological_term': 'a',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'source_of_heading_or_term': '2',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('chronological_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('750', '^established_heading_linking_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_topical_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Topical Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'topical_term_or_geographic_name_entry_element': 'a',
        'linkage': '6',
        'form_subdivision': 'v',
        'topical_term_following_geographic_name_entry_element': 'b',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('751', '^established_heading_linking_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_geographic_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Geographic Name."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'geographic_name': 'a',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('geographic_name'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21_authority.over('755', '^established_heading_linking_entry_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_genre_form_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Genre/Form Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'linkage': '6',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'genre_form_term_as_entry_element': 'a',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'source_of_heading_or_term': '2',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('genre_form_term_as_entry_element'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term')
        else indicator_map2.get(value.get('thesaurus'), '_'),
    }
