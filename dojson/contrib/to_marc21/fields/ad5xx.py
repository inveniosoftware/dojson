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


@to_marc21_authority.over('500', '^see_also_from_tracing_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_personal_name(self, key, value):
    """Reverse - See Also From Tracing-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'form_subdivision': 'v',
        'key_for_music': 'r',
        'field_link_and_sequence_number': '8',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'general_subdivision': 'x',
        'fuller_form_of_name': 'q',
        'medium': 'h',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'miscellaneous_information': 'g',
        'control_subfield': 'w',
        'dates_associated_with_a_name': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'numeration': 'b',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'personal_name': 'a',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'version': 's',
        'institution_to_which_field_applies': '5',
        'titles_and_other_words_associated_with_a_name': 'c',
        'linkage': '6',
        'relationship_information': 'i',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'number_of_part_section_of_a_work': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'r': value.get('key_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'q': value.get('fuller_form_of_name'),
        'h': value.get('medium'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': value.get('control_subfield'),
        'd': value.get('dates_associated_with_a_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': value.get('numeration'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('personal_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('510', '^see_also_from_tracing_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_corporate_name(self, key, value):
    """Reverse - See Also From Tracing-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'form_subdivision': 'v',
        'key_for_music': 'r',
        'field_link_and_sequence_number': '8',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'general_subdivision': 'x',
        'medium': 'h',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'miscellaneous_information': 'g',
        'control_subfield': 'w',
        'date_of_meeting_or_treaty_signing': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'subordinate_unit': 'b',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'form_subheading': 'k',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'version': 's',
        'institution_to_which_field_applies': '5',
        'location_of_meeting': 'c',
        'linkage': '6',
        'relationship_information': 'i',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'number_of_part_section_meeting': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'r': value.get('key_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': value.get('control_subfield'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('511', '^see_also_from_tracing_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_meeting_name(self, key, value):
    """Reverse - See Also From Tracing-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'e',
        'general_subdivision': 'x',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'relationship_information': 'i',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'date_of_a_work': 'f',
        'control_subfield': 'w',
        'date_of_meeting': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'medium': 'h',
        'form_subheading': 'k',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_part_section_of_a_work': 'p',
        'version': 's',
        'title_of_a_work': 't',
        'location_of_meeting': 'c',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'relator_term': 'j',
        'number_of_part_section_meeting': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'f': value.get('date_of_a_work'),
        'w': value.get('control_subfield'),
        'd': value.get('date_of_meeting'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('530', '^see_also_from_tracing_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_uniform_title(self, key, value):
    """Reverse - See Also From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
        'general_subdivision': 'x',
        'relationship_information': 'i',
        'medium': 'h',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'miscellaneous_information': 'g',
        'control_subfield': 'w',
        'date_of_treaty_signing': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'form_subheading': 'k',
        'uniform_title': 'a',
        'name_of_part_section_of_a_work': 'p',
        'version': 's',
        'title_of_a_work': 't',
        'medium_of_performance_for_music': 'm',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'number_of_part_section_of_a_work': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': value.get('control_subfield'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('uniform_title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('548', '^see_also_from_tracing_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_chronological_term(self, key, value):
    """Reverse - See Also From Tracing-Chronological Term."""
    field_map = {
        'record_control_number': '0',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'chronological_term': 'a',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('550', '^see_also_from_tracing_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_topical_term(self, key, value):
    """Reverse - See Also From Tracing-Topical Term."""
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'topical_term_or_geographic_name_entry_element': 'a',
        'general_subdivision': 'x',
        'topical_term_following_geographic_name_entry_element': 'b',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'relationship_information': 'i',
        'miscellaneous_information': 'g',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('551', '^see_also_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_name(self, key, value):
    """Reverse - See Also From Tracing-Geographic Name."""
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'geographic_name': 'a',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'relationship_information': 'i',
        'miscellaneous_information': 'g',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('geographic_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('555', '^see_also_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_genre_form_term(self, key, value):
    """Reverse - See Also From Tracing-Genre/Form Term."""
    field_map = {
        'record_control_number': '0',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'genre_form_term': 'a',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('genre_form_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('562', '^see_also_from_tracing_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_medium_of_performance_term(self, key, value):
    """Reverse - See Also From Tracing-Medium of Performance Term."""
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'relationship_information': 'i',
        'medium_of_performance_term': 'a',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'a': value.get('medium_of_performance_term'),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('580', '^see_also_from_tracing_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_general_subdivision(self, key, value):
    """Reverse - See Also From Tracing-General Subdivision."""
    field_map = {
        'record_control_number': '0',
        'linkage': '6',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('581', '^see_also_from_tracing_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Geographic Subdivision."""
    field_map = {
        'record_control_number': '0',
        'linkage': '6',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('582', '^see_also_from_tracing_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_chronological_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Chronological Subdivision."""
    field_map = {
        'record_control_number': '0',
        'linkage': '6',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('585', '^see_also_from_tracing_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_form_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Form Subdivision."""
    field_map = {
        'record_control_number': '0',
        'linkage': '6',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
