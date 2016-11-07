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


@marc21_authority.over('series_dates_of_publication_and_or_sequential_designation', '^640[0_1].')
@utils.for_each_value
@utils.filter_values
def series_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Series Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted style"}
    field_map = {
        'a': 'dates_of_publication_and_or_sequential_designation',
        '6': 'linkage',
        'z': 'source_of_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('note_format_style')

    return {
        '__order__': tuple(order) if len(order) else None,
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'linkage': value.get('6'),
        'source_of_information': value.get('z'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_format_style': indicator_map1.get(key[3]),
    }


@marc21_authority.over('series_numbering_peculiarities', '^641..')
@utils.for_each_value
@utils.filter_values
def series_numbering_peculiarities(self, key, value):
    """Series Numbering Peculiarities."""
    field_map = {
        'a': 'numbering_peculiarities_note',
        '6': 'linkage',
        'z': 'source_of_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'numbering_peculiarities_note': value.get('a'),
        'linkage': value.get('6'),
        'source_of_information': value.get('z'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('series_numbering_example', '^642..')
@utils.for_each_value
@utils.filter_values
def series_numbering_example(self, key, value):
    """Series Numbering Example."""
    field_map = {
        'd': 'volumes_dates_to_which_series_numbering_example_applies',
        'a': 'series_numbering_example',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_copy_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_series_numbering_example_applies': value.get('d'),
        'series_numbering_example': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
    }


@marc21_authority.over('series_place_and_publisher_issuing_body', '^643..')
@utils.for_each_value
@utils.filter_values
def series_place_and_publisher_issuing_body(self, key, value):
    """Series Place and Publisher/Issuing Body."""
    field_map = {
        'a': 'place',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'b': 'publisher_issuing_body',
        'd': 'volumes_dates_to_which_place_and_publisher_issuing_body_apply',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'publisher_issuing_body': utils.force_list(
            value.get('b')
        ),
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': value.get('d'),
    }


@marc21_authority.over('series_analysis_practice', '^644..')
@utils.for_each_value
@utils.filter_values
def series_analysis_practice(self, key, value):
    """Series Analysis Practice."""
    field_map = {
        '6': 'linkage',
        'a': 'series_analysis_practice',
        '5': 'institution_copy_to_which_field_applies',
        '8': 'field_link_and_sequence_number',
        'b': 'exceptions_to_analysis_practice',
        'd': 'volumes_dates_to_which_analysis_practice_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'series_analysis_practice': value.get('a'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'exceptions_to_analysis_practice': value.get('b'),
        'volumes_dates_to_which_analysis_practice_applies': value.get('d'),
    }


@marc21_authority.over('series_tracing_practice', '^645..')
@utils.for_each_value
@utils.filter_values
def series_tracing_practice(self, key, value):
    """Series Tracing Practice."""
    field_map = {
        'd': 'volumes_dates_to_which_tracing_practice_applies',
        'a': 'series_tracing_practice',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_copy_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_tracing_practice_applies': value.get('d'),
        'series_tracing_practice': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
    }


@marc21_authority.over('series_classification_practice', '^646..')
@utils.for_each_value
@utils.filter_values
def series_classification_practice(self, key, value):
    """Series Classification Practice."""
    field_map = {
        'd': 'volumes_dates_to_which_classification_practice_applies',
        'a': 'series_classification_practice',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_classification_practice_applies': value.get('d'),
        'series_classification_practice': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
    }


@marc21_authority.over('complex_see_also_reference_name', '^663..')
@utils.filter_values
def complex_see_also_reference_name(self, key, value):
    """Complex See Also Reference-Name."""
    field_map = {
        'a': 'explanatory_text',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'b': 'heading_referred_to',
        't': 'title_referred_to',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
    }


@marc21_authority.over('complex_see_reference_name', '^664..')
@utils.filter_values
def complex_see_reference_name(self, key, value):
    """Complex See Reference-Name."""
    field_map = {
        'a': 'explanatory_text',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'b': 'heading_referred_to',
        't': 'title_referred_to',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
    }


@marc21_authority.over('history_reference', '^665..')
@utils.filter_values
def history_reference(self, key, value):
    """History Reference."""
    field_map = {
        'a': 'history_reference',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'history_reference': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('general_explanatory_reference_name', '^666..')
@utils.filter_values
def general_explanatory_reference_name(self, key, value):
    """General Explanatory Reference-Name."""
    field_map = {
        'a': 'general_explanatory_reference',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'general_explanatory_reference': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('nonpublic_general_note', '^667..')
@utils.for_each_value
@utils.filter_values
def nonpublic_general_note(self, key, value):
    """Nonpublic General Note."""
    field_map = {
        'a': 'nonpublic_general_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'nonpublic_general_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
    }


@marc21_authority.over('source_data_found', '^670..')
@utils.for_each_value
@utils.filter_values
def source_data_found(self, key, value):
    """Source Data Found."""
    field_map = {
        '6': 'linkage',
        'a': 'source_citation',
        'u': 'uniform_resource_identifier',
        '8': 'field_link_and_sequence_number',
        'b': 'information_found',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'source_citation': value.get('a'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'information_found': value.get('b'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
    }


@marc21_authority.over('title_related_to_the_entity', '^672.[801347652_9]')
@utils.for_each_value
@utils.filter_values
def title_related_to_the_entity(self, key, value):
    """Title Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '6': 'linkage',
        'f': 'date',
        '8': 'field_link_and_sequence_number',
        'a': 'title',
        '0': 'authority_record_control_number_or_standard_number',
        'b': 'remainder_of_title',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'date': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'remainder_of_title': value.get('b'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }


@marc21_authority.over('title_not_related_to_the_entity', '^673.[801347652_9]')
@utils.for_each_value
@utils.filter_values
def title_not_related_to_the_entity(self, key, value):
    """Title Not Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        '6': 'linkage',
        'f': 'date',
        '8': 'field_link_and_sequence_number',
        'a': 'title',
        '0': 'authority_record_control_number_or_standard_number',
        'b': 'remainder_of_title',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('nonfiling_characters')

    return {
        '__order__': tuple(order) if len(order) else None,
        'linkage': value.get('6'),
        'date': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'title': value.get('a'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'remainder_of_title': value.get('b'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'nonfiling_characters': indicator_map2.get(key[4]),
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

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_citation': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('biographical_or_historical_data', '^678[0_1].')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {"0": "Biographical sketch", "1": "Administrative history", "_": "No information provided"}
    field_map = {
        'a': 'biographical_or_historical_data',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'b': 'expansion',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_data')

    return {
        '__order__': tuple(order) if len(order) else None,
        'biographical_or_historical_data': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'expansion': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'type_of_data': indicator_map1.get(key[3]),
    }


@marc21_authority.over('public_general_note', '^680..')
@utils.for_each_value
@utils.filter_values
def public_general_note(self, key, value):
    """Public General Note."""
    field_map = {
        'a': 'heading_or_subdivision_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'i': 'explanatory_text',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
    }


@marc21_authority.over('subject_example_tracing_note', '^681..')
@utils.for_each_value
@utils.filter_values
def subject_example_tracing_note(self, key, value):
    """Subject Example Tracing Note."""
    field_map = {
        'a': 'subject_heading_or_subdivision_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'i': 'explanatory_text',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'subject_heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
    }


@marc21_authority.over('deleted_heading_information', '^682..')
@utils.filter_values
def deleted_heading_information(self, key, value):
    """Deleted Heading Information."""
    field_map = {
        '0': 'replacement_authority_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'replacement_heading',
        'i': 'explanatory_text',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'replacement_authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'replacement_heading': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
    }


@marc21_authority.over('application_history_note', '^688..')
@utils.for_each_value
@utils.filter_values
def application_history_note(self, key, value):
    """Application History Note."""
    field_map = {
        'a': 'application_history_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'application_history_note': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
    }
