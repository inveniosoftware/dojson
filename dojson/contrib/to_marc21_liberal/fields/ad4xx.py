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


@to_marc21_liberal_authority.over('400', '^see_from_tracing_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_personal_name(self, key, value):
    """Reverse - See From Tracing-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'title_of_a_work': 't',
        'dates_associated_with_a_name': 'd',
        'relationship_information': 'i',
        'language_of_a_work': 'l',
        'control_subfield': 'w',
        'numeration': 'b',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'name_of_part_section_of_a_work': 'p',
        'geographic_subdivision': 'z',
        'personal_name': 'a',
        'medium': 'h',
        'form_subdivision': 'v',
        'relationship_code': '4',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'attribution_qualifier': 'j',
        'key_for_music': 'r',
        'titles_and_other_words_associated_with_a_name': 'c',
        'number_of_part_section_of_a_work': 'n',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'fuller_form_of_name': 'q',
        'form_subheading': 'k',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        'd': value.get('dates_associated_with_a_name'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'l': value.get('language_of_a_work'),
        'w': value.get('control_subfield'),
        'b': value.get('numeration'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('personal_name'),
        'h': value.get('medium'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'r': value.get('key_for_music'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'q': value.get('fuller_form_of_name'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_element'), value.get('type_of_personal_name_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('410', '^see_from_tracing_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_corporate_name(self, key, value):
    """Reverse - See From Tracing-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'title_of_a_work': 't',
        'date_of_meeting_or_treaty_signing': 'd',
        'relationship_information': 'i',
        'language_of_a_work': 'l',
        'control_subfield': 'w',
        'subordinate_unit': 'b',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'name_of_part_section_of_a_work': 'p',
        'geographic_subdivision': 'z',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'form_subdivision': 'v',
        'relationship_code': '4',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'location_of_meeting': 'c',
        'number_of_part_section_meeting': 'n',
        'key_for_music': 'r',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'medium': 'h',
        'form_subheading': 'k',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'l': value.get('language_of_a_work'),
        'w': value.get('control_subfield'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'r': value.get('key_for_music'),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('411', '^see_from_tracing_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_meeting_name(self, key, value):
    """Reverse - See From Tracing-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'title_of_a_work': 't',
        'date_of_meeting': 'd',
        'relationship_information': 'i',
        'language_of_a_work': 'l',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'geographic_subdivision': 'z',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'medium': 'h',
        'relationship_code': '4',
        'subordinate_unit': 'e',
        'miscellaneous_information': 'g',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'relator_term': 'j',
        'location_of_meeting': 'c',
        'number_of_part_section_meeting': 'n',
        'date_of_a_work': 'f',
        'linkage': '6',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'form_subheading': 'k',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        'd': value.get('date_of_meeting'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'l': value.get('language_of_a_work'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'h': value.get('medium'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'f': value.get('date_of_a_work'),
        '6': value.get('linkage'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('430', '^see_from_tracing_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_uniform_title(self, key, value):
    """Reverse - See From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'title_of_a_work': 't',
        'date_of_treaty_signing': 'd',
        'relationship_information': 'i',
        'language_of_a_work': 'l',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'geographic_subdivision': 'z',
        'uniform_title': 'a',
        'relationship_code': '4',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
        'number_of_part_section_of_a_work': 'n',
        'control_subfield': 'w',
        'date_of_a_work': 'f',
        'arranged_statement_for_music': 'o',
        'medium': 'h',
        'form_subheading': 'k',
        'version': 's',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'l': value.get('language_of_a_work'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'w': value.get('control_subfield'),
        'f': value.get('date_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        's': value.get('version'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('448', '^see_from_tracing_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_chronological_term(self, key, value):
    """Reverse - See From Tracing-Chronological Term."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'chronological_term': 'a',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'a': value.get('chronological_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('450', '^see_from_tracing_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_topical_term(self, key, value):
    """Reverse - See From Tracing-Topical Term."""
    field_map = {
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'topical_term_following_geographic_name_entry_element': 'b',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'topical_term_or_geographic_name_entry_element': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('451', '^see_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_geographic_name(self, key, value):
    """Reverse - See From Tracing-Geographic Name."""
    field_map = {
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'relationship_information': 'i',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'geographic_name': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'a': value.get('geographic_name'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('455', '^see_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_genre_form_term(self, key, value):
    """Reverse - See From Tracing-Genre/Form Term."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'genre_form_term': 'a',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'a': value.get('genre_form_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('462', '^see_from_tracing_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_medium_of_performance_term(self, key, value):
    """Reverse - See From Tracing-Medium of Performance Term."""
    field_map = {
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'medium_of_performance_term': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'a': value.get('medium_of_performance_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('480', '^see_from_tracing_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_general_subdivision(self, key, value):
    """Reverse - See From Tracing-General Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('481', '^see_from_tracing_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_geographic_subdivision(self, key, value):
    """Reverse - See From Tracing-Geographic Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('482', '^see_from_tracing_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_chronological_subdivision(self, key, value):
    """Reverse - See From Tracing-Chronological Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('485', '^see_from_tracing_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_from_tracing_form_subdivision(self, key, value):
    """Reverse - See From Tracing-Form Subdivision."""
    field_map = {
        'form_subdivision': 'v',
        'relationship_code': '4',
        'linkage': '6',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
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
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
