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

from ..model import marc21


@marc21.over('edition_statement', '^250..')
@utils.for_each_value
@utils.filter_values
def edition_statement(self, key, value):
    """Edition Statement."""
    field_map = {
        'a': 'edition_statement',
        'b': 'remainder_of_edition_statement',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'edition_statement': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'remainder_of_edition_statement': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('musical_presentation_statement', '^254..')
@utils.filter_values
def musical_presentation_statement(self, key, value):
    """Musical Presentation Statement."""
    field_map = {
        'a': 'musical_presentation_statement',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'musical_presentation_statement': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('cartographic_mathematical_data', '^255..')
@utils.for_each_value
@utils.filter_values
def cartographic_mathematical_data(self, key, value):
    """Cartographic Mathematical Data."""
    field_map = {
        'a': 'statement_of_scale',
        'b': 'statement_of_projection',
        'c': 'statement_of_coordinates',
        'd': 'statement_of_zone',
        'e': 'statement_of_equinox',
        'f': 'outer_g_ring_coordinate_pairs',
        'g': 'exclusion_g_ring_coordinate_pairs',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'statement_of_scale': value.get('a'),
        'statement_of_coordinates': value.get('c'),
        'statement_of_projection': value.get('b'),
        'statement_of_equinox': value.get('e'),
        'statement_of_zone': value.get('d'),
        'exclusion_g_ring_coordinate_pairs': value.get('g'),
        'outer_g_ring_coordinate_pairs': value.get('f'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('computer_file_characteristics', '^256..')
@utils.filter_values
def computer_file_characteristics(self, key, value):
    """Computer File Characteristics."""
    field_map = {
        'a': 'computer_file_characteristics',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'computer_file_characteristics': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('country_of_producing_entity', '^257..')
@utils.for_each_value
@utils.filter_values
def country_of_producing_entity(self, key, value):
    """Country of Producing Entity."""
    field_map = {
        'a': 'country_of_producing_entity',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'country_of_producing_entity': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
    }


@marc21.over('philatelic_issue_data', '^258..')
@utils.for_each_value
@utils.filter_values
def philatelic_issue_data(self, key, value):
    """Philatelic Issue Data."""
    field_map = {
        'a': 'issuing_jurisdiction',
        'b': 'denomination',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'issuing_jurisdiction': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'denomination': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('publication_distribution_imprint', '^260[_23].')
@utils.for_each_value
@utils.filter_values
def publication_distribution_imprint(self, key, value):
    """Publication, Distribution, etc. (Imprint)."""
    indicator_map1 = {
        '_': 'Not applicable/No information provided/Earliest available publisher',
        '2': 'Intervening publisher',
        '3': 'Current/latest publisher',
    }

    field_map = {
        'a': 'place_of_publication_distribution',
        'b': 'name_of_publisher_distributor',
        'c': 'date_of_publication_distribution',
        'e': 'place_of_manufacture',
        'f': 'manufacturer',
        'g': 'date_of_manufacture',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('sequence_of_publishing_statements')

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_publication_distribution': utils.force_list(
            value.get('a')
        ),
        'date_of_publication_distribution': utils.force_list(
            value.get('c')
        ),
        'name_of_publisher_distributor': utils.force_list(
            value.get('b')
        ),
        'place_of_manufacture': utils.force_list(
            value.get('e')
        ),
        'date_of_manufacture': utils.force_list(
            value.get('g')
        ),
        'manufacturer': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'sequence_of_publishing_statements': indicator_map1.get(key[3]),
    }


@marc21.over('imprint_statement_for_films_pre_aacr_1_revised', '^261..')
@utils.filter_values
def imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Imprint Statement for Films (Pre-AACR 1 Revised)."""
    field_map = {
        'a': 'producing_company',
        'b': 'releasing_company',
        'd': 'date_of_production_release',
        'e': 'contractual_producer',
        'f': 'place_of_production_release',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'producing_company': utils.force_list(
            value.get('a')
        ),
        'releasing_company': utils.force_list(
            value.get('b')
        ),
        'contractual_producer': utils.force_list(
            value.get('e')
        ),
        'date_of_production_release': utils.force_list(
            value.get('d')
        ),
        'place_of_production_release': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('imprint_statement_for_sound_recordings_pre_aacr_1', '^262..')
@utils.filter_values
def imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    """Imprint Statement for Sound Recordings (Pre-AACR 1)."""
    field_map = {
        'a': 'place_of_production_release',
        'b': 'publisher_or_trade_name',
        'c': 'date_of_production_release',
        'k': 'serial_identification',
        'l': 'matrix_and_or_take_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_production_release': value.get('a'),
        'date_of_production_release': value.get('c'),
        'publisher_or_trade_name': value.get('b'),
        'serial_identification': value.get('k'),
        'matrix_and_or_take_number': value.get('l'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('projected_publication_date', '^263..')
@utils.filter_values
def projected_publication_date(self, key, value):
    """Projected Publication Date."""
    field_map = {
        'a': 'projected_publication_date',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'projected_publication_date': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over(
    'production_publication_distribution_manufacture_and_copyright_notice',
    '^264[_23][10324_]')
@utils.for_each_value
@utils.filter_values
def production_publication_distribution_manufacture_and_copyright_notice(
        self, key, value):
    """Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {
        '_': 'Not applicable/No information provided/Earliest',
        '2': 'Intervening',
        '3': 'Current/latest',
    }

    indicator_map2 = {
        '0': 'Production',
        '1': 'Publication',
        '2': 'Distribution',
        '3': 'Manufacture',
        '4': 'Copyright notice date',
    }

    field_map = {
        'a': 'place_of_production_publication_distribution_manufacture',
        'b': 'name_of_producer_publisher_distributor_manufacturer',
        'c': 'date_of_production_publication_distribution_manufacture_or_copyright_notice',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('sequence_of_statements')
    if key[4] in indicator_map2:
        order.append('function_of_entity')

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_production_publication_distribution_manufacture': utils.force_list(
            value.get('a')),
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': utils.force_list(
            value.get('c')),
        'name_of_producer_publisher_distributor_manufacturer': utils.force_list(
            value.get('b')),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
        'sequence_of_statements': indicator_map1.get(
            key[3]),
        'function_of_entity': indicator_map2.get(
            key[4]),
    }


@marc21.over('address', '^270[1_2].')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    indicator_map1 = {
        '_': 'No level specified',
        '1': 'Primary',
        '2': 'Secondary',
    }

    indicator_map2 = {
        '_': 'No type specified',
        '0': 'Mailing',
        '7': 'Type specified in subfield $i',
    }

    field_map = {
        'a': 'address',
        'b': 'city',
        'c': 'state_or_province',
        'd': 'country',
        'e': 'postal_code',
        'f': 'terms_preceding_attention_name',
        'g': 'attention_name',
        'h': 'attention_position',
        'i': 'type_of_address',
        'j': 'specialized_telephone_number',
        'k': 'telephone_number',
        'l': 'fax_number',
        'm': 'electronic_mail_address',
        'n': 'tdd_or_tty_number',
        'p': 'contact_person',
        'q': 'title_of_contact_person',
        'r': 'hours',
        'z': 'public_note',
        '4': 'relator_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level')

    if 'type_of_address' not in order and key[4] in indicator_map2:
        order.append('type_of_address')

    return {
        '__order__': tuple(order) if len(order) else None,
        'address': utils.force_list(
            value.get('a')
        ),
        'state_or_province': value.get('c'),
        'city': value.get('b'),
        'postal_code': value.get('e'),
        'country': value.get('d'),
        'attention_name': value.get('g'),
        'terms_preceding_attention_name': value.get('f'),
        'attention_position': value.get('h'),
        'telephone_number': utils.force_list(
            value.get('k')
        ),
        'specialized_telephone_number': utils.force_list(
            value.get('j')
        ),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'fax_number': utils.force_list(
            value.get('l')
        ),
        'tdd_or_tty_number': utils.force_list(
            value.get('n')
        ),
        'title_of_contact_person': utils.force_list(
            value.get('q')
        ),
        'contact_person': utils.force_list(
            value.get('p')
        ),
        'hours': utils.force_list(
            value.get('r')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'level': indicator_map1.get(key[3]),
        'type_of_address': value.get('i') if key[4] == '7' else indicator_map2.get(key[4]),
    }
