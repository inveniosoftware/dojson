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


@marc21_liberal_authority.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    field_map = {
        'a': 'lc_control_number',
        'z': 'canceled_invalid_lc_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'lc_control_number': value.get('a'),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
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


@marc21_liberal_authority.over('link_to_bibliographic_record_for_serial_or_multipart_item', '^014..')
@utils.for_each_value
@utils.filter_values
def link_to_bibliographic_record_for_serial_or_multipart_item(self, key, value):
    """Link to Bibliographic Record for Serial or Multipart Item."""
    field_map = {
        'a': 'control_number_of_related_bibliographic_record',
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
        'control_number_of_related_bibliographic_record': value.get('a'),
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


@marc21_liberal_authority.over('national_bibliographic_agency_control_number', '^016..')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    field_map = {
        'a': 'record_control_number',
        'z': 'canceled_or_invalid_record_control_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': value.get('a'),
        'canceled_or_invalid_record_control_number': utils.force_list(
            value.get('z')
        ),
        'source': value.get('2'),
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


@marc21_liberal_authority.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    field_map = {
        'a': 'international_standard_book_number',
        'c': 'terms_of_availability',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_isbn',
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
        'international_standard_book_number': value.get('a'),
        'terms_of_availability': value.get('c'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
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


@marc21_liberal_authority.over('international_standard_serial_number', '^022..')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    field_map = {
        'a': 'international_standard_serial_number',
        'l': 'issn_l',
        'm': 'canceled_issn_l',
        'y': 'incorrect_issn',
        'z': 'canceled_issn',
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
        'international_standard_serial_number': value.get('a'),
        'issn_l': value.get('l'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'canceled_issn': utils.force_list(
            value.get('z')
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


@marc21_liberal_authority.over('other_standard_identifier', '^024..')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {"7": "Source specified in subfield $2", "8": "Unspecified type of standard number or code"}
    field_map = {
        'a': 'standard_number_or_code',
        'c': 'terms_of_availability',
        'd': 'additional_codes_following_the_standard_number_or_code',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_standard_number_or_code',
        '2': 'source_of_number_or_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_standard_number_or_code')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_standard_number_or_code': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    field_map = {
        'a': 'number_of_work',
        'b': 'number_of_movement',
        'c': 'number_of_excerpt',
        'd': 'caption_or_heading',
        'e': 'role',
        'g': 'clef',
        'm': 'voice_instrument',
        'n': 'key_signature',
        'o': 'time_signature',
        'p': 'musical_notation',
        'q': 'general_note',
        'r': 'key_or_mode',
        's': 'coded_validity_note',
        't': 'text_incipit',
        'u': 'uniform_resource_identifier',
        'y': 'link_text',
        'z': 'public_note',
        '2': 'system_code',
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
        'number_of_work': value.get('a'),
        'number_of_movement': value.get('b'),
        'number_of_excerpt': value.get('c'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'role': value.get('e'),
        'clef': value.get('g'),
        'voice_instrument': value.get('m'),
        'key_signature': value.get('n'),
        'time_signature': value.get('o'),
        'musical_notation': value.get('p'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'key_or_mode': value.get('r'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'system_code': value.get('2'),
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


@marc21_liberal_authority.over('coded_cartographic_mathematical_data', '^034..')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map2 = {"0": "Outer ring", "1": "Exclusion ring", "_": "Not applicable"}
    field_map = {
        'd': 'coordinates_westernmost_longitude',
        'e': 'coordinates_easternmost_longitude',
        'f': 'coordinates_northernmost_latitude',
        'g': 'coordinates_southernmost_latitude',
        'j': 'declination_northern_limit',
        'k': 'declination_southern_limit',
        'm': 'right_ascension_eastern_limit',
        'n': 'right_ascension_western_limit',
        'p': 'equinox',
        'r': 'distance_from_earth',
        's': 'g_ring_latitude',
        't': 'g_ring_longitude',
        'x': 'beginning_date',
        'y': 'ending_date',
        'z': 'name_of_extraterrestrial_body',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('type_of_ring')

    record_dict = {
        '__order__': order if len(order) else None,
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_northernmost_latitude': value.get('f'),
        'coordinates_southernmost_latitude': value.get('g'),
        'declination_northern_limit': value.get('j'),
        'declination_southern_limit': value.get('k'),
        'right_ascension_eastern_limit': value.get('m'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'distance_from_earth': value.get('r'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'beginning_date': value.get('x'),
        'ending_date': value.get('y'),
        'name_of_extraterrestrial_body': value.get('z'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'type_of_ring': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    field_map = {
        'a': 'system_control_number',
        'z': 'canceled_invalid_system_control_number',
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
        'system_control_number': value.get('a'),
        'canceled_invalid_system_control_number': utils.force_list(
            value.get('z')
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


@marc21_liberal_authority.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    field_map = {
        'a': 'original_cataloging_agency',
        'b': 'language_of_cataloging',
        'c': 'transcribing_agency',
        'd': 'modifying_agency',
        'e': 'description_conventions',
        'f': 'subject_heading_thesaurus_conventions',
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
        'original_cataloging_agency': value.get('a'),
        'language_of_cataloging': value.get('b'),
        'transcribing_agency': value.get('c'),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'subject_heading_thesaurus_conventions': value.get('f'),
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


@marc21_liberal_authority.over('authentication_code', '^042..')
@utils.filter_values
def authentication_code(self, key, value):
    """Authentication Code."""
    field_map = {
        'a': 'authentication_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authentication_code': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    field_map = {
        'a': 'geographic_area_code',
        'b': 'local_gac_code',
        'c': 'iso_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_local_code',
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
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'iso_code': utils.force_list(
            value.get('c')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
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


@marc21_liberal_authority.over('time_period_of_heading', '^045..')
@utils.filter_values
def time_period_of_heading(self, key, value):
    """Time Period of Heading."""
    indicator_map1 = {"0": "Single date/time", "1": "Multiple single dates/times", "2": "Range of dates/times", "_": "Subfield $b or $c not present"}
    field_map = {
        'a': 'time_period_code',
        'b': 'formatted_9999_bc_through_ce_time_period',
        'c': 'formatted_pre_9999_bc_time_period',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_time_period_in_subfield_b_or_c')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
        ),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    field_map = {
        'f': 'birth_date',
        'g': 'death_date',
        'k': 'beginning_or_single_date_created',
        'l': 'ending_date_created',
        'o': 'single_or_starting_date_for_aggregated_content',
        'p': 'ending_date_for_aggregated_content',
        'q': 'establishment_date',
        'r': 'termination_date',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '2': 'source_of_date_scheme',
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
        'birth_date': value.get('f'),
        'death_date': value.get('g'),
        'beginning_or_single_date_created': value.get('k'),
        'ending_date_created': value.get('l'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'ending_date_for_aggregated_content': value.get('p'),
        'establishment_date': value.get('q'),
        'termination_date': value.get('r'),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'source_of_date_scheme': value.get('2'),
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


@marc21_liberal_authority.over('library_of_congress_call_number', '^050..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('geographic_classification', '^052..')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    indicator_map1 = {"1": "U.S. Dept. of Defense Classification", "7": "Source specified in subfield $2", "_": "Library of Congress Classification"}
    field_map = {
        'a': 'geographic_classification_area_code',
        'b': 'geographic_classification_subarea_code',
        'd': 'populated_place_name',
        '2': 'code_source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('code_source')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'code_source': value.get('2', indicator_map1.get(key[3], key[3])),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('lc_classification_number', '^053..')
@utils.for_each_value
@utils.filter_values
def lc_classification_number(self, key, value):
    """LC Classification Number."""
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_classification_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_classification_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('library_and_archives_canada_call_number', '^055..')
@utils.for_each_value
@utils.filter_values
def library_and_archives_canada_call_number(self, key, value):
    """Library and Archives Canada Call Number."""
    indicator_map2 = {"0": "Assigned by LAC", "4": "Assigned by agency other than LC"}
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('national_library_of_medicine_call_number', '^060..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map2 = {"0": "Assigned by NLM", "4": "Assigned by agency other than NLM"}
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('other_classification_number', '^065..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    field_map = {
        'a': 'classification_number_element_single_number_or_beginning_of_span',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
        '2': 'number_source',
        '5': 'institution_to_which_field_applies',
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
        'classification_number_element_single_number_or_beginning_of_span': value.get('a'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
        'number_source': value.get('2'),
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


@marc21_liberal_authority.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    """Character Sets Present."""
    field_map = {
        'a': 'primary_g0_character_set',
        'b': 'primary_g1_character_set',
        'c': 'alternate_g0_or_g1_character_set',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'primary_g0_character_set': value.get('a'),
        'primary_g1_character_set': value.get('b'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('national_agricultural_library_call_number', '^070..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'd': 'volumes_dates_to_which_call_number_applies',
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
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
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


@marc21_liberal_authority.over('subject_category_code', '^072..')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    indicator_map2 = {"0": "NAL subject category code list", "7": "Source specified in subfield $2", "_": "No information provided"}
    field_map = {
        'a': 'subject_category_code',
        'x': 'subject_category_code_subdivision',
        '2': 'code_source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('code_source')

    record_dict = {
        '__order__': order if len(order) else None,
        'subject_category_code': value.get('a'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'code_source': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('subdivision_usage', '^073..')
@utils.filter_values
def subdivision_usage(self, key, value):
    """Subdivision Usage."""
    field_map = {
        'a': 'subdivision_usage',
        'z': 'code_source',
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
        'subdivision_usage': utils.force_list(
            value.get('a')
        ),
        'code_source': value.get('z'),
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


@marc21_liberal_authority.over('universal_decimal_classification_number', '^080..')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "_": "No information provided"}
    field_map = {
        'a': 'universal_decimal_classification_number',
        'b': 'item_number',
        'x': 'common_auxiliary_subdivision',
        '2': 'edition_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'edition_identifier': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('dewey_decimal_call_number', '^082..')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_call_number(self, key, value):
    """Dewey Decimal Call Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC", "_": "No information provided"}
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '2': 'edition_number',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'edition_number': value.get('2'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('dewey_decimal_classification_number', '^083..')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        'z': 'table_identification_table_number',
        '2': 'edition_number',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('source_of_classification_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'table_identification_table_number': value.get('z'),
        'edition_number': value.get('2'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        'source_of_classification_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('government_document_call_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_call_number(self, key, value):
    """Government Document Call Number."""
    field_map = {
        'a': 'call_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        'z': 'canceled_invalid_call_number',
        '2': 'number_source',
        '5': 'institution_to_which_field_applies',
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
        'call_number': value.get('a'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'canceled_invalid_call_number': utils.force_list(
            value.get('z')
        ),
        'number_source': value.get('2'),
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


@marc21_liberal_authority.over('government_document_classification_number', '^087..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    field_map = {
        'a': 'classification_number_element_single_number_of_beginning_number_of_span',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_information',
        '2': 'number_source',
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
        'classification_number_element_single_number_of_beginning_number_of_span': value.get('a'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_information': value.get('c'),
        'number_source': value.get('2'),
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
