# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21


@marc21.over('added_entry_personal_name', '^700[_130][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    """Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        't': 'title_of_a_work',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        '3': 'materials_specified',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'h': 'medium',
        'k': 'form_subheading',
        'b': 'numeration',
        '6': 'linkage',
        'd': 'dates_associated_with_a_name',
        'a': 'personal_name',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'fuller_form_of_name',
        's': 'version',
        'p': 'name_of_part_section_of_a_work',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'r': 'key_for_music',
        'u': 'affiliation',
        'o': 'arranged_statement_for_music',
        'j': 'attribution_qualifier',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')

    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title_of_a_work': value.get('t'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'materials_specified': value.get('3'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'numeration': value.get('b'),
        'linkage': value.get('6'),
        'dates_associated_with_a_name': value.get('d'),
        'personal_name': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'fuller_form_of_name': value.get('q'),
        'version': value.get('s'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'arranged_statement_for_music': value.get('o'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_corporate_name', '^710[_120][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    """Added Entry-Corporate Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        't': 'title_of_a_work',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        '3': 'materials_specified',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'h': 'medium',
        'k': 'form_subheading',
        'b': 'subordinate_unit',
        '6': 'linkage',
        'd': 'date_of_meeting_or_treaty_signing',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'version',
        'p': 'name_of_part_section_of_a_work',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'r': 'key_for_music',
        'u': 'affiliation',
        'o': 'arranged_statement_for_music',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_meeting',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')

    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title_of_a_work': value.get('t'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'materials_specified': value.get('3'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'version': value.get('s'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'arranged_statement_for_music': value.get('o'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_meeting_name', '^711[_120][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    """Added Entry-Meeting Name."""
    indicator_map1 = {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        't': 'title_of_a_work',
        'g': 'miscellaneous_information',
        'i': 'relationship_information',
        '3': 'materials_specified',
        'x': 'international_standard_serial_number',
        '4': 'relator_code',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'h': 'medium',
        'k': 'form_subheading',
        '6': 'linkage',
        'd': 'date_of_meeting',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        's': 'version',
        'p': 'name_of_part_section_of_a_work',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'u': 'affiliation',
        'j': 'relator_term',
        'n': 'number_of_part_section_meeting',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')

    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title_of_a_work': value.get('t'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'materials_specified': value.get('3'),
        'international_standard_serial_number': value.get('x'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'date_of_meeting': value.get('d'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'version': value.get('s'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'affiliation': value.get('u'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_uncontrolled_name', '^720[_12].')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    """Added Entry-Uncontrolled Name."""
    indicator_map1 = {"1": "Personal", "2": "Other", "_": "Not specified"}
    field_map = {
        'e': 'relator_term',
        'a': 'name',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_name')

    return {
        '__order__': tuple(order) if len(order) else None,
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'name': value.get('a'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_name': indicator_map1.get(key[3]),
    }


@marc21.over('added_entry_uniform_title', '^730[5830_249176][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    """Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        't': 'title_of_a_work',
        'a': 'uniform_title',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'g': 'miscellaneous_information',
        'x': 'international_standard_serial_number',
        's': 'version',
        'p': 'name_of_part_section_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        'f': 'date_of_a_work',
        'h': 'medium',
        'i': 'relationship_information',
        'k': 'form_subheading',
        'o': 'arranged_statement_for_music',
        'l': 'language_of_a_work',
        '6': 'linkage',
        'd': 'date_of_treaty_signing',
        'n': 'number_of_part_section_of_a_work',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('nonfiling_characters')

    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title_of_a_work': value.get('t'),
        'uniform_title': value.get('a'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'international_standard_serial_number': value.get('x'),
        'version': value.get('s'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'arranged_statement_for_music': value.get('o'),
        'language_of_a_work': value.get('l'),
        'linkage': value.get('6'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_uncontrolled_related_analytical_title',
             '^740[5830_249176][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        'a': 'uncontrolled_related_analytical_title',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        'p': 'name_of_part_section_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('nonfiling_characters')

    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uncontrolled_related_analytical_title': value.get('a'),
        'medium': value.get('h'),
        'institution_to_which_field_applies': value.get('5'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    """Added Entry-Geographic Name."""
    field_map = {
        'e': 'relator_term',
        'a': 'geographic_name',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '0': 'authority_record_control_number',
        '2': 'source_of_heading_or_term',
        '4': 'relator_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'geographic_name': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('added_entry_hierarchical_place_name', '^752..')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    """Added Entry-Hierarchical Place Name."""
    field_map = {
        'a': 'country_or_larger_entity',
        'h': 'extraterrestrial_area',
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        'f': 'city_subsection',
        'b': 'first_order_political_jurisdiction',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        'c': 'intermediate_political_jurisdiction',
        'd': 'city',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'city': value.get('d'),
    }


@marc21.over('system_details_access_to_computer_files', '^753..')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    """System Details Access to Computer Files."""
    field_map = {
        'a': 'make_and_model_of_machine',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'b': 'programming_language',
        '2': 'source_of_term',
        '6': 'linkage',
        'c': 'operating_system',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'make_and_model_of_machine': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'programming_language': value.get('b'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'operating_system': value.get('c'),
    }


@marc21.over('added_entry_taxonomic_identification', '^754..')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    """Added Entry-Taxonomic Identification."""
    field_map = {
        'z': 'public_note',
        'a': 'taxonomic_name',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        '2': 'source_of_taxonomic_identification',
        'x': 'non_public_note',
        '6': 'linkage',
        'c': 'taxonomic_category',
        'd': 'common_or_alternative_name',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'public_note': utils.force_list(
            value.get('z')
        ),
        'taxonomic_name': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_taxonomic_identification': value.get('2'),
        'non_public_note': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'taxonomic_category': utils.force_list(
            value.get('c')
        ),
        'common_or_alternative_name': utils.force_list(
            value.get('d')
        ),
    }
