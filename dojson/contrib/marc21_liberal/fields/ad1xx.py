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


@marc21_liberal_authority.over('heading_personal_name', '^100..')
@utils.filter_values
def heading_personal_name(self, key, value):
    """Heading-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    field_map = {
        'a': 'personal_name',
        's': 'version',
        'n': 'number_of_part_section_of_a_work',
        'j': 'attribution_qualifier',
        'm': 'medium_of_performance_for_music',
        'e': 'relator_term',
        'q': 'fuller_form_of_name',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
        'c': 'titles_and_other_words_associated_with_a_name',
        '6': 'linkage',
        'd': 'dates_associated_with_a_name',
        'v': 'form_subdivision',
        'o': 'arranged_statement_for_music',
        'x': 'general_subdivision',
        'b': 'numeration',
        'l': 'language_of_a_work',
        'r': 'key_for_music',
        'z': 'geographic_subdivision',
        'f': 'date_of_a_work',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_personal_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'personal_name': value.get('a'),
        'version': value.get('s'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'fuller_form_of_name': value.get('q'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
        'dates_associated_with_a_name': value.get('d'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'arranged_statement_for_music': value.get('o'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'numeration': value.get('b'),
        'language_of_a_work': value.get('l'),
        'key_for_music': value.get('r'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'date_of_a_work': value.get('f'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_corporate_name', '^110..')
@utils.filter_values
def heading_corporate_name(self, key, value):
    """Heading-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        'a': 'corporate_name_or_jurisdiction_name_as_entry_element',
        's': 'version',
        'b': 'subordinate_unit',
        'm': 'medium_of_performance_for_music',
        'e': 'relator_term',
        'k': 'form_subheading',
        '8': 'field_link_and_sequence_number',
        'g': 'miscellaneous_information',
        'c': 'location_of_meeting',
        '6': 'linkage',
        'd': 'date_of_meeting_or_treaty_signing',
        'v': 'form_subdivision',
        'o': 'arranged_statement_for_music',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_meeting',
        'l': 'language_of_a_work',
        'r': 'key_for_music',
        'z': 'geographic_subdivision',
        'f': 'date_of_a_work',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_corporate_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'version': value.get('s'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'arranged_statement_for_music': value.get('o'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'language_of_a_work': value.get('l'),
        'key_for_music': value.get('r'),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'date_of_a_work': value.get('f'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_meeting_name', '^111..')
@utils.filter_values
def heading_meeting_name(self, key, value):
    """Heading-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    field_map = {
        '6': 'linkage',
        'a': 'meeting_name_or_jurisdiction_name_as_entry_element',
        't': 'title_of_a_work',
        'q': 'name_of_meeting_following_jurisdiction_name_entry_element',
        's': 'version',
        'n': 'number_of_part_section_meeting',
        'z': 'geographic_subdivision',
        'j': 'relator_term',
        'd': 'date_of_meeting',
        '8': 'field_link_and_sequence_number',
        'e': 'subordinate_unit',
        'g': 'miscellaneous_information',
        'v': 'form_subdivision',
        'k': 'form_subheading',
        'l': 'language_of_a_work',
        'x': 'general_subdivision',
        'f': 'date_of_a_work',
        'c': 'location_of_meeting',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_meeting_name_entry_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'title_of_a_work': value.get('t'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'version': value.get('s'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'date_of_meeting': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'language_of_a_work': value.get('l'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'date_of_a_work': value.get('f'),
        'location_of_meeting': utils.force_list(
            value.get('c')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_uniform_title', '^130..')
@utils.filter_values
def heading_uniform_title(self, key, value):
    """Heading-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '6': 'linkage',
        'a': 'uniform_title',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        'o': 'arranged_statement_for_music',
        'r': 'key_for_music',
        's': 'version',
        'x': 'general_subdivision',
        'n': 'number_of_part_section_of_a_work',
        'd': 'date_of_treaty_signing',
        'l': 'language_of_a_work',
        'g': 'miscellaneous_information',
        'k': 'form_subheading',
        'm': 'medium_of_performance_for_music',
        'z': 'geographic_subdivision',
        'f': 'date_of_a_work',
        't': 'title_of_a_work',
        'p': 'name_of_part_section_of_a_work',
        'h': 'medium',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'uniform_title': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'arranged_statement_for_music': value.get('o'),
        'key_for_music': value.get('r'),
        'version': value.get('s'),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'language_of_a_work': value.get('l'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'date_of_a_work': value.get('f'),
        'title_of_a_work': value.get('t'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'medium': value.get('h'),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_chronological_term', '^148..')
@utils.filter_values
def heading_chronological_term(self, key, value):
    """Heading-Chronological Term."""
    field_map = {
        '6': 'linkage',
        'a': 'chronological_term',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'chronological_term': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
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


@marc21_liberal_authority.over('heading_topical_term', '^150..')
@utils.filter_values
def heading_topical_term(self, key, value):
    """Heading-Topical Term."""
    field_map = {
        '6': 'linkage',
        'a': 'topical_term_or_geographic_name_entry_element',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'g': 'miscellaneous_information',
        'x': 'general_subdivision',
        'b': 'topical_term_following_geographic_name_entry_element',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
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


@marc21_liberal_authority.over('heading_geographic_name', '^151..')
@utils.filter_values
def heading_geographic_name(self, key, value):
    """Heading-Geographic Name."""
    field_map = {
        '6': 'linkage',
        'a': 'geographic_name',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'g': 'miscellaneous_information',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'geographic_name': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
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


@marc21_liberal_authority.over('heading_genre_form_term', '^155..')
@utils.filter_values
def heading_genre_form_term(self, key, value):
    """Heading-Genre/Form Term."""
    field_map = {
        '6': 'linkage',
        'a': 'genre_form_term',
        'v': 'form_subdivision',
        'y': 'chronological_subdivision',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'genre_form_term': value.get('a'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
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


@marc21_liberal_authority.over('heading_medium_of_performance_term', '^162..')
@utils.filter_values
def heading_medium_of_performance_term(self, key, value):
    """Heading-Medium of Performance Term."""
    field_map = {
        '6': 'linkage',
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
        'linkage': value.get('6'),
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


@marc21_liberal_authority.over('heading_general_subdivision', '^180..')
@utils.filter_values
def heading_general_subdivision(self, key, value):
    """Heading-General Subdivision."""
    field_map = {
        '6': 'linkage',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_geographic_subdivision', '^181..')
@utils.filter_values
def heading_geographic_subdivision(self, key, value):
    """Heading-Geographic Subdivision."""
    field_map = {
        '6': 'linkage',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_chronological_subdivision', '^182..')
@utils.filter_values
def heading_chronological_subdivision(self, key, value):
    """Heading-Chronological Subdivision."""
    field_map = {
        '6': 'linkage',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('heading_form_subdivision', '^185..')
@utils.filter_values
def heading_form_subdivision(self, key, value):
    """Heading-Form Subdivision."""
    field_map = {
        '6': 'linkage',
        'v': 'form_subdivision',
        '8': 'field_link_and_sequence_number',
        'z': 'geographic_subdivision',
        'x': 'general_subdivision',
        'y': 'chronological_subdivision',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'form_subdivision': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_subdivision': utils.force_list(
            value.get('z')
        ),
        'general_subdivision': utils.force_list(
            value.get('x')
        ),
        'chronological_subdivision': utils.force_list(
            value.get('y')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
