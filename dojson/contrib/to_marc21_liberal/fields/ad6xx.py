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

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('640', '^series_dates_of_publication_and_or_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Reverse - Series Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"Formatted style": "0", "Unformatted style": "1"}
    field_map = {
        'source_of_information': 'z',
        'linkage': '6',
        'dates_of_publication_and_or_sequential_designation': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_format_style', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': value.get('source_of_information'),
        '6': value.get('linkage'),
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('note_format_style'), value.get('note_format_style', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('641', '^series_numbering_peculiarities$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_numbering_peculiarities(self, key, value):
    """Reverse - Series Numbering Peculiarities."""
    field_map = {
        'source_of_information': 'z',
        'linkage': '6',
        'numbering_peculiarities_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': value.get('source_of_information'),
        '6': value.get('linkage'),
        'a': value.get('numbering_peculiarities_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('642', '^series_numbering_example$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_numbering_example(self, key, value):
    """Reverse - Series Numbering Example."""
    field_map = {
        'volumes_dates_to_which_series_numbering_example_applies': 'd',
        'linkage': '6',
        'institution_copy_to_which_field_applies': '5',
        'series_numbering_example': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_series_numbering_example_applies'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        'a': value.get('series_numbering_example'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('643', '^series_place_and_publisher_issuing_body$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_place_and_publisher_issuing_body(self, key, value):
    """Reverse - Series Place and Publisher/Issuing Body."""
    field_map = {
        'publisher_issuing_body': 'b',
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': 'd',
        'linkage': '6',
        'place': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('publisher_issuing_body')
        ),
        'd': value.get('volumes_dates_to_which_place_and_publisher_issuing_body_apply'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('place')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('644', '^series_analysis_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_analysis_practice(self, key, value):
    """Reverse - Series Analysis Practice."""
    field_map = {
        'exceptions_to_analysis_practice': 'b',
        'institution_copy_to_which_field_applies': '5',
        'volumes_dates_to_which_analysis_practice_applies': 'd',
        'linkage': '6',
        'series_analysis_practice': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('exceptions_to_analysis_practice'),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_analysis_practice_applies'),
        '6': value.get('linkage'),
        'a': value.get('series_analysis_practice'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('645', '^series_tracing_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_tracing_practice(self, key, value):
    """Reverse - Series Tracing Practice."""
    field_map = {
        'volumes_dates_to_which_tracing_practice_applies': 'd',
        'linkage': '6',
        'institution_copy_to_which_field_applies': '5',
        'series_tracing_practice': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_tracing_practice_applies'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        'a': value.get('series_tracing_practice'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('646', '^series_classification_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_classification_practice(self, key, value):
    """Reverse - Series Classification Practice."""
    field_map = {
        'volumes_dates_to_which_classification_practice_applies': 'd',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'series_classification_practice': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_classification_practice_applies'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('series_classification_practice'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('663', '^complex_see_also_reference_name$')
@utils.filter_values
def reverse_complex_see_also_reference_name(self, key, value):
    """Reverse - Complex See Also Reference-Name."""
    field_map = {
        'heading_referred_to': 'b',
        'linkage': '6',
        'title_referred_to': 't',
        'explanatory_text': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        '6': value.get('linkage'),
        't': utils.reverse_force_list(
            value.get('title_referred_to')
        ),
        'a': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('664', '^complex_see_reference_name$')
@utils.filter_values
def reverse_complex_see_reference_name(self, key, value):
    """Reverse - Complex See Reference-Name."""
    field_map = {
        'heading_referred_to': 'b',
        'linkage': '6',
        'title_referred_to': 't',
        'explanatory_text': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        '6': value.get('linkage'),
        't': utils.reverse_force_list(
            value.get('title_referred_to')
        ),
        'a': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('665', '^history_reference$')
@utils.filter_values
def reverse_history_reference(self, key, value):
    """Reverse - History Reference."""
    field_map = {
        'linkage': '6',
        'history_reference': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('history_reference')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('666', '^general_explanatory_reference_name$')
@utils.filter_values
def reverse_general_explanatory_reference_name(self, key, value):
    """Reverse - General Explanatory Reference-Name."""
    field_map = {
        'linkage': '6',
        'general_explanatory_reference': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('general_explanatory_reference')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('667', '^nonpublic_general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_nonpublic_general_note(self, key, value):
    """Reverse - Nonpublic General Note."""
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'nonpublic_general_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('nonpublic_general_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('670', '^source_data_found$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_data_found(self, key, value):
    """Reverse - Source Data Found."""
    field_map = {
        'information_found': 'b',
        'uniform_resource_identifier': 'u',
        'bibliographic_record_control_number': 'w',
        'linkage': '6',
        'source_citation': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('information_found'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('source_citation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('672', '^title_related_to_the_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_title_related_to_the_entity(self, key, value):
    """Reverse - Title Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'date': 'f',
        'remainder_of_title': 'b',
        'bibliographic_record_control_number': 'w',
        'linkage': '6',
        'title': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': value.get('date'),
        'b': value.get('remainder_of_title'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('673', '^title_not_related_to_the_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_title_not_related_to_the_entity(self, key, value):
    """Reverse - Title Not Related to the Entity."""
    indicator_map2 = {str(x): str(x) for x in range(10)}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'date': 'f',
        'remainder_of_title': 'b',
        'bibliographic_record_control_number': 'w',
        'linkage': '6',
        'title': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'nonfiling_characters'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': value.get('date'),
        'b': value.get('remainder_of_title'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), value.get('nonfiling_characters', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('675', '^source_data_not_found$')
@utils.filter_values
def reverse_source_data_not_found(self, key, value):
    """Reverse - Source Data Not Found."""
    field_map = {
        'linkage': '6',
        'source_citation': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('source_citation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('678', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {"Administrative history": "1", "Biographical sketch": "0", "No information provided": "_"}
    field_map = {
        'expansion': 'b',
        'linkage': '6',
        'biographical_or_historical_data': 'a',
        'uniform_resource_identifier': 'u',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_data', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('expansion'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('biographical_or_historical_data')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_data'), value.get('type_of_data', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('680', '^public_general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_public_general_note(self, key, value):
    """Reverse - Public General Note."""
    field_map = {
        'explanatory_text': 'i',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'heading_or_subdivision_term': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': utils.reverse_force_list(
            value.get('heading_or_subdivision_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('681', '^subject_example_tracing_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_example_tracing_note(self, key, value):
    """Reverse - Subject Example Tracing Note."""
    field_map = {
        'explanatory_text': 'i',
        'linkage': '6',
        'subject_heading_or_subdivision_term': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('subject_heading_or_subdivision_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('682', '^deleted_heading_information$')
@utils.filter_values
def reverse_deleted_heading_information(self, key, value):
    """Reverse - Deleted Heading Information."""
    field_map = {
        'explanatory_text': 'i',
        'replacement_authority_record_control_number': '0',
        'linkage': '6',
        'replacement_heading': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '0': utils.reverse_force_list(
            value.get('replacement_authority_record_control_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('replacement_heading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('688', '^application_history_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_application_history_note(self, key, value):
    """Reverse - Application History Note."""
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'application_history_note': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('application_history_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
