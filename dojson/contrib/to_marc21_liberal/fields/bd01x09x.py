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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""
    field_map = {
        'canceled_invalid_lc_control_number': 'z',
        'nucmc_control_number': 'b',
        'field_link_and_sequence_number': '8',
        'lc_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('nucmc_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('lc_control_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('013', '^patent_control_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_patent_control_information(self, key, value):
    """Reverse - Patent Control Information."""
    field_map = {
        'linkage': '6',
        'date': 'd',
        'country': 'b',
        'field_link_and_sequence_number': '8',
        'number': 'a',
        'party_to_document': 'f',
        'status': 'e',
        'type_of_number': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('date')
        ),
        'b': value.get('country'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('number'),
        'f': utils.reverse_force_list(
            value.get('party_to_document')
        ),
        'e': utils.reverse_force_list(
            value.get('status')
        ),
        'c': value.get('type_of_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('015', '^national_bibliography_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliography_number(self, key, value):
    """Reverse - National Bibliography Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_national_bibliography_number': 'z',
        'qualifying_information': 'q',
        'national_bibliography_number': 'a',
        'source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_national_bibliography_number')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'a': utils.reverse_force_list(
            value.get('national_bibliography_number')
        ),
        '2': value.get('source'),
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


@to_marc21_liberal.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    indicator_map1 = {"Library and Archives Canada": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source': '2',
        'canceled_invalid_control_number': 'z',
        'field_link_and_sequence_number': '8',
        'record_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['national_bibliographic_agency', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('record_control_number'),
        '$ind1': '7' if 'national_bibliographic_agency' in value and
        not indicator_map1.get(value.get('national_bibliographic_agency')) and
        value.get('national_bibliographic_agency') == value.get('source') and
        field_map.get('national_bibliographic_agency') in order
        else indicator_map1.get(value.get('national_bibliographic_agency'), value.get('national_bibliographic_agency', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('017', '^copyright_or_legal_deposit_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copyright_or_legal_deposit_number(self, key, value):
    """Reverse - Copyright or Legal Deposit Number."""
    indicator_map2 = {"Copyright or legal deposit number": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'date': 'd',
        'assigning_agency': 'b',
        'copyright_or_legal_deposit_number': 'a',
        'display_text': 'i',
        'source': '2',
        'canceled_invalid_copyright_or_legal_deposit_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('date'),
        'b': value.get('assigning_agency'),
        'a': utils.reverse_force_list(
            value.get('copyright_or_legal_deposit_number')
        ),
        'i': value.get('display_text'),
        '2': value.get('source'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_copyright_or_legal_deposit_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('018', '^copyright_article_fee_code$')
@utils.filter_values
def reverse_copyright_article_fee_code(self, key, value):
    """Reverse - Copyright Article-Fee Code."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'copyright_article_fee_code_nr': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('copyright_article_fee_code_nr')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('020', '^international_standard_book_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_book_number(self, key, value):
    """Reverse - International Standard Book Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_isbn': 'z',
        'qualifying_information': 'q',
        'international_standard_book_number': 'a',
        'field_link_and_sequence_number': '8',
        'terms_of_availability': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        'a': value.get('international_standard_book_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('terms_of_availability'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    indicator_map1 = {"Continuing resource not of international interest": "1", "Continuing resource of international interest": "0", "No level specified": "_"}
    field_map = {
        'linkage': '6',
        'canceled_issn': 'z',
        'international_standard_serial_number': 'a',
        'issn_l': 'l',
        'source': '2',
        'canceled_issn_l': 'm',
        'field_link_and_sequence_number': '8',
        'incorrect_issn': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level_of_international_interest', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        'a': value.get('international_standard_serial_number'),
        'l': value.get('issn_l'),
        '2': value.get('source'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_international_interest'), value.get('level_of_international_interest', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {"International Article Number": "3", "International Standard Music Number": "2", "International Standard Recording Code": "0", "Serial Item and Contribution Identifier": "4", "Source specified in subfield $2": "7", "Universal Product Code": "1", "Unspecified type of standard number or code": "8"}
    indicator_map2 = {"Difference": "1", "No difference": "0", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'field_link_and_sequence_number': '8',
        'standard_number_or_code': 'a',
        'source_of_number_or_code': '2',
        'canceled_invalid_standard_number_or_code': 'z',
        'terms_of_availability': 'c',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_standard_number_or_code', 'difference_indicator'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('standard_number_or_code'),
        '2': value.get('source_of_number_or_code'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        'c': value.get('terms_of_availability'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '$ind1': '7' if 'type_of_standard_number_or_code' in value and
        not indicator_map1.get(value.get('type_of_standard_number_or_code')) and
        value.get('type_of_standard_number_or_code') == value.get('source_of_number_or_code') and
        field_map.get('type_of_standard_number_or_code') in order
        else indicator_map1.get(value.get('type_of_standard_number_or_code'), value.get('type_of_standard_number_or_code', '_')),
        '$ind2': indicator_map2.get(value.get('difference_indicator'), value.get('difference_indicator', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('025', '^overseas_acquisition_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_overseas_acquisition_number(self, key, value):
    """Reverse - Overseas Acquisition Number."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'overseas_acquisition_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('overseas_acquisition_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('026', '^fingerprint_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_fingerprint_identifier(self, key, value):
    """Reverse - Fingerprint Identifier."""
    field_map = {
        'linkage': '6',
        'number_of_volume_or_part': 'd',
        'institution_to_which_field_applies': '5',
        'date': 'c',
        'first_and_second_groups_of_characters': 'a',
        'source': '2',
        'third_and_fourth_groups_of_characters': 'b',
        'unparsed_fingerprint': 'e',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('number_of_volume_or_part')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'c': value.get('date'),
        'a': value.get('first_and_second_groups_of_characters'),
        '2': value.get('source'),
        'b': value.get('third_and_fourth_groups_of_characters'),
        'e': value.get('unparsed_fingerprint'),
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


@to_marc21_liberal.over('027', '^standard_technical_report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_standard_technical_report_number(self, key, value):
    """Reverse - Standard Technical Report Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_number': 'z',
        'qualifying_information': 'q',
        'field_link_and_sequence_number': '8',
        'standard_technical_report_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_number')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('standard_technical_report_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('028', '^publisher_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publisher_number(self, key, value):
    """Reverse - Publisher Number."""
    indicator_map1 = {"Issue number": "0", "Matrix number": "1", "Other music number": "3", "Other publisher number": "5", "Plate number": "2", "Videorecording number": "4"}
    indicator_map2 = {"No note, added entry": "3", "No note, no added entry": "0", "Note, added entry": "1", "Note, no added entry": "2"}
    field_map = {
        'linkage': '6',
        'source': 'b',
        'qualifying_information': 'q',
        'field_link_and_sequence_number': '8',
        'publisher_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_publisher_number', 'note_added_entry_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('source'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('publisher_number'),
        '$ind1': indicator_map1.get(value.get('type_of_publisher_number'), value.get('type_of_publisher_number', '_')),
        '$ind2': indicator_map2.get(value.get('note_added_entry_controller'), value.get('note_added_entry_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('030', '^coden_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coden_designation(self, key, value):
    """Reverse - CODEN Designation."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_coden': 'z',
        'field_link_and_sequence_number': '8',
        'coden': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_coden')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('coden'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""
    field_map = {
        'caption_or_heading': 'd',
        'coded_validity_note': 's',
        'key_signature': 'n',
        'number_of_work': 'a',
        'public_note': 'z',
        'system_code': '2',
        'voice_instrument': 'm',
        'key_or_mode': 'r',
        'number_of_excerpt': 'c',
        'linkage': '6',
        'uniform_resource_identifier': 'u',
        'number_of_movement': 'b',
        'time_signature': 'o',
        'field_link_and_sequence_number': '8',
        'text_incipit': 't',
        'clef': 'g',
        'link_text': 'y',
        'role': 'e',
        'musical_notation': 'p',
        'general_note': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        'n': value.get('key_signature'),
        'a': value.get('number_of_work'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('system_code'),
        'm': value.get('voice_instrument'),
        'r': value.get('key_or_mode'),
        'c': value.get('number_of_excerpt'),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'b': value.get('number_of_movement'),
        'o': value.get('time_signature'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'g': value.get('clef'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'e': value.get('role'),
        'p': value.get('musical_notation'),
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


@to_marc21_liberal.over('032', '^postal_registration_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_postal_registration_number(self, key, value):
    """Reverse - Postal Registration Number."""
    field_map = {
        'linkage': '6',
        'source_agency_assigning_number': 'b',
        'field_link_and_sequence_number': '8',
        'postal_registration_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('source_agency_assigning_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('postal_registration_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('033', '^date_time_and_place_of_an_event$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event(self, key, value):
    """Reverse - Date/Time and Place of an Event."""
    indicator_map1 = {"Multiple single dates": "1", "No date information": "_", "Range of dates": "2", "Single date": "0"}
    indicator_map2 = {"Broadcast": "1", "Capture": "0", "Finding": "2", "No information provided": "_"}
    field_map = {
        'materials_specified': '3',
        'linkage': '6',
        'authority_record_control_number': '0',
        'geographic_classification_area_code': 'b',
        'geographic_classification_subarea_code': 'c',
        'formatted_date_time': 'a',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'place_of_event': 'p',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_date_in_subfield_a', 'type_of_event'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_area_code')
        ),
        'c': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        'a': utils.reverse_force_list(
            value.get('formatted_date_time')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_date_in_subfield_a'), value.get('type_of_date_in_subfield_a', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_event'), value.get('type_of_event', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map1 = {"Range of scales": "3", "Scale indeterminable/No scale recorded": "0", "Single scale": "1"}
    indicator_map2 = {"Exclusion ring": "1", "Not applicable": "_", "Outer ring": "0"}
    field_map = {
        'angular_scale': 'h',
        'distance_from_earth': 'r',
        'g_ring_latitude': 's',
        'right_ascension_western_limit': 'n',
        'category_of_scale': 'a',
        'source': '2',
        'coordinates_northernmost_latitude': 'f',
        'name_of_extraterrestrial_body': 'z',
        'constant_ratio_linear_vertical_scale': 'c',
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'constant_ratio_linear_horizontal_scale': 'b',
        'field_link_and_sequence_number': '8',
        'g_ring_longitude': 't',
        'coordinates_southernmost_latitude': 'g',
        'declination_northern_limit': 'j',
        'coordinates_easternmost_longitude': 'e',
        'equinox': 'p',
        'materials_specified': '3',
        'coordinates_westernmost_longitude': 'd',
        'right_ascension_eastern_limit': 'm',
        'beginning_date': 'x',
        'ending_date': 'y',
        'declination_southern_limit': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_scale', 'type_of_ring'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': utils.reverse_force_list(
            value.get('angular_scale')
        ),
        'r': value.get('distance_from_earth'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        'n': value.get('right_ascension_western_limit'),
        'a': value.get('category_of_scale'),
        '2': value.get('source'),
        'f': value.get('coordinates_northernmost_latitude'),
        'z': value.get('name_of_extraterrestrial_body'),
        'c': utils.reverse_force_list(
            value.get('constant_ratio_linear_vertical_scale')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('constant_ratio_linear_horizontal_scale')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        'g': value.get('coordinates_southernmost_latitude'),
        'j': value.get('declination_northern_limit'),
        'e': value.get('coordinates_easternmost_longitude'),
        'p': value.get('equinox'),
        '3': value.get('materials_specified'),
        'd': value.get('coordinates_westernmost_longitude'),
        'm': value.get('right_ascension_eastern_limit'),
        'x': value.get('beginning_date'),
        'y': value.get('ending_date'),
        'k': value.get('declination_southern_limit'),
        '$ind1': indicator_map1.get(value.get('type_of_scale'), value.get('type_of_scale', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_ring'), value.get('type_of_ring', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_control_number': 'z',
        'field_link_and_sequence_number': '8',
        'system_control_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('system_control_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('036', '^original_study_number_for_computer_data_files$')
@utils.filter_values
def reverse_original_study_number_for_computer_data_files(self, key, value):
    """Reverse - Original Study Number for Computer Data Files."""
    field_map = {
        'linkage': '6',
        'source_agency_assigning_number': 'b',
        'field_link_and_sequence_number': '8',
        'original_study_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('source_agency_assigning_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('original_study_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('037', '^source_of_acquisition$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_acquisition(self, key, value):
    """Reverse - Source of Acquisition."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2", "Not applicable/No information provided/Earliest": "_"}
    field_map = {
        'materials_specified': '3',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'terms_of_availability': 'c',
        'stock_number': 'a',
        'additional_format_characteristics': 'g',
        'form_of_issue': 'f',
        'source_of_stock_number_acquisition': 'b',
        'field_link_and_sequence_number': '8',
        'note': 'n',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['source_of_acquisition_sequence', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'c': utils.reverse_force_list(
            value.get('terms_of_availability')
        ),
        'a': value.get('stock_number'),
        'g': utils.reverse_force_list(
            value.get('additional_format_characteristics')
        ),
        'f': utils.reverse_force_list(
            value.get('form_of_issue')
        ),
        'b': value.get('source_of_stock_number_acquisition'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '$ind1': indicator_map1.get(value.get('source_of_acquisition_sequence'), value.get('source_of_acquisition_sequence', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('038', '^record_content_licensor$')
@utils.filter_values
def reverse_record_content_licensor(self, key, value):
    """Reverse - Record Content Licensor."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'record_content_licensor': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('record_content_licensor'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    field_map = {
        'linkage': '6',
        'modifying_agency': 'd',
        'language_of_cataloging': 'b',
        'field_link_and_sequence_number': '8',
        'original_cataloging_agency': 'a',
        'description_conventions': 'e',
        'transcribing_agency': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        'b': value.get('language_of_cataloging'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('original_cataloging_agency'),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        'c': value.get('transcribing_agency'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('041', '^language_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_code(self, key, value):
    """Reverse - Language Code."""
    indicator_map1 = {"Item is or includes a translation": "1", "Item not a translation/does not include a translation": "0", "No information provided": "_"}
    indicator_map2 = {"MARC language code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'language_code_of_original_accompanying_materials_other_than_librettos': 'm',
        'language_code_of_original': 'h',
        'language_code_of_sung_or_spoken_text': 'd',
        'language_code_of_original_libretto': 'n',
        'language_code_of_text_sound_track_or_separate_title': 'a',
        'source_of_code': '2',
        'language_code_of_table_of_contents': 'f',
        'language_code_of_subtitles_or_captions': 'j',
        'linkage': '6',
        'language_code_of_summary_or_abstract': 'b',
        'field_link_and_sequence_number': '8',
        'language_code_of_accompanying_material_other_than_librettos': 'g',
        'language_code_of_librettos': 'e',
        'language_code_of_intermediate_translations': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['translation_indication', 'source_of_code'])

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'm': utils.reverse_force_list(
            value.get('language_code_of_original_accompanying_materials_other_than_librettos')
        ),
        'h': utils.reverse_force_list(
            value.get('language_code_of_original')
        ),
        'd': utils.reverse_force_list(
            value.get('language_code_of_sung_or_spoken_text')
        ),
        'n': utils.reverse_force_list(
            value.get('language_code_of_original_libretto')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code_of_text_sound_track_or_separate_title')
        ),
        '2': value.get('source_of_code'),
        'f': utils.reverse_force_list(
            value.get('language_code_of_table_of_contents')
        ),
        'j': utils.reverse_force_list(
            value.get('language_code_of_subtitles_or_captions')
        ),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('language_code_of_summary_or_abstract')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'g': utils.reverse_force_list(
            value.get('language_code_of_accompanying_material_other_than_librettos')
        ),
        'e': utils.reverse_force_list(
            value.get('language_code_of_librettos')
        ),
        'k': utils.reverse_force_list(
            value.get('language_code_of_intermediate_translations')
        ),
        '$ind1': indicator_map1.get(value.get('translation_indication'), value.get('translation_indication', '_')),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code') and
        field_map.get('source_of_code') in order
        else indicator_map2.get(value.get('source_of_code'), value.get('source_of_code', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('042', '^authentication_code$')
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


@to_marc21_liberal.over('043', '^geographic_area_code$')
@utils.filter_values
def reverse_geographic_area_code(self, key, value):
    """Reverse - Geographic Area Code."""
    field_map = {
        'linkage': '6',
        'authority_record_control_number_or_standard_number': '0',
        'local_gac_code': 'b',
        'iso_code': 'c',
        'geographic_area_code': 'a',
        'source_of_local_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
        ),
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


@to_marc21_liberal.over('044', '^country_of_publishing_producing_entity_code$')
@utils.filter_values
def reverse_country_of_publishing_producing_entity_code(self, key, value):
    """Reverse - Country of Publishing/Producing Entity Code."""
    field_map = {
        'linkage': '6',
        'local_subentity_code': 'b',
        'iso_country_code': 'c',
        'marc_country_code': 'a',
        'source_of_local_subentity_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('local_subentity_code')
        ),
        'c': utils.reverse_force_list(
            value.get('iso_country_code')
        ),
        'a': utils.reverse_force_list(
            value.get('marc_country_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_subentity_code')
        ),
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


@to_marc21_liberal.over('045', '^time_period_of_content$')
@utils.filter_values
def reverse_time_period_of_content(self, key, value):
    """Reverse - Time Period of Content."""
    indicator_map1 = {"Multiple single dates/times": "1", "Range of dates/times": "2", "Single date/time": "0", "Subfield $b or $c not present": "_"}
    field_map = {
        'linkage': '6',
        'formatted_9999_bc_through_ce_time_period': 'b',
        'formatted_pre_9999_bc_time_period': 'c',
        'field_link_and_sequence_number': '8',
        'time_period_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period_in_subfield_b_or_c', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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


@to_marc21_liberal.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""
    field_map = {
        'date_2_bc_date': 'd',
        'end_of_date_valid': 'n',
        'type_of_date_code': 'a',
        'source_of_date': '2',
        'beginning_of_date_valid': 'm',
        'date_1_ce_date': 'c',
        'linkage': '6',
        'date_1_bc_date': 'b',
        'single_or_starting_date_for_aggregated_content': 'o',
        'date_resource_modified': 'j',
        'ending_date_created': 'l',
        'field_link_and_sequence_number': '8',
        'date_2_ce_date': 'e',
        'ending_date_for_aggregated_content': 'p',
        'beginning_or_single_date_created': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('date_2_bc_date'),
        'n': value.get('end_of_date_valid'),
        'a': value.get('type_of_date_code'),
        '2': value.get('source_of_date'),
        'm': value.get('beginning_of_date_valid'),
        'c': value.get('date_1_ce_date'),
        '6': value.get('linkage'),
        'b': value.get('date_1_bc_date'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'j': value.get('date_resource_modified'),
        'l': value.get('ending_date_created'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': value.get('date_2_ce_date'),
        'p': value.get('ending_date_for_aggregated_content'),
        'k': value.get('beginning_or_single_date_created'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('047', '^form_of_musical_composition_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_musical_composition_code(self, key, value):
    """Reverse - Form of Musical Composition Code."""
    indicator_map2 = {"MARC musical composition code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source_of_code': '2',
        'field_link_and_sequence_number': '8',
        'form_of_musical_composition_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('form_of_musical_composition_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code') and
        field_map.get('source_of_code') in order
        else indicator_map2.get(value.get('source_of_code'), value.get('source_of_code', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('048', '^number_of_musical_instruments_or_voices_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_number_of_musical_instruments_or_voices_code(self, key, value):
    """Reverse - Number of Musical Instruments or Voices Code."""
    indicator_map2 = {"MARC code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'source_of_code': '2',
        'soloist': 'b',
        'field_link_and_sequence_number': '8',
        'performer_or_ensemble': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_code'),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('performer_or_ensemble')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source_of_code') and
        field_map.get('source_of_code') in order
        else indicator_map2.get(value.get('source_of_code'), value.get('source_of_code', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map1 = {"Item is in LC": "0", "Item is not in LC": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    field_map = {
        'materials_specified': '3',
        'linkage': '6',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_lc_collection', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_lc_collection'), value.get('existence_in_lc_collection', '_')),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('051', '^library_of_congress_copy_issue_offprint_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Reverse - Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('classification_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    indicator_map1 = {"Library of Congress Classification": "_", "Source specified in subfield $2": "7", "U.S. Dept. of Defense Classification": "1"}
    field_map = {
        'linkage': '6',
        'populated_place_name': 'd',
        'geographic_classification_subarea_code': 'b',
        'geographic_classification_area_code': 'a',
        'code_source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['code_source', 'None'])

    if (indicator_map1.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        'a': value.get('geographic_classification_area_code'),
        '2': value.get('code_source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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


@to_marc21_liberal.over('055', '^classification_numbers_assigned_in_canada$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_classification_numbers_assigned_in_canada(self, key, value):
    """Reverse - Classification Numbers Assigned in Canada."""
    indicator_map1 = {"Information not provided": "_", "Work held by LAC": "0", "Work not held by LAC": "1"}
    indicator_map2 = {"Complete LC class number assigned by LAC": "1", "Complete LC class number assigned by the contributing library": "4", "Incomplete LC class number assigned by LAC": "2", "Incomplete LC class number assigned by the contributing library": "5", "LC-based call number assigned by LAC": "0", "LC-based call number assigned by the contributing library": "3", "Other call number assigned by LAC": "6", "Other call number assigned by the contributing library": "8", "Other class number assigned by LAC": "7", "Other class number assigned by the contributing library": "9"}
    field_map = {
        'linkage': '6',
        'source_of_call_class_number': '2',
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_lac_collection', 'type_completeness_source_of_class_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source_of_call_class_number'),
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('classification_number'),
        '$ind1': indicator_map1.get(value.get('existence_in_lac_collection'), value.get('existence_in_lac_collection', '_')),
        '$ind2': indicator_map2.get(value.get('type_completeness_source_of_class_call_number'), value.get('type_completeness_source_of_class_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map1 = {"Item is in NLM": "0", "Item is not in NLM": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by NLM": "0", "Assigned by agency other than NLM": "4"}
    field_map = {
        'item_number': 'b',
        'field_link_and_sequence_number': '8',
        'classification_number_r': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_nlm_collection', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number_r')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_nlm_collection'), value.get('existence_in_nlm_collection', '_')),
        '$ind2': indicator_map2.get(value.get('source_of_call_number'), value.get('source_of_call_number', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('061', '^national_library_of_medicine_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_copy_statement(self, key, value):
    """Reverse - National Library of Medicine Copy Statement."""
    field_map = {
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('066', '^character_sets_present$')
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


@to_marc21_liberal.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""
    indicator_map1 = {"Item is in NAL": "0", "Item is not in NAL": "1"}
    field_map = {
        'item_number': 'b',
        'field_link_and_sequence_number_r': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_nal_collection', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '$ind1': indicator_map1.get(value.get('existence_in_nal_collection'), value.get('existence_in_nal_collection', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('071', '^national_agricultural_library_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_copy_statement(self, key, value):
    """Reverse - National Agricultural Library Copy Statement."""
    field_map = {
        'item_number': 'b',
        'copy_information': 'c',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('item_number'),
        'c': utils.reverse_force_list(
            value.get('copy_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    indicator_map2 = {"NAL subject category code list": "0", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'source': '2',
        'subject_category_code_subdivision': 'x',
        'field_link_and_sequence_number': '8',
        'subject_category_code': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'code_source'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('subject_category_code'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'code_source' in value and
        not indicator_map2.get(value.get('code_source')) and
        value.get('code_source') == value.get('source') and
        field_map.get('code_source') in order
        else indicator_map2.get(value.get('code_source'), value.get('code_source', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('074', '^gpo_item_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_gpo_item_number(self, key, value):
    """Reverse - GPO Item Number."""
    field_map = {
        'canceled_invalid_gpo_item_number': 'z',
        'field_link_and_sequence_number': '8',
        'gpo_item_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_gpo_item_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('gpo_item_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'item_number': 'b',
        'universal_decimal_classification_number': 'a',
        'edition_identifier': '2',
        'common_auxiliary_subdivision': 'x',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        'a': value.get('universal_decimal_classification_number'),
        '2': value.get('edition_identifier'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_edition'), value.get('type_of_edition', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('082', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4", "No information provided": "_"}
    field_map = {
        'linkage': '6',
        'item_number': 'b',
        'assigning_agency': 'q',
        'classification_number': 'a',
        'edition_number': '2',
        'standard_or_optional_designation': 'm',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        'q': value.get('assigning_agency'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '2': value.get('edition_number'),
        'm': value.get('standard_or_optional_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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


@to_marc21_liberal.over('083', '^additional_dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_dewey_decimal_classification_number(self, key, value):
    """Reverse - Additional Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'table_identification': 'z',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
        'edition_number': '2',
        'standard_or_optional_designation': 'm',
        'classification_number_ending_number_of_span': 'c',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '2': value.get('edition_number'),
        'm': value.get('standard_or_optional_designation'),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        'q': value.get('assigning_agency'),
        '$ind1': '7' if 'type_of_edition' in value and
        not indicator_map1.get(value.get('type_of_edition')) and
        value.get('type_of_edition') == value.get('edition_number') and
        field_map.get('type_of_edition') in order
        else indicator_map1.get(value.get('type_of_edition'), value.get('type_of_edition', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('084', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""
    field_map = {
        'linkage': '6',
        'item_number': 'b',
        'assigning_agency': 'q',
        'classification_number': 'a',
        'number_source': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('item_number'),
        'q': value.get('assigning_agency'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '2': value.get('number_source'),
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


@to_marc21_liberal.over('085', '^synthesized_classification_number_components$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_synthesized_classification_number_components(self, key, value):
    """Reverse - Synthesized Classification Number Components."""
    field_map = {
        'root_number': 'r',
        'digits_added_from_classification_number_in_schedule_or_external_table': 's',
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': 'a',
        'table_identification': 'z',
        'facet_designator': 'f',
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': 'v',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'number_being_analyzed': 'u',
        'base_number': 'b',
        'classification_number_ending_number_of_span': 'c',
        'digits_added_from_internal_subarrangement_or_add_table': 't',
        'table_identification_internal_subarrangement_or_add_table': 'w',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'r': utils.reverse_force_list(
            value.get('root_number')
        ),
        's': utils.reverse_force_list(
            value.get('digits_added_from_classification_number_in_schedule_or_external_table')
        ),
        'a': utils.reverse_force_list(
            value.get('number_where_instructions_are_found_single_number_or_beginning_number_of_span')
        ),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        'f': utils.reverse_force_list(
            value.get('facet_designator')
        ),
        'v': utils.reverse_force_list(
            value.get('number_in_internal_subarrangement_or_add_table_where_instructions_are_found')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'u': utils.reverse_force_list(
            value.get('number_being_analyzed')
        ),
        'b': utils.reverse_force_list(
            value.get('base_number')
        ),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        't': utils.reverse_force_list(
            value.get('digits_added_from_internal_subarrangement_or_add_table')
        ),
        'w': utils.reverse_force_list(
            value.get('table_identification_internal_subarrangement_or_add_table')
        ),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('086', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    indicator_map1 = {"Government of Canada Publications: Outline of Classification": "1", "Source specified in subfield $2": "_", "Superintendent of Documents Classification System": "0"}
    field_map = {
        'linkage': '6',
        'number_source': '2',
        'canceled_invalid_classification_number': 'z',
        'field_link_and_sequence_number': '8',
        'classification_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['number_source', 'None'])

    if (indicator_map1.get(value.get('number_source'), '7') != '7' or len(value.get('number_source', '')) == 1) and\
            field_map.get('number_source'):
        order.remove(field_map.get('number_source'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('number_source'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('classification_number'),
        '$ind1': '_' if 'number_source' in value and
        not indicator_map1.get(value.get('number_source')) and
        value.get('number_source') == value.get('number_source') and
        field_map.get('number_source') in order
        else indicator_map1.get(value.get('number_source'), value.get('number_source', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('088', '^report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_report_number(self, key, value):
    """Reverse - Report Number."""
    field_map = {
        'linkage': '6',
        'canceled_invalid_report_number': 'z',
        'field_link_and_sequence_number': '8',
        'report_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_report_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('report_number'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
