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

from ..model import marc21


@marc21.over('added_entry_personal_name', '^700[103_][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    """Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
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
        'miscellaneous_information': value.get('g'),
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
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_corporate_name', '^710[10_2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    """Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
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
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_meeting_name', '^711[10_2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    """Added Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_uncontrolled_name', '^720[1_2].')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    """Added Entry-Uncontrolled Name."""
    indicator_map1 = {"#": "Not specified", "1": "Personal", "2": "Other"}
    return {
        'name': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'type_of_name': indicator_map1.get(key[3]),
    }


@marc21.over('added_entry_uniform_title', '^730[_1032547698][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    """Added Entry-Uniform Title."""
    indicator_map1 = {
        "0": "Number of nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'uniform_title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
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
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'key_for_music': value.get('r'),
        'institution_to_which_field_applies': value.get('5'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'version': value.get('s'),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over(
    'added_entry_uncontrolled_related_analytical_title', '^740[_1032547698][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {
        "0": "No nonfiling characters",
        "1": "Number of nonfiling characters",
        "2": "Number of nonfiling characters",
        "3": "Number of nonfiling characters",
        "4": "Number of nonfiling characters",
        "5": "Number of nonfiling characters",
        "6": "Number of nonfiling characters",
        "7": "Number of nonfiling characters",
        "8": "Number of nonfiling characters",
        "9": "Number of nonfiling characters"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'uncontrolled_related_analytical_title': value.get('a'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    """Added Entry-Geographic Name."""
    return {
        'geographic_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('added_entry_hierarchical_place_name', '^752..')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    """Added Entry-Hierarchical Place Name."""
    return {
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('system_details_access_to_computer_files', '^753..')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    """System Details Access to Computer Files."""
    return {
        'make_and_model_of_machine': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'operating_system': value.get('c'),
        'programming_language': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('added_entry_taxonomic_identification', '^754..')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    """Added Entry-Taxonomic Identification."""
    return {
        'taxonomic_name': utils.force_list(
            value.get('a')
        ),
        'non_public_note': utils.force_list(
            value.get('x')
        ),
        'taxonomic_category': utils.force_list(
            value.get('c')
        ),
        'common_or_alternative_name': utils.force_list(
            value.get('d')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_taxonomic_identification': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
    }
