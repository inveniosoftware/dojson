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
        'shelving_form_of_title': 'l',
        'piece_designation': 'p',
        'sublocation_or_collection': 'b',
        'non_coded_location_qualifier': 'g',
        'former_shelving_location': 'd',
        'materials_specified': '3',
        'country_code': 'n',
        'coded_location_qualifier': 'f',
        'address': 'e',
        'call_number_suffix': 'm',
        'public_note': 'z',
        'call_number_prefix': 'k',
        'sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'location': 'a',
        'item_part': 'i',
        'classification_part': 'h',
        'nonpublic_note': 'x',
        'copy_number': 't',
        'source_of_classification_or_shelving_scheme': '2',
        'copyright_article_fee_code': 's',
        'linkage': '6',
        'piece_physical_condition': 'q',
        'shelving_location': 'c',
        'shelving_control_number': 'j',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['shelving_scheme', 'shelving_order'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('shelving_form_of_title'),
        'p': value.get('piece_designation'),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        '3': value.get('materials_specified'),
        'n': value.get('country_code'),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        '8': value.get('sequence_number'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': value.get('location'),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        'h': value.get('classification_part'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        't': value.get('copy_number'),
        '2': value.get('source_of_classification_or_shelving_scheme'),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        '6': value.get('linkage'),
        'q': value.get('piece_physical_condition'),
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        'j': value.get('shelving_control_number'),
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
        'logon': 'l',
        'port': 'p',
        'access_number': 'b',
        'record_control_number': 'w',
        'hours_access_method_available': 'v',
        'path': 'd',
        'materials_specified': '3',
        'name_of_location_of_host': 'n',
        'link_text': 'y',
        'electronic_name': 'f',
        'contact_for_access_assistance': 'm',
        'public_note': 'z',
        'password': 'k',
        'field_link_and_sequence_number': '8',
        'operating_system': 'o',
        'settings': 'r',
        'uniform_resource_identifier': 'u',
        'host_name': 'a',
        'instruction': 'i',
        'processor_of_request': 'h',
        'nonpublic_note': 'x',
        'terminal_emulation': 't',
        'access_method': '2',
        'file_size': 's',
        'linkage': '6',
        'electronic_format_type': 'q',
        'compression_information': 'c',
        'bits_per_second': 'j',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['access_method', 'relationship'])

    if (indicator_map1.get(value.get('access_method'), '7') != '7' or len(value.get('access_method', '')) == 1) and\
            field_map.get('access_method'):
        order.remove(field_map.get('access_method'))

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'l': value.get('logon'),
        'p': value.get('port'),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        '3': value.get('materials_specified'),
        'n': value.get('name_of_location_of_host'),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'k': value.get('password'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'o': value.get('operating_system'),
        'r': value.get('settings'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'h': value.get('processor_of_request'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        '2': value.get('access_method'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        '6': value.get('linkage'),
        'q': value.get('electronic_format_type'),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'j': value.get('bits_per_second'),
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
        'explanatory_text': 'i',
        'replacement_bibliographic_record_control_number': 'w',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'replacement_title': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
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
        'a': utils.reverse_force_list(
            value.get('replacement_title')
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
        'uniform_resource_identifier': 'u',
        'bibliographic_record_control_number': 'w',
        'field_link_and_sequence_number': '8',
        'generation_process': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'validity_end_date': 'x',
        'generation_date': 'd',
        'confidence_value': 'c',
        'generation_agency': 'q',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['method_of_machine_assignment', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': value.get('uniform_resource_identifier'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('generation_process'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': value.get('validity_end_date'),
        'd': value.get('generation_date'),
        'c': value.get('confidence_value'),
        'q': value.get('generation_agency'),
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
        'uniform_resource_identifier': 'u',
        'identifier_of_source_metadata': 'k',
        'conversion_date': 'g',
        'conversion_agency': 'q',
        'conversion_process': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'k': value.get('identifier_of_source_metadata'),
        'g': value.get('conversion_date'),
        'q': value.get('conversion_agency'),
        'a': value.get('conversion_process'),
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
        'source_of_data': '2',
        'content_of_non_marc_field': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source_of_data'),
        'a': value.get('content_of_non_marc_field'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
