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


@to_marc21_liberal_authority.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""
    field_map = {
        'lc_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'canceled_invalid_lc_control_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('lc_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
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
        'linkage': '6',
        'control_number_of_related_bibliographic_record': 'a',
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
        'a': value.get('control_number_of_related_bibliographic_record'),
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
        'field_link_and_sequence_number': '8',
        'source': '2',
        'canceled_or_invalid_record_control_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
        'z': utils.reverse_force_list(
            value.get('canceled_or_invalid_record_control_number')
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
        'qualifying_information': 'q',
        'international_standard_book_number': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'terms_of_availability': 'c',
        'canceled_invalid_isbn': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'a': value.get('international_standard_book_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
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
        'incorrect_issn': 'y',
        'international_standard_serial_number': 'a',
        'issn_l': 'l',
        'canceled_issn_l': 'm',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'canceled_issn': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        'a': value.get('international_standard_serial_number'),
        'l': value.get('issn_l'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
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
        'additional_codes_following_the_standard_number_or_code': 'd',
        'standard_number_or_code': 'a',
        'qualifying_information': 'q',
        'linkage': '6',
        'terms_of_availability': 'c',
        'field_link_and_sequence_number': '8',
        'source_of_number_or_code': '2',
        'canceled_invalid_standard_number_or_code': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_standard_number_or_code', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'a': value.get('standard_number_or_code'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '6': value.get('linkage'),
        'c': value.get('terms_of_availability'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_number_or_code'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
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
        'link_text': 'y',
        'role': 'e',
        'key_or_mode': 'r',
        'clef': 'g',
        'number_of_work': 'a',
        'number_of_excerpt': 'c',
        'field_link_and_sequence_number': '8',
        'public_note': 'z',
        'system_code': '2',
        'coded_validity_note': 's',
        'text_incipit': 't',
        'key_signature': 'n',
        'caption_or_heading': 'd',
        'voice_instrument': 'm',
        'uniform_resource_identifier': 'u',
        'musical_notation': 'p',
        'linkage': '6',
        'number_of_movement': 'b',
        'time_signature': 'o',
        'general_note': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'e': value.get('role'),
        'r': value.get('key_or_mode'),
        'g': value.get('clef'),
        'a': value.get('number_of_work'),
        'c': value.get('number_of_excerpt'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('system_code'),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'n': value.get('key_signature'),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        'm': value.get('voice_instrument'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'p': value.get('musical_notation'),
        '6': value.get('linkage'),
        'b': value.get('number_of_movement'),
        'o': value.get('time_signature'),
        'q': utils.reverse_force_list(
            value.get('general_note')
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
        'ending_date': 'y',
        'coordinates_westernmost_longitude': 'd',
        'distance_from_earth': 'r',
        'declination_southern_limit': 'k',
        'g_ring_latitude': 's',
        'coordinates_southernmost_latitude': 'g',
        'coordinates_easternmost_longitude': 'e',
        'right_ascension_western_limit': 'n',
        'field_link_and_sequence_number': '8',
        'source': '2',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'coordinates_northernmost_latitude': 'f',
        'right_ascension_eastern_limit': 'm',
        'declination_northern_limit': 'j',
        'g_ring_longitude': 't',
        'linkage': '6',
        'equinox': 'p',
        'name_of_extraterrestrial_body': 'z',
        'beginning_date': 'x',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'type_of_ring'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'y': value.get('ending_date'),
        'd': value.get('coordinates_westernmost_longitude'),
        'r': value.get('distance_from_earth'),
        'k': value.get('declination_southern_limit'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        'g': value.get('coordinates_southernmost_latitude'),
        'e': value.get('coordinates_easternmost_longitude'),
        'n': value.get('right_ascension_western_limit'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': value.get('coordinates_northernmost_latitude'),
        'm': value.get('right_ascension_eastern_limit'),
        'j': value.get('declination_northern_limit'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        '6': value.get('linkage'),
        'p': value.get('equinox'),
        'z': value.get('name_of_extraterrestrial_body'),
        'x': value.get('beginning_date'),
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
        'linkage': '6',
        'system_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'canceled_invalid_system_control_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('system_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_system_control_number')
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
        'modifying_agency': 'd',
        'original_cataloging_agency': 'a',
        'subject_heading_thesaurus_conventions': 'f',
        'description_conventions': 'e',
        'linkage': '6',
        'language_of_cataloging': 'b',
        'field_link_and_sequence_number': '8',
        'transcribing_agency': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'a': value.get('original_cataloging_agency'),
        'f': value.get('subject_heading_thesaurus_conventions'),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        '6': value.get('linkage'),
        'b': value.get('language_of_cataloging'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('transcribing_agency'),
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

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

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
        'authority_record_control_number_or_standard_number': '0',
        'geographic_area_code': 'a',
        'linkage': '6',
        'local_gac_code': 'b',
        'field_link_and_sequence_number': '8',
        'source_of_local_code': '2',
        'iso_code': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        'c': utils.reverse_force_list(
            value.get('iso_code')
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
        'linkage': '6',
        'time_period_code': 'a',
        'field_link_and_sequence_number': '8',
        'formatted_pre_9999_bc_time_period': 'c',
        'formatted_9999_bc_through_ce_time_period': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period_in_subfield_b_or_c', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('time_period_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
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
        'start_period': 's',
        'beginning_or_single_date_created': 'k',
        'death_date': 'g',
        'source_of_information': 'v',
        'source_of_date_scheme': '2',
        'field_link_and_sequence_number': '8',
        'termination_date': 'r',
        'establishment_date': 'q',
        'birth_date': 'f',
        'ending_date_created': 'l',
        'uniform_resource_identifier': 'u',
        'end_period': 't',
        'linkage': '6',
        'ending_date_for_aggregated_content': 'p',
        'single_or_starting_date_for_aggregated_content': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        's': value.get('start_period'),
        'k': value.get('beginning_or_single_date_created'),
        'g': value.get('death_date'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_date_scheme'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('termination_date'),
        'q': value.get('establishment_date'),
        'f': value.get('birth_date'),
        'l': value.get('ending_date_created'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        'p': value.get('ending_date_for_aggregated_content'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
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
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'populated_place_name': 'd',
        'geographic_classification_area_code': 'a',
        'linkage': '6',
        'geographic_classification_subarea_code': 'b',
        'field_link_and_sequence_number': '8',
        'code_source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['code_source', 'None'])

    if (indicator_map1.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        'a': value.get('geographic_classification_area_code'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('code_source'),
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
        'linkage': '6',
        'classification_number_element_ending_number_of_span': 'b',
        'field_link_and_sequence_number': '8',
        'explanatory_term': 'c',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_classification_number'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        '6': value.get('linkage'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('explanatory_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'explanatory_term': 'c',
        'linkage': '6',
        'classification_number_element_ending_number_of_span': 'b',
        'field_link_and_sequence_number': '8',
        'number_source': '2',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_or_beginning_of_span'),
        'c': value.get('explanatory_term'),
        '6': value.get('linkage'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('number_source'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

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
        'linkage': '6',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'volumes_dates_to_which_call_number_applies': 'd',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'b': value.get('item_number'),
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
        'linkage': '6',
        'subject_category_code': 'a',
        'field_link_and_sequence_number': '8',
        'code_source': '2',
        'subject_category_code_subdivision': 'x',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'code_source'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if (indicator_map2.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('subject_category_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('code_source'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
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
        'linkage': '6',
        'subdivision_usage': 'a',
        'field_link_and_sequence_number': '8',
        'code_source': 'z',
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
            value.get('subdivision_usage')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': value.get('code_source'),
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
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'edition_identifier': '2',
        'common_auxiliary_subdivision': 'x',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('universal_decimal_classification_number'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_identifier'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
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
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'edition_number': '2',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_number'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'explanatory_term': 'c',
        'linkage': '6',
        'classification_number_element_ending_number_of_span': 'b',
        'field_link_and_sequence_number': '8',
        'edition_number': '2',
        'table_identification_table_number': 'z',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
        'c': value.get('explanatory_term'),
        '6': value.get('linkage'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_number'),
        'z': value.get('table_identification_table_number'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'volumes_dates_to_which_call_number_applies': 'd',
        'call_number': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'number_source': '2',
        'canceled_invalid_call_number': 'z',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('call_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('number_source'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_call_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'linkage': '6',
        'classification_number_element_ending_number_of_span': 'b',
        'field_link_and_sequence_number': '8',
        'number_source': '2',
        'explanatory_information': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number_element_single_number_of_beginning_number_of_span'),
        '6': value.get('linkage'),
        'b': value.get('classification_number_element_ending_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('number_source'),
        'c': value.get('explanatory_information'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
