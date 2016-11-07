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
        'operating_system': 'o',
        'public_note': 'z',
        'instruction': 'i',
        'host_name': 'a',
        'electronic_name': 'f',
        'bits_per_second': 'j',
        'access_number': 'b',
        'name_of_location_of_host': 'n',
        'path': 'd',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'terminal_emulation': 't',
        'logon': 'l',
        'compression_information': 'c',
        'nonpublic_note': 'x',
        'processor_of_request': 'h',
        'uniform_resource_identifier': 'u',
        'link_text': 'y',
        'record_control_number': 'w',
        'access_method': '2',
        'port': 'p',
        'contact_for_access_assistance': 'm',
        'settings': 'r',
        'materials_specified': '3',
        'electronic_format_type': 'q',
        'hours_access_method_available': 'v',
        'file_size': 's',
        'password': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['access_method', 'relationship'])

    if (indicator_map1.get(value.get('access_method'), '7') != '7' or len(value.get('access_method', '')) == 1) and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'o': value.get('operating_system'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'j': value.get('bits_per_second'),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'n': value.get('name_of_location_of_host'),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'l': value.get('logon'),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'h': value.get('processor_of_request'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '2': value.get('access_method'),
        'p': value.get('port'),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'r': value.get('settings'),
        '3': value.get('materials_specified'),
        'q': value.get('electronic_format_type'),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        'k': value.get('password'),
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
        'same_as_associated_field_y': 'y',
        'same_as_associated_field_f': 'f',
        'same_as_associated_field_o': 'o',
        'same_as_associated_field_z': 'z',
        'same_as_associated_field_i': 'i',
        'same_as_associated_field_4': '4',
        'same_as_associated_field_e': 'e',
        'same_as_associated_field_5': '5',
        'same_as_associated_field_b': 'b',
        'same_as_associated_field_n': 'n',
        'same_as_associated_field_d': 'd',
        'same_as_associated_field_8': '8',
        'linkage': '6',
        'same_as_associated_field_0': '0',
        'same_as_associated_field_t': 't',
        'same_as_associated_field_l': 'l',
        'same_as_associated_field_c': 'c',
        'same_as_associated_field_x': 'x',
        'same_as_associated_field_h': 'h',
        'same_as_associated_field_u': 'u',
        'same_as_associated_field_j': 'j',
        'same_as_associated_field_v': 'v',
        'same_as_associated_field_1': '1',
        'same_as_associated_field_2': '2',
        'same_as_associated_field_p': 'p',
        'same_as_associated_field_w': 'w',
        'same_as_associated_field_m': 'm',
        'same_as_associated_field_s': 's',
        'same_as_associated_field_3': '3',
        'same_as_associated_field_9': '9',
        'same_as_associated_field_a': 'a',
        'same_as_associated_field_g': 'g',
        'same_as_associated_field_q': 'q',
        'same_as_associated_field_r': 'r',
        'same_as_associated_field_7': '7',
        'same_as_associated_field_k': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'y': utils.reverse_force_list(
            value.get('same_as_associated_field_y')
        ),
        'f': utils.reverse_force_list(
            value.get('same_as_associated_field_f')
        ),
        'o': utils.reverse_force_list(
            value.get('same_as_associated_field_o')
        ),
        'z': utils.reverse_force_list(
            value.get('same_as_associated_field_z')
        ),
        'i': utils.reverse_force_list(
            value.get('same_as_associated_field_i')
        ),
        '4': utils.reverse_force_list(
            value.get('same_as_associated_field_4')
        ),
        'e': utils.reverse_force_list(
            value.get('same_as_associated_field_e')
        ),
        '5': utils.reverse_force_list(
            value.get('same_as_associated_field_5')
        ),
        'b': utils.reverse_force_list(
            value.get('same_as_associated_field_b')
        ),
        'n': utils.reverse_force_list(
            value.get('same_as_associated_field_n')
        ),
        'd': utils.reverse_force_list(
            value.get('same_as_associated_field_d')
        ),
        '8': utils.reverse_force_list(
            value.get('same_as_associated_field_8')
        ),
        '6': value.get('linkage'),
        '0': utils.reverse_force_list(
            value.get('same_as_associated_field_0')
        ),
        't': utils.reverse_force_list(
            value.get('same_as_associated_field_t')
        ),
        'l': utils.reverse_force_list(
            value.get('same_as_associated_field_l')
        ),
        'c': utils.reverse_force_list(
            value.get('same_as_associated_field_c')
        ),
        'x': utils.reverse_force_list(
            value.get('same_as_associated_field_x')
        ),
        'h': utils.reverse_force_list(
            value.get('same_as_associated_field_h')
        ),
        'u': utils.reverse_force_list(
            value.get('same_as_associated_field_u')
        ),
        'j': utils.reverse_force_list(
            value.get('same_as_associated_field_j')
        ),
        'v': utils.reverse_force_list(
            value.get('same_as_associated_field_v')
        ),
        '1': utils.reverse_force_list(
            value.get('same_as_associated_field_1')
        ),
        '2': utils.reverse_force_list(
            value.get('same_as_associated_field_2')
        ),
        'p': utils.reverse_force_list(
            value.get('same_as_associated_field_p')
        ),
        'w': utils.reverse_force_list(
            value.get('same_as_associated_field_w')
        ),
        'm': utils.reverse_force_list(
            value.get('same_as_associated_field_m')
        ),
        's': utils.reverse_force_list(
            value.get('same_as_associated_field_s')
        ),
        '3': utils.reverse_force_list(
            value.get('same_as_associated_field_3')
        ),
        '9': utils.reverse_force_list(
            value.get('same_as_associated_field_9')
        ),
        'a': utils.reverse_force_list(
            value.get('same_as_associated_field_a')
        ),
        'g': utils.reverse_force_list(
            value.get('same_as_associated_field_g')
        ),
        'q': utils.reverse_force_list(
            value.get('same_as_associated_field_q')
        ),
        'r': utils.reverse_force_list(
            value.get('same_as_associated_field_r')
        ),
        '7': utils.reverse_force_list(
            value.get('same_as_associated_field_7')
        ),
        'k': utils.reverse_force_list(
            value.get('same_as_associated_field_k')
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
        'uniform_resource_identifier': 'u',
        'generation_date': 'd',
        'field_link_and_sequence_number': '8',
        'generation_process': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'generation_agency': 'q',
        'bibliographic_record_control_number': 'w',
        'confidence_value': 'c',
        'validity_end_date': 'x',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['method_of_machine_assignment', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': value.get('uniform_resource_identifier'),
        'd': value.get('generation_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('generation_process'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'q': value.get('generation_agency'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'c': value.get('confidence_value'),
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
        'conversion_process': 'a',
        'identifier_of_source_metadata': 'k',
        'conversion_agency': 'q',
        'uniform_resource_identifier': 'u',
        'conversion_date': 'g',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('conversion_process'),
        'k': value.get('identifier_of_source_metadata'),
        'q': value.get('conversion_agency'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'g': value.get('conversion_date'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
