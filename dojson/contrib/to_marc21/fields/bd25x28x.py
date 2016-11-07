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


@to_marc21.over('250', '^edition_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_edition_statement(self, key, value):
    """Reverse - Edition Statement."""
    field_map = {
        'linkage': '6',
        'edition_statement': 'a',
        'remainder_of_edition_statement': 'b',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('edition_statement'),
        'b': value.get('remainder_of_edition_statement'),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('254', '^musical_presentation_statement$')
@utils.filter_values
def reverse_musical_presentation_statement(self, key, value):
    """Reverse - Musical Presentation Statement."""
    field_map = {
        'linkage': '6',
        'musical_presentation_statement': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('musical_presentation_statement'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('255', '^cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cartographic_mathematical_data(self, key, value):
    """Reverse - Cartographic Mathematical Data."""
    field_map = {
        'linkage': '6',
        'statement_of_equinox': 'e',
        'statement_of_zone': 'd',
        'outer_g_ring_coordinate_pairs': 'f',
        'field_link_and_sequence_number': '8',
        'statement_of_projection': 'b',
        'statement_of_scale': 'a',
        'exclusion_g_ring_coordinate_pairs': 'g',
        'statement_of_coordinates': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'e': value.get('statement_of_equinox'),
        'd': value.get('statement_of_zone'),
        'f': value.get('outer_g_ring_coordinate_pairs'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('statement_of_projection'),
        'a': value.get('statement_of_scale'),
        'g': value.get('exclusion_g_ring_coordinate_pairs'),
        'c': value.get('statement_of_coordinates'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('256', '^computer_file_characteristics$')
@utils.filter_values
def reverse_computer_file_characteristics(self, key, value):
    """Reverse - Computer File Characteristics."""
    field_map = {
        'linkage': '6',
        'computer_file_characteristics': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('computer_file_characteristics'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('257', '^country_of_producing_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_country_of_producing_entity(self, key, value):
    """Reverse - Country of Producing Entity."""
    field_map = {
        'source': '2',
        'linkage': '6',
        'country_of_producing_entity': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('country_of_producing_entity')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('258', '^philatelic_issue_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_philatelic_issue_data(self, key, value):
    """Reverse - Philatelic Issue Data."""
    field_map = {
        'linkage': '6',
        'issuing_jurisdiction': 'a',
        'denomination': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('issuing_jurisdiction'),
        'b': value.get('denomination'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('260', '^publication_distribution_imprint$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publication_distribution_imprint(self, key, value):
    """Reverse - Publication, Distribution, etc. (Imprint)."""
    indicator_map1 = {"Current/latest publisher": "3", "Intervening publisher": "2", "Not applicable/No information provided/Earliest available publisher": "_"}
    field_map = {
        'linkage': '6',
        'place_of_manufacture': 'e',
        'manufacturer': 'f',
        'field_link_and_sequence_number': '8',
        'name_of_publisher_distributor': 'b',
        'place_of_publication_distribution': 'a',
        'date_of_manufacture': 'g',
        'date_of_publication_distribution': 'c',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('place_of_manufacture')
        ),
        'f': utils.reverse_force_list(
            value.get('manufacturer')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_publisher_distributor')
        ),
        'a': utils.reverse_force_list(
            value.get('place_of_publication_distribution')
        ),
        'g': utils.reverse_force_list(
            value.get('date_of_manufacture')
        ),
        'c': utils.reverse_force_list(
            value.get('date_of_publication_distribution')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('sequence_of_publishing_statements'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('261', '^imprint_statement_for_films_pre_aacr_1_revised$')
@utils.filter_values
def reverse_imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Reverse - Imprint Statement for Films (Pre-AACR 1 Revised)."""
    field_map = {
        'linkage': '6',
        'contractual_producer': 'e',
        'date_of_production_release': 'd',
        'place_of_production_release': 'f',
        'field_link_and_sequence_number': '8',
        'releasing_company': 'b',
        'producing_company': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'e': utils.reverse_force_list(
            value.get('contractual_producer')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_production_release')
        ),
        'f': utils.reverse_force_list(
            value.get('place_of_production_release')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('releasing_company')
        ),
        'a': utils.reverse_force_list(
            value.get('producing_company')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('262', '^imprint_statement_for_sound_recordings_pre_aacr_1$')
@utils.filter_values
def reverse_imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    """Reverse - Imprint Statement for Sound Recordings (Pre-AACR 1)."""
    field_map = {
        'linkage': '6',
        'serial_identification': 'k',
        'field_link_and_sequence_number': '8',
        'publisher_or_trade_name': 'b',
        'place_of_production_release': 'a',
        'matrix_and_or_take_number': 'l',
        'date_of_production_release': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'k': value.get('serial_identification'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('publisher_or_trade_name'),
        'a': value.get('place_of_production_release'),
        'l': value.get('matrix_and_or_take_number'),
        'c': value.get('date_of_production_release'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('263', '^projected_publication_date$')
@utils.filter_values
def reverse_projected_publication_date(self, key, value):
    """Reverse - Projected Publication Date."""
    field_map = {
        'linkage': '6',
        'projected_publication_date': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('projected_publication_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('264', '^production_publication_distribution_manufacture_and_copyright_notice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_production_publication_distribution_manufacture_and_copyright_notice(self, key, value):
    """Reverse - Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2", "Not applicable/No information provided/Earliest": "_"}
    indicator_map2 = {"Copyright notice date": "4", "Distribution": "2", "Manufacture": "3", "Production": "0", "Publication": "1"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'name_of_producer_publisher_distributor_manufacturer': 'b',
        'place_of_production_publication_distribution_manufacture': 'a',
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': 'c',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_producer_publisher_distributor_manufacturer')
        ),
        'a': utils.reverse_force_list(
            value.get('place_of_production_publication_distribution_manufacture')
        ),
        'c': utils.reverse_force_list(
            value.get('date_of_production_publication_distribution_manufacture_or_copyright_notice')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('sequence_of_statements'), '_'),
        '$ind2': indicator_map2.get(value.get('function_of_entity'), '_'),
    }


@to_marc21.over('270', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    indicator_map1 = {"No level specified": "_", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Mailing": "0", "No type specified": "_", "Type specified in subfield $i": "7"}
    field_map = {
        'relator_code': '4',
        'telephone_number': 'k',
        'terms_preceding_attention_name': 'f',
        'tdd_or_tty_number': 'n',
        'city': 'b',
        'attention_position': 'h',
        'type_of_address': 'i',
        'specialized_telephone_number': 'j',
        'fax_number': 'l',
        'title_of_contact_person': 'q',
        'linkage': '6',
        'postal_code': 'e',
        'country': 'd',
        'contact_person': 'p',
        'hours': 'r',
        'attention_name': 'g',
        'public_note': 'z',
        'field_link_and_sequence_number': '8',
        'address': 'a',
        'state_or_province': 'c',
        'electronic_mail_address': 'm',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('type_of_address'), '7') != '7' and\
            field_map.get('type_of_address'):
        order.remove(field_map.get('type_of_address'))

    return {
        '__order__': tuple(order) if len(order) else None,
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'k': utils.reverse_force_list(
            value.get('telephone_number')
        ),
        'f': value.get('terms_preceding_attention_name'),
        'n': utils.reverse_force_list(
            value.get('tdd_or_tty_number')
        ),
        'b': value.get('city'),
        'h': value.get('attention_position'),
        'i': value.get('type_of_address'),
        'j': utils.reverse_force_list(
            value.get('specialized_telephone_number')
        ),
        'l': utils.reverse_force_list(
            value.get('fax_number')
        ),
        'q': utils.reverse_force_list(
            value.get('title_of_contact_person')
        ),
        '6': value.get('linkage'),
        'e': value.get('postal_code'),
        'd': value.get('country'),
        'p': utils.reverse_force_list(
            value.get('contact_person')
        ),
        'r': utils.reverse_force_list(
            value.get('hours')
        ),
        'g': value.get('attention_name'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        'c': value.get('state_or_province'),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        '$ind1': indicator_map1.get(value.get('level'), '_'),
        '$ind2': '7' if 'type_of_address' in value and
        not indicator_map2.get(value.get('type_of_address')) and
        value.get('type_of_address') == value.get('type_of_address')
        else indicator_map2.get(value.get('type_of_address'), '_'),
    }
