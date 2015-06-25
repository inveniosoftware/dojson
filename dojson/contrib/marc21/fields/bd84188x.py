# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from dojson import utils

from ..model import marc21


@marc21.over('holding_institution', '^850..')
@utils.for_each_value
@utils.filter_values
def holding_institution(self, key, value):
    return {
        'holding_institution': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('location', '^852[_103254768][10_2]')
@utils.for_each_value
@utils.filter_values
def location(self, key, value):
    indicator_map1 = {u'#': u'No information provided', u'1': u'Dewey Decimal classification', u'0': u'Library of Congress classification', u'3': u'Superintendent of Documents classification', u'2':
                      u'National Library of Medicine classification', u'5': u'Title', u'4': u'Shelving control number', u'7': u'Source specified in subfield $2', u'6': u'Shelved separately', u'8': u'Other scheme'}
    indicator_map2 = {u'1': u'Primary enumeration', u'0': u'Not enumeration',
                      u'#': u'No information provided', u'2': u'Alternative enumeration'}
    return {
        'materials_specified': value.get('3'),
        'source_of_classification_or_shelving_scheme': value.get('2'),
        'linkage': value.get('6'),
        'sequence_number': value.get('8'),
        'location': value.get('a'),
        'shelving_location': value.get('c'),
        'sublocation_or_collection': value.get('b'),
        'address': value.get('e'),
        'former_shelving_location': value.get('d'),
        'non_coded_location_qualifier': value.get('g'),
        'coded_location_qualifier': value.get('f'),
        'item_part': value.get('i'),
        'classification_part': value.get('h'),
        'call_number_prefix': value.get('k'),
        'shelving_control_number': value.get('j'),
        'call_number_suffix': value.get('m'),
        'shelving_form_of_title': value.get('l'),
        'country_code': value.get('n'),
        'piece_physical_condition': value.get('q'),
        'piece_designation': value.get('p'),
        'copyright_article_fee_code': value.get('s'),
        'uniform_resource_identifier': value.get('u'),
        'copy_number': value.get('t'),
        'nonpublic_note': value.get('x'),
        'public_note': value.get('z'),
        'shelving_scheme': indicator_map1.get(key[3]),
        'shelving_order': indicator_map2.get(key[4]),
    }


@marc21.over('electronic_location_and_access', '^856.[10_28]')
@utils.for_each_value
@utils.filter_values
def electronic_location_and_access(self, key, value):
    indicator_map1 = {u'1': u'FTP', u'0': u'Email', u'#': u'No information provided', u'2':
                      u'Remote login (Telnet)', u'3': u'Dial-up', u'4': 'HTTP', u'7': 'Method specified in subfield access_method'}
    indicator_map2 = {u'1': u'Version of resource', u'0': u'Resource', u'#':
                      u'No information provided', u'2': u'Related resource', u'8': u'No display constant generated'}
    return {
        'materials_specified': value.get('3'),
        'access_method': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'host_name': value.get('a'),
        'compression_information': value.get('c'),
        'access_number': value.get('b'),
        'path': value.get('d'),
        'electronic_name': value.get('f'),
        'instruction': value.get('i'),
        'processor_of_request': value.get('h'),
        'password': value.get('k'),
        'bits_per_second': value.get('j'),
        'contact_for_access_assistance': value.get('m'),
        'logon': value.get('l'),
        'operating_system': value.get('o'),
        'name_of_location_of_host': value.get('n'),
        'electronic_format_type': value.get('q'),
        'port': value.get('p'),
        'file_size': value.get('s'),
        'settings': value.get('r'),
        'uniform_resource_identifier': value.get('u'),
        'terminal_emulation': value.get('t'),
        'record_control_number': value.get('w'),
        'hours_access_method_available': value.get('v'),
        'link_text': value.get('y'),
        'nonpublic_note': value.get('x'),
        'public_note': value.get('z'),
        'method': indicator_map1.get(key[3]),
        'relationship': indicator_map2.get(key[4]),
    }


@marc21.over('replacement_record_information', '^882..')
@utils.filter_values
def replacement_record_information(self, key, value):
    return {
        'replacement_title': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'explanatory_text': value.get('i'),
        'replacement_bibliographic_record_control_number': value.get('w'),
        'linkage': value.get('6'),
    }


@marc21.over('machine_generated_metadata_provenance', '^883[10_].')
@utils.for_each_value
@utils.filter_values
def machine_generated_metadata_provenance(self, key, value):
    indicator_map1 = {u'1': u'Partially machine-generated', u'0':
                      u'Fully machine-generated', u'#': u'No information provided/not applicable'}
    return {
        'generation_process': value.get('a'),
        'confidence_value': value.get('c'),
        'generation_date': value.get('d'),
        'generation_agency': value.get('q'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'uniform_resource_identifier': value.get('u'),
        'bibliographic_record_control_number': value.get('w'),
        'validity_end_date': value.get('x'),
        'field_link_and_sequence_number': value.get('8'),
        'method_of_machine_assignment': indicator_map1.get(key[3]),
    }


@marc21.over('non_marc_information_field', '^887..')
@utils.for_each_value
@utils.filter_values
def non_marc_information_field(self, key, value):
    return {
        'content_of_non_marc_field': value.get('a'),
        'source_of_data': value.get('2'),
    }
