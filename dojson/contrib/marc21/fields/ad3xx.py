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

from ..model import marc21_authority


@marc21_authority.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        'a': 'content_type_term',
        'b': 'content_type_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        'a': 'format_of_notated_music_term',
        'b': 'format_of_notated_music_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('complex_see_also_reference_subject', '^360..')
@utils.for_each_value
@utils.filter_values
def complex_see_also_reference_subject(self, key, value):
    """Complex See Also Reference-Subject."""
    field_map = {
        'a': 'heading_referred_to',
        'i': 'explanatory_text',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('other_attributes_of_person_or_corporate_body', '^368..')
@utils.for_each_value
@utils.filter_values
def other_attributes_of_person_or_corporate_body(self, key, value):
    """Other Attributes of Person or Corporate Body."""
    field_map = {
        'a': 'type_of_corporate_body',
        'b': 'type_of_jurisdiction',
        'c': 'other_designation',
        'd': 'title_of_person',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_corporate_body': utils.force_list(
            value.get('a')
        ),
        'type_of_jurisdiction': utils.force_list(
            value.get('b')
        ),
        'other_designation': utils.force_list(
            value.get('c')
        ),
        'title_of_person': utils.force_list(
            value.get('d')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'a': 'place_of_birth',
        'b': 'place_of_death',
        'c': 'associated_country',
        'e': 'place_of_residence_headquarters',
        'f': 'other_associated_place',
        'g': 'place_of_origin_of_work',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_birth': value.get('a'),
        'place_of_death': value.get('b'),
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'place_of_residence_headquarters': utils.force_list(
            value.get('e')
        ),
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('address', '^371..')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    field_map = {
        'a': 'address',
        'b': 'city',
        'c': 'intermediate_jurisdiction',
        'd': 'country',
        'e': 'postal_code',
        'm': 'electronic_mail_address',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        'z': 'public_note',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'address': utils.force_list(
            value.get('a')
        ),
        'city': value.get('b'),
        'intermediate_jurisdiction': value.get('c'),
        'country': value.get('d'),
        'postal_code': value.get('e'),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('field_of_activity', '^372..')
@utils.for_each_value
@utils.filter_values
def field_of_activity(self, key, value):
    """Field of Activity."""
    field_map = {
        'a': 'field_of_activity',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_of_activity': utils.force_list(
            value.get('a')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_group', '^373..')
@utils.for_each_value
@utils.filter_values
def associated_group(self, key, value):
    """Associated Group."""
    field_map = {
        'a': 'associated_group',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'associated_group': utils.force_list(
            value.get('a')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('occupation', '^374..')
@utils.for_each_value
@utils.filter_values
def occupation(self, key, value):
    """Occupation."""
    field_map = {
        'a': 'occupation',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'occupation': utils.force_list(
            value.get('a')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('gender', '^375..')
@utils.for_each_value
@utils.filter_values
def gender(self, key, value):
    """Gender."""
    field_map = {
        'a': 'gender',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'gender': utils.force_list(
            value.get('a')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('family_information', '^376..')
@utils.for_each_value
@utils.filter_values
def family_information(self, key, value):
    """Family Information."""
    field_map = {
        'a': 'type_of_family',
        'b': 'name_of_prominent_member',
        'c': 'hereditary_title',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_family': utils.force_list(
            value.get('a')
        ),
        'name_of_prominent_member': utils.force_list(
            value.get('b')
        ),
        'hereditary_title': utils.force_list(
            value.get('c')
        ),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('associated_language', '^377.[7_]')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {"7": "Source specified in $2", "_": "MARC language code"}
    field_map = {
        'a': 'language_code',
        'l': 'language_term',
        '2': 'source_of_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code': utils.force_list(
            value.get('a')
        ),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('fuller_form_of_personal_name', '^378..')
@utils.filter_values
def fuller_form_of_personal_name(self, key, value):
    """Fuller Form of Personal Name."""
    field_map = {
        'q': 'fuller_form_of_personal_name',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'fuller_form_of_personal_name': value.get('q'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        'a': 'form_of_work',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'a': 'other_distinguishing_characteristic',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('medium_of_performance', '^382[10_].')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {"0": "Medium of performance", "1": "Partial medium of performance", "_": "No information provided"}
    field_map = {
        'a': 'medium_of_performance',
        'b': 'soloist',
        'd': 'doubling_instrument',
        'e': 'number_of_ensembles_of_the_same_type',
        'n': 'number_of_performers_of_the_same_medium',
        'p': 'alternative_medium_of_performance',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        's': 'total_number_of_performers',
        't': 'total_number_of_ensembles',
        'v': 'note',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'number_of_ensembles_of_the_same_type': utils.force_list(
            value.get('e')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': value.get('r'),
        'total_number_of_performers': value.get('s'),
        'total_number_of_ensembles': value.get('t'),
        'note': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21_authority.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'a': 'serial_number',
        'b': 'opus_number',
        'c': 'thematic_index_number',
        'd': 'thematic_index_code',
        'e': 'publisher_associated_with_opus_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'thematic_index_code': value.get('d'),
        'publisher_associated_with_opus_number': value.get('e'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('key', '^384..')
@utils.filter_values
def key(self, key, value):
    """Key."""
    field_map = {
        'a': 'key',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'key': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'a': 'audience_term',
        'b': 'audience_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'a': 'creator_contributor_term',
        'b': 'creator_contributor_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('time_period_of_creation', '^388[12_].')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {"1": "Creation of work", "2": "Creation of aggregate work", "_": "No information provided"}
    field_map = {
        'a': 'time_period_of_creation_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period')

    return {
        '__order__': tuple(order) if len(order) else None,
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_time_period': indicator_map1.get(key[3]),
    }
