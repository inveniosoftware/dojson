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


@marc21_authority.over(
    'series_dates_of_publication_and_or_sequential_designation',
    '^640..')
@utils.for_each_value
@utils.filter_values
def series_dates_of_publication_and_or_sequential_designation(
        self,
        key,
        value):
    """Series Dates of Publication and/or Sequential Designation."""
    field_map = {
        'a': 'dates_of_publication_and_or_sequential_designation',
        'z': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        '0': 'Formatted_style',
        '1': 'Unformatted style',
    }

    if key[3] in indicator_map1:
        order.append('note_format_style')

    return {
        '__order__': tuple(order) if len(order) else None,
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'note_format_style': indicator_map1.get(key[3]),
    }


@marc21_authority.over('series_numbering_peculiarities', '^641..')
@utils.for_each_value
@utils.filter_values
def series_numbering_peculiarities(self, key, value):
    """Series Numbering Peculiarities."""
    field_map = {
        'a': 'numbering_peculiarities_note',
        'z': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'numbering_peculiarities_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
    }


@marc21_authority.over('series_numbering_example', '^642..')
@utils.for_each_value
@utils.filter_values
def series_numbering_example(self, key, value):
    """Series Numbering Example."""
    field_map = {
        'a': 'series_numbering_example',
        'd': 'volumes_dates_to_which_series_numbering_example_applies',
        '5': 'institution_copy_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'series_numbering_example': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')),
        'volumes_dates_to_which_series_numbering_example_applies': value.get('d'),
        'linkage': value.get('6'),
    }


@marc21_authority.over('series_place_and_publisher_issuing_body', '^643..')
@utils.for_each_value
@utils.filter_values
def series_place_and_publisher_issuing_body(self, key, value):
    """Series Place and Publisher/Issuing Body."""
    field_map = {
        'a': 'place',
        'b': 'publisher_issuing_body',
        'd': 'volumes_dates_to_which_place_and_publisher_issuing_body_apply',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'publisher_issuing_body': utils.force_list(
            value.get('b')
        ),
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': value.get('d'),
        'linkage': value.get('6'),
    }


@marc21_authority.over('series_analysis_practice', '^644..')
@utils.for_each_value
@utils.filter_values
def series_analysis_practice(self, key, value):
    """Series Analysis Practice."""
    field_map = {
        'a': 'series_analysis_practice',
        'b': 'exceptions_to_analysis_practice',
        'd': 'volumes_dates_to_which_analysis_practice_applies',
        '5': 'institution_copy_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'series_analysis_practice': value.get('a'),
        'exceptions_to_analysis_practice': value.get('b'),
        'volumes_dates_to_which_analysis_practice_applies': value.get('d'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('series_tracing_practice', '^645..')
@utils.for_each_value
@utils.filter_values
def series_tracing_practice(self, key, value):
    """Series Tracing Practice."""
    field_map = {
        'a': 'series_tracing_practice',
        'd': 'volumes_dates_to_which_tracing_practice_applies',
        '5': 'institution_copy_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'series_tracing_practice': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'volumes_dates_to_which_tracing_practice_applies': value.get('d'),
        'linkage': value.get('6'),
    }


@marc21_authority.over('series_classification_practice', '^646..')
@utils.for_each_value
@utils.filter_values
def series_classification_practice(self, key, value):
    """Series Classification Practice."""
    field_map = {
        'a': 'series_classification_practice',
        'd': 'volumes_dates_to_which_classification_practice_applies',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'series_classification_practice': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')),
        'volumes_dates_to_which_classification_practice_applies': value.get('d'),
        'linkage': value.get('6'),
    }
