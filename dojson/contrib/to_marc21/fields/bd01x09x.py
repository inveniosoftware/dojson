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
        'nucmc_control_number': 'b',
        'lc_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'canceled_invalid_lc_control_number': 'z',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('nucmc_control_number')
        ),
        'a': value.get('lc_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
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
        'party_to_document': 'f',
        'number': 'a',
        'date': 'd',
        'country': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'status': 'e',
        'type_of_number': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'f': utils.reverse_force_list(
            value.get('party_to_document')
        ),
        'a': value.get('number'),
        'd': utils.reverse_force_list(
            value.get('date')
        ),
        'b': value.get('country'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('status')
        ),
        'c': value.get('type_of_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('015', '^national_bibliography_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliography_number(self, key, value):
    """Reverse - National Bibliography Number."""
    field_map = {
        'canceled_invalid_national_bibliography_number': 'z',
        'national_bibliography_number': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'qualifying_information': 'q',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_national_bibliography_number')
        ),
        'a': utils.reverse_force_list(
            value.get('national_bibliography_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    indicator_map1 = {
        "Library and Archives Canada": "_",
        "Source specified in subfield $2": "7"}
    field_map = {
        'canceled_invalid_control_number': 'z',
        'record_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('national_bibliographic_agency'), '7') != '7':
        try:
            order.remove(field_map.get('national_bibliographic_agency'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        'a': value.get('record_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
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
    indicator_map2 = {
        "Copyright or legal deposit number": "_",
        "No display constant generated": "8"}
    field_map = {
        'canceled_invalid_copyright_or_legal_deposit_number': 'z',
        'copyright_or_legal_deposit_number': 'a',
        'date': 'd',
        'assigning_agency': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'display_text': 'i',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_copyright_or_legal_deposit_number')
        ),
        'a': utils.reverse_force_list(
            value.get('copyright_or_legal_deposit_number')
        ),
        'd': value.get('date'),
        'b': value.get('assigning_agency'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': value.get('display_text'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), '_'),
    }


@to_marc21.over('018', '^copyright_article_fee_code$')
@utils.filter_values
def reverse_copyright_article_fee_code(self, key, value):
    """Reverse - Copyright Article-Fee Code."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'copyright_article_fee_code_nr': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('copyright_article_fee_code_nr')
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
        'canceled_invalid_isbn': 'z',
        'international_standard_book_number': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'qualifying_information': 'q',
        'terms_of_availability': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        'a': value.get('international_standard_book_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'c': value.get('terms_of_availability'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    indicator_map1 = {
        "Continuing resource not of international interest": "1",
        "Continuing resource of international interest": "0",
        "No level specified": "_"}
    field_map = {
        'canceled_issn': 'z',
        'international_standard_serial_number': 'a',
        'incorrect_issn': 'y',
        'canceled_issn_l': 'm',
        'issn_l': 'l',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('level_of_international_interest'), '7') != '7':
        try:
            order.remove(field_map.get('level_of_international_interest'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        'a': value.get('international_standard_serial_number'),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        'l': value.get('issn_l'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
        '$ind1': indicator_map1.get(value.get('level_of_international_interest'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {
        "International Article Number": "3",
        "International Standard Music Number": "2",
        "International Standard Recording Code": "0",
        "Serial Item and Contribution Identifier": "4",
        "Source specified in subfield $2": "7",
        "Universal Product Code": "1",
        "Unspecified type of standard number or code": "8"}
    indicator_map2 = {
        "Difference": "1",
        "No difference": "0",
        "No information provided": "_"}
    field_map = {
        'canceled_invalid_standard_number_or_code': 'z',
        'standard_number_or_code': 'a',
        'source_of_number_or_code': '2',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'qualifying_information': 'q',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'terms_of_availability': 'c',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_standard_number_or_code'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_standard_number_or_code'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('difference_indicator'), '7') != '7':
        try:
            order.remove(field_map.get('difference_indicator'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        'a': value.get('standard_number_or_code'),
        '2': value.get('source_of_number_or_code'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('terms_of_availability'),
        '$ind1': '7' if 'type_of_standard_number_or_code' in value and
        not indicator_map1.get(value.get('type_of_standard_number_or_code')) and
        value.get('type_of_standard_number_or_code') == value.get(
            'source_of_number_or_code')
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
        'date': 'c',
        'institution_to_which_field_applies': '5',
        'first_and_second_groups_of_characters': 'a',
        'number_of_volume_or_part': 'd',
        'third_and_fourth_groups_of_characters': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'unparsed_fingerprint': 'e',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('date'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('first_and_second_groups_of_characters'),
        'd': utils.reverse_force_list(
            value.get('number_of_volume_or_part')
        ),
        'b': value.get('third_and_fourth_groups_of_characters'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': value.get('unparsed_fingerprint'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('027', '^standard_technical_report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_standard_technical_report_number(self, key, value):
    """Reverse - Standard Technical Report Number."""
    field_map = {
        'qualifying_information': 'q',
        'canceled_invalid_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'standard_technical_report_number': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('standard_technical_report_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('028', '^publisher_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publisher_number(self, key, value):
    """Reverse - Publisher Number."""
    indicator_map1 = {
        "Issue number": "0",
        "Matrix number": "1",
        "Other music number": "3",
        "Other publisher number": "5",
        "Plate number": "2",
        "Videorecording number": "4"}
    indicator_map2 = {
        "No note, added entry": "3",
        "No note, no added entry": "0",
        "Note, added entry": "1",
        "Note, no added entry": "2"}
    field_map = {
        'qualifying_information': 'q',
        'source': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'publisher_number': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_publisher_number'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_publisher_number'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('note_added_entry_controller'), '7') != '7':
        try:
            order.remove(field_map.get('note_added_entry_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'b': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('publisher_number'),
        '$ind1': indicator_map1.get(value.get('type_of_publisher_number'), '_'),
        '$ind2': indicator_map2.get(value.get('note_added_entry_controller'), '_'),
    }


@to_marc21.over('030', '^coden_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coden_designation(self, key, value):
    """Reverse - CODEN Designation."""
    field_map = {
        'canceled_invalid_coden': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'coden': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_coden')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('coden'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'key_or_mode': 'r',
        'voice_instrument': 'm',
        'link_text': 'y',
        'text_incipit': 't',
        'field_link_and_sequence_number': '8',
        'number_of_movement': 'b',
        'number_of_work': 'a',
        'key_signature': 'n',
        'number_of_excerpt': 'c',
        'general_note': 'q',
        'public_note': 'z',
        'time_signature': 'o',
        'caption_or_heading': 'd',
        'coded_validity_note': 's',
        'linkage': '6',
        'system_code': '2',
        'clef': 'g',
        'role': 'e',
        'musical_notation': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'r': value.get('key_or_mode'),
        'm': value.get('voice_instrument'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_movement'),
        'a': value.get('number_of_work'),
        'n': value.get('key_signature'),
        'c': value.get('number_of_excerpt'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'o': value.get('time_signature'),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        '6': value.get('linkage'),
        '2': value.get('system_code'),
        'g': value.get('clef'),
        'e': value.get('role'),
        'p': value.get('musical_notation'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('032', '^postal_registration_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_postal_registration_number(self, key, value):
    """Reverse - Postal Registration Number."""
    field_map = {
        'source_agency_assigning_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'postal_registration_number': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('postal_registration_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('033', '^date_time_and_place_of_an_event$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event(self, key, value):
    """Reverse - Date/Time and Place of an Event."""
    indicator_map1 = {
        "Multiple single dates": "1",
        "No date information": "_",
        "Range of dates": "2",
        "Single date": "0"}
    indicator_map2 = {
        "Broadcast": "1",
        "Capture": "0",
        "Finding": "2",
        "No information provided": "_"}
    field_map = {
        'geographic_classification_subarea_code': 'c',
        'materials_specified': '3',
        'formatted_date_time': 'a',
        'place_of_event': 'p',
        'authority_record_control_number': '0',
        'geographic_classification_area_code': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_date_in_subfield_a'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_date_in_subfield_a'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_event'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_event'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '3': value.get('materials_specified'),
        'a': utils.reverse_force_list(
            value.get('formatted_date_time')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_area_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_date_in_subfield_a'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_event'), '_'),
    }


@to_marc21.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map1 = {
        "Range of scales": "3",
        "Scale indeterminable/No scale recorded": "0",
        "Single scale": "1"}
    indicator_map2 = {
        "Exclusion ring": "1",
        "Not applicable": "_",
        "Outer ring": "0"}
    field_map = {
        'right_ascension_eastern_limit': 'm',
        'declination_northern_limit': 'j',
        'g_ring_longitude': 't',
        'field_link_and_sequence_number': '8',
        'category_of_scale': 'a',
        'right_ascension_western_limit': 'n',
        'source': '2',
        'authority_record_control_number_or_standard_number': '0',
        'angular_scale': 'h',
        'coordinates_southernmost_latitude': 'g',
        'g_ring_latitude': 's',
        'ending_date': 'y',
        'coordinates_easternmost_longitude': 'e',
        'coordinates_northernmost_latitude': 'f',
        'materials_specified': '3',
        'constant_ratio_linear_horizontal_scale': 'b',
        'declination_southern_limit': 'k',
        'beginning_date': 'x',
        'constant_ratio_linear_vertical_scale': 'c',
        'name_of_extraterrestrial_body': 'z',
        'coordinates_westernmost_longitude': 'd',
        'linkage': '6',
        'distance_from_earth': 'r',
        'equinox': 'p',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_scale'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_scale'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_ring'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_ring'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'm': value.get('right_ascension_eastern_limit'),
        'j': value.get('declination_northern_limit'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('category_of_scale'),
        'n': value.get('right_ascension_western_limit'),
        '2': value.get('source'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'h': utils.reverse_force_list(
            value.get('angular_scale')
        ),
        'g': value.get('coordinates_southernmost_latitude'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        'y': value.get('ending_date'),
        'e': value.get('coordinates_easternmost_longitude'),
        'f': value.get('coordinates_northernmost_latitude'),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('constant_ratio_linear_horizontal_scale')
        ),
        'k': value.get('declination_southern_limit'),
        'x': value.get('beginning_date'),
        'c': utils.reverse_force_list(
            value.get('constant_ratio_linear_vertical_scale')
        ),
        'z': value.get('name_of_extraterrestrial_body'),
        'd': value.get('coordinates_westernmost_longitude'),
        '6': value.get('linkage'),
        'r': value.get('distance_from_earth'),
        'p': value.get('equinox'),
        '$ind1': indicator_map1.get(value.get('type_of_scale'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_ring'), '_'),
    }


@to_marc21.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    field_map = {
        'canceled_invalid_control_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'system_control_number': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('system_control_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('036', '^original_study_number_for_computer_data_files$')
@utils.filter_values
def reverse_original_study_number_for_computer_data_files(self, key, value):
    """Reverse - Original Study Number for Computer Data Files."""
    field_map = {
        'source_agency_assigning_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'original_study_number': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('original_study_number'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('037', '^source_of_acquisition$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_acquisition(self, key, value):
    """Reverse - Source of Acquisition."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2",
                      "Not applicable/No information provided/Earliest": "_"}
    field_map = {
        'terms_of_availability': 'c',
        'form_of_issue': 'f',
        'materials_specified': '3',
        'stock_number': 'a',
        'note': 'n',
        'source_of_stock_number_acquisition': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'additional_format_characteristics': 'g',
        'institution_to_which_field_applies': '5',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('source_of_acquisition_sequence'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_acquisition_sequence'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('terms_of_availability')
        ),
        'f': utils.reverse_force_list(
            value.get('form_of_issue')
        ),
        '3': value.get('materials_specified'),
        'a': value.get('stock_number'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'b': value.get('source_of_stock_number_acquisition'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('additional_format_characteristics')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
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
        'field_link_and_sequence_number': '8',
        'record_content_licensor': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('record_content_licensor'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    field_map = {
        'original_cataloging_agency': 'a',
        'modifying_agency': 'd',
        'language_of_cataloging': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'description_conventions': 'e',
        'transcribing_agency': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_cataloging_agency'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'b': value.get('language_of_cataloging'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        'c': value.get('transcribing_agency'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('041', '^language_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_code(self, key, value):
    """Reverse - Language Code."""
    indicator_map1 = {
        "Item is or includes a translation": "1",
        "Item not a translation/does not include a translation": "0",
        "No information provided": "_"}
    indicator_map2 = {
        "MARC language code": "_",
        "Source specified in subfield $2": "7"}
    field_map = {
        'language_code_of_table_of_contents': 'f',
        'language_code_of_original_accompanying_materials_other_than_librettos': 'm',
        'language_code_of_subtitles_or_captions': 'j',
        'language_code_of_original_libretto': 'n',
        'language_code_of_intermediate_translations': 'k',
        'language_code_of_summary_or_abstract': 'b',
        'language_code_of_text_sound_track_or_separate_title': 'a',
        'field_link_and_sequence_number': '8',
        'source_of_code': '2',
        'language_code_of_sung_or_spoken_text': 'd',
        'language_code_of_original': 'h',
        'linkage': '6',
        'language_code_of_accompanying_material_other_than_librettos': 'g',
        'language_code_of_librettos': 'e',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('translation_indication'), '7') != '7':
        try:
            order.remove(field_map.get('translation_indication'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('source_of_code'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_code'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'f': utils.reverse_force_list(
            value.get('language_code_of_table_of_contents')
        ),
        'm': utils.reverse_force_list(
            value.get(
                'language_code_of_original_accompanying_materials_other_than_librettos')
        ),
        'j': utils.reverse_force_list(
            value.get('language_code_of_subtitles_or_captions')
        ),
        'n': utils.reverse_force_list(
            value.get('language_code_of_original_libretto')
        ),
        'k': utils.reverse_force_list(
            value.get('language_code_of_intermediate_translations')
        ),
        'b': utils.reverse_force_list(
            value.get('language_code_of_summary_or_abstract')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code_of_text_sound_track_or_separate_title')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_code'),
        'd': utils.reverse_force_list(
            value.get('language_code_of_sung_or_spoken_text')
        ),
        'h': utils.reverse_force_list(
            value.get('language_code_of_original')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get(
                'language_code_of_accompanying_material_other_than_librettos')
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
        'iso_code': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_area_code': 'a',
        'local_gac_code': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source_of_local_code': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('044', '^country_of_publishing_producing_entity_code$')
@utils.filter_values
def reverse_country_of_publishing_producing_entity_code(self, key, value):
    """Reverse - Country of Publishing/Producing Entity Code."""
    field_map = {
        'iso_country_code': 'c',
        'marc_country_code': 'a',
        'local_subentity_code': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'source_of_local_subentity_code': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('iso_country_code')
        ),
        'a': utils.reverse_force_list(
            value.get('marc_country_code')
        ),
        'b': utils.reverse_force_list(
            value.get('local_subentity_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
    indicator_map1 = {
        "Multiple single dates/times": "1",
        "Range of dates/times": "2",
        "Single date/time": "0",
        "Subfield $b or $c not present": "_"}
    field_map = {
        'formatted_9999_bc_through_ce_time_period': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'time_period_code': 'a',
        'formatted_pre_9999_bc_time_period': 'c',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('type_of_time_period_in_subfield_b_or_c'), '7') != '7':
        try:
            order.remove(
                field_map.get('type_of_time_period_in_subfield_b_or_c'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_code')
        ),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
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
        'beginning_of_date_valid': 'm',
        'date_resource_modified': 'j',
        'end_of_date_valid': 'n',
        'field_link_and_sequence_number': '8',
        'date_1_bc_date': 'b',
        'type_of_date_code': 'a',
        'beginning_or_single_date_created': 'k',
        'date_1_ce_date': 'c',
        'single_or_starting_date_for_aggregated_content': 'o',
        'date_2_bc_date': 'd',
        'ending_date_created': 'l',
        'linkage': '6',
        'source_of_date': '2',
        'date_2_ce_date': 'e',
        'ending_date_for_aggregated_content': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'm': value.get('beginning_of_date_valid'),
        'j': value.get('date_resource_modified'),
        'n': value.get('end_of_date_valid'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('date_1_bc_date'),
        'a': value.get('type_of_date_code'),
        'k': value.get('beginning_or_single_date_created'),
        'c': value.get('date_1_ce_date'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'd': value.get('date_2_bc_date'),
        'l': value.get('ending_date_created'),
        '6': value.get('linkage'),
        '2': value.get('source_of_date'),
        'e': value.get('date_2_ce_date'),
        'p': value.get('ending_date_for_aggregated_content'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('047', '^form_of_musical_composition_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_musical_composition_code(self, key, value):
    """Reverse - Form of Musical Composition Code."""
    indicator_map2 = {
        "MARC musical composition code": "_",
        "Source specified in subfield $2": "7"}
    field_map = {
        'form_of_musical_composition_code': 'a',
        'field_link_and_sequence_number': '8',
        'source_of_code': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_code'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('form_of_musical_composition_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_code'),
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
        'soloist': 'b',
        'performer_or_ensemble': 'a',
        'field_link_and_sequence_number': '8',
        'source_of_code': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_code'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        'a': utils.reverse_force_list(
            value.get('performer_or_ensemble')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source_of_code'),
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
    indicator_map1 = {
        "Item is in LC": "0",
        "Item is not in LC": "1",
        "No information provided": "_"}
    indicator_map2 = {"Assigned by LC": "0",
                      "Assigned by agency other than LC": "4"}
    field_map = {
        'item_number': 'b',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('existence_in_lc_collection'), '7') != '7':
        try:
            order.remove(field_map.get('existence_in_lc_collection'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('source_of_call_number'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_call_number'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_lc_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21.over('051', '^library_of_congress_copy_issue_offprint_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_copy_issue_offprint_statement(
        self, key, value):
    """Reverse - Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('copy_information'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {
        "Library of Congress Classification": "_",
        "Source specified in subfield $2": "7",
        "U.S. Dept. of Defense Classification": "1"}
    field_map = {
        'geographic_classification_area_code': 'a',
        'populated_place_name': 'd',
        'geographic_classification_subarea_code': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'code_source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('code_source'), '7') != '7':
        try:
            order.remove(field_map.get('code_source'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_classification_area_code'),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('code_source'),
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
    indicator_map1 = {
        "Information not provided": "_",
        "Work held by LAC": "0",
        "Work not held by LAC": "1"}
    indicator_map2 = {
        "Complete LC class number assigned by LAC": "1",
        "Complete LC class number assigned by the contributing library": "4",
        "Incomplete LC class number assigned by LAC": "2",
        "Incomplete LC class number assigned by the contributing library": "5",
        "LC-based call number assigned by LAC": "0",
        "LC-based call number assigned by the contributing library": "3",
        "Other call number assigned by LAC": "6",
        "Other call number assigned by the contributing library": "8",
        "Other class number assigned by LAC": "7",
        "Other class number assigned by the contributing library": "9"}
    field_map = {
        'item_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
        'source_of_call_class_number': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('existence_in_lac_collection'), '7') != '7':
        try:
            order.remove(field_map.get('existence_in_lac_collection'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('type_completeness_source_of_class_call_number'), '7') != '7':
        try:
            order.remove(
                field_map.get('type_completeness_source_of_class_call_number'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('classification_number'),
        '2': value.get('source_of_call_class_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_lac_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('type_completeness_source_of_class_call_number'), '_'),
    }


@to_marc21.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map1 = {
        "Item is in NLM": "0",
        "Item is not in NLM": "1",
        "No information provided": "_"}
    indicator_map2 = {"Assigned by NLM": "0",
                      "Assigned by agency other than NLM": "4"}
    field_map = {
        'item_number': 'b',
        'classification_number_r': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('existence_in_nlm_collection'), '7') != '7':
        try:
            order.remove(field_map.get('existence_in_nlm_collection'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('source_of_call_number'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_call_number'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'a': utils.reverse_force_list(
            value.get('classification_number_r')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_nlm_collection'), '_'),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), '_'),
    }


@to_marc21.over('061', '^national_library_of_medicine_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_copy_statement(self, key, value):
    """Reverse - National Library of Medicine Copy Statement."""
    field_map = {
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('copy_information'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""
    field_map = {
        'primary_g1_character_set': 'b',
        'primary_g0_character_set': 'a',
        'alternate_g0_or_g1_character_set': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('primary_g1_character_set'),
        'a': value.get('primary_g0_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
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
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number_r': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('existence_in_nal_collection'), '7') != '7':
        try:
            order.remove(field_map.get('existence_in_nal_collection'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_nal_collection'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('071', '^national_agricultural_library_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_copy_statement(self, key, value):
    """Reverse - National Agricultural Library Copy Statement."""
    field_map = {
        'item_number': 'b',
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('copy_information')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {
        "NAL subject category code list": "0",
        "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'subject_category_code_subdivision': 'x',
        'subject_category_code': 'a',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('code_source'), '7') != '7':
        try:
            order.remove(field_map.get('code_source'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        'a': value.get('subject_category_code'),
        '2': value.get('source'),
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
        'canceled_invalid_gpo_item_number': 'z',
        'gpo_item_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_gpo_item_number')
        ),
        'a': value.get('gpo_item_number'),
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
    indicator_map1 = {
        "Abridged": "1",
        "Full": "0",
        "No information provided": "_"}
    field_map = {
        'universal_decimal_classification_number': 'a',
        'item_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'common_auxiliary_subdivision': 'x',
        'edition_identifier': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_edition'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_edition'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('universal_decimal_classification_number'),
        'b': value.get('item_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '2': value.get('edition_identifier'),
        '$ind1': indicator_map1.get(value.get('type_of_edition'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('082', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {
        "Abridged edition": "1",
        "Full edition": "0",
        "Other edition specified in subfield $2": "7"}
    indicator_map2 = {
        "Assigned by LC": "0",
        "Assigned by agency other than LC": "4",
        "No information provided": "_"}
    field_map = {
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'assigning_agency': 'q',
        'item_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'edition_number': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_edition'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_edition'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('source_of_classification_number'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_classification_number'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        'q': value.get('assigning_agency'),
        'b': value.get('item_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_number'),
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
    indicator_map1 = {
        "Abridged edition": "1",
        "Full edition": "0",
        "Other edition specified in subfield $2": "7"}
    field_map = {
        'table_identification': 'z',
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'edition_number': '2',
        'assigning_agency': 'q',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'classification_number_ending_number_of_span': 'c',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_edition'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_edition'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        'y': utils.reverse_force_list(
            value.get(
                'table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        '2': value.get('edition_number'),
        'q': value.get('assigning_agency'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
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
        'classification_number': 'a',
        'assigning_agency': 'q',
        'item_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'number_source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'q': value.get('assigning_agency'),
        'b': value.get('item_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('number_source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('085', '^synthesized_classification_number_components$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_synthesized_classification_number_components(self, key, value):
    """Reverse - Synthesized Classification Number Components."""
    field_map = {
        'number_being_analyzed': 'u',
        'facet_designator': 'f',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'digits_added_from_internal_subarrangement_or_add_table': 't',
        'base_number': 'b',
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': 'a',
        'field_link_and_sequence_number': '8',
        'table_identification_internal_subarrangement_or_add_table': 'w',
        'classification_number_ending_number_of_span': 'c',
        'table_identification': 'z',
        'digits_added_from_classification_number_in_schedule_or_external_table': 's',
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': 'v',
        'linkage': '6',
        'root_number': 'r',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('number_being_analyzed')
        ),
        'f': utils.reverse_force_list(
            value.get('facet_designator')
        ),
        'y': utils.reverse_force_list(
            value.get(
                'table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        't': utils.reverse_force_list(
            value.get('digits_added_from_internal_subarrangement_or_add_table')
        ),
        'b': utils.reverse_force_list(
            value.get('base_number')
        ),
        'a': utils.reverse_force_list(
            value.get(
                'number_where_instructions_are_found_single_number_or_beginning_number_of_span')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': utils.reverse_force_list(
            value.get('table_identification_internal_subarrangement_or_add_table')
        ),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        's': utils.reverse_force_list(
            value.get(
                'digits_added_from_classification_number_in_schedule_or_external_table')
        ),
        'v': utils.reverse_force_list(
            value.get(
                'number_in_internal_subarrangement_or_add_table_where_instructions_are_found')
        ),
        '6': value.get('linkage'),
        'r': utils.reverse_force_list(
            value.get('root_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('086', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    indicator_map1 = {
        "Government of Canada Publications: Outline of Classification": "1",
        "Source specified in subfield $2": "_",
        "Superintendent of Documents Classification System": "0"}
    field_map = {
        'canceled_invalid_classification_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
        'number_source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('number_source'), '7') != '7':
        try:
            order.remove(field_map.get('number_source'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_classification_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('classification_number'),
        '2': value.get('number_source'),
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
        'canceled_invalid_report_number': 'z',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'report_number': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_report_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('report_number'),
        '$ind1': '_',
        '$ind2': '_',
    }
