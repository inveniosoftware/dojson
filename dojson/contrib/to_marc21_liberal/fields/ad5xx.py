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
        'general_subdivision': 'x',
        'numeration': 'b',
        'control_subfield': 'w',
        'key_for_music': 'r',
        'personal_name': 'a',
        'fuller_form_of_name': 'q',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'name_of_part_section_of_a_work': 'p',
        'titles_and_other_words_associated_with_a_name': 'c',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'relator_term': 'e',
        'linkage': '6',
        'dates_associated_with_a_name': 'd',
        'title_of_a_work': 't',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'number_of_part_section_of_a_work': 'n',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'attribution_qualifier': 'j',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': value.get('numeration'),
        'w': value.get('control_subfield'),
        'r': value.get('key_for_music'),
        'a': value.get('personal_name'),
        'q': value.get('fuller_form_of_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        'd': value.get('dates_associated_with_a_name'),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'subordinate_unit': 'b',
        'control_subfield': 'w',
        'key_for_music': 'r',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'name_of_part_section_of_a_work': 'p',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'relator_term': 'e',
        'linkage': '6',
        'date_of_meeting_or_treaty_signing': 'd',
        'title_of_a_work': 't',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'number_of_part_section_meeting': 'n',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'w': value.get('control_subfield'),
        'r': value.get('key_for_music'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'control_subfield': 'w',
        'version': 's',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'name_of_part_section_of_a_work': 'p',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'subordinate_unit': 'e',
        'linkage': '6',
        'date_of_meeting': 'd',
        'title_of_a_work': 't',
        'relationship_code': '4',
        'form_subdivision': 'v',
        'field_link_and_sequence_number': '8',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'number_of_part_section_meeting': 'n',
        'medium': 'h',
        'relator_term': 'j',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'w': value.get('control_subfield'),
        's': value.get('version'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '6': value.get('linkage'),
        'd': value.get('date_of_meeting'),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'h': value.get('medium'),
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


@to_marc21_liberal_authority.over('530', '^see_also_from_tracing_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_uniform_title(self, key, value):
    """Reverse - See Also From Tracing-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'general_subdivision': 'x',
        'control_subfield': 'w',
        'version': 's',
        'uniform_title': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'relationship_information': 'i',
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'arranged_statement_for_music': 'o',
        'linkage': '6',
        'date_of_treaty_signing': 'd',
        'title_of_a_work': 't',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
        'date_of_a_work': 'f',
        'language_of_a_work': 'l',
        'chronological_subdivision': 'y',
        'number_of_part_section_of_a_work': 'n',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'w': value.get('control_subfield'),
        's': value.get('version'),
        'a': value.get('uniform_title'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        't': value.get('title_of_a_work'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
        'f': value.get('date_of_a_work'),
        'l': value.get('language_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
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
        'general_subdivision': 'x',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_term': 'a',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
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
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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


@to_marc21_liberal_authority.over('550', '^see_also_from_tracing_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_topical_term(self, key, value):
    """Reverse - See Also From Tracing-Topical Term."""
    field_map = {
        'general_subdivision': 'x',
        'linkage': '6',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'topical_term_or_geographic_name_entry_element': 'a',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'topical_term_following_geographic_name_entry_element': 'b',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
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
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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


@to_marc21_liberal_authority.over('551', '^see_also_from_tracing_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_geographic_name(self, key, value):
    """Reverse - See Also From Tracing-Geographic Name."""
    field_map = {
        'general_subdivision': 'x',
        'linkage': '6',
        'control_subfield': 'w',
        'geographic_name': 'a',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'miscellaneous_information': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
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
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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


@to_marc21_liberal_authority.over('555', '^see_also_from_tracing_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_genre_form_term(self, key, value):
    """Reverse - See Also From Tracing-Genre/Form Term."""
    field_map = {
        'general_subdivision': 'x',
        'linkage': '6',
        'control_subfield': 'w',
        'genre_form_term': 'a',
        'relationship_code': '4',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
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
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
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


@to_marc21_liberal_authority.over('562', '^see_also_from_tracing_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_see_also_from_tracing_medium_of_performance_term(self, key, value):
    """Reverse - See Also From Tracing-Medium of Performance Term."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'medium_of_performance_term': 'a',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'a': value.get('medium_of_performance_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
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
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'record_control_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
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
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'record_control_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
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
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'record_control_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
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
        'general_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'institution_to_which_field_applies': '5',
        'relationship_code': '4',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
        'record_control_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
