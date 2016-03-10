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

from ..model import marc21


@marc21.over('library_of_congress_control_number', '^010__')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    field_map = {
        'a': 'lc_control_number',
        'b': 'nucmc_control_number',
        'z': 'canceled_invalid_lc_control_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'lc_control_number': value.get('a'),
        'nucmc_control_number': utils.force_list(value.get('b')),
        'canceled_invalid_lc_control_number': utils.force_list(value.get('z')),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('patent_control_information', '^013__')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    """Patent Control Information."""
    field_map = {
        'a': 'number',
        'b': 'country',
        'c': 'type_of_number',
        'd': 'date',
        'e': 'status',
        'f': 'party_to_document',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number': value.get('a'),
        'country': value.get('b'),
        'type_of_number': value.get('c'),
        'date': utils.force_list(value.get('d')),
        'status': utils.force_list(value.get('e')),
        'party_to_document': utils.force_list(value.get('f')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('national_bibliography_number', '^015__')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    """National Bibliography Number."""
    field_map = {
        'a': 'national_bibliography_number',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_national_bibliography_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'national_bibliography_number': utils.force_list(
            value.get('a')),
        'qualifying_information': utils.force_list(
            value.get('q')),
        'canceled_invalid_national_bibliography_number': utils.force_list(
            value.get('z')),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21.over('national_bibliographic_agency_control_number', '^016[_7]_')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    indicator_map1 = {
        '_': 'Library and Archives Canada',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'record_control_number',
        'z': 'canceled_invalid_control_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('national_bibliographic_agency')

    return {
        '__order__': tuple(order) if len(order) else None,
        'record_control_number': value.get('a'),
        'canceled_invalid_control_number': utils.force_list(value.get('z')),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'national_bibliographic_agency': indicator_map1.get(key[3]),
    }


@marc21.over('copyright_or_legal_deposit_number', '^017_[_8]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
    indicator_map2 = {
        '_': 'Copyright or legal deposit number',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'copyright_or_legal_deposit_number',
        'b': 'assigning_agency',
        'd': 'date',
        'i': 'display_text',
        'z': 'canceled_invalid_copyright_or_legal_deposit_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'copyright_or_legal_deposit_number': utils.force_list(
            value.get('a')),
        'assigning_agency': value.get('b'),
        'date': value.get('d'),
        'display_text': value.get('i'),
        'canceled_invalid_copyright_or_legal_deposit_number': utils.force_list(
            value.get('z')),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'display_constant_controller': indicator_map2.get(
            key[4]),
    }


@marc21.over('copyright_article_fee_code', '^018__')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    """Copyright Article-Fee Code."""
    field_map = {
        'a': 'copyright_article_fee_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'copyright_article_fee_code': utils.force_list(value.get('a')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('international_standard_book_number', '^020__')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'international_standard_book_number': value.get('a'),
        'terms_of_availability': value.get('c'),
        'qualifying_information': utils.force_list(value.get('q')),
        'canceled_invalid_isbn': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('international_standard_serial_number', '^022[_01]_')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    indicator_map1 = {
        '_': 'No level specified',
        '0': 'Continuing resource of international interest',
        '1': 'Continuing resource not of international interest',
    }

    field_map = {
        'a': 'international_standard_serial_number',
        'l': 'issn_l',
        'm': 'canceled_issn_l',
        'y': 'incorrect_issn',
        'z': 'canceled_issn',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_international_interest')

    return {
        '__order__': tuple(order) if len(order) else None,
        'international_standard_serial_number': value.get('a'),
        'issn_l': value.get('l'),
        'canceled_issn_l': utils.force_list(value.get('m')),
        'canceled_issn': utils.force_list(value.get('z')),
        'incorrect_issn': utils.force_list(value.get('y')),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'level_of_international_interest': indicator_map1.get(key[3]),
    }


@marc21.over('other_standard_identifier', '^024[_0123478][_01]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {
        '0': 'International Standard Recording Code',
        '1': 'Universal Product Code',
        '2': 'International Standard Music Number',
        '3': 'International Article Number',
        '4': 'Serial Item and Contribution Identifier',
        '7': 'Source specified in subfield $2',
        '8': 'Unspecified type of standard number or code',
    }
    indicator_map2 = {
        '_': 'No information provided',
        '0': 'No difference',
        '1': 'Difference',
    }
    field_map = {
        'a': 'standard_number_or_code',
        'c': 'terms_of_availability',
        'd': 'additional_codes_following_the_standard_number_or_code',
        'q': 'qualifying_information',
        '2': 'source_of_number_or_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_invalid_standard_number_or_code',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_standard_number_or_code')
    if key[4] in indicator_map2:
        order.append('difference_indicator')

    return {
        '__order__': tuple(order) if len(order) else None,
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'qualifying_information': utils.force_list(
            value.get('q')),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'type_of_standard_number_or_code': indicator_map1.get(
            key[3]),
        'difference_indicator': indicator_map2.get(
            key[4]),
    }


@marc21.over('overseas_acquisition_number', '^025__')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    """Overseas Acquisition Number."""
    field_map = {
        'a': 'overseas_acquisition_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'overseas_acquisition_number': utils.force_list(value.get('a')),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('fingerprint_identifier', '^026__')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    """Fingerprint Identifier."""
    field_map = {
        'a': 'first_and_second_groups_of_characters',
        'b': 'third_and_fourth_groups_of_characters',
        'c': 'date',
        'd': 'number_of_volume_or_part',
        'e': 'unparsed_fingerprint',
        '2': 'source',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'first_and_second_groups_of_characters': value.get('a'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'date': value.get('c'),
        'number_of_volume_or_part': utils.force_list(value.get('d')),
        'unparsed_fingerprint': value.get('e'),
        'source': value.get('2'),
        'institution_to_which_field_applies': utils.force_list(value.get('5')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('standard_technical_report_number', '^027__')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    field_map = {
        'a': 'standard_technical_report_number',
        'q': 'qualifying_information',
        'z': 'canceled_invalid_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'standard_technical_report_number': value.get('a'),
        'qualifying_information': utils.force_list(value.get('q')),
        'canceled_invalid_number': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('publisher_number', '^028[_0-5][_0-4]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    """Publisher Number."""
    indicator_map1 = {
        '0': 'Issue number',
        '1': 'Matrix number',
        '2': 'Plate number',
        '3': 'Other music number',
        '4': 'Videorecording number',
        '5': 'Other publisher number',
    }

    indicator_map2 = {
        '0': 'No note, no added entry',
        '1': 'Note, added entry',
        '2': 'Note, no added entry',
        '3': 'No note, added entry',
    }

    field_map = {
        'a': 'publisher_number',
        'b': 'source',
        'q': 'qualifying_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_publisher_number')
    if key[4] in indicator_map2:
        order.append('note_added_entry_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'publisher_number': value.get('a'),
        'source': value.get('b'),
        'qualifying_information': utils.force_list(value.get('q')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_publisher_number': indicator_map1.get(key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4]),
    }


@marc21.over('coden_designation', '^030__')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    """CODEN Designation."""
    field_map = {
        'a': 'coden',
        'z': 'canceled_invalid_coden',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'coden': value.get('a'),
        'canceled_invalid_coden': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('musical_incipits_information', '^031__')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_of_work': value.get('a'),
        'number_of_movement': value.get('b'),
        'number_of_excerpt': value.get('c'),
        'caption_or_heading': utils.force_list(value.get('d')),
        'role': value.get('e'),
        'clef': value.get('g'),
        'voice_instrument': value.get('m'),
        'key_signature': value.get('n'),
        'time_signature': value.get('o'),
        'musical_notation': value.get('p'),
        'general_note': utils.force_list(value.get('q')),
        'key_or_mode': value.get('r'),
        'coded_validity_note': utils.force_list(value.get('s')),
        'text_incipit': utils.force_list(value.get('t')),
        'uniform_resource_identifier': utils.force_list(value.get('u')),
        'link_text': utils.force_list(value.get('y')),
        'public_note': utils.force_list(value.get('z')),
        'system_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('postal_registration_number', '^032__')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    """Postal Registration Number."""
    field_map = {
        'a': 'postal_registration_number',
        'b': 'source_agency_assigning_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'postal_registration_number': value.get('a'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('date_time_and_place_of_an_event', '^033[_0-2][_0-2]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    """Date/Time and Place of an Event."""
    indicator_map1 = {
        '_': 'No date information',
        '0': 'Single date',
        '1': 'Multiple single dates',
        '2': 'Range of dates',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Capture',
        '1': 'Broadcast',
        '2': 'Finding',
    }

    field_map = {
        'a': 'formatted_date_time',
        'b': 'geographic_classification_area_code',
        'c': 'geographic_classification_subarea_code',
        'p': 'place_of_event',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_date_in_subfield_a')
    if key[4] in indicator_map2:
        order.append('type_of_event')

    return {
        '__order__': tuple(order) if len(order) else None,
        'formatted_date_time': utils.force_list(
            value.get('a')),
        'geographic_classification_area_code': utils.force_list(
            value.get('b')),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('c')),
        'place_of_event': utils.force_list(
            value.get('p')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source_of_term': utils.force_list(
            value.get('2')),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'type_of_date_in_subfield_a': indicator_map1.get(
            key[3]),
        'type_of_event': indicator_map2.get(
            key[4]),
    }


@marc21.over('coded_cartographic_mathematical_data', '^034[_013][_01]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map1 = {
        '0': 'Scale indeterminable/No scale recorded',
        '1': 'Single scale',
        '3': 'Range of scales',
    }
    indicator_map2 = {
        '_': 'Not applicable',
        '0': 'Outer ring',
        '1': 'Exclusion ring',
    }

    field_map = {
        'a': 'category_of_scale',
        'b': 'constant_ratio_linear_horizontal_scale',
        'c': 'constant_ratio_linear_vertical_scale',
        'd': 'coordinates_westernmost_longitude',
        'e': 'coordinates_easternmost_longitude',
        'f': 'coordinates_northernmost_latitude',
        'g': 'coordinates_southernmost_latitude',
        'h': 'angular_scale',
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

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_scale')
    if key[4] in indicator_map2:
        order.append('type_of_ring')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'category_of_scale': value.get('a'),
        'constant_ratio_linear_horizontal_scale': utils.force_list(
            value.get('b')),
        'constant_ratio_linear_vertical_scale': utils.force_list(
            value.get('c')),
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_northernmost_latitude': value.get('f'),
        'coordinates_southernmost_latitude': value.get('g'),
        'angular_scale': utils.force_list(
            value.get('h')),
        'declination_northern_limit': value.get('j'),
        'declination_southern_limit': value.get('k'),
        'right_ascension_eastern_limit': value.get('m'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'distance_from_earth': value.get('r'),
        'g_ring_latitude': utils.force_list(
            value.get('s')),
        'g_ring_longitude': utils.force_list(
            value.get('t')),
        'beginning_date': value.get('x'),
        'ending_date': value.get('y'),
        'name_of_extraterrestrial_body': value.get('z'),
        'type_of_scale': indicator_map1.get(
            key[3]),
        'type_of_ring': indicator_map2.get(
            key[4]),
    }


@marc21.over('system_control_number', '^035__')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    field_map = {
        'a': 'system_control_number',
        'z': 'canceled_invalid_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'system_control_number': value.get('a'),
        'canceled_invalid_control_number': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('original_study_number_for_computer_data_files', '^036__')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    """Original Study Number for Computer Data Files."""
    field_map = {
        'a': 'original_study_number',
        'b': 'source_agency_assigning_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'original_study_number': value.get('a'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('source_of_acquisition', '^037[_23]_')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    """Source of Acquisition."""
    indicator_map1 = {
        '_': 'Not applicable/No information provided/Earliest',
        '2': 'Intervening',
        '3': 'Current/Latest',
    }

    field_map = {
        'a': 'stock_number',
        'b': 'source_of_stock_number_acquisition',
        'c': 'terms_of_availability',
        'f': 'form_of_issue',
        'g': 'additional_format_characteristics',
        'n': 'note',
        '3': 'materials_specified',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('source_of_acquisition_sequence')

    return {
        '__order__': tuple(order) if len(order) else None,
        'stock_number': value.get('a'),
        'source_of_stock_number_acquisition': value.get('b'),
        'terms_of_availability': utils.force_list(value.get('c')),
        'form_of_issue': utils.force_list(value.get('f')),
        'additional_format_characteristics': utils.force_list(value.get('g')),
        'note': utils.force_list(value.get('n')),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'source_of_acquisition_sequence': indicator_map1.get(key[3], '_'),
    }


@marc21.over('record_content_licensor', '^038__')
@utils.filter_values
def record_content_licensor(self, key, value):
    """Record Content Licensor."""
    field_map = {
        'a': 'record_content_licensor',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'record_content_licensor': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('cataloging_source', '^040__')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    field_map = {
        'a': 'original_cataloging_agency',
        'b': 'language_of_cataloging',
        'c': 'transcribing_agency',
        'd': 'modifying_agency',
        'e': 'description_conventions',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'original_cataloging_agency': value.get('a'),
        'language_of_cataloging': value.get('b'),
        'transcribing_agency': value.get('c'),
        'modifying_agency': utils.force_list(value.get('d')),
        'description_conventions': utils.force_list(value.get('e')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('language_code', '^041[_01][_7]')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    """Language Code."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Item not a translation/does not include a translation',
        '1': 'Item is or includes a translation',
    }

    indicator_map2 = {
        '_': 'MARC language code',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'language_code_of_text_sound_track_or_separate_title',
        'b': 'language_code_of_summary_or_abstract',
        'd': 'language_code_of_sung_or_spoken_text',
        'e': 'language_code_of_librettos',
        'f': 'language_code_of_table_of_contents',
        'g': 'language_code_of_accompanying_material_other_than_librettos',
        'h': 'language_code_of_original',
        'j': 'language_code_of_subtitles_or_captions',
        'k': 'language_code_of_intermediate_translations',
        'm': 'language_code_of_original_accompanying_materials_other_than_librettos',
        'n': 'language_code_of_original_libretto',
        '2': 'source_of_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('translation_indication')
    if key[4] in indicator_map2 and 'source_of_code' not in order:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code_of_text_sound_track_or_separate_title': utils.force_list(value.get('a')),
        'language_code_of_summary_or_abstract': utils.force_list(value.get('b')),
        'language_code_of_sung_or_spoken_text': utils.force_list(value.get('d')),
        'language_code_of_librettos': utils.force_list(value.get('e')),
        'language_code_of_table_of_contents': utils.force_list(value.get('f')),
        'language_code_of_accompanying_material_other_than_librettos': utils.force_list(value.get('g')),
        'language_code_of_original': utils.force_list(value.get('h')),
        'language_code_of_subtitles_or_captions': utils.force_list(value.get('j')),
        'language_code_of_intermediate_translations': utils.force_list(value.get('k')),
        'language_code_of_original_accompanying_materials_other_than_librettos': utils.force_list(value.get('m')),
        'language_code_of_original_libretto': utils.force_list(value.get('n')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'translation_indication': indicator_map1.get(key[3]),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4])
    }


@marc21.over('authentication_code', '^042__')
@utils.filter_values
def authentication_code(self, key, value):
    """Authentication Code."""
    return {
        'authentication_code': utils.force_list(value.get('a')),
    }


@marc21.over('geographic_area_code', '^043__')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_area_code': utils.force_list(value.get('a')),
        'local_gac_code': utils.force_list(value.get('b')),
        'iso_code': utils.force_list(value.get('c')),
        'authority_record_control_number_or_standard_number': utils.force_list(value.get('0')),
        'source_of_local_code': utils.force_list(value.get('2')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('country_of_publishing_producing_entity_code', '^044__')
@utils.for_each_value
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    """Country of Publishing/Producing Entity Code."""
    field_map = {
        'a': 'marc_country_code',
        'b': 'local_subentity_code',
        'c': 'iso_country_code',
        '2': 'source_of_local_subentity_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'marc_country_code': utils.force_list(value.get('a')),
        'local_subentity_code': utils.force_list(value.get('b')),
        'iso_country_code': utils.force_list(value.get('c')),
        'source_of_local_subentity_code': utils.force_list(value.get('2')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('time_period_of_content', '^045[_012]_')
@utils.filter_values
def time_period_of_content(self, key, value):
    """Time Period of Content."""
    indicator_map1 = {
        '_': 'Subfield $b or $c not present',
        '0': 'Single date/time',
        '1': 'Multiple single dates/times',
        '2': 'Range of dates/times',
    }

    field_map = {
        'a': 'time_period_code',
        'b': 'formatted_9999_bc_through_ce_time_period',
        'c': 'formatted_pre_9999_bc_time_period',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period_in_subfield_b_or_c')

    return {
        '__order__': tuple(order) if len(order) else None,
        'time_period_code': utils.force_list(
            value.get('a')),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(
            key[3]),
    }


@marc21.over('special_coded_dates', '^046__')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    field_map = {
        'a': 'type_of_date_code',
        'b': 'date_1_bc_date',
        'c': 'date_1_ce_date',
        'd': 'date_2_bc_date',
        'e': 'date_2_ce_date',
        'j': 'date_resource_modified',
        'k': 'beginning_or_single_date_created',
        'l': 'ending_date_created',
        'm': 'beginning_of_date_valid',
        'n': 'end_of_date_valid',
        'o': 'single_or_starting_date_for_aggregated_content',
        'p': 'ending_date_for_aggregated_content',
        '2': 'source_of_date',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_date_code': value.get('a'),
        'date_1_bc_date': value.get('b'),
        'date_1_ce_date': value.get('c'),
        'date_2_bc_date': value.get('d'),
        'date_2_ce_date': value.get('e'),
        'date_resource_modified': value.get('j'),
        'beginning_or_single_date_created': value.get('k'),
        'ending_date_created': value.get('l'),
        'beginning_of_date_valid': value.get('m'),
        'end_of_date_valid': value.get('n'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'ending_date_for_aggregated_content': value.get('p'),
        'source_of_date': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('form_of_musical_composition_code', '^047_[_7]')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    """Form of Musical Composition Code."""
    indicator_map2 = {
        '_': 'MARC musical composition code',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'form_of_musical_composition_code',
        '2': 'source_of_code',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if 'source_of_code' not in order and key[4] in indicator_map2:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_of_musical_composition_code': utils.force_list(
            value.get('a')),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(
            key[4],
            '_'),
    }


@marc21.over('number_of_musical_instruments_or_voices_code', '^048_[_7]')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    """Number of Musical Instruments or Voices Code."""
    indicator_map2 = {
        '_': 'MARC musical composition code',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'performer_or_ensemble',
        'b': 'soloist',
        '2': 'source_of_code',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if 'source_of_code' not in order and key[4] in indicator_map2:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'performer_or_ensemble': utils.force_list(
            value.get('a')),
        'soloist': utils.force_list(
            value.get('b')),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(
            key[4],
            '_'),
    }


@marc21.over('library_of_congress_call_number', '^050[_01][_04]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Item is in LC',
        '1': 'Item is not in LC',
    }

    indicator_map2 = {
        '0': 'Assigned by LC',
        '4': 'Assigned by agency other than LC',
    }

    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_lc_collection')
    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'existence_in_lc_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('library_of_congress_copy_issue_offprint_statement', '^051__')
@utils.for_each_value
@utils.filter_values
def library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'c': 'copy_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'copy_information': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('geographic_classification', '^052[_17]_')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    indicator_map1 = {
        '_': 'Library of Congress Classification',
        '1': 'U.S. Dept. of Defense Classification',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'geographic_classification_area_code',
        'b': 'geographic_classification_subarea_code',
        'd': 'populated_place_name',
        '2': 'code_source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if 'code_source' not in order and key[3] in indicator_map1:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')),
        'populated_place_name': utils.force_list(
            value.get('d')),
        'code_source': value.get('2') if key[3] == '7' else indicator_map1.get(
            key[3]),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21.over(
    'classification_numbers_assigned_in_canada', '^055[_01][_0-9]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    """Classification Numbers Assigned in Canada."""
    indicator_map1 = {
        '_': 'Information not provided',
        '0': 'Work held by LAC',
        '1': 'Work not held by LAC',
    }

    indicator_map2 = {
        '0': 'LC-based call number assigned by LAC',
        '1': 'Complete LC class number assigned by LAC',
        '2': 'Incomplete LC class number assigned by LAC',
        '3': 'LC-based call number assigned by the contributing library',
        '4': 'Complete LC class number assigned by the contributing library',
        '5': 'Incomplete LC class number assigned by the contributing library',
        '6': 'Other call number assigned by LAC',
        '7': 'Other class number assigned by LAC',
        '8': 'Other call number assigned by the contributing library',
        '9': 'Other class number assigned by the contributing library',
    }

    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        '2': 'source_of_call_class_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_lac_collection')
    if key[4] in indicator_map2:
        order.append('type_completeness_source_of_class_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'source_of_call_class_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'existence_in_lac_collection': indicator_map1.get(
            key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(
            key[4]),
    }


@marc21.over('national_library_of_medicine_call_number', '^060[_01][_04]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Item is in NLM',
        '1': 'Item is not in NLM',
    }

    indicator_map2 = {
        '0': 'Assigned by NLM',
        '4': 'Assigned by agency other than NLM',
    }

    field_map = {
        'a': 'classification_number_r',
        'b': 'item_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_nlm_collection')
    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number_r': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'existence_in_nlm_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_copy_statement', '^061__')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    """National Library of Medicine Copy Statement."""
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'c': 'copy_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'copy_information': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('character_sets_present', '^066__')
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
        'alternate_g0_or_g1_character_set': utils.force_list(value.get('c')),
    }


@marc21.over('national_agricultural_library_call_number', '^070[_01]_')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    indicator_map1 = {
        '0': 'Item is in NAL',
        '1': 'Item is not in NAL',
    }

    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        '8': 'field_link_and_sequence_number_r',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_nal_collection')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'field_link_and_sequence_number_r': utils.force_list(value.get('8')),
        'existence_in_nal_collection': indicator_map1.get(key[3]),
    }


@marc21.over('national_agricultural_library_copy_statement', '^071__')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    """National Agricultural Library Copy Statement."""
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'c': 'copy_information',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'copy_information': utils.force_list(value.get('c')),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('subject_category_code', '^072_[_07]')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""

    indicator_map2 = {
        '0': 'NAL subject category code list ',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'subject_category_code',
        'x': 'subject_category_code_subdivision',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'subject_category_code': value.get('a'),
        'subject_category_code_subdivision': utils.force_list(value.get('x')),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'code_source': indicator_map2.get(key[4], '_'),
    }


@marc21.over('gpo_item_number', '^074__')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    """GPO Item Number."""
    field_map = {
        'a': 'gpo_item_number',
        'z': 'canceled_invalid_gpo_item_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'gpo_item_number': value.get('a'),
        'canceled_invalid_gpo_item_number': utils.force_list(value.get('z')),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('universal_decimal_classification_number', '^080[_01]_')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Full',
        '1': 'Abridged',
    }

    field_map = {
        'a': 'universal_decimal_classification_number',
        'b': 'item_number',
        'x': 'common_auxiliary_subdivision',
        '2': 'edition_identifier',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    return {
        '__order__': tuple(order) if len(order) else None,
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'common_auxiliary_subdivision': utils.force_list(value.get('x')),
        'edition_identifier': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('dewey_decimal_classification_number', '^082[_017][_04]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {
        '0': 'Full edition',
        '1': 'Abridged edition',
        '7': 'Other edition specified in subfield $2',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Assigned by LC',
        '4': 'Assigned by agency other than LC',
    }

    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'm': 'standard_or_optional_designation',
        'q': 'assigning_agency',
        '2': 'edition_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')
    if key[4] in indicator_map2:
        order.append('source_of_classification_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
        'type_of_edition': indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21.over('additional_dewey_decimal_classification_number', '^083[_017]_')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    """Additional Dewey Decimal Classification Number."""
    indicator_map1 = {
        '0': 'Full edition',
        '1': 'Abridged edition',
        '7': 'Other edition specified in subfield $2',
    }

    field_map = {
        'a': 'classification_number',
        'c': 'classification_number__ending_number_of_span',
        'm': 'standard_or_optional_designation',
        'q': 'assigning_agency',
        'y': 'table_sequence_number_for_internal',
        'z': 'table_identification',
        '2': 'edition_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(
            value.get('a')),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')),
        'table_identification': utils.force_list(
            value.get('z')),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'type_of_edition': indicator_map1.get(
            key[3]),
    }


@marc21.over('other_classification_number', '^084__')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    field_map = {
        'a': 'classification_number',
        'b': 'item_number',
        'q': 'assigning_agency',
        '2': 'number_source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': utils.force_list(value.get('a')),
        'item_number': value.get('b'),
        'assigning_agency': value.get('q'),
        'number_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('synthesized_classification_number_components', '^085__')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    """Synthesized Classification Number Components."""
    field_map = {
        'a': 'number_where_instructions_are_found_single_number_or_beginning_number_of_span',
        'b': 'base_number',
        'c': 'classification_number_ending_number_of_span',
        'f': 'facet_designator',
        'r': 'root_number',
        's': 'digits_added_from_classification_number_in_schedule_or_external_table',
        't': 'digits_added_from_internal_subarrangement_or_add_table',
        'u': 'number_being_analyzed',
        'v': 'number_in_internal_subarrangement_or_add_table_where',
        'w': 'table_identification_internal_subarrangement_or_add',
        'y': 'table_sequence_number_for_internal_subarrangement_or',
        'z': 'table_identification',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': utils.force_list(value.get('a')),
        'base_number': utils.force_list(value.get('b')),
        'classification_number_ending_number_of_span': utils.force_list(value.get('c')),
        'facet_designator': utils.force_list(value.get('f')),
        'root_number': utils.force_list(value.get('r')),
        'digits_added_from_classification_number_in_schedule_or_external_table': utils.force_list(value.get('s')),
        'digits_added_from_internal_subarrangement_or_add_table': utils.force_list(value.get('t')),
        'number_being_analyzed': utils.force_list(value.get('u')),
        'table_identification_internal_subarrangement_or_add_table': utils.force_list(value.get('w')),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': utils.force_list(value.get('v')),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(value.get('y')),
        'table_identification': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }


@marc21.over('government_document_classification_number', '^086[_01]_')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    indicator_map1 = {
        '_': 'Source specified in subfield $2',
        '0': 'Superintendent of Documents Classification System',
        '1': 'Government of Canada Publications: Outline of Classification',
    }

    field_map = {
        'a': 'classification_number',
        'z': 'canceled_invalid_classification_number',
        '2': 'number_source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and 'number_source' not in order:
        order.append('number_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'classification_number': value.get('a'),
        'canceled_invalid_classification_number': utils.force_list(
            value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'number_source': value.get('2') if key[3] == '_' else indicator_map1.get(
            key[3]),
    }


@marc21.over('report_number', '^088__')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    """Report Number."""
    field_map = {
        'a': 'report_number',
        'z': 'canceled_invalid_report_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'report_number': value.get('a'),
        'canceled_invalid_report_number': utils.force_list(value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(value.get('8')),
    }
