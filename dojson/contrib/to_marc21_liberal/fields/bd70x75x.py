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
        'medium': 'h',
        'numeration': 'b',
        'relator_code': '4',
        'titles_and_other_words_associated_with_a_name': 'c',
        'materials_specified': '3',
        'number_of_part_section_of_a_work': 'n',
        'name_of_part_section_of_a_work': 'p',
        'medium_of_performance_for_music': 'm',
        'date_of_a_work': 'f',
        'personal_name': 'a',
        'version': 's',
        'title_of_a_work': 't',
        'key_for_music': 'r',
        'fuller_form_of_name': 'q',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'institution_to_which_field_applies': '5',
        'attribution_qualifier': 'j',
        'international_standard_serial_number': 'x',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'relator_term': 'e',
        'dates_associated_with_a_name': 'd',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'affiliation': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        'b': value.get('numeration'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('personal_name'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
        'q': value.get('fuller_form_of_name'),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'x': value.get('international_standard_serial_number'),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'u': value.get('affiliation'),
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
        'medium': 'h',
        'subordinate_unit': 'b',
        'relator_code': '4',
        'location_of_meeting': 'c',
        'materials_specified': '3',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'medium_of_performance_for_music': 'm',
        'date_of_a_work': 'f',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'title_of_a_work': 't',
        'key_for_music': 'r',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'institution_to_which_field_applies': '5',
        'international_standard_serial_number': 'x',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'relator_term': 'e',
        'date_of_meeting_or_treaty_signing': 'd',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'affiliation': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'x': value.get('international_standard_serial_number'),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'u': value.get('affiliation'),
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
        'medium': 'h',
        'relator_code': '4',
        'location_of_meeting': 'c',
        'materials_specified': '3',
        'number_of_part_section_meeting': 'n',
        'name_of_part_section_of_a_work': 'p',
        'date_of_a_work': 'f',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'version': 's',
        'title_of_a_work': 't',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'institution_to_which_field_applies': '5',
        'relator_term': 'j',
        'international_standard_serial_number': 'x',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'subordinate_unit': 'e',
        'date_of_meeting': 'd',
        'field_link_and_sequence_number': '8',
        'relationship_information': 'i',
        'affiliation': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('medium'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'f': value.get('date_of_a_work'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'x': value.get('international_standard_serial_number'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'u': value.get('affiliation'),
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
        'name': 'a',
        'relator_code': '4',
        'relator_term': 'e',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_name', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('name'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'medium': 'h',
        'date_of_a_work': 'f',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'materials_specified': '3',
        'number_of_part_section_of_a_work': 'n',
        'institution_to_which_field_applies': '5',
        'name_of_part_section_of_a_work': 'p',
        'international_standard_serial_number': 'x',
        'medium_of_performance_for_music': 'm',
        'arranged_statement_for_music': 'o',
        'miscellaneous_information': 'g',
        'language_of_a_work': 'l',
        'date_of_treaty_signing': 'd',
        'field_link_and_sequence_number': '8',
        'uniform_title': 'a',
        'relationship_information': 'i',
        'version': 's',
        'title_of_a_work': 't',
        'key_for_music': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'f': value.get('date_of_a_work'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '3': value.get('materials_specified'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '5': value.get('institution_to_which_field_applies'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'x': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'o': value.get('arranged_statement_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'l': value.get('language_of_a_work'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        's': value.get('version'),
        't': value.get('title_of_a_work'),
        'r': value.get('key_for_music'),
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
        'medium': 'h',
        'number_of_part_section_of_a_work': 'n',
        'field_link_and_sequence_number': '8',
        'uncontrolled_related_analytical_title': 'a',
        'institution_to_which_field_applies': '5',
        'name_of_part_section_of_a_work': 'p',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['nonfiling_characters', 'type_of_added_entry'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('uncontrolled_related_analytical_title'),
        '5': value.get('institution_to_which_field_applies'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
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
        'relator_code': '4',
        'authority_record_control_number': '0',
        'materials_specified': '3',
        'geographic_name': 'a',
        'field_link_and_sequence_number': '8',
        'relator_term': 'e',
        'source_of_heading_or_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('geographic_name'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '2': value.get('source_of_heading_or_term'),
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
        'extraterrestrial_area': 'h',
        'first_order_political_jurisdiction': 'b',
        'city_subsection': 'f',
        'authority_record_control_number': '0',
        'intermediate_political_jurisdiction': 'c',
        'field_link_and_sequence_number': '8',
        'country_or_larger_entity': 'a',
        'city': 'd',
        'other_nonjurisdictional_geographic_region_and_feature': 'g',
        'source_of_heading_or_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'd': value.get('city'),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        '2': value.get('source_of_heading_or_term'),
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
        'programming_language': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'operating_system': 'c',
        'field_link_and_sequence_number': '8',
        'make_and_model_of_machine': 'a',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('programming_language'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'c': value.get('operating_system'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('make_and_model_of_machine'),
        '2': value.get('source_of_term'),
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
        'public_note': 'z',
        'authority_record_control_number': '0',
        'taxonomic_category': 'c',
        'field_link_and_sequence_number': '8',
        'taxonomic_name': 'a',
        'common_or_alternative_name': 'd',
        'non_public_note': 'x',
        'source_of_taxonomic_identification': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'c': utils.reverse_force_list(
            value.get('taxonomic_category')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('taxonomic_name')
        ),
        'd': utils.reverse_force_list(
            value.get('common_or_alternative_name')
        ),
        'x': utils.reverse_force_list(
            value.get('non_public_note')
        ),
        '2': value.get('source_of_taxonomic_identification'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
