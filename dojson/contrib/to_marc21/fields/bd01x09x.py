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
        'canceled_invalid_lc_control_number': 'z',
        'field_link_and_sequence_number': '8',
        'nucmc_control_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('lc_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('nucmc_control_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('013', '^patent_control_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_patent_control_information(self, key, value):
    """Reverse - Patent Control Information."""
    field_map = {
        'linkage': '6',
        'type_of_number': 'c',
        'number': 'a',
        'field_link_and_sequence_number': '8',
        'country': 'b',
        'date': 'd',
        'party_to_document': 'f',
        'status': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('type_of_number'),
        'a': value.get('number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('country'),
        'd': utils.reverse_force_list(
            value.get('date')
        ),
        'f': utils.reverse_force_list(
            value.get('party_to_document')
        ),
        'e': utils.reverse_force_list(
            value.get('status')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('015', '^national_bibliography_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliography_number(self, key, value):
    """Reverse - National Bibliography Number."""
    field_map = {
        'linkage': '6',
        'national_bibliography_number': 'a',
        'canceled_invalid_national_bibliography_number': 'z',
        'field_link_and_sequence_number': '8',
        'source': '2',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('national_bibliography_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_national_bibliography_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    indicator_map1 = {"Library and Archives Canada": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source': '2',
        'record_control_number': 'a',
        'canceled_invalid_control_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        'a': value.get('record_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'national_bibliographic_agency' in value and
        not indicator_map1.get(value.get('national_bibliographic_agency')) and
        value.get('national_bibliographic_agency') == value.get('source')
        else indicator_map1.get(value.get('national_bibliographic_agency'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('017', '^copyright_or_legal_deposit_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copyright_or_legal_deposit_number(self, key, value):
    """Reverse - Copyright or Legal Deposit Number."""
    indicator_map2 = {"Copyright or legal deposit number": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'canceled_invalid_copyright_or_legal_deposit_number': 'z',
        'copyright_or_legal_deposit_number': 'a',
        'display_text': 'i',
        'field_link_and_sequence_number': '8',
        'assigning_agency': 'b',
        'source': '2',
        'date': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_copyright_or_legal_deposit_number')
        ),
        'a': utils.reverse_force_list(
            value.get('copyright_or_legal_deposit_number')
        ),
        'i': value.get('display_text'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('assigning_agency'),
        '2': value.get('source'),
        'd': value.get('date'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('018', '^copyright_article_fee_code$')
@utils.filter_values
def reverse_copyright_article_fee_code(self, key, value):
    """Reverse - Copyright Article-Fee Code."""
    field_map = {
        'linkage': '6',
        'copyright_article_fee_code_nr': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('copyright_article_fee_code_nr')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('020', '^international_standard_book_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_book_number(self, key, value):
    """Reverse - International Standard Book Number."""
    field_map = {
        'linkage': '6',
        'terms_of_availability': 'c',
        'international_standard_book_number': 'a',
        'canceled_invalid_isbn': 'z',
        'field_link_and_sequence_number': '8',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('terms_of_availability'),
        'a': value.get('international_standard_book_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    indicator_map1 = {"Continuing resource not of international interest": "1", "Continuing resource of international interest": "0", "No level specified": "_"}
    field_map = {
        'linkage': '6',
        'canceled_issn': 'z',
        'international_standard_serial_number': 'a',
        'field_link_and_sequence_number': '8',
        'issn_l': 'l',
        'canceled_issn_l': 'm',
        'source': '2',
        'incorrect_issn': 'y',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        'a': value.get('international_standard_serial_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('issn_l'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        '2': value.get('source'),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_international_interest'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {"International Article Number": "3", "International Standard Music Number": "2", "International Standard Recording Code": "0", "Serial Item and Contribution Identifier": "4", "Source specified in subfield $2": "7", "Universal Product Code": "1", "Unspecified type of standard number or code": "8"}
    indicator_map2 = {"Difference": "1", "No difference": "0", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'terms_of_availability': 'c',
        'standard_number_or_code': 'a',
        'canceled_invalid_standard_number_or_code': 'z',
        'field_link_and_sequence_number': '8',
        'source_of_number_or_code': '2',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('terms_of_availability'),
        'a': value.get('standard_number_or_code'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_number_or_code'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '7' if 'type_of_standard_number_or_code' in value and
        not indicator_map1.get(value.get('type_of_standard_number_or_code')) and
        value.get('type_of_standard_number_or_code') == value.get('source_of_number_or_code')
        else indicator_map1.get(value.get('type_of_standard_number_or_code'), '_'),
        '$ind2': indicator_map2.get(value.get('difference_indicator'), '_'),
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
            value.get('overseas_acquisition_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('026', '^fingerprint_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_fingerprint_identifier(self, key, value):
    """Reverse - Fingerprint Identifier."""
    field_map = {
        'linkage': '6',
        'date': 'c',
        'first_and_second_groups_of_characters': 'a',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'third_and_fourth_groups_of_characters': 'b',
        'source': '2',
        'number_of_volume_or_part': 'd',
        'unparsed_fingerprint': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('date'),
        'a': value.get('first_and_second_groups_of_characters'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('third_and_fourth_groups_of_characters'),
        '2': value.get('source'),
        'd': utils.reverse_force_list(
            value.get('number_of_volume_or_part')
        ),
        'e': value.get('unparsed_fingerprint'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('027', '^standard_technical_report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_standard_technical_report_number(self, key, value):
    """Reverse - Standard Technical Report Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_number': 'z',
        'standard_technical_report_number': 'a',
        'qualifying_information': 'q',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_number')
        ),
        'a': value.get('standard_technical_report_number'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('028', '^publisher_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publisher_number(self, key, value):
    """Reverse - Publisher Number."""
    indicator_map1 = {"Issue number": "0", "Matrix number": "1", "Other music number": "3", "Other publisher number": "5", "Plate number": "2", "Videorecording number": "4"}
    indicator_map2 = {"No note, added entry": "3", "No note, no added entry": "0", "Note, added entry": "1", "Note, no added entry": "2"}
    field_map = {
        'linkage': '6',
        'publisher_number': 'a',
        'qualifying_information': 'q',
        'field_link_and_sequence_number': '8',
        'source': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('publisher_number'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source'),
        '$ind1': indicator_map1.get(value.get('type_of_publisher_number'), '_'),
        '$ind2': indicator_map2.get(value.get('note_added_entry_controller'), '_'),
    }


@to_marc21.over('030', '^coden_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coden_designation(self, key, value):
    """Reverse - CODEN Designation."""
    field_map = {
        'linkage': '6',
        'coden': 'a',
        'canceled_invalid_coden': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('coden'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_coden')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""
    field_map = {
        'linkage': '6',
        'clef': 'g',
        'musical_notation': 'p',
        'field_link_and_sequence_number': '8',
        'voice_instrument': 'm',
        'number_of_movement': 'b',
        'key_signature': 'n',
        'system_code': '2',
        'link_text': 'y',
        'number_of_excerpt': 'c',
        'coded_validity_note': 's',
        'key_or_mode': 'r',
        'number_of_work': 'a',
        'time_signature': 'o',
        'general_note': 'q',
        'public_note': 'z',
        'uniform_resource_identifier': 'u',
        'text_incipit': 't',
        'caption_or_heading': 'd',
        'role': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'g': value.get('clef'),
        'p': value.get('musical_notation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('voice_instrument'),
        'b': value.get('number_of_movement'),
        'n': value.get('key_signature'),
        '2': value.get('system_code'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'c': value.get('number_of_excerpt'),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        'r': value.get('key_or_mode'),
        'a': value.get('number_of_work'),
        'o': value.get('time_signature'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        'e': value.get('role'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('032', '^postal_registration_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_postal_registration_number(self, key, value):
    """Reverse - Postal Registration Number."""
    field_map = {
        'linkage': '6',
        'postal_registration_number': 'a',
        'field_link_and_sequence_number': '8',
        'source_agency_assigning_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('postal_registration_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_agency_assigning_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('033', '^date_time_and_place_of_an_event$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event(self, key, value):
    """Reverse - Date/Time and Place of an Event."""
    indicator_map1 = {"Multiple single dates": "1", "No date information": "_", "Range of dates": "2", "Single date": "0"}
    indicator_map2 = {"Broadcast": "1", "Capture": "0", "Finding": "2", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'geographic_classification_subarea_code': 'c',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'geographic_classification_area_code': 'b',
        'source_of_term': '2',
        'formatted_date_time': 'a',
        'authority_record_control_number': '0',
        'place_of_event': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_area_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        'a': utils.reverse_force_list(
            value.get('formatted_date_time')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_date_in_subfield_a'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_event'), '_'),
    }


@to_marc21.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map1 = {"Range of scales": "3", "Scale indeterminable/No scale recorded": "0", "Single scale": "1"}
    indicator_map2 = {"Exclusion ring": "1", "Not applicable": "_", "Outer ring": "0"}
    field_map = {
        'constant_ratio_linear_vertical_scale': 'c',
        'materials_specified': '3',
        'declination_northern_limit': 'j',
        'angular_scale': 'h',
        'right_ascension_western_limit': 'n',
        'source': '2',
        'coordinates_southernmost_latitude': 'g',
        'distance_from_earth': 'r',
        'declination_southern_limit': 'k',
        'name_of_extraterrestrial_body': 'z',
        'coordinates_northernmost_latitude': 'f',
        'coordinates_easternmost_longitude': 'e',
        'linkage': '6',
        'equinox': 'p',
        'g_ring_latitude': 's',
        'field_link_and_sequence_number': '8',
        'constant_ratio_linear_horizontal_scale': 'b',
        'ending_date': 'y',
        'authority_record_control_number_or_standard_number': '0',
        'right_ascension_eastern_limit': 'm',
        'category_of_scale': 'a',
        'beginning_date': 'x',
        'g_ring_longitude': 't',
        'coordinates_westernmost_longitude': 'd',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('constant_ratio_linear_vertical_scale')
        ),
        '3': value.get('materials_specified'),
        'j': value.get('declination_northern_limit'),
        'h': utils.reverse_force_list(
            value.get('angular_scale')
        ),
        'n': value.get('right_ascension_western_limit'),
        '2': value.get('source'),
        'g': value.get('coordinates_southernmost_latitude'),
        'r': value.get('distance_from_earth'),
        'k': value.get('declination_southern_limit'),
        'z': value.get('name_of_extraterrestrial_body'),
        'f': value.get('coordinates_northernmost_latitude'),
        'e': value.get('coordinates_easternmost_longitude'),
        '6': value.get('linkage'),
        'p': value.get('equinox'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('constant_ratio_linear_horizontal_scale')
        ),
        'y': value.get('ending_date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': value.get('right_ascension_eastern_limit'),
        'a': value.get('category_of_scale'),
        'x': value.get('beginning_date'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        'd': value.get('coordinates_westernmost_longitude'),
        '$ind1': indicator_map1.get(value.get('type_of_scale'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_ring'), '_'),
    }


@to_marc21.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    field_map = {
        'linkage': '6',
        'system_control_number': 'a',
        'canceled_invalid_control_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('system_control_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('036', '^original_study_number_for_computer_data_files$')
@utils.filter_values
def reverse_original_study_number_for_computer_data_files(self, key, value):
    """Reverse - Original Study Number for Computer Data Files."""
    field_map = {
        'linkage': '6',
        'original_study_number': 'a',
        'field_link_and_sequence_number': '8',
        'source_agency_assigning_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('original_study_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_agency_assigning_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('037', '^source_of_acquisition$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_acquisition(self, key, value):
    """Reverse - Source of Acquisition."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2", "Not applicable/No information provided/Earliest": "_"}
    field_map = {
        'additional_format_characteristics': 'g',
        'linkage': '6',
        'terms_of_availability': 'c',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'source_of_stock_number_acquisition': 'b',
        'note': 'n',
        'stock_number': 'a',
        'form_of_issue': 'f',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('additional_format_characteristics')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('terms_of_availability')
        ),
        '3': value.get('materials_specified'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_of_stock_number_acquisition'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'a': value.get('stock_number'),
        'f': utils.reverse_force_list(
            value.get('form_of_issue')
        ),
        '$ind1': indicator_map1.get(value.get('source_of_acquisition_sequence'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('038', '^record_content_licensor$')
@utils.filter_values
def reverse_record_content_licensor(self, key, value):
    """Reverse - Record Content Licensor."""
    field_map = {
        'linkage': '6',
        'record_content_licensor': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('record_content_licensor'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    field_map = {
        'linkage': '6',
        'transcribing_agency': 'c',
        'original_cataloging_agency': 'a',
        'field_link_and_sequence_number': '8',
        'language_of_cataloging': 'b',
        'modifying_agency': 'd',
        'description_conventions': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('transcribing_agency'),
        'a': value.get('original_cataloging_agency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('language_of_cataloging'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('041', '^language_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_code(self, key, value):
    """Reverse - Language Code."""
    indicator_map1 = {"Item is or includes a translation": "1", "Item not a translation/does not include a translation": "0", "No information provided": "_"}
    indicator_map2 = {"MARC language code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'language_code_of_accompanying_material_other_than_librettos': 'g',
        'language_code_of_intermediate_translations': 'k',
        'language_code_of_subtitles_or_captions': 'j',
        'language_code_of_original': 'h',
        'language_code_of_summary_or_abstract': 'b',
        'language_code_of_sung_or_spoken_text': 'd',
        'language_code_of_original_libretto': 'n',
        'source_of_code': '2',
        'language_code_of_table_of_contents': 'f',
        'language_code_of_original_accompanying_materials_other_than_librettos': 'm',
        'language_code_of_text_sound_track_or_separate_title': 'a',
        'field_link_and_sequence_number': '8',
        'language_code_of_librettos': 'e',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7' and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('language_code_of_accompanying_material_other_than_librettos')
        ),
        'k': utils.reverse_force_list(
            value.get('language_code_of_intermediate_translations')
        ),
        'j': utils.reverse_force_list(
            value.get('language_code_of_subtitles_or_captions')
        ),
        'h': utils.reverse_force_list(
            value.get('language_code_of_original')
        ),
        'b': utils.reverse_force_list(
            value.get('language_code_of_summary_or_abstract')
        ),
        'd': utils.reverse_force_list(
            value.get('language_code_of_sung_or_spoken_text')
        ),
        'n': utils.reverse_force_list(
            value.get('language_code_of_original_libretto')
        ),
        '2': value.get('source_of_code'),
        'f': utils.reverse_force_list(
            value.get('language_code_of_table_of_contents')
        ),
        'm': utils.reverse_force_list(
            value.get('language_code_of_original_accompanying_materials_other_than_librettos')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code_of_text_sound_track_or_separate_title')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('language_code_of_librettos')
        ),
        '$ind1': indicator_map1.get(value.get('translation_indication'), '_'),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code')
        else indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21.over('042', '^authentication_code$')
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


@to_marc21.over('043', '^geographic_area_code$')
@utils.filter_values
def reverse_geographic_area_code(self, key, value):
    """Reverse - Geographic Area Code."""
    field_map = {
        'linkage': '6',
        'iso_code': 'c',
        'geographic_area_code': 'a',
        'field_link_and_sequence_number': '8',
        'local_gac_code': 'b',
        'source_of_local_code': '2',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('044', '^country_of_publishing_producing_entity_code$')
@utils.filter_values
def reverse_country_of_publishing_producing_entity_code(self, key, value):
    """Reverse - Country of Publishing/Producing Entity Code."""
    field_map = {
        'linkage': '6',
        'iso_country_code': 'c',
        'marc_country_code': 'a',
        'field_link_and_sequence_number': '8',
        'local_subentity_code': 'b',
        'source_of_local_subentity_code': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('iso_country_code')
        ),
        'a': utils.reverse_force_list(
            value.get('marc_country_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('local_subentity_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_subentity_code')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('045', '^time_period_of_content$')
@utils.filter_values
def reverse_time_period_of_content(self, key, value):
    """Reverse - Time Period of Content."""
    indicator_map1 = {"Multiple single dates/times": "1", "Range of dates/times": "2", "Single date/time": "0", "Subfield $b or $c not present": "_"}
    field_map = {
        'linkage': '6',
        'formatted_pre_9999_bc_time_period': 'c',
        'time_period_code': 'a',
        'field_link_and_sequence_number': '8',
        'formatted_9999_bc_through_ce_time_period': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_code')
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


@to_marc21.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""
    field_map = {
        'linkage': '6',
        'date_1_ce_date': 'c',
        'beginning_or_single_date_created': 'k',
        'date_resource_modified': 'j',
        'field_link_and_sequence_number': '8',
        'date_1_bc_date': 'b',
        'end_of_date_valid': 'n',
        'source_of_date': '2',
        'ending_date_for_aggregated_content': 'p',
        'beginning_of_date_valid': 'm',
        'type_of_date_code': 'a',
        'single_or_starting_date_for_aggregated_content': 'o',
        'ending_date_created': 'l',
        'date_2_bc_date': 'd',
        'date_2_ce_date': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': value.get('date_1_ce_date'),
        'k': value.get('beginning_or_single_date_created'),
        'j': value.get('date_resource_modified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('date_1_bc_date'),
        'n': value.get('end_of_date_valid'),
        '2': value.get('source_of_date'),
        'p': value.get('ending_date_for_aggregated_content'),
        'm': value.get('beginning_of_date_valid'),
        'a': value.get('type_of_date_code'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'l': value.get('ending_date_created'),
        'd': value.get('date_2_bc_date'),
        'e': value.get('date_2_ce_date'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('047', '^form_of_musical_composition_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_musical_composition_code(self, key, value):
    """Reverse - Form of Musical Composition Code."""
    indicator_map2 = {"MARC musical composition code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source_of_code': '2',
        'form_of_musical_composition_code': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7' and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_code'),
        'a': utils.reverse_force_list(
            value.get('form_of_musical_composition_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code')
        else indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21.over('048', '^number_of_musical_instruments_or_voices_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_number_of_musical_instruments_or_voices_code(self, key, value):
    """Reverse - Number of Musical Instruments or Voices Code."""
    indicator_map2 = {"MARC code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source_of_code': '2',
        'performer_or_ensemble': 'a',
        'field_link_and_sequence_number': '8',
        'soloist': 'b',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7' and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_code'),
        'a': utils.reverse_force_list(
            value.get('performer_or_ensemble')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code')
        else indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map1 = {"Item is in LC": "0", "Item is not in LC": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'linkage': '6',
        'materials_specified': '3',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_lc_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21.over('051', '^library_of_congress_copy_issue_offprint_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Reverse - Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        'copy_information': 'c',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('copy_information'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {"Library of Congress Classification": "_", "Source specified in subfield $2": "7", "U.S. Dept. of Defense Classification": "1"}
    field_map = {
        'linkage': '6',
        'geographic_classification_area_code': 'a',
        'field_link_and_sequence_number': '8',
        'geographic_classification_subarea_code': 'b',
        'code_source': '2',
        'populated_place_name': 'd',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('code_source'), '7') != '7' and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('geographic_classification_area_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '2': value.get('code_source'),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        '$ind1': '7' if 'code_source' in value and
        not indicator_map1.get(value.get('code_source')) and
        value.get('code_source') == value.get('code_source')
        else indicator_map1.get(value.get('code_source'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('055', '^classification_numbers_assigned_in_canada$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_classification_numbers_assigned_in_canada(self, key, value):
    """Reverse - Classification Numbers Assigned in Canada."""
    indicator_map1 = {"Information not provided": "_", "Work held by LAC": "0", "Work not held by LAC": "1"}
    indicator_map2 = {"Complete LC class number assigned by LAC": "1", "Complete LC class number assigned by the contributing library": "4", "Incomplete LC class number assigned by LAC": "2", "Incomplete LC class number assigned by the contributing library": "5", "LC-based call number assigned by LAC": "0", "LC-based call number assigned by the contributing library": "3", "Other call number assigned by LAC": "6", "Other call number assigned by the contributing library": "8", "Other class number assigned by LAC": "7", "Other class number assigned by the contributing library": "9"}
    field_map = {
        'linkage': '6',
        'source_of_call_class_number': '2',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source_of_call_class_number'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_lac_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('type_completeness_source_of_class_call_number'), '_'),
    }


@to_marc21.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map1 = {"Item is in NLM": "0", "Item is not in NLM": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by NLM": "0", "Assigned by agency other than NLM": "4"}
    field_map = {
        'classification_number_r': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number_r')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_nlm_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21.over('061', '^national_library_of_medicine_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_copy_statement(self, key, value):
    """Reverse - National Library of Medicine Copy Statement."""
    field_map = {
        'copy_information': 'c',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('copy_information'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""
    field_map = {
        'alternate_g0_or_g1_character_set': 'c',
        'primary_g0_character_set': 'a',
        'primary_g1_character_set': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
        'a': value.get('primary_g0_character_set'),
        'b': value.get('primary_g1_character_set'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""
    indicator_map1 = {"Item is in NAL": "0", "Item is not in NAL": "1"}
    field_map = {
        'classification_number': 'a',
        'field_link_and_sequence_number_r': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')
        ),
        'b': value.get('item_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_nal_collection'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('071', '^national_agricultural_library_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_copy_statement(self, key, value):
    """Reverse - National Agricultural Library Copy Statement."""
    field_map = {
        'copy_information': 'c',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('copy_information')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {"NAL subject category code list": "0", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'source': '2',
        'subject_category_code': 'a',
        'subject_category_code_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source'),
        'a': value.get('subject_category_code'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '7' if 'code_source' in value and
        not indicator_map2.get(value.get('code_source')) and
        value.get('code_source') == value.get('source')
        else indicator_map2.get(value.get('code_source'), '_'),
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
            value.get('canceled_invalid_gpo_item_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'universal_decimal_classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'edition_identifier': '2',
        'common_auxiliary_subdivision': 'x',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('universal_decimal_classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '2': value.get('edition_identifier'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('082', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'edition_number': '2',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '2': value.get('edition_number'),
        'q': value.get('assigning_agency'),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number')
        else indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_classification_number'), '_'),
    }


@to_marc21.over('083', '^additional_dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_dewey_decimal_classification_number(self, key, value):
    """Reverse - Additional Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'classification_number_ending_number_of_span': 'c',
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'field_link_and_sequence_number': '8',
        'table_identification': 'z',
        'edition_number': '2',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        '2': value.get('edition_number'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'q': value.get('assigning_agency'),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number')
        else indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('084', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""
    field_map = {
        'linkage': '6',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'number_source': '2',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        '2': value.get('number_source'),
        'q': value.get('assigning_agency'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('085', '^synthesized_classification_number_components$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_synthesized_classification_number_components(self, key, value):
    """Reverse - Synthesized Classification Number Components."""
    field_map = {
        'linkage': '6',
        'classification_number_ending_number_of_span': 'c',
        'field_link_and_sequence_number': '8',
        'digits_added_from_classification_number_in_schedule_or_external_table': 's',
        'base_number': 'b',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': 'v',
        'table_identification_internal_subarrangement_or_add_table': 'w',
        'root_number': 'r',
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': 'a',
        'table_identification': 'z',
        'number_being_analyzed': 'u',
        'digits_added_from_internal_subarrangement_or_add_table': 't',
        'facet_designator': 'f',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': utils.reverse_force_list(
            value.get('digits_added_from_classification_number_in_schedule_or_external_table')
        ),
        'b': utils.reverse_force_list(
            value.get('base_number')
        ),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'v': utils.reverse_force_list(
            value.get('number_in_internal_subarrangement_or_add_table_where_instructions_are_found')
        ),
        'w': utils.reverse_force_list(
            value.get('table_identification_internal_subarrangement_or_add_table')
        ),
        'r': utils.reverse_force_list(
            value.get('root_number')
        ),
        'a': utils.reverse_force_list(
            value.get('number_where_instructions_are_found_single_number_or_beginning_number_of_span')
        ),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        'u': utils.reverse_force_list(
            value.get('number_being_analyzed')
        ),
        't': utils.reverse_force_list(
            value.get('digits_added_from_internal_subarrangement_or_add_table')
        ),
        'f': utils.reverse_force_list(
            value.get('facet_designator')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('086', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    indicator_map1 = {"Government of Canada Publications: Outline of Classification": "1", "Source specified in subfield $2": "_", "Superintendent of Documents Classification System": "0"}
    field_map = {
        'linkage': '6',
        'number_source': '2',
        'classification_number': 'a',
        'canceled_invalid_classification_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('number_source'), '7') != '7' and\
            field_map.get('number_source'):
        order.remove(field_map.get('number_source'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('number_source'),
        'a': value.get('classification_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_' if 'number_source' in value and
        not indicator_map1.get(value.get('number_source')) and
        value.get('number_source') == value.get('number_source')
        else indicator_map1.get(value.get('number_source'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('088', '^report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_report_number(self, key, value):
    """Reverse - Report Number."""
    field_map = {
        'linkage': '6',
        'report_number': 'a',
        'canceled_invalid_report_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('report_number'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_report_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
