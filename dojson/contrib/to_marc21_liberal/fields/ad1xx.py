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

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('100', '^heading_personal_name$')
@utils.filter_values
def reverse_heading_personal_name(self, key, value):
    """Reverse - Heading-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'personal_name': 'a',
        'geographic_subdivision': 'z',
        'number_of_part_section_of_a_work': 'n',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'fuller_form_of_name': 'q',
        'medium': 'h',
        'name_of_part_section_of_a_work': 'p',
        'numeration': 'b',
        'linkage': '6',
        'title_of_a_work': 't',
        'version': 's',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'titles_and_other_words_associated_with_a_name': 'c',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'key_for_music': 'r',
        'medium_of_performance_for_music': 'm',
        'general_subdivision': 'x',
        'attribution_qualifier': 'j',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('personal_name'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'q': value.get('fuller_form_of_name'),
        'h': value.get('medium'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'b': value.get('numeration'),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'r': value.get('key_for_music'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'o': value.get('arranged_statement_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('110', '^heading_corporate_name$')
@utils.filter_values
def reverse_heading_corporate_name(self, key, value):
    """Reverse - Heading-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'geographic_subdivision': 'z',
        'number_of_part_section_meeting': 'n',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'date_of_meeting_or_treaty_signing': 'd',
        'relator_term': 'e',
        'medium': 'h',
        'name_of_part_section_of_a_work': 'p',
        'subordinate_unit': 'b',
        'linkage': '6',
        'title_of_a_work': 't',
        'version': 's',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'key_for_music': 'r',
        'medium_of_performance_for_music': 'm',
        'general_subdivision': 'x',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'h': value.get('medium'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'r': value.get('key_for_music'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('111', '^heading_meeting_name$')
@utils.filter_values
def reverse_heading_meeting_name(self, key, value):
    """Reverse - Heading-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'form_subdivision': 'v',
        'location_of_meeting': 'c',
        'general_subdivision': 'x',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'miscellaneous_information': 'g',
        'form_subheading': 'k',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'date_of_meeting': 'd',
        'title_of_a_work': 't',
        'subordinate_unit': 'e',
        'number_of_part_section_meeting': 'n',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'medium': 'h',
        'relator_term': 'j',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'date_of_a_work': 'f',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'd': value.get('date_of_meeting'),
        't': value.get('title_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'h': value.get('medium'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('130', '^heading_uniform_title$')
@utils.filter_values
def reverse_heading_uniform_title(self, key, value):
    """Reverse - Heading-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'form_subdivision': 'v',
        'arranged_statement_for_music': 'o',
        'general_subdivision': 'x',
        'uniform_title': 'a',
        'geographic_subdivision': 'z',
        'number_of_part_section_of_a_work': 'n',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'language_of_a_work': 'l',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'medium': 'h',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'date_of_a_work': 'f',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'o': value.get('arranged_statement_for_music'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('uniform_title'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'l': value.get('language_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': value.get('title_of_a_work'),
        'h': value.get('medium'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('date_of_a_work'),
        'r': value.get('key_for_music'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('148', '^heading_chronological_term$')
@utils.filter_values
def reverse_heading_chronological_term(self, key, value):
    """Reverse - Heading-Chronological Term."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'chronological_term': 'a',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('150', '^heading_topical_term$')
@utils.filter_values
def reverse_heading_topical_term(self, key, value):
    """Reverse - Heading-Topical Term."""
    field_map = {
        'miscellaneous_information': 'g',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'topical_term_or_geographic_name_entry_element': 'a',
        'form_subdivision': 'v',
        'topical_term_following_geographic_name_entry_element': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('151', '^heading_geographic_name$')
@utils.filter_values
def reverse_heading_geographic_name(self, key, value):
    """Reverse - Heading-Geographic Name."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'geographic_name': 'a',
        'chronological_subdivision': 'y',
        'miscellaneous_information': 'g',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('geographic_name'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('155', '^heading_genre_form_term$')
@utils.filter_values
def reverse_heading_genre_form_term(self, key, value):
    """Reverse - Heading-Genre/Form Term."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'genre_form_term': 'a',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('genre_form_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('162', '^heading_medium_of_performance_term$')
@utils.filter_values
def reverse_heading_medium_of_performance_term(self, key, value):
    """Reverse - Heading-Medium of Performance Term."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'medium_of_performance_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('medium_of_performance_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('180', '^heading_general_subdivision$')
@utils.filter_values
def reverse_heading_general_subdivision(self, key, value):
    """Reverse - Heading-General Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('181', '^heading_geographic_subdivision$')
@utils.filter_values
def reverse_heading_geographic_subdivision(self, key, value):
    """Reverse - Heading-Geographic Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('182', '^heading_chronological_subdivision$')
@utils.filter_values
def reverse_heading_chronological_subdivision(self, key, value):
    """Reverse - Heading-Chronological Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('185', '^heading_form_subdivision$')
@utils.filter_values
def reverse_heading_form_subdivision(self, key, value):
    """Reverse - Heading-Form Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
