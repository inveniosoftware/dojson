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

from ..model import marc21_liberal


@marc21_liberal.over('physical_description', '^300..')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    """Physical Description."""
    field_map = {
        'e': 'accompanying_material',
        'c': 'dimensions',
        'b': 'other_physical_details',
        '8': 'field_link_and_sequence_number',
        'a': 'extent',
        'f': 'type_of_unit',
        'g': 'size_of_unit',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'accompanying_material': value.get('e'),
        'dimensions': utils.force_list(
            value.get('c')
        ),
        'other_physical_details': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'extent': utils.force_list(
            value.get('a')
        ),
        'type_of_unit': utils.force_list(
            value.get('f')
        ),
        'size_of_unit': utils.force_list(
            value.get('g')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('playing_time', '^306..')
@utils.filter_values
def playing_time(self, key, value):
    """Playing Time."""
    field_map = {
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'playing_time',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'playing_time': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('hours', '^307..')
@utils.for_each_value
@utils.filter_values
def hours(self, key, value):
    """Hours, Etc.."""
    indicator_map1 = {"8": "No display constant generated", "_": "Hours"}
    field_map = {
        'b': 'additional_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'hours',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'additional_information': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'hours': value.get('a'),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('current_publication_frequency', '^310..')
@utils.filter_values
def current_publication_frequency(self, key, value):
    """Current Publication Frequency."""
    field_map = {
        'b': 'date_of_current_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'current_publication_frequency',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'date_of_current_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'current_publication_frequency': value.get('a'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('former_publication_frequency', '^321..')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    """Former Publication Frequency."""
    field_map = {
        'b': 'dates_of_former_publication_frequency',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'former_publication_frequency',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'dates_of_former_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'former_publication_frequency': value.get('a'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'content_type_term',
        '3': 'materials_specified',
        'b': 'content_type_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    """Media Type."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'media_type_term',
        '3': 'materials_specified',
        'b': 'media_type_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'media_type_term': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'media_type_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    """Carrier Type."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'carrier_type_term',
        '3': 'materials_specified',
        'b': 'carrier_type_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'carrier_type_term': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'carrier_type_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('physical_medium', '^340..')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    """Physical Medium."""
    field_map = {
        'c': 'materials_applied_to_surface',
        'b': 'dimensions',
        '8': 'field_link_and_sequence_number',
        'm': 'book_format',
        'n': 'font_size',
        'd': 'information_recording_technique',
        'o': 'polarity',
        '6': 'linkage',
        'e': 'support',
        '0': 'authority_record_control_number_or_standard_number',
        'f': 'production_rate_ratio',
        '2': 'source',
        'a': 'material_base_and_configuration',
        'j': 'generation',
        'i': 'technical_specifications_of_medium',
        'k': 'layout',
        '3': 'materials_specified',
        'h': 'location_within_medium',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'materials_applied_to_surface': utils.force_list(
            value.get('c')
        ),
        'dimensions': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'book_format': utils.force_list(
            value.get('m')
        ),
        'font_size': utils.force_list(
            value.get('n')
        ),
        'information_recording_technique': utils.force_list(
            value.get('d')
        ),
        'polarity': utils.force_list(
            value.get('o')
        ),
        'linkage': value.get('6'),
        'support': utils.force_list(
            value.get('e')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'production_rate_ratio': utils.force_list(
            value.get('f')
        ),
        'source': value.get('2'),
        'material_base_and_configuration': utils.force_list(
            value.get('a')
        ),
        'generation': utils.force_list(
            value.get('j')
        ),
        'technical_specifications_of_medium': utils.force_list(
            value.get('i')
        ),
        'layout': utils.force_list(
            value.get('k')
        ),
        'materials_specified': value.get('3'),
        'location_within_medium': utils.force_list(
            value.get('h')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('geospatial_reference_data', '^342..')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    """Geospatial Reference Data."""
    indicator_map1 = {"0": "Horizontal coordinate system", "1": "Vertical coordinate system"}
    indicator_map2 = {"0": "Geographic", "1": "Map projection", "2": "Grid coordinate system", "3": "Local planar", "4": "Local", "5": "Geodetic model", "6": "Altitude", "7": "Method specified in $2", "8": "Depth"}
    field_map = {
        'p': 'zone_identifier',
        'b': 'coordinate_units_or_distance_units',
        'g': 'longitude_of_central_meridian_or_projection_center',
        'l': 'height_of_perspective_point_above_surface',
        'd': 'longitude_resolution',
        'o': 'landsat_number_and_path_number',
        'k': 'scale_factor',
        'e': 'standard_parallel_or_oblique_line_latitude',
        't': 'vertical_resolution',
        'f': 'oblique_line_longitude',
        '2': 'reference_method_used',
        'a': 'name',
        'j': 'false_northing',
        'h': 'latitude_of_projection_center_or_projection_origin',
        'c': 'latitude_resolution',
        'u': 'vertical_encoding_method',
        '8': 'field_link_and_sequence_number',
        'w': 'local_planar_or_local_georeference_information',
        '6': 'linkage',
        'i': 'false_easting',
        'm': 'azimuthal_angle',
        'q': 'ellipsoid_name',
        'r': 'semi_major_axis',
        's': 'denominator_of_flattening_ratio',
        'n': 'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole',
        'v': 'local_planar_local_or_other_projection_or_grid_description',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('geospatial_reference_dimension')

    if key[4] != '_':
        order.append('geospatial_reference_method')

    record_dict = {
        '__order__': order if len(order) else None,
        'zone_identifier': value.get('p'),
        'coordinate_units_or_distance_units': value.get('b'),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'height_of_perspective_point_above_surface': value.get('l'),
        'longitude_resolution': value.get('d'),
        'landsat_number_and_path_number': value.get('o'),
        'scale_factor': value.get('k'),
        'standard_parallel_or_oblique_line_latitude': utils.force_list(
            value.get('e')
        ),
        'vertical_resolution': value.get('t'),
        'oblique_line_longitude': utils.force_list(
            value.get('f')
        ),
        'reference_method_used': value.get('2'),
        'name': value.get('a'),
        'false_northing': value.get('j'),
        'latitude_of_projection_center_or_projection_origin': value.get('h'),
        'latitude_resolution': value.get('c'),
        'vertical_encoding_method': value.get('u'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'local_planar_or_local_georeference_information': value.get('w'),
        'linkage': value.get('6'),
        'false_easting': value.get('i'),
        'azimuthal_angle': value.get('m'),
        'ellipsoid_name': value.get('q'),
        'semi_major_axis': value.get('r'),
        'denominator_of_flattening_ratio': value.get('s'),
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': value.get('n'),
        'local_planar_local_or_other_projection_or_grid_description': value.get('v'),
        'geospatial_reference_dimension': indicator_map1.get(key[3], key[3]),
        'geospatial_reference_method': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('planar_coordinate_data', '^343..')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
    """Planar Coordinate Data."""
    field_map = {
        'e': 'distance_resolution',
        'c': 'abscissa_resolution',
        'h': 'bearing_reference_direction',
        'b': 'planar_distance_units',
        '8': 'field_link_and_sequence_number',
        'a': 'planar_coordinate_encoding_method',
        'f': 'bearing_resolution',
        'g': 'bearing_units',
        '6': 'linkage',
        'i': 'bearing_reference_meridian',
        'd': 'ordinate_resolution',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'distance_resolution': value.get('e'),
        'abscissa_resolution': value.get('c'),
        'bearing_reference_direction': value.get('h'),
        'planar_distance_units': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'planar_coordinate_encoding_method': value.get('a'),
        'bearing_resolution': value.get('f'),
        'bearing_units': value.get('g'),
        'linkage': value.get('6'),
        'bearing_reference_meridian': value.get('i'),
        'ordinate_resolution': value.get('d'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('sound_characteristics', '^344..')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    """Sound Characteristics."""
    field_map = {
        'c': 'playing_speed',
        'b': 'recording_medium',
        '8': 'field_link_and_sequence_number',
        'g': 'configuration_of_playback_channels',
        'd': 'groove_characteristic',
        '6': 'linkage',
        'e': 'track_configuration',
        '0': 'authority_record_control_number_or_standard_number',
        'f': 'tape_configuration',
        '2': 'source',
        'a': 'type_of_recording',
        '3': 'materials_specified',
        'h': 'special_playback_characteristics',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'playing_speed': utils.force_list(
            value.get('c')
        ),
        'recording_medium': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'configuration_of_playback_channels': utils.force_list(
            value.get('g')
        ),
        'groove_characteristic': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'track_configuration': utils.force_list(
            value.get('e')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'tape_configuration': utils.force_list(
            value.get('f')
        ),
        'source': value.get('2'),
        'type_of_recording': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'special_playback_characteristics': utils.force_list(
            value.get('h')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('projection_characteristics_of_moving_image', '^345..')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    """Projection Characteristics of Moving Image."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'presentation_format',
        '3': 'materials_specified',
        'b': 'projection_speed',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'presentation_format': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'projection_speed': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('video_characteristics', '^346..')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    """Video Characteristics."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'video_format',
        '3': 'materials_specified',
        'b': 'broadcast_standard',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'video_format': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'broadcast_standard': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('digital_file_characteristics', '^347..')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    """Digital File Characteristics."""
    field_map = {
        'e': 'regional_encoding',
        'c': 'file_size',
        'd': 'resolution',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'file_type',
        'f': 'encoded_bitrate',
        '3': 'materials_specified',
        'b': 'encoding_format',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'regional_encoding': utils.force_list(
            value.get('e')
        ),
        'file_size': utils.force_list(
            value.get('c')
        ),
        'resolution': utils.force_list(
            value.get('d')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'file_type': utils.force_list(
            value.get('a')
        ),
        'encoded_bitrate': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'encoding_format': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('format_of_notated_music', '^348..')
@utils.for_each_value
@utils.filter_values
def format_of_notated_music(self, key, value):
    """Format of Notated Music."""
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'a': 'format_of_notated_music_term',
        '3': 'materials_specified',
        'b': 'format_of_notated_music_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'format_of_notated_music_term': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'format_of_notated_music_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    """Organization and Arrangement of Materials."""
    field_map = {
        'c': 'hierarchical_level',
        'b': 'arrangement',
        '8': 'field_link_and_sequence_number',
        'a': 'organization',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'hierarchical_level': value.get('c'),
        'arrangement': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'organization': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('digital_graphic_representation', '^352..')
@utils.for_each_value
@utils.filter_values
def digital_graphic_representation(self, key, value):
    """Digital Graphic Representation."""
    field_map = {
        'e': 'column_count',
        'c': 'object_count',
        'b': 'object_type',
        '8': 'field_link_and_sequence_number',
        'a': 'direct_reference_method',
        'f': 'vertical_count',
        'q': 'format_of_the_digital_image',
        'g': 'vpf_topology_level',
        '6': 'linkage',
        'i': 'indirect_reference_description',
        'd': 'row_count',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'column_count': value.get('e'),
        'object_count': utils.force_list(
            value.get('c')
        ),
        'object_type': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'direct_reference_method': value.get('a'),
        'vertical_count': value.get('f'),
        'format_of_the_digital_image': value.get('q'),
        'vpf_topology_level': value.get('g'),
        'linkage': value.get('6'),
        'indirect_reference_description': value.get('i'),
        'row_count': value.get('d'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('security_classification_control', '^355..')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    """Security Classification Control."""
    indicator_map1 = {"0": "Document", "1": "Title", "2": "Abstract", "3": "Contents note", "4": "Author", "5": "Record", "8": "None of the above"}
    field_map = {
        'e': 'classification_system',
        'c': 'external_dissemination_information',
        'h': 'declassification_date',
        'b': 'handling_instructions',
        '8': 'field_link_and_sequence_number',
        'a': 'security_classification',
        'f': 'country_of_origin_code',
        'j': 'authorization',
        'g': 'downgrading_date',
        '6': 'linkage',
        'd': 'downgrading_or_declassification_event',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('controlled_element')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'classification_system': value.get('e'),
        'external_dissemination_information': utils.force_list(
            value.get('c')
        ),
        'declassification_date': value.get('h'),
        'handling_instructions': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'security_classification': value.get('a'),
        'country_of_origin_code': value.get('f'),
        'authorization': utils.force_list(
            value.get('j')
        ),
        'downgrading_date': value.get('g'),
        'linkage': value.get('6'),
        'downgrading_or_declassification_event': value.get('d'),
        'controlled_element': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('originator_dissemination_control', '^357..')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    """Originator Dissemination Control."""
    field_map = {
        'c': 'authorized_recipients_of_material',
        'b': 'originating_agency',
        '8': 'field_link_and_sequence_number',
        'a': 'originator_control_term',
        'g': 'other_restrictions',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authorized_recipients_of_material': utils.force_list(
            value.get('c')
        ),
        'originating_agency': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'originator_control_term': value.get('a'),
        'other_restrictions': utils.force_list(
            value.get('g')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('dates_of_publication_and_or_sequential_designation', '^362..')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    """Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted note"}
    field_map = {
        'z': 'source_of_information',
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'dates_of_publication_and_or_sequential_designation',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('format_of_date')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'format_of_date': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('normalized_date_and_sequential_designation', '^363..')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    """Normalized Date and Sequential Designation."""
    indicator_map1 = {"0": "Starting information", "1": "Ending information", "_": "No information provided"}
    indicator_map2 = {"0": "Closed", "1": "Open", "_": "Not specified"}
    field_map = {
        'x': 'nonpublic_note',
        'c': 'third_level_of_enumeration',
        'u': 'first_level_textual_designation',
        'b': 'second_level_of_enumeration',
        '8': 'field_link_and_sequence_number',
        'g': 'alternative_numbering_scheme_first_level_of_enumeration',
        'z': 'public_note',
        'v': 'first_level_of_chronology_issuance',
        '6': 'linkage',
        'i': 'first_level_of_chronology',
        'e': 'fifth_level_of_enumeration',
        'l': 'fourth_level_of_chronology',
        'd': 'fourth_level_of_enumeration',
        'f': 'sixth_level_of_enumeration',
        'a': 'first_level_of_enumeration',
        'j': 'second_level_of_chronology',
        'm': 'alternative_numbering_scheme_chronology',
        'k': 'third_level_of_chronology',
        'h': 'alternative_numbering_scheme_second_level_of_enumeration',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('start_end_designator')

    if key[4] != '_':
        order.append('state_of_issuance')

    record_dict = {
        '__order__': order if len(order) else None,
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'third_level_of_enumeration': value.get('c'),
        'first_level_textual_designation': value.get('u'),
        'second_level_of_enumeration': value.get('b'),
        'field_link_and_sequence_number': value.get('8'),
        'alternative_numbering_scheme_first_level_of_enumeration': value.get('g'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'first_level_of_chronology_issuance': value.get('v'),
        'linkage': value.get('6'),
        'first_level_of_chronology': value.get('i'),
        'fifth_level_of_enumeration': value.get('e'),
        'fourth_level_of_chronology': value.get('l'),
        'fourth_level_of_enumeration': value.get('d'),
        'sixth_level_of_enumeration': value.get('f'),
        'first_level_of_enumeration': value.get('a'),
        'second_level_of_chronology': value.get('j'),
        'alternative_numbering_scheme_chronology': value.get('m'),
        'third_level_of_chronology': value.get('k'),
        'alternative_numbering_scheme_second_level_of_enumeration': value.get('h'),
        'start_end_designator': indicator_map1.get(key[3], key[3]),
        'state_of_issuance': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('trade_price', '^365..')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
    """Trade Price."""
    field_map = {
        'c': 'currency_code',
        'm': 'identification_of_pricing_entity',
        'b': 'price_amount',
        '8': 'field_link_and_sequence_number',
        'g': 'price_effective_until',
        '6': 'linkage',
        'd': 'unit_of_pricing',
        'e': 'price_note',
        'f': 'price_effective_from',
        '2': 'source_of_price_type_code',
        'a': 'price_type_code',
        'j': 'iso_country_code',
        'i': 'tax_rate_2',
        'k': 'marc_country_code',
        'h': 'tax_rate_1',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'currency_code': value.get('c'),
        'identification_of_pricing_entity': value.get('m'),
        'price_amount': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'price_effective_until': value.get('g'),
        'linkage': value.get('6'),
        'unit_of_pricing': value.get('d'),
        'price_note': value.get('e'),
        'price_effective_from': value.get('f'),
        'source_of_price_type_code': value.get('2'),
        'price_type_code': value.get('a'),
        'iso_country_code': value.get('j'),
        'tax_rate_2': value.get('i'),
        'marc_country_code': value.get('k'),
        'tax_rate_1': value.get('h'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('trade_availability_information', '^366..')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
    """Trade Availability Information."""
    field_map = {
        'c': 'availability_status_code',
        'b': 'detailed_date_of_publication',
        '8': 'field_link_and_sequence_number',
        'g': 'date_made_out_of_print',
        '6': 'linkage',
        'd': 'expected_next_availability_date',
        'e': 'note',
        'f': 'publisher_s_discount_category',
        '2': 'source_of_availability_status_code',
        'a': 'publishers_compressed_title_identification',
        'j': 'iso_country_code',
        'm': 'identification_of_agency',
        'k': 'marc_country_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'availability_status_code': value.get('c'),
        'detailed_date_of_publication': value.get('b'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_made_out_of_print': value.get('g'),
        'linkage': value.get('6'),
        'expected_next_availability_date': value.get('d'),
        'note': value.get('e'),
        'publisher_s_discount_category': value.get('f'),
        'source_of_availability_status_code': value.get('2'),
        'publishers_compressed_title_identification': value.get('a'),
        'iso_country_code': value.get('j'),
        'identification_of_agency': value.get('m'),
        'marc_country_code': value.get('k'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('associated_place', '^370..')
@utils.for_each_value
@utils.filter_values
def associated_place(self, key, value):
    """Associated Place."""
    field_map = {
        'v': 'source_of_information',
        'c': 'associated_country',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'g': 'place_of_origin_of_work',
        's': 'start_period',
        'u': 'uniform_resource_identifier',
        '6': 'linkage',
        't': 'end_period',
        'f': 'other_associated_place',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'associated_country': utils.force_list(
            value.get('c')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'place_of_origin_of_work': utils.force_list(
            value.get('g')
        ),
        'start_period': value.get('s'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'end_period': value.get('t'),
        'other_associated_place': utils.force_list(
            value.get('f')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    indicator_map2 = {"7": "Source specified in subfield $2", "_": "MARC language code"}
    field_map = {
        'l': 'language_term',
        '8': 'field_link_and_sequence_number',
        '6': 'linkage',
        '2': 'source',
        'a': 'language_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('source_of_code')

    record_dict = {
        '__order__': order if len(order) else None,
        'language_term': utils.force_list(
            value.get('l')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'source': value.get('2'),
        'language_code': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        'source_of_code': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    field_map = {
        '8': 'field_link_and_sequence_number',
        '0': 'record_control_number',
        '6': 'linkage',
        '2': 'source_of_term',
        'a': 'form_of_work',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'linkage': value.get('6'),
        'source_of_term': value.get('2'),
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        '0': 'record_control_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'a': 'other_distinguishing_characteristic',
        'u': 'uniform_resource_identifier',
        'v': 'source_of_information',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('medium_of_performance', '^382..')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {"0": "Medium of performance", "1": "Partial medium of performance", "_": "No information provided"}
    indicator_map2 = {"0": "Not intended for access", "1": "Intended for access", "_": "No information provided"}
    field_map = {
        'p': 'alternative_medium_of_performance',
        'b': 'soloist',
        '8': 'field_link_and_sequence_number',
        'n': 'number_of_performers_of_the_same_medium',
        'd': 'doubling_instrument',
        't': 'total_number_of_ensembles',
        '6': 'linkage',
        'e': 'number_of_ensembles_of_the_same_type',
        'r': 'total_number_of_individuals_performing_alongside_ensembles',
        's': 'total_number_of_performers',
        '2': 'source_of_term',
        'a': 'medium_of_performance',
        '0': 'authority_record_control_number_or_standard_number',
        'v': 'note',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('display_constant_controller')

    if key[4] != '_':
        order.append('access_control')

    record_dict = {
        '__order__': order if len(order) else None,
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'total_number_of_ensembles': value.get('t'),
        'linkage': value.get('6'),
        'number_of_ensembles_of_the_same_type': utils.force_list(
            value.get('e')
        ),
        'total_number_of_individuals_performing_alongside_ensembles': value.get('r'),
        'total_number_of_performers': value.get('s'),
        'source_of_term': value.get('2'),
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'display_constant_controller': indicator_map1.get(key[3], key[3]),
        'access_control': indicator_map2.get(key[4], key[4]),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    field_map = {
        'c': 'thematic_index_number',
        '2': 'source',
        'b': 'opus_number',
        '8': 'field_link_and_sequence_number',
        'a': 'serial_number',
        'e': 'publisher_associated_with_opus_number',
        '6': 'linkage',
        'd': 'thematic_index_code',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'thematic_index_number': utils.force_list(
            value.get('c')
        ),
        'source': value.get('2'),
        'opus_number': utils.force_list(
            value.get('b')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'publisher_associated_with_opus_number': value.get('e'),
        'linkage': value.get('6'),
        'thematic_index_code': value.get('d'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('key', '^384..')
@utils.filter_values
def key(self, key, value):
    """Key."""
    indicator_map1 = {"0": "Original key", "1": "Transposed key", "_": "Relationship to original unknown"}
    field_map = {
        '6': 'linkage',
        '8': 'field_link_and_sequence_number',
        'a': 'key',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('key_type')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key': value.get('a'),
        'key_type': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    field_map = {
        'm': 'demographic_group_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'audience_term',
        'n': 'demographic_group_code',
        '3': 'materials_specified',
        'b': 'audience_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'demographic_group_term': value.get('m'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'audience_term': utils.force_list(
            value.get('a')
        ),
        'demographic_group_code': value.get('n'),
        'materials_specified': value.get('3'),
        'audience_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    field_map = {
        'm': 'demographic_group_term',
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source',
        '8': 'field_link_and_sequence_number',
        'a': 'creator_contributor_term',
        'n': 'demographic_group_code',
        '3': 'materials_specified',
        'b': 'creator_contributor_code',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('$ind1')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'demographic_group_term': value.get('m'),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'creator_contributor_term': utils.force_list(
            value.get('a')
        ),
        'demographic_group_code': value.get('n'),
        'materials_specified': value.get('3'),
        'creator_contributor_code': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        '$ind1': key[3] if key[3] != '_' else None,
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@marc21_liberal.over('time_period_of_creation', '^388..')
@utils.for_each_value
@utils.filter_values
def time_period_of_creation(self, key, value):
    """Time Period of Creation."""
    indicator_map1 = {"1": "Creation of work", "2": "Creation of aggregate work", "_": "No information provided"}
    field_map = {
        '0': 'authority_record_control_number_or_standard_number',
        '2': 'source_of_term',
        '8': 'field_link_and_sequence_number',
        'a': 'time_period_of_creation_term',
        '3': 'materials_specified',
        '6': 'linkage',
    }

    order = utils.map_order(field_map, value, liberal=True)

    if key[3] != '_':
        order.append('type_of_time_period')

    if key[4] != '_':
        order.append('$ind2')

    record_dict = {
        '__order__': order if len(order) else None,
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'time_period_of_creation_term': utils.force_list(
            value.get('a')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'type_of_time_period': indicator_map1.get(key[3], key[3]),
        '$ind2': key[4] if key[4] != '_' else None,
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys():
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
