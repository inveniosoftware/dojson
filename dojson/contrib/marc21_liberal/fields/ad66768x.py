# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_authority


@marc21_authority.over('nonpublic_general_note', '^667..')
@utils.for_each_value
@utils.filter_values
def nonpublic_general_note(self, key, value):
    """Nonpublic General Note."""
    field_map = {
        'a': 'nonpublic_general_note',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'nonpublic_general_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('source_data_found', '^670..')
@utils.for_each_value
@utils.filter_values
def source_data_found(self, key, value):
    """Source Data Found."""
    field_map = {
        'a': 'source_citation',
        'b': 'information_found',
        'u': 'uniform_resource_identifier',
        'w': 'bibliographic_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_citation': value.get('a'),
        'information_found': value.get('b'),
        'uniform_resource_identifier': value.get('u'),
        'bibliographic_record_control_number': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('title_related_to_the_entity', '^672..')
@utils.for_each_value
@utils.filter_values
def title_related_to_the_entity(self, key, value):
    """Source Data Found."""
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'f': 'date',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date': value.get('f'),
        'bibliographic_record_control_number': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4])
    }


@marc21_authority.over('title_not_related_to_the_entity', '^673..')
@utils.for_each_value
@utils.filter_values
def title_not_related_to_the_entity(self, key, value):
    """Source Data Found."""
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'f': 'date',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map2 = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date': value.get('f'),
        'bibliographic_record_control_number': value.get('w'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4])
    }


@marc21_authority.over('source_data_not_found', '^675..')
@utils.filter_values
def source_data_not_found(self, key, value):
    """Source Data Not Found."""
    field_map = {
        'a': 'source_citation',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    # TODO consider joining with source_data_found as source_data
    return {
        '__order__': tuple(order) if len(order) else None,
        'source_citation': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('biographical_or_historical_data', '^678..')
@utils.for_each_value
@utils.filter_values
def bibliographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    field_map = {
        'a': 'biographical_or_historical_data',
        'b': 'expansion',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        '_': 'No information provided',
        '1': 'Biographical sketch',
        '2': 'Administrative history',
    }

    if key[3] in indicator_map1:
        order.append('type_of_data')

    return {
        '__order__': tuple(order) if len(order) else None,
        'biographical_or_historical_data': value.get('a'),
        'expansion': value.get('b'),
        'uniform_resource_identifier': value.get('u'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'type_of_data': indicator_map1.get(key[3]),
    }


@marc21_authority.over('public_general_note', '^680..')
@utils.for_each_value
@utils.filter_values
def public_general_note(self, key, value):
    """Public General Note."""
    field_map = {
        'a': 'heading_or_subdivision_term',
        'i': 'explanatory_text',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('subject_example_tracing_note', '^681..')
@utils.for_each_value
@utils.filter_values
def subject_example_tracing_note(self, key, value):
    """Subject Example Tracing Note."""
    field_map = {
        'a': 'subject_heading_or_subdivision_term',
        'i': 'explanatory_text',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'subject_heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('deleted_heading_information', '^682..')
@utils.filter_values
def deleted_heading_information(self, key, value):
    """Deleted Heading Information."""
    field_map = {
        'a': 'replacement_heading',
        'i': 'explanatory_text',
        '0': 'replacement_authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'replacement_heading': utils.force_list(
            value.get('a')
        ),
        'replacement_authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('application_history_note', '^688..')
@utils.for_each_value
@utils.filter_values
def application_history_note(self, key, value):
    """Application History Note."""
    field_map = {
        'a': 'application_history_note',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'application_history_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
    }
