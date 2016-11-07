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

from ..model import marc21_authority


@marc21_authority.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    field_map = {
        'z': 'canceled_invalid_lc_control_number',
        'a': 'lc_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
        'lc_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('link_to_bibliographic_record_for_serial_or_multipart_item', '^014..')
@utils.for_each_value
@utils.filter_values
def link_to_bibliographic_record_for_serial_or_multipart_item(self, key, value):
    """Link to Bibliographic Record for Serial or Multipart Item."""
    field_map = {
        'a': 'control_number_of_related_bibliographic_record',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'control_number_of_related_bibliographic_record': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('national_bibliographic_agency_control_number', '^016..')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    field_map = {
        '2': 'source',
        'a': 'record_control_number',
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_or_invalid_record_control_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'source': value.get('2'),
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_or_invalid_record_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21_authority.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_isbn',
        'a': 'international_standard_book_number',
        '6': 'linkage',
        'c': 'terms_of_availability',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
        ),
        'international_standard_book_number': value.get('a'),
        'linkage': value.get('6'),
        'terms_of_availability': value.get('c'),
    }


@marc21_authority.over('international_standard_serial_number', '^022..')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_issn',
        'm': 'canceled_issn_l',
        'l': 'issn_l',
        'a': 'international_standard_serial_number',
        '6': 'linkage',
        'y': 'incorrect_issn',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'issn_l': value.get('l'),
        'international_standard_serial_number': value.get('a'),
        'linkage': value.get('6'),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
    }


@marc21_authority.over('other_standard_identifier', '^024[7_8].')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {"7": "Source specified in subfield $2", "8": "Unspecified type of standard number or code"}
    field_map = {
        '2': 'source_of_number_or_code',
        'd': 'additional_codes_following_the_standard_number_or_code',
        '8': 'field_link_and_sequence_number',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_standard_number_or_code',
        'a': 'standard_number_or_code',
        '6': 'linkage',
        'c': 'terms_of_availability',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_standard_number_or_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_number_or_code': value.get('2'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'standard_number_or_code': value.get('a'),
        'linkage': value.get('6'),
        'terms_of_availability': value.get('c'),
        'type_of_standard_number_or_code': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
    }


@marc21_authority.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    field_map = {
        'z': 'public_note',
        'e': 'role',
        'd': 'caption_or_heading',
        '8': 'field_link_and_sequence_number',
        'o': 'time_signature',
        's': 'coded_validity_note',
        'a': 'number_of_work',
        '6': 'linkage',
        'c': 'number_of_excerpt',
        'g': 'clef',
        '2': 'system_code',
        'n': 'key_signature',
        'p': 'musical_notation',
        'u': 'uniform_resource_identifier',
        'm': 'voice_instrument',
        'b': 'number_of_movement',
        't': 'text_incipit',
        'y': 'link_text',
        'q': 'general_note',
        'r': 'key_or_mode',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'public_note': utils.force_list(
            value.get('z')
        ),
        'role': value.get('e'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'time_signature': value.get('o'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'number_of_work': value.get('a'),
        'linkage': value.get('6'),
        'number_of_excerpt': value.get('c'),
        'clef': value.get('g'),
        'system_code': value.get('2'),
        'key_signature': value.get('n'),
        'musical_notation': value.get('p'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'voice_instrument': value.get('m'),
        'number_of_movement': value.get('b'),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'key_or_mode': value.get('r'),
    }


@marc21_authority.over('coded_cartographic_mathematical_data', '^034.[0_1]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map2 = {"0": "Outer ring", "1": "Exclusion ring", "_": "Not applicable"}
    field_map = {
        'z': 'name_of_extraterrestrial_body',
        'g': 'coordinates_southernmost_latitude',
        'j': 'declination_northern_limit',
        '3': 'materials_specified',
        'e': 'coordinates_easternmost_longitude',
        'f': 'coordinates_northernmost_latitude',
        'k': 'declination_southern_limit',
        '6': 'linkage',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        'n': 'right_ascension_western_limit',
        'p': 'equinox',
        'x': 'beginning_date',
        's': 'g_ring_latitude',
        'm': 'right_ascension_eastern_limit',
        'r': 'distance_from_earth',
        't': 'g_ring_longitude',
        'y': 'ending_date',
        '8': 'field_link_and_sequence_number',
        'd': 'coordinates_westernmost_longitude',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('type_of_ring')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name_of_extraterrestrial_body': value.get('z'),
        'coordinates_southernmost_latitude': value.get('g'),
        'declination_northern_limit': value.get('j'),
        'materials_specified': value.get('3'),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_northernmost_latitude': value.get('f'),
        'declination_southern_limit': value.get('k'),
        'linkage': value.get('6'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'beginning_date': value.get('x'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'right_ascension_eastern_limit': value.get('m'),
        'distance_from_earth': value.get('r'),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'ending_date': value.get('y'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'coordinates_westernmost_longitude': value.get('d'),
        'type_of_ring': indicator_map2.get(key[4]),
    }


@marc21_authority.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    field_map = {
        'z': 'canceled_invalid_system_control_number',
        'a': 'system_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'canceled_invalid_system_control_number': utils.force_list(
            value.get('z')
        ),
        'system_control_number': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    field_map = {
        'e': 'description_conventions',
        'd': 'modifying_agency',
        '8': 'field_link_and_sequence_number',
        'f': 'subject_heading_thesaurus_conventions',
        'a': 'original_cataloging_agency',
        '6': 'linkage',
        'b': 'language_of_cataloging',
        'c': 'transcribing_agency',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'subject_heading_thesaurus_conventions': value.get('f'),
        'original_cataloging_agency': value.get('a'),
        'linkage': value.get('6'),
        'language_of_cataloging': value.get('b'),
        'transcribing_agency': value.get('c'),
    }


@marc21_authority.over('authentication_code', '^042..')
@utils.filter_values
def authentication_code(self, key, value):
    """Authentication Code."""
    field_map = {
        'a': 'authentication_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authentication_code': utils.force_list(
            value.get('a')
        ),
    }


@marc21_authority.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_local_code',
        '8': 'field_link_and_sequence_number',
        'a': 'geographic_area_code',
        '6': 'linkage',
        'b': 'local_gac_code',
        'c': 'iso_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'iso_code': utils.force_list(
            value.get('c')
        ),
    }


@marc21_authority.over('time_period_of_heading', '^045[02_1].')
@utils.filter_values
def time_period_of_heading(self, key, value):
    """Time Period of Heading."""
    indicator_map1 = {"0": "Single date/time", "1": "Multiple single dates/times", "2": "Range of dates/times", "_": "Subfield $b or $c not present"}
    field_map = {
        'a': 'time_period_code',
        'c': 'formatted_pre_9999_bc_time_period',
        '6': 'linkage',
        'b': 'formatted_9999_bc_through_ce_time_period',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period_in_subfield_b_or_c')

    return {
        '__order__': tuple(order) if len(order) else None,
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3]),
    }


@marc21_authority.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    field_map = {
        'v': 'source_of_information',
        'r': 'termination_date',
        '8': 'field_link_and_sequence_number',
        'o': 'single_or_starting_date_for_aggregated_content',
        'f': 'birth_date',
        'k': 'beginning_or_single_date_created',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        'g': 'death_date',
        '2': 'source_of_date_scheme',
        'p': 'ending_date_for_aggregated_content',
        's': 'start_period',
        'l': 'ending_date_created',
        'q': 'establishment_date',
        't': 'end_period',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'termination_date': value.get('r'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'birth_date': value.get('f'),
        'beginning_or_single_date_created': value.get('k'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'death_date': value.get('g'),
        'source_of_date_scheme': value.get('2'),
        'ending_date_for_aggregated_content': value.get('p'),
        'start_period': value.get('s'),
        'ending_date_created': value.get('l'),
        'establishment_date': value.get('q'),
        'end_period': value.get('t'),
    }


@marc21_authority.over('library_of_congress_call_number', '^050.[04_]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        'd': 'volumes_dates_to_which_call_number_applies',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
        '6': 'linkage',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('geographic_classification', '^052[7_1].')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    indicator_map1 = {"1": "U.S. Dept. of Defense Classification", "7": "Source specified in subfield $2", "_": "Library of Congress Classification"}
    field_map = {
        '2': 'code_source',
        'd': 'populated_place_name',
        '8': 'field_link_and_sequence_number',
        'a': 'geographic_classification_area_code',
        '6': 'linkage',
        'b': 'geographic_classification_subarea_code',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and '2' not in value:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_classification_area_code': value.get('a'),
        'linkage': value.get('6'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'code_source': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
    }


@marc21_authority.over('lc_classification_number', '^053.[04_]')
@utils.for_each_value
@utils.filter_values
def lc_classification_number(self, key, value):
    """LC Classification Number."""
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
        '6': 'linkage',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_classification_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
        'linkage': value.get('6'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('library_and_archives_canada_call_number', '^055.[04_]')
@utils.for_each_value
@utils.filter_values
def library_and_archives_canada_call_number(self, key, value):
    """Library and Archives Canada Call Number."""
    indicator_map2 = {"0": "Assigned by LAC", "4": "Assigned by agency other than LC"}
    field_map = {
        'd': 'volumes_dates_to_which_call_number_applies',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
        '6': 'linkage',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('national_library_of_medicine_call_number', '^060.[04_]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map2 = {"0": "Assigned by NLM", "4": "Assigned by agency other than NLM"}
    field_map = {
        'd': 'volumes_dates_to_which_call_number_applies',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
        '6': 'linkage',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('other_classification_number', '^065..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    field_map = {
        '2': 'number_source',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number_element_single_number_or_beginning_of_span',
        '6': 'linkage',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number_element_single_number_or_beginning_of_span': value.get('a'),
        'linkage': value.get('6'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
    }


@marc21_authority.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    """Character Sets Present."""
    field_map = {
        'a': 'primary_g0_character_set',
        'b': 'primary_g1_character_set',
        'c': 'alternate_g0_or_g1_character_set',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'primary_g0_character_set': value.get('a'),
        'primary_g1_character_set': value.get('b'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
    }


@marc21_authority.over('national_agricultural_library_call_number', '^070..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    field_map = {
        'a': 'classification_number',
        '6': 'linkage',
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
        'd': 'volumes_dates_to_which_call_number_applies',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
    }


@marc21_authority.over('subject_category_code', '^072.[07_]')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    indicator_map2 = {"0": "NAL subject category code list", "7": "Source specified in subfield $2", "_": "No information provided"}
    field_map = {
        '2': 'code_source',
        'a': 'subject_category_code',
        '6': 'linkage',
        'x': 'subject_category_code_subdivision',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'subject_category_code': value.get('a'),
        'linkage': value.get('6'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'code_source': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21_authority.over('subdivision_usage', '^073..')
@utils.filter_values
def subdivision_usage(self, key, value):
    """Subdivision Usage."""
    field_map = {
        'z': 'code_source',
        'a': 'subdivision_usage',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'code_source': value.get('z'),
        'subdivision_usage': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_authority.over('universal_decimal_classification_number', '^080[0_1].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "_": "No information provided"}
    field_map = {
        '2': 'edition_identifier',
        '8': 'field_link_and_sequence_number',
        'a': 'universal_decimal_classification_number',
        '6': 'linkage',
        'b': 'item_number',
        'x': 'common_auxiliary_subdivision',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    return {
        '__order__': tuple(order) if len(order) else None,
        'edition_identifier': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'universal_decimal_classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21_authority.over('dewey_decimal_call_number', '^082[07_1][04_]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_call_number(self, key, value):
    """Dewey Decimal Call Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC", "_": "No information provided"}
    field_map = {
        '2': 'edition_number',
        'd': 'volumes_dates_to_which_call_number_applies',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'a': 'classification_number',
        '6': 'linkage',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'edition_number': value.get('2'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'item_number': value.get('b'),
        'type_of_edition': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('dewey_decimal_classification_number', '^083[07_1][04_]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        '2': 'edition_number',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'z': 'table_identification_table_number',
        'a': 'classification_number_element_single_number_or_beginning_number_of_span',
        '6': 'linkage',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_term',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    if key[4] in indicator_map2:
        order.append('source_of_classification_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'edition_number': value.get('2'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'table_identification_table_number': value.get('z'),
        'classification_number_element_single_number_or_beginning_number_of_span': value.get('a'),
        'linkage': value.get('6'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_term': value.get('c'),
        'type_of_edition': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21_authority.over('government_document_call_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_call_number(self, key, value):
    """Government Document Call Number."""
    field_map = {
        '2': 'number_source',
        'd': 'volumes_dates_to_which_call_number_applies',
        '8': 'field_link_and_sequence_number',
        '5': 'institution_to_which_field_applies',
        'z': 'canceled_invalid_call_number',
        'a': 'call_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_source': value.get('2'),
        'volumes_dates_to_which_call_number_applies': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'canceled_invalid_call_number': utils.force_list(
            value.get('z')
        ),
        'call_number': value.get('a'),
        'linkage': value.get('6'),
    }


@marc21_authority.over('government_document_classification_number', '^087..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    field_map = {
        '2': 'number_source',
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number_element_single_number_of_beginning_number_of_span',
        '6': 'linkage',
        'b': 'classification_number_element_ending_number_of_span',
        'c': 'explanatory_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number_element_single_number_of_beginning_number_of_span': value.get('a'),
        'linkage': value.get('6'),
        'classification_number_element_ending_number_of_span': value.get('b'),
        'explanatory_information': value.get('c'),
    }
