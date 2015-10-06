# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21, tomarc21


@marc21.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    return {
        'lc_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nucmc_control_number': utils.force_list(
            value.get('b')
        ),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('010', '^library_of_congress_control_number$')
@utils.filter_values
def reverse_library_of_congress_control_number(self, key, value):
    """Reverse - Library of Congress Control Number."""
    return {
        'a': utils.reverse_force_list(value.get('lc_control_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('nucmc_control_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_lc_control_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('patent_control_information', '^013..')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    """Patent Control Information."""
    return {
        'number': value.get('a'),
        'type_of_number': value.get('c'),
        'country': value.get('b'),
        'status': utils.force_list(
            value.get('e')
        ),
        'date': utils.force_list(
            value.get('d')
        ),
        'party_to_document': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('013', '^patent_control_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_patent_control_information(self, key, value):
    """Reverse - Patent Control Information."""
    return {
        'a': utils.reverse_force_list(value.get('number')),
        'c': utils.reverse_force_list(value.get('type_of_number')),
        'b': utils.reverse_force_list(value.get('country')),
        'e': utils.reverse_force_list(value.get('status')),
        'd': utils.reverse_force_list(value.get('date')),
        'f': utils.reverse_force_list(value.get('party_to_document')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('national_bibliography_number', '^015..')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    """National Bibliography Number."""
    return {
        'national_bibliography_number': utils.force_list(
            value.get('a')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_national_bibliography_number': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('015', '^national_bibliography_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliography_number(self, key, value):
    """Reverse - National Bibliography Number."""
    return {
        'a': utils.reverse_force_list(value.get('national_bibliography_number')),
        'q': utils.reverse_force_list(value.get('qualifying_information')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_national_bibliography_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('national_bibliographic_agency_control_number', '^016[_7].')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    indicator_map1 = {"#": "Library and Archives Canada", "7": "Source specified in subfield $2"}
    return {
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'national_bibliographic_agency': indicator_map1.get(key[3]),
    }


@tomarc21.over('016', '^national_bibliographic_agency_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_bibliographic_agency_control_number(self, key, value):
    """Reverse - National Bibliographic Agency Control Number."""
    indicator_map1 = {"Library and Archives Canada": "_", "Source specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('record_control_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_control_number')),
        '$ind1': indicator_map1.get(value.get('national_bibliographic_agency')),
        '$ind2': '_',
    }


@marc21.over('copyright_or_legal_deposit_number', '^017.[8_]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
    indicator_map2 = {"#": "Copyright or legal deposit number", "8": "No display constant generated"}
    return {
        'copyright_or_legal_deposit_number': utils.force_list(
            value.get('a')
        ),
        'assigning_agency': value.get('b'),
        'date': value.get('d'),
        'display_text': value.get('i'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_copyright_or_legal_deposit_number': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('017', '^copyright_or_legal_deposit_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copyright_or_legal_deposit_number(self, key, value):
    """Reverse - Copyright or Legal Deposit Number."""
    indicator_map2 = {"Copyright or legal deposit number": "_", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('copyright_or_legal_deposit_number')),
        'b': utils.reverse_force_list(value.get('assigning_agency')),
        'd': utils.reverse_force_list(value.get('date')),
        'i': utils.reverse_force_list(value.get('display_text')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_copyright_or_legal_deposit_number')),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('display_constant_controller')),
    }


@marc21.over('copyright_article_fee_code', '^018..')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    """Copyright Article-Fee Code."""
    return {
        'copyright_article_fee_code_nr': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('018', '^copyright_article_fee_code$')
@utils.filter_values
def reverse_copyright_article_fee_code(self, key, value):
    """Reverse - Copyright Article-Fee Code."""
    return {
        'a': utils.reverse_force_list(value.get('copyright_article_fee_code_nr')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    return {
        'international_standard_book_number': value.get('a'),
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
    }


@tomarc21.over('020', '^international_standard_book_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_book_number(self, key, value):
    """Reverse - International Standard Book Number."""
    return {
        'a': utils.reverse_force_list(value.get('international_standard_book_number')),
        'c': utils.reverse_force_list(value.get('terms_of_availability')),
        'q': utils.reverse_force_list(value.get('qualifying_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_isbn')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('international_standard_serial_number', '^022[10_].')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    indicator_map1 = {"#": "No level specified", "0": "Continuing resource of international interest", "1": "Continuing resource not of international interest"}
    return {
        'international_standard_serial_number': value.get('a'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'issn_l': value.get('l'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'level_of_international_interest': indicator_map1.get(key[3]),
    }


@tomarc21.over('022', '^international_standard_serial_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_international_standard_serial_number(self, key, value):
    """Reverse - International Standard Serial Number."""
    indicator_map1 = {"Continuing resource not of international interest": "1", "Continuing resource of international interest": "0", "No level specified": "_"}
    return {
        'a': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'm': utils.reverse_force_list(value.get('canceled_issn_l')),
        'l': utils.reverse_force_list(value.get('issn_l')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('incorrect_issn')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_issn')),
        '$ind1': indicator_map1.get(value.get('level_of_international_interest')),
        '$ind2': '_',
    }


@marc21.over('other_standard_identifier', '^024[1032478_][10_]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {"0": "International Standard Recording Code", "1": "Universal Product Code", "2": "International Standard Music Number", "3": "International Article Number", "4": "Serial Item and Contribution Identifier", "7": "Source specified in subfield $2", "8": "Unspecified type of standard number or code"}
    indicator_map2 = {"#": "No information provided", "0": "No difference", "1": "Difference"}
    return {
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'set_indicator': value.get('p'),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'type_of_standard_number_or_code': indicator_map1.get(key[3]),
        'difference_indicator': indicator_map2.get(key[4]),
    }


@tomarc21.over('024', '^other_standard_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_standard_identifier(self, key, value):
    """Reverse - Other Standard Identifier."""
    indicator_map1 = {"International Article Number": "3", "International Standard Music Number": "2", "International Standard Recording Code": "0", "Serial Item and Contribution Identifier": "4", "Source specified in subfield $2": "7", "Universal Product Code": "1", "Unspecified type of standard number or code": "8"}
    indicator_map2 = {"Difference": "1", "No difference": "0", "No information provided": "_"}
    return {
        'a': utils.reverse_force_list(value.get('standard_number_or_code')),
        'c': utils.reverse_force_list(value.get('terms_of_availability')),
        'd': utils.reverse_force_list(value.get('additional_codes_following_the_standard_number_or_code')),
        'q': utils.reverse_force_list(value.get('qualifying_information')),
        'p': utils.reverse_force_list(value.get('set_indicator')),
        '2': utils.reverse_force_list(value.get('source_of_number_or_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_standard_number_or_code')),
        '$ind1': indicator_map1.get(value.get('type_of_standard_number_or_code')),
        '$ind2': indicator_map2.get(value.get('difference_indicator')),
    }


@marc21.over('overseas_acquisition_number', '^025..')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    """Overseas Acquisition Number."""
    return {
        'overseas_acquisition_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('025', '^overseas_acquisition_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_overseas_acquisition_number(self, key, value):
    """Reverse - Overseas Acquisition Number."""
    return {
        'a': utils.reverse_force_list(value.get('overseas_acquisition_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('fingerprint_identifier', '^026..')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    """Fingerprint Identifier."""
    return {
        'first_and_second_groups_of_characters': value.get('a'),
        'date': value.get('c'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'unparsed_fingerprint': value.get('e'),
        'number_of_volume_or_part': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('026', '^fingerprint_identifier$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_fingerprint_identifier(self, key, value):
    """Reverse - Fingerprint Identifier."""
    return {
        'a': utils.reverse_force_list(value.get('first_and_second_groups_of_characters')),
        'c': utils.reverse_force_list(value.get('date')),
        'b': utils.reverse_force_list(value.get('third_and_fourth_groups_of_characters')),
        'e': utils.reverse_force_list(value.get('unparsed_fingerprint')),
        'd': utils.reverse_force_list(value.get('number_of_volume_or_part')),
        '2': utils.reverse_force_list(value.get('source')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    return {
        'standard_technical_report_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_number': utils.force_list(
            value.get('z')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('027', '^standard_technical_report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_standard_technical_report_number(self, key, value):
    """Reverse - Standard Technical Report Number."""
    return {
        'a': utils.reverse_force_list(value.get('standard_technical_report_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_number')),
        'q': utils.reverse_force_list(value.get('qualifying_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('publisher_number', '^028[103254_][1032_]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    """Publisher Number."""
    indicator_map1 = {"0": "Issue number", "1": "Matrix number", "2": "Plate number", "3": "Other music number", "4": "Videorecording number", "5": "Other publisher number"}
    indicator_map2 = {"0": "No note, no added entry", "1": "Note, added entry", "2": "Note, no added entry", "3": "No note, added entry"}
    return {
        'publisher_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('b'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'type_of_publisher_number': indicator_map1.get(key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4]),
    }


@tomarc21.over('028', '^publisher_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publisher_number(self, key, value):
    """Reverse - Publisher Number."""
    indicator_map1 = {"Issue number": "0", "Matrix number": "1", "Other music number": "3", "Other publisher number": "5", "Plate number": "2", "Videorecording number": "4"}
    indicator_map2 = {"No note, added entry": "3", "No note, no added entry": "0", "Note, added entry": "1", "Note, no added entry": "2"}
    return {
        'a': utils.reverse_force_list(value.get('publisher_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('source')),
        'q': utils.reverse_force_list(value.get('qualifying_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('type_of_publisher_number')),
        '$ind2': indicator_map2.get(value.get('note_added_entry_controller')),
    }


@marc21.over('coden_designation', '^030..')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    """CODEN Designation."""
    return {
        'coden': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_coden': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('030', '^coden_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coden_designation(self, key, value):
    """Reverse - CODEN Designation."""
    return {
        'a': utils.reverse_force_list(value.get('coden')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_coden')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    return {
        'number_of_work': value.get('a'),
        'number_of_excerpt': value.get('c'),
        'number_of_movement': value.get('b'),
        'role': value.get('e'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'clef': value.get('g'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'voice_instrument': value.get('m'),
        'time_signature': value.get('o'),
        'key_signature': value.get('n'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'musical_notation': value.get('p'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'system_code': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key_or_mode': value.get('r'),
    }


@tomarc21.over('031', '^musical_incipits_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_musical_incipits_information(self, key, value):
    """Reverse - Musical Incipits Information."""
    return {
        'a': utils.reverse_force_list(value.get('number_of_work')),
        'c': utils.reverse_force_list(value.get('number_of_excerpt')),
        'b': utils.reverse_force_list(value.get('number_of_movement')),
        'e': utils.reverse_force_list(value.get('role')),
        'd': utils.reverse_force_list(value.get('caption_or_heading')),
        'g': utils.reverse_force_list(value.get('clef')),
        'z': utils.reverse_force_list(value.get('public_note')),
        'm': utils.reverse_force_list(value.get('voice_instrument')),
        'o': utils.reverse_force_list(value.get('time_signature')),
        'n': utils.reverse_force_list(value.get('key_signature')),
        'q': utils.reverse_force_list(value.get('general_note')),
        'p': utils.reverse_force_list(value.get('musical_notation')),
        's': utils.reverse_force_list(value.get('coded_validity_note')),
        '2': utils.reverse_force_list(value.get('system_code')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        't': utils.reverse_force_list(value.get('text_incipit')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('link_text')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'r': utils.reverse_force_list(value.get('key_or_mode')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('postal_registration_number', '^032..')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    """Postal Registration Number."""
    return {
        'postal_registration_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('032', '^postal_registration_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_postal_registration_number(self, key, value):
    """Reverse - Postal Registration Number."""
    return {
        'a': utils.reverse_force_list(value.get('postal_registration_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('source_agency_assigning_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('date_time_and_place_of_an_event', '^033[10_2][10_2]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    """Date/Time and Place of an Event."""
    indicator_map1 = {"#": "No date information ", "0": "Single date ", "1": "Multiple single dates ", "2": "Range of dates "}
    indicator_map2 = {"#": "No information provided ", "0": "Capture ", "1": "Broadcast ", "2": "Finding "}
    return {
        'formatted_date_time': utils.force_list(
            value.get('a')
        ),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('c')
        ),
        'geographic_classification_area_code': utils.force_list(
            value.get('b')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_date_in_subfield_a': indicator_map1.get(key[3]),
        'type_of_event': indicator_map2.get(key[4]),
    }


@tomarc21.over('033', '^date_time_and_place_of_an_event$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event(self, key, value):
    """Reverse - Date/Time and Place of an Event."""
    indicator_map1 = {"Multiple single dates ": "1", "No date information ": "_", "Range of dates ": "2", "Single date ": "0"}
    indicator_map2 = {"Broadcast ": "1", "Capture ": "0", "Finding ": "2", "No information provided ": "_"}
    return {
        'a': utils.reverse_force_list(value.get('formatted_date_time')),
        'c': utils.reverse_force_list(value.get('geographic_classification_subarea_code')),
        'b': utils.reverse_force_list(value.get('geographic_classification_area_code')),
        'p': utils.reverse_force_list(value.get('place_of_event')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('type_of_date_in_subfield_a')),
        '$ind2': indicator_map2.get(value.get('type_of_event')),
    }


@marc21.over('coded_cartographic_mathematical_data', '^034[103_][10_]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map1 = {"0": "Scale indeterminable/No scale recorded", "1": "Single scale", "3": "Range of scales"}
    indicator_map2 = {"#": "Not applicable", "0": "Outer ring", "1": "Exclusion ring"}
    return {
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'category_of_scale': value.get('a'),
        'constant_ratio_linear_vertical_scale': utils.force_list(
            value.get('c')
        ),
        'constant_ratio_linear_horizontal_scale': utils.force_list(
            value.get('b')
        ),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_southernmost_latitude': value.get('g'),
        'coordinates_northernmost_latitude': value.get('f'),
        'angular_scale': utils.force_list(
            value.get('h')
        ),
        'declination_southern_limit': value.get('k'),
        'declination_northern_limit': value.get('j'),
        'right_ascension_eastern_limit': value.get('m'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'distance_from_earth': value.get('r'),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
        'ending_date': value.get('y'),
        'beginning_date': value.get('x'),
        'name_of_extraterrestrial_body': value.get('z'),
        'type_of_scale': indicator_map1.get(key[3]),
        'type_of_ring': indicator_map2.get(key[4]),
    }


@tomarc21.over('034', '^coded_cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_coded_cartographic_mathematical_data(self, key, value):
    """Reverse - Coded Cartographic Mathematical Data."""
    indicator_map1 = {"Range of scales": "3", "Scale indeterminable/No scale recorded": "0", "Single scale": "1"}
    indicator_map2 = {"Exclusion ring": "1", "Not applicable": "_", "Outer ring": "0"}
    return {
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('category_of_scale')),
        'c': utils.reverse_force_list(value.get('constant_ratio_linear_vertical_scale')),
        'b': utils.reverse_force_list(value.get('constant_ratio_linear_horizontal_scale')),
        'e': utils.reverse_force_list(value.get('coordinates_easternmost_longitude')),
        'd': utils.reverse_force_list(value.get('coordinates_westernmost_longitude')),
        'g': utils.reverse_force_list(value.get('coordinates_southernmost_latitude')),
        'f': utils.reverse_force_list(value.get('coordinates_northernmost_latitude')),
        'h': utils.reverse_force_list(value.get('angular_scale')),
        'k': utils.reverse_force_list(value.get('declination_southern_limit')),
        'j': utils.reverse_force_list(value.get('declination_northern_limit')),
        'm': utils.reverse_force_list(value.get('right_ascension_eastern_limit')),
        'n': utils.reverse_force_list(value.get('right_ascension_western_limit')),
        'p': utils.reverse_force_list(value.get('equinox')),
        's': utils.reverse_force_list(value.get('g_ring_latitude')),
        'r': utils.reverse_force_list(value.get('distance_from_earth')),
        't': utils.reverse_force_list(value.get('g_ring_longitude')),
        'y': utils.reverse_force_list(value.get('ending_date')),
        'x': utils.reverse_force_list(value.get('beginning_date')),
        'z': utils.reverse_force_list(value.get('name_of_extraterrestrial_body')),
        '$ind1': indicator_map1.get(value.get('type_of_scale')),
        '$ind2': indicator_map2.get(value.get('type_of_ring')),
    }


@marc21.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    return {
        'system_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('035', '^system_control_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_control_number(self, key, value):
    """Reverse - System Control Number."""
    return {
        'a': utils.reverse_force_list(value.get('system_control_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_control_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('original_study_number_for_computer_data_files', '^036..')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    """Original Study Number for Computer Data Files."""
    return {
        'original_study_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('036', '^original_study_number_for_computer_data_files$')
@utils.filter_values
def reverse_original_study_number_for_computer_data_files(self, key, value):
    """Reverse - Original Study Number for Computer Data Files."""
    return {
        'a': utils.reverse_force_list(value.get('original_study_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('source_agency_assigning_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('source_of_acquisition', '^037..')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    """Source of Acquisition."""
    return {
        'stock_number': value.get('a'),
        'terms_of_availability': utils.force_list(
            value.get('c')
        ),
        'source_of_stock_number_acquisition': value.get('b'),
        'additional_format_characteristics': utils.force_list(
            value.get('g')
        ),
        'form_of_issue': utils.force_list(
            value.get('f')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('037', '^source_of_acquisition$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_acquisition(self, key, value):
    """Reverse - Source of Acquisition."""
    return {
        'a': utils.reverse_force_list(value.get('stock_number')),
        'c': utils.reverse_force_list(value.get('terms_of_availability')),
        'b': utils.reverse_force_list(value.get('source_of_stock_number_acquisition')),
        'g': utils.reverse_force_list(value.get('additional_format_characteristics')),
        'f': utils.reverse_force_list(value.get('form_of_issue')),
        'n': utils.reverse_force_list(value.get('note')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('record_content_licensor', '^038..')
@utils.filter_values
def record_content_licensor(self, key, value):
    """Record Content Licensor."""
    return {
        'record_content_licensor': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('038', '^record_content_licensor$')
@utils.filter_values
def reverse_record_content_licensor(self, key, value):
    """Reverse - Record Content Licensor."""
    return {
        'a': utils.reverse_force_list(value.get('record_content_licensor')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    return {
        'original_cataloging_agency': value.get('a'),
        'transcribing_agency': value.get('c'),
        'language_of_cataloging': value.get('b'),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('040', '^cataloging_source$')
@utils.filter_values
def reverse_cataloging_source(self, key, value):
    """Reverse - Cataloging Source."""
    return {
        'a': utils.reverse_force_list(value.get('original_cataloging_agency')),
        'c': utils.reverse_force_list(value.get('transcribing_agency')),
        'b': utils.reverse_force_list(value.get('language_of_cataloging')),
        'e': utils.reverse_force_list(value.get('description_conventions')),
        'd': utils.reverse_force_list(value.get('modifying_agency')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('language_code', '^041[10_].')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    """Language Code."""
    indicator_map1 = {"#": "No information provided", "0": "Item not a translation/does not include a\n                  \t\t\t\t\t\ttranslation", "1": "Item is or includes a translation"}
    return {
        'language_code_of_text_sound_track_or_separate_title': utils.force_list(
            value.get('a')
        ),
        'language_code_of_summary_or_abstract': utils.force_list(
            value.get('b')
        ),
        'language_code_of_librettos': utils.force_list(
            value.get('e')
        ),
        'language_code_of_sung_or_spoken_text': utils.force_list(
            value.get('d')
        ),
        'language_code_of_accompanying_material_other_than_librettos': utils.force_list(
            value.get('g')
        ),
        'language_code_of_table_of_contents': utils.force_list(
            value.get('f')
        ),
        'language_code_of_original': utils.force_list(
            value.get('h')
        ),
        'language_code_of_intermediate_translations': utils.force_list(
            value.get('k')
        ),
        'language_code_of_subtitles_or_captions': utils.force_list(
            value.get('j')
        ),
        'language_code_of_original_accompanying_materials_other_than_librettos': utils.force_list(
            value.get('m')
        ),
        'language_code_of_original_libretto': utils.force_list(
            value.get('n')
        ),
        'source_of_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'translation_indication': indicator_map1.get(key[3]),
    }


@tomarc21.over('041', '^language_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_code(self, key, value):
    """Reverse - Language Code."""
    indicator_map1 = {"Item is or includes a translation": "1", "Item not a translation/does not include a\n                  \t\t\t\t\t\ttranslation": "0", "No information provided": "_"}
    return {
        'a': utils.reverse_force_list(value.get('language_code_of_text_sound_track_or_separate_title')),
        'b': utils.reverse_force_list(value.get('language_code_of_summary_or_abstract')),
        'e': utils.reverse_force_list(value.get('language_code_of_librettos')),
        'd': utils.reverse_force_list(value.get('language_code_of_sung_or_spoken_text')),
        'g': utils.reverse_force_list(value.get('language_code_of_accompanying_material_other_than_librettos')),
        'f': utils.reverse_force_list(value.get('language_code_of_table_of_contents')),
        'h': utils.reverse_force_list(value.get('language_code_of_original')),
        'k': utils.reverse_force_list(value.get('language_code_of_intermediate_translations')),
        'j': utils.reverse_force_list(value.get('language_code_of_subtitles_or_captions')),
        'm': utils.reverse_force_list(value.get('language_code_of_original_accompanying_materials_other_than_librettos')),
        'n': utils.reverse_force_list(value.get('language_code_of_original_libretto')),
        '2': utils.reverse_force_list(value.get('source_of_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('translation_indication')),
        '$ind2': '_',
    }


@marc21.over('authentication_code', '^042..')
@utils.filter_values
def authentication_code(self, key, value):
    """Authentication Code."""
    return {
        'authentication_code': utils.force_list(
            value.get('a')
        ),
    }


@tomarc21.over('042', '^authentication_code$')
@utils.filter_values
def reverse_authentication_code(self, key, value):
    """Reverse - Authentication Code."""
    return {
        'a': utils.reverse_force_list(value.get('authentication_code')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    return {
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'iso_code': utils.force_list(
            value.get('c')
        ),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('043', '^geographic_area_code$')
@utils.filter_values
def reverse_geographic_area_code(self, key, value):
    """Reverse - Geographic Area Code."""
    return {
        'a': utils.reverse_force_list(value.get('geographic_area_code')),
        'c': utils.reverse_force_list(value.get('iso_code')),
        'b': utils.reverse_force_list(value.get('local_gac_code')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '2': utils.reverse_force_list(value.get('source_of_local_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('country_of_publishing_producing_entity_code', '^044..')
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    """Country of Publishing/Producing Entity Code."""
    return {
        'marc_country_code': utils.force_list(
            value.get('a')
        ),
        'iso_country_code': utils.force_list(
            value.get('c')
        ),
        'local_subentity_code': utils.force_list(
            value.get('b')
        ),
        'source_of_local_subentity_code': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('044', '^country_of_publishing_producing_entity_code$')
@utils.filter_values
def reverse_country_of_publishing_producing_entity_code(self, key, value):
    """Reverse - Country of Publishing/Producing Entity Code."""
    return {
        'a': utils.reverse_force_list(value.get('marc_country_code')),
        'c': utils.reverse_force_list(value.get('iso_country_code')),
        'b': utils.reverse_force_list(value.get('local_subentity_code')),
        '2': utils.reverse_force_list(value.get('source_of_local_subentity_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('time_period_of_content', '^045[10_2].')
@utils.filter_values
def time_period_of_content(self, key, value):
    """Time Period of Content."""
    indicator_map1 = {"#": "Subfield $b or $c not present", "0": "Single date/time", "1": "Multiple single dates/times", "2": "Range of dates/times"}
    return {
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3]),
    }


@tomarc21.over('045', '^time_period_of_content$')
@utils.filter_values
def reverse_time_period_of_content(self, key, value):
    """Reverse - Time Period of Content."""
    indicator_map1 = {"Multiple single dates/times": "1", "Range of dates/times": "2", "Single date/time": "0", "Subfield $b or $c not present": "_"}
    return {
        'a': utils.reverse_force_list(value.get('time_period_code')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'c': utils.reverse_force_list(value.get('formatted_pre_9999_bc_time_period')),
        'b': utils.reverse_force_list(value.get('formatted_9999_bc_through_ce_time_period')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('type_of_time_period_in_subfield_b_or_c')),
        '$ind2': '_',
    }


@marc21.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
    return {
        'type_of_date_code': value.get('a'),
        'date_1_ce_date': value.get('c'),
        'date_1_bc_date': value.get('b'),
        'date_2_ce_date': value.get('e'),
        'date_2_bc_date': value.get('d'),
        'beginning_or_single_date_created': value.get('k'),
        'date_resource_modified': value.get('j'),
        'beginning_of_date_valid': value.get('m'),
        'ending_date_created': value.get('l'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'end_of_date_valid': value.get('n'),
        'ending_date_for_aggregated_content': value.get('p'),
        'source_of_date': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('046', '^special_coded_dates$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_special_coded_dates(self, key, value):
    """Reverse - Special Coded Dates."""
    return {
        'a': utils.reverse_force_list(value.get('type_of_date_code')),
        'c': utils.reverse_force_list(value.get('date_1_ce_date')),
        'b': utils.reverse_force_list(value.get('date_1_bc_date')),
        'e': utils.reverse_force_list(value.get('date_2_ce_date')),
        'd': utils.reverse_force_list(value.get('date_2_bc_date')),
        'k': utils.reverse_force_list(value.get('beginning_or_single_date_created')),
        'j': utils.reverse_force_list(value.get('date_resource_modified')),
        'm': utils.reverse_force_list(value.get('beginning_of_date_valid')),
        'l': utils.reverse_force_list(value.get('ending_date_created')),
        'o': utils.reverse_force_list(value.get('single_or_starting_date_for_aggregated_content')),
        'n': utils.reverse_force_list(value.get('end_of_date_valid')),
        'p': utils.reverse_force_list(value.get('ending_date_for_aggregated_content')),
        '2': utils.reverse_force_list(value.get('source_of_date')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('form_of_musical_composition_code', '^047..')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    """Form of Musical Composition Code."""
    return {
        'form_of_musical_composition_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2'),
    }


@tomarc21.over('047', '^form_of_musical_composition_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_musical_composition_code(self, key, value):
    """Reverse - Form of Musical Composition Code."""
    return {
        'a': utils.reverse_force_list(value.get('form_of_musical_composition_code')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source_of_code')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('number_of_musical_instruments_or_voices_code', '^048..')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    """Number of Musical Instruments or Voices Code."""
    return {
        'performer_or_ensemble': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2'),
        'soloist': utils.force_list(
            value.get('b')
        ),
    }


@tomarc21.over('048', '^number_of_musical_instruments_or_voices_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_number_of_musical_instruments_or_voices_code(self, key, value):
    """Reverse - Number of Musical Instruments or Voices Code."""
    return {
        'a': utils.reverse_force_list(value.get('performer_or_ensemble')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source_of_code')),
        'b': utils.reverse_force_list(value.get('soloist')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('library_of_congress_call_number', '^050[10_][0_4]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map1 = {"#": "No information provided", "0": "Item is in LC", "1": "Item is not in LC"}
    indicator_map2 = {"0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lc_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@tomarc21.over('050', '^library_of_congress_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_call_number(self, key, value):
    """Reverse - Library of Congress Call Number."""
    indicator_map1 = {"Item is in LC": "0", "Item is not in LC": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('existence_in_lc_collection')),
        '$ind2': indicator_map2.get(value.get('source_of_call_number')),
    }


@marc21.over('library_of_congress_copy_issue_offprint_statement', '^051..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Library of Congress Copy, Issue, Offprint Statement."""
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@tomarc21.over('051', '^library_of_congress_copy_issue_offprint_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_library_of_congress_copy_issue_offprint_statement(self, key, value):
    """Reverse - Library of Congress Copy, Issue, Offprint Statement."""
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'c': utils.reverse_force_list(value.get('copy_information')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('geographic_classification', '^052..')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    return {
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'code_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('052', '^geographic_classification$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_classification(self, key, value):
    """Reverse - Geographic Classification."""
    return {
        'a': utils.reverse_force_list(value.get('geographic_classification_area_code')),
        'b': utils.reverse_force_list(value.get('geographic_classification_subarea_code')),
        'd': utils.reverse_force_list(value.get('populated_place_name')),
        '2': utils.reverse_force_list(value.get('code_source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('classification_numbers_assigned_in_canada', '^055[10_][_1032547698]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    """Classification Numbers Assigned in Canada."""
    indicator_map1 = {"#": "Information not provided", "0": "Work held by LAC", "1": "Work not held by LAC"}
    indicator_map2 = {"0": "LC-based call number assigned by LAC", "1": "Complete LC class number assigned by LAC", "2": "Incomplete LC class number assigned by LAC", "3": "LC-based call number assigned by the contributing library", "4": "Complete LC class number assigned by the contributing library", "5": "Incomplete LC class number assigned by the contributing library", "6": "Other call number assigned by LAC", "7": "Other class number assigned by LAC", "8": "Other call number assigned by the contributing library", "9": "Other class number assigned by the contributing library"}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_call_class_number': value.get('2'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4]),
    }


@tomarc21.over('055', '^classification_numbers_assigned_in_canada$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_classification_numbers_assigned_in_canada(self, key, value):
    """Reverse - Classification Numbers Assigned in Canada."""
    indicator_map1 = {"Information not provided": "_", "Work held by LAC": "0", "Work not held by LAC": "1"}
    indicator_map2 = {"Complete LC class number assigned by LAC": "1", "Complete LC class number assigned by the contributing library": "4", "Incomplete LC class number assigned by LAC": "2", "Incomplete LC class number assigned by the contributing library": "5", "LC-based call number assigned by LAC": "0", "LC-based call number assigned by the contributing library": "3", "Other call number assigned by LAC": "6", "Other call number assigned by the contributing library": "8", "Other class number assigned by LAC": "7", "Other class number assigned by the contributing library": "9"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source_of_call_class_number')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': indicator_map1.get(value.get('existence_in_lac_collection')),
        '$ind2': indicator_map2.get(value.get('type_completeness_source_of_class_call_number')),
    }


@marc21.over('national_library_of_medicine_call_number', '^060[10_][0_4]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map1 = {"#": "No information provided", "0": "Item is in NLM", "1": "Item is not in NLM"}
    indicator_map2 = {"0": "Assigned by NLM", "4": "Assigned by agency other than NLM"}
    return {
        'classification_number_r': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'existence_in_nlm_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@tomarc21.over('060', '^national_library_of_medicine_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_call_number(self, key, value):
    """Reverse - National Library of Medicine Call Number."""
    indicator_map1 = {"Item is in NLM": "0", "Item is not in NLM": "1", "No information provided": "_"}
    indicator_map2 = {"Assigned by NLM": "0", "Assigned by agency other than NLM": "4"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number_r')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '$ind1': indicator_map1.get(value.get('existence_in_nlm_collection')),
        '$ind2': indicator_map2.get(value.get('source_of_call_number')),
    }


@marc21.over('national_library_of_medicine_copy_statement', '^061..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    """National Library of Medicine Copy Statement."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@tomarc21.over('061', '^national_library_of_medicine_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_library_of_medicine_copy_statement(self, key, value):
    """Reverse - National Library of Medicine Copy Statement."""
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'c': utils.reverse_force_list(value.get('copy_information')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    """Character Sets Present."""
    return {
        'primary_g0_character_set': value.get('a'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
        'primary_g1_character_set': value.get('b'),
    }


@tomarc21.over('066', '^character_sets_present$')
@utils.filter_values
def reverse_character_sets_present(self, key, value):
    """Reverse - Character Sets Present."""
    return {
        'a': utils.reverse_force_list(value.get('primary_g0_character_set')),
        'c': utils.reverse_force_list(value.get('alternate_g0_or_g1_character_set')),
        'b': utils.reverse_force_list(value.get('primary_g1_character_set')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('national_agricultural_library_call_number', '^070[10_].')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    indicator_map1 = {"0": "Item is in NAL", "1": "Item is not in NAL"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'existence_in_nal_collection': indicator_map1.get(key[3]),
    }


@tomarc21.over('070', '^national_agricultural_library_call_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_call_number(self, key, value):
    """Reverse - National Agricultural Library Call Number."""
    indicator_map1 = {"Item is in NAL": "0", "Item is not in NAL": "1"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number_r')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '$ind1': indicator_map1.get(value.get('existence_in_nal_collection')),
        '$ind2': '_',
    }


@marc21.over('national_agricultural_library_copy_statement', '^071..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    """National Agricultural Library Copy Statement."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': utils.force_list(
            value.get('c')
        ),
        'item_number': value.get('b'),
    }


@tomarc21.over('071', '^national_agricultural_library_copy_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_national_agricultural_library_copy_statement(self, key, value):
    """Reverse - National Agricultural Library Copy Statement."""
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'c': utils.reverse_force_list(value.get('copy_information')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('subject_category_code', '^072..')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    return {
        'subject_category_code': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('072', '^subject_category_code$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_category_code(self, key, value):
    """Reverse - Subject Category Code."""
    return {
        'a': utils.reverse_force_list(value.get('subject_category_code')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source')),
        'x': utils.reverse_force_list(value.get('subject_category_code_subdivision')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('gpo_item_number', '^074..')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    """GPO Item Number."""
    return {
        'gpo_item_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_gpo_item_number': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('074', '^gpo_item_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_gpo_item_number(self, key, value):
    """Reverse - GPO Item Number."""
    return {
        'a': utils.reverse_force_list(value.get('gpo_item_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_gpo_item_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('universal_decimal_classification_number', '^080[10_].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {"#": "No information provided", "0": "Full", "1": "Abridged"}
    return {
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'edition_identifier': value.get('2'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@tomarc21.over('080', '^universal_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_universal_decimal_classification_number(self, key, value):
    """Reverse - Universal Decimal Classification Number."""
    indicator_map1 = {"Abridged": "1", "Full": "0", "No information provided": "_"}
    return {
        'a': utils.reverse_force_list(value.get('universal_decimal_classification_number')),
        'b': utils.reverse_force_list(value.get('item_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '2': utils.reverse_force_list(value.get('edition_identifier')),
        'x': utils.reverse_force_list(value.get('common_auxiliary_subdivision')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('type_of_edition')),
        '$ind2': '_',
    }


@marc21.over('dewey_decimal_classification_number', '^082[10_7][0_4]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full edition", "1": "Abridged edition", "7": "Other edition specified in subfield $2"}
    indicator_map2 = {"#": "No information provided", "0": "Assigned by LC", "4": "Assigned by agency other than LC"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@tomarc21.over('082', '^dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dewey_decimal_classification_number(self, key, value):
    """Reverse - Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    indicator_map2 = {"Assigned by LC": "0", "Assigned by agency other than LC": "4", "No information provided": "_"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        'b': utils.reverse_force_list(value.get('item_number')),
        'm': utils.reverse_force_list(value.get('standard_or_optional_designation')),
        'q': utils.reverse_force_list(value.get('assigning_agency')),
        '2': utils.reverse_force_list(value.get('edition_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(value.get('type_of_edition')),
        '$ind2': indicator_map2.get(value.get('source_of_classification_number')),
    }


@marc21.over('additional_dewey_decimal_classification_number', '^083[10_7].')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    """Additional Dewey Decimal Classification Number."""
    indicator_map1 = {"0": "Full edition", "1": "Abridged edition", "7": "Other edition specified in subfield $2"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@tomarc21.over('083', '^additional_dewey_decimal_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_dewey_decimal_classification_number(self, key, value):
    """Reverse - Additional Dewey Decimal Classification Number."""
    indicator_map1 = {"Abridged edition": "1", "Full edition": "0", "Other edition specified in subfield $2": "7"}
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        'c': utils.reverse_force_list(value.get('classification_number_ending_number_of_span')),
        'm': utils.reverse_force_list(value.get('standard_or_optional_designation')),
        'q': utils.reverse_force_list(value.get('assigning_agency')),
        '2': utils.reverse_force_list(value.get('edition_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('table_sequence_number_for_internal_subarrangement_or_add_table')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('table_identification')),
        '$ind1': indicator_map1.get(value.get('type_of_edition')),
        '$ind2': '_',
    }


@marc21.over('other_classification_number', '^084..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'assigning_agency': value.get('q'),
        'number_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('084', '^other_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_classification_number(self, key, value):
    """Reverse - Other Classification Number."""
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        'b': utils.reverse_force_list(value.get('item_number')),
        'q': utils.reverse_force_list(value.get('assigning_agency')),
        '2': utils.reverse_force_list(value.get('number_source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('synthesized_classification_number_components', '^085..')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    """Synthesized Classification Number Components."""
    return {
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': utils.force_list(
            value.get('a')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'base_number': utils.force_list(
            value.get('b')
        ),
        'facet_designator': utils.force_list(
            value.get('f')
        ),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': utils.force_list(
            value.get('v')
        ),
        'digits_added_from_classification_number_in_schedule_or_external_table': utils.force_list(
            value.get('s')
        ),
        'root_number': utils.force_list(
            value.get('r')
        ),
        'number_being_analyzed': utils.force_list(
            value.get('u')
        ),
        'digits_added_from_internal_subarrangement_or_add_table': utils.force_list(
            value.get('t')
        ),
        'table_identification_internal_subarrangement_or_add_table': utils.force_list(
            value.get('w')
        ),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('085', '^synthesized_classification_number_components$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_synthesized_classification_number_components(self, key, value):
    """Reverse - Synthesized Classification Number Components."""
    return {
        'a': utils.reverse_force_list(value.get('number_where_instructions_are_found_single_number_or_beginning_number_of_span')),
        'c': utils.reverse_force_list(value.get('classification_number_ending_number_of_span')),
        'b': utils.reverse_force_list(value.get('base_number')),
        'f': utils.reverse_force_list(value.get('facet_designator')),
        'v': utils.reverse_force_list(value.get('number_in_internal_subarrangement_or_add_table_where_instructions_are_found')),
        's': utils.reverse_force_list(value.get('digits_added_from_classification_number_in_schedule_or_external_table')),
        'r': utils.reverse_force_list(value.get('root_number')),
        'u': utils.reverse_force_list(value.get('number_being_analyzed')),
        't': utils.reverse_force_list(value.get('digits_added_from_internal_subarrangement_or_add_table')),
        'w': utils.reverse_force_list(value.get('table_identification_internal_subarrangement_or_add_table')),
        '6': utils.reverse_force_list(value.get('linkage')),
        'y': utils.reverse_force_list(value.get('table_sequence_number_for_internal_subarrangement_or_add_table')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('table_identification')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('government_document_classification_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_source': value.get('2'),
        'canceled_invalid_classification_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('086', '^government_document_classification_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_government_document_classification_number(self, key, value):
    """Reverse - Government Document Classification Number."""
    return {
        'a': utils.reverse_force_list(value.get('classification_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('number_source')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_classification_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }


@marc21.over('report_number', '^088..')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    """Report Number."""
    return {
        'report_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_report_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('088', '^report_number$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_report_number(self, key, value):
    """Reverse - Report Number."""
    return {
        'a': utils.reverse_force_list(value.get('report_number')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('canceled_invalid_report_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '$ind1': '_',
        '$ind2': '_',
    }
