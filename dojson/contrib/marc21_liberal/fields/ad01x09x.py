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
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_invalid_lc_control_number',
        'a': 'lc_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
        'lc_control_number': value.get('a'),
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
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'control_number_of_related_bibliographic_record',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'control_number_of_related_bibliographic_record': value.get('a'),
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
        '8': 'field_link_and_sequence_number',
        '2': 'source',
        'z': 'canceled_or_invalid_record_control_number',
        'a': 'record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'canceled_or_invalid_record_control_number': utils.force_list(
            value.get('z')
        ),
        'record_control_number': value.get('a'),
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
        'c': 'terms_of_availability',
        'q': 'qualifying_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_invalid_isbn',
        'a': 'international_standard_book_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'terms_of_availability': value.get('c'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
        ),
        'international_standard_book_number': value.get('a'),
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
        'z': 'canceled_issn',
        'l': 'issn_l',
        'm': 'canceled_issn_l',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'y': 'incorrect_issn',
        'a': 'international_standard_serial_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'issn_l': value.get('l'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'international_standard_serial_number': value.get('a'),
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
        '8': 'field_link_and_sequence_number',
        'c': 'terms_of_availability',
        'q': 'qualifying_information',
        'd': 'additional_codes_following_the_standard_number_or_code',
        '6': 'linkage',
        '2': 'source_of_number_or_code',
        'z': 'canceled_invalid_standard_number_or_code',
        'a': 'standard_number_or_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_standard_number_or_code')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'terms_of_availability': value.get('c'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'linkage': value.get('6'),
        'source_of_number_or_code': value.get('2'),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'standard_number_or_code': value.get('a'),
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
        'z': 'public_note',
        '2': 'system_code',
        's': 'coded_validity_note',
        '6': 'linkage',
        't': 'text_incipit',
        '8': 'field_link_and_sequence_number',
        'y': 'link_text',
        'e': 'role',
        'a': 'number_of_work',
        'g': 'clef',
        'b': 'number_of_movement',
        'p': 'musical_notation',
        'c': 'number_of_excerpt',
        'u': 'uniform_resource_identifier',
        'm': 'voice_instrument',
        'q': 'general_note',
        'o': 'time_signature',
        'd': 'caption_or_heading',
        'r': 'key_or_mode',
        'n': 'key_signature',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'public_note': utils.force_list(
            value.get('z')
        ),
        'system_code': value.get('2'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'linkage': value.get('6'),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'role': value.get('e'),
        'number_of_work': value.get('a'),
        'clef': value.get('g'),
        'number_of_movement': value.get('b'),
        'musical_notation': value.get('p'),
        'number_of_excerpt': value.get('c'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'voice_instrument': value.get('m'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'time_signature': value.get('o'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'key_or_mode': value.get('r'),
        'key_signature': value.get('n'),
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
        'm': 'right_ascension_eastern_limit',
        '2': 'source',
        'z': 'name_of_extraterrestrial_body',
        'x': 'beginning_date',
        '6': 'linkage',
        't': 'g_ring_longitude',
        '8': 'field_link_and_sequence_number',
        'y': 'ending_date',
        'e': 'coordinates_easternmost_longitude',
        's': 'g_ring_latitude',
        'g': 'coordinates_southernmost_latitude',
        'p': 'equinox',
        'k': 'declination_southern_limit',
        'f': 'coordinates_northernmost_latitude',
        'j': 'declination_northern_limit',
        '3': 'materials_specified',
        'd': 'coordinates_westernmost_longitude',
        'r': 'distance_from_earth',
        'n': 'right_ascension_western_limit',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('type_of_ring')

    record_dict = {
        '__order__': order if len(order) else None,
        'right_ascension_eastern_limit': value.get('m'),
        'source': value.get('2'),
        'name_of_extraterrestrial_body': value.get('z'),
        'beginning_date': value.get('x'),
        'linkage': value.get('6'),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'ending_date': value.get('y'),
        'coordinates_easternmost_longitude': value.get('e'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'coordinates_southernmost_latitude': value.get('g'),
        'equinox': value.get('p'),
        'declination_southern_limit': value.get('k'),
        'coordinates_northernmost_latitude': value.get('f'),
        'declination_northern_limit': value.get('j'),
        'materials_specified': value.get('3'),
        'coordinates_westernmost_longitude': value.get('d'),
        'distance_from_earth': value.get('r'),
        'right_ascension_western_limit': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
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
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_invalid_system_control_number',
        'a': 'system_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_system_control_number': utils.force_list(
            value.get('z')
        ),
        'system_control_number': value.get('a'),
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
        'b': 'language_of_cataloging',
        'd': 'modifying_agency',
        'c': 'transcribing_agency',
        'f': 'subject_heading_thesaurus_conventions',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'e': 'description_conventions',
        'a': 'original_cataloging_agency',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'language_of_cataloging': value.get('b'),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'transcribing_agency': value.get('c'),
        'subject_heading_thesaurus_conventions': value.get('f'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'original_cataloging_agency': value.get('a'),
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
        'b': 'local_gac_code',
        '8': 'field_link_and_sequence_number',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        '2': 'source_of_local_code',
        'a': 'geographic_area_code',
        'c': 'iso_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'iso_code': utils.force_list(
            value.get('c')
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
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'c': 'formatted_pre_9999_bc_time_period',
        'a': 'time_period_code',
        'b': 'formatted_9999_bc_through_ce_time_period',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_time_period_in_subfield_b_or_c')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
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
        '2': 'source_of_date_scheme',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '6': 'linkage',
        't': 'end_period',
        '8': 'field_link_and_sequence_number',
        'l': 'ending_date_created',
        'p': 'ending_date_for_aggregated_content',
        'k': 'beginning_or_single_date_created',
        'f': 'birth_date',
        'g': 'death_date',
        'q': 'establishment_date',
        'o': 'single_or_starting_date_for_aggregated_content',
        'r': 'termination_date',
        's': 'start_period',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_date_scheme': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'ending_date_created': value.get('l'),
        'ending_date_for_aggregated_content': value.get('p'),
        'beginning_or_single_date_created': value.get('k'),
        'birth_date': value.get('f'),
        'death_date': value.get('g'),
        'establishment_date': value.get('q'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'termination_date': value.get('r'),
        'start_period': value.get('s'),
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
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
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
        'b': 'geographic_classification_subarea_code',
        '8': 'field_link_and_sequence_number',
        'd': 'populated_place_name',
        '6': 'linkage',
        '2': 'code_source',
        'a': 'geographic_classification_area_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('code_source')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'geographic_classification_area_code': value.get('a'),
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
        'b': 'classification_number_element_ending_number_of_span',
        '8': 'field_link_and_sequence_number',
        'c': 'explanatory_term',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_classification_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_ending_number_of_span': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_term': value.get('c'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
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
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
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
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
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
        'b': 'classification_number_element_ending_number_of_span',
        '8': 'field_link_and_sequence_number',
        'c': 'explanatory_term',
        '6': 'linkage',
        '2': 'number_source',
        'a': 'classification_number_element_single_number_or_beginning_of_span',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_ending_number_of_span': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_term': value.get('c'),
        'linkage': value.get('6'),
        'number_source': value.get('2'),
        'classification_number_element_single_number_or_beginning_of_span': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
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
        'b': 'primary_g1_character_set',
        'c': 'alternate_g0_or_g1_character_set',
        'a': 'primary_g0_character_set',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'primary_g1_character_set': value.get('b'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
        'primary_g0_character_set': value.get('a'),
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
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
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
        '6': 'linkage',
        '2': 'code_source',
        'x': 'subject_category_code_subdivision',
        'a': 'subject_category_code',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('code_source')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'subject_category_code': value.get('a'),
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
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'z': 'code_source',
        'a': 'subdivision_usage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'code_source': value.get('z'),
        'subdivision_usage': utils.force_list(
            value.get('a')
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
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'edition_identifier',
        'x': 'common_auxiliary_subdivision',
        'a': 'universal_decimal_classification_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'edition_identifier': value.get('2'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'universal_decimal_classification_number': value.get('a'),
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
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '2': 'edition_number',
        'a': 'classification_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'edition_number': value.get('2'),
        'classification_number': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
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
        'b': 'classification_number_element_ending_number_of_span',
        'z': 'table_identification_table_number',
        '8': 'field_link_and_sequence_number',
        'c': 'explanatory_term',
        '6': 'linkage',
        '2': 'edition_number',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('source_of_classification_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_ending_number_of_span': value.get('b'),
        'table_identification_table_number': value.get('z'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_term': value.get('c'),
        'linkage': value.get('6'),
        'edition_number': value.get('2'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
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
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '6': 'linkage',
        '2': 'number_source',
        'z': 'canceled_invalid_call_number',
        'a': 'call_number',
        '5': 'institution_to_which_field_applies',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'linkage': value.get('6'),
        'number_source': value.get('2'),
        'canceled_invalid_call_number': utils.force_list(
            value.get('z')
        ),
        'call_number': value.get('a'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
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
        'b': 'classification_number_element_ending_number_of_span',
        '8': 'field_link_and_sequence_number',
        'c': 'explanatory_information',
        '6': 'linkage',
        '2': 'number_source',
        'a': 'classification_number_element_single_number_of_beginning_number_of_span',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_number_element_ending_number_of_span': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_information': value.get('c'),
        'linkage': value.get('6'),
        'number_source': value.get('2'),
        'classification_number_element_single_number_of_beginning_number_of_span': value.get('a'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
