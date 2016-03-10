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


@marc21.over('added_entry_personal_name', '^700[_013][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    """Added Entry-Personal Name."""
    indicator_map1 = {
        '0': 'Forename',
        '1': 'Surname',
        '3': 'Family name',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '2': 'Analytical entry',
    }

    field_map = {
        'a': 'personal_name',
        'b': 'numeration',
        'c': 'titles_and_other_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
        'j': 'attribution_qualifier',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'q': 'fuller_form_of_name',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_personal_name_entry_element')
    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'personal_name': value.get('a'),
        'numeration': value.get('b'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'fuller_form_of_name': value.get('q'),
        'arranged_statement_for_music': value.get('o'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_corporate_name', '^710[_0-2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    """Added Entry-Corporate Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '2': 'Analytical entry',
    }

    field_map = {
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'b': 'subordinate_unit',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting_or_treaty_signing',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_meeting',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_corporate_name_entry_element')
    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'subordinate_unit': utils.force_list(value.get('b')),
        'location_of_meeting': value.get('c'),
        'date_of_meeting_or_treaty_signing': utils.force_list(value.get('d')),
        'relator_term': utils.force_list(value.get('e')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(value.get('m')),
        'number_of_part_section_meeting': utils.force_list(value.get('n')),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_meeting_name', '^711[_0-2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    """Added Entry-Meeting Name."""
    indicator_map1 = {
        '0': 'Inverted name',
        '1': 'Jurisdiction name',
        '2': 'Name in direct order',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '2': 'Analytical entry',
    }

    field_map = {
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
        'j': 'relator_term',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_meeting',
        'p': 'name_of_part_section_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        's': 'version',
        't': 'title_of_a_work',
        'u': 'affiliation',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_meeting_name_entry_element')
    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'date_of_meeting': value.get('d'),
        'subordinate_unit': utils.force_list(value.get('e')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'relator_term': utils.force_list(value.get('j')),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(value.get('n')),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'affiliation': value.get('u'),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_uncontrolled_name', '^720[_12]_')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    """Added Entry-Uncontrolled Name."""
    indicator_map1 = {
        '_': 'Not specified',
        '1': 'Personal',
        '2': 'Other',
    }

    field_map = {
        'a': 'name',
        'e': 'relator_term',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_name')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name': value.get('a'),
        'relator_term': utils.force_list(value.get('e')),
        'relator_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_name': indicator_map1.get(key[3]),
    }


@marc21.over('added_entry_uniform_title', '^730[_0-9][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    """Added Entry-Uniform Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map2 = {
        '_': 'No information provided',
        '2': 'Analytical entry',
    }

    field_map = {
        'a': 'uniform_title',
        'd': 'date_of_treaty_signing',
        'f': 'date_of_a_work',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'i': 'relationship_information',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'm': 'medium_of_performance_for_music',
        'n': 'number_of_part_section_of_a_work',
        'o': 'arranged_statement_for_music',
        'p': 'name_of_part_section_of_a_work',
        'r': 'key_for_music',
        's': 'version',
        't': 'title_of_a_work',
        'x': 'international_standard_serial_number',
        '0': 'authority_record_control_number_or_standard_number',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in valid_nonfiling_characters:
        order.append('nonfiling_characters')
    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': utils.force_list(value.get('d')),
        'date_of_a_work': value.get('f'),
        'miscellaneous_information': value.get('g'),
        'medium': value.get('h'),
        'relationship_information': utils.force_list(value.get('i')),
        'form_subheading': utils.force_list(value.get('k')),
        'language_of_a_work': value.get('l'),
        'medium_of_performance_for_music': utils.force_list(value.get('m')),
        'number_of_part_section_of_a_work': utils.force_list(value.get('n')),
        'arranged_statement_for_music': value.get('o'),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'nonfiling_characters': utils.int_with_default(key[3], None),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over(
    'added_entry_uncontrolled_related_analytical_title',
    '^740[_0-9][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Added Entry-Uncontrolled Related/Analytical Title."""
    valid_nonfiling_characters = [str(x) for x in range(10)]

    indicator_map2 = {
        '_': 'No information provided',
        '2': 'Analytical entry',
    }

    field_map = {
        'a': 'uncontrolled_related_analytical_title',
        'h': 'medium',
        'n': 'number_of_part_section_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in valid_nonfiling_characters:
        order.append('nonfiling_characters')
    if key[4] in indicator_map2:
        order.append('type_of_added_entry')

    return {
        '__order__': tuple(order) if len(order) else None,
        'uncontrolled_related_analytical_title': value.get('a'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(value.get('n')),
        'name_of_part_section_of_a_work': utils.force_list(value.get('p')),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': utils.int_with_default(key[3], None),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@marc21.over('added_entry_geographic_name', '^751__')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    """Added Entry-Geographic Name."""
    field_map = {
        'a': 'geographic_name',
        'e': 'relator_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_name': value.get('a'),
        'relator_term': utils.force_list(value.get('e')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'relator_code': utils.force_list(value.get('4')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('added_entry_hierarchical_place_name', '^752__')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    """Added Entry-Hierarchical Place Name."""
    field_map = {
        'a': 'country_or_larger_entity',
        'b': 'first_order_political_jurisdiction',
        'c': 'intermediate_political_jurisdiction',
        'd': 'city',
        'f': 'city_subsection',
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
        'h': 'extraterrestrial_area',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_heading_or_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'country_or_larger_entity': utils.force_list(value.get('a')),
        'first_order_political_jurisdiction': value.get('b'),
        'intermediate_political_jurisdiction': utils.force_list(value.get('c')),
        'city': value.get('d'),
        'city_subsection': utils.force_list(value.get('f')),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'extraterrestrial_area': utils.force_list(value.get('h')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('system_details_access_to_computer_files', '^753__')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    """System Details Access to Computer Files."""
    field_map = {
        'a': 'make_and_model_of_machine',
        'b': 'programming_language',
        'c': 'operating_system',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'make_and_model_of_machine': value.get('a'),
        'programming_language': value.get('b'),
        'operating_system': value.get('c'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('added_entry_taxonomic_identification', '^754__')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    """Added Entry-Taxonomic Identification."""
    field_map = {
        'a': 'taxonomic_name',
        'c': 'taxonomic_category',
        'd': 'common_or_alternative_name',
        'x': 'non_public_note',
        'z': 'public_note',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_taxonomic_identification',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'taxonomic_name': utils.force_list(value.get('a')),
        'taxonomic_category': utils.force_list(value.get('c')),
        'common_or_alternative_name': utils.force_list(value.get('d')),
        'non_public_note': utils.force_list(value.get('x')),
        'public_note': utils.force_list(value.get('z')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_taxonomic_identification': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }
