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


@marc21_liberal.over('holding_institution', '^850..')
@utils.for_each_value
@utils.filter_values
def holding_institution(self, key, value):
    """Holding Institution."""
    field_map = {
        'a': 'holding_institution',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'holding_institution': utils.force_list(
            value.get('a')
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


@marc21_liberal.over('location', '^852..')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
    indicator_map1 = {"0": "Library of Congress classification", "1": "Dewey Decimal classification", "2": "National Library of Medicine classification", "3": "Superintendent of Documents classification", "4": "Shelving control number", "5": "Title", "6": "Shelved separately", "7": "Source specified in subfield $2", "8": "Other scheme", "_": "No information provided"}
    indicator_map2 = {"0": "Not enumeration", "1": "Primary enumeration", "2": "Alternative enumeration", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'sublocation_or_collection',
        'd': 'former_shelving_location',
        'a': 'location',
        't': 'copy_number',
        'q': 'piece_physical_condition',
        'h': 'classification_part',
        'x': 'nonpublic_note',
        'z': 'public_note',
        '3': 'materials_specified',
        'n': 'country_code',
        '2': 'source_of_classification_or_shelving_scheme',
        'k': 'call_number_prefix',
        's': 'copyright_article_fee_code',
        'j': 'shelving_control_number',
        'f': 'coded_location_qualifier',
        'l': 'shelving_form_of_title',
        'g': 'non_coded_location_qualifier',
        'e': 'address',
        '6': 'linkage',
        'm': 'call_number_suffix',
        'p': 'piece_designation',
        'c': 'shelving_location',
        'i': 'item_part',
        '8': 'sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('shelving_scheme')

    if key[4] != '_':
        order.append('shelving_order')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'sublocation_or_collection': utils.force_list(
            value.get('b')
        ),
        'former_shelving_location': utils.force_list(
            value.get('d')
        ),
        'location': value.get('a'),
        'copy_number': value.get('t'),
        'piece_physical_condition': value.get('q'),
        'classification_part': value.get('h'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'materials_specified': value.get('3'),
        'country_code': value.get('n'),
        'source_of_classification_or_shelving_scheme': value.get('2'),
        'call_number_prefix': utils.force_list(
            value.get('k')
        ),
        'copyright_article_fee_code': utils.force_list(
            value.get('s')
        ),
        'shelving_control_number': value.get('j'),
        'coded_location_qualifier': utils.force_list(
            value.get('f')
        ),
        'shelving_form_of_title': value.get('l'),
        'non_coded_location_qualifier': utils.force_list(
            value.get('g')
        ),
        'address': utils.force_list(
            value.get('e')
        ),
        'linkage': value.get('6'),
        'call_number_suffix': utils.force_list(
            value.get('m')
        ),
        'piece_designation': value.get('p'),
        'shelving_location': utils.force_list(
            value.get('c')
        ),
        'item_part': utils.force_list(
            value.get('i')
        ),
        'sequence_number': value.get('8'),
        'shelving_scheme': indicator_map1.get(key[3], key[3]),
        'shelving_order': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('electronic_location_and_access', '^856..')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {"0": "Email", "1": "FTP", "2": "Remote login (Telnet)", "3": "Dial-up", "4": "HTTP", "7": "Method specified in subfield $2", "_": "No information provided"}
    indicator_map2 = {"0": "Resource", "1": "Version of resource", "2": "Related resource", "8": "No display constant generated", "_": "No information provided"}
    field_map = {
        'u': 'uniform_resource_identifier',
        'b': 'access_number',
        'd': 'path',
        'a': 'host_name',
        't': 'terminal_emulation',
        'q': 'electronic_format_type',
        'h': 'processor_of_request',
        'w': 'record_control_number',
        'k': 'password',
        'z': 'public_note',
        '3': 'materials_specified',
        'n': 'name_of_location_of_host',
        '2': 'access_method',
        'y': 'link_text',
        'o': 'operating_system',
        's': 'file_size',
        'j': 'bits_per_second',
        'f': 'electronic_name',
        'r': 'settings',
        'l': 'logon',
        'v': 'hours_access_method_available',
        '6': 'linkage',
        'x': 'nonpublic_note',
        'm': 'contact_for_access_assistance',
        'p': 'port',
        'c': 'compression_information',
        'i': 'instruction',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_' and '2' not in value:
        order.append('access_method')

    if key[4] != '_':
        order.append('relationship')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'path': utils.force_list(
            value.get('d')
        ),
        'host_name': utils.force_list(
            value.get('a')
        ),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'electronic_format_type': value.get('q'),
        'processor_of_request': value.get('h'),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'password': value.get('k'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'materials_specified': value.get('3'),
        'name_of_location_of_host': value.get('n'),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'operating_system': value.get('o'),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'bits_per_second': value.get('j'),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'settings': value.get('r'),
        'logon': value.get('l'),
        'hours_access_method_available': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'port': value.get('p'),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'access_method': value.get('2', indicator_map1.get(key[3], key[3])),
        'relationship': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('replacement_record_information', '^882..')
@utils.filter_values
def replacement_record_information(self, key, value):
    """Replacement Record Information."""
    field_map = {
        'a': 'replacement_title',
        'w': 'replacement_bibliographic_record_control_number',
        'i': 'explanatory_text',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'replacement_title': utils.force_list(
            value.get('a')
        ),
        'replacement_bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
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


@marc21_liberal.over('machine_generated_metadata_provenance', '^883..')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {"0": "Fully machine-generated", "1": "Partially machine-generated", "_": "No information provided/not applicable"}
    field_map = {
        'u': 'uniform_resource_identifier',
        '0': 'authority_record_control_number_or_standard_number',
        'q': 'generation_agency',
        'd': 'generation_date',
        'x': 'validity_end_date',
        'a': 'generation_process',
        '8': 'field_link_and_sequence_number',
        'w': 'bibliographic_record_control_number',
        'c': 'confidence_value',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('method_of_machine_assignment')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'uniform_resource_identifier': value.get('u'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'generation_agency': value.get('q'),
        'generation_date': value.get('d'),
        'validity_end_date': value.get('x'),
        'generation_process': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'confidence_value': value.get('c'),
        'method_of_machine_assignment': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('description_conversion_information', '^884..')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    field_map = {
        'a': 'conversion_process',
        'g': 'conversion_date',
        'q': 'conversion_agency',
        'k': 'identifier_of_source_metadata',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'conversion_process': value.get('a'),
        'conversion_date': value.get('g'),
        'conversion_agency': value.get('q'),
        'identifier_of_source_metadata': value.get('k'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('non_marc_information_field', '^887..')
@utils.for_each_value
@utils.filter_values
def non_marc_information_field(self, key, value):
    """Non-MARC Information Field."""
    field_map = {
        'a': 'content_of_non_marc_field',
        '2': 'source_of_data',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'content_of_non_marc_field': value.get('a'),
        'source_of_data': value.get('2'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
