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
        'field_link_and_sequence_number': '8',
        'holding_institution': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('holding_institution')
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
        "Dewey Decimal classification": "1",
        "Library of Congress classification": "0",
        "National Library of Medicine classification": "2",
        "No information provided": "_",
        "Other scheme": "8",
        "Shelved separately": "6",
        "Shelving control number": "4",
        "Source specified in subfield $2": "7",
        "Superintendent of Documents classification": "3",
        "Title": "5"}
    indicator_map2 = {
        "Alternative enumeration": "2",
        "No information provided": "_",
        "Not enumeration": "0",
        "Primary enumeration": "1"}
    field_map = {
        'piece_designation': 'p',
        'shelving_form_of_title': 'l',
        'shelving_location': 'c',
        'piece_physical_condition': 'q',
        'sequence_number': '8',
        'address': 'e',
        'linkage': '6',
        'item_part': 'i',
        'copy_number': 't',
        'nonpublic_note': 'x',
        'copyright_article_fee_code': 's',
        'call_number_prefix': 'k',
        'materials_specified': '3',
        'sublocation_or_collection': 'b',
        'uniform_resource_identifier': 'u',
        'source_of_classification_or_shelving_scheme': '2',
        'call_number_suffix': 'm',
        'coded_location_qualifier': 'f',
        'former_shelving_location': 'd',
        'shelving_control_number': 'j',
        'country_code': 'n',
        'public_note': 'z',
        'location': 'a',
        'non_coded_location_qualifier': 'g',
        'classification_part': 'h',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('shelving_scheme'), '7') != '7':
        try:
            order.remove(field_map.get('shelving_scheme'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('shelving_order'), '7') != '7':
        try:
            order.remove(field_map.get('shelving_order'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': value.get('piece_designation'),
        'l': value.get('shelving_form_of_title'),
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        'q': value.get('piece_physical_condition'),
        '8': value.get('sequence_number'),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        't': value.get('copy_number'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '2': value.get('source_of_classification_or_shelving_scheme'),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        'j': value.get('shelving_control_number'),
        'n': value.get('country_code'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'a': value.get('location'),
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'h': value.get('classification_part'),
        '$ind1': '7' if 'shelving_scheme' in value and
        not indicator_map1.get(value.get('shelving_scheme')) and
        value.get('shelving_scheme') == value.get(
            'source_of_classification_or_shelving_scheme')
        else indicator_map1.get(value.get('shelving_scheme'), '_'),
        '$ind2': indicator_map2.get(value.get('shelving_order'), '_'),
    }


@to_marc21.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {
        "Dial-up": "3",
        "Email": "0",
        "FTP": "1",
        "HTTP": "4",
        "Method specified in subfield $2": "7",
        "No information provided": "_",
        "Remote login (Telnet)": "2"}
    indicator_map2 = {
        "No display constant generated": "8",
        "No information provided": "_",
        "Related resource": "2",
        "Resource": "0",
        "Version of resource": "1"}
    field_map = {
        'port': 'p',
        'logon': 'l',
        'compression_information': 'c',
        'electronic_format_type': 'q',
        'field_link_and_sequence_number': '8',
        'record_control_number': 'w',
        'linkage': '6',
        'instruction': 'i',
        'terminal_emulation': 't',
        'nonpublic_note': 'x',
        'file_size': 's',
        'hours_access_method_available': 'v',
        'password': 'k',
        'materials_specified': '3',
        'access_number': 'b',
        'uniform_resource_identifier': 'u',
        'access_method': '2',
        'contact_for_access_assistance': 'm',
        'electronic_name': 'f',
        'path': 'd',
        'settings': 'r',
        'operating_system': 'o',
        'bits_per_second': 'j',
        'name_of_location_of_host': 'n',
        'public_note': 'z',
        'host_name': 'a',
        'processor_of_request': 'h',
        'link_text': 'y',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('access_method'), '7') != '7':
        try:
            order.remove(field_map.get('access_method'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('relationship'), '7') != '7':
        try:
            order.remove(field_map.get('relationship'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'p': value.get('port'),
        'l': value.get('logon'),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'q': value.get('electronic_format_type'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'k': value.get('password'),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '2': value.get('access_method'),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'r': value.get('settings'),
        'o': value.get('operating_system'),
        'j': value.get('bits_per_second'),
        'n': value.get('name_of_location_of_host'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'h': value.get('processor_of_request'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        '$ind1': '7' if 'access_method' in value and
        not indicator_map1.get(value.get('access_method')) and
        value.get('access_method') == value.get('access_method')
        else indicator_map1.get(value.get('access_method'), '_'),
        '$ind2': indicator_map2.get(value.get('relationship'), '_'),
    }


@to_marc21.over('882', '^replacement_record_information$')
@utils.filter_values
def reverse_replacement_record_information(self, key, value):
    """Reverse - Replacement Record Information."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'replacement_bibliographic_record_control_number': 'w',
        'replacement_title': 'a',
        'linkage': '6',
        'explanatory_text': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': utils.reverse_force_list(
            value.get('replacement_bibliographic_record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('replacement_title')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
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
        "Fully machine-generated": "0",
        "No information provided/not applicable": "_",
        "Partially machine-generated": "1"}
    field_map = {
        'validity_end_date': 'x',
        'generation_process': 'a',
        'confidence_value': 'c',
        'generation_agency': 'q',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'bibliographic_record_control_number': 'w',
        'generation_date': 'd',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('method_of_machine_assignment'), '7') != '7':
        try:
            order.remove(field_map.get('method_of_machine_assignment'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'x': value.get('validity_end_date'),
        'a': value.get('generation_process'),
        'c': value.get('confidence_value'),
        'q': value.get('generation_agency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'd': value.get('generation_date'),
        'u': value.get('uniform_resource_identifier'),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'identifier_of_source_metadata': 'k',
        'conversion_agency': 'q',
        'conversion_process': 'a',
        'conversion_date': 'g',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'k': value.get('identifier_of_source_metadata'),
        'q': value.get('conversion_agency'),
        'a': value.get('conversion_process'),
        'g': value.get('conversion_date'),
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
        'source_of_data': '2',
        'content_of_non_marc_field': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_data'),
        'a': value.get('content_of_non_marc_field'),
        '$ind1': '_',
        '$ind2': '_',
    }
