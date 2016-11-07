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


@marc21_liberal.over('edition_statement', '^250..')
@utils.for_each_value
@utils.filter_values
def edition_statement(self, key, value):
    """Edition Statement."""
    field_map = {
        '3': 'materials_specified',
        '6': 'linkage',
        'b': 'remainder_of_edition_statement',
        'a': 'edition_statement',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'remainder_of_edition_statement': value.get('b'),
        'edition_statement': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('musical_presentation_statement', '^254..')
@utils.filter_values
def musical_presentation_statement(self, key, value):
    """Musical Presentation Statement."""
    field_map = {
        '6': 'linkage',
        'a': 'musical_presentation_statement',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'musical_presentation_statement': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('cartographic_mathematical_data', '^255..')
@utils.for_each_value
@utils.filter_values
def cartographic_mathematical_data(self, key, value):
    """Cartographic Mathematical Data."""
    field_map = {
        '6': 'linkage',
        'd': 'statement_of_zone',
        'g': 'exclusion_g_ring_coordinate_pairs',
        'c': 'statement_of_coordinates',
        'b': 'statement_of_projection',
        'a': 'statement_of_scale',
        'e': 'statement_of_equinox',
        'f': 'outer_g_ring_coordinate_pairs',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'statement_of_zone': value.get('d'),
        'exclusion_g_ring_coordinate_pairs': value.get('g'),
        'statement_of_coordinates': value.get('c'),
        'statement_of_projection': value.get('b'),
        'statement_of_scale': value.get('a'),
        'statement_of_equinox': value.get('e'),
        'outer_g_ring_coordinate_pairs': value.get('f'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('computer_file_characteristics', '^256..')
@utils.filter_values
def computer_file_characteristics(self, key, value):
    """Computer File Characteristics."""
    field_map = {
        '6': 'linkage',
        'a': 'computer_file_characteristics',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'computer_file_characteristics': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('country_of_producing_entity', '^257..')
@utils.for_each_value
@utils.filter_values
def country_of_producing_entity(self, key, value):
    """Country of Producing Entity."""
    field_map = {
        '6': 'linkage',
        'a': 'country_of_producing_entity',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'country_of_producing_entity': utils.force_list(
            value.get('a')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('philatelic_issue_data', '^258..')
@utils.for_each_value
@utils.filter_values
def philatelic_issue_data(self, key, value):
    """Philatelic Issue Data."""
    field_map = {
        '6': 'linkage',
        'b': 'denomination',
        'a': 'issuing_jurisdiction',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'denomination': value.get('b'),
        'issuing_jurisdiction': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('publication_distribution_imprint', '^260..')
@utils.for_each_value
@utils.filter_values
def publication_distribution_imprint(self, key, value):
    """Publication, Distribution, etc. (Imprint)."""
    indicator_map1 = {"2": "Intervening publisher", "3": "Current/latest publisher", "_": "Not applicable/No information provided/Earliest available publisher"}
    field_map = {
        '6': 'linkage',
        'b': 'name_of_publisher_distributor',
        'g': 'date_of_manufacture',
        'c': 'date_of_publication_distribution',
        '3': 'materials_specified',
        'a': 'place_of_publication_distribution',
        'e': 'place_of_manufacture',
        'f': 'manufacturer',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('sequence_of_publishing_statements')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'name_of_publisher_distributor': utils.force_list(
            value.get('b')
        ),
        'date_of_manufacture': utils.force_list(
            value.get('g')
        ),
        'date_of_publication_distribution': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'place_of_publication_distribution': utils.force_list(
            value.get('a')
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
        'sequence_of_publishing_statements': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('imprint_statement_for_films_pre_aacr_1_revised', '^261..')
@utils.filter_values
def imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Imprint Statement for Films (Pre-AACR 1 Revised)."""
    field_map = {
        '6': 'linkage',
        'd': 'date_of_production_release',
        'b': 'releasing_company',
        'a': 'producing_company',
        'e': 'contractual_producer',
        'f': 'place_of_production_release',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'date_of_production_release': utils.force_list(
            value.get('d')
        ),
        'releasing_company': utils.force_list(
            value.get('b')
        ),
        'producing_company': utils.force_list(
            value.get('a')
        ),
        'contractual_producer': utils.force_list(
            value.get('e')
        ),
        'place_of_production_release': utils.force_list(
            value.get('f')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('imprint_statement_for_sound_recordings_pre_aacr_1', '^262..')
@utils.filter_values
def imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    """Imprint Statement for Sound Recordings (Pre-AACR 1)."""
    field_map = {
        '6': 'linkage',
        'c': 'date_of_production_release',
        'k': 'serial_identification',
        'l': 'matrix_and_or_take_number',
        'b': 'publisher_or_trade_name',
        'a': 'place_of_production_release',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'date_of_production_release': value.get('c'),
        'serial_identification': value.get('k'),
        'matrix_and_or_take_number': value.get('l'),
        'publisher_or_trade_name': value.get('b'),
        'place_of_production_release': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('projected_publication_date', '^263..')
@utils.filter_values
def projected_publication_date(self, key, value):
    """Projected Publication Date."""
    field_map = {
        '6': 'linkage',
        'a': 'projected_publication_date',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'projected_publication_date': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('production_publication_distribution_manufacture_and_copyright_notice', '^264..')
@utils.for_each_value
@utils.filter_values
def production_publication_distribution_manufacture_and_copyright_notice(self, key, value):
    """Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {"2": "Intervening", "3": "Current/Latest", "_": "Not applicable/No information provided/Earliest"}
    indicator_map2 = {"0": "Production", "1": "Publication", "2": "Distribution", "3": "Manufacture", "4": "Copyright notice date"}
    field_map = {
        '6': 'linkage',
        'b': 'name_of_producer_publisher_distributor_manufacturer',
        'c': 'date_of_production_publication_distribution_manufacture_or_copyright_notice',
        '3': 'materials_specified',
        'a': 'place_of_production_publication_distribution_manufacture',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('sequence_of_statements')

    if key[4] != '_':
        order.append('function_of_entity')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'name_of_producer_publisher_distributor_manufacturer': utils.force_list(
            value.get('b')
        ),
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'place_of_production_publication_distribution_manufacture': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'sequence_of_statements': indicator_map1.get(key[3], key[3]),
        'function_of_entity': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('address', '^270..')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    """Address."""
    indicator_map1 = {"1": "Primary", "2": "Secondary", "_": "No level specified"}
    indicator_map2 = {"0": "Mailing", "7": "Type specified in subfield $i", "_": "No type specified"}
    field_map = {
        'z': 'public_note',
        'c': 'state_or_province',
        'a': 'address',
        '4': 'relator_code',
        'm': 'electronic_mail_address',
        'p': 'contact_person',
        'q': 'title_of_contact_person',
        'k': 'telephone_number',
        'g': 'attention_name',
        'f': 'terms_preceding_attention_name',
        '6': 'linkage',
        'd': 'country',
        'n': 'tdd_or_tty_number',
        'i': 'type_of_address',
        'j': 'specialized_telephone_number',
        'b': 'city',
        'h': 'attention_position',
        'r': 'hours',
        'e': 'postal_code',
        '8': 'field_link_and_sequence_number',
        'l': 'fax_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('level')

    if key[4] != '_' and 'i' not in value:
        order.append('type_of_address')

    record_dict = {
        '__order__': order if len(order) else None,
        'public_note': utils.force_list(
            value.get('z')
        ),
        'state_or_province': value.get('c'),
        'address': utils.force_list(
            value.get('a')
        ),
        'relator_code': utils.force_list(
            value.get('4')
        ),
        'electronic_mail_address': utils.force_list(
            value.get('m')
        ),
        'contact_person': utils.force_list(
            value.get('p')
        ),
        'title_of_contact_person': utils.force_list(
            value.get('q')
        ),
        'telephone_number': utils.force_list(
            value.get('k')
        ),
        'attention_name': value.get('g'),
        'terms_preceding_attention_name': value.get('f'),
        'linkage': value.get('6'),
        'country': value.get('d'),
        'tdd_or_tty_number': utils.force_list(
            value.get('n')
        ),
        'specialized_telephone_number': utils.force_list(
            value.get('j')
        ),
        'city': value.get('b'),
        'attention_position': value.get('h'),
        'hours': utils.force_list(
            value.get('r')
        ),
        'postal_code': value.get('e'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'fax_number': utils.force_list(
            value.get('l')
        ),
        'level': indicator_map1.get(key[3], key[3]),
        'type_of_address': value.get('i', indicator_map2.get(key[4], key[4])),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
