# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
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
    return {
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
    return {
        '3': value.get('materials_specified'),
        '2': value.get('source_of_classification_or_shelving_scheme'),
        '6': value.get('linkage'),
        '8': value.get('sequence_number'),
        'a': value.get('location'),
        'c': utils.reverse_force_list(
            value.get('shelving_location')
        ),
        'b': utils.reverse_force_list(
            value.get('sublocation_or_collection')
        ),
        'e': utils.reverse_force_list(
            value.get('address')
        ),
        'd': utils.reverse_force_list(
            value.get('former_shelving_location')
        ),
        'g': utils.reverse_force_list(
            value.get('non_coded_location_qualifier')
        ),
        'f': utils.reverse_force_list(
            value.get('coded_location_qualifier')
        ),
        'i': utils.reverse_force_list(
            value.get('item_part')
        ),
        'h': value.get('classification_part'),
        'k': utils.reverse_force_list(
            value.get('call_number_prefix')
        ),
        'j': value.get('shelving_control_number'),
        'm': utils.reverse_force_list(
            value.get('call_number_suffix')
        ),
        'l': value.get('shelving_form_of_title'),
        'n': value.get('country_code'),
        'q': value.get('piece_physical_condition'),
        'p': value.get('piece_designation'),
        's': utils.reverse_force_list(
            value.get('copyright_article_fee_code')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('copy_number'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '$ind1': indicator_map1.get(value.get('shelving_scheme'), '_'),
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
    return {
        '3': value.get('materials_specified'),
        '2': value.get('access_method')
        if indicator_map1.get(value.get('access_method'), '7') == '7'
        else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('host_name')
        ),
        'c': utils.reverse_force_list(
            value.get('compression_information')
        ),
        'b': utils.reverse_force_list(
            value.get('access_number')
        ),
        'd': utils.reverse_force_list(
            value.get('path')
        ),
        'f': utils.reverse_force_list(
            value.get('electronic_name')
        ),
        'i': utils.reverse_force_list(
            value.get('instruction')
        ),
        'h': value.get('processor_of_request'),
        'k': value.get('password'),
        'j': value.get('bits_per_second'),
        'm': utils.reverse_force_list(
            value.get('contact_for_access_assistance')
        ),
        'l': value.get('logon'),
        'o': value.get('operating_system'),
        'n': value.get('name_of_location_of_host'),
        'q': value.get('electronic_format_type'),
        'p': value.get('port'),
        's': utils.reverse_force_list(
            value.get('file_size')
        ),
        'r': value.get('settings'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': utils.reverse_force_list(
            value.get('terminal_emulation')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'v': utils.reverse_force_list(
            value.get('hours_access_method_available')
        ),
        'y': utils.reverse_force_list(
            value.get('link_text')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '$ind1': indicator_map1.get(value.get('access_method'), '7'),
        '$ind2': indicator_map2.get(value.get('relationship'), '_'),
    }


@to_marc21.over('882', '^replacement_record_information$')
@utils.filter_values
def reverse_replacement_record_information(self, key, value):
    """Reverse - Replacement Record Information."""
    return {
        'a': utils.reverse_force_list(
            value.get('replacement_title')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        'w': utils.reverse_force_list(
            value.get('replacement_bibliographic_record_control_number')
        ),
        '6': value.get('linkage'),
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
    return {
        'a': value.get('generation_process'),
        'c': value.get('confidence_value'),
        'd': value.get('generation_date'),
        'q': value.get('generation_agency'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        'u': value.get('uniform_resource_identifier'),
        'w': utils.reverse_force_list(
            value.get('bibliographic_record_control_number')),
        'x': value.get('validity_end_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('method_of_machine_assignment'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('887', '^non_marc_information_field$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_non_marc_information_field(self, key, value):
    """Reverse - Non-MARC Information Field."""
    return {
        'a': value.get('content_of_non_marc_field'),
        '2': value.get('source_of_data'),
        '$ind1': '_',
        '$ind2': '_',
    }
