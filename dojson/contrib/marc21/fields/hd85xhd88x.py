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

from ..model import marc21_holdings


@marc21_holdings.over('location', '^852..')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    """Location."""
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
        'coded_location_qualifier_\n': utils.force_list(
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
    }


@marc21_holdings.over(
    'captions_and_pattern_basic_bibliographic_unit',
    '^853..')
@utils.for_each_value
@utils.filter_values
def captions_and_pattern_basic_bibliographic_unit(self, key, value):
    """Captions and Pattern-Basic Bibliographic Unit."""
    return {
    }


@marc21_holdings.over('captions_and_pattern_supplementary_material', '^854..')
@utils.for_each_value
@utils.filter_values
def captions_and_pattern_supplementary_material(self, key, value):
    """Captions and Pattern-Supplementary Material."""
    return {
    }


@marc21_holdings.over('captions_and_pattern_indexes', '^855..')
@utils.for_each_value
@utils.filter_values
def captions_and_pattern_indexes(self, key, value):
    """Captions and Pattern-Indexes."""
    return {
    }


@marc21_holdings.over('electronic_location_and_access', '^856..')
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


@marc21_holdings.over(
    'enumeration_and_chronology_basic_bibliographic_unit',
    '^863..')
@utils.for_each_value
@utils.filter_values
def enumeration_and_chronology_basic_bibliographic_unit(self, key, value):
    """Enumeration and Chronology-Basic Bibliographic Unit."""
    return {
    }


@marc21_holdings.over(
    'enumeration_and_chronology_supplementary_material',
    '^864..')
@utils.for_each_value
@utils.filter_values
def enumeration_and_chronology_supplementary_material(self, key, value):
    """Enumeration and Chronology-Supplementary Material."""
    return {
    }


@marc21_holdings.over('enumeration_and_chronology_indexes', '^865..')
@utils.for_each_value
@utils.filter_values
def enumeration_and_chronology_indexes(self, key, value):
    """Enumeration and Chronology-Indexes."""
    return {
    }


@marc21_holdings.over('textual_holdings_basic_bibliographic_unit', '^866..')
@utils.for_each_value
@utils.filter_values
def textual_holdings_basic_bibliographic_unit(self, key, value):
    """Textual Holdings-Basic Bibliographic Unit."""
    return {
    }


@marc21_holdings.over('textual_holdings_supplementary_material', '^867..')
@utils.for_each_value
@utils.filter_values
def textual_holdings_supplementary_material(self, key, value):
    """Textual Holdings-Supplementary Material."""
    return {
    }


@marc21_holdings.over('textual_holdings_indexes', '^868..')
@utils.for_each_value
@utils.filter_values
def textual_holdings_indexes(self, key, value):
    """Textual Holdings-Indexes."""
    return {
    }


@marc21_holdings.over('item_information_basic_bibliographic_unit', '^876..')
@utils.for_each_value
@utils.filter_values
def item_information_basic_bibliographic_unit(self, key, value):
    """Item Information-Basic Bibliographic Unit."""
    return {
    }


@marc21_holdings.over('item_information_supplementary_material', '^877..')
@utils.for_each_value
@utils.filter_values
def item_information_supplementary_material(self, key, value):
    """Item Information-Supplementary Material."""
    return {
    }


@marc21_holdings.over('item_information_indexes', '^878..')
@utils.for_each_value
@utils.filter_values
def item_information_indexes(self, key, value):
    """Item Information-Indexes."""
    return {
    }


@marc21_holdings.over('alternate_graphic_representation', '^880..')
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


@marc21_holdings.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    """Machine-generated Metadata Provenance."""
    indicator_map1 = {
        '#': 'No information provided/not applicable',
        '0': 'Fully machine-generated',
        '1': 'Partially machine-generated'}
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


@marc21_holdings.over('description_conversion_information', '^884..')
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
