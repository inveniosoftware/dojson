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
        'type_of_unit': 'f',
        'accompanying_material': 'e',
        'dimensions': 'c',
        'extent': 'a',
        'linkage': '6',
        'size_of_unit': 'g',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'other_physical_details': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'f': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'e': value.get('accompanying_material'),
        'c': utils.reverse_force_list(
            value.get('dimensions')
        ),
        'a': utils.reverse_force_list(
            value.get('extent')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('size_of_unit')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': value.get('other_physical_details'),
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
        'field_link_and_sequence_number': '8',
        'additional_information': 'b',
        'hours': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('additional_information'),
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
        'field_link_and_sequence_number': '8',
        'date_of_current_publication_frequency': 'b',
        'current_publication_frequency': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('date_of_current_publication_frequency'),
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
        'field_link_and_sequence_number': '8',
        'dates_of_former_publication_frequency': 'b',
        'former_publication_frequency': 'a',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('dates_of_former_publication_frequency'),
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
        'authority_record_control_number_or_standard_number': '0',
        'content_type_term': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'content_type_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('content_type_code')
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
        'authority_record_control_number_or_standard_number': '0',
        'media_type_term': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'media_type_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('media_type_term')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('media_type_code')
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
        'authority_record_control_number_or_standard_number': '0',
        'carrier_type_term': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'carrier_type_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('carrier_type_term')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('carrier_type_code')
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
        'support': 'e',
        'information_recording_technique': 'd',
        'polarity': 'o',
        'material_base_and_configuration': 'a',
        'source': '2',
        'font_size': 'n',
        'layout': 'k',
        'field_link_and_sequence_number': '8',
        'materials_applied_to_surface': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'production_rate_ratio': 'f',
        'book_format': 'm',
        'generation': 'j',
        'location_within_medium': 'h',
        'linkage': '6',
        'technical_specifications_of_medium': 'i',
        'materials_specified': '3',
        'dimensions': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': utils.reverse_force_list(
            value.get('support')
        ),
        'd': utils.reverse_force_list(
            value.get('information_recording_technique')
        ),
        'o': utils.reverse_force_list(
            value.get('polarity')
        ),
        'a': utils.reverse_force_list(
            value.get('material_base_and_configuration')
        ),
        '2': value.get('source'),
        'n': utils.reverse_force_list(
            value.get('font_size')
        ),
        'k': utils.reverse_force_list(
            value.get('layout')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('materials_applied_to_surface')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': utils.reverse_force_list(
            value.get('production_rate_ratio')
        ),
        'm': utils.reverse_force_list(
            value.get('book_format')
        ),
        'j': utils.reverse_force_list(
            value.get('generation')
        ),
        'h': utils.reverse_force_list(
            value.get('location_within_medium')
        ),
        '6': value.get('linkage'),
        'i': utils.reverse_force_list(
            value.get('technical_specifications_of_medium')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('dimensions')
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
        'local_planar_local_or_other_projection_or_grid_description': 'v',
        'longitude_resolution': 'd',
        'name': 'a',
        'scale_factor': 'k',
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': 'n',
        'false_northing': 'j',
        'semi_major_axis': 'r',
        'latitude_resolution': 'c',
        'false_easting': 'i',
        'oblique_line_longitude': 'f',
        'vertical_encoding_method': 'u',
        'ellipsoid_name': 'q',
        'local_planar_or_local_georeference_information': 'w',
        'linkage': '6',
        'coordinate_units_or_distance_units': 'b',
        'landsat_number_and_path_number': 'o',
        'standard_parallel_or_oblique_line_latitude': 'e',
        'height_of_perspective_point_above_surface': 'l',
        'reference_method_used': '2',
        'field_link_and_sequence_number': '8',
        'azimuthal_angle': 'm',
        'latitude_of_projection_center_or_projection_origin': 'h',
        'denominator_of_flattening_ratio': 's',
        'longitude_of_central_meridian_or_projection_center': 'g',
        'zone_identifier': 'p',
        'vertical_resolution': 't',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['geospatial_reference_dimension', 'geospatial_reference_method'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': value.get('local_planar_local_or_other_projection_or_grid_description'),
        'd': value.get('longitude_resolution'),
        'a': value.get('name'),
        'k': value.get('scale_factor'),
        'n': value.get('azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole'),
        'j': value.get('false_northing'),
        'r': value.get('semi_major_axis'),
        'c': value.get('latitude_resolution'),
        'i': value.get('false_easting'),
        'f': utils.reverse_force_list(
            value.get('oblique_line_longitude')
        ),
        'u': value.get('vertical_encoding_method'),
        'q': value.get('ellipsoid_name'),
        'w': value.get('local_planar_or_local_georeference_information'),
        '6': value.get('linkage'),
        'b': value.get('coordinate_units_or_distance_units'),
        'o': value.get('landsat_number_and_path_number'),
        'e': utils.reverse_force_list(
            value.get('standard_parallel_or_oblique_line_latitude')
        ),
        'l': value.get('height_of_perspective_point_above_surface'),
        '2': value.get('reference_method_used'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('azimuthal_angle'),
        'h': value.get('latitude_of_projection_center_or_projection_origin'),
        's': value.get('denominator_of_flattening_ratio'),
        'g': value.get('longitude_of_central_meridian_or_projection_center'),
        'p': value.get('zone_identifier'),
        't': value.get('vertical_resolution'),
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
        'bearing_reference_meridian': 'i',
        'bearing_resolution': 'f',
        'distance_resolution': 'e',
        'ordinate_resolution': 'd',
        'planar_distance_units': 'b',
        'planar_coordinate_encoding_method': 'a',
        'bearing_reference_direction': 'h',
        'linkage': '6',
        'bearing_units': 'g',
        'field_link_and_sequence_number': '8',
        'abscissa_resolution': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'i': value.get('bearing_reference_meridian'),
        'f': value.get('bearing_resolution'),
        'e': value.get('distance_resolution'),
        'd': value.get('ordinate_resolution'),
        'b': value.get('planar_distance_units'),
        'a': value.get('planar_coordinate_encoding_method'),
        'h': value.get('bearing_reference_direction'),
        '6': value.get('linkage'),
        'g': value.get('bearing_units'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('abscissa_resolution'),
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
        'track_configuration': 'e',
        'groove_characteristic': 'd',
        'type_of_recording': 'a',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'playing_speed': 'c',
        'authority_record_control_number_or_standard_number': '0',
        'tape_configuration': 'f',
        'special_playback_characteristics': 'h',
        'linkage': '6',
        'configuration_of_playback_channels': 'g',
        'materials_specified': '3',
        'recording_medium': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': utils.reverse_force_list(
            value.get('track_configuration')
        ),
        'd': utils.reverse_force_list(
            value.get('groove_characteristic')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_recording')
        ),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('playing_speed')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': utils.reverse_force_list(
            value.get('tape_configuration')
        ),
        'h': utils.reverse_force_list(
            value.get('special_playback_characteristics')
        ),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('configuration_of_playback_channels')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('recording_medium')
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
        'authority_record_control_number_or_standard_number': '0',
        'presentation_format': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'projection_speed': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('projection_speed')
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
        'authority_record_control_number_or_standard_number': '0',
        'video_format': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'broadcast_standard': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('video_format')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('broadcast_standard')
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
        'authority_record_control_number_or_standard_number': '0',
        'encoded_bitrate': 'f',
        'regional_encoding': 'e',
        'resolution': 'd',
        'file_size': 'c',
        'file_type': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'encoding_format': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': utils.reverse_force_list(
            value.get('encoded_bitrate')
        ),
        'e': utils.reverse_force_list(
            value.get('regional_encoding')
        ),
        'd': utils.reverse_force_list(
            value.get('resolution')
        ),
        'c': utils.reverse_force_list(
            value.get('file_size')
        ),
        'a': utils.reverse_force_list(
            value.get('file_type')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('encoding_format')
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
        'authority_record_control_number_or_standard_number': '0',
        'format_of_notated_music_term': 'a',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'format_of_notated_music_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
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
        'hierarchical_level': 'c',
        'organization': 'a',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'arrangement': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('hierarchical_level'),
        'a': utils.reverse_force_list(
            value.get('organization')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('arrangement')
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
        'indirect_reference_description': 'i',
        'vertical_count': 'f',
        'column_count': 'e',
        'row_count': 'd',
        'object_type': 'b',
        'direct_reference_method': 'a',
        'format_of_the_digital_image': 'q',
        'linkage': '6',
        'vpf_topology_level': 'g',
        'field_link_and_sequence_number': '8',
        'object_count': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'i': value.get('indirect_reference_description'),
        'f': value.get('vertical_count'),
        'e': value.get('column_count'),
        'd': value.get('row_count'),
        'b': utils.reverse_force_list(
            value.get('object_type')
        ),
        'a': value.get('direct_reference_method'),
        'q': value.get('format_of_the_digital_image'),
        '6': value.get('linkage'),
        'g': value.get('vpf_topology_level'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('object_count')
        ),
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
        'country_of_origin_code': 'f',
        'classification_system': 'e',
        'downgrading_or_declassification_event': 'd',
        'handling_instructions': 'b',
        'security_classification': 'a',
        'authorization': 'j',
        'declassification_date': 'h',
        'linkage': '6',
        'downgrading_date': 'g',
        'field_link_and_sequence_number': '8',
        'external_dissemination_information': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['controlled_element', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'f': value.get('country_of_origin_code'),
        'e': value.get('classification_system'),
        'd': value.get('downgrading_or_declassification_event'),
        'b': utils.reverse_force_list(
            value.get('handling_instructions')
        ),
        'a': value.get('security_classification'),
        'j': utils.reverse_force_list(
            value.get('authorization')
        ),
        'h': value.get('declassification_date'),
        '6': value.get('linkage'),
        'g': value.get('downgrading_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('external_dissemination_information')
        ),
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
        'originator_control_term': 'a',
        'linkage': '6',
        'other_restrictions': 'g',
        'field_link_and_sequence_number': '8',
        'authorized_recipients_of_material': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('originating_agency')
        ),
        'a': value.get('originator_control_term'),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('other_restrictions')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': utils.reverse_force_list(
            value.get('authorized_recipients_of_material')
        ),
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
        'field_link_and_sequence_number': '8',
        'dates_of_publication_and_or_sequential_designation': 'a',
        'source_of_information': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['format_of_date', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        'z': value.get('source_of_information'),
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
        'first_level_of_chronology_issuance': 'v',
        'fifth_level_of_enumeration': 'e',
        'fourth_level_of_enumeration': 'd',
        'fourth_level_of_chronology': 'l',
        'first_level_of_enumeration': 'a',
        'third_level_of_chronology': 'k',
        'nonpublic_note': 'x',
        'public_note': 'z',
        'field_link_and_sequence_number': '8',
        'third_level_of_enumeration': 'c',
        'first_level_of_chronology': 'i',
        'sixth_level_of_enumeration': 'f',
        'first_level_textual_designation': 'u',
        'alternative_numbering_scheme_chronology': 'm',
        'second_level_of_chronology': 'j',
        'alternative_numbering_scheme_second_level_of_enumeration': 'h',
        'linkage': '6',
        'alternative_numbering_scheme_first_level_of_enumeration': 'g',
        'second_level_of_enumeration': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['start_end_designator', 'state_of_issuance'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': value.get('first_level_of_chronology_issuance'),
        'e': value.get('fifth_level_of_enumeration'),
        'd': value.get('fourth_level_of_enumeration'),
        'l': value.get('fourth_level_of_chronology'),
        'a': value.get('first_level_of_enumeration'),
        'k': value.get('third_level_of_chronology'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        '8': value.get('field_link_and_sequence_number'),
        'c': value.get('third_level_of_enumeration'),
        'i': value.get('first_level_of_chronology'),
        'f': value.get('sixth_level_of_enumeration'),
        'u': value.get('first_level_textual_designation'),
        'm': value.get('alternative_numbering_scheme_chronology'),
        'j': value.get('second_level_of_chronology'),
        'h': value.get('alternative_numbering_scheme_second_level_of_enumeration'),
        '6': value.get('linkage'),
        'g': value.get('alternative_numbering_scheme_first_level_of_enumeration'),
        'b': value.get('second_level_of_enumeration'),
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
        'price_note': 'e',
        'unit_of_pricing': 'd',
        'price_type_code': 'a',
        'source_of_price_type_code': '2',
        'marc_country_code': 'k',
        'field_link_and_sequence_number': '8',
        'currency_code': 'c',
        'tax_rate_2': 'i',
        'price_effective_from': 'f',
        'identification_of_pricing_entity': 'm',
        'iso_country_code': 'j',
        'tax_rate_1': 'h',
        'linkage': '6',
        'price_effective_until': 'g',
        'price_amount': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': value.get('price_note'),
        'd': value.get('unit_of_pricing'),
        'a': value.get('price_type_code'),
        '2': value.get('source_of_price_type_code'),
        'k': value.get('marc_country_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('currency_code'),
        'i': value.get('tax_rate_2'),
        'f': value.get('price_effective_from'),
        'm': value.get('identification_of_pricing_entity'),
        'j': value.get('iso_country_code'),
        'h': value.get('tax_rate_1'),
        '6': value.get('linkage'),
        'g': value.get('price_effective_until'),
        'b': value.get('price_amount'),
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
        'note': 'e',
        'expected_next_availability_date': 'd',
        'publishers_compressed_title_identification': 'a',
        'source_of_availability_status_code': '2',
        'marc_country_code': 'k',
        'field_link_and_sequence_number': '8',
        'availability_status_code': 'c',
        'publisher_s_discount_category': 'f',
        'identification_of_agency': 'm',
        'iso_country_code': 'j',
        'linkage': '6',
        'date_made_out_of_print': 'g',
        'detailed_date_of_publication': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': value.get('note'),
        'd': value.get('expected_next_availability_date'),
        'a': value.get('publishers_compressed_title_identification'),
        '2': value.get('source_of_availability_status_code'),
        'k': value.get('marc_country_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'c': value.get('availability_status_code'),
        'f': value.get('publisher_s_discount_category'),
        'm': value.get('identification_of_agency'),
        'j': value.get('iso_country_code'),
        '6': value.get('linkage'),
        'g': value.get('date_made_out_of_print'),
        'b': value.get('detailed_date_of_publication'),
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
        'authority_record_control_number_or_standard_number': '0',
        'other_associated_place': 'f',
        'uniform_resource_identifier': 'u',
        'end_period': 't',
        'source_of_term': '2',
        'linkage': '6',
        'place_of_origin_of_work': 'g',
        'field_link_and_sequence_number': '8',
        'start_period': 's',
        'associated_country': 'c',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': value.get('end_period'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        's': value.get('start_period'),
        'c': utils.reverse_force_list(
            value.get('associated_country')
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
        'field_link_and_sequence_number': '8',
        'language_term': 'l',
        'language_code': 'a',
        'source': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'source_of_code'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        '2': value.get('source'),
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
        'record_control_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'form_of_work': 'a',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '2': value.get('source_of_term'),
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
        'source_of_information': 'v',
        'record_control_number': '0',
        'uniform_resource_identifier': 'u',
        'other_distinguishing_characteristic': 'a',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
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
        'note': 'v',
        'number_of_ensembles_of_the_same_type': 'e',
        'doubling_instrument': 'd',
        'medium_of_performance': 'a',
        'source_of_term': '2',
        'number_of_performers_of_the_same_medium': 'n',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'total_number_of_ensembles': 't',
        'linkage': '6',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'alternative_medium_of_performance': 'p',
        'total_number_of_performers': 's',
        'soloist': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['display_constant_controller', 'access_control'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        '2': value.get('source_of_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        't': value.get('total_number_of_ensembles'),
        '6': value.get('linkage'),
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        's': value.get('total_number_of_performers'),
        'b': utils.reverse_force_list(
            value.get('soloist')
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
        'publisher_associated_with_opus_number': 'e',
        'thematic_index_code': 'd',
        'thematic_index_number': 'c',
        'serial_number': 'a',
        'source': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'opus_number': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'e': value.get('publisher_associated_with_opus_number'),
        'd': value.get('thematic_index_code'),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        '2': value.get('source'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('opus_number')
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
        'authority_record_control_number_or_standard_number': '0',
        'demographic_group_term': 'm',
        'audience_term': 'a',
        'source': '2',
        'demographic_group_code': 'n',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'audience_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': value.get('demographic_group_term'),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        '2': value.get('source'),
        'n': value.get('demographic_group_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
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
        'authority_record_control_number_or_standard_number': '0',
        'demographic_group_term': 'm',
        'creator_contributor_term': 'a',
        'source': '2',
        'demographic_group_code': 'n',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
        'creator_contributor_code': 'b',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': value.get('demographic_group_term'),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        '2': value.get('source'),
        'n': value.get('demographic_group_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
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
        'authority_record_control_number_or_standard_number': '0',
        'time_period_of_creation_term': 'a',
        'source_of_term': '2',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'materials_specified': '3',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_time_period', 'None'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), value.get('type_of_time_period', '_')),
        '$ind2': value.get('$ind2', '_'),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
