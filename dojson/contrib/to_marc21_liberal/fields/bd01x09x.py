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
        'lc_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'nucmc_control_number': 'b',
        'canceled_invalid_lc_control_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('lc_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('nucmc_control_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_lc_control_number')
        ),
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
        'number': 'a',
        'status': 'e',
        'linkage': '6',
        'type_of_number': 'c',
        'party_to_document': 'f',
        'date': 'd',
        'field_link_and_sequence_number': '8',
        'country': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('number'),
        'e': utils.reverse_force_list(
            value.get('status')
        ),
        '6': value.get('linkage'),
        'c': value.get('type_of_number'),
        'f': utils.reverse_force_list(
            value.get('party_to_document')
        ),
        'd': utils.reverse_force_list(
            value.get('date')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('country'),
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
        'national_bibliography_number': 'a',
        'linkage': '6',
        'canceled_invalid_national_bibliography_number': 'z',
        'field_link_and_sequence_number': '8',
        'source': '2',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('national_bibliography_number')
        ),
        '6': value.get('linkage'),
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
        'record_control_number': 'a',
        'source': '2',
        'canceled_invalid_control_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['national_bibliographic_agency', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_control_number'),
        '2': value.get('source'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'copyright_or_legal_deposit_number': 'a',
        'display_text': 'i',
        'linkage': '6',
        'canceled_invalid_copyright_or_legal_deposit_number': 'z',
        'field_link_and_sequence_number': '8',
        'date': 'd',
        'source': '2',
        'assigning_agency': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'display_constant_controller'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('copyright_or_legal_deposit_number')
        ),
        'i': value.get('display_text'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_copyright_or_legal_deposit_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('date'),
        '2': value.get('source'),
        'b': value.get('assigning_agency'),
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
        'copyright_article_fee_code_nr': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('copyright_article_fee_code_nr')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
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
        'international_standard_book_number': 'a',
        'linkage': '6',
        'terms_of_availability': 'c',
        'canceled_invalid_isbn': 'z',
        'field_link_and_sequence_number': '8',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_book_number'),
        '6': value.get('linkage'),
        'c': value.get('terms_of_availability'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_isbn')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
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
        'international_standard_serial_number': 'a',
        'canceled_issn_l': 'm',
        'linkage': '6',
        'canceled_issn': 'z',
        'field_link_and_sequence_number': '8',
        'source': '2',
        'incorrect_issn': 'y',
        'issn_l': 'l',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level_of_international_interest', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('international_standard_serial_number'),
        'm': utils.reverse_force_list(
            value.get('canceled_issn_l')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_issn')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('source'),
        'y': utils.reverse_force_list(
            value.get('incorrect_issn')
        ),
        'l': value.get('issn_l'),
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
        'standard_number_or_code': 'a',
        'canceled_invalid_standard_number_or_code': 'z',
        'linkage': '6',
        'terms_of_availability': 'c',
        'field_link_and_sequence_number': '8',
        'additional_codes_following_the_standard_number_or_code': 'd',
        'source_of_number_or_code': '2',
        'qualifying_information': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_standard_number_or_code', 'difference_indicator'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('standard_number_or_code'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_standard_number_or_code')
        ),
        '6': value.get('linkage'),
        'c': value.get('terms_of_availability'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('additional_codes_following_the_standard_number_or_code'),
        '2': value.get('source_of_number_or_code'),
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
        'overseas_acquisition_number': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('overseas_acquisition_number')
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


@to_marc21_liberal.over('026', '^fingerprint_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_fingerprint_identifier(self, key, value):
    """Reverse - Fingerprint Identifier."""
    field_map = {
        'first_and_second_groups_of_characters': 'a',
        'unparsed_fingerprint': 'e',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'field_link_and_sequence_number': '8',
        'number_of_volume_or_part': 'd',
        'source': '2',
        'third_and_fourth_groups_of_characters': 'b',
        'date': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('first_and_second_groups_of_characters'),
        'e': value.get('unparsed_fingerprint'),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('number_of_volume_or_part')
        ),
        '2': value.get('source'),
        'b': value.get('third_and_fourth_groups_of_characters'),
        'c': value.get('date'),
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
        'standard_technical_report_number': 'a',
        'field_link_and_sequence_number': '8',
        'qualifying_information': 'q',
        'linkage': '6',
        'canceled_invalid_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('standard_technical_report_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_number')
        ),
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
        'publisher_number': 'a',
        'field_link_and_sequence_number': '8',
        'source': 'b',
        'qualifying_information': 'q',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_publisher_number', 'note_added_entry_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('publisher_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source'),
        'q': utils.reverse_force_list(
            value.get('qualifying_information')
        ),
        '6': value.get('linkage'),
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
        'coden': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'canceled_invalid_coden': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('coden'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_coden')
        ),
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
        'voice_instrument': 'm',
        'role': 'e',
        'number_of_excerpt': 'c',
        'system_code': '2',
        'link_text': 'y',
        'key_or_mode': 'r',
        'musical_notation': 'p',
        'key_signature': 'n',
        'number_of_work': 'a',
        'text_incipit': 't',
        'clef': 'g',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'public_note': 'z',
        'coded_validity_note': 's',
        'caption_or_heading': 'd',
        'field_link_and_sequence_number': '8',
        'number_of_movement': 'b',
        'general_note': 'q',
        'time_signature': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'm': value.get('voice_instrument'),
        'e': value.get('role'),
        'c': value.get('number_of_excerpt'),
        '2': value.get('system_code'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'r': value.get('key_or_mode'),
        'p': value.get('musical_notation'),
        'n': value.get('key_signature'),
        'a': value.get('number_of_work'),
        't': utils.reverse_force_list(
            value.get('text_incipit')
        ),
        'g': value.get('clef'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        's': utils.reverse_force_list(
            value.get('coded_validity_note')
        ),
        'd': utils.reverse_force_list(
            value.get('caption_or_heading')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_movement'),
        'q': utils.reverse_force_list(
            value.get('general_note')
        ),
        'o': value.get('time_signature'),
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
        'postal_registration_number': 'a',
        'field_link_and_sequence_number': '8',
        'source_agency_assigning_number': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('postal_registration_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
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
        'formatted_date_time': 'a',
        'linkage': '6',
        'geographic_classification_subarea_code': 'c',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'authority_record_control_number': '0',
        'geographic_classification_area_code': 'b',
        'place_of_event': 'p',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_date_in_subfield_a', 'type_of_event'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('formatted_date_time')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_area_code')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
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
        'coordinates_easternmost_longitude': 'e',
        'declination_northern_limit': 'j',
        'materials_specified': '3',
        'ending_date': 'y',
        'right_ascension_eastern_limit': 'm',
        'g_ring_longitude': 't',
        'linkage': '6',
        'name_of_extraterrestrial_body': 'z',
        'g_ring_latitude': 's',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'constant_ratio_linear_horizontal_scale': 'b',
        'angular_scale': 'h',
        'constant_ratio_linear_vertical_scale': 'c',
        'coordinates_northernmost_latitude': 'f',
        'source': '2',
        'distance_from_earth': 'r',
        'equinox': 'p',
        'right_ascension_western_limit': 'n',
        'category_of_scale': 'a',
        'coordinates_southernmost_latitude': 'g',
        'beginning_date': 'x',
        'declination_southern_limit': 'k',
        'coordinates_westernmost_longitude': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_scale', 'type_of_ring'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': value.get('coordinates_easternmost_longitude'),
        'j': value.get('declination_northern_limit'),
        '3': value.get('materials_specified'),
        'y': value.get('ending_date'),
        'm': value.get('right_ascension_eastern_limit'),
        't': utils.reverse_force_list(
            value.get('g_ring_longitude')
        ),
        '6': value.get('linkage'),
        'z': value.get('name_of_extraterrestrial_body'),
        's': utils.reverse_force_list(
            value.get('g_ring_latitude')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('constant_ratio_linear_horizontal_scale')
        ),
        'h': utils.reverse_force_list(
            value.get('angular_scale')
        ),
        'c': utils.reverse_force_list(
            value.get('constant_ratio_linear_vertical_scale')
        ),
        'f': value.get('coordinates_northernmost_latitude'),
        '2': value.get('source'),
        'r': value.get('distance_from_earth'),
        'p': value.get('equinox'),
        'n': value.get('right_ascension_western_limit'),
        'a': value.get('category_of_scale'),
        'g': value.get('coordinates_southernmost_latitude'),
        'x': value.get('beginning_date'),
        'k': value.get('declination_southern_limit'),
        'd': value.get('coordinates_westernmost_longitude'),
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
        'system_control_number': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'canceled_invalid_control_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('system_control_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_control_number')
        ),
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
        'original_study_number': 'a',
        'field_link_and_sequence_number': '8',
        'source_agency_assigning_number': 'b',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_study_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_agency_assigning_number'),
        '6': value.get('linkage'),
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
        'stock_number': 'a',
        'additional_format_characteristics': 'g',
        'linkage': '6',
        'institution_to_which_field_applies': '5',
        'form_of_issue': 'f',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'source_of_stock_number_acquisition': 'b',
        'note': 'n',
        'terms_of_availability': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['source_of_acquisition_sequence', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('stock_number'),
        'g': utils.reverse_force_list(
            value.get('additional_format_characteristics')
        ),
        '6': value.get('linkage'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'f': utils.reverse_force_list(
            value.get('form_of_issue')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('source_of_stock_number_acquisition'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'c': utils.reverse_force_list(
            value.get('terms_of_availability')
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
        'record_content_licensor': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('record_content_licensor'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
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
        'original_cataloging_agency': 'a',
        'description_conventions': 'e',
        'linkage': '6',
        'transcribing_agency': 'c',
        'modifying_agency': 'd',
        'field_link_and_sequence_number': '8',
        'language_of_cataloging': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('original_cataloging_agency'),
        'e': utils.reverse_force_list(
            value.get('description_conventions')
        ),
        '6': value.get('linkage'),
        'c': value.get('transcribing_agency'),
        'd': utils.reverse_force_list(
            value.get('modifying_agency')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('language_of_cataloging'),
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
        'language_code_of_librettos': 'e',
        'language_code_of_original': 'h',
        'language_code_of_table_of_contents': 'f',
        'language_code_of_subtitles_or_captions': 'j',
        'source_of_code': '2',
        'language_code_of_original_libretto': 'n',
        'language_code_of_text_sound_track_or_separate_title': 'a',
        'language_code_of_accompanying_material_other_than_librettos': 'g',
        'linkage': '6',
        'language_code_of_sung_or_spoken_text': 'd',
        'field_link_and_sequence_number': '8',
        'language_code_of_summary_or_abstract': 'b',
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
        'e': utils.reverse_force_list(
            value.get('language_code_of_librettos')
        ),
        'h': utils.reverse_force_list(
            value.get('language_code_of_original')
        ),
        'f': utils.reverse_force_list(
            value.get('language_code_of_table_of_contents')
        ),
        'j': utils.reverse_force_list(
            value.get('language_code_of_subtitles_or_captions')
        ),
        '2': value.get('source_of_code'),
        'n': utils.reverse_force_list(
            value.get('language_code_of_original_libretto')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code_of_text_sound_track_or_separate_title')
        ),
        'g': utils.reverse_force_list(
            value.get('language_code_of_accompanying_material_other_than_librettos')
        ),
        '6': value.get('linkage'),
        'd': utils.reverse_force_list(
            value.get('language_code_of_sung_or_spoken_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('language_code_of_summary_or_abstract')
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

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

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
        'geographic_area_code': 'a',
        'linkage': '6',
        'iso_code': 'c',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'local_gac_code': 'b',
        'source_of_local_code': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('geographic_area_code')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('iso_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'b': utils.reverse_force_list(
            value.get('local_gac_code')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_code')
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
        'marc_country_code': 'a',
        'linkage': '6',
        'iso_country_code': 'c',
        'field_link_and_sequence_number': '8',
        'source_of_local_subentity_code': '2',
        'local_subentity_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('marc_country_code')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('iso_country_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source_of_local_subentity_code')
        ),
        'b': utils.reverse_force_list(
            value.get('local_subentity_code')
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
        'time_period_code': 'a',
        'field_link_and_sequence_number': '8',
        'formatted_9999_bc_through_ce_time_period': 'b',
        'linkage': '6',
        'formatted_pre_9999_bc_time_period': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period_in_subfield_b_or_c', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('formatted_9999_bc_through_ce_time_period')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('formatted_pre_9999_bc_time_period')
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
        'beginning_of_date_valid': 'm',
        'date_2_ce_date': 'e',
        'date_1_ce_date': 'c',
        'date_resource_modified': 'j',
        'source_of_date': '2',
        'ending_date_for_aggregated_content': 'p',
        'end_of_date_valid': 'n',
        'type_of_date_code': 'a',
        'linkage': '6',
        'single_or_starting_date_for_aggregated_content': 'o',
        'date_2_bc_date': 'd',
        'field_link_and_sequence_number': '8',
        'date_1_bc_date': 'b',
        'ending_date_created': 'l',
        'beginning_or_single_date_created': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'm': value.get('beginning_of_date_valid'),
        'e': value.get('date_2_ce_date'),
        'c': value.get('date_1_ce_date'),
        'j': value.get('date_resource_modified'),
        '2': value.get('source_of_date'),
        'p': value.get('ending_date_for_aggregated_content'),
        'n': value.get('end_of_date_valid'),
        'a': value.get('type_of_date_code'),
        '6': value.get('linkage'),
        'o': value.get('single_or_starting_date_for_aggregated_content'),
        'd': value.get('date_2_bc_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('date_1_bc_date'),
        'l': value.get('ending_date_created'),
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
        'form_of_musical_composition_code': 'a',
        'source_of_code': '2',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('form_of_musical_composition_code')
        ),
        '2': value.get('source_of_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'performer_or_ensemble': 'a',
        'source_of_code': '2',
        'soloist': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if (indicator_map2.get(value.get('source_of_code'), '7') != '7' or len(value.get('source_of_code', '')) == 1) and\
            field_map.get('source_of_code'):
        order.remove(field_map.get('source_of_code'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('performer_or_ensemble')
        ),
        '2': value.get('source_of_code'),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'classification_number': 'a',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_lc_collection', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '6': value.get('linkage'),
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
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
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
        'geographic_classification_area_code': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'populated_place_name': 'd',
        'code_source': '2',
        'geographic_classification_subarea_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['code_source', 'None'])

    if (indicator_map1.get(value.get('code_source'), '7') != '7' or len(value.get('code_source', '')) == 1) and\
            field_map.get('code_source'):
        order.remove(field_map.get('code_source'))

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('geographic_classification_area_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('populated_place_name')
        ),
        '2': value.get('code_source'),
        'b': utils.reverse_force_list(
            value.get('geographic_classification_subarea_code')
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
        'classification_number': 'a',
        'source_of_call_class_number': '2',
        'item_number': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_lac_collection', 'type_completeness_source_of_class_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        '2': value.get('source_of_call_class_number'),
        'b': value.get('item_number'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'classification_number_r': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_nlm_collection', 'source_of_call_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number_r')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
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
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        'c': value.get('copy_information'),
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
        'primary_g0_character_set': 'a',
        'primary_g1_character_set': 'b',
        'alternate_g0_or_g1_character_set': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('primary_g0_character_set'),
        'b': value.get('primary_g1_character_set'),
        'c': utils.reverse_force_list(
            value.get('alternate_g0_or_g1_character_set')
        ),
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
        'classification_number': 'a',
        'field_link_and_sequence_number_r': '8',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['existence_in_nal_collection', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')
        ),
        'b': value.get('item_number'),
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
        'classification_number': 'a',
        'field_link_and_sequence_number': '8',
        'item_number': 'b',
        'copy_information': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('item_number'),
        'c': utils.reverse_force_list(
            value.get('copy_information')
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
        'subject_category_code': 'a',
        'source': '2',
        'subject_category_code_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'code_source'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('subject_category_code'),
        '2': value.get('source'),
        'x': utils.reverse_force_list(
            value.get('subject_category_code_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'gpo_item_number': 'a',
        'field_link_and_sequence_number': '8',
        'canceled_invalid_gpo_item_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('gpo_item_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_gpo_item_number')
        ),
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
        'universal_decimal_classification_number': 'a',
        'common_auxiliary_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'edition_identifier': '2',
        'item_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('universal_decimal_classification_number'),
        'x': utils.reverse_force_list(
            value.get('common_auxiliary_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_identifier'),
        'b': value.get('item_number'),
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
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'edition_number': '2',
        'item_number': 'b',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'source_of_classification_number'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_number'),
        'b': value.get('item_number'),
        'q': value.get('assigning_agency'),
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
        'classification_number': 'a',
        'standard_or_optional_designation': 'm',
        'table_identification': 'z',
        'linkage': '6',
        'classification_number_ending_number_of_span': 'c',
        'field_link_and_sequence_number': '8',
        'edition_number': '2',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_edition', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        'm': value.get('standard_or_optional_designation'),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('edition_number'),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
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
        'classification_number': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'number_source': '2',
        'item_number': 'b',
        'assigning_agency': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('classification_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': value.get('number_source'),
        'b': value.get('item_number'),
        'q': value.get('assigning_agency'),
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
        'table_identification_internal_subarrangement_or_add_table': 'w',
        'number_being_analyzed': 'u',
        'classification_number_ending_number_of_span': 'c',
        'facet_designator': 'f',
        'table_sequence_number_for_internal_subarrangement_or_add_table': 'y',
        'root_number': 'r',
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': 'v',
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': 'a',
        'digits_added_from_internal_subarrangement_or_add_table': 't',
        'linkage': '6',
        'digits_added_from_classification_number_in_schedule_or_external_table': 's',
        'table_identification': 'z',
        'field_link_and_sequence_number': '8',
        'base_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': utils.reverse_force_list(
            value.get('table_identification_internal_subarrangement_or_add_table')
        ),
        'u': utils.reverse_force_list(
            value.get('number_being_analyzed')
        ),
        'c': utils.reverse_force_list(
            value.get('classification_number_ending_number_of_span')
        ),
        'f': utils.reverse_force_list(
            value.get('facet_designator')
        ),
        'y': utils.reverse_force_list(
            value.get('table_sequence_number_for_internal_subarrangement_or_add_table')
        ),
        'r': utils.reverse_force_list(
            value.get('root_number')
        ),
        'v': utils.reverse_force_list(
            value.get('number_in_internal_subarrangement_or_add_table_where_instructions_are_found')
        ),
        'a': utils.reverse_force_list(
            value.get('number_where_instructions_are_found_single_number_or_beginning_number_of_span')
        ),
        't': utils.reverse_force_list(
            value.get('digits_added_from_internal_subarrangement_or_add_table')
        ),
        '6': value.get('linkage'),
        's': utils.reverse_force_list(
            value.get('digits_added_from_classification_number_in_schedule_or_external_table')
        ),
        'z': utils.reverse_force_list(
            value.get('table_identification')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('base_number')
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
        'classification_number': 'a',
        'number_source': '2',
        'linkage': '6',
        'canceled_invalid_classification_number': 'z',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['number_source', 'None'])

    if (indicator_map1.get(value.get('number_source'), '7') != '7' or len(value.get('number_source', '')) == 1) and\
            field_map.get('number_source'):
        order.remove(field_map.get('number_source'))

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('classification_number'),
        '2': value.get('number_source'),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_classification_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
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
        'report_number': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'canceled_invalid_report_number': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('report_number'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'z': utils.reverse_force_list(
            value.get('canceled_invalid_report_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
