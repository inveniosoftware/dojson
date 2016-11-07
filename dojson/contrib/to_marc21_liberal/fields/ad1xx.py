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
        'fuller_form_of_name': 'q',
        'title_of_a_work': 't',
        'dates_associated_with_a_name': 'd',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
        'numeration': 'b',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'titles_and_other_words_associated_with_a_name': 'c',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'attribution_qualifier': 'j',
        'arranged_statement_for_music': 'o',
        'personal_name': 'a',
        'number_of_part_section_of_a_work': 'n',
        'medium': 'h',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'version': 's',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('fuller_form_of_name'),
        't': value.get('title_of_a_work'),
        'd': value.get('dates_associated_with_a_name'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('numeration'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('personal_name'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        's': value.get('version'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
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
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'date_of_meeting_or_treaty_signing': 'd',
        'form_subheading': 'k',
        'geographic_subdivision': 'z',
        'subordinate_unit': 'b',
        'general_subdivision': 'x',
        'location_of_meeting': 'c',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'arranged_statement_for_music': 'o',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'number_of_part_section_meeting': 'n',
        'medium': 'h',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'version': 's',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'o': value.get('arranged_statement_for_music'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'h': value.get('medium'),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        's': value.get('version'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
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
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'number_of_part_section_meeting': 'n',
        'language_of_a_work': 'l',
        'form_subheading': 'k',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'medium': 'h',
        'field_link_and_sequence_number': '8',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'location_of_meeting': 'c',
        'version': 's',
        'date_of_meeting': 'd',
        'chronological_subdivision': 'y',
        'subordinate_unit': 'e',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'general_subdivision': 'x',
        'relator_term': 'j',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'l': value.get('language_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'h': value.get('medium'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        's': value.get('version'),
        'd': value.get('date_of_meeting'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
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
        'geographic_subdivision': 'z',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'number_of_part_section_of_a_work': 'n',
        'language_of_a_work': 'l',
        'form_subheading': 'k',
        'uniform_title': 'a',
        'medium': 'h',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'medium_of_performance_for_music': 'm',
        'version': 's',
        'date_of_treaty_signing': 'd',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': value.get('title_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'a': value.get('uniform_title'),
        'h': value.get('medium'),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        's': value.get('version'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'o': value.get('arranged_statement_for_music'),
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
        'chronological_term': 'a',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'topical_term_following_geographic_name_entry_element': 'b',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'general_subdivision': 'x',
        'topical_term_or_geographic_name_entry_element': 'a',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
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
        'miscellaneous_information': 'g',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'linkage': '6',
        'geographic_name': 'a',
        'geographic_subdivision': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'a': value.get('geographic_name'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
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
        'genre_form_term': 'a',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('genre_form_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'medium_of_performance_term': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('medium_of_performance_term'),
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


@to_marc21_liberal_authority.over('180', '^heading_general_subdivision$')
@utils.filter_values
def reverse_heading_general_subdivision(self, key, value):
    """Reverse - Heading-General Subdivision."""
    field_map = {
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
