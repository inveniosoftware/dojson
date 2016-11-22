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
from dojson.contrib.marc21_liberal.utils import liberal_map_order

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""

    field_map = {
        'lc_control_number': 'a',
        'canceled_invalid_lc_control_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('lc_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
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


@to_marc21_liberal_authority.over('014', '^link_to_bibliographic_record_for_serial_or_multipart_item$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_link_to_bibliographic_record_for_serial_or_multipart_item(self, key, value):
    """Reverse - Link to Bibliographic Record for Serial or Multipart Item."""

    field_map = {
        'control_number_of_related_bibliographic_record': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('control_number_of_related_bibliographic_record'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""

    field_map = {
        'record_control_number': 'a',
        'canceled_or_invalid_record_control_number': 'z',
        'source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_or_invalid_record_control_number')
        ),
        '2': value.get('source'),
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


@to_marc21_liberal_authority.over('020', '^international_standard_book_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_book_number(self, key, value):
    """Reverse - International Standard Book Number."""

    field_map = {
        'international_standard_book_number': 'a',
        'terms_of_availability': 'c',
        'qualifying_information': 'q',
        'canceled_invalid_isbn': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_book_number'),
        'c': value.get('terms_of_availability'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""

    field_map = {
        'international_standard_serial_number': 'a',
        'issn_l': 'l',
        'canceled_issn_l': 'm',
        'incorrect_issn': 'y',
        'canceled_issn': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_serial_number'),
        'l': value.get('issn_l'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {"Source specified in subfield $2": "7", "Unspecified type of standard number or code": "8"}

    field_map = {
        'standard_number_or_code': 'a',
        'terms_of_availability': 'c',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'qualifying_information': 'q',
        'canceled_invalid_standard_number_or_code': 'z',
        'source_of_number_or_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_standard_number_or_code', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('standard_number_or_code'),
        'c': value.get('terms_of_availability'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        '2': value.get('source_of_number_or_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'type_of_standard_number_or_code' in value and
        not indicator_map1.get(value.get('type_of_standard_number_or_code')) and
        value.get('type_of_standard_number_or_code') == value.get('source_of_number_or_code') and
        field_map.get('type_of_standard_number_or_code') in order
        else indicator_map1.get(value.get('type_of_standard_number_or_code'), value.get('type_of_standard_number_or_code', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""

    field_map = {
        'number_of_work': 'a',
        'number_of_movement': 'b',
        'number_of_excerpt': 'c',
        'caption_or_heading': 'd',
        'role': 'e',
        'clef': 'g',
        'voice_instrument': 'm',
        'key_signature': 'n',
        'time_signature': 'o',
        'musical_notation': 'p',
        'general_note': 'q',
        'key_or_mode': 'r',
        'coded_validity_note': 's',
        'text_incipit': 't',
        'uniform_resource_identifier': 'u',
        'link_text': 'y',
        'public_note': 'z',
        'system_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number_of_work'),
        'b': value.get('number_of_movement'),
        'c': value.get('number_of_excerpt'),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        'e': value.get('role'),
        'g': value.get('clef'),
        'm': value.get('voice_instrument'),
        'n': value.get('key_signature'),
        'o': value.get('time_signature'),
        'p': value.get('musical_notation'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        'r': value.get('key_or_mode'),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('system_code'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map2 = {"Exclusion ring": "1", "Not applicable": "_", "Outer ring": "0"}

    field_map = {
        'coordinates_westernmost_longitude': 'd',
        'coordinates_easternmost_longitude': 'e',
        'coordinates_northernmost_latitude': 'f',
        'coordinates_southernmost_latitude': 'g',
        'declination_northern_limit': 'j',
        'declination_southern_limit': 'k',
        'right_ascension_eastern_limit': 'm',
        'right_ascension_western_limit': 'n',
        'equinox': 'p',
        'distance_from_earth': 'r',
        'g_ring_latitude': 's',
        'g_ring_longitude': 't',
        'beginning_date': 'x',
        'ending_date': 'y',
        'name_of_extraterrestrial_body': 'z',
        'authority_record_control_number_or_standard_number': '0',
        'source': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'type_of_ring'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('coordinates_westernmost_longitude'),
        'e': value.get('coordinates_easternmost_longitude'),
        'f': value.get('coordinates_northernmost_latitude'),
        'g': value.get('coordinates_southernmost_latitude'),
        'j': value.get('declination_northern_limit'),
        'k': value.get('declination_southern_limit'),
        'm': value.get('right_ascension_eastern_limit'),
        'n': value.get('right_ascension_western_limit'),
        'p': value.get('equinox'),
        'r': value.get('distance_from_earth'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        'x': value.get('beginning_date'),
        'y': value.get('ending_date'),
        'z': value.get('name_of_extraterrestrial_body'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': value.get('source'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('type_of_ring'), value.get('type_of_ring', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""

    field_map = {
        'system_control_number': 'a',
        'canceled_invalid_system_control_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('system_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_system_control_number')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""

    field_map = {
        'original_cataloging_agency': 'a',
        'language_of_cataloging': 'b',
        'transcribing_agency': 'c',
        'modifying_agency': 'd',
        'description_conventions': 'e',
        'subject_heading_thesaurus_conventions': 'f',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_cataloging_agency'),
        'b': value.get('language_of_cataloging'),
        'c': value.get('transcribing_agency'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        'f': value.get('subject_heading_thesaurus_conventions'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('042', '^authentication_code$')
@utils.filter_values
def reverse_authentication_code(self, key, value):
    """Reverse - Authentication Code."""

    field_map = {
        'authentication_code': 'a',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('authentication_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('043', '^geographic_area_code$')
@utils.filter_values
def reverse_geographic_area_code(self, key, value):
    """Reverse - Geographic Area Code."""

    field_map = {
        'geographic_area_code': 'a',
        'local_gac_code': 'b',
        'iso_code': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_local_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('045', '^time_period_of_heading$')
@utils.filter_values
def reverse_time_period_of_heading(self, key, value):
    """Reverse - Time Period of Heading."""
    indicator_map1 = {"Multiple single dates/times": "1", "Range of dates/times": "2", "Single date/time": "0", "Subfield $b or $c not present": "_"}

    field_map = {
        'time_period_code': 'a',
        'formatted_9999_bc_through_ce_time_period': 'b',
        'formatted_pre_9999_bc_time_period': 'c',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_time_period_in_subfield_b_or_c', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_code')
        ),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_time_period_in_subfield_b_or_c'), value.get('type_of_time_period_in_subfield_b_or_c', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""

    field_map = {
        'birth_date': 'f',
        'death_date': 'g',
        'beginning_or_single_date_created': 'k',
        'ending_date_created': 'l',
        'single_or_starting_date_for_aggregated_content': 'o',
        'ending_date_for_aggregated_content': 'p',
        'establishment_date': 'q',
        'termination_date': 'r',
        'start_period': 's',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
        'source_of_information': 'v',
        'source_of_date_scheme': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'f': value.get('birth_date'),
        'g': value.get('death_date'),
        'k': value.get('beginning_or_single_date_created'),
        'l': value.get('ending_date_created'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'p': value.get('ending_date_for_aggregated_content'),
        'q': value.get('establishment_date'),
        'r': value.get('termination_date'),
        's': value.get('start_period'),
        't': value.get('end_period'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_date_scheme'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'volumes_dates_to_which_call_number_applies': 'd',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {"Library of Congress Classification": "_", "Source specified in subfield $2": "7", "U.S. Dept. of Defense Classification": "1"}

    field_map = {
        'geographic_classification_area_code': 'a',
        'geographic_classification_subarea_code': 'b',
        'populated_place_name': 'd',
        'code_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['code_source', 'None'])

    if (indicator_map1.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_classification_area_code'),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        '2': value.get('code_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'code_source' in value and
        not indicator_map1.get(value.get('code_source')) and
        value.get('code_source') == value.get('code_source') and
        field_map.get('code_source') in order
        else indicator_map1.get(value.get('code_source'), value.get('code_source', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('053', '^lc_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_lc_classification_number(self, key, value):
    """Reverse - LC Classification Number."""
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}

    field_map = {
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'classification_number_element_ending_number_of_span': 'b',
        'explanatory_term': 'c',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'c': value.get('explanatory_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('source_of_classification_number'), value.get('source_of_classification_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('055', '^library_and_archives_canada_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_and_archives_canada_call_number(self, key, value):
    """Reverse - Library and Archives Canada Call Number."""
    indicator_map2 = {"Assigned by LAC": "0", "Assigned by agency other than LC": "4"}

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'volumes_dates_to_which_call_number_applies': 'd',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map2 = {"Assigned by NLM": "0", "Assigned by agency other than NLM": "4"}

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'volumes_dates_to_which_call_number_applies': 'd',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('065', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""

    field_map = {
        'classification_number_element_single_number_or_beginning_of_span': 'a',
        'classification_number_element_ending_number_of_span': 'b',
        'explanatory_term': 'c',
        'number_source': '2',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_or_beginning_of_span'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'c': value.get('explanatory_term'),
        '2': value.get('number_source'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""

    field_map = {
        'primary_g0_character_set': 'a',
        'primary_g1_character_set': 'b',
        'alternate_g0_or_g1_character_set': 'c',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('primary_g0_character_set'),
        'b': value.get('primary_g1_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'volumes_dates_to_which_call_number_applies': 'd',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {"NAL subject category code list": "0", "No information provided": "_", "Source specified in subfield $2": "7"}

    field_map = {
        'subject_category_code': 'a',
        'subject_category_code_subdivision': 'x',
        'code_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'code_source'])

    if (indicator_map2.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('subject_category_code'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        '2': value.get('code_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'code_source' in value and
        not indicator_map2.get(value.get('code_source')) and
        value.get('code_source') == value.get('code_source') and
        field_map.get('code_source') in order
        else indicator_map2.get(value.get('code_source'), value.get('code_source', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('073', '^subdivision_usage$')
@utils.filter_values
def reverse_subdivision_usage(self, key, value):
    """Reverse - Subdivision Usage."""

    field_map = {
        'subdivision_usage': 'a',
        'code_source': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('subdivision_usage')
        ),
        'z': value.get('code_source'),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "No information provided": "_"}

    field_map = {
        'universal_decimal_classification_number': 'a',
        'item_number': 'b',
        'common_auxiliary_subdivision': 'x',
        'edition_identifier': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_edition', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('universal_decimal_classification_number'),
        'b': value.get('item_number'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '2': value.get('edition_identifier'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_edition'), value.get('type_of_edition', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('082', '^dewey_decimal_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_call_number(self, key, value):
    """Reverse - Dewey Decimal Call Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4", "No information provided": "_"}

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'volumes_dates_to_which_call_number_applies': 'd',
        'edition_number': '2',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_edition', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        '2': value.get('edition_number'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number') and
        field_map.get('type_of_edition') in order
        else indicator_map1.get(value.get('type_of_edition'), value.get('type_of_edition', '_')),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('083', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}

    field_map = {
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'classification_number_element_ending_number_of_span': 'b',
        'explanatory_term': 'c',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'table_identification_table_number': 'z',
        'edition_number': '2',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['type_of_edition', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'c': value.get('explanatory_term'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'z': value.get('table_identification_table_number'),
        '2': value.get('edition_number'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number') and
        field_map.get('type_of_edition') in order
        else indicator_map1.get(value.get('type_of_edition'), value.get('type_of_edition', '_')),
        '$ind2': indicator_map2.get(value.get('source_of_classification_number'), value.get('source_of_classification_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('086', '^government_document_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_call_number(self, key, value):
    """Reverse - Government Document Call Number."""

    field_map = {
        'call_number': 'a',
        'volumes_dates_to_which_call_number_applies': 'd',
        'canceled_invalid_call_number': 'z',
        'number_source': '2',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('call_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_call_number')
        ),
        '2': value.get('number_source'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal_authority.over('087', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""

    field_map = {
        'classification_number_element_single_number_of_beginning_number_of_span': 'a',
        'classification_number_element_ending_number_of_span': 'b',
        'explanatory_information': 'c',
        'number_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = liberal_map_order(field_map, value, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_of_beginning_number_of_span'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        'c': value.get('explanatory_information'),
        '2': value.get('number_source'),
        '6': value.get('linkage'),
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
