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


@to_marc21_authority.over('400', '^see_from_tracing_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_personal_name(self, key, value):
    """Reverse - See From Tracing-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'title_of_a_work': 't',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'dates_associated_with_a_name': 'd',
        'miscellaneous_information': 'g',
        'titles_and_other_words_associated_with_a_name': 'c',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'arranged_statement_for_music': 'o',
        'fuller_form_of_name': 'q',
        'geographic_subdivision': 'z',
        'relator_term': 'e',
        'attribution_qualifier': 'j',
        'language_of_a_work': 'l',
        'personal_name': 'a',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'medium': 'h',
        'form_subheading': 'k',
        'version': 's',
        'key_for_music': 'r',
        'medium_of_performance_for_music': 'm',
        'numeration': 'b',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        'q': value.get('fuller_form_of_name'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('personal_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': value.get('numeration'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('410', '^see_from_tracing_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_corporate_name(self, key, value):
    """Reverse - See From Tracing-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'title_of_a_work': 't',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'date_of_meeting_or_treaty_signing': 'd',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'relator_term': 'e',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'geographic_subdivision': 'z',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'medium': 'h',
        'form_subheading': 'k',
        'version': 's',
        'key_for_music': 'r',
        'medium_of_performance_for_music': 'm',
        'subordinate_unit': 'b',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        't': value.get('title_of_a_work'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('411', '^see_from_tracing_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_meeting_name(self, key, value):
    """Reverse - See From Tracing-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'control_subfield': 'w',
        'title_of_a_work': 't',
        'date_of_meeting': 'd',
        'miscellaneous_information': 'g',
        'location_of_meeting': 'c',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'geographic_subdivision': 'z',
        'subordinate_unit': 'e',
        'relator_term': 'j',
        'language_of_a_work': 'l',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'medium': 'h',
        'form_subheading': 'k',
        'version': 's',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        't': value.get('title_of_a_work'),
        'd': value.get('date_of_meeting'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('430', '^see_from_tracing_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_uniform_title(self, key, value):
    """Reverse - See From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'control_subfield': 'w',
        'title_of_a_work': 't',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'uniform_title': 'a',
        'geographic_subdivision': 'z',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'medium': 'h',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'key_for_music': 'r',
        'medium_of_performance_for_music': 'm',
        'general_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'w': value.get('control_subfield'),
        't': value.get('title_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('uniform_title'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'h': value.get('medium'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('448', '^see_from_tracing_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_chronological_term(self, key, value):
    """Reverse - See From Tracing-Chronological Term."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'chronological_term': 'a',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('chronological_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('450', '^see_from_tracing_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_topical_term(self, key, value):
    """Reverse - See From Tracing-Topical Term."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'topical_term_or_geographic_name_entry_element': 'a',
        'miscellaneous_information': 'g',
        'topical_term_following_geographic_name_entry_element': 'b',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('451', '^see_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_geographic_name(self, key, value):
    """Reverse - See From Tracing-Geographic Name."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'geographic_name': 'a',
        'miscellaneous_information': 'g',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('geographic_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('455', '^see_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_genre_form_term(self, key, value):
    """Reverse - See From Tracing-Genre/Form Term."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'genre_form_term': 'a',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('genre_form_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('462', '^see_from_tracing_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_medium_of_performance_term(self, key, value):
    """Reverse - See From Tracing-Medium of Performance Term."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'medium_of_performance_term': 'a',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'a': value.get('medium_of_performance_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': value.get('control_subfield'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('480', '^see_from_tracing_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_general_subdivision(self, key, value):
    """Reverse - See From Tracing-General Subdivision."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('481', '^see_from_tracing_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_geographic_subdivision(self, key, value):
    """Reverse - See From Tracing-Geographic Subdivision."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('482', '^see_from_tracing_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_chronological_subdivision(self, key, value):
    """Reverse - See From Tracing-Chronological Subdivision."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('485', '^see_from_tracing_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_form_subdivision(self, key, value):
    """Reverse - See From Tracing-Form Subdivision."""
    field_map = {
        'linkage': '6',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
