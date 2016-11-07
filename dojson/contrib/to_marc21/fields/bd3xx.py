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
        'dimensions': 'c',
        'accompanying_material': 'e',
        'type_of_unit': 'f',
        'size_of_unit': 'g',
        'extent': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'other_physical_details': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('dimensions')
        ),
        'e': value.get('accompanying_material'),
        'f': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'g': utils.reverse_force_list(
            value.get('size_of_unit')
        ),
        'a': utils.reverse_force_list(
            value.get('extent')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'b': value.get('other_physical_details'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('306', '^playing_time$')
@utils.filter_values
def reverse_playing_time(self, key, value):
    """Reverse - Playing Time."""
    field_map = {
        'playing_time': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('playing_time')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
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
        'hours': 'a',
        'additional_information': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('hours'),
        'b': value.get('additional_information'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('310', '^current_publication_frequency$')
@utils.filter_values
def reverse_current_publication_frequency(self, key, value):
    """Reverse - Current Publication Frequency."""
    field_map = {
        'current_publication_frequency': 'a',
        'date_of_current_publication_frequency': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('current_publication_frequency'),
        'b': value.get('date_of_current_publication_frequency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('321', '^former_publication_frequency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_publication_frequency(self, key, value):
    """Reverse - Former Publication Frequency."""
    field_map = {
        'former_publication_frequency': 'a',
        'dates_of_former_publication_frequency': 'b',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('former_publication_frequency'),
        'b': value.get('dates_of_former_publication_frequency'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('336', '^content_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    field_map = {
        'content_type_code': 'b',
        'content_type_term': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('content_type_code')
        ),
        'a': utils.reverse_force_list(
            value.get('content_type_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('337', '^media_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_media_type(self, key, value):
    """Reverse - Media Type."""
    field_map = {
        'media_type_code': 'b',
        'media_type_term': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('media_type_code')
        ),
        'a': utils.reverse_force_list(
            value.get('media_type_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('338', '^carrier_type$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_carrier_type(self, key, value):
    """Reverse - Carrier Type."""
    field_map = {
        'carrier_type_code': 'b',
        'carrier_type_term': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('carrier_type_code')
        ),
        'a': utils.reverse_force_list(
            value.get('carrier_type_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('340', '^physical_medium$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_medium(self, key, value):
    """Reverse - Physical Medium."""
    field_map = {
        'font_size': 'n',
        'generation': 'j',
        'source': '2',
        'dimensions': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'information_recording_technique': 'd',
        'materials_applied_to_surface': 'c',
        'support': 'e',
        'technical_specifications_of_medium': 'i',
        'layout': 'k',
        'location_within_medium': 'h',
        'material_base_and_configuration': 'a',
        'materials_specified': '3',
        'production_rate_ratio': 'f',
        'polarity': 'o',
        'book_format': 'm',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'n': utils.reverse_force_list(
            value.get('font_size')
        ),
        'j': utils.reverse_force_list(
            value.get('generation')
        ),
        '2': value.get('source'),
        'b': utils.reverse_force_list(
            value.get('dimensions')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('information_recording_technique')
        ),
        'c': utils.reverse_force_list(
            value.get('materials_applied_to_surface')
        ),
        'e': utils.reverse_force_list(
            value.get('support')
        ),
        'i': utils.reverse_force_list(
            value.get('technical_specifications_of_medium')
        ),
        'k': utils.reverse_force_list(
            value.get('layout')
        ),
        'h': utils.reverse_force_list(
            value.get('location_within_medium')
        ),
        'a': utils.reverse_force_list(
            value.get('material_base_and_configuration')
        ),
        '3': value.get('materials_specified'),
        'f': utils.reverse_force_list(
            value.get('production_rate_ratio')
        ),
        'o': utils.reverse_force_list(
            value.get('polarity')
        ),
        'm': utils.reverse_force_list(
            value.get('book_format')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('342', '^geospatial_reference_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geospatial_reference_data(self, key, value):
    """Reverse - Geospatial Reference Data."""
    indicator_map1 = {"Horizontal coordinate system": "0", "Vertical coordinate system": "1"}
    indicator_map2 = {"Altitude": "6", "Depth": "8", "Geodetic model": "5", "Geographic": "0", "Grid coordinate system": "2", "Local": "4", "Local planar": "3", "Map projection": "1", "Method specified in $2": "7"}
    field_map = {
        'vertical_resolution': 't',
        'ellipsoid_name': 'q',
        'reference_method_used': '2',
        'coordinate_units_or_distance_units': 'b',
        'height_of_perspective_point_above_surface': 'l',
        'name': 'a',
        'oblique_line_longitude': 'f',
        'azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole': 'n',
        'denominator_of_flattening_ratio': 's',
        'zone_identifier': 'p',
        'false_northing': 'j',
        'vertical_encoding_method': 'u',
        'semi_major_axis': 'r',
        'field_link_and_sequence_number': '8',
        'azimuthal_angle': 'm',
        'longitude_resolution': 'd',
        'latitude_resolution': 'c',
        'standard_parallel_or_oblique_line_latitude': 'e',
        'scale_factor': 'k',
        'local_planar_local_or_other_projection_or_grid_description': 'v',
        'longitude_of_central_meridian_or_projection_center': 'g',
        'landsat_number_and_path_number': 'o',
        'linkage': '6',
        'local_planar_or_local_georeference_information': 'w',
        'latitude_of_projection_center_or_projection_origin': 'h',
        'false_easting': 'i',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('vertical_resolution'),
        'q': value.get('ellipsoid_name'),
        '2': value.get('reference_method_used'),
        'b': value.get('coordinate_units_or_distance_units'),
        'l': value.get('height_of_perspective_point_above_surface'),
        'a': value.get('name'),
        'f': utils.reverse_force_list(
            value.get('oblique_line_longitude')
        ),
        'n': value.get('azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole'),
        's': value.get('denominator_of_flattening_ratio'),
        'p': value.get('zone_identifier'),
        'j': value.get('false_northing'),
        'u': value.get('vertical_encoding_method'),
        'r': value.get('semi_major_axis'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'm': value.get('azimuthal_angle'),
        'd': value.get('longitude_resolution'),
        'c': value.get('latitude_resolution'),
        'e': utils.reverse_force_list(
            value.get('standard_parallel_or_oblique_line_latitude')
        ),
        'k': value.get('scale_factor'),
        'v': value.get('local_planar_local_or_other_projection_or_grid_description'),
        'g': value.get('longitude_of_central_meridian_or_projection_center'),
        'o': value.get('landsat_number_and_path_number'),
        '6': value.get('linkage'),
        'w': value.get('local_planar_or_local_georeference_information'),
        'h': value.get('latitude_of_projection_center_or_projection_origin'),
        'i': value.get('false_easting'),
        '$ind1': indicator_map1.get(value.get('geospatial_reference_dimension'), '_'),
        '$ind2': '7' if 'geospatial_reference_method' in value and
        not indicator_map2.get(value.get('geospatial_reference_method')) and
        value.get('geospatial_reference_method') == value.get('reference_method_used')
        else indicator_map2.get(value.get('geospatial_reference_method'), '_'),
    }


@to_marc21.over('343', '^planar_coordinate_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_planar_coordinate_data(self, key, value):
    """Reverse - Planar Coordinate Data."""
    field_map = {
        'ordinate_resolution': 'd',
        'abscissa_resolution': 'c',
        'distance_resolution': 'e',
        'bearing_resolution': 'f',
        'bearing_reference_direction': 'h',
        'bearing_units': 'g',
        'planar_coordinate_encoding_method': 'a',
        'linkage': '6',
        'bearing_reference_meridian': 'i',
        'planar_distance_units': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('ordinate_resolution'),
        'c': value.get('abscissa_resolution'),
        'e': value.get('distance_resolution'),
        'f': value.get('bearing_resolution'),
        'h': value.get('bearing_reference_direction'),
        'g': value.get('bearing_units'),
        'a': value.get('planar_coordinate_encoding_method'),
        '6': value.get('linkage'),
        'i': value.get('bearing_reference_meridian'),
        'b': value.get('planar_distance_units'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('344', '^sound_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_sound_characteristics(self, key, value):
    """Reverse - Sound Characteristics."""
    field_map = {
        'source': '2',
        'recording_medium': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'groove_characteristic': 'd',
        'playing_speed': 'c',
        'track_configuration': 'e',
        'special_playback_characteristics': 'h',
        'configuration_of_playback_channels': 'g',
        'type_of_recording': 'a',
        'materials_specified': '3',
        'tape_configuration': 'f',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        '2': value.get('source'),
        'b': utils.reverse_force_list(
            value.get('recording_medium')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('groove_characteristic')
        ),
        'c': utils.reverse_force_list(
            value.get('playing_speed')
        ),
        'e': utils.reverse_force_list(
            value.get('track_configuration')
        ),
        'h': utils.reverse_force_list(
            value.get('special_playback_characteristics')
        ),
        'g': utils.reverse_force_list(
            value.get('configuration_of_playback_channels')
        ),
        'a': utils.reverse_force_list(
            value.get('type_of_recording')
        ),
        '3': value.get('materials_specified'),
        'f': utils.reverse_force_list(
            value.get('tape_configuration')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('345', '^projection_characteristics_of_moving_image$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_projection_characteristics_of_moving_image(self, key, value):
    """Reverse - Projection Characteristics of Moving Image."""
    field_map = {
        'projection_speed': 'b',
        'presentation_format': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('projection_speed')
        ),
        'a': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('346', '^video_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_video_characteristics(self, key, value):
    """Reverse - Video Characteristics."""
    field_map = {
        'broadcast_standard': 'b',
        'video_format': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('broadcast_standard')
        ),
        'a': utils.reverse_force_list(
            value.get('video_format')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('347', '^digital_file_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_file_characteristics(self, key, value):
    """Reverse - Digital File Characteristics."""
    field_map = {
        'resolution': 'd',
        'file_size': 'c',
        'regional_encoding': 'e',
        'encoding_format': 'b',
        'file_type': 'a',
        'materials_specified': '3',
        'encoded_bitrate': 'f',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': utils.reverse_force_list(
            value.get('resolution')
        ),
        'c': utils.reverse_force_list(
            value.get('file_size')
        ),
        'e': utils.reverse_force_list(
            value.get('regional_encoding')
        ),
        'b': utils.reverse_force_list(
            value.get('encoding_format')
        ),
        'a': utils.reverse_force_list(
            value.get('file_type')
        ),
        '3': value.get('materials_specified'),
        'f': utils.reverse_force_list(
            value.get('encoded_bitrate')
        ),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('348', '^format_of_notated_music$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_format_of_notated_music(self, key, value):
    """Reverse - Format of Notated Music."""
    field_map = {
        'format_of_notated_music_code': 'b',
        'format_of_notated_music_term': 'a',
        'materials_specified': '3',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'b': utils.reverse_force_list(
            value.get('format_of_notated_music_code')
        ),
        'a': utils.reverse_force_list(
            value.get('format_of_notated_music_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('351', '^organization_and_arrangement_of_materials$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_organization_and_arrangement_of_materials(self, key, value):
    """Reverse - Organization and Arrangement of Materials."""
    field_map = {
        'hierarchical_level': 'c',
        'organization': 'a',
        'materials_specified': '3',
        'linkage': '6',
        'arrangement': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': value.get('hierarchical_level'),
        'a': utils.reverse_force_list(
            value.get('organization')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('arrangement')
        ),
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
        'row_count': 'd',
        'object_count': 'c',
        'column_count': 'e',
        'vertical_count': 'f',
        'format_of_the_digital_image': 'q',
        'vpf_topology_level': 'g',
        'direct_reference_method': 'a',
        'linkage': '6',
        'indirect_reference_description': 'i',
        'object_type': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('row_count'),
        'c': utils.reverse_force_list(
            value.get('object_count')
        ),
        'e': value.get('column_count'),
        'f': value.get('vertical_count'),
        'q': value.get('format_of_the_digital_image'),
        'g': value.get('vpf_topology_level'),
        'a': value.get('direct_reference_method'),
        '6': value.get('linkage'),
        'i': value.get('indirect_reference_description'),
        'b': utils.reverse_force_list(
            value.get('object_type')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('355', '^security_classification_control$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_security_classification_control(self, key, value):
    """Reverse - Security Classification Control."""
    indicator_map1 = {"Abstract": "2", "Author": "4", "Contents note": "3", "Document": "0", "None of the above": "8", "Record": "5", "Title": "1"}
    field_map = {
        'downgrading_or_declassification_event': 'd',
        'external_dissemination_information': 'c',
        'classification_system': 'e',
        'country_of_origin_code': 'f',
        'authorization': 'j',
        'declassification_date': 'h',
        'downgrading_date': 'g',
        'security_classification': 'a',
        'linkage': '6',
        'handling_instructions': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('downgrading_or_declassification_event'),
        'c': utils.reverse_force_list(
            value.get('external_dissemination_information')
        ),
        'e': value.get('classification_system'),
        'f': value.get('country_of_origin_code'),
        'j': utils.reverse_force_list(
            value.get('authorization')
        ),
        'h': value.get('declassification_date'),
        'g': value.get('downgrading_date'),
        'a': value.get('security_classification'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('handling_instructions')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('controlled_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('357', '^originator_dissemination_control$')
@utils.filter_values
def reverse_originator_dissemination_control(self, key, value):
    """Reverse - Originator Dissemination Control."""
    field_map = {
        'authorized_recipients_of_material': 'c',
        'other_restrictions': 'g',
        'originator_control_term': 'a',
        'linkage': '6',
        'originating_agency': 'b',
        'field_link_and_sequence_number': '8',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('authorized_recipients_of_material')
        ),
        'g': utils.reverse_force_list(
            value.get('other_restrictions')
        ),
        'a': value.get('originator_control_term'),
        '6': value.get('linkage'),
        'b': utils.reverse_force_list(
            value.get('originating_agency')
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
def reverse_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Reverse - Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"Formatted style": "0", "Unformatted note": "1"}
    field_map = {
        'source_of_information': 'z',
        'dates_of_publication_and_or_sequential_designation': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': value.get('source_of_information'),
        'a': value.get('dates_of_publication_and_or_sequential_designation'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('format_of_date'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('363', '^normalized_date_and_sequential_designation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_normalized_date_and_sequential_designation(self, key, value):
    """Reverse - Normalized Date and Sequential Designation."""
    indicator_map1 = {"Ending information": "1", "No information provided": "_", "Starting information": "0"}
    indicator_map2 = {"Closed": "0", "Not specified": "_", "Open": "1"}
    field_map = {
        'public_note': 'z',
        'nonpublic_note': 'x',
        'second_level_of_chronology': 'j',
        'first_level_textual_designation': 'u',
        'fourth_level_of_chronology': 'l',
        'first_level_of_chronology_issuance': 'v',
        'second_level_of_enumeration': 'b',
        'field_link_and_sequence_number': '8',
        'fourth_level_of_enumeration': 'd',
        'third_level_of_enumeration': 'c',
        'fifth_level_of_enumeration': 'e',
        'first_level_of_chronology': 'i',
        'third_level_of_chronology': 'k',
        'first_level_of_enumeration': 'a',
        'alternative_numbering_scheme_first_level_of_enumeration': 'g',
        'alternative_numbering_scheme_second_level_of_enumeration': 'h',
        'sixth_level_of_enumeration': 'f',
        'alternative_numbering_scheme_chronology': 'm',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'j': value.get('second_level_of_chronology'),
        'u': value.get('first_level_textual_designation'),
        'l': value.get('fourth_level_of_chronology'),
        'v': value.get('first_level_of_chronology_issuance'),
        'b': value.get('second_level_of_enumeration'),
        '8': value.get('field_link_and_sequence_number'),
        'd': value.get('fourth_level_of_enumeration'),
        'c': value.get('third_level_of_enumeration'),
        'e': value.get('fifth_level_of_enumeration'),
        'i': value.get('first_level_of_chronology'),
        'k': value.get('third_level_of_chronology'),
        'a': value.get('first_level_of_enumeration'),
        'g': value.get('alternative_numbering_scheme_first_level_of_enumeration'),
        'h': value.get('alternative_numbering_scheme_second_level_of_enumeration'),
        'f': value.get('sixth_level_of_enumeration'),
        'm': value.get('alternative_numbering_scheme_chronology'),
        '6': value.get('linkage'),
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
        'source_of_price_type_code': '2',
        'field_link_and_sequence_number': '8',
        'price_amount': 'b',
        'unit_of_pricing': 'd',
        'currency_code': 'c',
        'price_note': 'e',
        'tax_rate_2': 'i',
        'marc_country_code': 'k',
        'price_type_code': 'a',
        'price_effective_until': 'g',
        'tax_rate_1': 'h',
        'price_effective_from': 'f',
        'identification_of_pricing_entity': 'm',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('iso_country_code'),
        '2': value.get('source_of_price_type_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('price_amount'),
        'd': value.get('unit_of_pricing'),
        'c': value.get('currency_code'),
        'e': value.get('price_note'),
        'i': value.get('tax_rate_2'),
        'k': value.get('marc_country_code'),
        'a': value.get('price_type_code'),
        'g': value.get('price_effective_until'),
        'h': value.get('tax_rate_1'),
        'f': value.get('price_effective_from'),
        'm': value.get('identification_of_pricing_entity'),
        '6': value.get('linkage'),
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
        'source_of_availability_status_code': '2',
        'field_link_and_sequence_number': '8',
        'detailed_date_of_publication': 'b',
        'expected_next_availability_date': 'd',
        'availability_status_code': 'c',
        'note': 'e',
        'marc_country_code': 'k',
        'date_made_out_of_print': 'g',
        'publishers_compressed_title_identification': 'a',
        'publisher_s_discount_category': 'f',
        'identification_of_agency': 'm',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'j': value.get('iso_country_code'),
        '2': value.get('source_of_availability_status_code'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('detailed_date_of_publication'),
        'd': value.get('expected_next_availability_date'),
        'c': value.get('availability_status_code'),
        'e': value.get('note'),
        'k': value.get('marc_country_code'),
        'g': value.get('date_made_out_of_print'),
        'a': value.get('publishers_compressed_title_identification'),
        'f': value.get('publisher_s_discount_category'),
        'm': value.get('identification_of_agency'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('370', '^associated_place$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_place(self, key, value):
    """Reverse - Associated Place."""
    field_map = {
        'associated_country': 'c',
        'start_period': 's',
        'end_period': 't',
        'place_of_origin_of_work': 'g',
        'source_of_information': 'v',
        'uniform_resource_identifier': 'u',
        'other_associated_place': 'f',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'c': utils.reverse_force_list(
            value.get('associated_country')
        ),
        's': value.get('start_period'),
        't': value.get('end_period'),
        'g': utils.reverse_force_list(
            value.get('place_of_origin_of_work')
        ),
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        'f': utils.reverse_force_list(
            value.get('other_associated_place')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('377', '^associated_language$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    indicator_map2 = {"MARC language code": "_", "Source specified in subfield $2": "7"}
    field_map = {
        'language_code': 'a',
        'language_term': 'l',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('language_code')
        ),
        'l': utils.reverse_force_list(
            value.get('language_term')
        ),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
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
        'form_of_work': 'a',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('form_of_work')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('381', '^other_distinguishing_characteristics_of_work_or_expression$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    field_map = {
        'source_of_information': 'v',
        'other_distinguishing_characteristic': 'a',
        'uniform_resource_identifier': 'u',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'record_control_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('source_of_information')
        ),
        'a': utils.reverse_force_list(
            value.get('other_distinguishing_characteristic')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('382', '^medium_of_performance$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {"Medium of performance": "0", "No information provided": "_", "Partial medium of performance": "1"}
    indicator_map2 = {"Intended for access": "1", "No information provided": "_", "Not intended for access": "0"}
    field_map = {
        'total_number_of_ensembles': 't',
        'alternative_medium_of_performance': 'p',
        'note': 'v',
        'total_number_of_individuals_performing_alongside_ensembles': 'r',
        'source_of_term': '2',
        'soloist': 'b',
        'authority_record_control_number_or_standard_number': '0',
        'field_link_and_sequence_number': '8',
        'doubling_instrument': 'd',
        'number_of_ensembles_of_the_same_type': 'e',
        'medium_of_performance': 'a',
        'number_of_performers_of_the_same_medium': 'n',
        'total_number_of_performers': 's',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        't': value.get('total_number_of_ensembles'),
        'p': utils.reverse_force_list(
            value.get('alternative_medium_of_performance')
        ),
        'v': utils.reverse_force_list(
            value.get('note')
        ),
        'r': value.get('total_number_of_individuals_performing_alongside_ensembles'),
        '2': value.get('source_of_term'),
        'b': utils.reverse_force_list(
            value.get('soloist')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'd': utils.reverse_force_list(
            value.get('doubling_instrument')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_ensembles_of_the_same_type')
        ),
        'a': utils.reverse_force_list(
            value.get('medium_of_performance')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_performers_of_the_same_medium')
        ),
        's': value.get('total_number_of_performers'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('access_control'), '_'),
    }


@to_marc21.over('383', '^numeric_designation_of_musical_work$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    field_map = {
        'thematic_index_code': 'd',
        'thematic_index_number': 'c',
        'publisher_associated_with_opus_number': 'e',
        'serial_number': 'a',
        'linkage': '6',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'opus_number': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'd': value.get('thematic_index_code'),
        'c': utils.reverse_force_list(
            value.get('thematic_index_number')
        ),
        'e': value.get('publisher_associated_with_opus_number'),
        'a': utils.reverse_force_list(
            value.get('serial_number')
        ),
        '6': value.get('linkage'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': utils.reverse_force_list(
            value.get('opus_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('384', '^key$')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    indicator_map1 = {"Original key": "0", "Relationship to original unknown": "_", "Transposed key": "1"}
    field_map = {
        'key': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('key'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('key_type'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('385', '^audience_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    field_map = {
        'demographic_group_code': 'n',
        'audience_code': 'b',
        'demographic_group_term': 'm',
        'audience_term': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'n': value.get('demographic_group_code'),
        'b': utils.reverse_force_list(
            value.get('audience_code')
        ),
        'm': value.get('demographic_group_term'),
        'a': utils.reverse_force_list(
            value.get('audience_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('386', '^creator_contributor_characteristics$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    field_map = {
        'demographic_group_code': 'n',
        'creator_contributor_code': 'b',
        'demographic_group_term': 'm',
        'creator_contributor_term': 'a',
        'materials_specified': '3',
        'source': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'n': value.get('demographic_group_code'),
        'b': utils.reverse_force_list(
            value.get('creator_contributor_code')
        ),
        'm': value.get('demographic_group_term'),
        'a': utils.reverse_force_list(
            value.get('creator_contributor_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('388', '^time_period_of_creation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_time_period_of_creation(self, key, value):
    """Reverse - Time Period of Creation."""
    indicator_map1 = {"Creation of aggregate work": "2", "Creation of work": "1", "No information provided": "_"}
    field_map = {
        'time_period_of_creation_term': 'a',
        'materials_specified': '3',
        'source_of_term': '2',
        'field_link_and_sequence_number': '8',
        'authority_record_control_number_or_standard_number': '0',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('time_period_of_creation_term')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_time_period'), '_'),
        '$ind2': '_',
    }
