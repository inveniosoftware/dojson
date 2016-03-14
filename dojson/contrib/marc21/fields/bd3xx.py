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


@marc21.over('physical_description', '^300__')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    """Physical Description."""
    field_map = {
        'a': 'extent',
        'b': 'other_physical_details',
        'c': 'dimensions',
        'e': 'accompanying_material',
        'f': 'type_of_unit',
        'g': 'size_of_unit',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'extent': utils.force_list(
            value.get('a')
        ),
        'other_physical_details': value.get('b'),
        'dimensions': utils.force_list(
            value.get('c')
        ),
        'accompanying_material': value.get('e'),
        'type_of_unit': utils.force_list(
            value.get('f')
        ),
        'size_of_unit': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('playing_time', '^306__')
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


@marc21.over('hours', '^307[8_]_')
@utils.for_each_value
@utils.filter_values
def hours(self, key, value):
    """Hours, Etc.."""
    indicator_map1 = {
        '_': 'Hours',
        '8': 'No display constant generated',
    }

    field_map = {
        'a': 'hours',
        'b': 'additional_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')

    return {
        '__order__': tuple(order) if len(order) else None,
        'hours': value.get('a'),
        'additional_information': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@marc21.over('current_publication_frequency', '^310__')
@utils.filter_values
def current_publication_frequency(self, key, value):
    """Current Publication Frequency."""
    field_map = {
        'a': 'current_publication_frequency',
        'b': 'date_of_current_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'current_publication_frequency': value.get('a'),
        'date_of_current_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('former_publication_frequency', '^321__')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    """Former Publication Frequency."""
    field_map = {
        'a': 'former_publication_frequency',
        'b': 'dates_of_former_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'former_publication_frequency': value.get('a'),
        'dates_of_former_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('content_type', '^336__')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        'a': 'content_type_term',
        'b': 'content_type_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'content_type_term': utils.force_list(
            value.get('a')),
        'content_type_code': utils.force_list(
            value.get('b')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21.over('media_type', '^337__')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    """Media Type."""
    field_map = {
        'a': 'media_type_term',
        'b': 'media_type_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'media_type_term': utils.force_list(
            value.get('a')
        ),
        'media_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('carrier_type', '^338__')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    """Carrier Type."""
    field_map = {
        'a': 'carrier_type_term',
        'b': 'carrier_type_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'carrier_type_term': utils.force_list(
            value.get('a')
        ),
        'carrier_type_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('physical_medium', '^340__')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    """Physical Medium."""
    field_map = {
        'a': 'material_base_and_configuration',
        'b': 'dimensions',
        'c': 'materials_applied_to_surface',
        'd': 'information_recording_technique',
        'e': 'support',
        'f': 'production_rate_ratio',
        'h': 'location_within_medium',
        'i': 'technical_specifications_of_medium',
        'j': 'generation',
        'k': 'layout',
        'm': 'book_format',
        'n': 'font_size',
        'o': 'polarity',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'material_base_and_configuration': utils.force_list(
            value.get('a')
        ),
        'dimensions': utils.force_list(
            value.get('b'),
        ),
        'materials_applied_to_surface': utils.force_list(
            value.get('c')
        ),
        'information_recording_technique': utils.force_list(
            value.get('d')
        ),
        'support': utils.force_list(
            value.get('e')
        ),
        'production_rate_ratio': utils.force_list(
            value.get('f')
        ),
        'location_within_medium': utils.force_list(
            value.get('h')
        ),
        'technical_specifications_of_medium': utils.force_list(
            value.get('i')
        ),
        'generation': utils.force_list(
            value.get('j')
        ),
        'layout': utils.force_list(
            value.get('k')
        ),
        'book_format': utils.force_list(
            value.get('m')
        ),
        'font_size': utils.force_list(
            value.get('n')
        ),
        'polarity': utils.force_list(
            value.get('o')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('geospatial_reference_data', '^342[_01][_012345678]')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    """Geospatial Reference Data."""
    indicator_map1 = {
        '0': 'Horizontal coordinate system',
        '1': 'Vertical coordinate system',
    }

    indicator_map2 = {
        '0': 'Geographic',
        '1': 'Map projection',
        '2': 'Grid coordinate system',
        '3': 'Local planar',
        '4': 'Local',
        '5': 'Geodetic model',
        '6': 'Altitude',
        '7': 'Method specified in $2',
        '8': 'Depth',
    }

    field_map = {
        'a': 'name',
        'b': 'coordinate_units_or_distance_units',
        'c': 'latitude_resolution',
        'd': 'longitude_resolution',
        'e': 'standard_parallel_or_oblique_line_latitude',
        'f': 'oblique_line_longitude',
        'g': 'longitude_of_central_meridian_or_projection_center',
        'h': 'latitude_of_projection_center_or_projection_origin',
        'i': 'false_easting',
        'j': 'false_northing',
        'k': 'scale_factor',
        'l': 'height_of_perspective_point_above_surface',
        'm': 'azimuthal_angle',
        'n': 'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole',
        'o': 'landsat_number_and_path_number',
        'p': 'zone_identifier',
        'q': 'ellipsoid_name',
        'r': 'semi_major_axis',
        's': 'denominator_of_flattening_ratio',
        't': 'vertical_resolution',
        'u': 'vertical_encoding_method',
        'v': 'local_planar_local_or_other_projection_or_grid_description',
        'w': 'local_planar_or_local_georeference_information',
        '2': 'reference_method_used',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('geospatial_reference_dimension')
    if key[4] in indicator_map2:
        order.append('geospatial_reference_method')

    return {
        '__order__': tuple(order) if len(order) else None,
        'name': value.get('a'),
        'coordinate_units_or_distance_units': value.get('b'),
        'latitude_resolution': value.get('c'),
        'longitude_resolution': value.get('d'),
        'standard_parallel_or_oblique_line_latitude': utils.force_list(
            value.get('e')
        ),
        'oblique_line_longitude': utils.force_list(
            value.get('f')
        ),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'latitude_of_projection_center_or_projection_origin': value.get('h'),
        'false_easting': value.get('i'),
        'false_northing': value.get('j'),
        'scale_factor': value.get('k'),
        'height_of_perspective_point_above_surface': value.get('l'),
        'azimuthal_angle': value.get('m'),
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': value.get('n'),
        'landsat_number_and_path_number': value.get('o'),
        'zone_identifier': value.get('p'),
        'ellipsoid_name': value.get('q'),
        'semi_major_axis': value.get('r'),
        'denominator_of_flattening_ratio': value.get('s'),
        'vertical_resolution': value.get('t'),
        'vertical_encoding_method': value.get('u'),
        'local_planar_local_or_other_projection_or_grid_description': value.get('v'),
        'local_planar_or_local_georeference_information': value.get('w'),
        'reference_method_used': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'geospatial_reference_dimension': indicator_map1.get(key[3]),
        'geospatial_reference_method': indicator_map2.get(key[4]),
    }


@marc21.over('planar_coordinate_data', '^343__')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
    """Planar Coordinate Data."""
    field_map = {
        'a': 'planar_coordinate_encoding_method',
        'b': 'planar_distance_units',
        'c': 'abscissa_resolution',
        'd': 'ordinate_resolution',
        'e': 'distance_resolution',
        'f': 'bearing_resolution',
        'g': 'bearing_units',
        'h': 'bearing_reference_direction',
        'i': 'bearing_reference_meridian',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'planar_coordinate_encoding_method': value.get('a'),
        'planar_distance_units': value.get('b'),
        'abscissa_resolution': value.get('c'),
        'ordinate_resolution': value.get('d'),
        'distance_resolution': value.get('e'),
        'bearing_resolution': value.get('f'),
        'bearing_units': value.get('g'),
        'bearing_reference_direction': value.get('h'),
        'bearing_reference_meridian': value.get('i'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('sound_characteristics', '^344__')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    """Sound Characteristics."""
    field_map = {
        'a': 'type_of_recording',
        'b': 'recording_medium',
        'c': 'playing_speed',
        'd': 'groove_characteristic',
        'e': 'track_configuration',
        'f': 'tape_configuration',
        'g': 'configuration_of_playback_channels',
        'h': 'special_playback_characteristics',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'type_of_recording': utils.force_list(
            value.get('a')
        ),
        'recording_medium': utils.force_list(
            value.get('b')
        ),
        'playing_speed': utils.force_list(
            value.get('c')
        ),
        'groove_characteristic': utils.force_list(
            value.get('d')
        ),
        'track_configuration': utils.force_list(
            value.get('e')
        ),
        'tape_configuration': utils.force_list(
            value.get('f')
        ),
        'configuration_of_playback_channels': utils.force_list(
            value.get('g')
        ),
        'special_playback_characteristics': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('projection_characteristics_of_moving_image', '^345__')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    """Projection Characteristics of Moving Image."""
    field_map = {
        'a': 'presentation_format',
        'b': 'projection_speed',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'presentation_format': utils.force_list(
            value.get('a')
        ),
        'projection_speed': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('video_characteristics', '^346__')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    """Video Characteristics."""
    field_map = {
        'a': 'video_format',
        'b': 'broadcast_standard',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'video_format': utils.force_list(
            value.get('a')
        ),
        'broadcast_standard': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('digital_file_characteristics', '^347__')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    """Digital File Characteristics."""
    field_map = {
        'a': 'file_type',
        'b': 'encoding_format',
        'c': 'file_size',
        'd': 'resolution',
        'e': 'regional_encoding',
        'f': 'encoded_bitrate',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'file_type': utils.force_list(
            value.get('a')
        ),
        'encoding_format': utils.force_list(
            value.get('b')
        ),
        'file_size': utils.force_list(
            value.get('c')
        ),
        'resolution': utils.force_list(
            value.get('d')
        ),
        'regional_encoding': utils.force_list(
            value.get('e')
        ),
        'encoded_bitrate': utils.force_list(value.get('f')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('format_of_notated_music', '^348__')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        'a': 'format_of_notated_music_term',
        'b': 'format_of_notated_music_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'format_of_notated_music_term': utils.force_list(
            value.get('a')),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    """Organization and Arrangement of Materials."""
    field_map = {
        'a': 'organization',
        'b': 'arrangement',
        'c': 'hierarchical_level',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'organization': utils.force_list(
            value.get('a')
        ),
        'arrangement': utils.force_list(
            value.get('b')
        ),
        'hierarchical_level': value.get('c'),
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
        'a': 'direct_reference_method',
        'b': 'object_type',
        'c': 'object_count',
        'd': 'row_count',
        'e': 'column_count',
        'f': 'vertical_count',
        'g': 'vpf_topology_level',
        'i': 'indirect_reference_description',
        'q': 'format_of_the_digital_image',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'direct_reference_method': value.get('a'),
        'object_type': utils.force_list(
            value.get('b')
        ),
        'object_count': utils.force_list(
            value.get('c')
        ),
        'row_count': value.get('d'),
        'column_count': value.get('e'),
        'vertical_count': value.get('f'),
        'vpf_topology_level': value.get('g'),
        'indirect_reference_description': value.get('i'),
        'format_of_the_digital_image': value.get('q'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('security_classification_control', '^355[_0123458]_')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    """Security Classification Control."""
    indicator_map1 = {
        '0': 'Document',
        '1': 'Title',
        '2': 'Abstract',
        '3': 'Contents note',
        '4': 'Author',
        '5': 'Record',
        '8': 'None of the above',
    }

    field_map = {
        'a': 'security_classification',
        'b': 'handling_instructions',
        'c': 'external_dissemination_information',
        'd': 'downgrading_or_declassification_event',
        'e': 'classification_system',
        'f': 'country_of_origin_code',
        'g': 'downgrading_date',
        'h': 'declassification_date',
        'j': 'authorization',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('controlled_element')

    return {
        '__order__': tuple(order) if len(order) else None,
        'security_classification': value.get('a'),
        'handling_instructions': utils.force_list(
            value.get('b')
        ),
        'external_dissemination_information': utils.force_list(
            value.get('c')
        ),
        'downgrading_or_declassification_event': value.get('d'),
        'classification_system': value.get('e'),
        'country_of_origin_code': value.get('f'),
        'downgrading_date': value.get('g'),
        'declassification_date': value.get('h'),
        'authorization': utils.force_list(
            value.get('j')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'controlled_element': indicator_map1.get(key[3]),
    }


@marc21.over('originator_dissemination_control', '^357__')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    """Originator Dissemination Control."""
    field_map = {
        'a': 'originator_control_term',
        'b': 'originating_agency',
        'c': 'authorized_recipients_of_material',
        'g': 'other_restrictions',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'originator_control_term': value.get('a'),
        'originating_agency': utils.force_list(
            value.get('b')
        ),
        'authorized_recipients_of_material': utils.force_list(
            value.get('c')
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
    'dates_of_publication_and_or_sequential_designation', '^362[_01]_')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    """Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {
        '0': 'Formatted style',
        '1': 'Unformatted note',
    }

    field_map = {
        'a': 'dates_of_publication_and_or_sequential_designation',
        'z': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('format_of_date')

    return {
        '__order__': tuple(order) if len(order) else None,
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'format_of_date': indicator_map1.get(key[3]),
    }


@marc21.over('normalized_date_and_sequential_designation', '^363[_01][_01]')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    """Normalized Date and Sequential Designation."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Starting information',
        '1': 'Ending information',
    }
    indicator_map2 = {
        '_': 'Not specified',
        '0': 'Closed',
        '1': 'Open',
    }

    field_map = {
        'a': 'first_level_of_enumeration',
        'b': 'second_level_of_enumeration',
        'c': 'third_level_of_enumeration',
        'd': 'fourth_level_of_enumeration',
        'e': 'fifth_level_of_enumeration',
        'f': 'sixth_level_of_enumeration',
        'g': 'alternative_numbering_scheme_first_level_of',
        'h': 'alternative_numbering_scheme_second_level_of',
        'i': 'first_level_of_chronology',
        'j': 'second_level_of_chronology',
        'k': 'third_level_of_chronology',
        'l': 'fourth_level_of_chronology',
        'm': 'alternative_numbering_scheme_chronology',
        'u': 'first_level_textual_designation',
        'v': 'first_level_of_chronology_issuance',
        'x': 'nonpublic_note',
        'z': 'public_note',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('start_end_designator')
    if key[4] in indicator_map2:
        order.append('state_of_issuance')

    return {
        '__order__': tuple(order) if len(order) else None,
        'first_level_of_enumeration': value.get('a'),
        'second_level_of_enumeration': value.get('b'),
        'third_level_of_enumeration': value.get('c'),
        'fourth_level_of_enumeration': value.get('d'),
        'fifth_level_of_enumeration': value.get('e'),
        'sixth_level_of_enumeration': value.get('f'),
        'alternative_numbering_scheme_first_level_of_enumeration': value.get('g'),
        'alternative_numbering_scheme_second_level_of_enumeration': value.get('h'),
        'first_level_of_chronology': value.get('i'),
        'second_level_of_chronology': value.get('j'),
        'third_level_of_chronology': value.get('k'),
        'fourth_level_of_chronology': value.get('l'),
        'alternative_numbering_scheme_chronology': value.get('m'),
        'first_level_textual_designation': value.get('u'),
        'first_level_of_chronology_issuance': value.get('v'),
        'nonpublic_note': utils.force_list(
            value.get('x')),
        'public_note': utils.force_list(
            value.get('z')),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'start_end_designator': indicator_map1.get(
            key[3]),
        'state_of_issuance': indicator_map2.get(
            key[4]),
    }


@marc21.over('trade_price', '^365__')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
    """Trade Price."""
    field_map = {
        'a': 'price_type_code',
        'b': 'price_amount',
        'c': 'currency_code',
        'd': 'unit_of_pricing',
        'e': 'price_note',
        'f': 'price_effective_from',
        'g': 'price_effective_until',
        'h': 'tax_rate_1',
        'i': 'tax_rate_2',
        'j': 'iso_country_code',
        'k': 'marc_country_code',
        'm': 'identification_of_pricing_entity',
        '2': 'source_of_price_type_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'price_type_code': value.get('a'),
        'price_amount': value.get('b'),
        'currency_code': value.get('c'),
        'unit_of_pricing': value.get('d'),
        'price_note': value.get('e'),
        'price_effective_from': value.get('f'),
        'price_effective_until': value.get('g'),
        'tax_rate_1': value.get('h'),
        'tax_rate_2': value.get('i'),
        'iso_country_code': value.get('j'),
        'marc_country_code': value.get('k'),
        'identification_of_pricing_entity': value.get('m'),
        'source_of_price_type_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('trade_availability_information', '^366__')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
    """Trade Availability Information."""
    field_map = {
        'a': 'publishers_compressed_title_identification',
        'b': 'detailed_date_of_publication',
        'c': 'availability_status_code',
        'd': 'expected_next_availability_date',
        'e': 'note',
        'f': 'publishers_discount_category',
        'g': 'date_made_out_of_print',
        'j': 'iso_country_code',
        'k': 'marc_country_code',
        'm': 'identification_of_agency',
        '2': 'source_of_availability_status_code',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'publishers_compressed_title_identification': value.get('a'),
        'detailed_date_of_publication': value.get('b'),
        'availability_status_code': value.get('c'),
        'expected_next_availability_date': value.get('d'),
        'note': value.get('e'),
        'publisher_s_discount_category': value.get('f'),
        'date_made_out_of_print': value.get('g'),
        'iso_country_code': value.get('j'),
        'marc_country_code': value.get('k'),
        'identification_of_agency': value.get('m'),
        'source_of_availability_status_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('associated_place', '^370__')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'c': 'associated_country',
        'f': 'other_associated_place',
        'g': 'place_of_origin_of_work',
        's': 'start_period',
        't': 'end_period',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'associated_country': utils.force_list(
            value.get('c')),
        'other_associated_place': utils.force_list(
            value.get('f')),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')),
        'start_period': value.get('s'),
        'end_period': value.get('t'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')),
        'source_of_information': utils.force_list(
            value.get('v')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')),
    }


@marc21.over('associated_language', '^377_[_7]')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {
        '_': 'MARC language code',
        '7': 'Source specified in subfield $2',
    }

    field_map = {
        'a': 'language_code',
        'l': 'language_term',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[4] in indicator_map2:
        order.append('source_of_code')

    if key[4] != '7':
        try:
            order.remove('source')
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'language_code': utils.force_list(
            value.get('a')
        ),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': indicator_map2.get(key[4]),
    }


@marc21.over('form_of_work', '^380__')
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
    'other_distinguishing_characteristics_of_work_or_expression', '^381__')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(
        self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'a': 'other_distinguishing_characteristic',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
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
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
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


@marc21.over('medium_of_performance', '^382[_01][_01]')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {
        '_': 'No information provided',
        '0': 'Medium of performance',
        '1': 'Partial medium of performance',
    }

    indicator_map2 = {
        '_': 'No information provided',
        '0': 'Not intended for access',
        '1': 'Intended for access',
    }

    field_map = {
        'a': 'medium_of_performance',
        'b': 'soloist',
        'd': 'doubling_instrument',
        'e': 'number_of_ensembles',
        'n': 'number_of_performers_of_the_same_medium',
        'p': 'alternative_medium_of_performance',
        's': 'total_number_of_performers',
        'v': 'note',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('display_constant_controller')
    if key[4] in indicator_map2:
        order.append('access_control')

    return {
        '__order__': tuple(order) if len(order) else None,
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'number_of_ensembles': utils.force_list(value.get('e')),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'total_number_of_performers': utils.force_list(
            value.get('s')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
        'access_control': indicator_map2.get(key[4]),
    }


@marc21.over('numeric_designation_of_musical_work', '^383__')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'a': 'serial_number',
        'b': 'opus_number',
        'c': 'thematic_index_number',
        'd': 'thematic_index_code',
        'e': 'publisher_associated_with_opus_number',
        '2': 'source',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'thematic_index_code': value.get('d'),
        'publisher_associated_with_opus_number': value.get('e'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('key', '^384[_01]_')
@utils.filter_values
def key(self, key, value):
    """Key."""
    indicator_map1 = {
        '_': 'Relationship to original unknown',
        '0': 'Original key',
        '1': 'Transposed key',
    }

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


@marc21.over('audience_characteristics', '^385__')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'a': 'audience_term',
        'b': 'audience_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('creator_contributor_characteristics', '^386__')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'a': 'creator_contributor_term',
        'b': 'creator_contributor_code',
        'm': 'demographic_group_term',
        'n': 'demographic_group_code',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('time_period_of_creation', '^388[_12]_')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {
        '_': 'No information provided',
        '1': 'Creation of work',
        '2': 'Creation of aggregate work',
    }

    field_map = {
        'a': 'time_period_of_creation_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '3': 'materials_specified',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
    }

    order = utils.map_order(field_map, value)

    if key[3] in indicator_map1:
        order.append('type_of_time_period')

    return {
        '__order__': tuple(order) if len(order) else None,
        'time_period_of_creation_term': utils.force_list(
            value.get('a')),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')),
        'source_of_term': value.get('2'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list('8'),
        'type_of_time_period': indicator_map1.get(
            key[3]),
    }
