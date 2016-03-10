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

from ..model import to_marc21


@to_marc21.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""
    field_map = {
        'lc_control_number': 'a',
        'nucmc_control_number': 'b',
        'canceled_invalid_lc_control_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('lc_control_number'),
        'b': utils.reverse_force_list(
            value.get('nucmc_control_number')),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('013', '^patent_control_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_patent_control_information(self, key, value):
    """Reverse - Patent Control Information."""
    field_map = {
        'number': 'a',
        'country': 'b',
        'type_of_number': 'c',
        'date': 'd',
        'status': 'e',
        'party_to_document': 'f',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number'),
        'b': value.get('country'),
        'c': value.get('type_of_number'),
        'd': utils.reverse_force_list(
            value.get('date')),
        'e': utils.reverse_force_list(
            value.get('status')),
        'f': utils.reverse_force_list(
            value.get('party_to_document')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('015', '^national_bibliography_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliography_number(self, key, value):
    """Reverse - National Bibliography Number."""
    field_map = {
        'national_bibliography_number': 'a',
        'qualifying_information': 'q',
        'canceled_invalid_national_bibliography_number': 'z',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('national_bibliography_number')),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_national_bibliography_number')),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    indicator_map1 = {
        'Library and Archives Canada': '_',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'record_control_number': 'a',
        'canceled_invalid_control_number': 'z',
        'source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('national_bibliographic_agency'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('017', '^copyright_or_legal_deposit_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copyright_or_legal_deposit_number(self, key, value):
    """Reverse - Copyright or Legal Deposit Number."""
    indicator_map2 = {
        "Copyright or legal deposit number": "_",
        "No display constant generated": "8",
    }

    field_map = {
        'copyright_or_legal_deposit_number': 'a',
        'assigning_agency': 'b',
        'date': 'd',
        'display_text': 'i',
        'canceled_invalid_copyright_or_legal_deposit_number': 'z',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('copyright_or_legal_deposit_number')),
        'b': value.get('assigning_agency'),
        'd': value.get('date'),
        'i': value.get('display_text'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_copyright_or_legal_deposit_number')),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(
            value.get('display_constant_controller'),
            '_'),
    }


@to_marc21.over('018', '^copyright_article_fee_code$')
@utils.filter_values
def reverse_copyright_article_fee_code(self, key, value):
    """Reverse - Copyright Article-Fee Code."""
    field_map = {
        'copyright_article_fee_code': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('copyright_article_fee_code')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('020', '^international_standard_book_number$')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_book_number'),
        'c': value.get('terms_of_availability'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    indicator_map1 = {
        'No level specified': '_',
        'Continuing resource of international interest': '0',
        'Continuing resource not of international interest': '1',
    }

    field_map = {
        'international_standard_serial_number': 'a',
        'issn_l': 'l',
        'canceled_issn_l': 'm',
        'incorrect_issn': 'y',
        'canceled_issn': 'z',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_serial_number'),
        'l': value.get('issn_l'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('level_of_international_interest'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {
        'International Article Number': '3',
        'International Standard Music Number': '2',
        'International Standard Recording Code': '0',
        'Serial Item and Contribution Identifier': '4',
        'Source specified in subfield $2': '7',
        'Universal Product Code': '1',
        'Unspecified type of standard number or code': '8',
    }

    indicator_map2 = {
        'Difference': '1',
        'No difference': '0',
        'No information provided': '_',
    }

    field_map = {
        'standard_number_or_code': 'a',
        'terms_of_availability': 'c',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'qualifying_information': 'q',
        'source_of_number_or_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'canceled_invalid_standard_number_or_code': 'z',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_standard_number_or_code'),
            '7') != '7' and '2' in order:
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('standard_number_or_code'),
        'c': value.get('terms_of_availability'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')),
        '2': value.get('source_of_number_or_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_standard_number_or_code'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get(
                'difference_indicator',
                '_')),
    }


@to_marc21.over('025', '^overseas_acquisition_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_overseas_acquisition_number(self, key, value):
    """Reverse - Overseas Acquisition Number."""
    field_map = {
        'overseas_acquisition_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('overseas_acquisition_number')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('026', '^fingerprint_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_fingerprint_identifier(self, key, value):
    """Reverse - Fingerprint Identifier."""
    field_map = {
        'first_and_second_groups_of_characters': 'a',
        'third_and_fourth_groups_of_characters': 'b',
        'date': 'c',
        'number_of_volume_or_part': 'd',
        'unparsed_fingerprint': 'e',
        'source': '2',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('first_and_second_groups_of_characters'),
        'b': value.get('third_and_fourth_groups_of_characters'),
        'c': value.get('date'),
        'd': utils.reverse_force_list(
            value.get('number_of_volume_or_part')),
        'e': value.get('unparsed_fingerprint'),
        '2': value.get('source'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('027', '^standard_technical_report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_standard_technical_report_number(self, key, value):
    """Reverse - Standard Technical Report Number."""
    field_map = {
        'standard_technical_report_number': 'a',
        'qualifying_information': 'q',
        'canceled_invalid_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('standard_technical_report_number'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_number')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('028', '^publisher_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publisher_number(self, key, value):
    """Reverse - Publisher Number."""
    indicator_map1 = {
        'Issue number': '0',
        'Matrix number': '1',
        'Plate number': '2',
        'Other music number': '3',
        'Videorecording number': '4',
        'Other publisher number': '5',
    }

    indicator_map2 = {
        'No note, no added entry': '0',
        'Note, added entry': '1',
        'Note, no added entry': '2',
        'No note, added entry': '3',
    }

    field_map = {
        'publisher_number': 'a',
        'source': 'b',
        'qualifying_information': 'q',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('publisher_number'),
        'b': value.get('source'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_publisher_number'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('note_added_entry_controller'),
            '_'),
    }


@to_marc21.over('030', '^coden_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coden_designation(self, key, value):
    """Reverse - CODEN Designation."""
    field_map = {
        'coden': 'a',
        'canceled_invalid_coden': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('coden'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_coden')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('031', '^musical_incipits_information$')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number_of_work'),
        'b': value.get('number_of_movement'),
        'c': value.get('number_of_excerpt'),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')),
        'e': value.get('role'),
        'g': value.get('clef'),
        'm': value.get('voice_instrument'),
        'n': value.get('key_signature'),
        'o': value.get('time_signature'),
        'p': value.get('musical_notation'),
        'q': utils.reverse_force_list(
            value.get('general_note')),
        'r': value.get('key_or_mode'),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')),
        't': utils.reverse_force_list(
            value.get('text_incipit')),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        'y': utils.reverse_force_list(
            value.get('link_text')),
        'z': utils.reverse_force_list(
            value.get('public_note')),
        '2': value.get('system_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('032', '^postal_registration_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_postal_registration_number(self, key, value):
    """Reverse - Postal Registration Number."""
    field_map = {
        'postal_registration_number': 'a',
        'source_agency_assigning_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('postal_registration_number'),
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('033', '^date_time_and_place_of_an_event$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event(self, key, value):
    """Reverse - Date/Time and Place of an Event."""
    indicator_map1 = {
        'No date information': '_',
        'Single date': '0',
        'Multiple single dates': '1',
        'Range of dates': '2',
    }

    indicator_map2 = {
        'No information provided': '_',
        'Capture': '0',
        'Broadcast': '1',
        'Finding': '2',
    }

    field_map = {
        'formatted_date_time': 'a',
        'geographic_classification_area_code': 'b',
        'geographic_classification_subarea_code': 'c',
        'place_of_event': 'p',
        'authority_record_control_number_or_standard_number': '0',
        'source_of_term': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('formatted_date_time')),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_area_code')),
        'c': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')),
        'p': utils.reverse_force_list(
            value.get('place_of_event')),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        '2': utils.reverse_force_list(
            value.get('source_of_term')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_date_in_subfield_a'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('type_of_event'),
            '_'),
    }


@to_marc21.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map1 = {
        'Scale indeterminable/No scale recorded': '0',
        'Single scale': '1',
        'Range of scales': '3',

    }

    indicator_map2 = {
        'Not applicable': '_',
        'Outer ring': '0',
        'Exclusion ring': '1',
    }

    field_map = {
        'category_of_scale': 'a',
        'constant_ratio_linear_horizontal_scale': 'b',
        'constant_ratio_linear_vertical_scale': 'c',
        'coordinates_westernmost_longitude': 'd',
        'coordinates_easternmost_longitude': 'e',
        'coordinates_northernmost_latitude': 'f',
        'coordinates_southernmost_latitude': 'g',
        'angular_scale': 'h',
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('category_of_scale'),
        'b': utils.reverse_force_list(
            value.get('constant_ratio_linear_horizontal_scale')),
        'c': utils.reverse_force_list(
            value.get('constant_ratio_linear_vertical_scale')),
        'd': value.get('coordinates_westernmost_longitude'),
        'e': value.get('coordinates_easternmost_longitude'),
        'f': value.get('coordinates_northernmost_latitude'),
        'g': value.get('coordinates_southernmost_latitude'),
        'h': utils.reverse_force_list(
            value.get('angular_scale')),
        'j': value.get('declination_northern_limit'),
        'k': value.get('declination_southern_limit'),
        'm': value.get('right_ascension_eastern_limit'),
        'n': value.get('right_ascension_western_limit'),
        'p': value.get('equinox'),
        'r': value.get('distance_from_earth'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')),
        'x': value.get('beginning_date'),
        'y': value.get('ending_date'),
        'z': value.get('name_of_extraterrestrial_body'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        '2': value.get('source'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_scale'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('type_of_ring'),
            '_'),
    }


@to_marc21.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    field_map = {
        'system_control_number': 'a',
        'canceled_invalid_control_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('system_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('036', '^original_study_number_for_computer_data_files$')
@utils.filter_values
def reverse_original_study_number_for_computer_data_files(self, key, value):
    """Reverse - Original Study Number for Computer Data Files."""
    field_map = {
        'original_study_number': 'a',
        'source_agency_assigning_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_study_number'),
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('037', '^source_of_acquisition$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_acquisition(self, key, value):
    """Reverse - Source of Acquisition."""
    indicator_map1 = {
        'Not applicable/No information provided/Earliest': '_',
        'Intervening': '2',
        'Current/Latest': '3',
    }

    field_map = {
        'stock_number': 'a',
        'source_of_stock_number_acquisition': 'b',
        'terms_of_availability': 'c',
        'form_of_issue': 'f',
        'additional_format_characteristics': 'g',
        'note': 'n',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('stock_number'),
        'b': value.get('source_of_stock_number_acquisition'),
        'c': utils.reverse_force_list(
            value.get('terms_of_availability')),
        'f': utils.reverse_force_list(
            value.get('form_of_issue')),
        'g': utils.reverse_force_list(
            value.get('additional_format_characteristics')),
        'n': utils.reverse_force_list(
            value.get('note')),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('source_of_acquisition_sequence'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('038', '^record_content_licensor$')
@utils.filter_values
def reverse_record_content_licensor(self, key, value):
    """Reverse - Record Content Licensor."""
    field_map = {
        'record_content_licensor': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_content_licensor'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    field_map = {
        'original_cataloging_agency': 'a',
        'language_of_cataloging': 'b',
        'transcribing_agency': 'c',
        'modifying_agency': 'd',
        'description_conventions': 'e',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_cataloging_agency'),
        'b': value.get('language_of_cataloging'),
        'c': value.get('transcribing_agency'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')),
        'e': utils.reverse_force_list(
            value.get('description_conventions')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('041', '^language_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_code(self, key, value):
    """Reverse - Language Code."""
    indicator_map1 = {
        'No information provided': '_',
        'Item not a translation/does not include a translation': '0',
        'Item is or includes a translation': '1',
    }

    indicator_map2 = {
        'MARC language code': '_',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'language_code_of_text_sound_track_or_separate_title': 'a',
        'language_code_of_summary_or_abstract': 'b',
        'language_code_of_sung_or_spoken_text': 'd',
        'language_code_of_librettos': 'e',
        'language_code_of_table_of_contents': 'f',
        'language_code_of_accompanying_material_other_than_librettos': 'g',
        'language_code_of_original': 'h',
        'language_code_of_subtitles_or_captions': 'j',
        'language_code_of_intermediate_translations': 'k',
        'language_code_of_original_accompanying_materials_other_than_librettos': 'm',
        'language_code_of_original_libretto': 'n',
        'source_of_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(
            value.get('source_of_code'),
            '7') != '7' and '2' in order:
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(value.get('language_code_of_text_sound_track_or_separate_title')),
        'b': utils.reverse_force_list(value.get('language_code_of_summary_or_abstract')),
        'd': utils.reverse_force_list(value.get('language_code_of_sung_or_spoken_text')),
        'e': utils.reverse_force_list(value.get('language_code_of_librettos')),
        'f': utils.reverse_force_list(value.get('language_code_of_table_of_contents')),
        'g': utils.reverse_force_list(value.get('language_code_of_accompanying_material_other_than_librettos')),
        'h': utils.reverse_force_list(value.get('language_code_of_original')),
        'j': utils.reverse_force_list(value.get('language_code_of_subtitles_or_captions')),
        'k': utils.reverse_force_list(value.get('language_code_of_intermediate_translations')),
        'm': utils.reverse_force_list(value.get('language_code_of_original_accompanying_materials_other_than_librettos')),
        'n': utils.reverse_force_list(value.get('language_code_of_original_libretto')),
        '2': value.get('source_of_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('translation_indication'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_code'), '7'),
    }


@to_marc21.over('042', '^authentication_code$')
@utils.filter_values
def reverse_authentication_code(self, key, value):
    """Reverse - Authentication Code."""
    return {
        'a': utils.reverse_force_list(value.get('authentication_code')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('043', '^geographic_area_code$')
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

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(value.get('geographic_area_code')),
        'b': utils.reverse_force_list(value.get('local_gac_code')),
        'c': utils.reverse_force_list(value.get('iso_code')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '2': utils.reverse_force_list(value.get('source_of_local_code')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('044', '^country_of_publishing_producing_entity_code$')
@utils.filter_values
def reverse_country_of_publishing_producing_entity_code(self, key, value):
    """Reverse - Country of Publishing/Producing Entity Code."""
    field_map = {
        'marc_country_code': 'a',
        'local_subentity_code': 'b',
        'iso_country_code': 'c',
        'source_of_local_subentity_code': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('marc_country_code')),
        'b': utils.reverse_force_list(
            value.get('local_subentity_code')),
        'c': utils.reverse_force_list(
            value.get('iso_country_code')),
        '2': utils.reverse_force_list(
            value.get('source_of_local_subentity_code')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('045', '^time_period_of_content$')
@utils.filter_values
def reverse_time_period_of_content(self, key, value):
    """Reverse - Time Period of Content."""
    indicator_map1 = {
        'Multiple single dates/times': '1',
        'Range of dates/times': '2',
        'Single date/time': '0',
        'Subfield $b or $c not present': '_',
    }

    field_map = {
        'time_period_code': 'a',
        'formatted_9999_bc_through_ce_time_period': 'b',
        'formatted_pre_9999_bc_time_period': 'c',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_code')),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_time_period_in_subfield_b_or_c'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""
    field_map = {
        'type_of_date_code': 'a',
        'date_1_bc_date': 'b',
        'date_1_ce_date': 'c',
        'date_2_bc_date': 'd',
        'date_2_ce_date': 'e',
        'date_resource_modified': 'j',
        'beginning_or_single_date_created': 'k',
        'ending_date_created': 'l',
        'beginning_of_date_valid': 'm',
        'end_of_date_valid': 'n',
        'single_or_starting_date_for_aggregated_content': 'o',
        'ending_date_for_aggregated_content': 'p',
        'source_of_date': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('type_of_date_code'),
        'b': value.get('date_1_bc_date'),
        'c': value.get('date_1_ce_date'),
        'd': value.get('date_2_bc_date'),
        'e': value.get('date_2_ce_date'),
        'j': value.get('date_resource_modified'),
        'k': value.get('beginning_or_single_date_created'),
        'l': value.get('ending_date_created'),
        'm': value.get('beginning_of_date_valid'),
        'n': value.get('end_of_date_valid'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'p': value.get('ending_date_for_aggregated_content'),
        '2': value.get('source_of_date'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('047', '^form_of_musical_composition_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_musical_composition_code(self, key, value):
    """Reverse - Form of Musical Composition Code."""
    indicator_map2 = {
        'MARC musical composition code': '_',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'form_of_musical_composition_code': 'a',
        'source_of_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7':
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('form_of_musical_composition_code')),
        '2': value.get('source_of_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(
            value.get('source_of_code'),
            '7'),
    }


@to_marc21.over('048', '^number_of_musical_instruments_or_voices_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_number_of_musical_instruments_or_voices_code(self, key, value):
    """Reverse - Number of Musical Instruments or Voices Code."""
    indicator_map2 = {
        'MARC musical composition code': '_',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'performer_or_ensemble': 'a',
        'soloist': 'b',
        'source_of_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(
            value.get('source_of_code'),
            '7') != '7' and '2' in order:
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('performer_or_ensemble')),
        'b': utils.reverse_force_list(
            value.get('soloist')),
        '2': value.get('source_of_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(
            value.get('source_of_code'),
            '7'),
    }


@to_marc21.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map1 = {
        'No information provided': '_',
        'Item is in LC': '0',
        'Item is not in LC': '1',
    }

    indicator_map2 = {
        'Assigned by LC': '0',
        'Assigned by agency other than LC': '4',
    }

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('existence_in_lc_collection'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('source_of_call_number'),
            '_'),
    }


@to_marc21.over('051', '^library_of_congress_copy_issue_offprint_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_copy_issue_offprint_statement(
        self,
        key,
        value):
    """Reverse - Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {
        'Library of Congress Classification': '_',
        'U.S. Dept. of Defense Classification': '1',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'geographic_classification_area_code': 'a',
        'geographic_classification_subarea_code': 'b',
        'populated_place_name': 'd',
        'code_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('code_source'), '7') != '7':
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_classification_area_code'),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')),
        '2': value.get('code_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('code_source'),
            '7'),
        '$ind2': '_',
    }


@to_marc21.over('055', '^classification_numbers_assigned_in_canada$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_classification_numbers_assigned_in_canada(self, key, value):
    """Reverse - Classification Numbers Assigned in Canada."""
    indicator_map1 = {
        'Information not provided': '_',
        'Work held by LAC': '0',
        'Work not held by LAC': '1',
    }

    indicator_map2 = {
        'Complete LC class number assigned by LAC': '1',
        'Complete LC class number assigned by the contributing library': '4',
        'Incomplete LC class number assigned by LAC': '2',
        'Incomplete LC class number assigned by the contributing library': '5',
        'LC-based call number assigned by LAC': '0',
        'LC-based call number assigned by the contributing library': '3',
        'Other call number assigned by LAC': '6',
        'Other call number assigned by the contributing library': '8',
        'Other class number assigned by LAC': '7',
        'Other class number assigned by the contributing library': '9',
    }

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'source_of_call_class_number': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'b': value.get('item_number'),
        '2': value.get('source_of_call_class_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('existence_in_lac_collection'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('type_completeness_source_of_class_call_number'),
            '_'),
    }


@to_marc21.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map1 = {
        'No information provided': '_',
        'Item is in NLM': '0',
        'Item is not in NLM': '1',
    }

    indicator_map2 = {
        'Assigned by NLM': '0',
        'Assigned by agency other than NLM': '4',
    }

    field_map = {
        'classification_number_r': 'a',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number_r')),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('existence_in_nlm_collection'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('source_of_call_number'),
            '_'),
    }


@to_marc21.over('061', '^national_library_of_medicine_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_copy_statement(self, key, value):
    """Reverse - National Library of Medicine Copy Statement."""
    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""
    field_map = {
        'primary_g0_character_set': 'a',
        'primary_g1_character_set': 'b',
        'alternate_g0_or_g1_character_set': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('primary_g0_character_set'),
        'b': value.get('primary_g1_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""
    indicator_map1 = {
        'Item is in NAL': '0',
        'Item is not in NAL': '1',
    }

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'field_link_and_sequence_number_r': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')),
        '$ind1': indicator_map1.get(
            value.get('existence_in_nal_collection'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('071', '^national_agricultural_library_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_copy_statement(self, key, value):
    """Reverse - National Agricultural Library Copy Statement."""
    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        'c': utils.reverse_force_list(
            value.get('copy_information')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {
        'NAL subject category code list ': '0',
        'Source specified in subfield $2': '7',
    }

    field_map = {
        'subject_category_code': 'a',
        'subject_category_code_subdivision': 'x',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(
            value.get('code_source'),
            '7') != '7' and '2' in order:
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('subject_category_code'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(
            value.get('code_source'),
            '_'),
    }


@to_marc21.over('074', '^gpo_item_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_gpo_item_number(self, key, value):
    """Reverse - GPO Item Number."""
    field_map = {
        'gpo_item_number': 'a',
        'canceled_invalid_gpo_item_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('gpo_item_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_gpo_item_number')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {
        'No information provided': '_',
        'Full': '0',
        'Abridged': '1',
    }

    field_map = {
        'universal_decimal_classification_number': 'a',
        'item_number': 'b',
        'common_auxiliary_subdivision': 'x',
        'edition_identifier': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('universal_decimal_classification_number'),
        'b': value.get('item_number'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')),
        '2': value.get('edition_identifier'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_edition'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('082', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {
        'Full edition': '0',
        'Abridged edition': '1',
        'Other edition specified in subfield $2': '7',
    }

    indicator_map2 = {
        'No information provided': '_',
        'Assigned by LC': '0',
        'Assigned by agency other than LC': '4',
    }

    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'standard_or_optional_designation': 'm',
        'assigning_agency': 'q',
        'edition_number': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        'm': value.get('standard_or_optional_designation'),
        'q': value.get('assigning_agency'),
        '2': value.get('edition_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_edition'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('source_of_classification_number'),
            '_'),
    }


@to_marc21.over('083', '^additional_dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_dewey_decimal_classification_number(self, key, value):
    """Reverse - Additional Dewey Decimal Classification Number."""
    indicator_map1 = {
        'Full edition': '0',
        'Abridged edition': '1',
        'Other edition specified in subfield $2': '7',
    }

    field_map = {
        'classification_number': 'a',
        'classification_number__ending_number_of_span': 'c',
        'standard_or_optional_designation': 'm',
        'assigning_agency': 'q',
        'table_sequence_number_for_internal': 'y',
        'table_identification': 'z',
        'edition_number': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')),
        'm': value.get('standard_or_optional_designation'),
        'q': value.get('assigning_agency'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')),
        'z': utils.reverse_force_list(
            value.get('table_identification')),
        '2': value.get('edition_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('type_of_edition'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('084', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""
    field_map = {
        'classification_number': 'a',
        'item_number': 'b',
        'assigning_agency': 'q',
        'number_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')),
        'b': value.get('item_number'),
        'q': value.get('assigning_agency'),
        '2': value.get('number_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('085', '^synthesized_classification_number_components$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_synthesized_classification_number_components(self, key, value):
    """Reverse - Synthesized Classification Number Components."""
    field_map = {
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': 'a',
        'base_number': 'b',
        'classification_number_ending_number_of_span': 'c',
        'facet_designator': 'f',
        'root_number': 'r',
        'digits_added_from_classification_number_in_schedule_or_external_table': 's',
        'digits_added_from_internal_subarrangement_or_add_table': 't',
        'number_being_analyzed': 'u',
        'number_in_internal_subarrangement_or_add_table_where': 'v',
        'table_identification_internal_subarrangement_or_add': 'w',
        'table_sequence_number_for_internal_subarrangement_or': 'y',
        'table_identification': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(value.get('number_where_instructions_are_found_single_number_or_beginning_number_of_span')),
        'b': utils.reverse_force_list(value.get('base_number')),
        'c': utils.reverse_force_list(value.get('classification_number_ending_number_of_span')),
        'f': utils.reverse_force_list(value.get('facet_designator')),
        'r': utils.reverse_force_list(value.get('root_number')),
        's': utils.reverse_force_list(value.get('digits_added_from_classification_number_in_schedule_or_external_table')),
        't': utils.reverse_force_list(value.get('digits_added_from_internal_subarrangement_or_add_table')),
        'u': utils.reverse_force_list(value.get('number_being_analyzed')),
        'v': utils.reverse_force_list(value.get('number_in_internal_subarrangement_or_add_table_where_instructions_are_found')),
        'w': utils.reverse_force_list(value.get('table_identification_internal_subarrangement_or_add_table')),
        'y': utils.reverse_force_list(value.get('table_sequence_number_for_internal_subarrangement_or_add_table')),
        'z': utils.reverse_force_list(value.get('table_identification')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('086', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    indicator_map1 = {
        'Source specified in subfield $2': '_',
        'Superintendent of Documents Classification System': '0',
        'Government of Canada Publications: Outline of Classification': '1',
    }

    field_map = {
        'classification_number': 'a',
        'canceled_invalid_classification_number': 'z',
        'number_source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('number_source'),
            '_') != '_' and '2' in order:
        order.remove('2')

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_classification_number')),
        '2': value.get('number_source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('number_source'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('088', '^report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_report_number(self, key, value):
    """Reverse - Report Number."""
    field_map = {
        'report_number': 'a',
        'canceled_invalid_report_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('report_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_report_number')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }
