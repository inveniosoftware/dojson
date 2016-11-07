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


@to_marc21_liberal_authority.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'materials_specified': '3',
        'content_type_term': 'a',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'content_type_code': 'b',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        '2': value.get('source'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('348', '^format_of_notated_music$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_format_of_notated_music(self, key, value):
    """Reverse - Format of Notated Music."""
    field_map = {
        'materials_specified': '3',
        'format_of_notated_music_term': 'a',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'format_of_notated_music_code': 'b',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('360', '^complex_see_also_reference_subject$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_complex_see_also_reference_subject(self, key, value):
    """Reverse - Complex See Also Reference-Subject."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'authority_record_control_number': '0',
        'linkage': '6',
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
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
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('368', '^other_attributes_of_person_or_corporate_body$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_attributes_of_person_or_corporate_body(self, key, value):
    """Reverse - Other Attributes of Person or Corporate Body."""
    field_map = {
        'type_of_corporate_body': 'a',
        'title_of_person': 'd',
        'uniform_resource_identifier': 'u',
        'type_of_jurisdiction': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'other_designation': 'c',
        'end_period': 't',
        'start_period': 's',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_information': 'v',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('type_of_corporate_body')
        ),
        'd': utils.reverse_force_list(
            value.get('title_of_person')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'b': utils.reverse_force_list(
            value.get('type_of_jurisdiction')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('other_designation')
        ),
        't': value.get('end_period'),
        's': value.get('start_period'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('370', '^associated_place$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_place(self, key, value):
    """Reverse - Associated Place."""
    field_map = {
        'place_of_birth': 'a',
        'uniform_resource_identifier': 'u',
        'place_of_death': 'b',
        'linkage': '6',
        'place_of_origin_of_work': 'g',
        'field_link_and_sequence_number': '8',
        'other_associated_place': 'f',
        'associated_country': 'c',
        'end_period': 't',
        'start_period': 's',
        'place_of_residence_headquarters': 'e',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('place_of_birth'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'b': value.get('place_of_death'),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        't': value.get('end_period'),
        's': value.get('start_period'),
        'e': utils.reverse_force_list(
            value.get('place_of_residence_headquarters')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('371', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    field_map = {
        'address': 'a',
        'country': 'd',
        'uniform_resource_identifier': 'u',
        'relator_code': '4',
        'public_note': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'intermediate_jurisdiction': 'c',
        'end_period': 't',
        'start_period': 's',
        'postal_code': 'e',
        'source_of_information': 'v',
        'electronic_mail_address': 'm',
        'city': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        'd': value.get('country'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('intermediate_jurisdiction'),
        't': value.get('end_period'),
        's': value.get('start_period'),
        'e': value.get('postal_code'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        'b': value.get('city'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('372', '^field_of_activity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_field_of_activity(self, key, value):
    """Reverse - Field of Activity."""
    field_map = {
        'field_of_activity': 'a',
        'start_period': 's',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('field_of_activity')
        ),
        's': value.get('start_period'),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('373', '^associated_group$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_group(self, key, value):
    """Reverse - Associated Group."""
    field_map = {
        'associated_group': 'a',
        'start_period': 's',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('associated_group')
        ),
        's': value.get('start_period'),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('374', '^occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_occupation(self, key, value):
    """Reverse - Occupation."""
    field_map = {
        'occupation': 'a',
        'start_period': 's',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('occupation')
        ),
        's': value.get('start_period'),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('375', '^gender$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_gender(self, key, value):
    """Reverse - Gender."""
    field_map = {
        'gender': 'a',
        'start_period': 's',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'source_of_information': 'v',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('gender')
        ),
        's': value.get('start_period'),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('376', '^family_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_family_information(self, key, value):
    """Reverse - Family Information."""
    field_map = {
        'source_of_information': 'v',
        'start_period': 's',
        'type_of_family': 'a',
        'hereditary_title': 'c',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'name_of_prominent_member': 'b',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        's': value.get('start_period'),
        'a': utils.reverse_force_list(
            value.get('type_of_family')
        ),
        'c': utils.reverse_force_list(
            value.get('hereditary_title')
        ),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('name_of_prominent_member')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    indicator_map2 = {"MARC language code": "_", "Source specified in $2": "7"}
    field_map = {
        'language_term': 'l',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'language_code': 'a',
        'source_of_code': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        '2': value.get('source_of_code'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code') and
        field_map.get('source_of_code') in order
        else indicator_map2.get(value.get('source_of_code'), value.get('source_of_code', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('378', '^fuller_form_of_personal_name$')
@utils.filter_values
def reverse_fuller_form_of_personal_name(self, key, value):
    """Reverse - Fuller Form of Personal Name."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'source_of_information': 'v',
        'linkage': '6',
        'fuller_form_of_personal_name': 'q',
        'uniform_resource_identifier': 'u',
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
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '6': value.get('linkage'),
        'q': value.get('fuller_form_of_personal_name'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('380', '^form_of_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'linkage': '6',
        'form_of_work': 'a',
        'source_of_term': '2',
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
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'other_distinguishing_characteristic': 'a',
        'uniform_resource_identifier': 'u',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {"Medium of performance": "0", "No information provided": "_", "Partial medium of performance": "1"}
    field_map = {
        'medium_of_performance': 'a',
        'doubling_instrument': 'd',
        'soloist': 'b',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'alternative_medium_of_performance': 'p',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'total_number_of_performers': 's',
        'total_number_of_ensembles': 't',
        'field_link_and_sequence_number': '8',
        'number_of_ensembles_of_the_same_type': 'e',
        'note': 'v',
        'number_of_performers_of_the_same_medium': 'n',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        's': value.get('total_number_of_performers'),
        't': value.get('total_number_of_ensembles'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        '2': value.get('source_of_term'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('383', '^numeric_designation_of_musical_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    field_map = {
        'serial_number': 'a',
        'thematic_index_code': 'd',
        'thematic_index_number': 'c',
        'field_link_and_sequence_number': '8',
        'opus_number': 'b',
        'linkage': '6',
        'publisher_associated_with_opus_number': 'e',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        'd': value.get('thematic_index_code'),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        '6': value.get('linkage'),
        'e': value.get('publisher_associated_with_opus_number'),
        '2': value.get('source'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'key': 'a',
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
        'a': value.get('key'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'materials_specified': '3',
        'demographic_group_code': 'n',
        'audience_term': 'a',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'audience_code': 'b',
        'demographic_group_term': 'm',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'n': value.get('demographic_group_code'),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        'm': value.get('demographic_group_term'),
        '2': value.get('source'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('386', '^creator_contributor_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    field_map = {
        'materials_specified': '3',
        'demographic_group_code': 'n',
        'creator_contributor_term': 'a',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'creator_contributor_code': 'b',
        'demographic_group_term': 'm',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'n': value.get('demographic_group_code'),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        'm': value.get('demographic_group_term'),
        '2': value.get('source'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    indicator_map1 = {"Creation of aggregate work": "2", "Creation of work": "1", "No information provided": "_"}
    field_map = {
        'materials_specified': '3',
        'time_period_of_creation_term': 'a',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), value.get('type_of_time_period', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
