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

from ..model import marc21_liberal


@marc21_liberal.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'lc_control_number',
        'z': 'canceled_invalid_lc_control_number',
        'b': 'nucmc_control_number',
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
        'lc_control_number': value.get('a'),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
        'nucmc_control_number': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('patent_control_information', '^013..')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    """Patent Control Information."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'number',
        'd': 'date',
        'f': 'party_to_document',
        'e': 'status',
        'c': 'type_of_number',
        'b': 'country',
        '6': 'linkage',
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
        'number': value.get('a'),
        'date': utils.force_list(
            value.get('d')
        ),
        'party_to_document': utils.force_list(
            value.get('f')
        ),
        'status': utils.force_list(
            value.get('e')
        ),
        'type_of_number': value.get('c'),
        'country': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('national_bibliography_number', '^015..')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    """National Bibliography Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'national_bibliography_number',
        'z': 'canceled_invalid_national_bibliography_number',
        '2': 'source',
        'q': 'qualifying_information',
        '6': 'linkage',
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
        'national_bibliography_number': utils.force_list(
            value.get('a')
        ),
        'canceled_invalid_national_bibliography_number': utils.force_list(
            value.get('z')
        ),
        'source': value.get('2'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('national_bibliographic_agency_control_number', '^016..')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    indicator_map1 = {"7": "Source specified in subfield $2", "_": "Library and Archives Canada"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'record_control_number',
        'z': 'canceled_invalid_control_number',
        '2': 'source',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('national_bibliographic_agency')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': value.get('a'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'source': value.get('2'),
        'national_bibliographic_agency': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('copyright_or_legal_deposit_number', '^017..')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
    indicator_map2 = {"8": "No display constant generated", "_": "Copyright or legal deposit number"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'copyright_or_legal_deposit_number',
        'd': 'date',
        'i': 'display_text',
        '2': 'source',
        'b': 'assigning_agency',
        'z': 'canceled_invalid_copyright_or_legal_deposit_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('display_constant_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copyright_or_legal_deposit_number': utils.force_list(
            value.get('a')
        ),
        'date': value.get('d'),
        'display_text': value.get('i'),
        'source': value.get('2'),
        'assigning_agency': value.get('b'),
        'canceled_invalid_copyright_or_legal_deposit_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        'display_constant_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('copyright_article_fee_code', '^018..')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    """Copyright Article-Fee Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'copyright_article_fee_code_nr',
        '6': 'linkage',
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
        'copyright_article_fee_code_nr': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'international_standard_book_number',
        'z': 'canceled_invalid_isbn',
        'q': 'qualifying_information',
        'c': 'terms_of_availability',
        '6': 'linkage',
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
        'international_standard_book_number': value.get('a'),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'terms_of_availability': value.get('c'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('international_standard_serial_number', '^022..')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    indicator_map1 = {"0": "Continuing resource of international interest", "1": "Continuing resource not of international interest", "_": "No level specified"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'international_standard_serial_number',
        'z': 'canceled_issn',
        '2': 'source',
        'y': 'incorrect_issn',
        'm': 'canceled_issn_l',
        '6': 'linkage',
        'l': 'issn_l',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('level_of_international_interest')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_serial_number': value.get('a'),
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'source': value.get('2'),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'linkage': value.get('6'),
        'issn_l': value.get('l'),
        'level_of_international_interest': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('other_standard_identifier', '^024..')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {"0": "International Standard Recording Code", "1": "Universal Product Code", "2": "International Standard Music Number", "3": "International Article Number", "4": "Serial Item and Contribution Identifier", "7": "Source specified in subfield $2", "8": "Unspecified type of standard number or code"}
    indicator_map2 = {"0": "No difference", "1": "Difference", "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'standard_number_or_code',
        'd': 'additional_codes_following_the_standard_number_or_code',
        'z': 'canceled_invalid_standard_number_or_code',
        '2': 'source_of_number_or_code',
        'q': 'qualifying_information',
        'c': 'terms_of_availability',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_standard_number_or_code')

    if key[4] != '_':
        order.append('difference_indicator')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'standard_number_or_code': value.get('a'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'source_of_number_or_code': value.get('2'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'terms_of_availability': value.get('c'),
        'linkage': value.get('6'),
        'type_of_standard_number_or_code': indicator_map1.get(key[3], key[3]),
        'difference_indicator': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('overseas_acquisition_number', '^025..')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    """Overseas Acquisition Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'overseas_acquisition_number',
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
        'overseas_acquisition_number': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('fingerprint_identifier', '^026..')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    """Fingerprint Identifier."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'first_and_second_groups_of_characters',
        'd': 'number_of_volume_or_part',
        '2': 'source',
        'e': 'unparsed_fingerprint',
        'c': 'date',
        'b': 'third_and_fourth_groups_of_characters',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
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
        'first_and_second_groups_of_characters': value.get('a'),
        'number_of_volume_or_part': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
        'unparsed_fingerprint': value.get('e'),
        'date': value.get('c'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'standard_technical_report_number',
        'z': 'canceled_invalid_number',
        '6': 'linkage',
        'q': 'qualifying_information',
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
        'standard_technical_report_number': value.get('a'),
        'canceled_invalid_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('publisher_number', '^028..')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    """Publisher Number."""
    indicator_map1 = {"0": "Issue number", "1": "Matrix number", "2": "Plate number", "3": "Other music number", "4": "Videorecording number", "5": "Other publisher number"}
    indicator_map2 = {"0": "No note, no added entry", "1": "Note, added entry", "2": "Note, no added entry", "3": "No note, added entry"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'publisher_number',
        'b': 'source',
        '6': 'linkage',
        'q': 'qualifying_information',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_publisher_number')

    if key[4] != '_':
        order.append('note_added_entry_controller')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'publisher_number': value.get('a'),
        'source': value.get('b'),
        'linkage': value.get('6'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'type_of_publisher_number': indicator_map1.get(key[3], key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('coden_designation', '^030..')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    """CODEN Designation."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'coden',
        'z': 'canceled_invalid_coden',
        '6': 'linkage',
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
        'coden': value.get('a'),
        'canceled_invalid_coden': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'number_of_movement',
        'u': 'uniform_resource_identifier',
        'y': 'link_text',
        'e': 'role',
        'z': 'public_note',
        'o': 'time_signature',
        'n': 'key_signature',
        'g': 'clef',
        '6': 'linkage',
        'r': 'key_or_mode',
        'a': 'number_of_work',
        'd': 'caption_or_heading',
        't': 'text_incipit',
        '2': 'system_code',
        's': 'coded_validity_note',
        'p': 'musical_notation',
        'c': 'number_of_excerpt',
        'm': 'voice_instrument',
        'q': 'general_note',
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
        'number_of_movement': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'role': value.get('e'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'time_signature': value.get('o'),
        'key_signature': value.get('n'),
        'clef': value.get('g'),
        'linkage': value.get('6'),
        'key_or_mode': value.get('r'),
        'number_of_work': value.get('a'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'system_code': value.get('2'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'musical_notation': value.get('p'),
        'number_of_excerpt': value.get('c'),
        'voice_instrument': value.get('m'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('postal_registration_number', '^032..')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    """Postal Registration Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'postal_registration_number',
        'b': 'source_agency_assigning_number',
        '6': 'linkage',
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
        'postal_registration_number': value.get('a'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('date_time_and_place_of_an_event', '^033..')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    """Date/Time and Place of an Event."""
    indicator_map1 = {"0": "Single date", "1": "Multiple single dates", "2": "Range of dates", "_": "No date information"}
    indicator_map2 = {"0": "Capture", "1": "Broadcast", "2": "Finding", "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'formatted_date_time',
        '2': 'source_of_term',
        'c': 'geographic_classification_subarea_code',
        '3': 'materials_specified',
        '0': 'authority_record_control_number',
        'b': 'geographic_classification_area_code',
        'p': 'place_of_event',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_date_in_subfield_a')

    if key[4] != '_':
        order.append('type_of_event')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'formatted_date_time': utils.force_list(
            value.get('a')
        ),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'geographic_classification_area_code': utils.force_list(
            value.get('b')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'type_of_date_in_subfield_a': indicator_map1.get(key[3], key[3]),
        'type_of_event': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('coded_cartographic_mathematical_data', '^034..')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map1 = {"0": "Scale indeterminable/No scale recorded", "1": "Single scale", "3": "Range of scales"}
    indicator_map2 = {"0": "Outer ring", "1": "Exclusion ring", "_": "Not applicable"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'x': 'beginning_date',
        'y': 'ending_date',
        'e': 'coordinates_easternmost_longitude',
        'n': 'right_ascension_western_limit',
        'a': 'category_of_scale',
        'c': 'constant_ratio_linear_vertical_scale',
        't': 'g_ring_longitude',
        's': 'g_ring_latitude',
        'p': 'equinox',
        'j': 'declination_northern_limit',
        'h': 'angular_scale',
        'g': 'coordinates_southernmost_latitude',
        'd': 'coordinates_westernmost_longitude',
        '6': 'linkage',
        'b': 'constant_ratio_linear_horizontal_scale',
        'r': 'distance_from_earth',
        'z': 'name_of_extraterrestrial_body',
        '2': 'source',
        '3': 'materials_specified',
        '0': 'authority_record_control_number_or_standard_number',
        'm': 'right_ascension_eastern_limit',
        'k': 'declination_southern_limit',
        'f': 'coordinates_northernmost_latitude',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_scale')

    if key[4] != '_':
        order.append('type_of_ring')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'beginning_date': value.get('x'),
        'ending_date': value.get('y'),
        'coordinates_easternmost_longitude': value.get('e'),
        'right_ascension_western_limit': value.get('n'),
        'category_of_scale': value.get('a'),
        'constant_ratio_linear_vertical_scale': utils.force_list(
            value.get('c')
        ),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'equinox': value.get('p'),
        'declination_northern_limit': value.get('j'),
        'angular_scale': utils.force_list(
            value.get('h')
        ),
        'coordinates_southernmost_latitude': value.get('g'),
        'coordinates_westernmost_longitude': value.get('d'),
        'linkage': value.get('6'),
        'constant_ratio_linear_horizontal_scale': utils.force_list(
            value.get('b')
        ),
        'distance_from_earth': value.get('r'),
        'name_of_extraterrestrial_body': value.get('z'),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'right_ascension_eastern_limit': value.get('m'),
        'declination_southern_limit': value.get('k'),
        'coordinates_northernmost_latitude': value.get('f'),
        'type_of_scale': indicator_map1.get(key[3], key[3]),
        'type_of_ring': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'system_control_number',
        'z': 'canceled_invalid_control_number',
        '6': 'linkage',
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
        'system_control_number': value.get('a'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('original_study_number_for_computer_data_files', '^036..')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    """Original Study Number for Computer Data Files."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'original_study_number',
        'b': 'source_agency_assigning_number',
        '6': 'linkage',
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
        'original_study_number': value.get('a'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('source_of_acquisition', '^037..')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    """Source of Acquisition."""
    indicator_map1 = {"2": "Intervening", "3": "Current/Latest", "_": "Not applicable/No information provided/Earliest"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'stock_number',
        'f': 'form_of_issue',
        '3': 'materials_specified',
        'c': 'terms_of_availability',
        'b': 'source_of_stock_number_acquisition',
        'n': 'note',
        'g': 'additional_format_characteristics',
        '5': 'institution_to_which_field_applies',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('source_of_acquisition_sequence')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'stock_number': value.get('a'),
        'form_of_issue': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'terms_of_availability': utils.force_list(
            value.get('c')
        ),
        'source_of_stock_number_acquisition': value.get('b'),
        'note': utils.force_list(
            value.get('n')
        ),
        'additional_format_characteristics': utils.force_list(
            value.get('g')
        ),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'source_of_acquisition_sequence': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('record_content_licensor', '^038..')
@utils.filter_values
def record_content_licensor(self, key, value):
    """Record Content Licensor."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'record_content_licensor',
        '6': 'linkage',
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
        'record_content_licensor': value.get('a'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'original_cataloging_agency',
        'd': 'modifying_agency',
        'e': 'description_conventions',
        'c': 'transcribing_agency',
        'b': 'language_of_cataloging',
        '6': 'linkage',
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
        'original_cataloging_agency': value.get('a'),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'transcribing_agency': value.get('c'),
        'language_of_cataloging': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('language_code', '^041..')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    """Language Code."""
    indicator_map1 = {"0": "Item not a translation/does not include a translation", "1": "Item is or includes a translation", "_": "No information provided"}
    indicator_map2 = {"7": "Source specified in subfield $2", "_": "MARC language code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'language_code_of_summary_or_abstract',
        'e': 'language_code_of_librettos',
        'h': 'language_code_of_original',
        'g': 'language_code_of_accompanying_material_other_than_librettos',
        '6': 'linkage',
        'k': 'language_code_of_intermediate_translations',
        'a': 'language_code_of_text_sound_track_or_separate_title',
        'd': 'language_code_of_sung_or_spoken_text',
        '2': 'source_of_code',
        'n': 'language_code_of_original_libretto',
        'm': 'language_code_of_original_accompanying_materials_other_than_librettos',
        'j': 'language_code_of_subtitles_or_captions',
        'f': 'language_code_of_table_of_contents',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('translation_indication')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_code')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'language_code_of_summary_or_abstract': utils.force_list(
            value.get('b')
        ),
        'language_code_of_librettos': utils.force_list(
            value.get('e')
        ),
        'language_code_of_original': utils.force_list(
            value.get('h')
        ),
        'language_code_of_accompanying_material_other_than_librettos': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'language_code_of_intermediate_translations': utils.force_list(
            value.get('k')
        ),
        'language_code_of_text_sound_track_or_separate_title': utils.force_list(
            value.get('a')
        ),
        'language_code_of_sung_or_spoken_text': utils.force_list(
            value.get('d')
        ),
        'language_code_of_original_libretto': utils.force_list(
            value.get('n')
        ),
        'language_code_of_original_accompanying_materials_other_than_librettos': utils.force_list(
            value.get('m')
        ),
        'language_code_of_subtitles_or_captions': utils.force_list(
            value.get('j')
        ),
        'language_code_of_table_of_contents': utils.force_list(
            value.get('f')
        ),
        'translation_indication': indicator_map1.get(key[3], key[3]),
        'source_of_code': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('authentication_code', '^042..')
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


@marc21_liberal.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'geographic_area_code',
        '2': 'source_of_local_code',
        'c': 'iso_code',
        '0': 'authority_record_control_number_or_standard_number',
        'b': 'local_gac_code',
        '6': 'linkage',
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
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'iso_code': utils.force_list(
            value.get('c')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('country_of_publishing_producing_entity_code', '^044..')
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    """Country of Publishing/Producing Entity Code."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'marc_country_code',
        '2': 'source_of_local_subentity_code',
        'c': 'iso_country_code',
        'b': 'local_subentity_code',
        '6': 'linkage',
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
        'marc_country_code': utils.force_list(
            value.get('a')
        ),
        'source_of_local_subentity_code': utils.force_list(
            value.get('2')
        ),
        'iso_country_code': utils.force_list(
            value.get('c')
        ),
        'local_subentity_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('time_period_of_content', '^045..')
@utils.filter_values
def time_period_of_content(self, key, value):
    """Time Period of Content."""
    indicator_map1 = {"0": "Single date/time", "1": "Multiple single dates/times", "2": "Range of dates/times", "_": "Subfield $b or $c not present"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'time_period_code',
        'b': 'formatted_9999_bc_through_ce_time_period',
        'c': 'formatted_pre_9999_bc_time_period',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_time_period_in_subfield_b_or_c')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
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
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'date_1_bc_date',
        'e': 'date_2_ce_date',
        'o': 'single_or_starting_date_for_aggregated_content',
        'n': 'end_of_date_valid',
        '6': 'linkage',
        'l': 'ending_date_created',
        'k': 'beginning_or_single_date_created',
        'a': 'type_of_date_code',
        'd': 'date_2_bc_date',
        '2': 'source_of_date',
        'p': 'ending_date_for_aggregated_content',
        'c': 'date_1_ce_date',
        'm': 'beginning_of_date_valid',
        'j': 'date_resource_modified',
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
        'date_1_bc_date': value.get('b'),
        'date_2_ce_date': value.get('e'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'end_of_date_valid': value.get('n'),
        'linkage': value.get('6'),
        'ending_date_created': value.get('l'),
        'beginning_or_single_date_created': value.get('k'),
        'type_of_date_code': value.get('a'),
        'date_2_bc_date': value.get('d'),
        'source_of_date': value.get('2'),
        'ending_date_for_aggregated_content': value.get('p'),
        'date_1_ce_date': value.get('c'),
        'beginning_of_date_valid': value.get('m'),
        'date_resource_modified': value.get('j'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('form_of_musical_composition_code', '^047..')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    """Form of Musical Composition Code."""
    indicator_map2 = {"7": "Source specified in subfield $2", "_": "MARC musical composition code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'form_of_musical_composition_code',
        '2': 'source_of_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_code')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'form_of_musical_composition_code': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_code': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('number_of_musical_instruments_or_voices_code', '^048..')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    """Number of Musical Instruments or Voices Code."""
    indicator_map2 = {"7": "Source specified in subfield $2", "_": "MARC code"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'performer_or_ensemble',
        '2': 'source_of_code',
        'b': 'soloist',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_' and '2' not in value:
        order.append('source_of_code')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'performer_or_ensemble': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_code': value.get('2', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('library_of_congress_call_number', '^050..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map1 = {"0": "Item is in LC", "1": "Item is not in LC", "_": "No information provided"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'b': 'item_number',
        '6': 'linkage',
        '3': 'materials_specified',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('existence_in_lc_collection')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'materials_specified': value.get('3'),
        'existence_in_lc_collection': indicator_map1.get(key[3], key[3]),
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('library_of_congress_copy_issue_offprint_statement', '^051..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Library of Congress Copy, Issue, Offprint Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'c': 'copy_information',
        'b': 'item_number',
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
        'classification_number': value.get('a'),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('geographic_classification', '^052..')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    indicator_map1 = {"1": "U.S. Dept. of Defense Classification", "7": "Source specified in subfield $2", "_": "Library of Congress Classification"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'geographic_classification_area_code',
        'd': 'populated_place_name',
        '2': 'code_source',
        'b': 'geographic_classification_subarea_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('code_source')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geographic_classification_area_code': value.get('a'),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'code_source': value.get('2', indicator_map1.get(key[3], key[3])),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('classification_numbers_assigned_in_canada', '^055..')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    """Classification Numbers Assigned in Canada."""
    indicator_map1 = {"0": "Work held by LAC", "1": "Work not held by LAC", "_": "Information not provided"}
    indicator_map2 = {"0": "LC-based call number assigned by LAC", "1": "Complete LC class number assigned by LAC", "2": "Incomplete LC class number assigned by LAC", "3": "LC-based call number assigned by the contributing library", "4": "Complete LC class number assigned by the contributing library", "5": "Incomplete LC class number assigned by the contributing library", "6": "Other call number assigned by LAC", "7": "Other class number assigned by LAC", "8": "Other call number assigned by the contributing library", "9": "Other class number assigned by the contributing library"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'b': 'item_number',
        '2': 'source_of_call_class_number',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('existence_in_lac_collection')

    if key[4] != '_':
        order.append('type_completeness_source_of_class_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'source_of_call_class_number': value.get('2'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3], key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('national_library_of_medicine_call_number', '^060..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map1 = {"0": "Item is in NLM", "1": "Item is not in NLM", "_": "No information provided"}
    indicator_map2 = {"0": "Assigned by NLM", "4": "Assigned by agency other than NLM"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number_r',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('existence_in_nlm_collection')

    if key[4] != '_':
        order.append('source_of_call_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number_r': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'existence_in_nlm_collection': indicator_map1.get(key[3], key[3]),
        'source_of_call_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('national_library_of_medicine_copy_statement', '^061..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    """National Library of Medicine Copy Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'c': 'copy_information',
        'b': 'item_number',
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
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('character_sets_present', '^066..')
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


@marc21_liberal.over('national_agricultural_library_call_number', '^070..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    indicator_map1 = {"0": "Item is in NAL", "1": "Item is not in NAL"}
    field_map = {
        '8': 'field_link_and_sequence_number_r',
        'a': 'classification_number',
        'b': 'item_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('existence_in_nal_collection')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'existence_in_nal_collection': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('national_agricultural_library_copy_statement', '^071..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    """National Agricultural Library Copy Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'c': 'copy_information',
        'b': 'item_number',
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
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'copy_information': utils.force_list(
            value.get('c')
        ),
        'item_number': value.get('b'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('subject_category_code', '^072..')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    indicator_map2 = {"0": "NAL subject category code list", "7": "Source specified in subfield $2"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'subject_category_code',
        'x': 'subject_category_code_subdivision',
        '2': 'source',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('code_source')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'subject_category_code': value.get('a'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        'code_source': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('gpo_item_number', '^074..')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    """GPO Item Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'gpo_item_number',
        'z': 'canceled_invalid_gpo_item_number',
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
        'gpo_item_number': value.get('a'),
        'canceled_invalid_gpo_item_number': utils.force_list(
            value.get('z')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('universal_decimal_classification_number', '^080..')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {"0": "Full", "1": "Abridged", "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'universal_decimal_classification_number',
        '2': 'edition_identifier',
        'b': 'item_number',
        'x': 'common_auxiliary_subdivision',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'universal_decimal_classification_number': value.get('a'),
        'edition_identifier': value.get('2'),
        'item_number': value.get('b'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('dewey_decimal_classification_number', '^082..')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full edition", "1": "Abridged edition", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC", "_": "No information provided"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        '2': 'edition_number',
        'q': 'assigning_agency',
        'b': 'item_number',
        'm': 'standard_or_optional_designation',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('source_of_classification_number')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'edition_number': value.get('2'),
        'assigning_agency': value.get('q'),
        'item_number': value.get('b'),
        'standard_or_optional_designation': value.get('m'),
        'linkage': value.get('6'),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        'source_of_classification_number': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('additional_dewey_decimal_classification_number', '^083..')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    """Additional Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full edition", "1": "Abridged edition", "7": "Other edition specified in subfield $2"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'z': 'table_identification',
        '2': 'edition_number',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        'q': 'assigning_agency',
        'c': 'classification_number_ending_number_of_span',
        'm': 'standard_or_optional_designation',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_edition')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'edition_number': value.get('2'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'assigning_agency': value.get('q'),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'standard_or_optional_designation': value.get('m'),
        'linkage': value.get('6'),
        'type_of_edition': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('other_classification_number', '^084..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        '2': 'number_source',
        'q': 'assigning_agency',
        'b': 'item_number',
        '6': 'linkage',
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
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'number_source': value.get('2'),
        'assigning_agency': value.get('q'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('synthesized_classification_number_components', '^085..')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    """Synthesized Classification Number Components."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'b': 'base_number',
        's': 'digits_added_from_classification_number_in_schedule_or_external_table',
        'y': 'table_sequence_number_for_internal_subarrangement_or_add_table',
        't': 'digits_added_from_internal_subarrangement_or_add_table',
        '6': 'linkage',
        'a': 'number_where_instructions_are_found_single_number_or_beginning_number_of_span',
        'r': 'root_number',
        'z': 'table_identification',
        'w': 'table_identification_internal_subarrangement_or_add_table',
        'u': 'number_being_analyzed',
        'c': 'classification_number_ending_number_of_span',
        'v': 'number_in_internal_subarrangement_or_add_table_where_instructions_are_found',
        'f': 'facet_designator',
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
        'base_number': utils.force_list(
            value.get('b')
        ),
        'digits_added_from_classification_number_in_schedule_or_external_table': utils.force_list(
            value.get('s')
        ),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'digits_added_from_internal_subarrangement_or_add_table': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': utils.force_list(
            value.get('a')
        ),
        'root_number': utils.force_list(
            value.get('r')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'table_identification_internal_subarrangement_or_add_table': utils.force_list(
            value.get('w')
        ),
        'number_being_analyzed': utils.force_list(
            value.get('u')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': utils.force_list(
            value.get('v')
        ),
        'facet_designator': utils.force_list(
            value.get('f')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('government_document_classification_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    indicator_map1 = {"0": "Superintendent of Documents Classification System", "1": "Government of Canada Publications: Outline of Classification", "_": "Source specified in subfield $2"}
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'classification_number',
        'z': 'canceled_invalid_classification_number',
        '2': 'number_source',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('number_source')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'classification_number': value.get('a'),
        'canceled_invalid_classification_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'number_source': value.get('2', indicator_map1.get(key[3], key[3])),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('report_number', '^088..')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    """Report Number."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'report_number',
        'z': 'canceled_invalid_report_number',
        '6': 'linkage',
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
        'report_number': value.get('a'),
        'canceled_invalid_report_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
