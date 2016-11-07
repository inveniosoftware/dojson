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

from ..model import marc21_authority


@marc21_authority.over('electronic_location_and_access', '^856[132_074][12_08]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {"0": "Email", "1": "FTP", "2": "Remote login (Telnet)", "3": "Dial-up", "4": "HTTP", "7": "Method specified in subfield $2", "_": "No information provided"}
    indicator_map2 = {"0": "Resource", "1": "Version of resource", "2": "Related resource", "8": "No display constant generated", "_": "No information provided"}
    field_map = {
        'q': 'electronic_format_type',
        'c': 'compression_information',
        'w': 'record_control_number',
        'o': 'operating_system',
        'j': 'bits_per_second',
        'a': 'host_name',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'i': 'instruction',
        'm': 'contact_for_access_assistance',
        'y': 'link_text',
        's': 'file_size',
        'n': 'name_of_location_of_host',
        't': 'terminal_emulation',
        'p': 'port',
        '2': 'access_method',
        'b': 'access_number',
        'h': 'processor_of_request',
        'k': 'password',
        'd': 'path',
        'z': 'public_note',
        'v': 'hours_access_method_available',
        '3': 'materials_specified',
        'x': 'nonpublic_note',
        'l': 'logon',
        'f': 'electronic_name',
        'r': 'settings',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and '2' not in value:
        order.append('access_method')

    if key[4] in indicator_map2:
        order.append('relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'electronic_format_type': value.get('q'),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'operating_system': value.get('o'),
        'bits_per_second': value.get('j'),
        'host_name': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'name_of_location_of_host': value.get('n'),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'port': value.get('p'),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'processor_of_request': value.get('h'),
        'password': value.get('k'),
        'path': utils.force_list(
            value.get('d')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'hours_access_method_available': utils.force_list(
            value.get('v')
        ),
        'materials_specified': value.get('3'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'logon': value.get('l'),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'settings': value.get('r'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'access_method': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'relationship': indicator_map2.get(key[4]),
    }


@marc21_authority.over('alternate_graphic_representation', '^880..')
@utils.for_each_value
@utils.filter_values
def alternate_graphic_representation(self, key, value):
    """Alternate Graphic Representation."""
    field_map = {
        '1': 'same_as_associated_field_1',
        'h': 'same_as_associated_field_h',
        'c': 'same_as_associated_field_c',
        'w': 'same_as_associated_field_w',
        'o': 'same_as_associated_field_o',
        't': 'same_as_associated_field_t',
        'j': 'same_as_associated_field_j',
        'a': 'same_as_associated_field_a',
        '6': 'linkage',
        '4': 'same_as_associated_field_4',
        '8': 'same_as_associated_field_8',
        'd': 'same_as_associated_field_d',
        'm': 'same_as_associated_field_m',
        'q': 'same_as_associated_field_q',
        'y': 'same_as_associated_field_y',
        's': 'same_as_associated_field_s',
        '0': 'same_as_associated_field_0',
        'e': 'same_as_associated_field_e',
        'n': 'same_as_associated_field_n',
        'g': 'same_as_associated_field_g',
        '5': 'same_as_associated_field_5',
        'p': 'same_as_associated_field_p',
        '2': 'same_as_associated_field_2',
        'b': 'same_as_associated_field_b',
        '7': 'same_as_associated_field_7',
        'k': 'same_as_associated_field_k',
        'i': 'same_as_associated_field_i',
        'z': 'same_as_associated_field_z',
        'v': 'same_as_associated_field_v',
        '3': 'same_as_associated_field_3',
        'x': 'same_as_associated_field_x',
        'l': 'same_as_associated_field_l',
        '9': 'same_as_associated_field_9',
        'f': 'same_as_associated_field_f',
        'r': 'same_as_associated_field_r',
        'u': 'same_as_associated_field_u',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'same_as_associated_field_1': utils.force_list(
            value.get('1')
        ),
        'same_as_associated_field_h': utils.force_list(
            value.get('h')
        ),
        'same_as_associated_field_c': utils.force_list(
            value.get('c')
        ),
        'same_as_associated_field_w': utils.force_list(
            value.get('w')
        ),
        'same_as_associated_field_o': utils.force_list(
            value.get('o')
        ),
        'same_as_associated_field_t': utils.force_list(
            value.get('t')
        ),
        'same_as_associated_field_j': utils.force_list(
            value.get('j')
        ),
        'same_as_associated_field_a': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'same_as_associated_field_4': utils.force_list(
            value.get('4')
        ),
        'same_as_associated_field_8': utils.force_list(
            value.get('8')
        ),
        'same_as_associated_field_d': utils.force_list(
            value.get('d')
        ),
        'same_as_associated_field_m': utils.force_list(
            value.get('m')
        ),
        'same_as_associated_field_q': utils.force_list(
            value.get('q')
        ),
        'same_as_associated_field_y': utils.force_list(
            value.get('y')
        ),
        'same_as_associated_field_s': utils.force_list(
            value.get('s')
        ),
        'same_as_associated_field_0': utils.force_list(
            value.get('0')
        ),
        'same_as_associated_field_e': utils.force_list(
            value.get('e')
        ),
        'same_as_associated_field_n': utils.force_list(
            value.get('n')
        ),
        'same_as_associated_field_g': utils.force_list(
            value.get('g')
        ),
        'same_as_associated_field_5': utils.force_list(
            value.get('5')
        ),
        'same_as_associated_field_p': utils.force_list(
            value.get('p')
        ),
        'same_as_associated_field_2': utils.force_list(
            value.get('2')
        ),
        'same_as_associated_field_b': utils.force_list(
            value.get('b')
        ),
        'same_as_associated_field_7': utils.force_list(
            value.get('7')
        ),
        'same_as_associated_field_k': utils.force_list(
            value.get('k')
        ),
        'same_as_associated_field_i': utils.force_list(
            value.get('i')
        ),
        'same_as_associated_field_z': utils.force_list(
            value.get('z')
        ),
        'same_as_associated_field_v': utils.force_list(
            value.get('v')
        ),
        'same_as_associated_field_3': utils.force_list(
            value.get('3')
        ),
        'same_as_associated_field_x': utils.force_list(
            value.get('x')
        ),
        'same_as_associated_field_l': utils.force_list(
            value.get('l')
        ),
        'same_as_associated_field_9': utils.force_list(
            value.get('9')
        ),
        'same_as_associated_field_f': utils.force_list(
            value.get('f')
        ),
        'same_as_associated_field_r': utils.force_list(
            value.get('r')
        ),
        'same_as_associated_field_u': utils.force_list(
            value.get('u')
        ),
    }


@marc21_authority.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {"0": "Fully machine-generated", "1": "Partially machine-generated", "_": "No information provided/not applicable"}
    field_map = {
        'd': 'generation_date',
        'a': 'generation_process',
        'c': 'confidence_value',
        'w': 'bibliographic_record_control_number',
        'x': 'validity_end_date',
        'u': 'uniform_resource_identifier',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'generation_agency',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('method_of_machine_assignment')

    return {
        '__order__': tuple(order) if len(order) else None,
        'generation_date': value.get('d'),
        'generation_process': value.get('a'),
        'confidence_value': value.get('c'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'validity_end_date': value.get('x'),
        'uniform_resource_identifier': value.get('u'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'generation_agency': value.get('q'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'method_of_machine_assignment': indicator_map1.get(key[3]),
    }


@marc21_authority.over('description_conversion_information', '^884..')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    field_map = {
        'q': 'conversion_agency',
        'a': 'conversion_process',
        'k': 'identifier_of_source_metadata',
        'u': 'uniform_resource_identifier',
        'g': 'conversion_date',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'conversion_agency': value.get('q'),
        'conversion_process': value.get('a'),
        'identifier_of_source_metadata': value.get('k'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'conversion_date': value.get('g'),
    }
