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

from ..model import marc21_liberal_authority


@marc21_liberal_authority.over('electronic_location_and_access', '^856..')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {"0": "Email", "1": "FTP", "2": "Remote login (Telnet)", "3": "Dial-up", "4": "HTTP", "7": "Method specified in subfield $2", "_": "No information provided"}
    indicator_map2 = {"0": "Resource", "1": "Version of resource", "2": "Related resource", "8": "No display constant generated", "_": "No information provided"}
    field_map = {
        'z': 'public_note',
        'j': 'bits_per_second',
        'm': 'contact_for_access_assistance',
        'a': 'host_name',
        'h': 'processor_of_request',
        'd': 'path',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'w': 'record_control_number',
        'v': 'hours_access_method_available',
        '3': 'materials_specified',
        'p': 'port',
        't': 'terminal_emulation',
        'y': 'link_text',
        'n': 'name_of_location_of_host',
        'x': 'nonpublic_note',
        '6': 'linkage',
        'k': 'password',
        'b': 'access_number',
        'l': 'logon',
        'i': 'instruction',
        '2': 'access_method',
        's': 'file_size',
        'r': 'settings',
        'q': 'electronic_format_type',
        'c': 'compression_information',
        'o': 'operating_system',
        'f': 'electronic_name',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('access_method')

    if key[4] != '_':
        order.append('relationship')

    record_dict = {
        '__order__': order if len(order) else None,
        'public_note': utils.force_list(
            value.get('z')
        ),
        'bits_per_second': value.get('j'),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'host_name': utils.force_list(
            value.get('a')
        ),
        'processor_of_request': value.get('h'),
        'path': utils.force_list(
            value.get('d')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'hours_access_method_available': utils.force_list(
            value.get('v')
        ),
        'materials_specified': value.get('3'),
        'port': value.get('p'),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'name_of_location_of_host': value.get('n'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'password': value.get('k'),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'logon': value.get('l'),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'settings': value.get('r'),
        'electronic_format_type': value.get('q'),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'operating_system': value.get('o'),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'access_method': value.get('2', indicator_map1.get(key[3], key[3])),
        'relationship': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('alternate_graphic_representation', '^880..')
@utils.for_each_value
@utils.filter_values
def alternate_graphic_representation(self, key, value):
    """Alternate Graphic Representation."""
    field_map = {
        '0': 'same_as_associated_field_0',
        'z': 'same_as_associated_field_z',
        'j': 'same_as_associated_field_j',
        'm': 'same_as_associated_field_m',
        '2': 'same_as_associated_field_2',
        'h': 'same_as_associated_field_h',
        'd': 'same_as_associated_field_d',
        '8': 'same_as_associated_field_8',
        'g': 'same_as_associated_field_g',
        'u': 'same_as_associated_field_u',
        'w': 'same_as_associated_field_w',
        '4': 'same_as_associated_field_4',
        'v': 'same_as_associated_field_v',
        '7': 'same_as_associated_field_7',
        'f': 'same_as_associated_field_f',
        '3': 'same_as_associated_field_3',
        'p': 'same_as_associated_field_p',
        't': 'same_as_associated_field_t',
        'y': 'same_as_associated_field_y',
        'n': 'same_as_associated_field_n',
        'x': 'same_as_associated_field_x',
        '6': 'linkage',
        'k': 'same_as_associated_field_k',
        'b': 'same_as_associated_field_b',
        'e': 'same_as_associated_field_e',
        'l': 'same_as_associated_field_l',
        'i': 'same_as_associated_field_i',
        'a': 'same_as_associated_field_a',
        's': 'same_as_associated_field_s',
        '1': 'same_as_associated_field_1',
        'r': 'same_as_associated_field_r',
        'q': 'same_as_associated_field_q',
        'c': 'same_as_associated_field_c',
        'o': 'same_as_associated_field_o',
        '9': 'same_as_associated_field_9',
        '5': 'same_as_associated_field_5',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'same_as_associated_field_0': utils.force_list(
            value.get('0')
        ),
        'same_as_associated_field_z': utils.force_list(
            value.get('z')
        ),
        'same_as_associated_field_j': utils.force_list(
            value.get('j')
        ),
        'same_as_associated_field_m': utils.force_list(
            value.get('m')
        ),
        'same_as_associated_field_2': utils.force_list(
            value.get('2')
        ),
        'same_as_associated_field_h': utils.force_list(
            value.get('h')
        ),
        'same_as_associated_field_d': utils.force_list(
            value.get('d')
        ),
        'same_as_associated_field_8': utils.force_list(
            value.get('8')
        ),
        'same_as_associated_field_g': utils.force_list(
            value.get('g')
        ),
        'same_as_associated_field_u': utils.force_list(
            value.get('u')
        ),
        'same_as_associated_field_w': utils.force_list(
            value.get('w')
        ),
        'same_as_associated_field_4': utils.force_list(
            value.get('4')
        ),
        'same_as_associated_field_v': utils.force_list(
            value.get('v')
        ),
        'same_as_associated_field_7': utils.force_list(
            value.get('7')
        ),
        'same_as_associated_field_f': utils.force_list(
            value.get('f')
        ),
        'same_as_associated_field_3': utils.force_list(
            value.get('3')
        ),
        'same_as_associated_field_p': utils.force_list(
            value.get('p')
        ),
        'same_as_associated_field_t': utils.force_list(
            value.get('t')
        ),
        'same_as_associated_field_y': utils.force_list(
            value.get('y')
        ),
        'same_as_associated_field_n': utils.force_list(
            value.get('n')
        ),
        'same_as_associated_field_x': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
        'same_as_associated_field_k': utils.force_list(
            value.get('k')
        ),
        'same_as_associated_field_b': utils.force_list(
            value.get('b')
        ),
        'same_as_associated_field_e': utils.force_list(
            value.get('e')
        ),
        'same_as_associated_field_l': utils.force_list(
            value.get('l')
        ),
        'same_as_associated_field_i': utils.force_list(
            value.get('i')
        ),
        'same_as_associated_field_a': utils.force_list(
            value.get('a')
        ),
        'same_as_associated_field_s': utils.force_list(
            value.get('s')
        ),
        'same_as_associated_field_1': utils.force_list(
            value.get('1')
        ),
        'same_as_associated_field_r': utils.force_list(
            value.get('r')
        ),
        'same_as_associated_field_q': utils.force_list(
            value.get('q')
        ),
        'same_as_associated_field_c': utils.force_list(
            value.get('c')
        ),
        'same_as_associated_field_o': utils.force_list(
            value.get('o')
        ),
        'same_as_associated_field_9': utils.force_list(
            value.get('9')
        ),
        'same_as_associated_field_5': utils.force_list(
            value.get('5')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('machine_generated_metadata_provenance', '^883..')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {"0": "Fully machine-generated", "1": "Partially machine-generated", "_": "No information provided/not applicable"}
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'c': 'confidence_value',
        'a': 'generation_process',
        'q': 'generation_agency',
        'd': 'generation_date',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'x': 'validity_end_date',
        'w': 'bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('method_of_machine_assignment')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'confidence_value': value.get('c'),
        'generation_process': value.get('a'),
        'generation_agency': value.get('q'),
        'generation_date': value.get('d'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': value.get('u'),
        'validity_end_date': value.get('x'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'method_of_machine_assignment': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal_authority.over('description_conversion_information', '^884..')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    field_map = {
        'q': 'conversion_agency',
        'k': 'identifier_of_source_metadata',
        'g': 'conversion_date',
        'u': 'uniform_resource_identifier',
        'a': 'conversion_process',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'conversion_agency': value.get('q'),
        'identifier_of_source_metadata': value.get('k'),
        'conversion_date': value.get('g'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'conversion_process': value.get('a'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
