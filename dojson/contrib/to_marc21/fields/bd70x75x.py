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
        'medium': 'h',
        'linkage': '6',
        'personal_name': 'a',
        'language_of_a_work': 'l',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'version': 's',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_of_a_work': 'n',
        'relator_code': '4',
        'relator_term': 'e',
        'affiliation': 'u',
        'international_standard_serial_number': 'x',
        'arranged_statement_for_music': 'o',
        'fuller_form_of_name': 'q',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'dates_associated_with_a_name': 'd',
        'attribution_qualifier': 'j',
        'form_subheading': 'k',
        'titles_and_other_words_associated_with_a_name': 'c',
        'key_for_music': 'r',
        'numeration': 'b',
        'relationship_information': 'i',
        'name_of_part_section_of_a_work': 'p',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_personal_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_personal_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_added_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('personal_name'),
        'l': value.get('language_of_a_work'),
        '5': value.get('institution_to_which_field_applies'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'u': value.get('affiliation'),
        'x': value.get('international_standard_serial_number'),
        'o': value.get('arranged_statement_for_music'),
        'q': value.get('fuller_form_of_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        'd': value.get('dates_associated_with_a_name'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'r': value.get('key_for_music'),
        'b': value.get('numeration'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
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
    field_map = {
        'medium': 'h',
        'linkage': '6',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'language_of_a_work': 'l',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'version': 's',
        'medium_of_performance_for_music': 'm',
        'number_of_part_section_meeting': 'n',
        'relator_code': '4',
        'relator_term': 'e',
        'affiliation': 'u',
        'international_standard_serial_number': 'x',
        'arranged_statement_for_music': 'o',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'date_of_meeting_or_treaty_signing': 'd',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
        'key_for_music': 'r',
        'subordinate_unit': 'b',
        'relationship_information': 'i',
        'name_of_part_section_of_a_work': 'p',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_corporate_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_corporate_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_added_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'l': value.get('language_of_a_work'),
        '5': value.get('institution_to_which_field_applies'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'u': value.get('affiliation'),
        'x': value.get('international_standard_serial_number'),
        'o': value.get('arranged_statement_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'r': value.get('key_for_music'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
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
    field_map = {
        'medium': 'h',
        'linkage': '6',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'subordinate_unit': 'e',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'version': 's',
        'number_of_part_section_meeting': 'n',
        'relator_code': '4',
        'language_of_a_work': 'l',
        'affiliation': 'u',
        'international_standard_serial_number': 'x',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'date_of_meeting': 'd',
        'relator_term': 'j',
        'form_subheading': 'k',
        'location_of_meeting': 'c',
        'relationship_information': 'i',
        'name_of_part_section_of_a_work': 'p',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_meeting_name_entry_element'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_meeting_name_entry_element'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_added_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        's': value.get('version'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'l': value.get('language_of_a_work'),
        'u': value.get('affiliation'),
        'x': value.get('international_standard_serial_number'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        'd': value.get('date_of_meeting'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
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
        'linkage': '6',
        'relator_code': '4',
        'name': 'a',
        'relator_term': 'e',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_name'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_name'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'a': value.get('name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'medium': 'h',
        'version': 's',
        'linkage': '6',
        'uniform_title': 'a',
        'institution_to_which_field_applies': '5',
        'miscellaneous_information': 'g',
        'date_of_a_work': 'f',
        'materials_specified': '3',
        'title_of_a_work': 't',
        'date_of_treaty_signing': 'd',
        'medium_of_performance_for_music': 'm',
        'form_subheading': 'k',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'key_for_music': 'r',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'relationship_information': 'i',
        'arranged_statement_for_music': 'o',
        'international_standard_serial_number': 'x',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_added_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        's': value.get('version'),
        '6': value.get('linkage'),
        'a': value.get('uniform_title'),
        '5': value.get('institution_to_which_field_applies'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'f': value.get('date_of_a_work'),
        '3': value.get('materials_specified'),
        't': value.get('title_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'r': value.get('key_for_music'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'o': value.get('arranged_statement_for_music'),
        'x': value.get('international_standard_serial_number'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('740', '^added_entry_uncontrolled_related_analytical_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_related_analytical_title(
        self, key, value):
    """Reverse - Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'uncontrolled_related_analytical_title': 'a',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('nonfiling_characters'), '7') != '7':
        try:
            order.remove(field_map.get('nonfiling_characters'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_added_entry'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_added_entry'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'a': value.get('uncontrolled_related_analytical_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), '_'),
    }


@to_marc21.over('751', '^added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_geographic_name(self, key, value):
    """Reverse - Added Entry-Geographic Name."""
    field_map = {
        'source_of_heading_or_term': '2',
        'relator_code': '4',
        'geographic_name': 'a',
        'relator_term': 'e',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'materials_specified': '3',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'a': value.get('geographic_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
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
        'source_of_heading_or_term': '2',
        'extraterrestrial_area': 'h',
        'intermediate_political_jurisdiction': 'c',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'country_or_larger_entity': 'a',
        'first_order_political_jurisdiction': 'b',
        'field_link_and_sequence_number': '8',
        'city': 'd',
        'linkage': '6',
        'city_subsection': 'f',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_heading_or_term'),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('city'),
        '6': value.get('linkage'),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
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
        'source_of_term': '2',
        'operating_system': 'c',
        'make_and_model_of_machine': 'a',
        'programming_language': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_term'),
        'c': value.get('operating_system'),
        'a': value.get('make_and_model_of_machine'),
        'b': value.get('programming_language'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('754', '^added_entry_taxonomic_identification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_taxonomic_identification(self, key, value):
    """Reverse - Added Entry-Taxonomic Identification."""
    field_map = {
        'source_of_taxonomic_identification': '2',
        'taxonomic_category': 'c',
        'public_note': 'z',
        'taxonomic_name': 'a',
        'field_link_and_sequence_number': '8',
        'common_or_alternative_name': 'd',
        'linkage': '6',
        'non_public_note': 'x',
        'authority_record_control_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_taxonomic_identification'),
        'c': utils.reverse_force_list(
            value.get('taxonomic_category')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'a': utils.reverse_force_list(
            value.get('taxonomic_name')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('common_or_alternative_name')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('non_public_note')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
