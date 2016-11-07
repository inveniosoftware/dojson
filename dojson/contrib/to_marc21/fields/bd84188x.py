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
    indicator_map1 = {"Dewey Decimal classification": "1", "Library of Congress classification": "0", "National Library of Medicine classification": "2", "No information provided": "_", "Other scheme": "8", "Shelved separately": "6", "Shelving control number": "4", "Source specified in subfield $2": "7", "Superintendent of Documents classification": "3", "Title": "5"}
    indicator_map2 = {"Alternative enumeration": "2", "No information provided": "_", "Not enumeration": "0", "Primary enumeration": "1"}
    field_map = {
        'non_coded_location_qualifier': 'g',
        'location': 'a',
        'copy_number': 't',
        'coded_location_qualifier': 'f',
        'call_number_prefix': 'k',
        'sublocation_or_collection': 'b',
        'piece_physical_condition': 'q',
        'source_of_classification_or_shelving_scheme': '2',
        'classification_part': 'h',
        'materials_specified': '3',
        'shelving_control_number': 'j',
        'country_code': 'n',
        'shelving_location': 'c',
        'linkage': '6',
        'sequence_number': '8',
        'address': 'e',
        'uniform_resource_identifier': 'u',
        'public_note': 'z',
        'call_number_suffix': 'm',
        'shelving_form_of_title': 'l',
        'former_shelving_location': 'd',
        'item_part': 'i',
        'nonpublic_note': 'x',
        'copyright_article_fee_code': 's',
        'piece_designation': 'p',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'a': value.get('location'),
        't': value.get('copy_number'),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'q': value.get('piece_physical_condition'),
        '2': value.get('source_of_classification_or_shelving_scheme'),
        'h': value.get('classification_part'),
        '3': value.get('materials_specified'),
        'j': value.get('shelving_control_number'),
        'n': value.get('country_code'),
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        '6': value.get('linkage'),
        '8': value.get('sequence_number'),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        'l': value.get('shelving_form_of_title'),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        'p': value.get('piece_designation'),
        '$ind1': '7' if 'shelving_scheme' in value and
        not indicator_map1.get(value.get('shelving_scheme')) and
        value.get('shelving_scheme') == value.get('source_of_classification_or_shelving_scheme')
        else indicator_map1.get(value.get('shelving_scheme'), '_'),
        '$ind2': indicator_map2.get(value.get('shelving_order'), '_'),
    }


@to_marc21.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {"Dial-up": "3", "Email": "0", "FTP": "1", "HTTP": "4", "Method specified in subfield $2": "7", "No information provided": "_", "Remote login (Telnet)": "2"}
    indicator_map2 = {"No display constant generated": "8", "No information provided": "_", "Related resource": "2", "Resource": "0", "Version of resource": "1"}
    field_map = {
        'host_name': 'a',
        'record_control_number': 'w',
        'terminal_emulation': 't',
        'electronic_name': 'f',
        'password': 'k',
        'hours_access_method_available': 'v',
        'access_number': 'b',
        'link_text': 'y',
        'electronic_format_type': 'q',
        'access_method': '2',
        'materials_specified': '3',
        'processor_of_request': 'h',
        'path': 'd',
        'bits_per_second': 'j',
        'name_of_location_of_host': 'n',
        'nonpublic_note': 'x',
        'compression_information': 'c',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'public_note': 'z',
        'contact_for_access_assistance': 'm',
        'logon': 'l',
        'operating_system': 'o',
        'instruction': 'i',
        'port': 'p',
        'file_size': 's',
        'settings': 'r',
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
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'k': value.get('password'),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'q': value.get('electronic_format_type'),
        '2': value.get('access_method'),
        '3': value.get('materials_specified'),
        'h': value.get('processor_of_request'),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'j': value.get('bits_per_second'),
        'n': value.get('name_of_location_of_host'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'l': value.get('logon'),
        'o': value.get('operating_system'),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'p': value.get('port'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        'r': value.get('settings'),
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
        'explanatory_text': 'i',
        'replacement_title': 'a',
        'linkage': '6',
        'replacement_bibliographic_record_control_number': 'w',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        'a': utils.reverse_force_list(
            value.get('replacement_title')
        ),
        '6': value.get('linkage'),
        'w': utils.reverse_force_list(
            value.get('replacement_bibliographic_record_control_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('883', '^machine_generated_metadata_provenance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {"Fully machine-generated": "0", "No information provided/not applicable": "_", "Partially machine-generated": "1"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'generation_process': 'a',
        'bibliographic_record_control_number': 'w',
        'generation_agency': 'q',
        'generation_date': 'd',
        'uniform_resource_identifier': 'u',
        'validity_end_date': 'x',
        'confidence_value': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('generation_process'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'q': value.get('generation_agency'),
        'd': value.get('generation_date'),
        'u': value.get('uniform_resource_identifier'),
        'x': value.get('validity_end_date'),
        'c': value.get('confidence_value'),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'conversion_agency': 'q',
        'conversion_date': 'g',
        'conversion_process': 'a',
        'identifier_of_source_metadata': 'k',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('conversion_agency'),
        'g': value.get('conversion_date'),
        'a': value.get('conversion_process'),
        'k': value.get('identifier_of_source_metadata'),
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
