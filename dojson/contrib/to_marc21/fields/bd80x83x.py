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
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'titles_and_other_words_associated_with_a_name': 'c',
        'fuller_form_of_name': 'q',
        'bibliographic_record_control_number': 'w',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'international_standard_serial_number': 'x',
        'numeration': 'b',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'relator_code': '4',
        'control_subfield': '7',
        'language_of_a_work': 'l',
        'title_of_a_work': 't',
        'volume_sequential_designation': 'v',
        'affiliation': 'u',
        'dates_associated_with_a_name': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'personal_name': 'a',
        'form_subheading': 'k',
        'number_of_part_section_of_a_work': 'n',
        'attribution_qualifier': 'j',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'q': value.get('fuller_form_of_name'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'b': value.get('numeration'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '7': value.get('control_subfield'),
        'l': value.get('language_of_a_work'),
        't': value.get('title_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        'u': value.get('affiliation'),
        'd': value.get('dates_associated_with_a_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('personal_name'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('810', '^series_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_corporate_name(self, key, value):
    """Reverse - Series Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'location_of_meeting': 'c',
        'bibliographic_record_control_number': 'w',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'international_standard_serial_number': 'x',
        'subordinate_unit': 'b',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'medium': 'h',
        'medium_of_performance_for_music': 'm',
        'relator_term': 'e',
        'relator_code': '4',
        'control_subfield': '7',
        'language_of_a_work': 'l',
        'title_of_a_work': 't',
        'volume_sequential_designation': 'v',
        'affiliation': 'u',
        'date_of_meeting_or_treaty_signing': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'form_subheading': 'k',
        'number_of_part_section_meeting': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '7': value.get('control_subfield'),
        'l': value.get('language_of_a_work'),
        't': value.get('title_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        'u': value.get('affiliation'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('811', '^series_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_added_entry_meeting_name(self, key, value):
    """Reverse - Series Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    field_map = {
        'location_of_meeting': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'bibliographic_record_control_number': 'w',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'field_link_and_sequence_number': '8',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'international_standard_serial_number': 'x',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'medium': 'h',
        'materials_specified': '3',
        'subordinate_unit': 'e',
        'relator_code': '4',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'language_of_a_work': 'l',
        'title_of_a_work': 't',
        'volume_sequential_designation': 'v',
        'affiliation': 'u',
        'date_of_meeting': 'd',
        'control_subfield': '7',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'form_subheading': 'k',
        'number_of_part_section_meeting': 'n',
        'relator_term': 'j',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'h': value.get('medium'),
        '3': value.get('materials_specified'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'l': value.get('language_of_a_work'),
        't': value.get('title_of_a_work'),
        'v': value.get('volume_sequential_designation'),
        'u': value.get('affiliation'),
        'd': value.get('date_of_meeting'),
        '7': value.get('control_subfield'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
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
        'arranged_statement_for_music': 'o',
        'key_for_music': 'r',
        'miscellaneous_information': 'g',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'field_link_and_sequence_number': '8',
        'bibliographic_record_control_number': 'w',
        'date_of_a_work': 'f',
        'international_standard_serial_number': 'x',
        'name_of_part_section_of_a_work': 'p',
        'linkage': '6',
        'title_of_a_work': 't',
        'medium_of_performance_for_music': 'm',
        'control_subfield': '7',
        'medium': 'h',
        'volume_sequential_designation': 'v',
        'date_of_treaty_signing': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'uniform_title': 'a',
        'form_subheading': 'k',
        'language_of_a_work': 'l',
        'number_of_part_section_of_a_work': 'n',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'o': value.get('arranged_statement_for_music'),
        'r': value.get('key_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'f': value.get('date_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        't': value.get('title_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '7': value.get('control_subfield'),
        'h': value.get('medium'),
        'v': value.get('volume_sequential_designation'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('uniform_title'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }
