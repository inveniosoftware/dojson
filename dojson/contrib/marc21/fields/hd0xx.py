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

from ..model import marc21_holdings


@marc21_holdings.over('library_of_congress_control_number', '^010..')
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
        'canceled_or_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21_holdings.over('linkage_number', '^014..')
@utils.for_each_value
@utils.filter_values
def linkage_number(self, key, value):
    """Linkage Number."""
    return {
        'linkage_number': value.get('a'),
        'source_of_number': value.get('b'),
        'canceled_or_invalid_linkage_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@marc21_holdings.over('national_bibliographic_agency_control_number', '^016..')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    return {
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'canceled_or_invalid_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21_holdings.over('copyright_or_legal_deposit_number', '^017..')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
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
    }


@marc21_holdings.over('international_standard_book_number', '^020..')
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


@marc21_holdings.over('international_standard_serial_number', '^022..')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    return {
        'international_standard_serial_number': value.get('a'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'issn_l': value.get('l'),
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
    }


@marc21_holdings.over('other_standard_identifier', '^024[1032478_][10_]')
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
        '8': 'Unspecified type of standard number or code'}
    indicator_map2 = {
        '#': 'No information provided',
        '0': 'No difference',
        '1': 'Difference'}
    return {
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get(
            'd'),
        'qualifying_information': utils.force_list(
            value.get('q')),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')),
        'type_of_standard_number_or_code': indicator_map1.get(
            key[3]),
        'difference_indicator': indicator_map2.get(
            key[4]),
    }


@marc21_holdings.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    return {
        'standard_technical_report_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_strn': utils.force_list(
            value.get('z')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
    }


@marc21_holdings.over('coden_designation', '^030..')
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


@marc21_holdings.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    """System Control Number."""
    return {
        'system_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_or_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@marc21_holdings.over('record_source', '^040..')
@utils.filter_values
def record_source(self, key, value):
    """Record Source."""
    return {
        'original_cataloging_agency': value.get('a'),
        'transcribing_agency': value.get('c'),
        'language_of_cataloging': value.get('b'),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21_holdings.over('character_sets_present', '^066..')
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
