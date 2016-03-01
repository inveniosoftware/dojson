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

from ..model import to_marc21


@to_marc21.over('850', '^holding_institution$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_holding_institution(self, key, value):
    """Reverse - Holding Institution."""
    field_map = {
        'holding_institution': 'a',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('holding_institution')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('852', '^location$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location(self, key, value):
    """Reverse - Location."""
    indicator_map1 = {
        'No information provided': '_',
        'Library of Congress classification': '0',
        'Dewey Decimal classification': '1',
        'National Library of Medicine classification': '2',
        'Superintendent of Documents classification': '3',
        'Shelving control number': '4',
        'Title': '5',
        'Shelved separately': '6',
        'Source specified in subfield $2': '7',
        'Other scheme': '8'
    }
    indicator_map2 = {
        'No information provided': '_',
        'Not enumeration': '0',
        'Primary enumeration': '1',
        'Alternative enumeration': '2',
    }

    field_map = {
        'location': 'a',
        'sublocation_or_collection': 'b',
        'shelving_location': 'c',
        'former_shelving_location': 'd',
        'address': 'e',
        'coded_location_qualifier': 'f',
        'non_coded_location_qualifier': 'g',
        'classification_part': 'h',
        'item_part': 'i',
        'shelving_control_number': 'j',
        'call_number_prefix': 'k',
        'shelving_form_of_title': 'l',
        'call_number_suffix': 'm',
        'country_code': 'n',
        'piece_designation': 'p',
        'piece_physical_condition': 'q',
        'copyright_article_fee_code': 's',
        'copy_number': 't',
        'uniform_resource_identifier': 'u',
        'nonpublic_note': 'x',
        'public_note': 'z',
        'materials_specified': '3',
        'linkage': '6',
        'sequence_number': '8',
    }

    # Subfield '2' can be either called 'source_of_classification' or
    # 'shelving scheme', depending on the first indicator
    if indicator_map1.get(value.get('shelving_scheme'), '7') == '7':
        field_map['shelving_scheme'] = '2'
    else:
        field_map['source_of_classification'] = '2'

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('location'),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'h': value.get('classification_part'),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        'j': value.get('shelving_control_number'),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        'l': value.get('shelving_form_of_title'),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        'n': value.get('country_code'),
        'p': value.get('piece_designation'),
        'q': value.get('piece_physical_condition'),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        't': value.get('copy_number'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '2': value.get('shelving_scheme')
        if indicator_map1.get(value.get('shelving_scheme'), '7') == '7'
        else value.get('source_of_classification'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': value.get('sequence_number'),
        '$ind1': indicator_map1.get(value.get('shelving_scheme'), '7'),
        '$ind2': indicator_map2.get(value.get('shelving_order'), '_'),
    }


@to_marc21.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {
        'No information provided': '_',
        'Email': '0',
        'FTP': '1',
        'Remote login (Telnet)': '2',
        'Dial-up': '3',
        'HTTP': '4',
        'Method specified in subfield $2': '7',
    }
    indicator_map2 = {
        'No information provided': '_',
        'Resource': '0',
        'Version of resource': '1',
        'Related resource': '2',
        'No display constant generated': '8',
    }
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
    if indicator_map1.get(value.get('access_method'), '7') != '7':
        order.remove('2')

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
        '2': value.get('access_method')
        if indicator_map1.get(value.get('access_method'), '7') == '7'
        else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('access_method'), '7'),
        '$ind2': indicator_map2.get(value.get('relationship'), '_'),
    }


@to_marc21.over('882', '^replacement_record_information$')
@utils.filter_values
def reverse_replacement_record_information(self, key, value):
    """Reverse - Replacement Record Information."""
    field_map = {
        'replacement_title': 'a',
        'explanatory_text': 'i',
        'replacement_bibliographic_record_control_number': 'w',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('replacement_title')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        'w': utils.reverse_force_list(
            value.get('replacement_bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('883', '^machine_generated_metadata_provenance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {
        'No information provided/not applicable': '_',
        'Fully machine-generated': '0',
        'Partially machine-generated': '1'
    }
    field_map = {
        'generation_process': 'a',
        'confidence_value': 'c',
        'generation_date': 'd',
        'generation_agency': 'q',
        'validity_end_date': 'x',
        'uniform_resource_identifier': 'u',
        'bibliographic_record_control_number': 'w',
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
            value.get('bibliographic_record_control_number')),
        'x': value.get('validity_end_date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('method_of_machine_assignment'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('884', '^description_conversion_information$')
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


@to_marc21.over('887', '^non_marc_information_field$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_non_marc_information_field(self, key, value):
    """Reverse - Non-MARC Information Field."""
    field_map = {
        'content_of_non_marc_field': 'a',
        'source_of_data': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('content_of_non_marc_field'),
        '2': value.get('source_of_data'),
        '$ind1': '_',
        '$ind2': '_',
    }
