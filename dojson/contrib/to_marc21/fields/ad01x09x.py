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

from ..model import to_marc21_authority


@to_marc21_authority.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""
    field_map = {
        'canceled_invalid_lc_control_number': 'z',
        'lc_control_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
        ),
        'a': value.get('lc_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('014', '^link_to_bibliographic_record_for_serial_or_multipart_item$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_link_to_bibliographic_record_for_serial_or_multipart_item(self, key, value):
    """Reverse - Link to Bibliographic Record for Serial or Multipart Item."""
    field_map = {
        'control_number_of_related_bibliographic_record': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('control_number_of_related_bibliographic_record'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    field_map = {
        'canceled_or_invalid_record_control_number': 'z',
        'record_control_number': 'a',
        'source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_or_invalid_record_control_number')
        ),
        'a': value.get('record_control_number'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('020', '^international_standard_book_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_book_number(self, key, value):
    """Reverse - International Standard Book Number."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'terms_of_availability': 'c',
        'canceled_invalid_isbn': 'z',
        'international_standard_book_number': 'a',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        'a': value.get('international_standard_book_number'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    field_map = {
        'incorrect_issn': 'y',
        'linkage': '6',
        'canceled_issn_l': 'm',
        'field_link_and_sequence_number': '8',
        'canceled_issn': 'z',
        'international_standard_serial_number': 'a',
        'issn_l': 'l',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        '6': value.get('linkage'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        'a': value.get('international_standard_serial_number'),
        'l': value.get('issn_l'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {"Source specified in subfield $2": "7", "Unspecified type of standard number or code": "8"}
    field_map = {
        'source_of_number_or_code': '2',
        'field_link_and_sequence_number': '8',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'terms_of_availability': 'c',
        'canceled_invalid_standard_number_or_code': 'z',
        'standard_number_or_code': 'a',
        'linkage': '6',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_number_or_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        'a': value.get('standard_number_or_code'),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '7' if 'type_of_standard_number_or_code' in value and
        not indicator_map1.get(value.get('type_of_standard_number_or_code')) and
        value.get('type_of_standard_number_or_code') == value.get('source_of_number_or_code')
        else indicator_map1.get(value.get('type_of_standard_number_or_code'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""
    field_map = {
        'number_of_work': 'a',
        'musical_notation': 'p',
        'system_code': '2',
        'role': 'e',
        'field_link_and_sequence_number': '8',
        'number_of_movement': 'b',
        'key_or_mode': 'r',
        'number_of_excerpt': 'c',
        'clef': 'g',
        'time_signature': 'o',
        'link_text': 'y',
        'linkage': '6',
        'general_note': 'q',
        'text_incipit': 't',
        'uniform_resource_identifier': 'u',
        'coded_validity_note': 's',
        'key_signature': 'n',
        'caption_or_heading': 'd',
        'public_note': 'z',
        'voice_instrument': 'm',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number_of_work'),
        'p': value.get('musical_notation'),
        '2': value.get('system_code'),
        'e': value.get('role'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_movement'),
        'r': value.get('key_or_mode'),
        'c': value.get('number_of_excerpt'),
        'g': value.get('clef'),
        'o': value.get('time_signature'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        'n': value.get('key_signature'),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'm': value.get('voice_instrument'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map2 = {"Exclusion ring": "1", "Not applicable": "_", "Outer ring": "0"}
    field_map = {
        'equinox': 'p',
        'linkage': '6',
        'beginning_date': 'x',
        'coordinates_easternmost_longitude': 'e',
        'field_link_and_sequence_number': '8',
        'distance_from_earth': 'r',
        'coordinates_westernmost_longitude': 'd',
        'coordinates_southernmost_latitude': 'g',
        'coordinates_northernmost_latitude': 'f',
        'ending_date': 'y',
        'declination_southern_limit': 'k',
        'declination_northern_limit': 'j',
        'g_ring_longitude': 't',
        'materials_specified': '3',
        'g_ring_latitude': 's',
        'source': '2',
        'authority_record_control_number_or_standard_number': '0',
        'right_ascension_western_limit': 'n',
        'name_of_extraterrestrial_body': 'z',
        'right_ascension_eastern_limit': 'm',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': value.get('equinox'),
        '6': value.get('linkage'),
        'x': value.get('beginning_date'),
        'e': value.get('coordinates_easternmost_longitude'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('distance_from_earth'),
        'd': value.get('coordinates_westernmost_longitude'),
        'g': value.get('coordinates_southernmost_latitude'),
        'f': value.get('coordinates_northernmost_latitude'),
        'y': value.get('ending_date'),
        'k': value.get('declination_southern_limit'),
        'j': value.get('declination_northern_limit'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        '3': value.get('materials_specified'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        '2': value.get('source'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'n': value.get('right_ascension_western_limit'),
        'z': value.get('name_of_extraterrestrial_body'),
        'm': value.get('right_ascension_eastern_limit'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('type_of_ring'), '_'),
    }


@to_marc21_authority.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    field_map = {
        'canceled_invalid_system_control_number': 'z',
        'system_control_number': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_system_control_number')
        ),
        'a': value.get('system_control_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    field_map = {
        'linkage': '6',
        'subject_heading_thesaurus_conventions': 'f',
        'description_conventions': 'e',
        'field_link_and_sequence_number': '8',
        'modifying_agency': 'd',
        'transcribing_agency': 'c',
        'original_cataloging_agency': 'a',
        'language_of_cataloging': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'f': value.get('subject_heading_thesaurus_conventions'),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'c': value.get('transcribing_agency'),
        'a': value.get('original_cataloging_agency'),
        'b': value.get('language_of_cataloging'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('042', '^authentication_code$')
@utils.filter_values
def reverse_authentication_code(self, key, value):
    """Reverse - Authentication Code."""
    field_map = {
        'authentication_code': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('authentication_code')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('043', '^geographic_area_code$')
@utils.filter_values
def reverse_geographic_area_code(self, key, value):
    """Reverse - Geographic Area Code."""
    field_map = {
        'linkage': '6',
        'iso_code': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'local_gac_code': 'b',
        'geographic_area_code': 'a',
        'source_of_local_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('045', '^time_period_of_heading$')
@utils.filter_values
def reverse_time_period_of_heading(self, key, value):
    """Reverse - Time Period of Heading."""
    indicator_map1 = {"Multiple single dates/times": "1", "Range of dates/times": "2", "Single date/time": "0", "Subfield $b or $c not present": "_"}
    field_map = {
        'time_period_code': 'a',
        'linkage': '6',
        'formatted_pre_9999_bc_time_period': 'c',
        'field_link_and_sequence_number': '8',
        'formatted_9999_bc_through_ce_time_period': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_code')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_time_period_in_subfield_b_or_c'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""
    field_map = {
        'ending_date_for_aggregated_content': 'p',
        'uniform_resource_identifier': 'u',
        'source_of_date_scheme': '2',
        'birth_date': 'f',
        'end_period': 't',
        'field_link_and_sequence_number': '8',
        'termination_date': 'r',
        'death_date': 'g',
        'single_or_starting_date_for_aggregated_content': 'o',
        'ending_date_created': 'l',
        'establishment_date': 'q',
        'beginning_or_single_date_created': 'k',
        'start_period': 's',
        'linkage': '6',
        'source_of_information': 'v',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': value.get('ending_date_for_aggregated_content'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '2': value.get('source_of_date_scheme'),
        'f': value.get('birth_date'),
        't': value.get('end_period'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('termination_date'),
        'g': value.get('death_date'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'l': value.get('ending_date_created'),
        'q': value.get('establishment_date'),
        'k': value.get('beginning_or_single_date_created'),
        's': value.get('start_period'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21_authority.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {"Library of Congress Classification": "_", "Source specified in subfield $2": "7", "U.S. Dept. of Defense Classification": "1"}
    field_map = {
        'code_source': '2',
        'field_link_and_sequence_number': '8',
        'populated_place_name': 'd',
        'geographic_classification_subarea_code': 'b',
        'geographic_classification_area_code': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('code_source'), '7') != '7' and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('code_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        'a': value.get('geographic_classification_area_code'),
        '6': value.get('linkage'),
        '$ind1': '7' if 'code_source' in value and
        not indicator_map1.get(value.get('code_source')) and
        value.get('code_source') == value.get('code_source')
        else indicator_map1.get(value.get('code_source'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('053', '^lc_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_lc_classification_number(self, key, value):
    """Reverse - LC Classification Number."""
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'linkage': '6',
        'explanatory_term': 'c',
        'institution_to_which_field_applies': '5',
        'classification_number_element_ending_number_of_span': 'b',
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('source_of_classification_number'), '_'),
    }


@to_marc21_authority.over('055', '^library_and_archives_canada_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_and_archives_canada_call_number(self, key, value):
    """Reverse - Library and Archives Canada Call Number."""
    indicator_map2 = {"Assigned by LAC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21_authority.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map2 = {"Assigned by NLM": "0", "Assigned by agency other than NLM": "4"}
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21_authority.over('065', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""
    field_map = {
        'linkage': '6',
        'explanatory_term': 'c',
        'institution_to_which_field_applies': '5',
        'classification_number_element_ending_number_of_span': 'b',
        'classification_number_element_single_number_or_beginning_of_span': 'a',
        'number_source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'a': value.get('classification_number_element_single_number_or_beginning_of_span'),
        '2': value.get('number_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""
    field_map = {
        'primary_g0_character_set': 'a',
        'alternate_g0_or_g1_character_set': 'c',
        'primary_g1_character_set': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('primary_g0_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
        'b': value.get('primary_g1_character_set'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""
    field_map = {
        'classification_number': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {"NAL subject category code list": "0", "No information provided": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'subject_category_code': 'a',
        'code_source': '2',
        'subject_category_code_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('code_source'), '7') != '7' and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('subject_category_code'),
        '2': value.get('code_source'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'code_source' in value and
        not indicator_map2.get(value.get('code_source')) and
        value.get('code_source') == value.get('code_source')
        else indicator_map2.get(value.get('code_source'), '_'),
    }


@to_marc21_authority.over('073', '^subdivision_usage$')
@utils.filter_values
def reverse_subdivision_usage(self, key, value):
    """Reverse - Subdivision Usage."""
    field_map = {
        'code_source': 'z',
        'subdivision_usage': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': value.get('code_source'),
        'a': utils.reverse_force_list(
            value.get('subdivision_usage')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "No information provided": "_"}
    field_map = {
        'edition_identifier': '2',
        'common_auxiliary_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'universal_decimal_classification_number': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('edition_identifier'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        'a': value.get('universal_decimal_classification_number'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('082', '^dewey_decimal_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_call_number(self, key, value):
    """Reverse - Dewey Decimal Call Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
        'classification_number': 'a',
        'edition_number': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
        'a': value.get('classification_number'),
        '2': value.get('edition_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number')
        else indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21_authority.over('083', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'linkage': '6',
        'explanatory_term': 'c',
        'institution_to_which_field_applies': '5',
        'classification_number_element_ending_number_of_span': 'b',
        'table_identification_table_number': 'z',
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'edition_number': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'z': value.get('table_identification_table_number'),
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        '2': value.get('edition_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number')
        else indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_classification_number'), '_'),
    }


@to_marc21_authority.over('086', '^government_document_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_call_number(self, key, value):
    """Reverse - Government Document Call Number."""
    field_map = {
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'volumes_dates_to_which_call_number_applies': 'd',
        'canceled_invalid_call_number': 'z',
        'call_number': 'a',
        'number_source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_call_number')
        ),
        'a': value.get('call_number'),
        '2': value.get('number_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('087', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    field_map = {
        'number_source': '2',
        'explanatory_information': 'c',
        'field_link_and_sequence_number': '8',
        'classification_number_element_ending_number_of_span': 'b',
        'classification_number_element_single_number_of_beginning_number_of_span': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('number_source'),
        'c': value.get('explanatory_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'a': value.get('classification_number_element_single_number_of_beginning_number_of_span'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }
