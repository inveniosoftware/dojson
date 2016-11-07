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


@to_marc21_liberal_authority.over('500', '^see_also_from_tracing_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_personal_name(self, key, value):
    """Reverse - See Also From Tracing-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'relator_term': 'e',
        'geographic_subdivision': 'z',
        'version': 's',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'titles_and_other_words_associated_with_a_name': 'c',
        'miscellaneous_information': 'g',
        'attribution_qualifier': 'j',
        'key_for_music': 'r',
        'dates_associated_with_a_name': 'd',
        'medium_of_performance_for_music': 'm',
        'numeration': 'b',
        'arranged_statement_for_music': 'o',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'personal_name': 'a',
        'relationship_code': '4',
        'number_of_part_section_of_a_work': 'n',
        'linkage': '6',
        'form_subdivision': 'v',
        'fuller_form_of_name': 'q',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'medium': 'h',
        'control_subfield': 'w',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        's': value.get('version'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'r': value.get('key_for_music'),
        'd': value.get('dates_associated_with_a_name'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': value.get('numeration'),
        'o': value.get('arranged_statement_for_music'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('personal_name'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'q': value.get('fuller_form_of_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('510', '^see_also_from_tracing_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_corporate_name(self, key, value):
    """Reverse - See Also From Tracing-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'relator_term': 'e',
        'geographic_subdivision': 'z',
        'version': 's',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'key_for_music': 'r',
        'date_of_meeting_or_treaty_signing': 'd',
        'medium_of_performance_for_music': 'm',
        'subordinate_unit': 'b',
        'arranged_statement_for_music': 'o',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'relationship_code': '4',
        'number_of_part_section_meeting': 'n',
        'linkage': '6',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'medium': 'h',
        'control_subfield': 'w',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        's': value.get('version'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'r': value.get('key_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'o': value.get('arranged_statement_for_music'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('511', '^see_also_from_tracing_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_meeting_name(self, key, value):
    """Reverse - See Also From Tracing-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'subordinate_unit': 'e',
        'geographic_subdivision': 'z',
        'version': 's',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'relator_term': 'j',
        'date_of_meeting': 'd',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'relationship_code': '4',
        'number_of_part_section_meeting': 'n',
        'linkage': '6',
        'form_subdivision': 'v',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'medium': 'h',
        'control_subfield': 'w',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        's': value.get('version'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('date_of_meeting'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('530', '^see_also_from_tracing_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_uniform_title(self, key, value):
    """Reverse - See Also From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'geographic_subdivision': 'z',
        'version': 's',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'miscellaneous_information': 'g',
        'key_for_music': 'r',
        'date_of_treaty_signing': 'd',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
        'date_of_a_work': 'f',
        'title_of_a_work': 't',
        'form_subheading': 'k',
        'chronological_subdivision': 'y',
        'uniform_title': 'a',
        'relationship_code': '4',
        'number_of_part_section_of_a_work': 'n',
        'linkage': '6',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'general_subdivision': 'x',
        'medium': 'h',
        'control_subfield': 'w',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        's': value.get('version'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'r': value.get('key_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
        'f': value.get('date_of_a_work'),
        't': value.get('title_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'a': value.get('uniform_title'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'h': value.get('medium'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('548', '^see_also_from_tracing_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_chronological_term(self, key, value):
    """Reverse - See Also From Tracing-Chronological Term."""
    field_map = {
        'geographic_subdivision': 'z',
        'chronological_term': 'a',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('chronological_term'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('550', '^see_also_from_tracing_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_topical_term(self, key, value):
    """Reverse - See Also From Tracing-Topical Term."""
    field_map = {
        'geographic_subdivision': 'z',
        'topical_term_or_geographic_name_entry_element': 'a',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'institution_to_which_field_applies': '5',
        'topical_term_following_geographic_name_entry_element': 'b',
        'general_subdivision': 'x',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('551', '^see_also_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_name(self, key, value):
    """Reverse - See Also From Tracing-Geographic Name."""
    field_map = {
        'geographic_subdivision': 'z',
        'geographic_name': 'a',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('geographic_name'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('555', '^see_also_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_genre_form_term(self, key, value):
    """Reverse - See Also From Tracing-Genre/Form Term."""
    field_map = {
        'geographic_subdivision': 'z',
        'genre_form_term': 'a',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'institution_to_which_field_applies': '5',
        'relationship_information': 'i',
        'control_subfield': 'w',
        'general_subdivision': 'x',
        'chronological_subdivision': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'a': value.get('genre_form_term'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'w': value.get('control_subfield'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('562', '^see_also_from_tracing_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_medium_of_performance_term(self, key, value):
    """Reverse - See Also From Tracing-Medium of Performance Term."""
    field_map = {
        'medium_of_performance_term': 'a',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('medium_of_performance_term'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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


@to_marc21_liberal_authority.over('580', '^see_also_from_tracing_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_general_subdivision(self, key, value):
    """Reverse - See Also From Tracing-General Subdivision."""
    field_map = {
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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


@to_marc21_liberal_authority.over('581', '^see_also_from_tracing_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Geographic Subdivision."""
    field_map = {
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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


@to_marc21_liberal_authority.over('582', '^see_also_from_tracing_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_chronological_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Chronological Subdivision."""
    field_map = {
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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


@to_marc21_liberal_authority.over('585', '^see_also_from_tracing_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_form_subdivision(self, key, value):
    """Reverse - See Also From Tracing-Form Subdivision."""
    field_map = {
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'form_subdivision': 'v',
        'chronological_subdivision': 'y',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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
