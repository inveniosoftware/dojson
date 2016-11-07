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

from ..model import to_marc21_liberal


@to_marc21_liberal.over('850', '^holding_institution$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_holding_institution(self, key, value):
    """Reverse - Holding Institution."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'holding_institution': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('holding_institution')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('852', '^location$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location(self, key, value):
    """Reverse - Location."""
    indicator_map1 = {"Dewey Decimal classification": "1", "Library of Congress classification": "0", "National Library of Medicine classification": "2", "No information provided": "_", "Other scheme": "8", "Shelved separately": "6", "Shelving control number": "4", "Source specified in subfield $2": "7", "Superintendent of Documents classification": "3", "Title": "5"}
    indicator_map2 = {"Alternative enumeration": "2", "No information provided": "_", "Not enumeration": "0", "Primary enumeration": "1"}
    field_map = {
        'shelving_location': 'c',
        'location': 'a',
        'shelving_control_number': 'j',
        'address': 'e',
        'public_note': 'z',
        'piece_designation': 'p',
        'country_code': 'n',
        'sublocation_or_collection': 'b',
        'piece_physical_condition': 'q',
        'copyright_article_fee_code': 's',
        'source_of_classification_or_shelving_scheme': '2',
        'linkage': '6',
        'shelving_form_of_title': 'l',
        'nonpublic_note': 'x',
        'non_coded_location_qualifier': 'g',
        'classification_part': 'h',
        'uniform_resource_identifier': 'u',
        'call_number_suffix': 'm',
        'copy_number': 't',
        'call_number_prefix': 'k',
        'item_part': 'i',
        'materials_specified': '3',
        'sequence_number': '8',
        'former_shelving_location': 'd',
        'coded_location_qualifier': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['shelving_scheme', 'shelving_order'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        'a': value.get('location'),
        'j': value.get('shelving_control_number'),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'p': value.get('piece_designation'),
        'n': value.get('country_code'),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'q': value.get('piece_physical_condition'),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        '2': value.get('source_of_classification_or_shelving_scheme'),
        '6': value.get('linkage'),
        'l': value.get('shelving_form_of_title'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'h': value.get('classification_part'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        't': value.get('copy_number'),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        '3': value.get('materials_specified'),
        '8': value.get('sequence_number'),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        '$ind1': '7' if 'shelving_scheme' in value and
        not indicator_map1.get(value.get('shelving_scheme')) and
        value.get('shelving_scheme') == value.get('source_of_classification_or_shelving_scheme') and
        field_map.get('shelving_scheme') in order
        else indicator_map1.get(value.get('shelving_scheme'), value.get('shelving_scheme', '_')),
        '$ind2': indicator_map2.get(value.get('shelving_order'), value.get('shelving_order', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('856', '^electronic_location_and_access$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map1 = {"Dial-up": "3", "Email": "0", "FTP": "1", "HTTP": "4", "Method specified in subfield $2": "7", "No information provided": "_", "Remote login (Telnet)": "2"}
    indicator_map2 = {"No display constant generated": "8", "No information provided": "_", "Related resource": "2", "Resource": "0", "Version of resource": "1"}
    field_map = {
        'compression_information': 'c',
        'host_name': 'a',
        'bits_per_second': 'j',
        'hours_access_method_available': 'v',
        'port': 'p',
        'name_of_location_of_host': 'n',
        'access_number': 'b',
        'electronic_format_type': 'q',
        'file_size': 's',
        'access_method': '2',
        'linkage': '6',
        'logon': 'l',
        'record_control_number': 'w',
        'nonpublic_note': 'x',
        'link_text': 'y',
        'processor_of_request': 'h',
        'settings': 'r',
        'uniform_resource_identifier': 'u',
        'contact_for_access_assistance': 'm',
        'public_note': 'z',
        'terminal_emulation': 't',
        'password': 'k',
        'electronic_name': 'f',
        'instruction': 'i',
        'materials_specified': '3',
        'field_link_and_sequence_number': '8',
        'path': 'd',
        'operating_system': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['access_method', 'relationship'])

    if (indicator_map1.get(value.get('access_method'), '7') != '7' or len(value.get('access_method', '')) == 1) and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'j': value.get('bits_per_second'),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'p': value.get('port'),
        'n': value.get('name_of_location_of_host'),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'q': value.get('electronic_format_type'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        '2': value.get('access_method'),
        '6': value.get('linkage'),
        'l': value.get('logon'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'h': value.get('processor_of_request'),
        'r': value.get('settings'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'k': value.get('password'),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        '3': value.get('materials_specified'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'o': value.get('operating_system'),
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


@to_marc21_liberal.over('882', '^replacement_record_information$')
@utils.filter_values
def reverse_replacement_record_information(self, key, value):
    """Reverse - Replacement Record Information."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'replacement_bibliographic_record_control_number': 'w',
        'replacement_title': 'a',
        'explanatory_text': 'i',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'w': utils.reverse_force_list(
            value.get('replacement_bibliographic_record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('replacement_title')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('883', '^machine_generated_metadata_provenance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {"Fully machine-generated": "0", "No information provided/not applicable": "_", "Partially machine-generated": "1"}
    field_map = {
        'confidence_value': 'c',
        'generation_process': 'a',
        'bibliographic_record_control_number': 'w',
        'validity_end_date': 'x',
        'uniform_resource_identifier': 'u',
        'field_link_and_sequence_number': '8',
        'generation_agency': 'q',
        'generation_date': 'd',
        'authority_record_control_number_or_standard_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['method_of_machine_assignment', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('confidence_value'),
        'a': value.get('generation_process'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        'x': value.get('validity_end_date'),
        'u': value.get('uniform_resource_identifier'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('generation_agency'),
        'd': value.get('generation_date'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '$ind1': indicator_map1.get(value.get('method_of_machine_assignment'), value.get('method_of_machine_assignment', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('884', '^description_conversion_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_description_conversion_information(self, key, value):
    """Reverse - Description Conversion Information."""
    field_map = {
        'conversion_date': 'g',
        'identifier_of_source_metadata': 'k',
        'conversion_process': 'a',
        'conversion_agency': 'q',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': value.get('conversion_date'),
        'k': value.get('identifier_of_source_metadata'),
        'a': value.get('conversion_process'),
        'q': value.get('conversion_agency'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('887', '^non_marc_information_field$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_non_marc_information_field(self, key, value):
    """Reverse - Non-MARC Information Field."""
    field_map = {
        'content_of_non_marc_field': 'a',
        'source_of_data': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('content_of_non_marc_field'),
        '2': value.get('source_of_data'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
