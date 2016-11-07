# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        'a': 'content_type_term',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'b': 'content_type_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        'a': 'format_of_notated_music_term',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'b': 'format_of_notated_music_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('complex_see_also_reference_subject', '^360..')
@utils.for_each_value
@utils.filter_values
def complex_see_also_reference_subject(self, key, value):
    """Complex See Also Reference-Subject."""
    field_map = {
        'a': 'heading_referred_to',
        '6': 'linkage',
        'i': 'explanatory_text',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('other_attributes_of_person_or_corporate_body', '^368..')
@utils.for_each_value
@utils.filter_values
def other_attributes_of_person_or_corporate_body(self, key, value):
    """Other Attributes of Person or Corporate Body."""
    field_map = {
        'c': 'other_designation',
        'd': 'title_of_person',
        '0': 'authority_record_control_number_or_standard_number',
        's': 'start_period',
        't': 'end_period',
        '2': 'source',
        'v': 'source_of_information',
        'a': 'type_of_corporate_body',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
        '8': 'field_link_and_sequence_number',
        'b': 'type_of_jurisdiction',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'other_designation': utils.force_list(
            value.get('c')
        ),
        'title_of_person': utils.force_list(
            value.get('d')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'source': value.get('2'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'type_of_corporate_body': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_jurisdiction': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'e': 'place_of_residence_headquarters',
        'c': 'associated_country',
        '0': 'record_control_number',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'g': 'place_of_origin_of_work',
        'f': 'other_associated_place',
        'v': 'source_of_information',
        'a': 'place_of_birth',
        '6': 'linkage',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'b': 'place_of_death',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'place_of_residence_headquarters': utils.force_list(
            value.get('e')
        ),
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'place_of_birth': value.get('a'),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_of_death': value.get('b'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('address', '^371..')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    field_map = {
        'e': 'postal_code',
        'c': 'intermediate_jurisdiction',
        'd': 'country',
        'b': 'city',
        's': 'start_period',
        't': 'end_period',
        'm': 'electronic_mail_address',
        'a': 'address',
        '6': 'linkage',
        'z': 'public_note',
        'u': 'uniform_resource_identifier',
        '8': 'field_link_and_sequence_number',
        'v': 'source_of_information',
        '4': 'relator_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'postal_code': value.get('e'),
        'intermediate_jurisdiction': value.get('c'),
        'country': value.get('d'),
        'city': value.get('b'),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'address': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('field_of_activity', '^372..')
@utils.for_each_value
@utils.filter_values
def field_of_activity(self, key, value):
    """Field of Activity."""
    field_map = {
        'a': 'field_of_activity',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        't': 'end_period',
        '0': 'record_control_number',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_of_activity': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'end_period': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('associated_group', '^373..')
@utils.for_each_value
@utils.filter_values
def associated_group(self, key, value):
    """Associated Group."""
    field_map = {
        'a': 'associated_group',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        't': 'end_period',
        '0': 'record_control_number',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'associated_group': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'end_period': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('occupation', '^374..')
@utils.for_each_value
@utils.filter_values
def occupation(self, key, value):
    """Occupation."""
    field_map = {
        'a': 'occupation',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        't': 'end_period',
        '0': 'record_control_number',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'occupation': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'end_period': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('gender', '^375..')
@utils.for_each_value
@utils.filter_values
def gender(self, key, value):
    """Gender."""
    field_map = {
        'a': 'gender',
        '6': 'linkage',
        '2': 'source_of_term',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        't': 'end_period',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'gender': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'end_period': value.get('t'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('family_information', '^376..')
@utils.for_each_value
@utils.filter_values
def family_information(self, key, value):
    """Family Information."""
    field_map = {
        'a': 'type_of_family',
        '6': 'linkage',
        'c': 'hereditary_title',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        't': 'end_period',
        '0': 'record_control_number',
        'b': 'name_of_prominent_member',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'type_of_family': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'hereditary_title': utils.force_list(
            value.get('c')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'end_period': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'name_of_prominent_member': utils.force_list(
            value.get('b')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {"7": "Source specified in $2", "_": "MARC language code"}
    field_map = {
        'a': 'language_code',
        '6': 'linkage',
        'l': 'language_term',
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_code')

    record_dict = {
        '__order__': order if len(order) else None,
        'language_code': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_code': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('fuller_form_of_personal_name', '^378..')
@utils.filter_values
def fuller_form_of_personal_name(self, key, value):
    """Fuller Form of Personal Name."""
    field_map = {
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        'q': 'fuller_form_of_personal_name',
        'v': 'source_of_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'fuller_form_of_personal_name': value.get('q'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        'a': 'form_of_work',
        '6': 'linkage',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'a': 'other_distinguishing_characteristic',
        '6': 'linkage',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        '0': 'record_control_number',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('medium_of_performance', '^382..')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {"0": "Medium of performance", "1": "Partial medium of performance", "_": "No information provided"}
    field_map = {
        'e': 'number_of_ensembles_of_the_same_type',
        'b': 'soloist',
        'd': 'doubling_instrument',
        'p': 'alternative_medium_of_performance',
        's': 'total_number_of_performers',
        't': 'total_number_of_ensembles',
        '0': 'authority_record_control_number_or_standard_number',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        'a': 'medium_of_performance',
        '6': 'linkage',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'v': 'note',
        'n': 'number_of_performers_of_the_same_medium',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'number_of_ensembles_of_the_same_type': utils.force_list(
            value.get('e')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'total_number_of_performers': value.get('s'),
        'total_number_of_ensembles': value.get('t'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': value.get('r'),
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'a': 'serial_number',
        '6': 'linkage',
        'd': 'thematic_index_code',
        'c': 'thematic_index_number',
        'b': 'opus_number',
        '8': 'field_link_and_sequence_number',
        'e': 'publisher_associated_with_opus_number',
        '2': 'source',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'thematic_index_code': value.get('d'),
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'publisher_associated_with_opus_number': value.get('e'),
        'source': value.get('2'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('key', '^384..')
@utils.filter_values
def key(self, key, value):
    """Key."""
    field_map = {
        'a': 'key',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'key': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'a': 'audience_term',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'm': 'demographic_group_term',
        'b': 'audience_code',
        'n': 'demographic_group_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'demographic_group_term': value.get('m'),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_code': value.get('n'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'a': 'creator_contributor_term',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        'm': 'demographic_group_term',
        'b': 'creator_contributor_code',
        'n': 'demographic_group_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'demographic_group_term': value.get('m'),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_code': value.get('n'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('time_period_of_creation', '^388..')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {"1": "Creation of work", "2": "Creation of aggregate work", "_": "No information provided"}
    field_map = {
        'a': 'time_period_of_creation_term',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_time_period')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'type_of_time_period': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
