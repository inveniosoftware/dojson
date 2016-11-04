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

from ..model import to_marc21_authority


@to_marc21_authority.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'content_type_term': 'a',
        'content_type_code': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'source': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'format_of_notated_music_term': 'a',
        'format_of_notated_music_code': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
        'authority_record_control_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over(
    '368', '^other_attributes_of_person_or_corporate_body$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_attributes_of_person_or_corporate_body(self, key, value):
    """Reverse - Other Attributes of Person or Corporate Body."""
    field_map = {
        'type_of_corporate_body': 'a',
        'type_of_jurisdiction': 'b',
        'other_designation': 'c',
        'title_of_person': 'd',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'authority_record_control_number_or_standard_number': '0',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('type_of_corporate_body')
        ),
        'c': utils.reverse_force_list(
            value.get('other_designation')
        ),
        'b': utils.reverse_force_list(
            value.get('type_of_jurisdiction')
        ),
        'd': utils.reverse_force_list(
            value.get('title_of_person')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'place_of_birth': 'a',
        'place_of_death': 'b',
        'associated_country': 'c',
        'place_of_residence_headquarters': 'e',
        'other_associated_place': 'f',
        'place_of_origin_of_work': 'g',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('place_of_birth'),
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        'b': value.get('place_of_death'),
        'e': utils.reverse_force_list(
            value.get('place_of_residence_headquarters')
        ),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('371', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    field_map = {
        'address': 'a',
        'city': 'b',
        'intermediate_jurisdiction': 'c',
        'country': 'd',
        'postal_code': 'e',
        'electronic_mail_address': 'm',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'public_note': 'z',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        'c': value.get('intermediate_jurisdiction'),
        'b': value.get('city'),
        'e': value.get('postal_code'),
        'd': value.get('country'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        's': value.get('start_period'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        't': value.get('end_period'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('372', '^field_of_activity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_field_of_activity(self, key, value):
    """Reverse - Field of Activity."""
    field_map = {
        'field_of_activity': 'a',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('field_of_activity')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'associated_group': 'a',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('associated_group')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'occupation': 'a',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('occupation')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'gender': 'a',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('gender')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'type_of_family': 'a',
        'name_of_prominent_member': 'b',
        'hereditary_title': 'c',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('type_of_family')
        ),
        'c': utils.reverse_force_list(
            value.get('hereditary_title')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_prominent_member')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('start_period'),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    field_map = {
        'language_code': 'a',
        'language_term': 'l',
        'source_of_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        'MARC language code': '_',
        'Source specified in $2': '7'
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_code'),
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21_authority.over('378', '^fuller_form_of_personal_name$')
@utils.filter_values
def reverse_fuller_form_of_personal_name(self, key, value):
    """Reverse - Fuller Form of Personal Name."""
    field_map = {
        'fuller_form_of_personal_name': 'q',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('fuller_form_of_personal_name'),
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
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('380', '^form_of_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    field_map = {
        'form_of_work': 'a',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over(
    '381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(
        self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'other_distinguishing_characteristic': 'a',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'record_control_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': value.get('source_of_term'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    field_map = {
        'medium_of_performance': 'a',
        'soloist': 'b',
        'doubling_instrument': 'd',
        'number_of_ensembles': 'e',
        'number_of_performers_of_the_same_medium': 'n',
        'alternative_medium_of_performance': 'p',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'total_number_of_performers': 's',
        'note': 'v',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Medium of performance': '0',
                      'No information provided': '_', 'Partial medium of performance': '1'}
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles')
        ),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        'r': utils.reverse_force_list(
            value.get(
                'total_number_of_individuals_performing_alongside_ensembles')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        's': value.get('total_number_of_performers'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'serial_number': 'a',
        'opus_number': 'b',
        'thematic_index_number': 'c',
        'thematic_index_code': 'd',
        'publisher_associated_with_opus_number': 'e',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        'e': value.get('publisher_associated_with_opus_number'),
        'd': value.get('thematic_index_code'),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    field_map = {
        'key': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        'Relationship to original unknown': '_',
        'Original key': '0',
        'Transposed key': '1'
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('key'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('key_type'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'audience_term': 'a',
        'audience_code': 'b',
        'demographic_group_term': 'm',
        'demographic_group_code': 'n',
        'authority_record_control_number_or_standard_number': '0',
        'source': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        'm': value.get('demographic_group_term'),
        'n': value.get('demographic_group_code'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'creator_contributor_term': 'a',
        'creator_contributor_code': 'b',
        'demographic_group_term': 'm',
        'demographic_group_code': 'n',
        'authority_record_control_number_or_standard_number': '0',
        'source': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        'm': value.get('demographic_group_term'),
        'n': value.get('demographic_group_code'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    field_map = {
        'time_period_of_creation_term': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {'Creation of aggregate work': '2',
                      'Creation of work': '1', 'No information provided': '_'}
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), '_'),
        '$ind2': '_',
    }
