# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21, tomarc21


@marc21.over('added_entry_personal_name', '^700[103_][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    """Added Entry-Personal Name."""
    indicator_map1 = {"0": "Forename", "1": "Surname", "3": "Family name"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': utils.force_list(
            value.get('c')
        ),
        'numeration': value.get('b'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'attribution_qualifier': utils.force_list(
            value.get('j')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('^700[103_][_2]', 'added_entry_personal_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_personal_name(self, key, value):
    """Reverse - Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "#"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('personal_name')),
        'c': utils.reverse_force_list(value.get('titles_and_other_words_associated_with_a_name')),
        'b': utils.reverse_force_list(value.get('numeration')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('dates_associated_with_a_name')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('attribution_qualifier')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'q': utils.reverse_force_list(value.get('fuller_form_of_name')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        '_indicator1': indicator_map1.get(value.get('type_of_personal_name_entry_element')),
        '_indicator2': indicator_map2.get(value.get('type_of_added_entry')),
    }


@marc21.over('added_entry_corporate_name', '^710[10_2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    """Added Entry-Corporate Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('b')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting_or_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('^710[10_2][_2]', 'added_entry_corporate_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_corporate_name(self, key, value):
    """Reverse - Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "#"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('corporate_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'b': utils.reverse_force_list(value.get('subordinate_unit')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        'd': utils.reverse_force_list(value.get('date_of_meeting_or_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        '_indicator1': indicator_map1.get(value.get('type_of_corporate_name_entry_element')),
        '_indicator2': indicator_map2.get(value.get('type_of_added_entry')),
    }


@marc21.over('added_entry_meeting_name', '^711[10_2][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    """Added Entry-Meeting Name."""
    indicator_map1 = {"0": "Inverted name", "1": "Jurisdiction name", "2": "Name in direct order"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': utils.force_list(
            value.get('e')
        ),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'relator_term': utils.force_list(
            value.get('j')
        ),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': utils.force_list(
            value.get('n')
        ),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('^711[10_2][_2]', 'added_entry_meeting_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_meeting_name(self, key, value):
    """Reverse - Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "#"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('meeting_name_or_jurisdiction_name_as_entry_element')),
        'c': utils.reverse_force_list(value.get('location_of_meeting')),
        'e': utils.reverse_force_list(value.get('subordinate_unit')),
        'd': utils.reverse_force_list(value.get('date_of_meeting')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'j': utils.reverse_force_list(value.get('relator_term')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_meeting')),
        'q': utils.reverse_force_list(value.get('name_of_meeting_following_jurisdiction_name_entry_element')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        's': utils.reverse_force_list(value.get('version')),
        'u': utils.reverse_force_list(value.get('affiliation')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        '_indicator1': indicator_map1.get(value.get('type_of_meeting_name_entry_element')),
        '_indicator2': indicator_map2.get(value.get('type_of_added_entry')),
    }


@marc21.over('added_entry_uncontrolled_name', '^720[1_2].')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    """Added Entry-Uncontrolled Name."""
    indicator_map1 = {"#": "Not specified", "1": "Personal", "2": "Other"}
    return {
        'name': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'type_of_name': indicator_map1.get(key[3]),
    }


@tomarc21.over('^720[1_2].', 'added_entry_uncontrolled_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_name(self, key, value):
    """Reverse - Added Entry-Uncontrolled Name."""
    indicator_map1 = {"Not specified": "#", "Other": "2", "Personal": "1"}
    return {
        'a': utils.reverse_force_list(value.get('name')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('type_of_name')),
    }


@marc21.over('added_entry_uniform_title', '^730[_1032547698][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    """Added Entry-Uniform Title."""
    indicator_map1 = {"0": "Number of nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'uniform_title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'date_of_treaty_signing': utils.force_list(
            value.get('d')
        ),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': utils.force_list(
            value.get('i')
        ),
        'medium': value.get('h'),
        'form_subheading': utils.force_list(
            value.get('k')
        ),
        'medium_of_performance_for_music': utils.force_list(
            value.get('m')
        ),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'key_for_music': value.get('r'),
        'institution_to_which_field_applies': value.get('5'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'version': value.get('s'),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('^730[_1032547698][_2]', 'added_entry_uniform_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uniform_title(self, key, value):
    """Reverse - Added Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "#"}
    return {
        'a': utils.reverse_force_list(value.get('uniform_title')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        'd': utils.reverse_force_list(value.get('date_of_treaty_signing')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'f': utils.reverse_force_list(value.get('date_of_a_work')),
        'i': utils.reverse_force_list(value.get('relationship_information')),
        'h': utils.reverse_force_list(value.get('medium')),
        'k': utils.reverse_force_list(value.get('form_subheading')),
        'm': utils.reverse_force_list(value.get('medium_of_performance_for_music')),
        'l': utils.reverse_force_list(value.get('language_of_a_work')),
        'o': utils.reverse_force_list(value.get('arranged_statement_for_music')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'r': utils.reverse_force_list(value.get('key_for_music')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        't': utils.reverse_force_list(value.get('title_of_a_work')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        's': utils.reverse_force_list(value.get('version')),
        '_indicator1': indicator_map1.get(value.get('nonfiling_characters')),
        '_indicator2': indicator_map2.get(value.get('type_of_added_entry')),
    }


@marc21.over('added_entry_uncontrolled_related_analytical_title', '^740[_1032547698][_2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {"0": "No nonfiling characters", "1": "Number of nonfiling characters", "2": "Number of nonfiling characters", "3": "Number of nonfiling characters", "4": "Number of nonfiling characters", "5": "Number of nonfiling characters", "6": "Number of nonfiling characters", "7": "Number of nonfiling characters", "8": "Number of nonfiling characters", "9": "Number of nonfiling characters"}
    indicator_map2 = {"#": "No information provided", "2": "Analytical entry"}
    return {
        'uncontrolled_related_analytical_title': value.get('a'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': utils.force_list(
            value.get('n')
        ),
        'name_of_part_section_of_a_work': utils.force_list(
            value.get('p')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }


@tomarc21.over('^740[_1032547698][_2]', 'added_entry_uncontrolled_related_analytical_title')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Reverse - Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {"No nonfiling characters": "0", "Number of nonfiling characters": "8"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "#"}
    return {
        'a': utils.reverse_force_list(value.get('uncontrolled_related_analytical_title')),
        'h': utils.reverse_force_list(value.get('medium')),
        'n': utils.reverse_force_list(value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(value.get('name_of_part_section_of_a_work')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('nonfiling_characters')),
        '_indicator2': indicator_map2.get(value.get('type_of_added_entry')),
    }


@marc21.over('added_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    """Added Entry-Geographic Name."""
    return {
        'geographic_name': value.get('a'),
        'relator_term': utils.force_list(
            value.get('e')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^751..', 'added_entry_geographic_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_geographic_name(self, key, value):
    """Reverse - Added Entry-Geographic Name."""
    return {
        'a': utils.reverse_force_list(value.get('geographic_name')),
        'e': utils.reverse_force_list(value.get('relator_term')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '4': utils.reverse_force_list(value.get('relator_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('added_entry_hierarchical_place_name', '^752..')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    """Added Entry-Hierarchical Place Name."""
    return {
        'country_or_larger_entity': utils.force_list(
            value.get('a')
        ),
        'intermediate_political_jurisdiction': utils.force_list(
            value.get('c')
        ),
        'first_order_political_jurisdiction': value.get('b'),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': utils.force_list(
            value.get('g')
        ),
        'city_subsection': utils.force_list(
            value.get('f')
        ),
        'extraterrestrial_area': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^752..', 'added_entry_hierarchical_place_name')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Added Entry-Hierarchical Place Name."""
    return {
        'a': utils.reverse_force_list(value.get('country_or_larger_entity')),
        'c': utils.reverse_force_list(value.get('intermediate_political_jurisdiction')),
        'b': utils.reverse_force_list(value.get('first_order_political_jurisdiction')),
        'd': utils.reverse_force_list(value.get('city')),
        'g': utils.reverse_force_list(value.get('other_nonjurisdictional_geographic_region_and_feature')),
        'f': utils.reverse_force_list(value.get('city_subsection')),
        'h': utils.reverse_force_list(value.get('extraterrestrial_area')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '2': utils.reverse_force_list(value.get('source_of_heading_or_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('system_details_access_to_computer_files', '^753..')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    """System Details Access to Computer Files."""
    return {
        'make_and_model_of_machine': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'operating_system': value.get('c'),
        'programming_language': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^753..', 'system_details_access_to_computer_files')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_access_to_computer_files(self, key, value):
    """Reverse - System Details Access to Computer Files."""
    return {
        'a': utils.reverse_force_list(value.get('make_and_model_of_machine')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'c': utils.reverse_force_list(value.get('operating_system')),
        'b': utils.reverse_force_list(value.get('programming_language')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('added_entry_taxonomic_identification', '^754..')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    """Added Entry-Taxonomic Identification."""
    return {
        'taxonomic_name': utils.force_list(
            value.get('a')
        ),
        'non_public_note': utils.force_list(
            value.get('x')
        ),
        'taxonomic_category': utils.force_list(
            value.get('c')
        ),
        'common_or_alternative_name': utils.force_list(
            value.get('d')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_taxonomic_identification': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('^754..', 'added_entry_taxonomic_identification')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_taxonomic_identification(self, key, value):
    """Reverse - Added Entry-Taxonomic Identification."""
    return {
        'a': utils.reverse_force_list(value.get('taxonomic_name')),
        'x': utils.reverse_force_list(value.get('non_public_note')),
        'c': utils.reverse_force_list(value.get('taxonomic_category')),
        'd': utils.reverse_force_list(value.get('common_or_alternative_name')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '2': utils.reverse_force_list(value.get('source_of_taxonomic_identification')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('public_note')),
    }
