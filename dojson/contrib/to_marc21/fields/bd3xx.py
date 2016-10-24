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

from ..model import to_marc21


@to_marc21.over('300', '^physical_description$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_description(self, key, value):
    """Reverse - Physical Description."""
    field_map = {
        'materials_specified': '3',
        'linkage': '6',
        'extent': 'a',
        'other_physical_details': 'b',
        'dimensions': 'c',
        'size_of_unit': 'g',
        'field_link_and_sequence_number': '8',
        'type_of_unit': 'f',
        'accompanying_material': 'e',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('extent')
        ),
        'b': value.get('other_physical_details'),
        'c': utils.reverse_force_list(
            value.get('dimensions')
        ),
        'g': utils.reverse_force_list(
            value.get('size_of_unit')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'e': value.get('accompanying_material'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('306', '^playing_time$')
@utils.filter_values
def reverse_playing_time(self, key, value):
    """Reverse - Playing Time."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'playing_time': 'a',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('playing_time')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('307', '^hours$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_hours(self, key, value):
    """Reverse - Hours, Etc.."""
    indicator_map1 = {"Hours": "_", "No display constant generated": "8"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'hours': 'a',
        'additional_information': 'b',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('hours'),
        'b': value.get('additional_information'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('310', '^current_publication_frequency$')
@utils.filter_values
def reverse_current_publication_frequency(self, key, value):
    """Reverse - Current Publication Frequency."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'current_publication_frequency': 'a',
        'date_of_current_publication_frequency': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('current_publication_frequency'),
        'b': value.get('date_of_current_publication_frequency'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('321', '^former_publication_frequency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_publication_frequency(self, key, value):
    """Reverse - Former Publication Frequency."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'former_publication_frequency': 'a',
        'dates_of_former_publication_frequency': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('former_publication_frequency'),
        'b': value.get('dates_of_former_publication_frequency'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'content_type_term': 'a',
        'content_type_code': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('337', '^media_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_media_type(self, key, value):
    """Reverse - Media Type."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'media_type_term': 'a',
        'media_type_code': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('media_type_term')
        ),
        'b': utils.reverse_force_list(
            value.get('media_type_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('338', '^carrier_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_carrier_type(self, key, value):
    """Reverse - Carrier Type."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'carrier_type_term': 'a',
        'carrier_type_code': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('carrier_type_term')
        ),
        'b': utils.reverse_force_list(
            value.get('carrier_type_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('340', '^physical_medium$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_medium(self, key, value):
    """Reverse - Physical Medium."""
    field_map = {
        'materials_specified': '3',
        'generation': 'j',
        'authority_record_control_number_or_standard_number': '0',
        'material_base_and_configuration': 'a',
        'dimensions': 'b',
        'materials_applied_to_surface': 'c',
        'book_format': 'm',
        'technical_specifications_of_medium': 'i',
        'production_rate_ratio': 'f',
        'information_recording_technique': 'd',
        'support': 'e',
        'linkage': '6',
        'polarity': 'o',
        'source': '2',
        'font_size': 'n',
        'field_link_and_sequence_number': '8',
        'layout': 'k',
        'location_within_medium': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        'j': utils.reverse_force_list(
            value.get('generation')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('material_base_and_configuration')
        ),
        'b': utils.reverse_force_list(
            value.get('dimensions')
        ),
        'c': utils.reverse_force_list(
            value.get('materials_applied_to_surface')
        ),
        'm': utils.reverse_force_list(
            value.get('book_format')
        ),
        'i': utils.reverse_force_list(
            value.get('technical_specifications_of_medium')
        ),
        'f': utils.reverse_force_list(
            value.get('production_rate_ratio')
        ),
        'd': utils.reverse_force_list(
            value.get('information_recording_technique')
        ),
        'e': utils.reverse_force_list(
            value.get('support')
        ),
        '6': value.get('linkage'),
        'o': utils.reverse_force_list(
            value.get('polarity')
        ),
        '2': value.get('source'),
        'n': utils.reverse_force_list(
            value.get('font_size')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'k': utils.reverse_force_list(
            value.get('layout')
        ),
        'h': utils.reverse_force_list(
            value.get('location_within_medium')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('342', '^geospatial_reference_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geospatial_reference_data(self, key, value):
    """Reverse - Geospatial Reference Data."""
    indicator_map1 = {
        "Horizontal coordinate system": "0",
        "Vertical coordinate system": "1"}
    indicator_map2 = {
        "Altitude": "6",
        "Depth": "8",
        "Geodetic model": "5",
        "Geographic": "0",
        "Grid coordinate system": "2",
        "Local": "4",
        "Local planar": "3",
        "Map projection": "1",
        "Method specified in $2": "7"}
    field_map = {
        'false_northing': 'j',
        'name': 'a',
        'zone_identifier': 'p',
        'standard_parallel_or_oblique_line_latitude': 'e',
        'oblique_line_longitude': 'f',
        'scale_factor': 'k',
        'landsat_number_and_path_number': 'o',
        'reference_method_used': '2',
        'ellipsoid_name': 'q',
        'denominator_of_flattening_ratio': 's',
        'longitude_of_central_meridian_or_projection_center': 'g',
        'height_of_perspective_point_above_surface': 'l',
        'local_planar_or_local_georeference_information': 'w',
        'azimuthal_angle': 'm',
        'linkage': '6',
        'coordinate_units_or_distance_units': 'b',
        'latitude_resolution': 'c',
        'longitude_resolution': 'd',
        'false_easting': 'i',
        'vertical_resolution': 't',
        'semi_major_axis': 'r',
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': 'n',
        'field_link_and_sequence_number': '8',
        'vertical_encoding_method': 'u',
        'local_planar_local_or_other_projection_or_grid_description': 'v',
        'latitude_of_projection_center_or_projection_origin': 'h',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('geospatial_reference_dimension'), '7') != '7':
        try:
            order.remove(field_map.get('geospatial_reference_dimension'))
        except ValueError:
            pass

    if indicator_map2.get(
            value.get('geospatial_reference_method'), '7') != '7':
        try:
            order.remove(field_map.get('geospatial_reference_method'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('false_northing'),
        'a': value.get('name'),
        'p': value.get('zone_identifier'),
        'e': utils.reverse_force_list(
            value.get('standard_parallel_or_oblique_line_latitude')
        ),
        'f': utils.reverse_force_list(
            value.get('oblique_line_longitude')
        ),
        'k': value.get('scale_factor'),
        'o': value.get('landsat_number_and_path_number'),
        '2': value.get('reference_method_used'),
        'q': value.get('ellipsoid_name'),
        's': value.get('denominator_of_flattening_ratio'),
        'g': value.get('longitude_of_central_meridian_or_projection_center'),
        'l': value.get('height_of_perspective_point_above_surface'),
        'w': value.get('local_planar_or_local_georeference_information'),
        'm': value.get('azimuthal_angle'),
        '6': value.get('linkage'),
        'b': value.get('coordinate_units_or_distance_units'),
        'c': value.get('latitude_resolution'),
        'd': value.get('longitude_resolution'),
        'i': value.get('false_easting'),
        't': value.get('vertical_resolution'),
        'r': value.get('semi_major_axis'),
        'n': value.get('azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': value.get('vertical_encoding_method'),
        'v': value.get('local_planar_local_or_other_projection_or_grid_description'),
        'h': value.get('latitude_of_projection_center_or_projection_origin'),
        '$ind1': indicator_map1.get(value.get('geospatial_reference_dimension'), '_'),
        '$ind2': indicator_map2.get(value.get('geospatial_reference_method'), '_'),
    }


@to_marc21.over('343', '^planar_coordinate_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_planar_coordinate_data(self, key, value):
    """Reverse - Planar Coordinate Data."""
    field_map = {
        'bearing_reference_meridian': 'i',
        'linkage': '6',
        'planar_coordinate_encoding_method': 'a',
        'planar_distance_units': 'b',
        'abscissa_resolution': 'c',
        'bearing_units': 'g',
        'field_link_and_sequence_number': '8',
        'bearing_resolution': 'f',
        'ordinate_resolution': 'd',
        'distance_resolution': 'e',
        'bearing_reference_direction': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'i': value.get('bearing_reference_meridian'),
        '6': value.get('linkage'),
        'a': value.get('planar_coordinate_encoding_method'),
        'b': value.get('planar_distance_units'),
        'c': value.get('abscissa_resolution'),
        'g': value.get('bearing_units'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('bearing_resolution'),
        'd': value.get('ordinate_resolution'),
        'e': value.get('distance_resolution'),
        'h': value.get('bearing_reference_direction'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('344', '^sound_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_sound_characteristics(self, key, value):
    """Reverse - Sound Characteristics."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'type_of_recording': 'a',
        'recording_medium': 'b',
        'playing_speed': 'c',
        'tape_configuration': 'f',
        'groove_characteristic': 'd',
        'track_configuration': 'e',
        'linkage': '6',
        'source': '2',
        'configuration_of_playback_channels': 'g',
        'field_link_and_sequence_number': '8',
        'special_playback_characteristics': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_recording')
        ),
        'b': utils.reverse_force_list(
            value.get('recording_medium')
        ),
        'c': utils.reverse_force_list(
            value.get('playing_speed')
        ),
        'f': utils.reverse_force_list(
            value.get('tape_configuration')
        ),
        'd': utils.reverse_force_list(
            value.get('groove_characteristic')
        ),
        'e': utils.reverse_force_list(
            value.get('track_configuration')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        'g': utils.reverse_force_list(
            value.get('configuration_of_playback_channels')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'h': utils.reverse_force_list(
            value.get('special_playback_characteristics')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('345', '^projection_characteristics_of_moving_image$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_projection_characteristics_of_moving_image(self, key, value):
    """Reverse - Projection Characteristics of Moving Image."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'presentation_format': 'a',
        'projection_speed': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        'b': utils.reverse_force_list(
            value.get('projection_speed')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('346', '^video_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_video_characteristics(self, key, value):
    """Reverse - Video Characteristics."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'video_format': 'a',
        'broadcast_standard': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('video_format')
        ),
        'b': utils.reverse_force_list(
            value.get('broadcast_standard')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('347', '^digital_file_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_file_characteristics(self, key, value):
    """Reverse - Digital File Characteristics."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'file_type': 'a',
        'encoding_format': 'b',
        'file_size': 'c',
        'field_link_and_sequence_number': '8',
        'encoded_bitrate': 'f',
        'resolution': 'd',
        'regional_encoding': 'e',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('file_type')
        ),
        'b': utils.reverse_force_list(
            value.get('encoding_format')
        ),
        'c': utils.reverse_force_list(
            value.get('file_size')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('encoded_bitrate')
        ),
        'd': utils.reverse_force_list(
            value.get('resolution')
        ),
        'e': utils.reverse_force_list(
            value.get('regional_encoding')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('348', '^format_of_notated_music$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_format_of_notated_music(self, key, value):
    """Reverse - Format of Notated Music."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'format_of_notated_music_term': 'a',
        'format_of_notated_music_code': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('351', '^organization_and_arrangement_of_materials$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_organization_and_arrangement_of_materials(self, key, value):
    """Reverse - Organization and Arrangement of Materials."""
    field_map = {
        'materials_specified': '3',
        'linkage': '6',
        'organization': 'a',
        'arrangement': 'b',
        'hierarchical_level': 'c',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('organization')
        ),
        'b': utils.reverse_force_list(
            value.get('arrangement')
        ),
        'c': value.get('hierarchical_level'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('352', '^digital_graphic_representation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_graphic_representation(self, key, value):
    """Reverse - Digital Graphic Representation."""
    field_map = {
        'format_of_the_digital_image': 'q',
        'linkage': '6',
        'direct_reference_method': 'a',
        'object_type': 'b',
        'object_count': 'c',
        'vpf_topology_level': 'g',
        'field_link_and_sequence_number': '8',
        'vertical_count': 'f',
        'row_count': 'd',
        'column_count': 'e',
        'indirect_reference_description': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'q': value.get('format_of_the_digital_image'),
        '6': value.get('linkage'),
        'a': value.get('direct_reference_method'),
        'b': utils.reverse_force_list(
            value.get('object_type')
        ),
        'c': utils.reverse_force_list(
            value.get('object_count')
        ),
        'g': value.get('vpf_topology_level'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('vertical_count'),
        'd': value.get('row_count'),
        'e': value.get('column_count'),
        'i': value.get('indirect_reference_description'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('355', '^security_classification_control$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_security_classification_control(self, key, value):
    """Reverse - Security Classification Control."""
    indicator_map1 = {
        "Abstract": "2",
        "Author": "4",
        "Contents note": "3",
        "Document": "0",
        "None of the above": "8",
        "Record": "5",
        "Title": "1"}
    field_map = {
        'authorization': 'j',
        'linkage': '6',
        'security_classification': 'a',
        'handling_instructions': 'b',
        'external_dissemination_information': 'c',
        'downgrading_date': 'g',
        'field_link_and_sequence_number': '8',
        'country_of_origin_code': 'f',
        'downgrading_or_declassification_event': 'd',
        'classification_system': 'e',
        'declassification_date': 'h',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('controlled_element'), '7') != '7':
        try:
            order.remove(field_map.get('controlled_element'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': utils.reverse_force_list(
            value.get('authorization')
        ),
        '6': value.get('linkage'),
        'a': value.get('security_classification'),
        'b': utils.reverse_force_list(
            value.get('handling_instructions')
        ),
        'c': utils.reverse_force_list(
            value.get('external_dissemination_information')
        ),
        'g': value.get('downgrading_date'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': value.get('country_of_origin_code'),
        'd': value.get('downgrading_or_declassification_event'),
        'e': value.get('classification_system'),
        'h': value.get('declassification_date'),
        '$ind1': indicator_map1.get(value.get('controlled_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('357', '^originator_dissemination_control$')
@utils.filter_values
def reverse_originator_dissemination_control(self, key, value):
    """Reverse - Originator Dissemination Control."""
    field_map = {
        'linkage': '6',
        'originator_control_term': 'a',
        'originating_agency': 'b',
        'authorized_recipients_of_material': 'c',
        'other_restrictions': 'g',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': value.get('originator_control_term'),
        'b': utils.reverse_force_list(
            value.get('originating_agency')
        ),
        'c': utils.reverse_force_list(
            value.get('authorized_recipients_of_material')
        ),
        'g': utils.reverse_force_list(
            value.get('other_restrictions')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('362', '^dates_of_publication_and_or_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dates_of_publication_and_or_sequential_designation(
        self, key, value):
    """Reverse - Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"Formatted style": "0", "Unformatted note": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'dates_of_publication_and_or_sequential_designation': 'a',
        'source_of_information': 'z',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('format_of_date'), '7') != '7':
        try:
            order.remove(field_map.get('format_of_date'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        'z': value.get('source_of_information'),
        '$ind1': indicator_map1.get(value.get('format_of_date'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('363', '^normalized_date_and_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_normalized_date_and_sequential_designation(self, key, value):
    """Reverse - Normalized Date and Sequential Designation."""
    indicator_map1 = {
        "Ending information": "1",
        "No information provided": "_",
        "Starting information": "0"}
    indicator_map2 = {"Closed": "0", "Not specified": "_", "Open": "1"}
    field_map = {
        'second_level_of_chronology': 'j',
        'linkage': '6',
        'first_level_of_enumeration': 'a',
        'second_level_of_enumeration': 'b',
        'third_level_of_enumeration': 'c',
        'fifth_level_of_enumeration': 'e',
        'sixth_level_of_enumeration': 'f',
        'fourth_level_of_enumeration': 'd',
        'first_level_of_chronology': 'i',
        'third_level_of_chronology': 'k',
        'nonpublic_note': 'x',
        'alternative_numbering_scheme_first_level_of_enumeration': 'g',
        'fourth_level_of_chronology': 'l',
        'field_link_and_sequence_number': '8',
        'alternative_numbering_scheme_chronology': 'm',
        'first_level_textual_designation': 'u',
        'public_note': 'z',
        'first_level_of_chronology_issuance': 'v',
        'alternative_numbering_scheme_second_level_of_enumeration': 'h',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('start_end_designator'), '7') != '7':
        try:
            order.remove(field_map.get('start_end_designator'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('state_of_issuance'), '7') != '7':
        try:
            order.remove(field_map.get('state_of_issuance'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('second_level_of_chronology'),
        '6': value.get('linkage'),
        'a': value.get('first_level_of_enumeration'),
        'b': value.get('second_level_of_enumeration'),
        'c': value.get('third_level_of_enumeration'),
        'e': value.get('fifth_level_of_enumeration'),
        'f': value.get('sixth_level_of_enumeration'),
        'd': value.get('fourth_level_of_enumeration'),
        'i': value.get('first_level_of_chronology'),
        'k': value.get('third_level_of_chronology'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'g': value.get('alternative_numbering_scheme_first_level_of_enumeration'),
        'l': value.get('fourth_level_of_chronology'),
        '8': value.get('field_link_and_sequence_number'),
        'm': value.get('alternative_numbering_scheme_chronology'),
        'u': value.get('first_level_textual_designation'),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'v': value.get('first_level_of_chronology_issuance'),
        'h': value.get('alternative_numbering_scheme_second_level_of_enumeration'),
        '$ind1': indicator_map1.get(value.get('start_end_designator'), '_'),
        '$ind2': indicator_map2.get(value.get('state_of_issuance'), '_'),
    }


@to_marc21.over('365', '^trade_price$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_price(self, key, value):
    """Reverse - Trade Price."""
    field_map = {
        'iso_country_code': 'j',
        'linkage': '6',
        'price_type_code': 'a',
        'price_amount': 'b',
        'currency_code': 'c',
        'tax_rate_2': 'i',
        'price_effective_from': 'f',
        'unit_of_pricing': 'd',
        'price_note': 'e',
        'marc_country_code': 'k',
        'source_of_price_type_code': '2',
        'price_effective_until': 'g',
        'field_link_and_sequence_number': '8',
        'identification_of_pricing_entity': 'm',
        'tax_rate_1': 'h',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('iso_country_code'),
        '6': value.get('linkage'),
        'a': value.get('price_type_code'),
        'b': value.get('price_amount'),
        'c': value.get('currency_code'),
        'i': value.get('tax_rate_2'),
        'f': value.get('price_effective_from'),
        'd': value.get('unit_of_pricing'),
        'e': value.get('price_note'),
        'k': value.get('marc_country_code'),
        '2': value.get('source_of_price_type_code'),
        'g': value.get('price_effective_until'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('identification_of_pricing_entity'),
        'h': value.get('tax_rate_1'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('366', '^trade_availability_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_availability_information(self, key, value):
    """Reverse - Trade Availability Information."""
    field_map = {
        'iso_country_code': 'j',
        'linkage': '6',
        'publishers_compressed_title_identification': 'a',
        'detailed_date_of_publication': 'b',
        'availability_status_code': 'c',
        'publisher_s_discount_category': 'f',
        'expected_next_availability_date': 'd',
        'note': 'e',
        'marc_country_code': 'k',
        'source_of_availability_status_code': '2',
        'date_made_out_of_print': 'g',
        'field_link_and_sequence_number': '8',
        'identification_of_agency': 'm',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('iso_country_code'),
        '6': value.get('linkage'),
        'a': value.get('publishers_compressed_title_identification'),
        'b': value.get('detailed_date_of_publication'),
        'c': value.get('availability_status_code'),
        'f': value.get('publisher_s_discount_category'),
        'd': value.get('expected_next_availability_date'),
        'e': value.get('note'),
        'k': value.get('marc_country_code'),
        '2': value.get('source_of_availability_status_code'),
        'g': value.get('date_made_out_of_print'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('identification_of_agency'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('370', '^associated_place$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_place(self, key, value):
    """Reverse - Associated Place."""
    field_map = {
        'uniform_resource_identifier': 'u',
        'authority_record_control_number_or_standard_number': '0',
        'start_period': 's',
        'associated_country': 'c',
        'place_of_origin_of_work': 'g',
        'field_link_and_sequence_number': '8',
        'other_associated_place': 'f',
        'end_period': 't',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        's': value.get('start_period'),
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        't': value.get('end_period'),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    indicator_map2 = {
        "MARC language code": "_",
        "Source specified in subfield $2": "7"}
    field_map = {
        'language_term': 'l',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'language_code': 'a',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map2.get(value.get('source_of_code'), '7') != '7':
        try:
            order.remove(field_map.get('source_of_code'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '7' if 'source_of_code' in value and
        not indicator_map2.get(value.get('source_of_code')) and
        value.get('source_of_code') == value.get('source')
        else indicator_map2.get(value.get('source_of_code'), '_'),
    }


@to_marc21.over('380', '^form_of_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    field_map = {
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'form_of_work': 'a',
        'linkage': '6',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over(
    '381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(
        self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'record_control_number': '0',
        'other_distinguishing_characteristic': 'a',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
        'linkage': '6',
        'source_of_information': 'v',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        '2': value.get('source_of_term'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {
        "Medium of performance": "0",
        "No information provided": "_",
        "Partial medium of performance": "1"}
    indicator_map2 = {
        "Intended for access": "1",
        "No information provided": "_",
        "Not intended for access": "0"}
    field_map = {
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance': 'a',
        'soloist': 'b',
        'total_number_of_performers': 's',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'doubling_instrument': 'd',
        'number_of_ensembles_of_the_same_type': 'e',
        'linkage': '6',
        'alternative_medium_of_performance': 'p',
        'source_of_term': '2',
        'number_of_performers_of_the_same_medium': 'n',
        'field_link_and_sequence_number': '8',
        'note': 'v',
        'total_number_of_ensembles': 't',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(
            value.get('display_constant_controller'), '7') != '7':
        try:
            order.remove(field_map.get('display_constant_controller'))
        except ValueError:
            pass

    if indicator_map2.get(value.get('access_control'), '7') != '7':
        try:
            order.remove(field_map.get('access_control'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        's': value.get('total_number_of_performers'),
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        '6': value.get('linkage'),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        '2': value.get('source_of_term'),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        't': value.get('total_number_of_ensembles'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('access_control'), '_'),
    }


@to_marc21.over('383', '^numeric_designation_of_musical_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    field_map = {
        'linkage': '6',
        'serial_number': 'a',
        'opus_number': 'b',
        'thematic_index_number': 'c',
        'field_link_and_sequence_number': '8',
        'thematic_index_code': 'd',
        'publisher_associated_with_opus_number': 'e',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': value.get('thematic_index_code'),
        'e': value.get('publisher_associated_with_opus_number'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    indicator_map1 = {
        "Original key": "0",
        "Relationship to original unknown": "_",
        "Transposed key": "1"}
    field_map = {
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'key': 'a',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('key_type'), '7') != '7':
        try:
            order.remove(field_map.get('key_type'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('key'),
        '$ind1': indicator_map1.get(value.get('key_type'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'audience_term': 'a',
        'audience_code': 'b',
        'demographic_group_code': 'n',
        'field_link_and_sequence_number': '8',
        'demographic_group_term': 'm',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        'n': value.get('demographic_group_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('demographic_group_term'),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('386', '^creator_contributor_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'creator_contributor_term': 'a',
        'creator_contributor_code': 'b',
        'demographic_group_code': 'n',
        'field_link_and_sequence_number': '8',
        'demographic_group_term': 'm',
        'linkage': '6',
        'source': '2',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        'n': value.get('demographic_group_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('demographic_group_term'),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    indicator_map1 = {
        "Creation of aggregate work": "2",
        "Creation of work": "1",
        "No information provided": "_"}
    field_map = {
        'materials_specified': '3',
        'authority_record_control_number_or_standard_number': '0',
        'time_period_of_creation_term': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'source_of_term': '2',
    }

    order = utils.map_order(field_map, value)

    if indicator_map1.get(value.get('type_of_time_period'), '7') != '7':
        try:
            order.remove(field_map.get('type_of_time_period'))
        except ValueError:
            pass

    return {
        '__order__': tuple(order) if len(order) else None,
        '3': value.get('materials_specified'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source_of_term'),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), '_'),
        '$ind2': '_',
    }
