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
        'logon': 'l',
        'operating_system': 'o',
        'compression_information': 'c',
        'nonpublic_note': 'x',
        'port': 'p',
        'field_link_and_sequence_number': '8',
        'name_of_location_of_host': 'n',
        'materials_specified': '3',
        'processor_of_request': 'h',
        'access_number': 'b',
        'public_note': 'z',
        'path': 'd',
        'terminal_emulation': 't',
        'access_method': '2',
        'password': 'k',
        'contact_for_access_assistance': 'm',
        'bits_per_second': 'j',
        'electronic_name': 'f',
        'instruction': 'i',
        'record_control_number': 'w',
        'linkage': '6',
        'hours_access_method_available': 'v',
        'host_name': 'a',
        'settings': 'r',
        'electronic_format_type': 'q',
        'uniform_resource_identifier': 'u',
        'link_text': 'y',
        'file_size': 's',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('access_method'), '7') != '7' and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    return {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('logon'),
        'o': value.get('operating_system'),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'p': value.get('port'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'n': value.get('name_of_location_of_host'),
        '3': value.get('materials_specified'),
        'h': value.get('processor_of_request'),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        '2': value.get('access_method'),
        'k': value.get('password'),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'j': value.get('bits_per_second'),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'r': value.get('settings'),
        'q': value.get('electronic_format_type'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        's': utils.reverse_force_list(
            value.get('file_size')
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
        'same_as_associated_field_l': 'l',
        'same_as_associated_field_o': 'o',
        'same_as_associated_field_c': 'c',
        'same_as_associated_field_x': 'x',
        'same_as_associated_field_u': 'u',
        'same_as_associated_field_w': 'w',
        'same_as_associated_field_p': 'p',
        'same_as_associated_field_8': '8',
        'same_as_associated_field_5': '5',
        'same_as_associated_field_n': 'n',
        'same_as_associated_field_3': '3',
        'same_as_associated_field_h': 'h',
        'same_as_associated_field_d': 'd',
        'same_as_associated_field_e': 'e',
        'same_as_associated_field_b': 'b',
        'same_as_associated_field_z': 'z',
        'same_as_associated_field_g': 'g',
        'same_as_associated_field_t': 't',
        'same_as_associated_field_2': '2',
        'same_as_associated_field_k': 'k',
        'same_as_associated_field_m': 'm',
        'same_as_associated_field_j': 'j',
        'same_as_associated_field_f': 'f',
        'same_as_associated_field_i': 'i',
        'same_as_associated_field_9': '9',
        'same_as_associated_field_0': '0',
        'linkage': '6',
        'same_as_associated_field_v': 'v',
        'same_as_associated_field_a': 'a',
        'same_as_associated_field_r': 'r',
        'same_as_associated_field_q': 'q',
        'same_as_associated_field_1': '1',
        'same_as_associated_field_7': '7',
        'same_as_associated_field_y': 'y',
        'same_as_associated_field_4': '4',
        'same_as_associated_field_s': 's',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'l': utils.reverse_force_list(
            value.get('same_as_associated_field_l')
        ),
        'o': utils.reverse_force_list(
            value.get('same_as_associated_field_o')
        ),
        'c': utils.reverse_force_list(
            value.get('same_as_associated_field_c')
        ),
        'x': utils.reverse_force_list(
            value.get('same_as_associated_field_x')
        ),
        'u': utils.reverse_force_list(
            value.get('same_as_associated_field_u')
        ),
        'w': utils.reverse_force_list(
            value.get('same_as_associated_field_w')
        ),
        'p': utils.reverse_force_list(
            value.get('same_as_associated_field_p')
        ),
        '8': utils.reverse_force_list(
            value.get('same_as_associated_field_8')
        ),
        '5': utils.reverse_force_list(
            value.get('same_as_associated_field_5')
        ),
        'n': utils.reverse_force_list(
            value.get('same_as_associated_field_n')
        ),
        '3': utils.reverse_force_list(
            value.get('same_as_associated_field_3')
        ),
        'h': utils.reverse_force_list(
            value.get('same_as_associated_field_h')
        ),
        'd': utils.reverse_force_list(
            value.get('same_as_associated_field_d')
        ),
        'e': utils.reverse_force_list(
            value.get('same_as_associated_field_e')
        ),
        'b': utils.reverse_force_list(
            value.get('same_as_associated_field_b')
        ),
        'z': utils.reverse_force_list(
            value.get('same_as_associated_field_z')
        ),
        'g': utils.reverse_force_list(
            value.get('same_as_associated_field_g')
        ),
        't': utils.reverse_force_list(
            value.get('same_as_associated_field_t')
        ),
        '2': utils.reverse_force_list(
            value.get('same_as_associated_field_2')
        ),
        'k': utils.reverse_force_list(
            value.get('same_as_associated_field_k')
        ),
        'm': utils.reverse_force_list(
            value.get('same_as_associated_field_m')
        ),
        'j': utils.reverse_force_list(
            value.get('same_as_associated_field_j')
        ),
        'f': utils.reverse_force_list(
            value.get('same_as_associated_field_f')
        ),
        'i': utils.reverse_force_list(
            value.get('same_as_associated_field_i')
        ),
        '9': utils.reverse_force_list(
            value.get('same_as_associated_field_9')
        ),
        '0': utils.reverse_force_list(
            value.get('same_as_associated_field_0')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('same_as_associated_field_v')
        ),
        'a': utils.reverse_force_list(
            value.get('same_as_associated_field_a')
        ),
        'r': utils.reverse_force_list(
            value.get('same_as_associated_field_r')
        ),
        'q': utils.reverse_force_list(
            value.get('same_as_associated_field_q')
        ),
        '1': utils.reverse_force_list(
            value.get('same_as_associated_field_1')
        ),
        '7': utils.reverse_force_list(
            value.get('same_as_associated_field_7')
        ),
        'y': utils.reverse_force_list(
            value.get('same_as_associated_field_y')
        ),
        '4': utils.reverse_force_list(
            value.get('same_as_associated_field_4')
        ),
        's': utils.reverse_force_list(
            value.get('same_as_associated_field_s')
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
        'generation_date': 'd',
        'confidence_value': 'c',
        'validity_end_date': 'x',
        'bibliographic_record_control_number': 'w',
        'uniform_resource_identifier': 'u',
        'generation_agency': 'q',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'generation_process': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('generation_date'),
        'c': value.get('confidence_value'),
        'x': value.get('validity_end_date'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'u': value.get('uniform_resource_identifier'),
        'q': value.get('generation_agency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('generation_process'),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), '_'),
        '$ind2': '_',
    }


@to_marc21_authority.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'conversion_date': 'g',
        'conversion_agency': 'q',
        'uniform_resource_identifier': 'u',
        'identifier_of_source_metadata': 'k',
        'conversion_process': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'g': value.get('conversion_date'),
        'q': value.get('conversion_agency'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'k': value.get('identifier_of_source_metadata'),
        'a': value.get('conversion_process'),
        '$ind1': '_',
        '$ind2': '_',
    }
