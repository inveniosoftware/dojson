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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('700', '^added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_personal_name(self, key, value):
    """Reverse - Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'fuller_form_of_name': 'q',
        'date_of_a_work': 'f',
        'authority_record_control_number_or_standard_number': '0',
        'medium': 'h',
        'materials_specified': '3',
        'number_of_part_section_of_a_work': 'n',
        'dates_associated_with_a_name': 'd',
        'version': 's',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'personal_name': 'a',
        'relationship_information': 'i',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'numeration': 'b',
        'affiliation': 'u',
        'attribution_qualifier': 'j',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'relator_code': '4',
        'title_of_a_work': 't',
        'titles_and_other_words_associated_with_a_name': 'c',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('fuller_form_of_name'),
        'f': value.get('date_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': value.get('medium'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'd': value.get('dates_associated_with_a_name'),
        's': value.get('version'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('personal_name'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': value.get('numeration'),
        'u': value.get('affiliation'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'o': value.get('arranged_statement_for_music'),
        '5': value.get('institution_to_which_field_applies'),
        'x': value.get('international_standard_serial_number'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        't': value.get('title_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'r': value.get('key_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), value.get('type_of_added_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('710', '^added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_corporate_name(self, key, value):
    """Reverse - Added Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'version': 's',
        'date_of_a_work': 'f',
        'authority_record_control_number_or_standard_number': '0',
        'medium': 'h',
        'materials_specified': '3',
        'number_of_part_section_meeting': 'n',
        'date_of_meeting_or_treaty_signing': 'd',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'relationship_information': 'i',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'subordinate_unit': 'b',
        'affiliation': 'u',
        'form_subheading': 'k',
        'arranged_statement_for_music': 'o',
        'institution_to_which_field_applies': '5',
        'relator_code': '4',
        'location_of_meeting': 'c',
        'name_of_part_section_of_a_work': 'p',
        'title_of_a_work': 't',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('version'),
        'f': value.get('date_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': value.get('medium'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'u': value.get('affiliation'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'o': value.get('arranged_statement_for_music'),
        '5': value.get('institution_to_which_field_applies'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), value.get('type_of_added_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('711', '^added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_meeting_name(self, key, value):
    """Reverse - Added Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'version': 's',
        'date_of_a_work': 'f',
        'authority_record_control_number_or_standard_number': '0',
        'medium': 'h',
        'materials_specified': '3',
        'number_of_part_section_meeting': 'n',
        'date_of_meeting': 'd',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'relationship_information': 'i',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'subordinate_unit': 'e',
        'affiliation': 'u',
        'relator_term': 'j',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'institution_to_which_field_applies': '5',
        'relator_code': '4',
        'title_of_a_work': 't',
        'location_of_meeting': 'c',
        'name_of_part_section_of_a_work': 'p',
        'form_subheading': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('version'),
        'f': value.get('date_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': value.get('medium'),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'd': value.get('date_of_meeting'),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'u': value.get('affiliation'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '5': value.get('institution_to_which_field_applies'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        't': value.get('title_of_a_work'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), value.get('type_of_added_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('720', '^added_entry_uncontrolled_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_name(self, key, value):
    """Reverse - Added Entry-Uncontrolled Name."""
    indicator_map1 = {"Not specified": "_", "Other": "2", "Personal": "1"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'name': 'a',
        'relator_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_name', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'a': value.get('name'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_name'), value.get('type_of_name', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('730', '^added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uniform_title(self, key, value):
    """Reverse - Added Entry-Uniform Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'name_of_part_section_of_a_work': 'p',
        'date_of_a_work': 'f',
        'medium_of_performance_for_music': 'm',
        'authority_record_control_number_or_standard_number': '0',
        'medium': 'h',
        'materials_specified': '3',
        'form_subheading': 'k',
        'arranged_statement_for_music': 'o',
        'number_of_part_section_of_a_work': 'n',
        'date_of_treaty_signing': 'd',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'miscellaneous_information': 'g',
        'title_of_a_work': 't',
        'language_of_a_work': 'l',
        'international_standard_serial_number': 'x',
        'uniform_title': 'a',
        'key_for_music': 'r',
        'relationship_information': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': value.get('medium'),
        '3': value.get('materials_specified'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '5': value.get('institution_to_which_field_applies'),
        's': value.get('version'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        't': value.get('title_of_a_work'),
        'l': value.get('language_of_a_work'),
        'x': value.get('international_standard_serial_number'),
        'a': value.get('uniform_title'),
        'r': value.get('key_for_music'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), value.get('type_of_added_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('740', '^added_entry_uncontrolled_related_analytical_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_uncontrolled_related_analytical_title(self, key, value):
    """Reverse - Added Entry-Uncontrolled Related/Analytical Title."""
    indicator_map1 = {str(x): str(x) for x in range(10)}
    indicator_map2 = {"Analytical entry": "2", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'medium': 'h',
        'name_of_part_section_of_a_work': 'p',
        'number_of_part_section_of_a_work': 'n',
        'uncontrolled_related_analytical_title': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'h': value.get('medium'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'a': value.get('uncontrolled_related_analytical_title'),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_added_entry'), value.get('type_of_added_entry', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('751', '^added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_geographic_name(self, key, value):
    """Reverse - Added Entry-Geographic Name."""
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'relator_term': 'e',
        'authority_record_control_number': '0',
        'relator_code': '4',
        'field_link_and_sequence_number': '8',
        'source_of_heading_or_term': '2',
        'geographic_name': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        'a': value.get('geographic_name'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('752', '^added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Added Entry-Hierarchical Place Name."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'city': 'd',
        'city_subsection': 'f',
        'first_order_political_jurisdiction': 'b',
        'authority_record_control_number': '0',
        'extraterrestrial_area': 'h',
        'source_of_heading_or_term': '2',
        'intermediate_political_jurisdiction': 'c',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'country_or_larger_entity': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('city'),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        '2': value.get('source_of_heading_or_term'),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('753', '^system_details_access_to_computer_files$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_access_to_computer_files(self, key, value):
    """Reverse - System Details Access to Computer Files."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'programming_language': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'operating_system': 'c',
        'make_and_model_of_machine': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('programming_language'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source_of_term'),
        'c': value.get('operating_system'),
        'a': value.get('make_and_model_of_machine'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('754', '^added_entry_taxonomic_identification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_added_entry_taxonomic_identification(self, key, value):
    """Reverse - Added Entry-Taxonomic Identification."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'common_or_alternative_name': 'd',
        'non_public_note': 'x',
        'authority_record_control_number': '0',
        'public_note': 'z',
        'source_of_taxonomic_identification': '2',
        'taxonomic_category': 'c',
        'taxonomic_name': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('common_or_alternative_name')
        ),
        'x': utils.reverse_force_list(
            value.get('non_public_note')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('source_of_taxonomic_identification'),
        'c': utils.reverse_force_list(
            value.get('taxonomic_category')
        ),
        'a': utils.reverse_force_list(
            value.get('taxonomic_name')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
