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

from ..model import marc21_authority


@marc21_authority.over('electronic_location_and_access', '^856..')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    """Electronic Location and Access."""
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
    }


@marc21_authority.over('alternate_graphic_representation', '^880..')
@utils.for_each_value
@utils.filter_values
def alternate_graphic_representation(self, key, value):
    """Alternate Graphic Representation."""
    return {
        'same_as_associated_field': utils.force_list(
            value.get('1')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('0')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('3')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('2')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('5')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('4')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('7')
        ),
        'linkage': value.get('6'),
        'same_as_associated_field': utils.force_list(
            value.get('9')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('8')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('a')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('c')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('b')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('e')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('d')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('g')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('f')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('i')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('h')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('k')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('j')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('m')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('l')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('o')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('n')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('q')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('p')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('s')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('r')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('u')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('t')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('w')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('v')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('y')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('x')
        ),
        'same_as_associated_field': utils.force_list(
            value.get('z')
        ),
    }


@marc21_authority.over('machine_generated_metadata_provenance', '^883[10_].')
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


@marc21_authority.over('description_conversion_information', '^884..')
@utils.for_each_value
@utils.filter_values
def description_conversion_information(self, key, value):
    """Description Conversion Information."""
    return {
        'conversion_process': value.get('a'),
        'conversion_agency': value.get('q'),
        'identifier_of_source_metadata': value.get('k'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'conversion_date': value.get('g'),
    }
