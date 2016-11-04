# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21


@marc21.over('physical_description', '^300..')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    """Physical Description."""
    field_map = {
        'c': 'dimensions',
        'a': 'extent',
        'b': 'other_physical_details',
        'e': 'accompanying_material',
        'f': 'type_of_unit',
        '3': 'materials_specified',
        'g': 'size_of_unit',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'dimensions': utils.force_list(
            value.get('c')
        ),
        'extent': utils.force_list(
            value.get('a')
        ),
        'other_physical_details': value.get('b'),
        'accompanying_material': value.get('e'),
        'type_of_unit': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'size_of_unit': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('playing_time', '^306..')
@utils.filter_values
def playing_time(self, key, value):
    """Playing Time."""
    field_map = {
        'a': 'playing_time',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'playing_time': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('hours', '^307[8_].')
@utils.for_each_value
@utils.filter_values
def hours(self, key, value):
    """Hours, Etc.."""
    indicator_map1 = {"8": "No display constant generated", "_": "Hours"}
    field_map = {
        'b': 'additional_information',
        'a': 'hours',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'additional_information': value.get('b'),
        'hours': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('current_publication_frequency', '^310..')
@utils.filter_values
def current_publication_frequency(self, key, value):
    """Current Publication Frequency."""
    field_map = {
        'b': 'date_of_current_publication_frequency',
        'a': 'current_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'date_of_current_publication_frequency': value.get('b'),
        'current_publication_frequency': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('former_publication_frequency', '^321..')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    """Former Publication Frequency."""
    field_map = {
        'b': 'dates_of_former_publication_frequency',
        'a': 'former_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'dates_of_former_publication_frequency': value.get('b'),
        'former_publication_frequency': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        '3': 'materials_specified',
        'b': 'content_type_code',
        'a': 'content_type_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    """Media Type."""
    field_map = {
        '3': 'materials_specified',
        'b': 'media_type_code',
        'a': 'media_type_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'media_type_code': utils.force_list(
            value.get('b')
        ),
        'media_type_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    """Carrier Type."""
    field_map = {
        '3': 'materials_specified',
        'b': 'carrier_type_code',
        'a': 'carrier_type_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'carrier_type_code': utils.force_list(
            value.get('b')
        ),
        'carrier_type_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('physical_medium', '^340..')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    """Physical Medium."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'k': 'layout',
        'o': 'polarity',
        'f': 'production_rate_ratio',
        'e': 'support',
        'd': 'information_recording_technique',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'n': 'font_size',
        'j': 'generation',
        'c': 'materials_applied_to_surface',
        '3': 'materials_specified',
        'b': 'dimensions',
        'i': 'technical_specifications_of_medium',
        'a': 'material_base_and_configuration',
        'm': 'book_format',
        '6': 'linkage',
        'h': 'location_within_medium',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'layout': utils.force_list(
            value.get('k')
        ),
        'polarity': utils.force_list(
            value.get('o')
        ),
        'production_rate_ratio': utils.force_list(
            value.get('f')
        ),
        'support': utils.force_list(
            value.get('e')
        ),
        'information_recording_technique': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'font_size': utils.force_list(
            value.get('n')
        ),
        'generation': utils.force_list(
            value.get('j')
        ),
        'materials_applied_to_surface': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'dimensions': utils.force_list(
            value.get('b')
        ),
        'technical_specifications_of_medium': utils.force_list(
            value.get('i')
        ),
        'material_base_and_configuration': utils.force_list(
            value.get('a')
        ),
        'book_format': utils.force_list(
            value.get('m')
        ),
        'linkage': value.get('6'),
        'location_within_medium': utils.force_list(
            value.get('h')
        ),
    }


@marc21.over('geospatial_reference_data', '^342[10_][1_02853467]')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    """Geospatial Reference Data."""
    indicator_map1 = {
        "0": "Horizontal coordinate system",
        "1": "Vertical coordinate system"}
    indicator_map2 = {
        "0": "Geographic",
        "1": "Map projection",
        "2": "Grid coordinate system",
        "3": "Local planar",
        "4": "Local",
        "5": "Geodetic model",
        "6": "Altitude",
        "7": "Method specified in $2",
        "8": "Depth"}
    field_map = {
        'u': 'vertical_encoding_method',
        'f': 'oblique_line_longitude',
        'e': 'standard_parallel_or_oblique_line_latitude',
        't': 'vertical_resolution',
        'd': 'longitude_resolution',
        '2': 'reference_method_used',
        'g': 'longitude_of_central_meridian_or_projection_center',
        'r': 'semi_major_axis',
        'c': 'latitude_resolution',
        'q': 'ellipsoid_name',
        'b': 'coordinate_units_or_distance_units',
        'p': 'zone_identifier',
        'j': 'false_northing',
        '6': 'linkage',
        'm': 'azimuthal_angle',
        's': 'denominator_of_flattening_ratio',
        'w': 'local_planar_or_local_georeference_information',
        '8': 'field_link_and_sequence_number',
        'n': 'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole',
        'v': 'local_planar_local_or_other_projection_or_grid_description',
        'k': 'scale_factor',
        'l': 'height_of_perspective_point_above_surface',
        'o': 'landsat_number_and_path_number',
        'a': 'name',
        'h': 'latitude_of_projection_center_or_projection_origin',
        'i': 'false_easting',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('geospatial_reference_dimension')

    if key[4] in indicator_map2:
        order.append('geospatial_reference_method')

    return {
        '__order__': tuple(order) if len(order) else None,
        'vertical_encoding_method': value.get('u'),
        'oblique_line_longitude': utils.force_list(
            value.get('f')
        ),
        'standard_parallel_or_oblique_line_latitude': utils.force_list(
            value.get('e')
        ),
        'vertical_resolution': value.get('t'),
        'longitude_resolution': value.get('d'),
        'reference_method_used': value.get('2'),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'semi_major_axis': value.get('r'),
        'latitude_resolution': value.get('c'),
        'ellipsoid_name': value.get('q'),
        'coordinate_units_or_distance_units': value.get('b'),
        'zone_identifier': value.get('p'),
        'false_northing': value.get('j'),
        'linkage': value.get('6'),
        'azimuthal_angle': value.get('m'),
        'denominator_of_flattening_ratio': value.get('s'),
        'local_planar_or_local_georeference_information': value.get('w'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': value.get('n'),
        'local_planar_local_or_other_projection_or_grid_description': value.get('v'),
        'scale_factor': value.get('k'),
        'height_of_perspective_point_above_surface': value.get('l'),
        'landsat_number_and_path_number': value.get('o'),
        'name': value.get('a'),
        'latitude_of_projection_center_or_projection_origin': value.get('h'),
        'false_easting': value.get('i'),
        'geospatial_reference_dimension': indicator_map1.get(key[3]),
        'geospatial_reference_method': indicator_map2.get(key[4]),
    }


@marc21.over('planar_coordinate_data', '^343..')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
    """Planar Coordinate Data."""
    field_map = {
        'h': 'bearing_reference_direction',
        'i': 'bearing_reference_meridian',
        'c': 'abscissa_resolution',
        'a': 'planar_coordinate_encoding_method',
        'b': 'planar_distance_units',
        'f': 'bearing_resolution',
        'e': 'distance_resolution',
        'd': 'ordinate_resolution',
        '6': 'linkage',
        'g': 'bearing_units',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'bearing_reference_direction': value.get('h'),
        'bearing_reference_meridian': value.get('i'),
        'abscissa_resolution': value.get('c'),
        'planar_coordinate_encoding_method': value.get('a'),
        'planar_distance_units': value.get('b'),
        'bearing_resolution': value.get('f'),
        'distance_resolution': value.get('e'),
        'ordinate_resolution': value.get('d'),
        'linkage': value.get('6'),
        'bearing_units': value.get('g'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('sound_characteristics', '^344..')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    """Sound Characteristics."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'f': 'tape_configuration',
        'e': 'track_configuration',
        'd': 'groove_characteristic',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'g': 'configuration_of_playback_channels',
        'c': 'playing_speed',
        '3': 'materials_specified',
        'b': 'recording_medium',
        'a': 'type_of_recording',
        '6': 'linkage',
        'h': 'special_playback_characteristics',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'tape_configuration': utils.force_list(
            value.get('f')
        ),
        'track_configuration': utils.force_list(
            value.get('e')
        ),
        'groove_characteristic': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'configuration_of_playback_channels': utils.force_list(
            value.get('g')
        ),
        'playing_speed': utils.force_list(
            value.get('c')
        ),
        'materials_specified': value.get('3'),
        'recording_medium': utils.force_list(
            value.get('b')
        ),
        'type_of_recording': utils.force_list(
            value.get('a')
        ),
        'linkage': value.get('6'),
        'special_playback_characteristics': utils.force_list(
            value.get('h')
        ),
    }


@marc21.over('projection_characteristics_of_moving_image', '^345..')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    """Projection Characteristics of Moving Image."""
    field_map = {
        '3': 'materials_specified',
        'b': 'projection_speed',
        'a': 'presentation_format',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'projection_speed': utils.force_list(
            value.get('b')
        ),
        'presentation_format': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('video_characteristics', '^346..')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    """Video Characteristics."""
    field_map = {
        '3': 'materials_specified',
        'b': 'broadcast_standard',
        'a': 'video_format',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'broadcast_standard': utils.force_list(
            value.get('b')
        ),
        'video_format': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('digital_file_characteristics', '^347..')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    """Digital File Characteristics."""
    field_map = {
        'c': 'file_size',
        'd': 'resolution',
        '3': 'materials_specified',
        'b': 'encoding_format',
        'e': 'regional_encoding',
        'f': 'encoded_bitrate',
        'a': 'file_type',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'file_size': utils.force_list(
            value.get('c')
        ),
        'resolution': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'encoding_format': utils.force_list(
            value.get('b')
        ),
        'regional_encoding': utils.force_list(
            value.get('e')
        ),
        'encoded_bitrate': utils.force_list(
            value.get('f')
        ),
        'file_type': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        '3': 'materials_specified',
        'b': 'format_of_notated_music_code',
        'a': 'format_of_notated_music_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    """Organization and Arrangement of Materials."""
    field_map = {
        'c': 'hierarchical_level',
        'a': 'organization',
        'b': 'arrangement',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'hierarchical_level': value.get('c'),
        'organization': utils.force_list(
            value.get('a')
        ),
        'arrangement': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('digital_graphic_representation', '^352..')
@utils.for_each_value
@utils.filter_values
def digital_graphic_representation(self, key, value):
    """Digital Graphic Representation."""
    field_map = {
        'i': 'indirect_reference_description',
        'c': 'object_count',
        'a': 'direct_reference_method',
        'b': 'object_type',
        'q': 'format_of_the_digital_image',
        'f': 'vertical_count',
        'e': 'column_count',
        'd': 'row_count',
        '6': 'linkage',
        'g': 'vpf_topology_level',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'indirect_reference_description': value.get('i'),
        'object_count': utils.force_list(
            value.get('c')
        ),
        'direct_reference_method': value.get('a'),
        'object_type': utils.force_list(
            value.get('b')
        ),
        'format_of_the_digital_image': value.get('q'),
        'vertical_count': value.get('f'),
        'column_count': value.get('e'),
        'row_count': value.get('d'),
        'linkage': value.get('6'),
        'vpf_topology_level': value.get('g'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('security_classification_control', '^355[513_4028].')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    """Security Classification Control."""
    indicator_map1 = {
        "0": "Document",
        "1": "Title",
        "2": "Abstract",
        "3": "Contents note",
        "4": "Author",
        "5": "Record",
        "8": "None of the above"}
    field_map = {
        'h': 'declassification_date',
        'j': 'authorization',
        'c': 'external_dissemination_information',
        'a': 'security_classification',
        'b': 'handling_instructions',
        'f': 'country_of_origin_code',
        'e': 'classification_system',
        'd': 'downgrading_or_declassification_event',
        '6': 'linkage',
        'g': 'downgrading_date',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('controlled_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'declassification_date': value.get('h'),
        'authorization': utils.force_list(
            value.get('j')
        ),
        'external_dissemination_information': utils.force_list(
            value.get('c')
        ),
        'security_classification': value.get('a'),
        'handling_instructions': utils.force_list(
            value.get('b')
        ),
        'country_of_origin_code': value.get('f'),
        'classification_system': value.get('e'),
        'downgrading_or_declassification_event': value.get('d'),
        'linkage': value.get('6'),
        'downgrading_date': value.get('g'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'controlled_element': indicator_map1.get(key[3]),
    }


@marc21.over('originator_dissemination_control', '^357..')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    """Originator Dissemination Control."""
    field_map = {
        'c': 'authorized_recipients_of_material',
        'a': 'originator_control_term',
        'b': 'originating_agency',
        'g': 'other_restrictions',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'authorized_recipients_of_material': utils.force_list(
            value.get('c')
        ),
        'originator_control_term': value.get('a'),
        'originating_agency': utils.force_list(
            value.get('b')
        ),
        'other_restrictions': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over(
    'dates_of_publication_and_or_sequential_designation', '^362[10_].')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    """Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted note"}
    field_map = {
        'z': 'source_of_information',
        'a': 'dates_of_publication_and_or_sequential_designation',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('format_of_date')

    return {
        '__order__': tuple(order) if len(order) else None,
        'source_of_information': value.get('z'),
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'format_of_date': indicator_map1.get(key[3]),
    }


@marc21.over('normalized_date_and_sequential_designation', '^363[10_][10_]')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    """Normalized Date and Sequential Designation."""
    indicator_map1 = {
        "0": "Starting information",
        "1": "Ending information",
        "_": "No information provided"}
    indicator_map2 = {"0": "Closed", "1": "Open", "_": "Not specified"}
    field_map = {
        'u': 'first_level_textual_designation',
        'v': 'first_level_of_chronology_issuance',
        'x': 'nonpublic_note',
        'f': 'sixth_level_of_enumeration',
        'e': 'fifth_level_of_enumeration',
        'd': 'fourth_level_of_enumeration',
        '8': 'field_link_and_sequence_number',
        'g': 'alternative_numbering_scheme_first_level_of_enumeration',
        'j': 'second_level_of_chronology',
        'c': 'third_level_of_enumeration',
        'a': 'first_level_of_enumeration',
        'b': 'second_level_of_enumeration',
        'l': 'fourth_level_of_chronology',
        'i': 'first_level_of_chronology',
        'k': 'third_level_of_chronology',
        'z': 'public_note',
        'm': 'alternative_numbering_scheme_chronology',
        '6': 'linkage',
        'h': 'alternative_numbering_scheme_second_level_of_enumeration',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('start_end_designator')

    if key[4] in indicator_map2:
        order.append('state_of_issuance')

    return {
        '__order__': tuple(order) if len(order) else None,
        'first_level_textual_designation': value.get('u'),
        'first_level_of_chronology_issuance': value.get('v'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'sixth_level_of_enumeration': value.get('f'),
        'fifth_level_of_enumeration': value.get('e'),
        'fourth_level_of_enumeration': value.get('d'),
        'field_link_and_sequence_number': value.get('8'),
        'alternative_numbering_scheme_first_level_of_enumeration': value.get('g'),
        'second_level_of_chronology': value.get('j'),
        'third_level_of_enumeration': value.get('c'),
        'first_level_of_enumeration': value.get('a'),
        'second_level_of_enumeration': value.get('b'),
        'fourth_level_of_chronology': value.get('l'),
        'first_level_of_chronology': value.get('i'),
        'third_level_of_chronology': value.get('k'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'alternative_numbering_scheme_chronology': value.get('m'),
        'linkage': value.get('6'),
        'alternative_numbering_scheme_second_level_of_enumeration': value.get('h'),
        'start_end_designator': indicator_map1.get(key[3]),
        'state_of_issuance': indicator_map2.get(key[4]),
    }


@marc21.over('trade_price', '^365..')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
    """Trade Price."""
    field_map = {
        'f': 'price_effective_from',
        'e': 'price_note',
        'd': 'unit_of_pricing',
        '2': 'source_of_price_type_code',
        '8': 'field_link_and_sequence_number',
        'g': 'price_effective_until',
        'j': 'iso_country_code',
        'c': 'currency_code',
        'a': 'price_type_code',
        'b': 'price_amount',
        'i': 'tax_rate_2',
        'k': 'marc_country_code',
        'm': 'identification_of_pricing_entity',
        '6': 'linkage',
        'h': 'tax_rate_1',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'price_effective_from': value.get('f'),
        'price_note': value.get('e'),
        'unit_of_pricing': value.get('d'),
        'source_of_price_type_code': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'price_effective_until': value.get('g'),
        'iso_country_code': value.get('j'),
        'currency_code': value.get('c'),
        'price_type_code': value.get('a'),
        'price_amount': value.get('b'),
        'tax_rate_2': value.get('i'),
        'marc_country_code': value.get('k'),
        'identification_of_pricing_entity': value.get('m'),
        'linkage': value.get('6'),
        'tax_rate_1': value.get('h'),
    }


@marc21.over('trade_availability_information', '^366..')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
    """Trade Availability Information."""
    field_map = {
        'f': 'publisher_s_discount_category',
        'e': 'note',
        'd': 'expected_next_availability_date',
        '2': 'source_of_availability_status_code',
        '8': 'field_link_and_sequence_number',
        'g': 'date_made_out_of_print',
        'c': 'availability_status_code',
        'a': 'publishers_compressed_title_identification',
        'b': 'detailed_date_of_publication',
        'j': 'iso_country_code',
        'm': 'identification_of_agency',
        '6': 'linkage',
        'k': 'marc_country_code',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'publisher_s_discount_category': value.get('f'),
        'note': value.get('e'),
        'expected_next_availability_date': value.get('d'),
        'source_of_availability_status_code': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_made_out_of_print': value.get('g'),
        'availability_status_code': value.get('c'),
        'publishers_compressed_title_identification': value.get('a'),
        'detailed_date_of_publication': value.get('b'),
        'iso_country_code': value.get('j'),
        'identification_of_agency': value.get('m'),
        'linkage': value.get('6'),
        'marc_country_code': value.get('k'),
    }


@marc21.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'c': 'associated_country',
        'u': 'uniform_resource_identifier',
        's': 'start_period',
        'f': 'other_associated_place',
        'v': 'source_of_information',
        't': 'end_period',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        'g': 'place_of_origin_of_work',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'start_period': value.get('s'),
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'end_period': value.get('t'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('associated_language', '^377.[_7]')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {
        "7": "Source specified in subfield $2",
        "_": "MARC language code"}
    field_map = {
        'a': 'language_code',
        '2': 'source',
        '6': 'linkage',
        'l': 'language_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_code')

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code': utils.force_list(
            value.get('a')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2') if key[4] == '7' else indicator_map2.get(key[4]),
    }


@marc21.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        'a': 'form_of_work',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over(
    'other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(
        self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'a': 'other_distinguishing_characteristic',
        'v': 'source_of_information',
        'u': 'uniform_resource_identifier',
        '0': 'record_control_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('medium_of_performance', '^382[10_][10_]')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {
        "0": "Medium of performance",
        "1": "Partial medium of performance",
        "_": "No information provided"}
    indicator_map2 = {
        "0": "Not intended for access",
        "1": "Intended for access",
        "_": "No information provided"}
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        'v': 'note',
        's': 'total_number_of_performers',
        'e': 'number_of_ensembles_of_the_same_type',
        'd': 'doubling_instrument',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_performers_of_the_same_medium',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        't': 'total_number_of_ensembles',
        'a': 'medium_of_performance',
        'b': 'soloist',
        'p': 'alternative_medium_of_performance',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    if key[4] in indicator_map2:
        order.append('access_control')

    return {
        '__order__': tuple(order) if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'total_number_of_performers': value.get('s'),
        'number_of_ensembles_of_the_same_type': utils.force_list(
            value.get('e')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': value.get('r'),
        'total_number_of_ensembles': value.get('t'),
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
        'access_control': indicator_map2.get(key[4]),
    }


@marc21.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'c': 'thematic_index_number',
        'a': 'serial_number',
        'b': 'opus_number',
        'e': 'publisher_associated_with_opus_number',
        'd': 'thematic_index_code',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'publisher_associated_with_opus_number': value.get('e'),
        'thematic_index_code': value.get('d'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('key', '^384[10_].')
@utils.filter_values
def key(self, key, value):
    """Key."""
    indicator_map1 = {
        "0": "Original key",
        "1": "Transposed key",
        "_": "Relationship to original unknown"}
    field_map = {
        'a': 'key',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('key_type')

    return {
        '__order__': tuple(order) if len(order) else None,
        'key': value.get('a'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key_type': indicator_map1.get(key[3]),
    }


@marc21.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'n': 'demographic_group_code',
        '3': 'materials_specified',
        'b': 'audience_code',
        'a': 'audience_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        'm': 'demographic_group_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'demographic_group_code': value.get('n'),
        'materials_specified': value.get('3'),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'demographic_group_term': value.get('m'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'n': 'demographic_group_code',
        '3': 'materials_specified',
        'b': 'creator_contributor_code',
        'a': 'creator_contributor_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '6': 'linkage',
        'm': 'demographic_group_term',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'demographic_group_code': value.get('n'),
        'materials_specified': value.get('3'),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'demographic_group_term': value.get('m'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('time_period_of_creation', '^388[12_].')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {
        "1": "Creation of work",
        "2": "Creation of aggregate work",
        "_": "No information provided"}
    field_map = {
        '3': 'materials_specified',
        'a': 'time_period_of_creation_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period')

    return {
        '__order__': tuple(order) if len(order) else None,
        'materials_specified': value.get('3'),
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_time_period': indicator_map1.get(key[3]),
    }
