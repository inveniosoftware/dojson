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

from ..model import to_marc21_authority


@to_marc21_authority.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {"Dial-up": "3", "Email": "0", "FTP": "1", "HTTP": "4", "Method specified in subfield $2": "7", "No information provided": "_", "Remote login (Telnet)": "2"}
    indicator_map2 = {"No display constant generated": "8", "No information provided": "_", "Related resource": "2", "Resource": "0", "Version of resource": "1"}
    field_map = {
        'host_name': 'a',
        'access_number': 'b',
        'compression_information': 'c',
        'path': 'd',
        'electronic_name': 'f',
        'processor_of_request': 'h',
        'instruction': 'i',
        'bits_per_second': 'j',
        'password': 'k',
        'logon': 'l',
        'contact_for_access_assistance': 'm',
        'name_of_location_of_host': 'n',
        'operating_system': 'o',
        'port': 'p',
        'electronic_format_type': 'q',
        'settings': 'r',
        'file_size': 's',
        'terminal_emulation': 't',
        'uniform_resource_identifier': 'u',
        'hours_access_method_available': 'v',
        'record_control_number': 'w',
        'nonpublic_note': 'x',
        'link_text': 'y',
        'public_note': 'z',
        'access_method': '2',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('access_method'), '7') != '7' and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'h': value.get('processor_of_request'),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'j': value.get('bits_per_second'),
        'k': value.get('password'),
        'l': value.get('logon'),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'n': value.get('name_of_location_of_host'),
        'o': value.get('operating_system'),
        'p': value.get('port'),
        'q': value.get('electronic_format_type'),
        'r': value.get('settings'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('access_method'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '7' if 'access_method' in value and
        not indicator_map1.get(value.get('access_method')) and
        value.get('access_method') == value.get('access_method')
        else indicator_map1.get(value.get('access_method'), '_'),
        '$ind2': indicator_map2.get(value.get('relationship'), '_'),
    }


@to_marc21_authority.over('880', '^alternate_graphic_representation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_alternate_graphic_representation(self, key, value):
    """Reverse - Alternate Graphic Representation."""
    field_map = {
        'same_as_associated_field_a': 'a',
        'same_as_associated_field_b': 'b',
        'same_as_associated_field_c': 'c',
        'same_as_associated_field_d': 'd',
        'same_as_associated_field_e': 'e',
        'same_as_associated_field_f': 'f',
        'same_as_associated_field_g': 'g',
        'same_as_associated_field_h': 'h',
        'same_as_associated_field_i': 'i',
        'same_as_associated_field_j': 'j',
        'same_as_associated_field_k': 'k',
        'same_as_associated_field_l': 'l',
        'same_as_associated_field_m': 'm',
        'same_as_associated_field_n': 'n',
        'same_as_associated_field_o': 'o',
        'same_as_associated_field_p': 'p',
        'same_as_associated_field_q': 'q',
        'same_as_associated_field_r': 'r',
        'same_as_associated_field_s': 's',
        'same_as_associated_field_t': 't',
        'same_as_associated_field_u': 'u',
        'same_as_associated_field_v': 'v',
        'same_as_associated_field_w': 'w',
        'same_as_associated_field_x': 'x',
        'same_as_associated_field_y': 'y',
        'same_as_associated_field_z': 'z',
        'same_as_associated_field_0': '0',
        'same_as_associated_field_1': '1',
        'same_as_associated_field_2': '2',
        'same_as_associated_field_3': '3',
        'same_as_associated_field_4': '4',
        'same_as_associated_field_5': '5',
        'linkage': '6',
        'same_as_associated_field_7': '7',
        'same_as_associated_field_8': '8',
        'same_as_associated_field_9': '9',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('same_as_associated_field_a')
        ),
        'b': utils.reverse_force_list(
            value.get('same_as_associated_field_b')
        ),
        'c': utils.reverse_force_list(
            value.get('same_as_associated_field_c')
        ),
        'd': utils.reverse_force_list(
            value.get('same_as_associated_field_d')
        ),
        'e': utils.reverse_force_list(
            value.get('same_as_associated_field_e')
        ),
        'f': utils.reverse_force_list(
            value.get('same_as_associated_field_f')
        ),
        'g': utils.reverse_force_list(
            value.get('same_as_associated_field_g')
        ),
        'h': utils.reverse_force_list(
            value.get('same_as_associated_field_h')
        ),
        'i': utils.reverse_force_list(
            value.get('same_as_associated_field_i')
        ),
        'j': utils.reverse_force_list(
            value.get('same_as_associated_field_j')
        ),
        'k': utils.reverse_force_list(
            value.get('same_as_associated_field_k')
        ),
        'l': utils.reverse_force_list(
            value.get('same_as_associated_field_l')
        ),
        'm': utils.reverse_force_list(
            value.get('same_as_associated_field_m')
        ),
        'n': utils.reverse_force_list(
            value.get('same_as_associated_field_n')
        ),
        'o': utils.reverse_force_list(
            value.get('same_as_associated_field_o')
        ),
        'p': utils.reverse_force_list(
            value.get('same_as_associated_field_p')
        ),
        'q': utils.reverse_force_list(
            value.get('same_as_associated_field_q')
        ),
        'r': utils.reverse_force_list(
            value.get('same_as_associated_field_r')
        ),
        's': utils.reverse_force_list(
            value.get('same_as_associated_field_s')
        ),
        't': utils.reverse_force_list(
            value.get('same_as_associated_field_t')
        ),
        'u': utils.reverse_force_list(
            value.get('same_as_associated_field_u')
        ),
        'v': utils.reverse_force_list(
            value.get('same_as_associated_field_v')
        ),
        'w': utils.reverse_force_list(
            value.get('same_as_associated_field_w')
        ),
        'x': utils.reverse_force_list(
            value.get('same_as_associated_field_x')
        ),
        'y': utils.reverse_force_list(
            value.get('same_as_associated_field_y')
        ),
        'z': utils.reverse_force_list(
            value.get('same_as_associated_field_z')
        ),
        '0': utils.reverse_force_list(
            value.get('same_as_associated_field_0')
        ),
        '1': utils.reverse_force_list(
            value.get('same_as_associated_field_1')
        ),
        '2': utils.reverse_force_list(
            value.get('same_as_associated_field_2')
        ),
        '3': utils.reverse_force_list(
            value.get('same_as_associated_field_3')
        ),
        '4': utils.reverse_force_list(
            value.get('same_as_associated_field_4')
        ),
        '5': utils.reverse_force_list(
            value.get('same_as_associated_field_5')
        ),
        '6': value.get('linkage'),
        '7': utils.reverse_force_list(
            value.get('same_as_associated_field_7')
        ),
        '8': utils.reverse_force_list(
            value.get('same_as_associated_field_8')
        ),
        '9': utils.reverse_force_list(
            value.get('same_as_associated_field_9')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21_authority.over('883', '^machine_generated_metadata_provenance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {"Fully machine-generated": "0", "No information provided/not applicable": "_", "Partially machine-generated": "1"}
    field_map = {
        'generation_process': 'a',
        'confidence_value': 'c',
        'generation_date': 'd',
        'generation_agency': 'q',
        'uniform_resource_identifier': 'u',
        'bibliographic_record_control_number': 'w',
        'validity_end_date': 'x',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('generation_process'),
        'c': value.get('confidence_value'),
        'd': value.get('generation_date'),
        'q': value.get('generation_agency'),
        'u': value.get('uniform_resource_identifier'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'x': value.get('validity_end_date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'conversion_process': 'a',
        'conversion_date': 'g',
        'identifier_of_source_metadata': 'k',
        'conversion_agency': 'q',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('conversion_process'),
        'g': value.get('conversion_date'),
        'k': value.get('identifier_of_source_metadata'),
        'q': value.get('conversion_agency'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
