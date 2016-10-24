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

from ..model import to_marc21


@to_marc21.over('800', '^series_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_personal_name(self, key, value):
    """Reverse - Series Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    field_map = {
        'titles_and_other_words_associated_with_a_name': 'c',
        'form_subheading': 'k',
        'control_subfield': '7',
        'attribution_qualifier': 'j',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'personal_name': 'a',
        'version': 's',
        'title_of_a_work': 't',
        'dates_associated_with_a_name': 'd',
        'affiliation': 'u',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'fuller_form_of_name': 'q',
        'volume_sequential_designation': 'v',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'materials_specified': '3',
        'key_for_music': 'r',
        'relator_code': '4',
        'relator_term': 'e',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'bibliographic_record_control_number': 'w',
        'numeration': 'b',
        'name_of_part_section_of_a_work': 'p',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_personal_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_personal_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '7': value.get('control_subfield'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('personal_name'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'd': value.get('dates_associated_with_a_name'),
        'u': value.get('affiliation'),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('fuller_form_of_name'),
        'v': value.get('volume_sequential_designation'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'r': value.get('key_for_music'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'b': value.get('numeration'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('810', '^series_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_corporate_name(self, key, value):
    """Reverse - Series Added Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    field_map = {
        'location_of_meeting': 'c',
        'form_subheading': 'k',
        'control_subfield': '7',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'title_of_a_work': 't',
        'date_of_meeting_or_treaty_signing': 'd',
        'affiliation': 'u',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'volume_sequential_designation': 'v',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'materials_specified': '3',
        'key_for_music': 'r',
        'relator_term': 'e',
        'relator_code': '4',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'bibliographic_record_control_number': 'w',
        'subordinate_unit': 'b',
        'number_of_part_section_meeting': 'n',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_corporate_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_corporate_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '7': value.get('control_subfield'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'u': value.get('affiliation'),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': value.get('volume_sequential_designation'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'r': value.get('key_for_music'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('811', '^series_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_meeting_name(self, key, value):
    """Reverse - Series Added Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    field_map = {
        'location_of_meeting': 'c',
        'control_subfield': '7',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'title_of_a_work': 't',
        'date_of_meeting': 'd',
        'affiliation': 'u',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'volume_sequential_designation': 'v',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'materials_specified': '3',
        'relator_code': '4',
        'subordinate_unit': 'e',
        'version': 's',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
        'bibliographic_record_control_number': 'w',
        'relator_term': 'j',
        'number_of_part_section_meeting': 'n',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_meeting_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_meeting_name_entry_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '7': value.get('control_subfield'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        't': value.get('title_of_a_work'),
        'd': value.get('date_of_meeting'),
        'u': value.get('affiliation'),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'v': value.get('volume_sequential_designation'),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        's': value.get('version'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('830', '^series_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_uniform_title(self, key, value):
    """Reverse - Series Added Entry-Uniform Title."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'form_subheading': 'k',
        'control_subfield': '7',
        'name_of_part_section_of_a_work': 'p',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'uniform_title': 'a',
        'title_of_a_work': 't',
        'date_of_treaty_signing': 'd',
        'language_of_a_work': 'l',
        'field_link_and_sequence_number': '8',
        'medium_of_performance_for_music': 'm',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'materials_specified': '3',
        'key_for_music': 'r',
        'volume_sequential_designation': 'v',
        'version': 's',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'bibliographic_record_control_number': 'w',
        'number_of_part_section_of_a_work': 'n',
        'date_of_a_work': 'f',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '7': value.get('control_subfield'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('uniform_title'),
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'l': value.get('language_of_a_work'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'r': value.get('key_for_music'),
        'v': value.get('volume_sequential_designation'),
        's': value.get('version'),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }
