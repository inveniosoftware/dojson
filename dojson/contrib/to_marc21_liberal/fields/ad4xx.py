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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'relator_term': 'e',
        'fuller_form_of_name': 'q',
        'number_of_part_section_of_a_work': 'n',
        'form_subdivision': 'v',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'numeration': 'b',
        'version': 's',
        'key_for_music': 'r',
        'form_subheading': 'k',
        'medium': 'h',
        'personal_name': 'a',
        'dates_associated_with_a_name': 'd',
        'titles_and_other_words_associated_with_a_name': 'c',
        'attribution_qualifier': 'j',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'q': value.get('fuller_form_of_name'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('numeration'),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'h': value.get('medium'),
        'a': value.get('personal_name'),
        'd': value.get('dates_associated_with_a_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'date_of_a_work': 'f',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'relator_term': 'e',
        'number_of_part_section_meeting': 'n',
        'chronological_subdivision': 'y',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'b',
        'version': 's',
        'key_for_music': 'r',
        'form_subheading': 'k',
        'medium': 'h',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_meeting_or_treaty_signing': 'd',
        'location_of_meeting': 'c',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('title_of_a_work'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'h': value.get('medium'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'date_of_a_work': 'f',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'subordinate_unit': 'e',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'date_of_meeting': 'd',
        'number_of_part_section_meeting': 'n',
        'form_subdivision': 'v',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'form_subheading': 'k',
        'medium': 'h',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'title_of_a_work': 't',
        'location_of_meeting': 'c',
        'relator_term': 'j',
        'name_of_part_section_of_a_work': 'p',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'f': value.get('date_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'd': value.get('date_of_meeting'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'h': value.get('medium'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        't': value.get('title_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'date_of_a_work': 'f',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'date_of_treaty_signing': 'd',
        'number_of_part_section_of_a_work': 'n',
        'chronological_subdivision': 'y',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'key_for_music': 'r',
        'form_subheading': 'k',
        'medium': 'h',
        'uniform_title': 'a',
        'title_of_a_work': 't',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
        'linkage': '6',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'h': value.get('medium'),
        'a': value.get('uniform_title'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
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
        'linkage': '6',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'chronological_term': 'a',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('chronological_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'geographic_subdivision': 'z',
        'topical_term_or_geographic_name_entry_element': 'a',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'topical_term_following_geographic_name_entry_element': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
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
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'form_subdivision': 'v',
        'geographic_name': 'a',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'control_subfield': 'w',
        'relationship_code': '4',
        'chronological_subdivision': 'y',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('geographic_name'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
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
        'linkage': '6',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'genre_form_term': 'a',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('genre_form_term'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'medium_of_performance_term': 'a',
        'relationship_information': 'i',
        'control_subfield': 'w',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('medium_of_performance_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
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
        'linkage': '6',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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
        'linkage': '6',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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
        'linkage': '6',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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
        'linkage': '6',
        'control_subfield': 'w',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
