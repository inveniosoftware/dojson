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

@marc21.over('physical_description', '^300..')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    return {
        'extent': value.get('a'),
        'dimensions': value.get('c'),
        'other_physical_details': value.get('b'),
        'accompanying_material': value.get('e'),
        'size_of_unit': value.get('g'),
        'type_of_unit': value.get('f'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('playing_time', '^306..')
@utils.filter_values
def playing_time(self, key, value):
    return {
        'playing_time': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('hours_', '^307[8.].')
@utils.for_each_value
@utils.filter_values
def hours_(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Hours'}
    return {
        'hours': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'additional_information': value.get('b'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('current_publication_frequency', '^310..')
@utils.filter_values
def current_publication_frequency(self, key, value):
    return {
        'current_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'date_of_current_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('former_publication_frequency', '^321..')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    return {
        'former_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'dates_of_former_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    return {
        'content_type_term': value.get('a'),
        'content_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    return {
        'media_type_term': value.get('a'),
        'media_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    return {
        'carrier_type_term': value.get('a'),
        'carrier_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('physical_medium', '^340..')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    return {
        'material_base_and_configuration': value.get('a'),
        'materials_applied_to_surface': value.get('c'),
        'dimensions': value.get('b'),
        'support': value.get('e'),
        'information_recording_technique': value.get('d'),
        'production_rate_ratio': value.get('f'),
        'technical_specifications_of_medium': value.get('i'),
        'location_within_medium': value.get('h'),
        'layout': value.get('k'),
        'generation': value.get('j'),
        'book_format': value.get('m'),
        'polarity': value.get('o'),
        'font_size': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('geospatial_reference_data', '^342[10][103254768]')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    indicator_map1 = {u'1': u'Vertical coordinate system', u'0': u'Horizontal coordinate system'}
    indicator_map2 = {u'1': u'Map projection', u'0': u'Geographic', u'3': u'Local planar', u'2': u'Grid coordinate system', u'5': u'Geodetic model', u'4': u'Local', u'7': u'Method specified in $2', u'6': u'Altitude', u'8': u'Depth'}
    return {
        'reference_method_used': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'name': value.get('a'),
        'latitude_resolution': value.get('c'),
        'coordinate_units_or_distance_units': value.get('b'),
        'standard_parallel_or_oblique_line_latitude': value.get('e'),
        'longitude_resolution': value.get('d'),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'oblique_line_longitude': value.get('f'),
        'false_easting': value.get('i'),
        'latitude_of_projection_center_or_projection_origin': value.get('h'),
        'scale_factor': value.get('k'),
        'false_northing': value.get('j'),
        'azimuthal_angle': value.get('m'),
        'height_of_perspective_point_above_surface': value.get('l'),
        'landsat_number_and_path_number': value.get('o'),
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': value.get('n'),
        'ellipsoid_name': value.get('q'),
        'zone_identifier': value.get('p'),
        'denominator_of_flattening_ratio': value.get('s'),
        'semi_major_axis': value.get('r'),
        'vertical_encoding_method': value.get('u'),
        'vertical_resolution': value.get('t'),
        'local_planar_or_local_georeference_information': value.get('w'),
        'local_planar_local_or_other_projection_or_grid_description': value.get('v'),
        'geospatial_reference_dimension': indicator_map1.get(key[3]),
        'geospatial_reference_method': indicator_map2.get(key[4]),
    }

@marc21.over('planar_coordinate_data', '^343..')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
    return {
        'planar_coordinate_encoding_method': value.get('a'),
        'abscissa_resolution': value.get('c'),
        'planar_distance_units': value.get('b'),
        'distance_resolution': value.get('e'),
        'ordinate_resolution': value.get('d'),
        'bearing_units': value.get('g'),
        'bearing_resolution': value.get('f'),
        'bearing_reference_meridian': value.get('i'),
        'bearing_reference_direction': value.get('h'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('sound_characteristics', '^344..')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    return {
        'type_of_recording': value.get('a'),
        'playing_speed': value.get('c'),
        'recording_medium': value.get('b'),
        'track_configuration': value.get('e'),
        'groove_characteristic': value.get('d'),
        'configuration_of_playback_channels': value.get('g'),
        'tape_configuration': value.get('f'),
        'special_playback_characteristics': value.get('h'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('projection_characteristics_of_moving_image', '^345..')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    return {
        'presentation_format': value.get('a'),
        'projection_speed': value.get('b'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('video_characteristics', '^346..')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    return {
        'video_format': value.get('a'),
        'broadcast_standard': value.get('b'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('digital_file_characteristics', '^347..')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    return {
        'file_type': value.get('a'),
        'file_size': value.get('c'),
        'encoding_format': value.get('b'),
        'regional_encoding': value.get('e'),
        'resolution': value.get('d'),
        'transmission_speed': value.get('f'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    return {
        'organization': value.get('a'),
        'hierarchical_level': value.get('c'),
        'arrangement': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('digital_graphic_representation', '^352..')
@utils.for_each_value
@utils.filter_values
def digital_graphic_representation(self, key, value):
    return {
        'direct_reference_method': value.get('a'),
        'object_count': value.get('c'),
        'object_type': value.get('b'),
        'column_count': value.get('e'),
        'row_count': value.get('d'),
        'vpf_topology_level': value.get('g'),
        'vertical_count': value.get('f'),
        'indirect_reference_description': value.get('i'),
        'format_of_the_digital_image': value.get('q'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('security_classification_control', '^355[1032548].')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    indicator_map1 = {u'1': u'Title', u'0': u'Document', u'3': u'Contents note', u'2': u'Abstract', u'5': u'Record', u'4': u'Author', u'8': u'None of the above'}
    return {
        'security_classification': value.get('a'),
        'external_dissemination_information': value.get('c'),
        'handling_instructions': value.get('b'),
        'classification_system': value.get('e'),
        'downgrading_or_declassification_event': value.get('d'),
        'downgrading_date': value.get('g'),
        'country_of_origin_code': value.get('f'),
        'declassification_date': value.get('h'),
        'authorization': value.get('j'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'controlled_element': indicator_map1.get(key[3]),
    }

@marc21.over('originator_dissemination_control', '^357..')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    return {
        'originator_control_term': value.get('a'),
        'authorized_recipients_of_material': value.get('c'),
        'originating_agency': value.get('b'),
        'other_restrictions': value.get('g'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('dates_of_publication_and_or_sequential_designation', '^362[10].')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    indicator_map1 = {u'1': u'Unformatted note', u'0': u'Formatted style'}
    return {
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'format_of_date': indicator_map1.get(key[3]),
    }

@marc21.over('normalized_date_and_sequential_designation', '^363[10.][10.]')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    indicator_map1 = {u'1': u'Ending information', u'0': u'Starting information', u'#': u'No information provided'}
    indicator_map2 = {u'1': u'Open', u'0': u'Closed', u'#': u'Not specified'}
    return {
        'first_level_of_enumeration': value.get('a'),
        'nonpublic_note': value.get('x'),
        'third_level_of_enumeration': value.get('c'),
        'second_level_of_enumeration': value.get('b'),
        'fifth_level_of_enumeration': value.get('e'),
        'fourth_level_of_enumeration': value.get('d'),
        'alternative_numbering_scheme_first_level_of_enumeration': value.get('g'),
        'sixth_level_of_enumeration': value.get('f'),
        'first_level_of_chronology': value.get('i'),
        'alternative_numbering_scheme_second_level_of_enumeration': value.get('h'),
        'third_level_of_chronology': value.get('k'),
        'second_level_of_chronology': value.get('j'),
        'alternative_numbering_scheme_chronology': value.get('m'),
        'fourth_level_of_chronology': value.get('l'),
        'first_level_textual_designation': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'public_note': value.get('z'),
        'first_level_of_chronology_issuance': value.get('v'),
        'start_end_designator': indicator_map1.get(key[3]),
        'state_of_issuance': indicator_map2.get(key[4]),
    }

@marc21.over('trade_price', '^365..')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
    return {
        'price_type_code': value.get('a'),
        'currency_code': value.get('c'),
        'price_amount': value.get('b'),
        'price_note': value.get('e'),
        'unit_of_pricing': value.get('d'),
        'price_effective_until': value.get('g'),
        'price_effective_from': value.get('f'),
        'tax_rate_2': value.get('i'),
        'tax_rate_1': value.get('h'),
        'marc_country_code': value.get('k'),
        'iso_country_code': value.get('j'),
        'identification_of_pricing_entity': value.get('m'),
        'source_of_price_type_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('trade_availability_information', '^366..')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
    return {
        'publishers_compressed_title_identification': value.get('a'),
        'availability_status_code': value.get('c'),
        'detailed_date_of_publication': value.get('b'),
        'note': value.get('e'),
        'expected_next_availability_date': value.get('d'),
        'date_made_out_of_print': value.get('g'),
        'publisher_s_discount_category': value.get('f'),
        'marc_country_code': value.get('k'),
        'iso_country_code': value.get('j'),
        'identification_of_agency': value.get('m'),
        'source_of_availability_status_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    return {
        'language_code': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'language_term': value.get('l'),
        'linkage': value.get('6'),
    }

@marc21.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    return {
        'form_of_work': value.get('a'),
        'record_control_number': value.get('0'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    return {
        'other_distinguishing_characteristic': value.get('a'),
        'source_of_information': value.get('v'),
        'record_control_number': value.get('0'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('medium_of_performance', '^382[10.][10.]')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    indicator_map1 = {u'1': u'Partial medium of performance', u'0': u'Medium of performance', u'#': u'No information provided'}
    indicator_map2 = {u'1': u'Intended for access', u'0': u'Not intended for access', u'#': u'No information provided'}
    return {
        'medium_of_performance': value.get('a'),
        'soloist': value.get('b'),
        'doubling_instrument': value.get('d'),
        'alternative_medium_of_performance': value.get('p'),
        'note': value.get('v'),
        'number_of_performers_of_the_same_medium': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'total_number_of_performers': value.get('s'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
        'access_control': indicator_map2.get(key[4]),
    }

@marc21.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    return {
        'serial_number': value.get('a'),
        'thematic_index_number': value.get('c'),
        'opus_number': value.get('b'),
        'publisher_associated_with_opus_number': value.get('e'),
        'thematic_index_code': value.get('d'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('key', '^384[10.].')
@utils.filter_values
def key(self, key, value):
    indicator_map1 = {u'1': u'Transposed key ', u'0': u'Original key ', u'#': u'Relationship to original unknown '}
    return {
        'key': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'key_type': indicator_map1.get(key[3]),
    }

@marc21.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    return {
        'audience_term': value.get('a'),
        'audience_code': value.get('b'),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    return {
        'creator_contributor_term': value.get('a'),
        'creator_contributor_code': value.get('b'),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }
