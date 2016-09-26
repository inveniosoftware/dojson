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

from ..model import marc21_holdings


@marc21_holdings.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    """Media Type."""
    return {
        'media_type_term': utils.force_list(
            value.get('a')
        ),
        'media_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_holdings.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    """Carrier Type."""
    return {
        'carrier_type_term': utils.force_list(
            value.get('a')
        ),
        'carrier_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_holdings.over('restrictions_on_access_note', '^506..')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    return {
        'terms_governing_access': value.get('a'),
        'physical_access_provisions': utils.force_list(
            value.get('c')
        ),
        'jurisdiction': utils.force_list(
            value.get('b')
        ),
        'authorization': utils.force_list(
            value.get('e')
        ),
        'authorized_users': utils.force_list(
            value.get('d')
        ),
        'standardized_terminology_for_access_restriction': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21_holdings.over('system_details_note', '^538..')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    """System Details Note."""
    return {
        'system_details_note': value.get('a'),
        'display_text': value.get('i'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21_holdings.over('immediate_source_of_acquisition_note', '^541..')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    return {
        'source_of_acquisition': value.get('a'),
        'method_of_acquisition': value.get('c'),
        'address': value.get('b'),
        'accession_number': value.get('e'),
        'date_of_acquisition': value.get('d'),
        'owner': value.get('f'),
        'purchase_price': value.get('h'),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_holdings.over('ownership_and_custodial_history', '^561[10_].')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {
        '#': 'No information provided',
        '0': 'Private',
        '1': 'Not private'}
    return {
        'history': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@marc21_holdings.over('copy_and_version_identification_note', '^562..')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    """Copy and Version Identification Note."""
    return {
        'identifying_markings': utils.force_list(
            value.get('a')
        ),
        'version_identification': utils.force_list(
            value.get('c')
        ),
        'copy_identification': utils.force_list(
            value.get('b')
        ),
        'number_of_copies': utils.force_list(
            value.get('e')
        ),
        'presentation_format': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_holdings.over('binding_information', '^563..')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    """Binding Information."""
    return {
        'binding_note': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21_holdings.over('action_note', '^583..')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    return {
        'action': value.get('a'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'time_date_of_action': utils.force_list(
            value.get('c')
        ),
        'action_identification': utils.force_list(
            value.get('b')
        ),
        'contingency_for_action': utils.force_list(
            value.get('e')
        ),
        'action_interval': utils.force_list(
            value.get('d')
        ),
        'authorization': utils.force_list(
            value.get('f')
        ),
        'method_of_action': utils.force_list(
            value.get('i')
        ),
        'jurisdiction': utils.force_list(
            value.get('h')
        ),
        'action_agent': utils.force_list(
            value.get('k')
        ),
        'site_of_action': utils.force_list(
            value.get('j')
        ),
        'status': utils.force_list(
            value.get('l')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21_holdings.over('holdings_coded_data_values', '^841..')
@utils.filter_values
def holdings_coded_data_values(self, key, value):
    """Holdings Coded Data Values."""
    return {
        'type_of_record': value.get('a'),
        'fixed_length_data_elements': value.get('b'),
        'encoding_level': value.get('e'),
    }


@marc21_holdings.over('textual_physical_form_designator', '^842..')
@utils.filter_values
def textual_physical_form_designator(self, key, value):
    """Textual Physical Form Designator."""
    return {
        'textual_physical_form_designator': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_holdings.over('reproduction_note', '^843..')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    """Reproduction Note."""
    return {
        'type_of_reproduction': value.get('a'),
        'agency_responsible_for_reproduction': utils.force_list(
            value.get('c')),
        'place_of_reproduction': utils.force_list(
            value.get('b')),
        'physical_description_of_reproduction': value.get('e'),
        'date_of_reproduction': value.get('d'),
        'series_statement_of_reproduction': utils.force_list(
            value.get('f')),
        'dates_of_publication_and_or_sequential_'
        'designation_of_issues_reproduced': utils.force_list(
            value.get('m')),
        'note_about_reproduction': utils.force_list(
            value.get('n')),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21_holdings.over('name_of_unit', '^844..')
@utils.filter_values
def name_of_unit(self, key, value):
    """Name of Unit."""
    return {
        'name_of_unit': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_holdings.over('terms_governing_use_and_reproduction_note', '^845..')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    return {
        'terms_governing_use_and_reproduction': value.get('a'),
        'authorization': value.get('c'),
        'jurisdiction': value.get('b'),
        'authorized_users': value.get('d'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }
