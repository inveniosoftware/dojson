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


@to_marc21_authority.over(
    '640', '^series_dates_of_publication_and_or_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_dates_of_publication_and_or_sequential_designation(
        self, key, value):
    """Reverse - Series Dates of Publication and/or Sequential Designation."""
    field_map = {
        'dates_of_publication_and_or_sequential_designation': 'a',
        'source_of_information': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        'Formatted_style': '0',
        'Unformatted style': '1',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': value.get('source_of_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('note_format_style'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('641', '^series_numbering_peculiarities$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_numbering_peculiarities(self, key, value):
    """Reverse - Series Numbering Peculiarities."""
    field_map = {
        'numbering_peculiarities_note': 'a',
        'source_of_information': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('numbering_peculiarities_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': value.get('source_of_information'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('642', '^series_numbering_example$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_numbering_example(self, key, value):
    """Reverse - Series Numbering Example."""
    field_map = {
        'series_numbering_example': 'a',
        'volumes_dates_to_which_series_numbering_example_applies': 'd',
        'institution_copy_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('series_numbering_example'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_series_numbering_example_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('643', '^series_place_and_publisher_issuing_body$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_place_and_publisher_issuing_body(self, key, value):
    """Reverse - Series Place and Publisher/Issuing Body."""
    field_map = {
        'place': 'a',
        'publisher_issuing_body': 'b',
        'volumes_dates_to_which_place_and_publisher_issuing_body_apply': 'd',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('place')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('publisher_issuing_body')
        ),
        'd': value.get('volumes_dates_to_which_place_and_publisher_issuing_body_apply'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('644', '^series_analysis_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_analysis_practice(self, key, value):
    """Reverse - Series Analysis Practice."""
    field_map = {
        'series_analysis_practice': 'a',
        'exceptions_to_analysis_practice': 'b',
        'volumes_dates_to_which_analysis_practice_applies': 'd',
        'institution_copy_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('series_analysis_practice'),
        'b': value.get('exceptions_to_analysis_practice'),
        'd': value.get('volumes_dates_to_which_analysis_practice_applies'),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('645', '^series_tracing_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_tracing_practice(self, key, value):
    """Reverse - Series Tracing Practice."""
    field_map = {
        'series_tracing_practice': 'a',
        'volumes_dates_to_which_tracing_practice_applies': 'd',
        'institution_copy_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('series_tracing_practice'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_copy_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_tracing_practice_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('646', '^series_classification_practice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_series_classification_practice(self, key, value):
    """Reverse - Series Classification Practice."""
    field_map = {
        'series_classification_practice': 'a',
        'volumes_dates_to_which_classification_practice_applies': 'd',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('series_classification_practice'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_classification_practice_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('663', '^complex_see_also_reference_name$')
@utils.filter_values
def reverse_complex_see_also_reference_name(self, key, value):
    """Reverse - Complex See Also Reference-Name."""
    field_map = {
        'explanatory_text': 'a',
        'heading_referred_to': 'b',
        'title_referred_to': 't',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        't': utils.reverse_force_list(
            value.get('title_referred_to')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('664', '^complex_see_reference_name$')
@utils.filter_values
def reverse_complex_see_reference_name(self, key, value):
    """Reverse - Complex See Reference-Name."""
    field_map = {
        'explanatory_text': 'a',
        'heading_referred_to': 'b',
        'title_referred_to': 't',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        't': utils.reverse_force_list(
            value.get('title_referred_to')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('665', '^history_reference$')
@utils.filter_values
def reverse_history_reference(self, key, value):
    """Reverse - History Reference."""
    field_map = {
        'history_reference': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('history_reference')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('666', '^general_explanatory_reference_name$')
@utils.filter_values
def reverse_general_explanatory_reference_name(self, key, value):
    """Reverse - General Explanatory Reference-Name."""
    field_map = {
        'general_explanatory_reference': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('general_explanatory_reference')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('667', '^nonpublic_general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_nonpublic_general_note(self, key, value):
    """Reverse - Nonpublic General Note."""
    field_map = {
        'nonpublic_general_note': 'a',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('nonpublic_general_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('670', '^source_data_found$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_data_found(self, key, value):
    """Reverse - Source Data Found."""
    field_map = {
        'source_citation': 'a',
        'information_found': 'b',
        'uniform_resource_identifier': 'u',
        'bibliographic_record_control_number': 'w',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('source_citation'),
        'b': value.get('information_found'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('672', '^title_related_to_the_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_title_related_to_the_entity(self, key, value):
    """Reverse - Title Related to the Entity."""
    field_map = {
        'title': 'a',
        'remainder_of_title': 'b',
        'date': 'f',
        'bibliographic_record_control_number': 'w',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
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
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'f': value.get('date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('673', '^title_not_related_to_the_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_title_not_related_to_the_entity(self, key, value):
    """Reverse - Title Not Related to the Entity."""
    field_map = {
        'title': 'a',
        'remainder_of_title': 'b',
        'date': 'f',
        'bibliographic_record_control_number': 'w',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
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

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('title'),
        'b': value.get('remainder_of_title'),
        'f': value.get('date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21_authority.over('675', '^source_data_not_found$')
@utils.filter_values
def reverse_source_data_not_found(self, key, value):
    """Reverse - Source Data Not Found."""
    field_map = {
        'source_citation': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('source_citation')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('678', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    field_map = {
        'biographical_or_historical_data': 'a',
        'expansion': 'b',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    indicator_map1 = {
        'No information provided': '_',
        'Biographical sketch': '1',
        'Administrative history': '2',
    }
    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('biographical_or_historical_data')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('expansion'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_data'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('680', '^public_general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_public_general_note(self, key, value):
    """Reverse - Public General Note."""
    field_map = {
        'heading_or_subdivision_term': 'a',
        'explanatory_text': 'i',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('heading_or_subdivision_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('681', '^subject_example_tracing_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_example_tracing_note(self, key, value):
    """Reverse - Subject Example Tracing Note."""
    field_map = {
        'subject_heading_or_subdivision_term': 'a',
        'explanatory_text': 'i',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('subject_heading_or_subdivision_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('682', '^deleted_heading_information$')
@utils.filter_values
def reverse_deleted_heading_information(self, key, value):
    """Reverse - Deleted Heading Information."""
    field_map = {
        'replacement_heading': 'a',
        'explanatory_text': 'i',
        'replacement_authority_record_control_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('replacement_heading')
        ),
        '0': utils.reverse_force_list(
            value.get('replacement_authority_record_control_number')
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


@to_marc21_authority.over('688', '^application_history_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_application_history_note(self, key, value):
    """Reverse - Application History Note."""
    field_map = {
        'application_history_note': 'a',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('application_history_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }
