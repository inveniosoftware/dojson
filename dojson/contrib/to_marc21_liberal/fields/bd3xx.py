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


@to_marc21_liberal.over('300', '^physical_description$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_description(self, key, value):
    """Reverse - Physical Description."""
    field_map = {
        'other_physical_details': 'b',
        'dimensions': 'c',
        'materials_specified': '3',
        'accompanying_material': 'e',
        'linkage': '6',
        'size_of_unit': 'g',
        'type_of_unit': 'f',
        'field_link_and_sequence_number': '8',
        'extent': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': value.get('other_physical_details'),
        'c': utils.reverse_force_list(
            value.get('dimensions')
        ),
        '3': value.get('materials_specified'),
        'e': value.get('accompanying_material'),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('size_of_unit')
        ),
        'f': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('extent')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('306', '^playing_time$')
@utils.filter_values
def reverse_playing_time(self, key, value):
    """Reverse - Playing Time."""
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'playing_time': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('playing_time')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('307', '^hours$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_hours(self, key, value):
    """Reverse - Hours, Etc.."""
    indicator_map1 = {"Hours": "_", "No display constant generated": "8"}
    field_map = {
        'linkage': '6',
        'additional_information': 'b',
        'field_link_and_sequence_number': '8',
        'hours': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('additional_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('hours'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('310', '^current_publication_frequency$')
@utils.filter_values
def reverse_current_publication_frequency(self, key, value):
    """Reverse - Current Publication Frequency."""
    field_map = {
        'linkage': '6',
        'date_of_current_publication_frequency': 'b',
        'field_link_and_sequence_number': '8',
        'current_publication_frequency': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('date_of_current_publication_frequency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('current_publication_frequency'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('321', '^former_publication_frequency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_publication_frequency(self, key, value):
    """Reverse - Former Publication Frequency."""
    field_map = {
        'linkage': '6',
        'dates_of_former_publication_frequency': 'b',
        'field_link_and_sequence_number': '8',
        'former_publication_frequency': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'b': value.get('dates_of_former_publication_frequency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('former_publication_frequency'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'content_type_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'content_type_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('337', '^media_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_media_type(self, key, value):
    """Reverse - Media Type."""
    field_map = {
        'media_type_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'media_type_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('media_type_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('media_type_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('338', '^carrier_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_carrier_type(self, key, value):
    """Reverse - Carrier Type."""
    field_map = {
        'carrier_type_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'carrier_type_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('carrier_type_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('carrier_type_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('340', '^physical_medium$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_medium(self, key, value):
    """Reverse - Physical Medium."""
    field_map = {
        'materials_specified': '3',
        'production_rate_ratio': 'f',
        'support': 'e',
        'materials_applied_to_surface': 'c',
        'field_link_and_sequence_number': '8',
        'material_base_and_configuration': 'a',
        'technical_specifications_of_medium': 'i',
        'location_within_medium': 'h',
        'dimensions': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'generation': 'j',
        'linkage': '6',
        'font_size': 'n',
        'source': '2',
        'information_recording_technique': 'd',
        'layout': 'k',
        'polarity': 'o',
        'book_format': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'f': utils.reverse_force_list(
            value.get('production_rate_ratio')
        ),
        'e': utils.reverse_force_list(
            value.get('support')
        ),
        'c': utils.reverse_force_list(
            value.get('materials_applied_to_surface')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('material_base_and_configuration')
        ),
        'i': utils.reverse_force_list(
            value.get('technical_specifications_of_medium')
        ),
        'h': utils.reverse_force_list(
            value.get('location_within_medium')
        ),
        'b': utils.reverse_force_list(
            value.get('dimensions')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'j': utils.reverse_force_list(
            value.get('generation')
        ),
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('font_size')
        ),
        '2': value.get('source'),
        'd': utils.reverse_force_list(
            value.get('information_recording_technique')
        ),
        'k': utils.reverse_force_list(
            value.get('layout')
        ),
        'o': utils.reverse_force_list(
            value.get('polarity')
        ),
        'm': utils.reverse_force_list(
            value.get('book_format')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('342', '^geospatial_reference_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geospatial_reference_data(self, key, value):
    """Reverse - Geospatial Reference Data."""
    indicator_map1 = {"Horizontal coordinate system": "0", "Vertical coordinate system": "1"}
    indicator_map2 = {"Altitude": "6", "Depth": "8", "Geodetic model": "5", "Geographic": "0", "Grid coordinate system": "2", "Local": "4", "Local planar": "3", "Map projection": "1", "Method specified in $2": "7"}
    field_map = {
        'vertical_encoding_method': 'u',
        'standard_parallel_or_oblique_line_latitude': 'e',
        'vertical_resolution': 't',
        'latitude_of_projection_center_or_projection_origin': 'h',
        'coordinate_units_or_distance_units': 'b',
        'longitude_resolution': 'd',
        'linkage': '6',
        'landsat_number_and_path_number': 'o',
        'reference_method_used': '2',
        'scale_factor': 'k',
        'ellipsoid_name': 'q',
        'azimuthal_angle': 'm',
        'semi_major_axis': 'r',
        'height_of_perspective_point_above_surface': 'l',
        'oblique_line_longitude': 'f',
        'latitude_resolution': 'c',
        'field_link_and_sequence_number': '8',
        'name': 'a',
        'false_easting': 'i',
        'zone_identifier': 'p',
        'denominator_of_flattening_ratio': 's',
        'false_northing': 'j',
        'local_planar_or_local_georeference_information': 'w',
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': 'n',
        'longitude_of_central_meridian_or_projection_center': 'g',
        'local_planar_local_or_other_projection_or_grid_description': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['geospatial_reference_dimension', 'geospatial_reference_method'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': value.get('vertical_encoding_method'),
        'e': utils.reverse_force_list(
            value.get('standard_parallel_or_oblique_line_latitude')
        ),
        't': value.get('vertical_resolution'),
        'h': value.get('latitude_of_projection_center_or_projection_origin'),
        'b': value.get('coordinate_units_or_distance_units'),
        'd': value.get('longitude_resolution'),
        '6': value.get('linkage'),
        'o': value.get('landsat_number_and_path_number'),
        '2': value.get('reference_method_used'),
        'k': value.get('scale_factor'),
        'q': value.get('ellipsoid_name'),
        'm': value.get('azimuthal_angle'),
        'r': value.get('semi_major_axis'),
        'l': value.get('height_of_perspective_point_above_surface'),
        'f': utils.reverse_force_list(
            value.get('oblique_line_longitude')
        ),
        'c': value.get('latitude_resolution'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('name'),
        'i': value.get('false_easting'),
        'p': value.get('zone_identifier'),
        's': value.get('denominator_of_flattening_ratio'),
        'j': value.get('false_northing'),
        'w': value.get('local_planar_or_local_georeference_information'),
        'n': value.get('azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole'),
        'g': value.get('longitude_of_central_meridian_or_projection_center'),
        'v': value.get('local_planar_local_or_other_projection_or_grid_description'),
        '$ind1': indicator_map1.get(value.get('geospatial_reference_dimension'), value.get('geospatial_reference_dimension', '_')),
        '$ind2': '7' if 'geospatial_reference_method' in value and
        not indicator_map2.get(value.get('geospatial_reference_method')) and
        value.get('geospatial_reference_method') == value.get('reference_method_used') and
        field_map.get('geospatial_reference_method') in order
        else indicator_map2.get(value.get('geospatial_reference_method'), value.get('geospatial_reference_method', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('343', '^planar_coordinate_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_planar_coordinate_data(self, key, value):
    """Reverse - Planar Coordinate Data."""
    field_map = {
        'bearing_reference_direction': 'h',
        'planar_distance_units': 'b',
        'ordinate_resolution': 'd',
        'bearing_reference_meridian': 'i',
        'distance_resolution': 'e',
        'linkage': '6',
        'bearing_units': 'g',
        'bearing_resolution': 'f',
        'abscissa_resolution': 'c',
        'field_link_and_sequence_number': '8',
        'planar_coordinate_encoding_method': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('bearing_reference_direction'),
        'b': value.get('planar_distance_units'),
        'd': value.get('ordinate_resolution'),
        'i': value.get('bearing_reference_meridian'),
        'e': value.get('distance_resolution'),
        '6': value.get('linkage'),
        'g': value.get('bearing_units'),
        'f': value.get('bearing_resolution'),
        'c': value.get('abscissa_resolution'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('planar_coordinate_encoding_method'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('344', '^sound_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_sound_characteristics(self, key, value):
    """Reverse - Sound Characteristics."""
    field_map = {
        'materials_specified': '3',
        'tape_configuration': 'f',
        'track_configuration': 'e',
        'playing_speed': 'c',
        'field_link_and_sequence_number': '8',
        'type_of_recording': 'a',
        'special_playback_characteristics': 'h',
        'recording_medium': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'configuration_of_playback_channels': 'g',
        'source': '2',
        'groove_characteristic': 'd',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'f': utils.reverse_force_list(
            value.get('tape_configuration')
        ),
        'e': utils.reverse_force_list(
            value.get('track_configuration')
        ),
        'c': utils.reverse_force_list(
            value.get('playing_speed')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_recording')
        ),
        'h': utils.reverse_force_list(
            value.get('special_playback_characteristics')
        ),
        'b': utils.reverse_force_list(
            value.get('recording_medium')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('configuration_of_playback_channels')
        ),
        '2': value.get('source'),
        'd': utils.reverse_force_list(
            value.get('groove_characteristic')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('345', '^projection_characteristics_of_moving_image$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_projection_characteristics_of_moving_image(self, key, value):
    """Reverse - Projection Characteristics of Moving Image."""
    field_map = {
        'projection_speed': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'presentation_format': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('projection_speed')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('346', '^video_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_video_characteristics(self, key, value):
    """Reverse - Video Characteristics."""
    field_map = {
        'broadcast_standard': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'video_format': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('broadcast_standard')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('video_format')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('347', '^digital_file_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_file_characteristics(self, key, value):
    """Reverse - Digital File Characteristics."""
    field_map = {
        'encoding_format': 'b',
        'resolution': 'd',
        'file_size': 'c',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'regional_encoding': 'e',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'file_type': 'a',
        'encoded_bitrate': 'f',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('encoding_format')
        ),
        'd': utils.reverse_force_list(
            value.get('resolution')
        ),
        'c': utils.reverse_force_list(
            value.get('file_size')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'e': utils.reverse_force_list(
            value.get('regional_encoding')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('file_type')
        ),
        'f': utils.reverse_force_list(
            value.get('encoded_bitrate')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('348', '^format_of_notated_music$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_format_of_notated_music(self, key, value):
    """Reverse - Format of Notated Music."""
    field_map = {
        'format_of_notated_music_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'format_of_notated_music_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('351', '^organization_and_arrangement_of_materials$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_organization_and_arrangement_of_materials(self, key, value):
    """Reverse - Organization and Arrangement of Materials."""
    field_map = {
        'arrangement': 'b',
        'hierarchical_level': 'c',
        'materials_specified': '3',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'organization': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('arrangement')
        ),
        'c': value.get('hierarchical_level'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('organization')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('352', '^digital_graphic_representation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_graphic_representation(self, key, value):
    """Reverse - Digital Graphic Representation."""
    field_map = {
        'object_type': 'b',
        'row_count': 'd',
        'indirect_reference_description': 'i',
        'column_count': 'e',
        'linkage': '6',
        'vpf_topology_level': 'g',
        'vertical_count': 'f',
        'object_count': 'c',
        'field_link_and_sequence_number': '8',
        'format_of_the_digital_image': 'q',
        'direct_reference_method': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('object_type')
        ),
        'd': value.get('row_count'),
        'i': value.get('indirect_reference_description'),
        'e': value.get('column_count'),
        '6': value.get('linkage'),
        'g': value.get('vpf_topology_level'),
        'f': value.get('vertical_count'),
        'c': utils.reverse_force_list(
            value.get('object_count')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'q': value.get('format_of_the_digital_image'),
        'a': value.get('direct_reference_method'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('355', '^security_classification_control$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_security_classification_control(self, key, value):
    """Reverse - Security Classification Control."""
    indicator_map1 = {"Abstract": "2", "Author": "4", "Contents note": "3", "Document": "0", "None of the above": "8", "Record": "5", "Title": "1"}
    field_map = {
        'declassification_date': 'h',
        'handling_instructions': 'b',
        'downgrading_or_declassification_event': 'd',
        'classification_system': 'e',
        'authorization': 'j',
        'linkage': '6',
        'downgrading_date': 'g',
        'country_of_origin_code': 'f',
        'external_dissemination_information': 'c',
        'field_link_and_sequence_number': '8',
        'security_classification': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['controlled_element', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'h': value.get('declassification_date'),
        'b': utils.reverse_force_list(
            value.get('handling_instructions')
        ),
        'd': value.get('downgrading_or_declassification_event'),
        'e': value.get('classification_system'),
        'j': utils.reverse_force_list(
            value.get('authorization')
        ),
        '6': value.get('linkage'),
        'g': value.get('downgrading_date'),
        'f': value.get('country_of_origin_code'),
        'c': utils.reverse_force_list(
            value.get('external_dissemination_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('security_classification'),
        '$ind1': indicator_map1.get(value.get('controlled_element'), value.get('controlled_element', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('357', '^originator_dissemination_control$')
@utils.filter_values
def reverse_originator_dissemination_control(self, key, value):
    """Reverse - Originator Dissemination Control."""
    field_map = {
        'originating_agency': 'b',
        'other_restrictions': 'g',
        'linkage': '6',
        'authorized_recipients_of_material': 'c',
        'field_link_and_sequence_number': '8',
        'originator_control_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('originating_agency')
        ),
        'g': utils.reverse_force_list(
            value.get('other_restrictions')
        ),
        '6': value.get('linkage'),
        'c': utils.reverse_force_list(
            value.get('authorized_recipients_of_material')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('originator_control_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('362', '^dates_of_publication_and_or_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Reverse - Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"Formatted style": "0", "Unformatted note": "1"}
    field_map = {
        'linkage': '6',
        'source_of_information': 'z',
        'field_link_and_sequence_number': '8',
        'dates_of_publication_and_or_sequential_designation': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['format_of_date', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'z': value.get('source_of_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        '$ind1': indicator_map1.get(value.get('format_of_date'), value.get('format_of_date', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('363', '^normalized_date_and_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_normalized_date_and_sequential_designation(self, key, value):
    """Reverse - Normalized Date and Sequential Designation."""
    indicator_map1 = {"Ending information": "1", "No information provided": "_", "Starting information": "0"}
    indicator_map2 = {"Closed": "0", "Not specified": "_", "Open": "1"}
    field_map = {
        'nonpublic_note': 'x',
        'first_level_textual_designation': 'u',
        'fourth_level_of_chronology': 'l',
        'alternative_numbering_scheme_first_level_of_enumeration': 'g',
        'fifth_level_of_enumeration': 'e',
        'sixth_level_of_enumeration': 'f',
        'field_link_and_sequence_number': '8',
        'first_level_of_enumeration': 'a',
        'first_level_of_chronology': 'i',
        'alternative_numbering_scheme_second_level_of_enumeration': 'h',
        'second_level_of_enumeration': 'b',
        'third_level_of_enumeration': 'c',
        'public_note': 'z',
        'second_level_of_chronology': 'j',
        'linkage': '6',
        'fourth_level_of_enumeration': 'd',
        'third_level_of_chronology': 'k',
        'first_level_of_chronology_issuance': 'v',
        'alternative_numbering_scheme_chronology': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['start_end_designator', 'state_of_issuance'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'u': value.get('first_level_textual_designation'),
        'l': value.get('fourth_level_of_chronology'),
        'g': value.get('alternative_numbering_scheme_first_level_of_enumeration'),
        'e': value.get('fifth_level_of_enumeration'),
        'f': value.get('sixth_level_of_enumeration'),
        '8': value.get('field_link_and_sequence_number'),
        'a': value.get('first_level_of_enumeration'),
        'i': value.get('first_level_of_chronology'),
        'h': value.get('alternative_numbering_scheme_second_level_of_enumeration'),
        'b': value.get('second_level_of_enumeration'),
        'c': value.get('third_level_of_enumeration'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'j': value.get('second_level_of_chronology'),
        '6': value.get('linkage'),
        'd': value.get('fourth_level_of_enumeration'),
        'k': value.get('third_level_of_chronology'),
        'v': value.get('first_level_of_chronology_issuance'),
        'm': value.get('alternative_numbering_scheme_chronology'),
        '$ind1': indicator_map1.get(value.get('start_end_designator'), value.get('start_end_designator', '_')),
        '$ind2': indicator_map2.get(value.get('state_of_issuance'), value.get('state_of_issuance', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('365', '^trade_price$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_price(self, key, value):
    """Reverse - Trade Price."""
    field_map = {
        'price_effective_until': 'g',
        'currency_code': 'c',
        'price_effective_from': 'f',
        'field_link_and_sequence_number': '8',
        'price_type_code': 'a',
        'tax_rate_2': 'i',
        'tax_rate_1': 'h',
        'price_amount': 'b',
        'price_note': 'e',
        'iso_country_code': 'j',
        'linkage': '6',
        'source_of_price_type_code': '2',
        'unit_of_pricing': 'd',
        'marc_country_code': 'k',
        'identification_of_pricing_entity': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': value.get('price_effective_until'),
        'c': value.get('currency_code'),
        'f': value.get('price_effective_from'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('price_type_code'),
        'i': value.get('tax_rate_2'),
        'h': value.get('tax_rate_1'),
        'b': value.get('price_amount'),
        'e': value.get('price_note'),
        'j': value.get('iso_country_code'),
        '6': value.get('linkage'),
        '2': value.get('source_of_price_type_code'),
        'd': value.get('unit_of_pricing'),
        'k': value.get('marc_country_code'),
        'm': value.get('identification_of_pricing_entity'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('366', '^trade_availability_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_availability_information(self, key, value):
    """Reverse - Trade Availability Information."""
    field_map = {
        'date_made_out_of_print': 'g',
        'availability_status_code': 'c',
        'publisher_s_discount_category': 'f',
        'field_link_and_sequence_number': '8',
        'publishers_compressed_title_identification': 'a',
        'detailed_date_of_publication': 'b',
        'note': 'e',
        'iso_country_code': 'j',
        'linkage': '6',
        'source_of_availability_status_code': '2',
        'expected_next_availability_date': 'd',
        'marc_country_code': 'k',
        'identification_of_agency': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'g': value.get('date_made_out_of_print'),
        'c': value.get('availability_status_code'),
        'f': value.get('publisher_s_discount_category'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('publishers_compressed_title_identification'),
        'b': value.get('detailed_date_of_publication'),
        'e': value.get('note'),
        'j': value.get('iso_country_code'),
        '6': value.get('linkage'),
        '2': value.get('source_of_availability_status_code'),
        'd': value.get('expected_next_availability_date'),
        'k': value.get('marc_country_code'),
        'm': value.get('identification_of_agency'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('370', '^associated_place$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_place(self, key, value):
    """Reverse - Associated Place."""
    field_map = {
        'source_of_information': 'v',
        'other_associated_place': 'f',
        'associated_country': 'c',
        'start_period': 's',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'place_of_origin_of_work': 'g',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'end_period': 't',
        'uniform_resource_identifier': 'u',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        's': value.get('start_period'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('end_period'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    indicator_map2 = {"MARC language code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'language_code': 'a',
        'language_term': 'l',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source') and
        field_map.get('source_of_code') in order
        else indicator_map2.get(value.get('source_of_code'), value.get('source_of_code', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('380', '^form_of_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    field_map = {
        'linkage': '6',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'form_of_work': 'a',
        'record_control_number': '0',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'record_control_number': '0',
        'linkage': '6',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'other_distinguishing_characteristic': 'a',
        'source_of_information': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {"Medium of performance": "0", "No information provided": "_", "Partial medium of performance": "1"}
    indicator_map2 = {"Intended for access": "1", "No information provided": "_", "Not intended for access": "0"}
    field_map = {
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'number_of_ensembles_of_the_same_type': 'e',
        'field_link_and_sequence_number': '8',
        'medium_of_performance': 'a',
        'total_number_of_ensembles': 't',
        'soloist': 'b',
        'note': 'v',
        'total_number_of_performers': 's',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'number_of_performers_of_the_same_medium': 'n',
        'source_of_term': '2',
        'doubling_instrument': 'd',
        'alternative_medium_of_performance': 'p',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'access_control'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        't': value.get('total_number_of_ensembles'),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        's': value.get('total_number_of_performers'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        '2': value.get('source_of_term'),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
        '$ind2': indicator_map2.get(value.get('access_control'), value.get('access_control', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('383', '^numeric_designation_of_musical_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    field_map = {
        'opus_number': 'b',
        'thematic_index_code': 'd',
        'thematic_index_number': 'c',
        'publisher_associated_with_opus_number': 'e',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'serial_number': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        'd': value.get('thematic_index_code'),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        'e': value.get('publisher_associated_with_opus_number'),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    indicator_map1 = {"Original key": "0", "Relationship to original unknown": "_", "Transposed key": "1"}
    field_map = {
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'key': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['key_type', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('key'),
        '$ind1': indicator_map1.get(value.get('key_type'), value.get('key_type', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'audience_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'demographic_group_code': 'n',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'audience_term': 'a',
        'demographic_group_term': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'n': value.get('demographic_group_code'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        'm': value.get('demographic_group_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('386', '^creator_contributor_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    field_map = {
        'creator_contributor_code': 'b',
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'demographic_group_code': 'n',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'creator_contributor_term': 'a',
        'demographic_group_term': 'm',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        'n': value.get('demographic_group_code'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        'm': value.get('demographic_group_term'),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    indicator_map1 = {"Creation of aggregate work": "2", "Creation of work": "1", "No information provided": "_"}
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'time_period_of_creation_term': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period', 'None'])

    if not value.get('$ind2') and '$ind2' in order:
        order.remove('$ind2')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), value.get('type_of_time_period', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
