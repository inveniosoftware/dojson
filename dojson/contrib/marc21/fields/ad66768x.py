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
    return {
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
    return {
        'source_citation': value.get('a'),
        'information_found': value.get('b'),
        'uniform_resource_identifier': value.get('u'),
        'bibliographic_record_control': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('source_data_not_found', '^675..')
@utils.filter_values
def source_data_not_found(self, key, value):
    """Source Data Not Found."""
    # TODO consider joining with source_data_found as source_data
    return {
        'source_citation': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('bibliographical_or_historical_data', '^678[_01].')
@utils.for_each_value
@utils.filter_values
def bibliographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {
        "#": "No information provided",
        "1": "Biographical sketch",
        "2": "Administrative history",
    }
    return {
        'bibliographical_or_historical_data': value.get('a'),
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
    return {
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
    return {
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
    return {
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
    return {
        'application_history_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
    }
