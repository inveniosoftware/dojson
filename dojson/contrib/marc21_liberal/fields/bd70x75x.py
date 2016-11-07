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

from ..model import marc21_liberal


@marc21_liberal.over('added_entry_personal_name', '^700..')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    """Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        's': 'version',
        'a': 'personal_name',
        'n': 'number_of_part_section_of_a_work',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'r': 'key_for_music',
        'k': 'form_subheading',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        't': 'title_of_a_work',
        'q': 'fuller_form_of_name',
        'b': 'numeration',
        'i': 'relationship_information',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        '6': 'linkage',
        'j': 'attribution_qualifier',
        'm': 'medium_of_performance_for_music',
        '4': 'relator_code',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'u': 'affiliation',
        'x': 'international_standard_serial_number',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'd': 'dates_associated_with_a_name',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('type_of_added_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'version': value.get('s'),
        'personal_name': value.get('a'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'key_for_music': value.get('r'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'title_of_a_work': value.get('t'),
        'fuller_form_of_name': value.get('q'),
        'numeration': value.get('b'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'international_standard_serial_number': value.get('x'),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'institution_to_which_field_applies': value.get('5'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        'type_of_added_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_corporate_name', '^710..')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    """Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        's': 'version',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'n': 'number_of_part_section_meeting',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        't': 'title_of_a_work',
        'b': 'subordinate_unit',
        'i': 'relationship_information',
        'e': 'relator_term',
        'f': 'date_of_a_work',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'd': 'date_of_meeting_or_treaty_signing',
        'm': 'medium_of_performance_for_music',
        'r': 'key_for_music',
        'p': 'name_of_part_section_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'u': 'affiliation',
        'x': 'international_standard_serial_number',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        '4': 'relator_code',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('type_of_added_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'version': value.get('s'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'title_of_a_work': value.get('t'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'key_for_music': value.get('r'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'affiliation': value.get('u'),
        'international_standard_serial_number': value.get('x'),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        'type_of_added_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_meeting_name', '^711..')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    """Added Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        's': 'version',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        'h': 'medium',
        'g': 'miscellaneous_information',
        'u': 'affiliation',
        'k': 'form_subheading',
        '3': 'materials_specified',
        't': 'title_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        'i': 'relationship_information',
        'e': 'subordinate_unit',
        'f': 'date_of_a_work',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'j': 'relator_term',
        '4': 'relator_code',
        'p': 'name_of_part_section_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_meeting',
        'x': 'international_standard_serial_number',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'd': 'date_of_meeting',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('type_of_added_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'version': value.get('s'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'affiliation': value.get('u'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'title_of_a_work': value.get('t'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_a_work': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'international_standard_serial_number': value.get('x'),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'date_of_meeting': value.get('d'),
        'institution_to_which_field_applies': value.get('5'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        'type_of_added_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_uncontrolled_name', '^720..')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    """Added Entry-Uncontrolled Name."""
    indicator_map1 = {"1": "Personal", "2": "Other", "_": "Not specified"}
    field_map = {
        '6': 'linkage',
        'e': 'relator_term',
        'a': 'name',
        '4': 'relator_code',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_name')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'name': value.get('a'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_name': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_uniform_title', '^730..')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    """Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        's': 'version',
        'a': 'uniform_title',
        'f': 'date_of_a_work',
        'i': 'relationship_information',
        'p': 'name_of_part_section_of_a_work',
        '6': 'linkage',
        'd': 'date_of_treaty_signing',
        'm': 'medium_of_performance_for_music',
        'h': 'medium',
        'g': 'miscellaneous_information',
        '8': 'field_link_and_sequence_number',
        'k': 'form_subheading',
        '3': 'materials_specified',
        'o': 'arranged_statement_for_music',
        't': 'title_of_a_work',
        '0': 'authority_record_control_number_or_standard_number',
        'n': 'number_of_part_section_of_a_work',
        'x': 'international_standard_serial_number',
        'l': 'language_of_a_work',
        'r': 'key_for_music',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('nonfiling_characters')

    if key[4] != '_':
        order.append('type_of_added_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'version': value.get('s'),
        'uniform_title': value.get('a'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'medium': value.get('h'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'arranged_statement_for_music': value.get('o'),
        'title_of_a_work': value.get('t'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'international_standard_serial_number': value.get('x'),
        'language_of_a_work': value.get('l'),
        'key_for_music': value.get('r'),
        'institution_to_which_field_applies': value.get('5'),
        'nonfiling_characters': indicator_map1.get(key[3], key[3]),
        'type_of_added_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_uncontrolled_related_analytical_title', '^740..')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"2": "Analytical entry", "_": "No information provided"}
    field_map = {
        'a': 'uncontrolled_related_analytical_title',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_part_section_of_a_work',
        '6': 'linkage',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('nonfiling_characters')

    if key[4] != '_':
        order.append('type_of_added_entry')

    record_dict = {
        '__order__': order if len(order) else None,
        'uncontrolled_related_analytical_title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'institution_to_which_field_applies': value.get('5'),
        'nonfiling_characters': indicator_map1.get(key[3], key[3]),
        'type_of_added_entry': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    """Added Entry-Geographic Name."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_heading_or_term',
        '3': 'materials_specified',
        'a': 'geographic_name',
        'e': 'relator_term',
        '6': 'linkage',
        '0': 'authority_record_control_number',
        '4': 'relator_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_heading_or_term': value.get('2'),
        'materials_specified': value.get('3'),
        'geographic_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_hierarchical_place_name', '^752..')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    """Added Entry-Hierarchical Place Name."""
    field_map = {
        'g': 'other_nonjurisdictional_geographic_region_and_feature',
        'a': 'country_or_larger_entity',
        '2': 'source_of_heading_or_term',
        'c': 'intermediate_political_jurisdiction',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        'b': 'first_order_political_jurisdiction',
        '6': 'linkage',
        'h': 'extraterrestrial_area',
        'd': 'city',
        'f': 'city_subsection',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'source_of_heading_or_term': value.get('2'),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'linkage': value.get('6'),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'city': value.get('d'),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('system_details_access_to_computer_files', '^753..')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    """System Details Access to Computer Files."""
    field_map = {
        'a': 'make_and_model_of_machine',
        '2': 'source_of_term',
        'c': 'operating_system',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        'b': 'programming_language',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'make_and_model_of_machine': value.get('a'),
        'source_of_term': value.get('2'),
        'operating_system': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'programming_language': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('added_entry_taxonomic_identification', '^754..')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    """Added Entry-Taxonomic Identification."""
    field_map = {
        'a': 'taxonomic_name',
        '2': 'source_of_taxonomic_identification',
        'c': 'taxonomic_category',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
        'd': 'common_or_alternative_name',
        '6': 'linkage',
        'z': 'public_note',
        'x': 'non_public_note',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'taxonomic_name': utils.force_list(
            value.get('a')
        ),
        'source_of_taxonomic_identification': value.get('2'),
        'taxonomic_category': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'common_or_alternative_name': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'non_public_note': utils.force_list(
            value.get('x')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
