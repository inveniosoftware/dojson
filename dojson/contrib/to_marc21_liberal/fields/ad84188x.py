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

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {"Dial-up": "3", "Email": "0", "FTP": "1", "HTTP": "4", "Method specified in subfield $2": "7", "No information provided": "_", "Remote login (Telnet)": "2"}
    indicator_map2 = {"No display constant generated": "8", "No information provided": "_", "Related resource": "2", "Resource": "0", "Version of resource": "1"}
    field_map = {
        'access_number': 'b',
        'materials_specified': '3',
        'link_text': 'y',
        'host_name': 'a',
        'contact_for_access_assistance': 'm',
        'terminal_emulation': 't',
        'uniform_resource_identifier': 'u',
        'settings': 'r',
        'instruction': 'i',
        'field_link_and_sequence_number': '8',
        'bits_per_second': 'j',
        'name_of_location_of_host': 'n',
        'electronic_name': 'f',
        'public_note': 'z',
        'electronic_format_type': 'q',
        'port': 'p',
        'path': 'd',
        'processor_of_request': 'h',
        'linkage': '6',
        'compression_information': 'c',
        'password': 'k',
        'operating_system': 'o',
        'nonpublic_note': 'x',
        'logon': 'l',
        'file_size': 's',
        'record_control_number': 'w',
        'access_method': '2',
        'hours_access_method_available': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['access_method', 'relationship'])

    if (indicator_map1.get(value.get('access_method'), '7') != '7' or len(value.get('access_method', '')) == 1) and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        '3': value.get('materials_specified'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'r': value.get('settings'),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'j': value.get('bits_per_second'),
        'n': value.get('name_of_location_of_host'),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'q': value.get('electronic_format_type'),
        'p': value.get('port'),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'h': value.get('processor_of_request'),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'k': value.get('password'),
        'o': value.get('operating_system'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'l': value.get('logon'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': value.get('access_method'),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        '$ind1': '7' if 'access_method' in value and
        not indicator_map1.get(value.get('access_method')) and
        value.get('access_method') == value.get('access_method') and
        field_map.get('access_method') in order
        else indicator_map1.get(value.get('access_method'), value.get('access_method', '_')),
        '$ind2': indicator_map2.get(value.get('relationship'), value.get('relationship', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('880', '^alternate_graphic_representation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_alternate_graphic_representation(self, key, value):
    """Reverse - Alternate Graphic Representation."""
    field_map = {
        'same_as_associated_field_b': 'b',
        'same_as_associated_field_3': '3',
        'same_as_associated_field_0': '0',
        'same_as_associated_field_a': 'a',
        'same_as_associated_field_o': 'o',
        'same_as_associated_field_r': 'r',
        'same_as_associated_field_t': 't',
        'same_as_associated_field_u': 'u',
        'same_as_associated_field_8': '8',
        'same_as_associated_field_i': 'i',
        'same_as_associated_field_z': 'z',
        'same_as_associated_field_e': 'e',
        'same_as_associated_field_4': '4',
        'same_as_associated_field_n': 'n',
        'same_as_associated_field_j': 'j',
        'same_as_associated_field_f': 'f',
        'same_as_associated_field_q': 'q',
        'same_as_associated_field_7': '7',
        'same_as_associated_field_p': 'p',
        'same_as_associated_field_d': 'd',
        'same_as_associated_field_h': 'h',
        'linkage': '6',
        'same_as_associated_field_c': 'c',
        'same_as_associated_field_9': '9',
        'same_as_associated_field_k': 'k',
        'same_as_associated_field_m': 'm',
        'same_as_associated_field_x': 'x',
        'same_as_associated_field_l': 'l',
        'same_as_associated_field_5': '5',
        'same_as_associated_field_w': 'w',
        'same_as_associated_field_g': 'g',
        'same_as_associated_field_y': 'y',
        'same_as_associated_field_s': 's',
        'same_as_associated_field_1': '1',
        'same_as_associated_field_2': '2',
        'same_as_associated_field_v': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('same_as_associated_field_b')
        ),
        '3': utils.reverse_force_list(
            value.get('same_as_associated_field_3')
        ),
        '0': utils.reverse_force_list(
            value.get('same_as_associated_field_0')
        ),
        'a': utils.reverse_force_list(
            value.get('same_as_associated_field_a')
        ),
        'o': utils.reverse_force_list(
            value.get('same_as_associated_field_o')
        ),
        'r': utils.reverse_force_list(
            value.get('same_as_associated_field_r')
        ),
        't': utils.reverse_force_list(
            value.get('same_as_associated_field_t')
        ),
        'u': utils.reverse_force_list(
            value.get('same_as_associated_field_u')
        ),
        '8': utils.reverse_force_list(
            value.get('same_as_associated_field_8')
        ),
        'i': utils.reverse_force_list(
            value.get('same_as_associated_field_i')
        ),
        'z': utils.reverse_force_list(
            value.get('same_as_associated_field_z')
        ),
        'e': utils.reverse_force_list(
            value.get('same_as_associated_field_e')
        ),
        '4': utils.reverse_force_list(
            value.get('same_as_associated_field_4')
        ),
        'n': utils.reverse_force_list(
            value.get('same_as_associated_field_n')
        ),
        'j': utils.reverse_force_list(
            value.get('same_as_associated_field_j')
        ),
        'f': utils.reverse_force_list(
            value.get('same_as_associated_field_f')
        ),
        'q': utils.reverse_force_list(
            value.get('same_as_associated_field_q')
        ),
        '7': utils.reverse_force_list(
            value.get('same_as_associated_field_7')
        ),
        'p': utils.reverse_force_list(
            value.get('same_as_associated_field_p')
        ),
        'd': utils.reverse_force_list(
            value.get('same_as_associated_field_d')
        ),
        'h': utils.reverse_force_list(
            value.get('same_as_associated_field_h')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('same_as_associated_field_c')
        ),
        '9': utils.reverse_force_list(
            value.get('same_as_associated_field_9')
        ),
        'k': utils.reverse_force_list(
            value.get('same_as_associated_field_k')
        ),
        'm': utils.reverse_force_list(
            value.get('same_as_associated_field_m')
        ),
        'x': utils.reverse_force_list(
            value.get('same_as_associated_field_x')
        ),
        'l': utils.reverse_force_list(
            value.get('same_as_associated_field_l')
        ),
        '5': utils.reverse_force_list(
            value.get('same_as_associated_field_5')
        ),
        'w': utils.reverse_force_list(
            value.get('same_as_associated_field_w')
        ),
        'g': utils.reverse_force_list(
            value.get('same_as_associated_field_g')
        ),
        'y': utils.reverse_force_list(
            value.get('same_as_associated_field_y')
        ),
        's': utils.reverse_force_list(
            value.get('same_as_associated_field_s')
        ),
        '1': utils.reverse_force_list(
            value.get('same_as_associated_field_1')
        ),
        '2': utils.reverse_force_list(
            value.get('same_as_associated_field_2')
        ),
        'v': utils.reverse_force_list(
            value.get('same_as_associated_field_v')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('883', '^machine_generated_metadata_provenance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {"Fully machine-generated": "0", "No information provided/not applicable": "_", "Partially machine-generated": "1"}
    field_map = {
        'generation_date': 'd',
        'authority_record_control_number_or_standard_number': '0',
        'generation_process': 'a',
        'confidence_value': 'c',
        'bibliographic_record_control_number': 'w',
        'uniform_resource_identifier': 'u',
        'generation_agency': 'q',
        'field_link_and_sequence_number': '8',
        'validity_end_date': 'x',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['method_of_machine_assignment', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('generation_date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('generation_process'),
        'c': value.get('confidence_value'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'u': value.get('uniform_resource_identifier'),
        'q': value.get('generation_agency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'x': value.get('validity_end_date'),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), value.get('method_of_machine_assignment', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'identifier_of_source_metadata': 'k',
        'conversion_agency': 'q',
        'conversion_process': 'a',
        'conversion_date': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'k': value.get('identifier_of_source_metadata'),
        'q': value.get('conversion_agency'),
        'a': value.get('conversion_process'),
        'g': value.get('conversion_date'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
