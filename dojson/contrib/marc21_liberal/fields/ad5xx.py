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

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('see_also_from_tracing_personal_name', '^500..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_personal_name(self, key, value):
    """See Also From Tracing-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'o': 'arranged_statement_for_music',
        'k': 'form_subheading',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'b': 'numeration',
        'v': 'form_subdivision',
        'a': 'personal_name',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'l': 'language_of_a_work',
        'c': 'titles_and_other_words_associated_with_a_name',
        'n': 'number_of_part_section_of_a_work',
        'j': 'attribution_qualifier',
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        's': 'version',
        'f': 'date_of_a_work',
        '4': 'relationship_code',
        'd': 'dates_associated_with_a_name',
        'p': 'name_of_part_section_of_a_work',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'e': 'relator_term',
        'i': 'relationship_information',
        'q': 'fuller_form_of_name',
        'r': 'key_for_music',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'arranged_statement_for_music': value.get('o'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'numeration': value.get('b'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'personal_name': value.get('a'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'language_of_a_work': value.get('l'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'version': value.get('s'),
        'date_of_a_work': value.get('f'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'fuller_form_of_name': value.get('q'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_corporate_name', '^510..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_corporate_name(self, key, value):
    """See Also From Tracing-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'o': 'arranged_statement_for_music',
        'k': 'form_subheading',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'b': 'subordinate_unit',
        'v': 'form_subdivision',
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'n': 'number_of_part_section_meeting',
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        's': 'version',
        'f': 'date_of_a_work',
        '4': 'relationship_code',
        'd': 'date_of_meeting_or_treaty_signing',
        'p': 'name_of_part_section_of_a_work',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'e': 'relator_term',
        'i': 'relationship_information',
        'r': 'key_for_music',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'arranged_statement_for_music': value.get('o'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'version': value.get('s'),
        'date_of_a_work': value.get('f'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_meeting_name', '^511..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_meeting_name(self, key, value):
    """See Also From Tracing-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'k': 'form_subheading',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        '0': 'authority_record_control_number_or_standard_number',
        'l': 'language_of_a_work',
        'c': 'location_of_meeting',
        'n': 'number_of_part_section_meeting',
        'j': 'relator_term',
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        's': 'version',
        'f': 'date_of_a_work',
        '4': 'relationship_code',
        'd': 'date_of_meeting',
        'p': 'name_of_part_section_of_a_work',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'e': 'subordinate_unit',
        'i': 'relationship_information',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'language_of_a_work': value.get('l'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'version': value.get('s'),
        'date_of_a_work': value.get('f'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'date_of_meeting': value.get('d'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_uniform_title', '^530..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_uniform_title(self, key, value):
    """See Also From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'o': 'arranged_statement_for_music',
        'k': 'form_subheading',
        'm': 'medium_of_performance_for_music',
        'g': 'miscellaneous_information',
        'h': 'medium',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'a': 'uniform_title',
        '0': 'authority_record_control_number_or_standard_number',
        'l': 'language_of_a_work',
        'n': 'number_of_part_section_of_a_work',
        '8': 'field_link_and_sequence_number',
        'w': 'control_subfield',
        '6': 'linkage',
        's': 'version',
        'f': 'date_of_a_work',
        '4': 'relationship_code',
        'd': 'date_of_treaty_signing',
        'p': 'name_of_part_section_of_a_work',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'r': 'key_for_music',
        't': 'title_of_a_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'arranged_statement_for_music': value.get('o'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'medium': value.get('h'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'uniform_title': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'version': value.get('s'),
        'date_of_a_work': value.get('f'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_chronological_term', '^548..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_chronological_term(self, key, value):
    """See Also From Tracing-Chronological Term."""
    field_map = {
        'w': 'control_subfield',
        '6': 'linkage',
        '4': 'relationship_code',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'a': 'chronological_term',
        '0': 'record_control_number',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_term': value.get('a'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_topical_term', '^550..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_topical_term(self, key, value):
    """See Also From Tracing-Topical Term."""
    field_map = {
        'w': 'control_subfield',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        '4': 'relationship_code',
        'b': 'topical_term_following_geographic_name_entry_element',
        'v': 'form_subdivision',
        'a': 'topical_term_or_geographic_name_entry_element',
        'z': 'geographic_subdivision',
        '0': 'authority_record_control_number_or_standard_number',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_geographic_name', '^551..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_geographic_name(self, key, value):
    """See Also From Tracing-Geographic Name."""
    field_map = {
        'w': 'control_subfield',
        '6': 'linkage',
        'g': 'miscellaneous_information',
        '4': 'relationship_code',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'a': 'geographic_name',
        '0': 'authority_record_control_number_or_standard_number',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'geographic_name': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_genre_form_term', '^555..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_genre_form_term(self, key, value):
    """See Also From Tracing-Genre/Form Term."""
    field_map = {
        'w': 'control_subfield',
        '6': 'linkage',
        '4': 'relationship_code',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        'a': 'genre_form_term',
        '0': 'record_control_number',
        'y': 'chronological_subdivision',
        'x': 'general_subdivision',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'control_subfield': value.get('w'),
        'linkage': value.get('6'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'genre_form_term': value.get('a'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_medium_of_performance_term', '^562..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_medium_of_performance_term(self, key, value):
    """See Also From Tracing-Medium of Performance Term."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        'w': 'control_subfield',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'a': 'medium_of_performance_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium_of_performance_term': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_general_subdivision', '^580..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_general_subdivision(self, key, value):
    """See Also From Tracing-General Subdivision."""
    field_map = {
        '0': 'record_control_number',
        '6': 'linkage',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_geographic_subdivision', '^581..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_geographic_subdivision(self, key, value):
    """See Also From Tracing-Geographic Subdivision."""
    field_map = {
        '0': 'record_control_number',
        '6': 'linkage',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_chronological_subdivision', '^582..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_chronological_subdivision(self, key, value):
    """See Also From Tracing-Chronological Subdivision."""
    field_map = {
        '0': 'record_control_number',
        '6': 'linkage',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('see_also_from_tracing_form_subdivision', '^585..')
@utils.for_each_value
@utils.filter_values
def see_also_from_tracing_form_subdivision(self, key, value):
    """See Also From Tracing-Form Subdivision."""
    field_map = {
        '0': 'record_control_number',
        '6': 'linkage',
        'w': 'control_subfield',
        'y': 'chronological_subdivision',
        '4': 'relationship_code',
        '5': 'institution_to_which_field_applies',
        'i': 'relationship_information',
        'x': 'general_subdivision',
        'z': 'geographic_subdivision',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'control_subfield': value.get('w'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'relationship_code': utils.force_list(
            value.get('4')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
