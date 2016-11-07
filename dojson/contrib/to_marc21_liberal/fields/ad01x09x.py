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
        'field_link_and_sequence_number': '8',
        'canceled_invalid_lc_control_number': 'z',
        'lc_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
        ),
        'a': value.get('lc_control_number'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'control_number_of_related_bibliographic_record': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('control_number_of_related_bibliographic_record'),
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
        'source': '2',
        'field_link_and_sequence_number': '8',
        'canceled_or_invalid_record_control_number': 'z',
        'record_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_or_invalid_record_control_number')
        ),
        'a': value.get('record_control_number'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'qualifying_information': 'q',
        'terms_of_availability': 'c',
        'canceled_invalid_isbn': 'z',
        'international_standard_book_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        'a': value.get('international_standard_book_number'),
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
        'issn_l': 'l',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'canceled_issn_l': 'm',
        'incorrect_issn': 'y',
        'canceled_issn': 'z',
        'international_standard_serial_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('issn_l'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        'a': value.get('international_standard_serial_number'),
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
        'source_of_number_or_code': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'qualifying_information': 'q',
        'terms_of_availability': 'c',
        'canceled_invalid_standard_number_or_code': 'z',
        'standard_number_or_code': 'a',
        'additional_codes_following_the_standard_number_or_code': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_standard_number_or_code', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_number_or_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        'a': value.get('standard_number_or_code'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
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
        'number_of_movement': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'key_or_mode': 'r',
        'voice_instrument': 'm',
        'general_note': 'q',
        'number_of_excerpt': 'c',
        'link_text': 'y',
        'coded_validity_note': 's',
        'caption_or_heading': 'd',
        'role': 'e',
        'system_code': '2',
        'time_signature': 'o',
        'number_of_work': 'a',
        'public_note': 'z',
        'musical_notation': 'p',
        'text_incipit': 't',
        'uniform_resource_identifier': 'u',
        'clef': 'g',
        'key_signature': 'n',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('number_of_movement'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'r': value.get('key_or_mode'),
        'm': value.get('voice_instrument'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        'c': value.get('number_of_excerpt'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        'e': value.get('role'),
        '2': value.get('system_code'),
        'o': value.get('time_signature'),
        'a': value.get('number_of_work'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'p': value.get('musical_notation'),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'g': value.get('clef'),
        'n': value.get('key_signature'),
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
        'name_of_extraterrestrial_body': 'z',
        'equinox': 'p',
        'g_ring_latitude': 's',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'distance_from_earth': 'r',
        'right_ascension_eastern_limit': 'm',
        'g_ring_longitude': 't',
        'ending_date': 'y',
        'materials_specified': '3',
        'coordinates_westernmost_longitude': 'd',
        'coordinates_easternmost_longitude': 'e',
        'source': '2',
        'beginning_date': 'x',
        'coordinates_northernmost_latitude': 'f',
        'authority_record_control_number_or_standard_number': '0',
        'right_ascension_western_limit': 'n',
        'coordinates_southernmost_latitude': 'g',
        'declination_southern_limit': 'k',
        'declination_northern_limit': 'j',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'type_of_ring'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': value.get('name_of_extraterrestrial_body'),
        'p': value.get('equinox'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'r': value.get('distance_from_earth'),
        'm': value.get('right_ascension_eastern_limit'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        'y': value.get('ending_date'),
        '3': value.get('materials_specified'),
        'd': value.get('coordinates_westernmost_longitude'),
        'e': value.get('coordinates_easternmost_longitude'),
        '2': value.get('source'),
        'x': value.get('beginning_date'),
        'f': value.get('coordinates_northernmost_latitude'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'n': value.get('right_ascension_western_limit'),
        'g': value.get('coordinates_southernmost_latitude'),
        'k': value.get('declination_southern_limit'),
        'j': value.get('declination_northern_limit'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'canceled_invalid_system_control_number': 'z',
        'system_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_system_control_number')
        ),
        'a': value.get('system_control_number'),
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
        'language_of_cataloging': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'subject_heading_thesaurus_conventions': 'f',
        'description_conventions': 'e',
        'transcribing_agency': 'c',
        'original_cataloging_agency': 'a',
        'modifying_agency': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('language_of_cataloging'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'f': value.get('subject_heading_thesaurus_conventions'),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        'c': value.get('transcribing_agency'),
        'a': value.get('original_cataloging_agency'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
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

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

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
        'local_gac_code': 'b',
        'source_of_local_code': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'iso_code': 'c',
        'geographic_area_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
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
        'formatted_9999_bc_through_ce_time_period': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'formatted_pre_9999_bc_time_period': 'c',
        'time_period_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period_in_subfield_b_or_c', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_code')
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
        'ending_date_created': 'l',
        'ending_date_for_aggregated_content': 'p',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'establishment_date': 'q',
        'end_period': 't',
        'start_period': 's',
        'source_of_date_scheme': '2',
        'single_or_starting_date_for_aggregated_content': 'o',
        'birth_date': 'f',
        'source_of_information': 'v',
        'death_date': 'g',
        'beginning_or_single_date_created': 'k',
        'termination_date': 'r',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('ending_date_created'),
        'p': value.get('ending_date_for_aggregated_content'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'q': value.get('establishment_date'),
        't': value.get('end_period'),
        's': value.get('start_period'),
        '2': value.get('source_of_date_scheme'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'f': value.get('birth_date'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'g': value.get('death_date'),
        'k': value.get('beginning_or_single_date_created'),
        'r': value.get('termination_date'),
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
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
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
        'geographic_classification_subarea_code': 'b',
        'code_source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'geographic_classification_area_code': 'a',
        'populated_place_name': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['code_source', 'None'])

    if (indicator_map1.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '2': value.get('code_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('geographic_classification_area_code'),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
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
        'classification_number_element_ending_number_of_span': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'explanatory_term': 'c',
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('classification_number_element_ending_number_of_span'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
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
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
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
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
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
        'classification_number_element_ending_number_of_span': 'b',
        'number_source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'explanatory_term': 'c',
        'classification_number_element_single_number_or_beginning_of_span': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('classification_number_element_ending_number_of_span'),
        '2': value.get('number_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        'a': value.get('classification_number_element_single_number_or_beginning_of_span'),
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
        'primary_g1_character_set': 'b',
        'alternate_g0_or_g1_character_set': 'c',
        'primary_g0_character_set': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('primary_g1_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
        'a': value.get('primary_g0_character_set'),
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
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'classification_number': 'a',
        'volumes_dates_to_which_call_number_applies': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('classification_number'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
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
        'code_source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'subject_category_code_subdivision': 'x',
        'subject_category_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'code_source'])

    if (indicator_map2.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('code_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        'a': value.get('subject_category_code'),
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
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'code_source': 'z',
        'subdivision_usage': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'z': value.get('code_source'),
        'a': utils.reverse_force_list(
            value.get('subdivision_usage')
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
        'item_number': 'b',
        'edition_identifier': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'common_auxiliary_subdivision': 'x',
        'universal_decimal_classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '2': value.get('edition_identifier'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        'a': value.get('universal_decimal_classification_number'),
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
        'item_number': 'b',
        'edition_number': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'volumes_dates_to_which_call_number_applies': 'd',
        'classification_number': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '2': value.get('edition_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'a': value.get('classification_number'),
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
        'classification_number_element_ending_number_of_span': 'b',
        'edition_number': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'explanatory_term': 'c',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'table_identification_table_number': 'z',
        'classification_number_element_single_number_or_beginning_number_of_span': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('classification_number_element_ending_number_of_span'),
        '2': value.get('edition_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'c': value.get('explanatory_term'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'z': value.get('table_identification_table_number'),
        'a': value.get('classification_number_element_single_number_or_beginning_number_of_span'),
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
        'number_source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'volumes_dates_to_which_call_number_applies': 'd',
        'canceled_invalid_call_number': 'z',
        'call_number': 'a',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('number_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('volumes_dates_to_which_call_number_applies'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_call_number')
        ),
        'a': value.get('call_number'),
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
        'classification_number_element_ending_number_of_span': 'b',
        'number_source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'explanatory_information': 'c',
        'classification_number_element_single_number_of_beginning_number_of_span': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('classification_number_element_ending_number_of_span'),
        '2': value.get('number_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'c': value.get('explanatory_information'),
        'a': value.get('classification_number_element_single_number_of_beginning_number_of_span'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
