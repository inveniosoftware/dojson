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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

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
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
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
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
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
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'd': value.get('date_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
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
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'f': value.get('date_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'h': value.get('medium'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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
        'r': value.get('key_for_music'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'chronological_term': 'a',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('topical_term_or_geographic_name_entry_element'),
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
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('551', '^see_also_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_name(self, key, value):
    """Reverse - See Also From Tracing-Geographic Name."""
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
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('555', '^see_also_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_genre_form_term(self, key, value):
    """Reverse - See Also From Tracing-Genre/Form Term."""
    field_map = {
        'genre_form_term': 'a',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('genre_form_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'medium_of_performance_term': 'a',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'authority_record_control_number_or_standard_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('medium_of_performance_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('580', '^see_also_from_tracing_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_general_subdivision(self, key, value):
    """Reverse - See Also From Tracing-General Subdivision."""
    field_map = {
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'record_control_number': '0',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'w': value.get('control_subfield'),
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
            value.get('record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
