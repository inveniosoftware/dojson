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
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'content_type_term',
        '8': 'field_link_and_sequence_number',
        'b': 'content_type_code',
        '6': 'linkage',
        '2': 'source',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
    }


@marc21_authority.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'format_of_notated_music_term',
        '8': 'field_link_and_sequence_number',
        'b': 'format_of_notated_music_code',
        '6': 'linkage',
        '2': 'source_of_term',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
    }


@marc21_authority.over('complex_see_also_reference_subject', '^360..')
@utils.for_each_value
@utils.filter_values
def complex_see_also_reference_subject(self, key, value):
    """Complex See Also Reference-Subject."""
    field_map = {
        'i': 'explanatory_text',
        '6': 'linkage',
        '0': 'authority_record_control_number',
        'a': 'heading_referred_to',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'heading_referred_to': utils.force_list(
            value.get('a')
        ),
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
        '6': 'linkage',
        'v': 'source_of_information',
        't': 'end_period',
        'c': 'other_designation',
        'b': 'type_of_jurisdiction',
        's': 'start_period',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'type_of_corporate_body',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'd': 'title_of_person',
        '2': 'source',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'end_period': value.get('t'),
        'other_designation': utils.force_list(
            value.get('c')
        ),
        'type_of_jurisdiction': utils.force_list(
            value.get('b')
        ),
        'start_period': value.get('s'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'type_of_corporate_body': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'title_of_person': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
    }


@marc21_authority.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'f': 'other_associated_place',
        '0': 'record_control_number',
        's': 'start_period',
        'u': 'uniform_resource_identifier',
        'b': 'place_of_death',
        '6': 'linkage',
        't': 'end_period',
        'e': 'place_of_residence_headquarters',
        'g': 'place_of_origin_of_work',
        'a': 'place_of_birth',
        '8': 'field_link_and_sequence_number',
        'c': 'associated_country',
        '2': 'source_of_term',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'start_period': value.get('s'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'place_of_death': value.get('b'),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'place_of_residence_headquarters': utils.force_list(
            value.get('e')
        ),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'place_of_birth': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'source_of_term': value.get('2'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
    }


@marc21_authority.over('address', '^371..')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    field_map = {
        '6': 'linkage',
        'v': 'source_of_information',
        'm': 'electronic_mail_address',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'b': 'city',
        's': 'start_period',
        'a': 'address',
        'e': 'postal_code',
        'z': 'public_note',
        '8': 'field_link_and_sequence_number',
        '4': 'relator_code',
        'c': 'intermediate_jurisdiction',
        'd': 'country',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'city': value.get('b'),
        'start_period': value.get('s'),
        'address': utils.force_list(
            value.get('a')
        ),
        'postal_code': value.get('e'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'intermediate_jurisdiction': value.get('c'),
        'country': value.get('d'),
    }


@marc21_authority.over('field_of_activity', '^372..')
@utils.for_each_value
@utils.filter_values
def field_of_activity(self, key, value):
    """Field of Activity."""
    field_map = {
        'u': 'uniform_resource_identifier',
        '0': 'record_control_number',
        'a': 'field_of_activity',
        'v': 'source_of_information',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        't': 'end_period',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'field_of_activity': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('associated_group', '^373..')
@utils.for_each_value
@utils.filter_values
def associated_group(self, key, value):
    """Associated Group."""
    field_map = {
        'u': 'uniform_resource_identifier',
        '0': 'record_control_number',
        'a': 'associated_group',
        'v': 'source_of_information',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        't': 'end_period',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'associated_group': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('occupation', '^374..')
@utils.for_each_value
@utils.filter_values
def occupation(self, key, value):
    """Occupation."""
    field_map = {
        'u': 'uniform_resource_identifier',
        '0': 'record_control_number',
        'a': 'occupation',
        'v': 'source_of_information',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        't': 'end_period',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'occupation': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('gender', '^375..')
@utils.for_each_value
@utils.filter_values
def gender(self, key, value):
    """Gender."""
    field_map = {
        'u': 'uniform_resource_identifier',
        'a': 'gender',
        'v': 'source_of_information',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        't': 'end_period',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'gender': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('family_information', '^376..')
@utils.for_each_value
@utils.filter_values
def family_information(self, key, value):
    """Family Information."""
    field_map = {
        't': 'end_period',
        '0': 'record_control_number',
        'a': 'type_of_family',
        'v': 'source_of_information',
        's': 'start_period',
        '8': 'field_link_and_sequence_number',
        'b': 'name_of_prominent_member',
        '6': 'linkage',
        'c': 'hereditary_title',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'end_period': value.get('t'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'type_of_family': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'start_period': value.get('s'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name_of_prominent_member': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'hereditary_title': utils.force_list(
            value.get('c')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('associated_language', '^377.[7_]')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {"7": "Source specified in $2", "_": "MARC language code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'language_code',
        'l': 'language_term',
        '2': 'source_of_code',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'language_code': utils.force_list(
            value.get('a')
        ),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('fuller_form_of_personal_name', '^378..')
@utils.filter_values
def fuller_form_of_personal_name(self, key, value):
    """Fuller Form of Personal Name."""
    field_map = {
        'u': 'uniform_resource_identifier',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'q': 'fuller_form_of_personal_name',
        'v': 'source_of_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'fuller_form_of_personal_name': value.get('q'),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
    }


@marc21_authority.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        '6': 'linkage',
        '0': 'record_control_number',
        'a': 'form_of_work',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'source_of_term': value.get('2'),
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
        '0': 'record_control_number',
        'a': 'other_distinguishing_characteristic',
        'v': 'source_of_information',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'u': 'uniform_resource_identifier',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_term': value.get('2'),
    }


@marc21_authority.over('medium_of_performance', '^382[10_].')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {"0": "Medium of performance", "1": "Partial medium of performance", "_": "No information provided"}
    field_map = {
        'v': 'note',
        's': 'total_number_of_performers',
        'b': 'soloist',
        '6': 'linkage',
        't': 'total_number_of_ensembles',
        'p': 'alternative_medium_of_performance',
        'a': 'medium_of_performance',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        '0': 'authority_record_control_number_or_standard_number',
        'e': 'number_of_ensembles_of_the_same_type',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_performers_of_the_same_medium',
        'd': 'doubling_instrument',
        '2': 'source_of_term',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'note': utils.force_list(
            value.get('v')
        ),
        'total_number_of_performers': value.get('s'),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'total_number_of_ensembles': value.get('t'),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': value.get('r'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'number_of_ensembles_of_the_same_type': utils.force_list(
            value.get('e')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'source_of_term': value.get('2'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21_authority.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'e': 'publisher_associated_with_opus_number',
        'a': 'serial_number',
        '8': 'field_link_and_sequence_number',
        'b': 'opus_number',
        '6': 'linkage',
        'c': 'thematic_index_number',
        'd': 'thematic_index_code',
        '2': 'source',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'publisher_associated_with_opus_number': value.get('e'),
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'thematic_index_code': value.get('d'),
        'source': value.get('2'),
    }


@marc21_authority.over('key', '^384..')
@utils.filter_values
def key(self, key, value):
    """Key."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'key',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'key': value.get('a'),
    }


@marc21_authority.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'audience_term',
        'm': 'demographic_group_term',
        '8': 'field_link_and_sequence_number',
        'b': 'audience_code',
        '6': 'linkage',
        '2': 'source',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'demographic_group_term': value.get('m'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
    }


@marc21_authority.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'creator_contributor_term',
        'm': 'demographic_group_term',
        '8': 'field_link_and_sequence_number',
        'b': 'creator_contributor_code',
        '6': 'linkage',
        '2': 'source',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'demographic_group_term': value.get('m'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
    }


@marc21_authority.over('time_period_of_creation', '^388[12_].')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {"1": "Creation of work", "2": "Creation of aggregate work", "_": "No information provided"}
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'time_period_of_creation_term',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'source_of_term',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'type_of_time_period': indicator_map1.get(key[3]),
    }
