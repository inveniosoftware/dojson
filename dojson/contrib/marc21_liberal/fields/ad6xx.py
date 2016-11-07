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


@marc21_liberal_authority.over('series_dates_of_publication_and_or_sequential_designation', '^640..')
@utils.for_each_value
@utils.filter_values
def series_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Series Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted style"}
    field_map = {
        'z': 'source_of_information',
        '6': 'linkage',
        'a': 'dates_of_publication_and_or_sequential_designation',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('note_format_style')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
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
        'z': 'source_of_information',
        '6': 'linkage',
        'a': 'numbering_peculiarities_note',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'numbering_peculiarities_note': value.get('a'),
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
        'd': 'volumes_dates_to_which_series_numbering_example_applies',
        '6': 'linkage',
        '5': 'institution_copy_to_which_field_applies',
        'a': 'series_numbering_example',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'volumes_dates_to_which_series_numbering_example_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'series_numbering_example': value.get('a'),
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
        'b': 'publisher_issuing_body',
        '6': 'linkage',
        'd': 'volumes_dates_to_which_place_and_publisher_issuing_body_apply',
        'a': 'place',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'publisher_issuing_body': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': value.get('d'),
        'place': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('series_analysis_practice', '^644..')
@utils.for_each_value
@utils.filter_values
def series_analysis_practice(self, key, value):
    """Series Analysis Practice."""
    field_map = {
        'b': 'exceptions_to_analysis_practice',
        'd': 'volumes_dates_to_which_analysis_practice_applies',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '5': 'institution_copy_to_which_field_applies',
        'a': 'series_analysis_practice',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'exceptions_to_analysis_practice': value.get('b'),
        'volumes_dates_to_which_analysis_practice_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'series_analysis_practice': value.get('a'),
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
        'd': 'volumes_dates_to_which_tracing_practice_applies',
        '6': 'linkage',
        '5': 'institution_copy_to_which_field_applies',
        'a': 'series_tracing_practice',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'volumes_dates_to_which_tracing_practice_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_copy_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'series_tracing_practice': value.get('a'),
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
        'd': 'volumes_dates_to_which_classification_practice_applies',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'series_classification_practice',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'volumes_dates_to_which_classification_practice_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'series_classification_practice': value.get('a'),
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
        'b': 'heading_referred_to',
        '6': 'linkage',
        'a': 'explanatory_text',
        't': 'title_referred_to',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
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


@marc21_liberal_authority.over('complex_see_reference_name', '^664..')
@utils.filter_values
def complex_see_reference_name(self, key, value):
    """Complex See Reference-Name."""
    field_map = {
        'b': 'heading_referred_to',
        '6': 'linkage',
        'a': 'explanatory_text',
        't': 'title_referred_to',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
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


@marc21_liberal_authority.over('history_reference', '^665..')
@utils.filter_values
def history_reference(self, key, value):
    """History Reference."""
    field_map = {
        '6': 'linkage',
        'a': 'history_reference',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'history_reference': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('general_explanatory_reference_name', '^666..')
@utils.filter_values
def general_explanatory_reference_name(self, key, value):
    """General Explanatory Reference-Name."""
    field_map = {
        '6': 'linkage',
        'a': 'general_explanatory_reference',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'general_explanatory_reference': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('nonpublic_general_note', '^667..')
@utils.for_each_value
@utils.filter_values
def nonpublic_general_note(self, key, value):
    """Nonpublic General Note."""
    field_map = {
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'nonpublic_general_note',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'nonpublic_general_note': value.get('a'),
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
        'u': 'uniform_resource_identifier',
        'b': 'information_found',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'source_citation',
        'w': 'bibliographic_record_control_number',
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
        'information_found': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'source_citation': value.get('a'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
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
        'b': 'remainder_of_title',
        'a': 'title',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'f': 'date',
        '0': 'authority_record_control_number_or_standard_number',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'remainder_of_title': value.get('b'),
        'title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'date': value.get('f'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
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
        'b': 'remainder_of_title',
        'a': 'title',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'f': 'date',
        '0': 'authority_record_control_number_or_standard_number',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('nonfiling_characters')

    record_dict = {
        '__order__': order if len(order) else None,
        'remainder_of_title': value.get('b'),
        'title': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'date': value.get('f'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
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
        '6': 'linkage',
        'a': 'source_citation',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'source_citation': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('biographical_or_historical_data', '^678..')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {"0": "Biographical sketch", "1": "Administrative history", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'expansion',
        '6': 'linkage',
        'a': 'biographical_or_historical_data',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_data')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'expansion': value.get('b'),
        'linkage': value.get('6'),
        'biographical_or_historical_data': utils.force_list(
            value.get('a')
        ),
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
        'i': 'explanatory_text',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'heading_or_subdivision_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'heading_or_subdivision_term': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('subject_example_tracing_note', '^681..')
@utils.for_each_value
@utils.filter_values
def subject_example_tracing_note(self, key, value):
    """Subject Example Tracing Note."""
    field_map = {
        'i': 'explanatory_text',
        '6': 'linkage',
        'a': 'subject_heading_or_subdivision_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'subject_heading_or_subdivision_term': utils.force_list(
            value.get('a')
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


@marc21_liberal_authority.over('deleted_heading_information', '^682..')
@utils.filter_values
def deleted_heading_information(self, key, value):
    """Deleted Heading Information."""
    field_map = {
        'i': 'explanatory_text',
        '0': 'replacement_authority_record_control_number',
        'a': 'replacement_heading',
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
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'replacement_authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'replacement_heading': utils.force_list(
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


@marc21_liberal_authority.over('application_history_note', '^688..')
@utils.for_each_value
@utils.filter_values
def application_history_note(self, key, value):
    """Application History Note."""
    field_map = {
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'application_history_note',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'application_history_note': value.get('a'),
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
