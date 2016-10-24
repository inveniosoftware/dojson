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
        'materials_specified': '3',
        'linkage': '6',
        'remainder_of_edition_statement': 'b',
        'edition_statement': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'b': value.get('remainder_of_edition_statement'),
        'a': value.get('edition_statement'),
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
        'statement_of_zone': 'd',
        'linkage': '6',
        'statement_of_coordinates': 'c',
        'exclusion_g_ring_coordinate_pairs': 'g',
        'statement_of_scale': 'a',
        'field_link_and_sequence_number': '8',
        'outer_g_ring_coordinate_pairs': 'f',
        'statement_of_equinox': 'e',
        'statement_of_projection': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('statement_of_zone'),
        '6': value.get('linkage'),
        'c': value.get('statement_of_coordinates'),
        'g': value.get('exclusion_g_ring_coordinate_pairs'),
        'a': value.get('statement_of_scale'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('outer_g_ring_coordinate_pairs'),
        'e': value.get('statement_of_equinox'),
        'b': value.get('statement_of_projection'),
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
        'country_of_producing_entity': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        'a': utils.reverse_force_list(
            value.get('country_of_producing_entity')
        ),
        '6': value.get('linkage'),
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
        'denomination': 'b',
        'issuing_jurisdiction': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('denomination'),
        'a': value.get('issuing_jurisdiction'),
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
    indicator_map1 = {
        "Current/latest publisher": "3",
        "Intervening publisher": "2",
        "Not applicable/No information provided/Earliest available publisher": "_"}
    field_map = {
        'linkage': '6',
        'date_of_publication_distribution': 'c',
        'date_of_manufacture': 'g',
        'place_of_publication_distribution': 'a',
        'field_link_and_sequence_number': '8',
        'manufacturer': 'f',
        'materials_specified': '3',
        'place_of_manufacture': 'e',
        'name_of_publisher_distributor': 'b',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('sequence_of_publishing_statements'), '7') != '7':
        try:
            order.remove(field_map.get('sequence_of_publishing_statements'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('date_of_publication_distribution')
        ),
        'g': utils.reverse_force_list(
            value.get('date_of_manufacture')
        ),
        'a': utils.reverse_force_list(
            value.get('place_of_publication_distribution')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('manufacturer')
        ),
        '3': value.get('materials_specified'),
        'e': utils.reverse_force_list(
            value.get('place_of_manufacture')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_publisher_distributor')
        ),
        '$ind1': indicator_map1.get(value.get('sequence_of_publishing_statements'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('261', '^imprint_statement_for_films_pre_aacr_1_revised$')
@utils.filter_values
def reverse_imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Reverse - Imprint Statement for Films (Pre-AACR 1 Revised)."""
    field_map = {
        'date_of_production_release': 'd',
        'linkage': '6',
        'place_of_production_release': 'f',
        'producing_company': 'a',
        'field_link_and_sequence_number': '8',
        'contractual_producer': 'e',
        'releasing_company': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('date_of_production_release')
        ),
        '6': value.get('linkage'),
        'f': utils.reverse_force_list(
            value.get('place_of_production_release')
        ),
        'a': utils.reverse_force_list(
            value.get('producing_company')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'e': utils.reverse_force_list(
            value.get('contractual_producer')
        ),
        'b': utils.reverse_force_list(
            value.get('releasing_company')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('262', '^imprint_statement_for_sound_recordings_pre_aacr_1$')
@utils.filter_values
def reverse_imprint_statement_for_sound_recordings_pre_aacr_1(
        self, key, value):
    """Reverse - Imprint Statement for Sound Recordings (Pre-AACR 1)."""
    field_map = {
        'matrix_and_or_take_number': 'l',
        'linkage': '6',
        'date_of_production_release': 'c',
        'place_of_production_release': 'a',
        'field_link_and_sequence_number': '8',
        'serial_identification': 'k',
        'publisher_or_trade_name': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('matrix_and_or_take_number'),
        '6': value.get('linkage'),
        'c': value.get('date_of_production_release'),
        'a': value.get('place_of_production_release'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': value.get('serial_identification'),
        'b': value.get('publisher_or_trade_name'),
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


@to_marc21.over(
    '264', '^production_publication_distribution_manufacture_and_copyright_notice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_production_publication_distribution_manufacture_and_copyright_notice(
        self, key, value):
    """Reverse - Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2",
                      "Not applicable/No information provided/Earliest": "_"}
    indicator_map2 = {
        "Copyright notice date": "4",
        "Distribution": "2",
        "Manufacture": "3",
        "Production": "0",
        "Publication": "1"}
    field_map = {
        'linkage': '6',
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': 'c',
        'place_of_production_publication_distribution_manufacture': 'a',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'name_of_producer_publisher_distributor_manufacturer': 'b',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('sequence_of_statements'), '7') != '7':
        try:
            order.remove(field_map.get('sequence_of_statements'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('function_of_entity'), '7') != '7':
        try:
            order.remove(field_map.get('function_of_entity'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get(
                'date_of_production_publication_distribution_manufacture_or_copyright_notice')
        ),
        'a': utils.reverse_force_list(
            value.get('place_of_production_publication_distribution_manufacture')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('name_of_producer_publisher_distributor_manufacturer')
        ),
        '$ind1': indicator_map1.get(value.get('sequence_of_statements'), '_'),
        '$ind2': indicator_map2.get(value.get('function_of_entity'), '_'),
    }


@to_marc21.over('270', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    indicator_map1 = {
        "No level specified": "_",
        "Primary": "1",
        "Secondary": "2"}
    indicator_map2 = {
        "Mailing": "0",
        "No type specified": "_",
        "Type specified in subfield $i": "7"}
    field_map = {
        'relator_code': '4',
        'country': 'd',
        'telephone_number': 'k',
        'state_or_province': 'c',
        'electronic_mail_address': 'm',
        'contact_person': 'p',
        'attention_position': 'h',
        'city': 'b',
        'title_of_contact_person': 'q',
        'fax_number': 'l',
        'tdd_or_tty_number': 'n',
        'linkage': '6',
        'attention_name': 'g',
        'address': 'a',
        'field_link_and_sequence_number': '8',
        'type_of_address': 'i',
        'terms_preceding_attention_name': 'f',
        'hours': 'r',
        'postal_code': 'e',
        'public_note': 'z',
        'specialized_telephone_number': 'j',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('level'), '7') != '7':
        try:
            order.remove(field_map.get('level'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('type_of_address'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_address'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        'd': value.get('country'),
        'k': utils.reverse_force_list(
            value.get('telephone_number')
        ),
        'c': value.get('state_or_province'),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        'p': utils.reverse_force_list(
            value.get('contact_person')
        ),
        'h': value.get('attention_position'),
        'b': value.get('city'),
        'q': utils.reverse_force_list(
            value.get('title_of_contact_person')
        ),
        'l': utils.reverse_force_list(
            value.get('fax_number')
        ),
        'n': utils.reverse_force_list(
            value.get('tdd_or_tty_number')
        ),
        '6': value.get('linkage'),
        'g': value.get('attention_name'),
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': value.get('type_of_address'),
        'f': value.get('terms_preceding_attention_name'),
        'r': utils.reverse_force_list(
            value.get('hours')
        ),
        'e': value.get('postal_code'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'j': utils.reverse_force_list(
            value.get('specialized_telephone_number')
        ),
        '$ind1': indicator_map1.get(value.get('level'), '_'),
        '$ind2': '7' if 'type_of_address' in value and
        not indicator_map2.get(value.get('type_of_address')) and
        value.get('type_of_address') == value.get('type_of_address')
        else indicator_map2.get(value.get('type_of_address'), '_'),
    }
