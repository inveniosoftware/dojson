# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('700', '^added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_personal_name(self, key, value):
    """Reverse - Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'authority_record_control_number': '0',
        'materials_specified': '3',
        'relator_code': '4',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'personal_name': 'a',
        'numeration': 'b',
        'titles_and_other_words_associated_with_a_name': 'c',
        'dates_associated_with_a_name': 'd',
        'relator_term': 'e',
        'date_of_a_work': 'f',
        'medium': 'h',
        'relationship_information': 'i',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'language_or_a_work': 'l',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'arranged_statement_for_music': 'o',
        'name_of_part_section_of_a_work': 'p',
        'version': 's',
        'key_for_music': 'r',
        'affiliation': 'u',
        'title_of_a_work': 't',
        'international_standard_serial_number': 'x',
        'type_of_personal_name_entry_element': None,
        'type_of_added_entry': None
    }

    ind1 = indicator_map1.get(value.get('type_of_personal_name_entry_element', '_'))
    ind2 = indicator_map2.get(value.get('type_of_added_entry', '_'))
    order = utils.map_order(field_map, value)

    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('personal_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'b': value.get('numeration'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        '$ind1': ind1,
        '$ind2': ind2,
        '__order__': tuple(order) if len(order) else None
    }


@to_marc21.over('710', '^added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_corporate_name(self, key, value):
    """Reverse - Added Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('711', '^added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_meeting_name(self, key, value):
    """Reverse - Added Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('720', '^added_entry_uncontrolled_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_name(self, key, value):
    """Reverse - Added Entry-Uncontrolled Name."""
    indicator_map1 = {"Not specified": "_", "Other": "2", "Personal": "1"}
    return {
        'a': value.get('name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_name'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('730', '^added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uniform_title(self, key, value):
    """Reverse - Added Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    return {
        'a': value.get('uniform_title'),
        'x': value.get('international_standard_serial_number'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        'r': value.get('key_for_music'),
        '5': value.get('institution_to_which_field_applies'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('740', '^added_entry_uncontrolled_related_analytical_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_related_analytical_title(
        self,
        key,
        value):
    """Reverse - Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {
        "No nonfiling characters": "0",
        "Number of nonfiling characters": "8"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    return {
        'a': value.get('uncontrolled_related_analytical_title'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('751', '^added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_geographic_name(self, key, value):
    """Reverse - Added Entry-Geographic Name."""
    return {
        'a': value.get('geographic_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('752', '^added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Added Entry-Hierarchical Place Name."""
    return {
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        'd': value.get('city'),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('753', '^system_details_access_to_computer_files$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_access_to_computer_files(self, key, value):
    """Reverse - System Details Access to Computer Files."""
    return {
        'a': value.get('make_and_model_of_machine'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('operating_system'),
        'b': value.get('programming_language'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('754', '^added_entry_taxonomic_identification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_taxonomic_identification(self, key, value):
    """Reverse - Added Entry-Taxonomic Identification."""
    return {
        'a': utils.reverse_force_list(
            value.get('taxonomic_name')
        ),
        'x': utils.reverse_force_list(
            value.get('non_public_note')
        ),
        'c': utils.reverse_force_list(
            value.get('taxonomic_category')
        ),
        'd': utils.reverse_force_list(
            value.get('common_or_alternative_name')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '2': value.get('source_of_taxonomic_identification'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
