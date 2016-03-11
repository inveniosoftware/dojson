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

from ..model import marc21_authority


@marc21_authority.over('see_from_tracing_personal_name', '^400[103_].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_personal_name(self, key, value):
    """See From Tracing-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    return {
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
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
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'title_of_a_work': value.get('t'),
        'control_subfield': value.get('w'),
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
        'type_of_personal_name_element': indicator_map1.get(key[3]),
    }


@marc21_authority.over('see_from_tracing_corporate_name', '^410[10_2].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_corporate_name(self, key, value):
    """See From Tracing-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    return {
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'title_of_a_work': value.get('t'),
        'control_subfield': value.get('w'),
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
    }


@marc21_authority.over('see_from_tracing_meeting_name', '^411[10_2].')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_meeting_name(self, key, value):
    """See From Tracing-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    return {
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')),
        'relationship_code': utils.force_list(
            value.get('4')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': utils.force_list(
            value.get('c')),
        'subordinate_unit': utils.force_list(
            value.get('e')),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')),
        'relator_term': utils.force_list(
            value.get('j')),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')),
        'chronological_subdivision': utils.force_list(
            value.get('y')),
        'general_subdivision': utils.force_list(
            value.get('x')),
        'geographic_subdivision': utils.force_list(
            value.get('z')),
        'type_of_meeting_name_entry_element': indicator_map1.get(
            key[3]),
    }


@marc21_authority.over('see_from_tracing_uniform_title', '^430.[_1032547698]')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_uniform_title(self, key, value):
    """See From Tracing-Uniform Title."""
    indicator_map2 = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"}
    return {
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
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
        'control_subfield': value.get('w'),
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
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('see_from_tracing_chronological_term', '^448..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_term(self, key, value):
    """See From Tracing-Chronological Term."""
    return {
        'chronological_term': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
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


@marc21_authority.over('see_from_tracing_topical_term', '^450..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_topical_term(self, key, value):
    """See From Tracing-Topical Term."""
    return {
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
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


@marc21_authority.over('see_from_tracing_geographic_name', '^451..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_name(self, key, value):
    """See From Tracing-Geographic Name."""
    return {
        'geographic_name': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
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


@marc21_authority.over('see_from_tracing_genre_form_term', '^455..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_genre_form_term(self, key, value):
    """See From Tracing-Genre/Form Term."""
    return {
        'genre_form_term': value.get('a'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
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


@marc21_authority.over('see_from_tracing_medium_of_performance_term', '^462..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_medium_of_performance_term(self, key, value):
    """See From Tracing-Medium of Performance Term."""
    return {
        'medium_of_performance_term': value.get('a'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('see_from_tracing_general_subdivision', '^480..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_general_subdivision(self, key, value):
    """See From Tracing-General Subdivision."""
    return {
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
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


@marc21_authority.over('see_from_tracing_geographic_subdivision', '^481..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_geographic_subdivision(self, key, value):
    """See From Tracing-Geographic Subdivision."""
    return {
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
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


@marc21_authority.over('see_from_tracing_chronological_subdivision', '^482..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_chronological_subdivision(self, key, value):
    """See From Tracing-Chronological Subdivision."""
    return {
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
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


@marc21_authority.over('see_from_tracing_form_subdivision', '^485..')
@utils.for_each_value
@utils.filter_values
def see_from_tracing_form_subdivision(self, key, value):
    """See From Tracing-Form Subdivision."""
    return {
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'control_subfield': value.get('w'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
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
