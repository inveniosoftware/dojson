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


@marc21.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'nucmc_control_number',
        'a': 'lc_control_number',
        'z': 'canceled_invalid_lc_control_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nucmc_control_number': utils.force_list(
            value.get('b')
        ),
        'lc_control_number': value.get('a'),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('patent_control_information', '^013..')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    """Patent Control Information."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'd': 'date',
        'a': 'number',
        'f': 'party_to_document',
        'b': 'country',
        'c': 'type_of_number',
        '6': 'linkage',
        'e': 'status',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date': utils.force_list(
            value.get('d')
        ),
        'number': value.get('a'),
        'party_to_document': utils.force_list(
            value.get('f')
        ),
        'country': value.get('b'),
        'type_of_number': value.get('c'),
        'linkage': value.get('6'),
        'status': utils.force_list(
            value.get('e')
        ),
    }


@marc21.over('national_bibliography_number', '^015..')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    """National Bibliography Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'national_bibliography_number',
        '2': 'source',
        'q': 'qualifying_information',
        '6': 'linkage',
        'z': 'canceled_invalid_national_bibliography_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'national_bibliography_number': utils.force_list(
            value.get('a')
        ),
        'source': value.get('2'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'canceled_invalid_national_bibliography_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('national_bibliographic_agency_control_number', '^016[7_].')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    indicator_map1 = {
        "7": "Source specified in subfield $2",
        "_": "Library and Archives Canada"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'source',
        'a': 'record_control_number',
        'z': 'canceled_invalid_control_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('national_bibliographic_agency')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'record_control_number': value.get('a'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'national_bibliographic_agency': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
    }


@marc21.over('copyright_or_legal_deposit_number', '^017.[8_]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
    indicator_map2 = {
        "8": "No display constant generated",
        "_": "Copyright or legal deposit number"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'd': 'date',
        'a': 'copyright_or_legal_deposit_number',
        'b': 'assigning_agency',
        '2': 'source',
        'i': 'display_text',
        '6': 'linkage',
        'z': 'canceled_invalid_copyright_or_legal_deposit_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date': value.get('d'),
        'copyright_or_legal_deposit_number': utils.force_list(
            value.get('a')
        ),
        'assigning_agency': value.get('b'),
        'source': value.get('2'),
        'display_text': value.get('i'),
        'linkage': value.get('6'),
        'canceled_invalid_copyright_or_legal_deposit_number': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('copyright_article_fee_code', '^018..')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    """Copyright Article-Fee Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'copyright_article_fee_code_nr',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copyright_article_fee_code_nr': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'international_standard_book_number',
        'z': 'canceled_invalid_isbn',
        'q': 'qualifying_information',
        '6': 'linkage',
        'c': 'terms_of_availability',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_book_number': value.get('a'),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'terms_of_availability': value.get('c'),
    }


@marc21.over('international_standard_serial_number', '^022[01_].')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    indicator_map1 = {
        "0": "Continuing resource of international interest",
        "1": "Continuing resource not of international interest",
        "_": "No level specified"}
    field_map = {
        'l': 'issn_l',
        '8': 'field_link_and_sequence_number',
        'a': 'international_standard_serial_number',
        'y': 'incorrect_issn',
        '2': 'source',
        'z': 'canceled_issn',
        '6': 'linkage',
        'm': 'canceled_issn_l',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level_of_international_interest')

    return {
        '__order__': tuple(order) if len(order) else None,
        'issn_l': value.get('l'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_serial_number': value.get('a'),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'source': value.get('2'),
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'level_of_international_interest': indicator_map1.get(key[3]),
    }


@marc21.over('other_standard_identifier', '^024[4837201_][01_]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {
        "0": "International Standard Recording Code",
        "1": "Universal Product Code",
        "2": "International Standard Music Number",
        "3": "International Article Number",
        "4": "Serial Item and Contribution Identifier",
        "7": "Source specified in subfield $2",
        "8": "Unspecified type of standard number or code"}
    indicator_map2 = {
        "0": "No difference",
        "1": "Difference",
        "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'd': 'additional_codes_following_the_standard_number_or_code',
        'a': 'standard_number_or_code',
        'z': 'canceled_invalid_standard_number_or_code',
        '2': 'source_of_number_or_code',
        'c': 'terms_of_availability',
        '6': 'linkage',
        'q': 'qualifying_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_standard_number_or_code')

    if key[4] in indicator_map2:
        order.append('difference_indicator')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'standard_number_or_code': value.get('a'),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'source_of_number_or_code': value.get('2'),
        'terms_of_availability': value.get('c'),
        'linkage': value.get('6'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'type_of_standard_number_or_code': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'difference_indicator': indicator_map2.get(key[4]),
    }


@marc21.over('overseas_acquisition_number', '^025..')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    """Overseas Acquisition Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'overseas_acquisition_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'overseas_acquisition_number': utils.force_list(
            value.get('a')
        ),
    }


@marc21.over('fingerprint_identifier', '^026..')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    """Fingerprint Identifier."""
    field_map = {
        '5': 'institution_to_which_field_applies',
        'd': 'number_of_volume_or_part',
        'a': 'first_and_second_groups_of_characters',
        'e': 'unparsed_fingerprint',
        'b': 'third_and_fourth_groups_of_characters',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'c': 'date',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'number_of_volume_or_part': utils.force_list(
            value.get('d')
        ),
        'first_and_second_groups_of_characters': value.get('a'),
        'unparsed_fingerprint': value.get('e'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'date': value.get('c'),
    }


@marc21.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'z': 'canceled_invalid_number',
        'a': 'standard_technical_report_number',
        '6': 'linkage',
        'q': 'qualifying_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_number': utils.force_list(
            value.get('z')
        ),
        'standard_technical_report_number': value.get('a'),
        'linkage': value.get('6'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
    }


@marc21.over('publisher_number', '^028[453201_][2103_]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    """Publisher Number."""
    indicator_map1 = {
        "0": "Issue number",
        "1": "Matrix number",
        "2": "Plate number",
        "3": "Other music number",
        "4": "Videorecording number",
        "5": "Other publisher number"}
    indicator_map2 = {
        "0": "No note, no added entry",
        "1": "Note, added entry",
        "2": "Note, no added entry",
        "3": "No note, added entry"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'source',
        'a': 'publisher_number',
        '6': 'linkage',
        'q': 'qualifying_information',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_publisher_number')

    if key[4] in indicator_map2:
        order.append('note_added_entry_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('b'),
        'publisher_number': value.get('a'),
        'linkage': value.get('6'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'type_of_publisher_number': indicator_map1.get(key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4]),
    }


@marc21.over('coden_designation', '^030..')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    """CODEN Designation."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'coden',
        '6': 'linkage',
        'z': 'canceled_invalid_coden',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'coden': value.get('a'),
        'linkage': value.get('6'),
        'canceled_invalid_coden': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    field_map = {
        's': 'coded_validity_note',
        'y': 'link_text',
        'a': 'number_of_work',
        'p': 'musical_notation',
        'n': 'key_signature',
        'b': 'number_of_movement',
        '2': 'system_code',
        'z': 'public_note',
        '6': 'linkage',
        'c': 'number_of_excerpt',
        'r': 'key_or_mode',
        '8': 'field_link_and_sequence_number',
        'd': 'caption_or_heading',
        'm': 'voice_instrument',
        'u': 'uniform_resource_identifier',
        't': 'text_incipit',
        'o': 'time_signature',
        'q': 'general_note',
        'g': 'clef',
        'e': 'role',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'number_of_work': value.get('a'),
        'musical_notation': value.get('p'),
        'key_signature': value.get('n'),
        'number_of_movement': value.get('b'),
        'system_code': value.get('2'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'number_of_excerpt': value.get('c'),
        'key_or_mode': value.get('r'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'voice_instrument': value.get('m'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'time_signature': value.get('o'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'clef': value.get('g'),
        'role': value.get('e'),
    }


@marc21.over('postal_registration_number', '^032..')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    """Postal Registration Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'source_agency_assigning_number',
        'a': 'postal_registration_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'postal_registration_number': value.get('a'),
        'linkage': value.get('6'),
    }


@marc21.over('date_time_and_place_of_an_event', '^033[201_][201_]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    """Date/Time and Place of an Event."""
    indicator_map1 = {
        "0": "Single date",
        "1": "Multiple single dates",
        "2": "Range of dates",
        "_": "No date information"}
    indicator_map2 = {
        "0": "Capture",
        "1": "Broadcast",
        "2": "Finding",
        "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'c': 'geographic_classification_subarea_code',
        '3': 'materials_specified',
        'p': 'place_of_event',
        'b': 'geographic_classification_area_code',
        '2': 'source_of_term',
        '0': 'authority_record_control_number',
        '6': 'linkage',
        'a': 'formatted_date_time',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_date_in_subfield_a')

    if key[4] in indicator_map2:
        order.append('type_of_event')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'geographic_classification_area_code': utils.force_list(
            value.get('b')
        ),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'formatted_date_time': utils.force_list(
            value.get('a')
        ),
        'type_of_date_in_subfield_a': indicator_map1.get(key[3]),
        'type_of_event': indicator_map2.get(key[4]),
    }


@marc21.over('coded_cartographic_mathematical_data', '^034[103_][01_]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map1 = {
        "0": "Scale indeterminable/No scale recorded",
        "1": "Single scale",
        "3": "Range of scales"}
    indicator_map2 = {
        "0": "Outer ring",
        "1": "Exclusion ring",
        "_": "Not applicable"}
    field_map = {
        'j': 'declination_northern_limit',
        'z': 'name_of_extraterrestrial_body',
        'n': 'right_ascension_western_limit',
        'b': 'constant_ratio_linear_horizontal_scale',
        '2': 'source',
        'a': 'category_of_scale',
        'm': 'right_ascension_eastern_limit',
        'y': 'ending_date',
        's': 'g_ring_latitude',
        'c': 'constant_ratio_linear_vertical_scale',
        '3': 'materials_specified',
        'p': 'equinox',
        'e': 'coordinates_easternmost_longitude',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'g': 'coordinates_southernmost_latitude',
        'r': 'distance_from_earth',
        'k': 'declination_southern_limit',
        'd': 'coordinates_westernmost_longitude',
        'f': 'coordinates_northernmost_latitude',
        't': 'g_ring_longitude',
        'x': 'beginning_date',
        'h': 'angular_scale',
        '0': 'authority_record_control_number_or_standard_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_scale')

    if key[4] in indicator_map2:
        order.append('type_of_ring')

    return {
        '__order__': tuple(order) if len(order) else None,
        'declination_northern_limit': value.get('j'),
        'name_of_extraterrestrial_body': value.get('z'),
        'right_ascension_western_limit': value.get('n'),
        'constant_ratio_linear_horizontal_scale': utils.force_list(
            value.get('b')
        ),
        'source': value.get('2'),
        'category_of_scale': value.get('a'),
        'right_ascension_eastern_limit': value.get('m'),
        'ending_date': value.get('y'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'constant_ratio_linear_vertical_scale': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'equinox': value.get('p'),
        'coordinates_easternmost_longitude': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'coordinates_southernmost_latitude': value.get('g'),
        'distance_from_earth': value.get('r'),
        'declination_southern_limit': value.get('k'),
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_northernmost_latitude': value.get('f'),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'beginning_date': value.get('x'),
        'angular_scale': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'type_of_scale': indicator_map1.get(key[3]),
        'type_of_ring': indicator_map2.get(key[4]),
    }


@marc21.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'system_control_number',
        '6': 'linkage',
        'z': 'canceled_invalid_control_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'system_control_number': value.get('a'),
        'linkage': value.get('6'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('original_study_number_for_computer_data_files', '^036..')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    """Original Study Number for Computer Data Files."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'source_agency_assigning_number',
        'a': 'original_study_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'original_study_number': value.get('a'),
        'linkage': value.get('6'),
    }


@marc21.over('source_of_acquisition', '^037[23_].')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    """Source of Acquisition."""
    indicator_map1 = {"2": "Intervening", "3": "Current/Latest",
                      "_": "Not applicable/No information provided/Earliest"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'c': 'terms_of_availability',
        '3': 'materials_specified',
        'f': 'form_of_issue',
        'n': 'note',
        'b': 'source_of_stock_number_acquisition',
        'g': 'additional_format_characteristics',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
        'a': 'stock_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('source_of_acquisition_sequence')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'terms_of_availability': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'form_of_issue': utils.force_list(
            value.get('f')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'source_of_stock_number_acquisition': value.get('b'),
        'additional_format_characteristics': utils.force_list(
            value.get('g')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'stock_number': value.get('a'),
        'source_of_acquisition_sequence': indicator_map1.get(key[3]),
    }


@marc21.over('record_content_licensor', '^038..')
@utils.filter_values
def record_content_licensor(self, key, value):
    """Record Content Licensor."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'record_content_licensor',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_content_licensor': value.get('a'),
        'linkage': value.get('6'),
    }


@marc21.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'd': 'modifying_agency',
        'a': 'original_cataloging_agency',
        'b': 'language_of_cataloging',
        'c': 'transcribing_agency',
        '6': 'linkage',
        'e': 'description_conventions',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'original_cataloging_agency': value.get('a'),
        'language_of_cataloging': value.get('b'),
        'transcribing_agency': value.get('c'),
        'linkage': value.get('6'),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
    }


@marc21.over('language_code', '^041[01_][7_]')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    """Language Code."""
    indicator_map1 = {
        "0": "Item not a translation/does not include a translation",
        "1": "Item is or includes a translation",
        "_": "No information provided"}
    indicator_map2 = {
        "7": "Source specified in subfield $2",
        "_": "MARC language code"}
    field_map = {
        'j': 'language_code_of_subtitles_or_captions',
        'a': 'language_code_of_text_sound_track_or_separate_title',
        'n': 'language_code_of_original_libretto',
        'b': 'language_code_of_summary_or_abstract',
        '2': 'source_of_code',
        'm': 'language_code_of_original_accompanying_materials_other_than_librettos',
        'k': 'language_code_of_intermediate_translations',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'd': 'language_code_of_sung_or_spoken_text',
        'f': 'language_code_of_table_of_contents',
        'h': 'language_code_of_original',
        'g': 'language_code_of_accompanying_material_other_than_librettos',
        'e': 'language_code_of_librettos',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('translation_indication')

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code_of_subtitles_or_captions': utils.force_list(
            value.get('j')
        ),
        'language_code_of_text_sound_track_or_separate_title': utils.force_list(
            value.get('a')
        ),
        'language_code_of_original_libretto': utils.force_list(
            value.get('n')
        ),
        'language_code_of_summary_or_abstract': utils.force_list(
            value.get('b')
        ),
        'language_code_of_original_accompanying_materials_other_than_librettos': utils.force_list(
            value.get('m')
        ),
        'language_code_of_intermediate_translations': utils.force_list(
            value.get('k')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_code_of_sung_or_spoken_text': utils.force_list(
            value.get('d')
        ),
        'language_code_of_table_of_contents': utils.force_list(
            value.get('f')
        ),
        'language_code_of_original': utils.force_list(
            value.get('h')
        ),
        'language_code_of_accompanying_material_other_than_librettos': utils.force_list(
            value.get('g')
        ),
        'language_code_of_librettos': utils.force_list(
            value.get('e')
        ),
        'translation_indication': indicator_map1.get(key[3]),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('authentication_code', '^042..')
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


@marc21.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'geographic_area_code',
        'b': 'local_gac_code',
        '2': 'source_of_local_code',
        '0': 'authority_record_control_number_or_standard_number',
        '6': 'linkage',
        'c': 'iso_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'iso_code': utils.force_list(
            value.get('c')
        ),
    }


@marc21.over('country_of_publishing_producing_entity_code', '^044..')
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    """Country of Publishing/Producing Entity Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'marc_country_code',
        'b': 'local_subentity_code',
        '2': 'source_of_local_subentity_code',
        'c': 'iso_country_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'marc_country_code': utils.force_list(
            value.get('a')
        ),
        'local_subentity_code': utils.force_list(
            value.get('b')
        ),
        'source_of_local_subentity_code': utils.force_list(
            value.get('2')
        ),
        'iso_country_code': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('time_period_of_content', '^045[201_].')
@utils.filter_values
def time_period_of_content(self, key, value):
    """Time Period of Content."""
    indicator_map1 = {
        "0": "Single date/time",
        "1": "Multiple single dates/times",
        "2": "Range of dates/times",
        "_": "Subfield $b or $c not present"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'formatted_9999_bc_through_ce_time_period',
        'a': 'time_period_code',
        '6': 'linkage',
        'c': 'formatted_pre_9999_bc_time_period',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period_in_subfield_b_or_c')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
        ),
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3]),
    }


@marc21.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    field_map = {
        'l': 'ending_date_created',
        'j': 'date_resource_modified',
        'a': 'type_of_date_code',
        'p': 'ending_date_for_aggregated_content',
        'n': 'end_of_date_valid',
        'b': 'date_1_bc_date',
        '2': 'source_of_date',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'k': 'beginning_or_single_date_created',
        'd': 'date_2_bc_date',
        'm': 'beginning_of_date_valid',
        'o': 'single_or_starting_date_for_aggregated_content',
        'c': 'date_1_ce_date',
        'e': 'date_2_ce_date',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'ending_date_created': value.get('l'),
        'date_resource_modified': value.get('j'),
        'type_of_date_code': value.get('a'),
        'ending_date_for_aggregated_content': value.get('p'),
        'end_of_date_valid': value.get('n'),
        'date_1_bc_date': value.get('b'),
        'source_of_date': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'beginning_or_single_date_created': value.get('k'),
        'date_2_bc_date': value.get('d'),
        'beginning_of_date_valid': value.get('m'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'date_1_ce_date': value.get('c'),
        'date_2_ce_date': value.get('e'),
    }


@marc21.over('form_of_musical_composition_code', '^047.[7_]')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    """Form of Musical Composition Code."""
    indicator_map2 = {
        "7": "Source specified in subfield $2",
        "_": "MARC musical composition code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_code',
        'a': 'form_of_musical_composition_code',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_of_musical_composition_code': utils.force_list(
            value.get('a')
        ),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('number_of_musical_instruments_or_voices_code', '^048.[7_]')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    """Number of Musical Instruments or Voices Code."""
    indicator_map2 = {"7": "Source specified in subfield $2", "_": "MARC code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_code',
        'b': 'soloist',
        'a': 'performer_or_ensemble',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2 and '2' not in value:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'performer_or_ensemble': utils.force_list(
            value.get('a')
        ),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('library_of_congress_call_number', '^050[01_][40_]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map1 = {
        "0": "Item is in LC",
        "1": "Item is not in LC",
        "_": "No information provided"}
    indicator_map2 = {"0": "Assigned by LC",
                      "4": "Assigned by agency other than LC"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'item_number',
        '6': 'linkage',
        '3': 'materials_specified',
        'a': 'classification_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_lc_collection')

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'materials_specified': value.get('3'),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'existence_in_lc_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('library_of_congress_copy_issue_offprint_statement', '^051..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'item_number',
        'a': 'classification_number',
        'c': 'copy_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'classification_number': value.get('a'),
        'copy_information': value.get('c'),
    }


@marc21.over('geographic_classification', '^052[71_].')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    indicator_map1 = {
        "1": "U.S. Dept. of Defense Classification",
        "7": "Source specified in subfield $2",
        "_": "Library of Congress Classification"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'd': 'populated_place_name',
        'a': 'geographic_classification_area_code',
        'b': 'geographic_classification_subarea_code',
        '2': 'code_source',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and '2' not in value:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'code_source': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
    }


@marc21.over('classification_numbers_assigned_in_canada',
             '^055[01_][9721645803_]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    """Classification Numbers Assigned in Canada."""
    indicator_map1 = {
        "0": "Work held by LAC",
        "1": "Work not held by LAC",
        "_": "Information not provided"}
    indicator_map2 = {
        "0": "LC-based call number assigned by LAC",
        "1": "Complete LC class number assigned by LAC",
        "2": "Incomplete LC class number assigned by LAC",
        "3": "LC-based call number assigned by the contributing library",
        "4": "Complete LC class number assigned by the contributing library",
        "5": "Incomplete LC class number assigned by the contributing library",
        "6": "Other call number assigned by LAC",
        "7": "Other class number assigned by LAC",
        "8": "Other call number assigned by the contributing library",
        "9": "Other class number assigned by the contributing library"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'source_of_call_class_number',
        'b': 'item_number',
        'a': 'classification_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_lac_collection')

    if key[4] in indicator_map2:
        order.append('type_completeness_source_of_class_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_call_class_number': value.get('2'),
        'item_number': value.get('b'),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_call_number', '^060[01_][40_]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map1 = {
        "0": "Item is in NLM",
        "1": "Item is not in NLM",
        "_": "No information provided"}
    indicator_map2 = {"0": "Assigned by NLM",
                      "4": "Assigned by agency other than NLM"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'item_number',
        'a': 'classification_number_r',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_nlm_collection')

    if key[4] in indicator_map2:
        order.append('source_of_call_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'classification_number_r': utils.force_list(
            value.get('a')
        ),
        'existence_in_nlm_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_copy_statement', '^061..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    """National Library of Medicine Copy Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'item_number',
        'a': 'classification_number',
        'c': 'copy_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'copy_information': value.get('c'),
    }


@marc21.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    """Character Sets Present."""
    field_map = {
        'b': 'primary_g1_character_set',
        'a': 'primary_g0_character_set',
        'c': 'alternate_g0_or_g1_character_set',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'primary_g1_character_set': value.get('b'),
        'primary_g0_character_set': value.get('a'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
    }


@marc21.over('national_agricultural_library_call_number', '^070[01_].')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    indicator_map1 = {"0": "Item is in NAL", "1": "Item is not in NAL"}
    field_map = {
        '8': 'field_link_and_sequence_number_r',
        'b': 'item_number',
        'a': 'classification_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('existence_in_nal_collection')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'existence_in_nal_collection': indicator_map1.get(key[3]),
    }


@marc21.over('national_agricultural_library_copy_statement', '^071..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    """National Agricultural Library Copy Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'item_number',
        'a': 'classification_number',
        'c': 'copy_information',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'copy_information': utils.force_list(
            value.get('c')
        ),
    }


@marc21.over('subject_category_code', '^072.[70_]')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    indicator_map2 = {
        "0": "NAL subject category code list",
        "7": "Source specified in subfield $2"}
    field_map = {
        'x': 'subject_category_code_subdivision',
        '8': 'field_link_and_sequence_number',
        '2': 'source',
        'a': 'subject_category_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('code_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'subject_category_code': value.get('a'),
        'linkage': value.get('6'),
        'code_source': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('gpo_item_number', '^074..')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    """GPO Item Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'gpo_item_number',
        'z': 'canceled_invalid_gpo_item_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'gpo_item_number': value.get('a'),
        'canceled_invalid_gpo_item_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('universal_decimal_classification_number', '^080[01_].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {
        "0": "Full",
        "1": "Abridged",
        "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'x': 'common_auxiliary_subdivision',
        'a': 'universal_decimal_classification_number',
        'b': 'item_number',
        '2': 'edition_identifier',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'edition_identifier': value.get('2'),
        'linkage': value.get('6'),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('dewey_decimal_classification_number', '^082[701_][40_]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {
        "0": "Full edition",
        "1": "Abridged edition",
        "7": "Other edition specified in subfield $2"}
    indicator_map2 = {
        "0": "Assigned by LC",
        "4": "Assigned by agency other than LC",
        "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'b': 'item_number',
        '2': 'edition_number',
        'q': 'assigning_agency',
        '6': 'linkage',
        'm': 'standard_or_optional_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    if key[4] in indicator_map2:
        order.append('source_of_classification_number')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'edition_number': value.get('2'),
        'assigning_agency': value.get('q'),
        'linkage': value.get('6'),
        'standard_or_optional_designation': value.get('m'),
        'type_of_edition': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21.over('additional_dewey_decimal_classification_number', '^083[701_].')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    """Additional Dewey Decimal Classification Number."""
    indicator_map1 = {
        "0": "Full edition",
        "1": "Abridged edition",
        "7": "Other edition specified in subfield $2"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        'z': 'table_identification',
        '2': 'edition_number',
        'q': 'assigning_agency',
        'c': 'classification_number_ending_number_of_span',
        '6': 'linkage',
        'm': 'standard_or_optional_designation',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_edition')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'edition_number': value.get('2'),
        'assigning_agency': value.get('q'),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'linkage': value.get('6'),
        'standard_or_optional_designation': value.get('m'),
        'type_of_edition': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
    }


@marc21.over('other_classification_number', '^084..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'b': 'item_number',
        '2': 'number_source',
        'q': 'assigning_agency',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'number_source': value.get('2'),
        'assigning_agency': value.get('q'),
        'linkage': value.get('6'),
    }


@marc21.over('synthesized_classification_number_components', '^085..')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    """Synthesized Classification Number Components."""
    field_map = {
        'a': 'number_where_instructions_are_found_single_number_or_beginning_number_of_span',
        'r': 'root_number',
        'w': 'table_identification_internal_subarrangement_or_add_table',
        'b': 'base_number',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        'v': 'number_in_internal_subarrangement_or_add_table_where_instructions_are_found',
        '6': 'linkage',
        'z': 'table_identification',
        '8': 'field_link_and_sequence_number',
        'f': 'facet_designator',
        'u': 'number_being_analyzed',
        't': 'digits_added_from_internal_subarrangement_or_add_table',
        's': 'digits_added_from_classification_number_in_schedule_or_external_table',
        'c': 'classification_number_ending_number_of_span',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': utils.force_list(
            value.get('a')
        ),
        'root_number': utils.force_list(
            value.get('r')
        ),
        'table_identification_internal_subarrangement_or_add_table': utils.force_list(
            value.get('w')
        ),
        'base_number': utils.force_list(
            value.get('b')
        ),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'facet_designator': utils.force_list(
            value.get('f')
        ),
        'number_being_analyzed': utils.force_list(
            value.get('u')
        ),
        'digits_added_from_internal_subarrangement_or_add_table': utils.force_list(
            value.get('t')
        ),
        'digits_added_from_classification_number_in_schedule_or_external_table': utils.force_list(
            value.get('s')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
    }


@marc21.over('government_document_classification_number', '^086[01_].')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    indicator_map1 = {
        "0": "Superintendent of Documents Classification System",
        "1": "Government of Canada Publications: Outline of Classification",
        "_": "Source specified in subfield $2"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        '2': 'number_source',
        'a': 'classification_number',
        '6': 'linkage',
        'z': 'canceled_invalid_classification_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and '2' not in value:
        order.append('number_source')

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': value.get('a'),
        'linkage': value.get('6'),
        'canceled_invalid_classification_number': utils.force_list(
            value.get('z')
        ),
        'number_source': value.get('2') if key[3] == '_' else indicator_map1.get(key[3]),
    }


@marc21.over('report_number', '^088..')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    """Report Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'report_number',
        '6': 'linkage',
        'z': 'canceled_invalid_report_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'report_number': value.get('a'),
        'linkage': value.get('6'),
        'canceled_invalid_report_number': utils.force_list(
            value.get('z')
        ),
    }
