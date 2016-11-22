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


@to_marc21_liberal.over('250', '^edition_statement$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_edition_statement(self, key, value):
    """Reverse - Edition Statement."""

    field_map = {
        'edition_statement': 'a',
        'remainder_of_edition_statement': 'b',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('edition_statement'),
        'b': value.get('remainder_of_edition_statement'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('254', '^musical_presentation_statement$')
@utils.filter_values
def reverse_musical_presentation_statement(self, key, value):
    """Reverse - Musical Presentation Statement."""

    field_map = {
        'musical_presentation_statement': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('musical_presentation_statement'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('255', '^cartographic_mathematical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cartographic_mathematical_data(self, key, value):
    """Reverse - Cartographic Mathematical Data."""

    field_map = {
        'statement_of_scale': 'a',
        'statement_of_projection': 'b',
        'statement_of_coordinates': 'c',
        'statement_of_zone': 'd',
        'statement_of_equinox': 'e',
        'outer_g_ring_coordinate_pairs': 'f',
        'exclusion_g_ring_coordinate_pairs': 'g',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('statement_of_scale'),
        'b': value.get('statement_of_projection'),
        'c': value.get('statement_of_coordinates'),
        'd': value.get('statement_of_zone'),
        'e': value.get('statement_of_equinox'),
        'f': value.get('outer_g_ring_coordinate_pairs'),
        'g': value.get('exclusion_g_ring_coordinate_pairs'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('256', '^computer_file_characteristics$')
@utils.filter_values
def reverse_computer_file_characteristics(self, key, value):
    """Reverse - Computer File Characteristics."""

    field_map = {
        'computer_file_characteristics': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('computer_file_characteristics'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('257', '^country_of_producing_entity$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_country_of_producing_entity(self, key, value):
    """Reverse - Country of Producing Entity."""

    field_map = {
        'country_of_producing_entity': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('country_of_producing_entity')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('258', '^philatelic_issue_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_philatelic_issue_data(self, key, value):
    """Reverse - Philatelic Issue Data."""

    field_map = {
        'issuing_jurisdiction': 'a',
        'denomination': 'b',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('issuing_jurisdiction'),
        'b': value.get('denomination'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('260', '^publication_distribution_imprint$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publication_distribution_imprint(self, key, value):
    """Reverse - Publication, Distribution, etc. (Imprint)."""
    indicator_map1 = {"Current/latest publisher": "3", "Intervening publisher": "2", "Not applicable/No information provided/Earliest available publisher": "_"}

    field_map = {
        'place_of_publication_distribution': 'a',
        'name_of_publisher_distributor': 'b',
        'date_of_publication_distribution': 'c',
        'place_of_manufacture': 'e',
        'manufacturer': 'f',
        'date_of_manufacture': 'g',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['sequence_of_publishing_statements', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('place_of_publication_distribution')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_publisher_distributor')
        ),
        'c': utils.reverse_force_list(
            value.get('date_of_publication_distribution')
        ),
        'e': utils.reverse_force_list(
            value.get('place_of_manufacture')
        ),
        'f': utils.reverse_force_list(
            value.get('manufacturer')
        ),
        'g': utils.reverse_force_list(
            value.get('date_of_manufacture')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('sequence_of_publishing_statements'), value.get('sequence_of_publishing_statements', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('261', '^imprint_statement_for_films_pre_aacr_1_revised$')
@utils.filter_values
def reverse_imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    """Reverse - Imprint Statement for Films (Pre-AACR 1 Revised)."""

    field_map = {
        'producing_company': 'a',
        'releasing_company': 'b',
        'date_of_production_release': 'd',
        'contractual_producer': 'e',
        'place_of_production_release': 'f',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('producing_company')
        ),
        'b': utils.reverse_force_list(
            value.get('releasing_company')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_production_release')
        ),
        'e': utils.reverse_force_list(
            value.get('contractual_producer')
        ),
        'f': utils.reverse_force_list(
            value.get('place_of_production_release')
        ),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('262', '^imprint_statement_for_sound_recordings_pre_aacr_1$')
@utils.filter_values
def reverse_imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    """Reverse - Imprint Statement for Sound Recordings (Pre-AACR 1)."""

    field_map = {
        'place_of_production_release': 'a',
        'publisher_or_trade_name': 'b',
        'date_of_production_release': 'c',
        'serial_identification': 'k',
        'matrix_and_or_take_number': 'l',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('place_of_production_release'),
        'b': value.get('publisher_or_trade_name'),
        'c': value.get('date_of_production_release'),
        'k': value.get('serial_identification'),
        'l': value.get('matrix_and_or_take_number'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('263', '^projected_publication_date$')
@utils.filter_values
def reverse_projected_publication_date(self, key, value):
    """Reverse - Projected Publication Date."""

    field_map = {
        'projected_publication_date': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('projected_publication_date'),
        '6': value.get('linkage'),
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


@to_marc21_liberal.over('264', '^production_publication_distribution_manufacture_and_copyright_notice$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_production_publication_distribution_manufacture_and_copyright_notice(self, key, value):
    """Reverse - Production, Publication, Distribution, Manufacture, and Copyright Notice."""
    indicator_map1 = {"Current/Latest": "3", "Intervening": "2", "Not applicable/No information provided/Earliest": "_"}
    indicator_map2 = {"Copyright notice date": "4", "Distribution": "2", "Manufacture": "3", "Production": "0", "Publication": "1"}

    field_map = {
        'place_of_production_publication_distribution_manufacture': 'a',
        'name_of_producer_publisher_distributor_manufacturer': 'b',
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': 'c',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['sequence_of_statements', 'function_of_entity'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('place_of_production_publication_distribution_manufacture')
        ),
        'b': utils.reverse_force_list(
            value.get('name_of_producer_publisher_distributor_manufacturer')
        ),
        'c': utils.reverse_force_list(
            value.get('date_of_production_publication_distribution_manufacture_or_copyright_notice')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('sequence_of_statements'), value.get('sequence_of_statements', '_')),
        '$ind2': indicator_map2.get(value.get('function_of_entity'), value.get('function_of_entity', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('270', '^address$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_address(self, key, value):
    """Reverse - Address."""
    indicator_map1 = {"No level specified": "_", "Primary": "1", "Secondary": "2"}
    indicator_map2 = {"Mailing": "0", "No type specified": "_", "Type specified in subfield $i": "7"}

    field_map = {
        'address': 'a',
        'city': 'b',
        'state_or_province': 'c',
        'country': 'd',
        'postal_code': 'e',
        'terms_preceding_attention_name': 'f',
        'attention_name': 'g',
        'attention_position': 'h',
        'type_of_address': 'i',
        'specialized_telephone_number': 'j',
        'telephone_number': 'k',
        'fax_number': 'l',
        'electronic_mail_address': 'm',
        'tdd_or_tty_number': 'n',
        'contact_person': 'p',
        'title_of_contact_person': 'q',
        'hours': 'r',
        'public_note': 'z',
        'relator_code': '4',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['level', 'type_of_address'])

    if (indicator_map2.get(value.get('type_of_address'), '7') != '7' or len(value.get('type_of_address', '')) == 1) and\
            field_map.get('type_of_address'):
        order.remove(field_map.get('type_of_address'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('address')
        ),
        'b': value.get('city'),
        'c': value.get('state_or_province'),
        'd': value.get('country'),
        'e': value.get('postal_code'),
        'f': value.get('terms_preceding_attention_name'),
        'g': value.get('attention_name'),
        'h': value.get('attention_position'),
        'i': value.get('type_of_address'),
        'j': utils.reverse_force_list(
            value.get('specialized_telephone_number')
        ),
        'k': utils.reverse_force_list(
            value.get('telephone_number')
        ),
        'l': utils.reverse_force_list(
            value.get('fax_number')
        ),
        'm': utils.reverse_force_list(
            value.get('electronic_mail_address')
        ),
        'n': utils.reverse_force_list(
            value.get('tdd_or_tty_number')
        ),
        'p': utils.reverse_force_list(
            value.get('contact_person')
        ),
        'q': utils.reverse_force_list(
            value.get('title_of_contact_person')
        ),
        'r': utils.reverse_force_list(
            value.get('hours')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('level'), value.get('level', '_')),
        '$ind2': '7' if 'type_of_address' in value and
        not indicator_map2.get(value.get('type_of_address')) and
        value.get('type_of_address') == value.get('type_of_address') and
        field_map.get('type_of_address') in order
        else indicator_map2.get(value.get('type_of_address'), value.get('type_of_address', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
