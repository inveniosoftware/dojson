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

from ..model import marc21, tomarc21


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


@tomarc21.over('^850..', 'holding_institution')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_holding_institution(self, key, value):
    """Reverse - Holding Institution."""
    return {
        'a': utils.reverse_force_list(value.get('holding_institution')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('location', '^852[_103254768][10_2]')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
    indicator_map1 = {"#": "No information provided", "0": "Library of Congress classification", "1": "Dewey Decimal classification", "2": "National Library of Medicine classification", "3": "Superintendent of Documents classification", "4": "Shelving control number", "5": "Title", "6": "Shelved separately", "7": "Source specified in subfield $2", "8": "Other scheme"}
    indicator_map2 = {"#": "No information provided", "0": "Not enumeration", "1": "Primary enumeration", "2": "Alternative enumeration"}
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


@tomarc21.over('^852[_103254768][10_2]', 'location')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location(self, key, value):
    """Reverse - Location."""
    indicator_map1 = {"Dewey Decimal classification": "1", "Library of Congress classification": "0", "National Library of Medicine classification": "2", "No information provided": "#", "Other scheme": "8", "Shelved separately": "6", "Shelving control number": "4", "Source specified in subfield $2": "7", "Superintendent of Documents classification": "3", "Title": "5"}
    indicator_map2 = {"Alternative enumeration": "2", "No information provided": "#", "Not enumeration": "0", "Primary enumeration": "1"}
    return {
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_classification_or_shelving_scheme')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('sequence_number')),
        'a': utils.reverse_force_list(value.get('location')),
        'c': utils.reverse_force_list(value.get('shelving_location')),
        'b': utils.reverse_force_list(value.get('sublocation_or_collection')),
        'e': utils.reverse_force_list(value.get('address')),
        'd': utils.reverse_force_list(value.get('former_shelving_location')),
        'g': utils.reverse_force_list(value.get('non_coded_location_qualifier')),
        'f': utils.reverse_force_list(value.get('coded_location_qualifier')),
        'i': utils.reverse_force_list(value.get('item_part')),
        'h': utils.reverse_force_list(value.get('classification_part')),
        'k': utils.reverse_force_list(value.get('call_number_prefix')),
        'j': utils.reverse_force_list(value.get('shelving_control_number')),
        'm': utils.reverse_force_list(value.get('call_number_suffix')),
        'l': utils.reverse_force_list(value.get('shelving_form_of_title')),
        'n': utils.reverse_force_list(value.get('country_code')),
        'q': utils.reverse_force_list(value.get('piece_physical_condition')),
        'p': utils.reverse_force_list(value.get('piece_designation')),
        's': utils.reverse_force_list(value.get('copyright_article_fee_code')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        't': utils.reverse_force_list(value.get('copy_number')),
        'x': utils.reverse_force_list(value.get('nonpublic_note')),
        'z': utils.reverse_force_list(value.get('public_note')),
        '_indicator1': indicator_map1.get(value.get('shelving_scheme')),
        '_indicator2': indicator_map2.get(value.get('shelving_order')),
    }


@marc21.over('electronic_location_and_access', '^856.[10_28]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
    indicator_map2 = {"#": "No information provided", "0": "Resource", "1": "Version of resource", "2": "Related resource", "8": "No display constant generated"}
    return {
        'materials_specified': value.get('3'),
        'access_method': value.get('2'),
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
    }


@tomarc21.over('^856.[10_28]', 'electronic_location_and_access')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_electronic_location_and_access(self, key, value):
    """Reverse - Electronic Location and Access."""
    indicator_map2 = {"No display constant generated": "8", "No information provided": "#", "Related resource": "2", "Resource": "0", "Version of resource": "1"}
    return {
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('access_method')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('host_name')),
        'c': utils.reverse_force_list(value.get('compression_information')),
        'b': utils.reverse_force_list(value.get('access_number')),
        'd': utils.reverse_force_list(value.get('path')),
        'f': utils.reverse_force_list(value.get('electronic_name')),
        'i': utils.reverse_force_list(value.get('instruction')),
        'h': utils.reverse_force_list(value.get('processor_of_request')),
        'k': utils.reverse_force_list(value.get('password')),
        'j': utils.reverse_force_list(value.get('bits_per_second')),
        'm': utils.reverse_force_list(value.get('contact_for_access_assistance')),
        'l': utils.reverse_force_list(value.get('logon')),
        'o': utils.reverse_force_list(value.get('operating_system')),
        'n': utils.reverse_force_list(value.get('name_of_location_of_host')),
        'q': utils.reverse_force_list(value.get('electronic_format_type')),
        'p': utils.reverse_force_list(value.get('port')),
        's': utils.reverse_force_list(value.get('file_size')),
        'r': utils.reverse_force_list(value.get('settings')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        't': utils.reverse_force_list(value.get('terminal_emulation')),
        'w': utils.reverse_force_list(value.get('record_control_number')),
        'v': utils.reverse_force_list(value.get('hours_access_method_available')),
        'y': utils.reverse_force_list(value.get('link_text')),
        'x': utils.reverse_force_list(value.get('nonpublic_note')),
        'z': utils.reverse_force_list(value.get('public_note')),
        '_indicator2': indicator_map2.get(value.get('relationship')),
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


@tomarc21.over('^882..', 'replacement_record_information')
@utils.filter_values
def reverse_replacement_record_information(self, key, value):
    """Reverse - Replacement Record Information."""
    return {
        'a': utils.reverse_force_list(value.get('replacement_title')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'i': utils.reverse_force_list(value.get('explanatory_text')),
        'w': utils.reverse_force_list(value.get('replacement_bibliographic_record_control_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {"#": "No information provided/not applicable", "0": "Fully machine-generated", "1": "Partially machine-generated"}
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


@tomarc21.over('^883[10_].', 'machine_generated_metadata_provenance')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_machine_generated_metadata_provenance(self, key, value):
    """Reverse - Machine-generated Metadata Provenance."""
    indicator_map1 = {"Fully machine-generated": "0", "No information provided/not applicable": "#", "Partially machine-generated": "1"}
    return {
        'a': utils.reverse_force_list(value.get('generation_process')),
        'c': utils.reverse_force_list(value.get('confidence_value')),
        'd': utils.reverse_force_list(value.get('generation_date')),
        'q': utils.reverse_force_list(value.get('generation_agency')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        'w': utils.reverse_force_list(value.get('bibliographic_record_control_number')),
        'x': utils.reverse_force_list(value.get('validity_end_date')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('method_of_machine_assignment')),
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


@tomarc21.over('^887..', 'non_marc_information_field')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_non_marc_information_field(self, key, value):
    """Reverse - Non-MARC Information Field."""
    return {
        'a': utils.reverse_force_list(value.get('content_of_non_marc_field')),
        '2': utils.reverse_force_list(value.get('source_of_data')),
    }
