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


@to_marc21.over('700', '^added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_personal_name(self, key, value):
    """Reverse - Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'personal_name': 'a',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'form_subheading': 'k',
        'attribution_qualifier': 'j',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'number_of_part_section_of_a_work': 'n',
        'titles_and_other_words_associated_with_a_name': 'c',
        'arranged_statement_for_music': 'o',
        'dates_associated_with_a_name': 'd',
        'linkage': '6',
        'relationship_information': 'i',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'international_standard_serial_number': 'x',
        'version': 's',
        'relator_term': 'e',
        'institution_to_which_field_applies': '5',
        'numeration': 'b',
        'materials_specified': '3',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'affiliation': 'u',
        'fuller_form_of_name': 'q',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('personal_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': value.get('dates_associated_with_a_name'),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': value.get('international_standard_serial_number'),
        's': value.get('version'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'b': value.get('numeration'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': value.get('affiliation'),
        'q': value.get('fuller_form_of_name'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('710', '^added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_corporate_name(self, key, value):
    """Reverse - Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_a_work': 'f',
        'form_subheading': 'k',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'number_of_part_section_meeting': 'n',
        'location_of_meeting': 'c',
        'arranged_statement_for_music': 'o',
        'date_of_meeting_or_treaty_signing': 'd',
        'linkage': '6',
        'relationship_information': 'i',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'international_standard_serial_number': 'x',
        'version': 's',
        'relator_term': 'e',
        'institution_to_which_field_applies': '5',
        'subordinate_unit': 'b',
        'materials_specified': '3',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'affiliation': 'u',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': value.get('international_standard_serial_number'),
        's': value.get('version'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': value.get('affiliation'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('711', '^added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_meeting_name(self, key, value):
    """Reverse - Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_a_work': 'f',
        'form_subheading': 'k',
        'relator_term': 'j',
        'number_of_part_section_meeting': 'n',
        'location_of_meeting': 'c',
        'miscellaneous_information': 'g',
        'date_of_meeting': 'd',
        'linkage': '6',
        'relationship_information': 'i',
        'medium': 'h',
        'authority_record_control_number_or_standard_number': '0',
        'international_standard_serial_number': 'x',
        'version': 's',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'institution_to_which_field_applies': '5',
        'materials_specified': '3',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'e',
        'affiliation': 'u',
        'language_of_a_work': 'l',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': value.get('date_of_meeting'),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': value.get('international_standard_serial_number'),
        's': value.get('version'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '5': value.get('institution_to_which_field_applies'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'u': value.get('affiliation'),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('720', '^added_entry_uncontrolled_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_name(self, key, value):
    """Reverse - Added Entry-Uncontrolled Name."""
    indicator_map1 = {"Not specified": "_", "Other": "2", "Personal": "1"}
    field_map = {
        'name': 'a',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'linkage': '6',
        'relator_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_name'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('730', '^added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uniform_title(self, key, value):
    """Reverse - Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'uniform_title': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'international_standard_serial_number': 'x',
        'date_of_a_work': 'f',
        'form_subheading': 'k',
        'title_of_a_work': 't',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'version': 's',
        'number_of_part_section_of_a_work': 'n',
        'key_for_music': 'r',
        'miscellaneous_information': 'g',
        'name_of_part_section_of_a_work': 'p',
        'language_of_a_work': 'l',
        'date_of_treaty_signing': 'd',
        'linkage': '6',
        'relationship_information': 'i',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uniform_title'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': value.get('international_standard_serial_number'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        't': value.get('title_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
        '5': value.get('institution_to_which_field_applies'),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('version'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'l': value.get('language_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('740', '^added_entry_uncontrolled_related_analytical_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Reverse - Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'uncontrolled_related_analytical_title': 'a',
        'field_link_and_sequence_number': '8',
        'number_of_part_section_of_a_work': 'n',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'name_of_part_section_of_a_work': 'p',
        'medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('uncontrolled_related_analytical_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'h': value.get('medium'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('751', '^added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_geographic_name(self, key, value):
    """Reverse - Added Entry-Geographic Name."""
    field_map = {
        'geographic_name': 'a',
        'authority_record_control_number': '0',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'linkage': '6',
        'materials_specified': '3',
        'relator_code': '4',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('752', '^added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Added Entry-Hierarchical Place Name."""
    field_map = {
        'country_or_larger_entity': 'a',
        'authority_record_control_number': '0',
        'extraterrestrial_area': 'h',
        'intermediate_political_jurisdiction': 'c',
        'source_of_heading_or_term': '2',
        'field_link_and_sequence_number': '8',
        'city': 'd',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'linkage': '6',
        'first_order_political_jurisdiction': 'b',
        'city_subsection': 'f',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        '2': value.get('source_of_heading_or_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('city'),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        '6': value.get('linkage'),
        'b': value.get('first_order_political_jurisdiction'),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('753', '^system_details_access_to_computer_files$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_access_to_computer_files(self, key, value):
    """Reverse - System Details Access to Computer Files."""
    field_map = {
        'make_and_model_of_machine': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'operating_system': 'c',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'programming_language': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('make_and_model_of_machine'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'c': value.get('operating_system'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('programming_language'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('754', '^added_entry_taxonomic_identification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_taxonomic_identification(self, key, value):
    """Reverse - Added Entry-Taxonomic Identification."""
    field_map = {
        'taxonomic_name': 'a',
        'authority_record_control_number': '0',
        'taxonomic_category': 'c',
        'source_of_taxonomic_identification': '2',
        'field_link_and_sequence_number': '8',
        'common_or_alternative_name': 'd',
        'non_public_note': 'x',
        'linkage': '6',
        'public_note': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('taxonomic_name')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'c': utils.reverse_force_list(
            value.get('taxonomic_category')
        ),
        '2': value.get('source_of_taxonomic_identification'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('common_or_alternative_name')
        ),
        'x': utils.reverse_force_list(
            value.get('non_public_note')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
