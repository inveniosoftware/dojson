# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
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
    return {
        'holding_institution': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('location', '^852[_103254768][10_2]')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Library of Congress classification",
        "1": "Dewey Decimal classification",
        "2": "National Library of Medicine classification",
        "3": "Superintendent of Documents classification",
        "4": "Shelving control number",
        "5": "Title",
        "6": "Shelved separately",
        "7": "Source specified in subfield $2",
        "8": "Other scheme"}
    indicator_map2 = {
        "#": "No information provided",
        "0": "Not enumeration",
        "1": "Primary enumeration",
        "2": "Alternative enumeration"}
    return {
        'materials_specified': value.get('3'),
        'source_of_classification_or_shelving_scheme': value.get('2'),
        'linkage': value.get('6'),
        'sequence_number': value.get('8'),
        'location': value.get('a'),
        'shelving_location': utils.force_list(
            value.get('c')
        ),
        'sublocation_or_collection': utils.force_list(
            value.get('b')
        ),
        'address': utils.force_list(
            value.get('e')
        ),
        'former_shelving_location': utils.force_list(
            value.get('d')
        ),
        'non_coded_location_qualifier': utils.force_list(
            value.get('g')
        ),
        'coded_location_qualifier': utils.force_list(
            value.get('f')
        ),
        'item_part': utils.force_list(
            value.get('i')
        ),
        'classification_part': value.get('h'),
        'call_number_prefix': utils.force_list(
            value.get('k')
        ),
        'shelving_control_number': value.get('j'),
        'call_number_suffix': utils.force_list(
            value.get('m')
        ),
        'shelving_form_of_title': value.get('l'),
        'country_code': value.get('n'),
        'piece_physical_condition': value.get('q'),
        'piece_designation': value.get('p'),
        'copyright_article_fee_code': utils.force_list(
            value.get('s')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'copy_number': value.get('t'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'shelving_scheme': indicator_map1.get(key[3]),
        'shelving_order': indicator_map2.get(key[4]),
    }


@marc21.over('electronic_location_and_access', '^856[10_2473][10_28]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Email",
        "1": "FTP",
        "2": "Remote login (Telnet)",
        "3": "Dial-up",
        "4": "HTTP",
        "7": "Method specified in subfield $2"}
    indicator_map2 = {
        "#": "No information provided",
        "0": "Resource",
        "1": "Version of resource",
        "2": "Related resource",
        "8": "No display constant generated"}
    field_map = {
        '3': 'materials_specified',
        '2': 'access_method',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'host_name',
        'c': 'compression_information',
        'b': 'access_number',
        'd': 'path',
        'f': 'electronic_name',
        'i': 'instruction',
        'h': 'processor_of_request',
        'k': 'password',
        'j': 'bits_per_second',
        'm': 'contact_for_access_assistance',
        'l': 'logon',
        'o': 'operating_system',
        'n': 'name_of_location_of_host',
        'p': 'port',
        'q': 'electronic_format_type',
        's': 'file_size',
        'r': 'settings',
        'u': 'uniform_resource_identifier',
        't': 'terminal_emulation',
        'v': 'hours_access_method_available',
        'w': 'record_control_number',
        'x': 'nonpublic_note',
        'z': 'public_note'
    }
    return {
        'materials_specified': value.get('3'),
        'access_method':
        value.get('2') if key[3] == '7' else indicator_map1.get(key[3]),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'host_name': utils.force_list(
            value.get('a')
        ),
        'compression_information': utils.force_list(
            value.get('c')
        ),
        'access_number': utils.force_list(
            value.get('b')
        ),
        'path': utils.force_list(
            value.get('d')
        ),
        'electronic_name': utils.force_list(
            value.get('f')
        ),
        'instruction': utils.force_list(
            value.get('i')
        ),
        'processor_of_request': value.get('h'),
        'password': value.get('k'),
        'bits_per_second': value.get('j'),
        'contact_for_access_assistance': utils.force_list(
            value.get('m')
        ),
        'logon': value.get('l'),
        'operating_system': value.get('o'),
        'name_of_location_of_host': value.get('n'),
        'electronic_format_type': value.get('q'),
        'port': value.get('p'),
        'file_size': utils.force_list(
            value.get('s')
        ),
        'settings': value.get('r'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'terminal_emulation': utils.force_list(
            value.get('t')
        ),
        'record_control_number': utils.force_list(
            value.get('w')
        ),
        'hours_access_method_available': utils.force_list(
            value.get('v')
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
        'relationship': indicator_map2.get(key[4]),
        '__order__': tuple([field_map[k] for k in value['__order__']]) if '__order__' in value else None,
    }


@marc21.over('replacement_record_information', '^882..')
@utils.filter_values
def replacement_record_information(self, key, value):
    """Replacement Record Information."""
    return {
        'replacement_title': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'explanatory_text': utils.force_list(
            value.get('i')
        ),
        'replacement_bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {
        "#": "No information provided/not applicable",
        "0": "Fully machine-generated",
        "1": "Partially machine-generated"}
    return {
        'generation_process': value.get('a'),
        'confidence_value': value.get('c'),
        'generation_date': value.get('d'),
        'generation_agency': value.get('q'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'uniform_resource_identifier': value.get('u'),
        'bibliographic_record_control_number': utils.force_list(
            value.get('w')
        ),
        'validity_end_date': value.get('x'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'method_of_machine_assignment': indicator_map1.get(key[3]),
    }


@marc21.over('non_marc_information_field', '^887..')
@utils.for_each_value
@utils.filter_values
def non_marc_information_field(self, key, value):
    """Non-MARC Information Field."""
    return {
        'content_of_non_marc_field': value.get('a'),
        'source_of_data': value.get('2'),
    }
