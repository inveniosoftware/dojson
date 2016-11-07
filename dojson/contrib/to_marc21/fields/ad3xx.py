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

from ..model import to_marc21_authority


@to_marc21_authority.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'linkage': '6',
        'content_type_code': 'b',
        'source': '2',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'content_type_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        '2': value.get('source'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('348', '^format_of_notated_music$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_format_of_notated_music(self, key, value):
    """Reverse - Format of Notated Music."""
    field_map = {
        'linkage': '6',
        'format_of_notated_music_code': 'b',
        'source_of_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'format_of_notated_music_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('360', '^complex_see_also_reference_subject$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_complex_see_also_reference_subject(self, key, value):
    """Reverse - Complex See Also Reference-Subject."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number': '0',
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('368', '^other_attributes_of_person_or_corporate_body$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_attributes_of_person_or_corporate_body(self, key, value):
    """Reverse - Other Attributes of Person or Corporate Body."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'other_designation': 'c',
        'linkage': '6',
        'source': '2',
        'start_period': 's',
        'field_link_and_sequence_number': '8',
        'type_of_jurisdiction': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'title_of_person': 'd',
        'end_period': 't',
        'source_of_information': 'v',
        'type_of_corporate_body': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': utils.reverse_force_list(
            value.get('other_designation')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        's': value.get('start_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('type_of_jurisdiction')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'd': utils.reverse_force_list(
            value.get('title_of_person')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_corporate_body')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('370', '^associated_place$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_place(self, key, value):
    """Reverse - Associated Place."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'associated_country': 'c',
        'linkage': '6',
        'place_of_residence_headquarters': 'e',
        'source_of_term': '2',
        'start_period': 's',
        'field_link_and_sequence_number': '8',
        'place_of_death': 'b',
        'source_of_information': 'v',
        'other_associated_place': 'f',
        'record_control_number': '0',
        'end_period': 't',
        'place_of_origin_of_work': 'g',
        'place_of_birth': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('place_of_residence_headquarters')
        ),
        '2': value.get('source_of_term'),
        's': value.get('start_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('place_of_death'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        't': value.get('end_period'),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        'a': value.get('place_of_birth'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('371', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'intermediate_jurisdiction': 'c',
        'linkage': '6',
        'postal_code': 'e',
        'start_period': 's',
        'field_link_and_sequence_number': '8',
        'city': 'b',
        'public_note': 'z',
        'electronic_mail_address': 'm',
        'country': 'd',
        'relator_code': '4',
        'end_period': 't',
        'source_of_information': 'v',
        'address': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': value.get('intermediate_jurisdiction'),
        '6': value.get('linkage'),
        'e': value.get('postal_code'),
        's': value.get('start_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('city'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        'd': value.get('country'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('372', '^field_of_activity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_field_of_activity(self, key, value):
    """Reverse - Field of Activity."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'start_period': 's',
        'source_of_term': '2',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'source_of_information': 'v',
        'field_of_activity': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('field_of_activity')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('373', '^associated_group$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_group(self, key, value):
    """Reverse - Associated Group."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'start_period': 's',
        'source_of_term': '2',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'source_of_information': 'v',
        'associated_group': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('associated_group')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('374', '^occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_occupation(self, key, value):
    """Reverse - Occupation."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'start_period': 's',
        'source_of_term': '2',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'source_of_information': 'v',
        'occupation': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('occupation')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('375', '^gender$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_gender(self, key, value):
    """Reverse - Gender."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_term': '2',
        'start_period': 's',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'source_of_information': 'v',
        'gender': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        's': value.get('start_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('gender')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('376', '^family_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_family_information(self, key, value):
    """Reverse - Family Information."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'hereditary_title': 'c',
        'linkage': '6',
        'name_of_prominent_member': 'b',
        'start_period': 's',
        'source_of_term': '2',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'source_of_information': 'v',
        'type_of_family': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'c': utils.reverse_force_list(
            value.get('hereditary_title')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('name_of_prominent_member')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_family')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    indicator_map2 = {"MARC language code": "_", "Source specified in $2": "7"}
    field_map = {
        'source_of_code': '2',
        'language_term': 'l',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'language_code': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7' and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_code'),
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
        '$ind1': '_',
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code')
        else indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21_authority.over('378', '^fuller_form_of_personal_name$')
@utils.filter_values
def reverse_fuller_form_of_personal_name(self, key, value):
    """Reverse - Fuller Form of Personal Name."""
    field_map = {
        'source_of_information': 'v',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'fuller_form_of_personal_name': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'q': value.get('fuller_form_of_personal_name'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('380', '^form_of_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    field_map = {
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'form_of_work': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_term': '2',
        'record_control_number': '0',
        'field_link_and_sequence_number': '8',
        'source_of_information': 'v',
        'other_distinguishing_characteristic': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {"Medium of performance": "0", "No information provided": "_", "Partial medium of performance": "1"}
    field_map = {
        'linkage': '6',
        'number_of_ensembles_of_the_same_type': 'e',
        'source_of_term': '2',
        'total_number_of_performers': 's',
        'field_link_and_sequence_number': '8',
        'number_of_performers_of_the_same_medium': 'n',
        'note': 'v',
        'authority_record_control_number_or_standard_number': '0',
        'soloist': 'b',
        'doubling_instrument': 'd',
        'alternative_medium_of_performance': 'p',
        'total_number_of_ensembles': 't',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'medium_of_performance': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        '2': value.get('source_of_term'),
        's': value.get('total_number_of_performers'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        't': value.get('total_number_of_ensembles'),
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('383', '^numeric_designation_of_musical_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    field_map = {
        'thematic_index_number': 'c',
        'linkage': '6',
        'serial_number': 'a',
        'thematic_index_code': 'd',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'publisher_associated_with_opus_number': 'e',
        'opus_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        'd': value.get('thematic_index_code'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': value.get('publisher_associated_with_opus_number'),
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'key': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('key'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'demographic_group_code': 'n',
        'demographic_group_term': 'm',
        'linkage': '6',
        'audience_code': 'b',
        'source': '2',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'audience_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'n': value.get('demographic_group_code'),
        'm': value.get('demographic_group_term'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        '2': value.get('source'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('386', '^creator_contributor_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    field_map = {
        'demographic_group_code': 'n',
        'demographic_group_term': 'm',
        'linkage': '6',
        'creator_contributor_code': 'b',
        'source': '2',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'creator_contributor_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'n': value.get('demographic_group_code'),
        'm': value.get('demographic_group_term'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        '2': value.get('source'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    indicator_map1 = {"Creation of aggregate work": "2", "Creation of work": "1", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'source_of_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'time_period_of_creation_term': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), '_'),
        '$ind2': '_',
    }
