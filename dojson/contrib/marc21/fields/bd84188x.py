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


@marc21.over('holding_institution', '^850..')
@utils.for_each_value
@utils.filter_values
def holding_institution(self, key, value):
    """Holding Institution."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        'a': 'holding_institution',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'holding_institution': utils.force_list(
            value.get('a')
        ),
    }


@marc21.over('location', '^852[05_3168724][102_]')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
    indicator_map1 = {
        "0": "Library of Congress classification",
        "1": "Dewey Decimal classification",
        "2": "National Library of Medicine classification",
        "3": "Superintendent of Documents classification",
        "4": "Shelving control number",
        "5": "Title",
        "6": "Shelved separately",
        "7": "Source specified in subfield $2",
        "8": "Other scheme",
        "_": "No information provided"}
    indicator_map2 = {
        "0": "Not enumeration",
        "1": "Primary enumeration",
        "2": "Alternative enumeration",
        "_": "No information provided"}
    field_map = {
        'g': 'non_coded_location_qualifier',
        'i': 'item_part',
        'e': 'address',
        'u': 'uniform_resource_identifier',
        'h': 'classification_part',
        '6': 'linkage',
        'q': 'piece_physical_condition',
        'd': 'former_shelving_location',
        'f': 'coded_location_qualifier',
        'n': 'country_code',
        'a': 'location',
        'c': 'shelving_location',
        '2': 'source_of_classification_or_shelving_scheme',
        't': 'copy_number',
        'l': 'shelving_form_of_title',
        '3': 'materials_specified',
        'b': 'sublocation_or_collection',
        'p': 'piece_designation',
        'z': 'public_note',
        'm': 'call_number_suffix',
        'j': 'shelving_control_number',
        '8': 'sequence_number',
        'k': 'call_number_prefix',
        's': 'copyright_article_fee_code',
        'x': 'nonpublic_note',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('shelving_scheme')

    if key[4] in indicator_map2:
        order.append('shelving_order')

    return {
        '__order__': tuple(order) if len(order) else None,
        'non_coded_location_qualifier': utils.force_list(
            value.get('g')
        ),
        'item_part': utils.force_list(
            value.get('i')
        ),
        'address': utils.force_list(
            value.get('e')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'classification_part': value.get('h'),
        'linkage': value.get('6'),
        'piece_physical_condition': value.get('q'),
        'former_shelving_location': utils.force_list(
            value.get('d')
        ),
        'coded_location_qualifier': utils.force_list(
            value.get('f')
        ),
        'country_code': value.get('n'),
        'location': value.get('a'),
        'shelving_location': utils.force_list(
            value.get('c')
        ),
        'source_of_classification_or_shelving_scheme': value.get('2'),
        'copy_number': value.get('t'),
        'shelving_form_of_title': value.get('l'),
        'materials_specified': value.get('3'),
        'sublocation_or_collection': utils.force_list(
            value.get('b')
        ),
        'piece_designation': value.get('p'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'call_number_suffix': utils.force_list(
            value.get('m')
        ),
        'shelving_control_number': value.get('j'),
        'sequence_number': value.get('8'),
        'call_number_prefix': utils.force_list(
            value.get('k')
        ),
        'copyright_article_fee_code': utils.force_list(
            value.get('s')
        ),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'shelving_scheme': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'shelving_order': indicator_map2.get(key[4]),
    }


@marc21.over('electronic_location_and_access', '^856[073142_][0812_]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {
        "0": "Email",
        "1": "FTP",
        "2": "Remote login (Telnet)",
        "3": "Dial-up",
        "4": "HTTP",
        "7": "Method specified in subfield $2",
        "_": "No information provided"}
    indicator_map2 = {
        "0": "Resource",
        "1": "Version of resource",
        "2": "Related resource",
        "8": "No display constant generated",
        "_": "No information provided"}
    field_map = {
        'w': 'record_control_number',
        'i': 'instruction',
        'z': 'public_note',
        'u': 'uniform_resource_identifier',
        'h': 'processor_of_request',
        '6': 'linkage',
        'q': 'electronic_format_type',
        'd': 'path',
        'f': 'electronic_name',
        'n': 'name_of_location_of_host',
        'a': 'host_name',
        'v': 'hours_access_method_available',
        'c': 'compression_information',
        'y': 'link_text',
        '2': 'access_method',
        't': 'terminal_emulation',
        'l': 'logon',
        's': 'file_size',
        '3': 'materials_specified',
        'b': 'access_number',
        'p': 'port',
        'o': 'operating_system',
        'm': 'contact_for_access_assistance',
        'j': 'bits_per_second',
        '8': 'field_link_and_sequence_number',
        'k': 'password',
        'r': 'settings',
        'x': 'nonpublic_note',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1 and '2' not in value:
        order.append('access_method')

    if key[4] in indicator_map2:
        order.append('relationship')

    return {
        '__order__': tuple(order) if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'processor_of_request': value.get('h'),
        'linkage': value.get('6'),
        'electronic_format_type': value.get('q'),
        'path': utils.force_list(
            value.get('d')
        ),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'name_of_location_of_host': value.get('n'),
        'host_name': utils.force_list(
            value.get('a')
        ),
        'hours_access_method_available': utils.force_list(
            value.get('v')
        ),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'logon': value.get('l'),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'materials_specified': value.get('3'),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'port': value.get('p'),
        'operating_system': value.get('o'),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'bits_per_second': value.get('j'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'password': value.get('k'),
        'settings': value.get('r'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'access_method': value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'relationship': indicator_map2.get(key[4]),
    }


@marc21.over('replacement_record_information', '^882..')
@utils.filter_values
def replacement_record_information(self, key, value):
    """Replacement Record Information."""
    field_map = {
        'a': 'replacement_title',
        '8': 'field_link_and_sequence_number',
        'i': 'explanatory_text',
        '6': 'linkage',
        'w': 'replacement_bibliographic_record_control_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'replacement_title': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'linkage': value.get('6'),
        'replacement_bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
    }


@marc21.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {
        "0": "Fully machine-generated",
        "1": "Partially machine-generated",
        "_": "No information provided/not applicable"}
    field_map = {
        'w': 'bibliographic_record_control_number',
        '0': 'authority_record_control_number_or_standard_number',
        'a': 'generation_process',
        'x': 'validity_end_date',
        'c': 'confidence_value',
        '8': 'field_link_and_sequence_number',
        'u': 'uniform_resource_identifier',
        'q': 'generation_agency',
        'd': 'generation_date',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('method_of_machine_assignment')

    return {
        '__order__': tuple(order) if len(order) else None,
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'generation_process': value.get('a'),
        'validity_end_date': value.get('x'),
        'confidence_value': value.get('c'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': value.get('u'),
        'generation_agency': value.get('q'),
        'generation_date': value.get('d'),
        'method_of_machine_assignment': indicator_map1.get(key[3]),
    }


@marc21.over('description_conversion_information', '^884..')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    field_map = {
        'u': 'uniform_resource_identifier',
        'g': 'conversion_date',
        'q': 'conversion_agency',
        'a': 'conversion_process',
        'k': 'identifier_of_source_metadata',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'conversion_date': value.get('g'),
        'conversion_agency': value.get('q'),
        'conversion_process': value.get('a'),
        'identifier_of_source_metadata': value.get('k'),
    }


@marc21.over('non_marc_information_field', '^887..')
@utils.for_each_value
@utils.filter_values
def non_marc_information_field(self, key, value):
    """Non-MARC Information Field."""
    field_map = {
        '2': 'source_of_data',
        'a': 'content_of_non_marc_field',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_data': value.get('2'),
        'content_of_non_marc_field': value.get('a'),
    }
