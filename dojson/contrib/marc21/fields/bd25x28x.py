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
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '6': 'linkage',
        'b': 'remainder_of_edition_statement',
        'a': 'edition_statement',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'remainder_of_edition_statement': value.get('b'),
        'edition_statement': value.get('a'),
    }


@marc21.over('musical_presentation_statement', '^254..')
@utils.filter_values
def musical_presentation_statement(self, key, value):
    """Musical Presentation Statement."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'musical_presentation_statement',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'musical_presentation_statement': value.get('a'),
    }


@marc21.over('cartographic_mathematical_data', '^255..')
@utils.for_each_value
@utils.filter_values
def cartographic_mathematical_data(self, key, value):
    """Cartographic Mathematical Data."""
    field_map = {
        'a': 'statement_of_scale',
        'c': 'statement_of_coordinates',
        'g': 'exclusion_g_ring_coordinate_pairs',
        'e': 'statement_of_equinox',
        'f': 'outer_g_ring_coordinate_pairs',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'b': 'statement_of_projection',
        'd': 'statement_of_zone',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'statement_of_scale': value.get('a'),
        'statement_of_coordinates': value.get('c'),
        'exclusion_g_ring_coordinate_pairs': value.get('g'),
        'statement_of_equinox': value.get('e'),
        'outer_g_ring_coordinate_pairs': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'statement_of_projection': value.get('b'),
        'statement_of_zone': value.get('d'),
    }


@marc21.over('computer_file_characteristics', '^256..')
@utils.filter_values
def computer_file_characteristics(self, key, value):
    """Computer File Characteristics."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'computer_file_characteristics',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'computer_file_characteristics': value.get('a'),
    }


@marc21.over('country_of_producing_entity', '^257..')
@utils.for_each_value
@utils.filter_values
def country_of_producing_entity(self, key, value):
    """Country of Producing Entity."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'country_of_producing_entity',
        '2': 'source',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'country_of_producing_entity': utils.force_list(
            value.get('a')
        ),
        'source': value.get('2'),
    }


@marc21.over('philatelic_issue_data', '^258..')
@utils.for_each_value
@utils.filter_values
def philatelic_issue_data(self, key, value):
    """Philatelic Issue Data."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'b': 'denomination',
        'a': 'issuing_jurisdiction',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'denomination': value.get('b'),
        'issuing_jurisdiction': value.get('a'),
    }


@marc21.over('publication_distribution_imprint', '^260[3_2].')
@utils.for_each_value
@utils.filter_values
def publication_distribution_imprint(self, key, value):
    """Publication, Distribution, etc. (Imprint)."""
    indicator_map1 = {
        "2": "Intervening publisher",
        "3": "Current/latest publisher",
        "_": "Not applicable/No information provided/Earliest available publisher"}
    field_map = {
        'a': 'place_of_publication_distribution',
        'c': 'date_of_publication_distribution',
        'g': 'date_of_manufacture',
        'e': 'place_of_manufacture',
        'f': 'manufacturer',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '6': 'linkage',
        'b': 'name_of_publisher_distributor',
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
        'date_of_manufacture': utils.force_list(
            value.get('g')
        ),
        'place_of_manufacture': utils.force_list(
            value.get('e')
        ),
        'manufacturer': utils.force_list(
            value.get('f')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'name_of_publisher_distributor': utils.force_list(
            value.get('b')
        ),
        'sequence_of_publishing_statements': indicator_map1.get(key[3]),
    }


@marc21.over('imprint_statement_for_films_pre_aacr_1_revised', '^261..')
@utils.filter_values
def imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Imprint Statement for Films (Pre-AACR 1 Revised)."""
    field_map = {
        'a': 'producing_company',
        'f': 'place_of_production_release',
        'e': 'contractual_producer',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'b': 'releasing_company',
        'd': 'date_of_production_release',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'producing_company': utils.force_list(
            value.get('a')
        ),
        'place_of_production_release': utils.force_list(
            value.get('f')
        ),
        'contractual_producer': utils.force_list(
            value.get('e')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'releasing_company': utils.force_list(
            value.get('b')
        ),
        'date_of_production_release': utils.force_list(
            value.get('d')
        ),
    }


@marc21.over('imprint_statement_for_sound_recordings_pre_aacr_1', '^262..')
@utils.filter_values
def imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    """Imprint Statement for Sound Recordings (Pre-AACR 1)."""
    field_map = {
        'a': 'place_of_production_release',
        'c': 'date_of_production_release',
        'k': 'serial_identification',
        'l': 'matrix_and_or_take_number',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'b': 'publisher_or_trade_name',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_production_release': value.get('a'),
        'date_of_production_release': value.get('c'),
        'serial_identification': value.get('k'),
        'matrix_and_or_take_number': value.get('l'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'publisher_or_trade_name': value.get('b'),
    }


@marc21.over('projected_publication_date', '^263..')
@utils.filter_values
def projected_publication_date(self, key, value):
    """Projected Publication Date."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        'a': 'projected_publication_date',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'projected_publication_date': value.get('a'),
    }


@marc21.over(
    'production_publication_distribution_manufacture_and_copyright_notice', '^264[3_2][_12430]')
@utils.for_each_value
@utils.filter_values
def production_publication_distribution_manufacture_and_copyright_notice(
        self, key, value):
    """Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {"2": "Intervening", "3": "Current/Latest",
                      "_": "Not applicable/No information provided/Earliest"}
    indicator_map2 = {
        "0": "Production",
        "1": "Publication",
        "2": "Distribution",
        "3": "Manufacture",
        "4": "Copyright notice date"}
    field_map = {
        'a': 'place_of_production_publication_distribution_manufacture',
        'c': 'date_of_production_publication_distribution_manufacture_or_copyright_notice',
        '8': 'field_link_and_sequence_number',
        '3': 'materials_specified',
        '6': 'linkage',
        'b': 'name_of_producer_publisher_distributor_manufacturer',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('sequence_of_statements')

    if key[4] in indicator_map2:
        order.append('function_of_entity')

    return {
        '__order__': tuple(order) if len(order) else None,
        'place_of_production_publication_distribution_manufacture': utils.force_list(
            value.get('a')
        ),
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': utils.force_list(
            value.get('c')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'name_of_producer_publisher_distributor_manufacturer': utils.force_list(
            value.get('b')
        ),
        'sequence_of_statements': indicator_map1.get(key[3]),
        'function_of_entity': indicator_map2.get(key[4]),
    }


@marc21.over('address', '^270[_12][_07]')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    indicator_map1 = {
        "1": "Primary",
        "2": "Secondary",
        "_": "No level specified"}
    indicator_map2 = {
        "0": "Mailing",
        "7": "Type specified in subfield $i",
        "_": "No type specified"}
    field_map = {
        'g': 'attention_name',
        'i': 'type_of_address',
        'k': 'telephone_number',
        'f': 'terms_preceding_attention_name',
        'e': 'postal_code',
        'l': 'fax_number',
        '6': 'linkage',
        'b': 'city',
        'd': 'country',
        'j': 'specialized_telephone_number',
        'a': 'address',
        'p': 'contact_person',
        'z': 'public_note',
        'c': 'state_or_province',
        'q': 'title_of_contact_person',
        '8': 'field_link_and_sequence_number',
        '4': 'relator_code',
        'r': 'hours',
        'n': 'tdd_or_tty_number',
        'm': 'electronic_mail_address',
        'h': 'attention_position',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('level')

    if key[4] in indicator_map2 and 'i' not in value:
        order.append('type_of_address')

    return {
        '__order__': tuple(order) if len(order) else None,
        'attention_name': value.get('g'),
        'telephone_number': utils.force_list(
            value.get('k')
        ),
        'terms_preceding_attention_name': value.get('f'),
        'postal_code': value.get('e'),
        'fax_number': utils.force_list(
            value.get('l')
        ),
        'linkage': value.get('6'),
        'city': value.get('b'),
        'country': value.get('d'),
        'specialized_telephone_number': utils.force_list(
            value.get('j')
        ),
        'address': utils.force_list(
            value.get('a')
        ),
        'contact_person': utils.force_list(
            value.get('p')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'state_or_province': value.get('c'),
        'title_of_contact_person': utils.force_list(
            value.get('q')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'hours': utils.force_list(
            value.get('r')
        ),
        'tdd_or_tty_number': utils.force_list(
            value.get('n')
        ),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'attention_position': value.get('h'),
        'level': indicator_map1.get(key[3]),
        'type_of_address': value.get('i') if key[4] == '7' else indicator_map2.get(key[4]),
    }
