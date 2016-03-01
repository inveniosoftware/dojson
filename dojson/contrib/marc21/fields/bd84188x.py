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


@marc21.over('holding_institution', '^850__')
@utils.for_each_value
@utils.filter_values
def holding_institution(self, key, value):
    """Holding Institution."""
    field_map = {
        'a': 'holding_institution',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'holding_institution': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('location', '^852[_012345678][_012]')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Library of Congress classification',
        '1': 'Dewey Decimal classification',
        '2': 'National Library of Medicine classification',
        '3': 'Superintendent of Documents classification',
        '4': 'Shelving control number',
        '5': 'Title',
        '6': 'Shelved separately',
        '7': 'Source specified in subfield $2',
        '8': 'Other scheme'}
    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Not enumeration',
        '1': 'Primary enumeration',
        '2': 'Alternative enumeration'
    }

    field_map = {
        'a': 'location',
        'b': 'sublocation_or_collection',
        'c': 'shelving_location',
        'd': 'former_shelving_location',
        'e': 'address',
        'f': 'coded_location_qualifier',
        'g': 'non_coded_location_qualifier',
        'h': 'classification_part',
        'i': 'item_part',
        'j': 'shelving_control_number',
        'k': 'call_number_prefix',
        'l': 'shelving_form_of_title',
        'm': 'call_number_suffix',
        'n': 'country_code',
        'p': 'piece_designation',
        'q': 'piece_physical_condition',
        's': 'copyright_article_fee_code',
        't': 'copy_number',
        'u': 'uniform_resource_identifier',
        'x': 'nonpublic_note',
        'z': 'public_note',
        '2': 'source_of_classification',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('shelving_scheme')
    if key[4] in indicator_map2:
        order.append('shelving_order')

    if key[3] == '7':
        order.remove('source_of_classification')

    return {
        '__order__': tuple(order) if len(order) else None,
        'location': value.get('a'),
        'sublocation_or_collection': utils.force_list(
            value.get('b')
        ),
        'shelving_location': utils.force_list(
            value.get('c')
        ),
        'former_shelving_location': utils.force_list(
            value.get('d')
        ),
        'address': utils.force_list(
            value.get('e')
        ),
        'coded_location_qualifier': utils.force_list(
            value.get('f')
        ),
        'non_coded_location_qualifier': utils.force_list(
            value.get('g')
        ),
        'classification_part': value.get('h'),
        'item_part': utils.force_list(
            value.get('i')
        ),
        'shelving_control_number': value.get('j'),
        'call_number_prefix': utils.force_list(
            value.get('k')
        ),
        'shelving_form_of_title': value.get('l'),
        'call_number_suffix': utils.force_list(
            value.get('m')
        ),
        'country_code': value.get('n'),
        'piece_designation': value.get('p'),
        'piece_physical_condition': value.get('q'),
        'copyright_article_fee_code': utils.force_list(
            value.get('s')
        ),
        'copy_number': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'source_of_classification': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'sequence_number': value.get('8'),
        'shelving_scheme':
        value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'shelving_order': indicator_map2.get(key[4]),
    }


@marc21.over('electronic_location_and_access', '^856[_012347][_0128]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Email',
        '1': 'FTP',
        '2': 'Remote login (Telnet)',
        '3': 'Dial-up',
        '4': 'HTTP',
        '7': 'Method specified in subfield $2'
    }
    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Resource',
        '1': 'Version of resource',
        '2': 'Related resource',
        '8': 'No display constant generated'
    }
    field_map = {
        'a': 'host_name',
        'b': 'access_number',
        'c': 'compression_information',
        'd': 'path',
        'f': 'electronic_name',
        'h': 'processor_of_request',
        'i': 'instruction',
        'j': 'bits_per_second',
        'k': 'password',
        'l': 'logon',
        'm': 'contact_for_access_assistance',
        'n': 'name_of_location_of_host',
        'o': 'operating_system',
        'p': 'port',
        'q': 'electronic_format_type',
        'r': 'settings',
        's': 'file_size',
        't': 'terminal_emulation',
        'u': 'uniform_resource_identifier',
        'v': 'hours_access_method_available',
        'w': 'record_control_number',
        'x': 'nonpublic_note',
        'y': 'link_text',
        'z': 'public_note',
        '2': 'access_method',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)
    if key[3] != '7' and key[3] in indicator_map1:
        order.append('access_method')
    if key[4] in indicator_map2:
        order.append('relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'host_name': utils.force_list(
            value.get('a')
        ),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'path': utils.force_list(
            value.get('d')
        ),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'processor_of_request': value.get('h'),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'bits_per_second': value.get('j'),
        'password': value.get('k'),
        'logon': value.get('l'),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'name_of_location_of_host': value.get('n'),
        'operating_system': value.get('o'),
        'port': value.get('p'),
        'electronic_format_type': value.get('q'),
        'settings': value.get('r'),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'hours_access_method_available': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'access_method':
        value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'relationship': indicator_map2.get(key[4]),
    }


@marc21.over('replacement_record_information', '^882__')
@utils.filter_values
def replacement_record_information(self, key, value):
    """Replacement Record Information."""
    field_map = {
        'a': 'replacement_title',
        'i': 'explanatory_text',
        'w': 'replacement_bibliographic_record_control_number',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'replacement_title': utils.force_list(
            value.get('a')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'replacement_bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('machine_generated_metadata_provenance', '^883[_01]_')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {
        '_': 'No information provided/not applicable',
        '0': 'Fully machine-generated',
        '1': 'Partially machine-generated'}

    field_map = {
        'a': 'generation_process',
        'c': 'confidence_value',
        'd': 'generation_date',
        'q': 'generation_agency',
        'x': 'validity_end_date',
        'u': 'uniform_resource_identifier',
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('method_of_machine_assignment')

    return {
        '__order__': tuple(order) if len(order) else None,
        'generation_process': value.get('a'),
        'confidence_value': value.get('c'),
        'generation_date': value.get('d'),
        'generation_agency': value.get('q'),
        'uniform_resource_identifier': value.get('u'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'validity_end_date': value.get('x'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'method_of_machine_assignment': indicator_map1.get(key[3]),
    }


@marc21.over('description_conversion_information', '^884__')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    field_map = {
        'a': 'conversion_process',
        'g': 'conversion_date',
        'k': 'identifier_of_source_metadata',
        'q': 'conversion_agency',
        'u': 'uniform_resource_identifier',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'conversion_process': value.get('a'),
        'conversion_date': value.get('g'),
        'identifier_of_source_metadata': value.get('k'),
        'conversion_agency': value.get('q'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@marc21.over('non_marc_information_field', '^887__')
@utils.for_each_value
@utils.filter_values
def non_marc_information_field(self, key, value):
    """Non-MARC Information Field."""
    field_map = {
        'a': 'content_of_non_marc_field',
        '2': 'source_of_data',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'content_of_non_marc_field': value.get('a'),
        'source_of_data': value.get('2'),
    }
