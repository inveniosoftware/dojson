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

from ..utils import liberal_map_order
from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('series_dates_of_publication_and_or_sequential_designation', '^640..')
@utils.for_each_value
@utils.filter_values
def series_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Series Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted style"}
    field_map = {
        'a': 'dates_of_publication_and_or_sequential_designation',
        'z': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('note_format_style')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'note_format_style': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('series_numbering_peculiarities', '^641..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'numbering_peculiarities_note': value.get('a'),
        'source_of_information': value.get('z'),
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


@marc21_liberal_authority.over('series_numbering_example', '^642..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'series_numbering_example': value.get('a'),
        'volumes_dates_to_which_series_numbering_example_applies': value.get('d'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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


@marc21_liberal_authority.over('series_place_and_publisher_issuing_body', '^643..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'place': utils.force_list(
            value.get('a')
        ),
        'publisher_issuing_body': utils.force_list(
            value.get('b')
        ),
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': value.get('d'),
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


@marc21_liberal_authority.over('series_analysis_practice', '^644..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
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
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('series_tracing_practice', '^645..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'series_tracing_practice': value.get('a'),
        'volumes_dates_to_which_tracing_practice_applies': value.get('d'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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


@marc21_liberal_authority.over('series_classification_practice', '^646..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'series_classification_practice': value.get('a'),
        'volumes_dates_to_which_classification_practice_applies': value.get('d'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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


@marc21_liberal_authority.over('complex_see_also_reference_name', '^663..')
@utils.filter_values
def complex_see_also_reference_name(self, key, value):
    """Complex See Also Reference-Name."""
    field_map = {
        'a': 'explanatory_text',
        'b': 'heading_referred_to',
        't': 'title_referred_to',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
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


@marc21_liberal_authority.over('complex_see_reference_name', '^664..')
@utils.filter_values
def complex_see_reference_name(self, key, value):
    """Complex See Reference-Name."""
    field_map = {
        'a': 'explanatory_text',
        'b': 'heading_referred_to',
        't': 'title_referred_to',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
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


@marc21_liberal_authority.over('history_reference', '^665..')
@utils.filter_values
def history_reference(self, key, value):
    """History Reference."""
    field_map = {
        'a': 'history_reference',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'history_reference': utils.force_list(
            value.get('a')
        ),
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


@marc21_liberal_authority.over('general_explanatory_reference_name', '^666..')
@utils.filter_values
def general_explanatory_reference_name(self, key, value):
    """General Explanatory Reference-Name."""
    field_map = {
        'a': 'general_explanatory_reference',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'general_explanatory_reference': utils.force_list(
            value.get('a')
        ),
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


@marc21_liberal_authority.over('nonpublic_general_note', '^667..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'nonpublic_general_note': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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


@marc21_liberal_authority.over('source_data_found', '^670..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_citation': value.get('a'),
        'information_found': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
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


@marc21_liberal_authority.over('title_related_to_the_entity', '^672..')
@utils.for_each_value
@utils.filter_values
def title_related_to_the_entity(self, key, value):
    """Title Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'f': 'date',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date': value.get('f'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('title_not_related_to_the_entity', '^673..')
@utils.for_each_value
@utils.filter_values
def title_not_related_to_the_entity(self, key, value):
    """Title Not Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'a': 'title',
        'b': 'remainder_of_title',
        'f': 'date',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'date': value.get('f'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'nonfiling_characters': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('source_data_not_found', '^675..')
@utils.filter_values
def source_data_not_found(self, key, value):
    """Source Data Not Found."""
    field_map = {
        'a': 'source_citation',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_citation': utils.force_list(
            value.get('a')
        ),
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


@marc21_liberal_authority.over('biographical_or_historical_data', '^678..')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {"0": "Biographical sketch", "1": "Administrative history", "_": "No information provided"}
    field_map = {
        'a': 'biographical_or_historical_data',
        'b': 'expansion',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('type_of_data')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'biographical_or_historical_data': utils.force_list(
            value.get('a')
        ),
        'expansion': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_data': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('public_general_note', '^680..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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


@marc21_liberal_authority.over('subject_example_tracing_note', '^681..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'subject_heading_or_subdivision_term': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
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


@marc21_liberal_authority.over('deleted_heading_information', '^682..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'replacement_heading': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'replacement_authority_record_control_number': utils.force_list(
            value.get('0')
        ),
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


@marc21_liberal_authority.over('application_history_note', '^688..')
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

    order = liberal_map_order(field_map, value)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'application_history_note': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
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
