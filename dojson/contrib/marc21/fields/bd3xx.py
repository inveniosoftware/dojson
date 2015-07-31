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

from ..model import marc21, tomarc21


@marc21.over('physical_description', '^300..')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    """Physical Description."""
    return {
        'extent': utils.force_list(
            value.get('a')
        ),
        'dimensions': utils.force_list(
            value.get('c')
        ),
        'other_physical_details': value.get('b'),
        'accompanying_material': value.get('e'),
        'size_of_unit': utils.force_list(
            value.get('g')
        ),
        'type_of_unit': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^300..', 'physical_description')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_description(self, key, value):
    """Reverse - Physical Description."""
    return {
        'a': utils.reverse_force_list(value.get('extent')),
        'c': utils.reverse_force_list(value.get('dimensions')),
        'b': utils.reverse_force_list(value.get('other_physical_details')),
        'e': utils.reverse_force_list(value.get('accompanying_material')),
        'g': utils.reverse_force_list(value.get('size_of_unit')),
        'f': utils.reverse_force_list(value.get('type_of_unit')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('playing_time', '^306..')
@utils.filter_values
def playing_time(self, key, value):
    """Playing Time."""
    return {
        'playing_time': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^306..', 'playing_time')
@utils.filter_values
def reverse_playing_time(self, key, value):
    """Reverse - Playing Time."""
    return {
        'a': utils.reverse_force_list(value.get('playing_time')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('hours', '^307[8_].')
@utils.for_each_value
@utils.filter_values
def hours(self, key, value):
    """Hours, Etc.."""
    indicator_map1 = {"#": "Hours", "8": "No display constant generated"}
    return {
        'hours': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'additional_information': value.get('b'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^307[8_].', 'hours')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_hours(self, key, value):
    """Reverse - Hours, Etc.."""
    indicator_map1 = {"Hours": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('hours')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('additional_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('current_publication_frequency', '^310..')
@utils.filter_values
def current_publication_frequency(self, key, value):
    """Current Publication Frequency."""
    return {
        'current_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'date_of_current_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^310..', 'current_publication_frequency')
@utils.filter_values
def reverse_current_publication_frequency(self, key, value):
    """Reverse - Current Publication Frequency."""
    return {
        'a': utils.reverse_force_list(value.get('current_publication_frequency')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('date_of_current_publication_frequency')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('former_publication_frequency', '^321..')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    """Former Publication Frequency."""
    return {
        'former_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'dates_of_former_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^321..', 'former_publication_frequency')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_publication_frequency(self, key, value):
    """Reverse - Former Publication Frequency."""
    return {
        'a': utils.reverse_force_list(value.get('former_publication_frequency')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('dates_of_former_publication_frequency')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    """Content Type."""
    return {
        'content_type_term': utils.force_list(
            value.get('a')
        ),
        'content_type_code': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^336..', 'content_type')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_content_type(self, key, value):
    """Reverse - Content Type."""
    return {
        'a': utils.reverse_force_list(value.get('content_type_term')),
        'b': utils.reverse_force_list(value.get('content_type_code')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    """Media Type."""
    return {
        'media_type_term': utils.force_list(
            value.get('a')
        ),
        'media_type_code': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^337..', 'media_type')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_media_type(self, key, value):
    """Reverse - Media Type."""
    return {
        'a': utils.reverse_force_list(value.get('media_type_term')),
        'b': utils.reverse_force_list(value.get('media_type_code')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    """Carrier Type."""
    return {
        'carrier_type_term': utils.force_list(
            value.get('a')
        ),
        'carrier_type_code': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^338..', 'carrier_type')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_carrier_type(self, key, value):
    """Reverse - Carrier Type."""
    return {
        'a': utils.reverse_force_list(value.get('carrier_type_term')),
        'b': utils.reverse_force_list(value.get('carrier_type_code')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('physical_medium', '^340..')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    """Physical Medium."""
    return {
        'material_base_and_configuration': utils.force_list(
            value.get('a')
        ),
        'materials_applied_to_surface': utils.force_list(
            value.get('c')
        ),
        'dimensions': utils.force_list(
            value.get('b')
        ),
        'support': utils.force_list(
            value.get('e')
        ),
        'information_recording_technique': utils.force_list(
            value.get('d')
        ),
        'production_rate_ratio': utils.force_list(
            value.get('f')
        ),
        'technical_specifications_of_medium': utils.force_list(
            value.get('i')
        ),
        'location_within_medium': utils.force_list(
            value.get('h')
        ),
        'layout': utils.force_list(
            value.get('k')
        ),
        'generation': utils.force_list(
            value.get('j')
        ),
        'book_format': utils.force_list(
            value.get('m')
        ),
        'polarity': utils.force_list(
            value.get('o')
        ),
        'font_size': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^340..', 'physical_medium')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_physical_medium(self, key, value):
    """Reverse - Physical Medium."""
    return {
        'a': utils.reverse_force_list(value.get('material_base_and_configuration')),
        'c': utils.reverse_force_list(value.get('materials_applied_to_surface')),
        'b': utils.reverse_force_list(value.get('dimensions')),
        'e': utils.reverse_force_list(value.get('support')),
        'd': utils.reverse_force_list(value.get('information_recording_technique')),
        'f': utils.reverse_force_list(value.get('production_rate_ratio')),
        'i': utils.reverse_force_list(value.get('technical_specifications_of_medium')),
        'h': utils.reverse_force_list(value.get('location_within_medium')),
        'k': utils.reverse_force_list(value.get('layout')),
        'j': utils.reverse_force_list(value.get('generation')),
        'm': utils.reverse_force_list(value.get('book_format')),
        'o': utils.reverse_force_list(value.get('polarity')),
        'n': utils.reverse_force_list(value.get('font_size')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('geospatial_reference_data', '^342[10_][_103254768]')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    """Geospatial Reference Data."""
    indicator_map1 = {"0": "Horizontal coordinate system", "1": "Vertical coordinate system"}
    indicator_map2 = {"0": "Geographic", "1": "Map projection", "2": "Grid coordinate system", "3": "Local planar", "4": "Local", "5": "Geodetic model", "6": "Altitude", "7": "Method specified in $2", "8": "Depth"}
    return {
        'reference_method_used': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'name': value.get('a'),
        'latitude_resolution': value.get('c'),
        'coordinate_units_or_distance_units': value.get('b'),
        'standard_parallel_or_oblique_line_latitude': utils.force_list(
            value.get('e')
        ),
        'longitude_resolution': value.get('d'),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'oblique_line_longitude': utils.force_list(
            value.get('f')
        ),
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


@tomarc21.over('^342[10_][_103254768]', 'geospatial_reference_data')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geospatial_reference_data(self, key, value):
    """Reverse - Geospatial Reference Data."""
    indicator_map1 = {"Horizontal coordinate system": "0", "Vertical coordinate system": "1"}
    indicator_map2 = {"Altitude": "6", "Depth": "8", "Geodetic model": "5", "Geographic": "0", "Grid coordinate system": "2", "Local": "4", "Local planar": "3", "Map projection": "1", "Method specified in $2": "7"}
    return {
        '2': utils.reverse_force_list(value.get('reference_method_used')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('name')),
        'c': utils.reverse_force_list(value.get('latitude_resolution')),
        'b': utils.reverse_force_list(value.get('coordinate_units_or_distance_units')),
        'e': utils.reverse_force_list(value.get('standard_parallel_or_oblique_line_latitude')),
        'd': utils.reverse_force_list(value.get('longitude_resolution')),
        'g': utils.reverse_force_list(value.get('longitude_of_central_meridian_or_projection_center')),
        'f': utils.reverse_force_list(value.get('oblique_line_longitude')),
        'i': utils.reverse_force_list(value.get('false_easting')),
        'h': utils.reverse_force_list(value.get('latitude_of_projection_center_or_projection_origin')),
        'k': utils.reverse_force_list(value.get('scale_factor')),
        'j': utils.reverse_force_list(value.get('false_northing')),
        'm': utils.reverse_force_list(value.get('azimuthal_angle')),
        'l': utils.reverse_force_list(value.get('height_of_perspective_point_above_surface')),
        'o': utils.reverse_force_list(value.get('landsat_number_and_path_number')),
        'n': utils.reverse_force_list(value.get('azimuth_measure_point_longitude_or_straight_vertical_longitude_from_pole')),
        'q': utils.reverse_force_list(value.get('ellipsoid_name')),
        'p': utils.reverse_force_list(value.get('zone_identifier')),
        's': utils.reverse_force_list(value.get('denominator_of_flattening_ratio')),
        'r': utils.reverse_force_list(value.get('semi_major_axis')),
        'u': utils.reverse_force_list(value.get('vertical_encoding_method')),
        't': utils.reverse_force_list(value.get('vertical_resolution')),
        'w': utils.reverse_force_list(value.get('local_planar_or_local_georeference_information')),
        'v': utils.reverse_force_list(value.get('local_planar_local_or_other_projection_or_grid_description')),
        '_indicator1': indicator_map1.get(value.get('geospatial_reference_dimension')),
        '_indicator2': indicator_map2.get(value.get('geospatial_reference_method')),
    }


@marc21.over('planar_coordinate_data', '^343..')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
    """Planar Coordinate Data."""
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
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^343..', 'planar_coordinate_data')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_planar_coordinate_data(self, key, value):
    """Reverse - Planar Coordinate Data."""
    return {
        'a': utils.reverse_force_list(value.get('planar_coordinate_encoding_method')),
        'c': utils.reverse_force_list(value.get('abscissa_resolution')),
        'b': utils.reverse_force_list(value.get('planar_distance_units')),
        'e': utils.reverse_force_list(value.get('distance_resolution')),
        'd': utils.reverse_force_list(value.get('ordinate_resolution')),
        'g': utils.reverse_force_list(value.get('bearing_units')),
        'f': utils.reverse_force_list(value.get('bearing_resolution')),
        'i': utils.reverse_force_list(value.get('bearing_reference_meridian')),
        'h': utils.reverse_force_list(value.get('bearing_reference_direction')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('sound_characteristics', '^344..')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    """Sound Characteristics."""
    return {
        'type_of_recording': utils.force_list(
            value.get('a')
        ),
        'playing_speed': utils.force_list(
            value.get('c')
        ),
        'recording_medium': utils.force_list(
            value.get('b')
        ),
        'track_configuration': utils.force_list(
            value.get('e')
        ),
        'groove_characteristic': utils.force_list(
            value.get('d')
        ),
        'configuration_of_playback_channels': utils.force_list(
            value.get('g')
        ),
        'tape_configuration': utils.force_list(
            value.get('f')
        ),
        'special_playback_characteristics': utils.force_list(
            value.get('h')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^344..', 'sound_characteristics')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_sound_characteristics(self, key, value):
    """Reverse - Sound Characteristics."""
    return {
        'a': utils.reverse_force_list(value.get('type_of_recording')),
        'c': utils.reverse_force_list(value.get('playing_speed')),
        'b': utils.reverse_force_list(value.get('recording_medium')),
        'e': utils.reverse_force_list(value.get('track_configuration')),
        'd': utils.reverse_force_list(value.get('groove_characteristic')),
        'g': utils.reverse_force_list(value.get('configuration_of_playback_channels')),
        'f': utils.reverse_force_list(value.get('tape_configuration')),
        'h': utils.reverse_force_list(value.get('special_playback_characteristics')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('projection_characteristics_of_moving_image', '^345..')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    """Projection Characteristics of Moving Image."""
    return {
        'presentation_format': utils.force_list(
            value.get('a')
        ),
        'projection_speed': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^345..', 'projection_characteristics_of_moving_image')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_projection_characteristics_of_moving_image(self, key, value):
    """Reverse - Projection Characteristics of Moving Image."""
    return {
        'a': utils.reverse_force_list(value.get('presentation_format')),
        'b': utils.reverse_force_list(value.get('projection_speed')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('video_characteristics', '^346..')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    """Video Characteristics."""
    return {
        'video_format': utils.force_list(
            value.get('a')
        ),
        'broadcast_standard': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^346..', 'video_characteristics')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_video_characteristics(self, key, value):
    """Reverse - Video Characteristics."""
    return {
        'a': utils.reverse_force_list(value.get('video_format')),
        'b': utils.reverse_force_list(value.get('broadcast_standard')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('digital_file_characteristics', '^347..')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    """Digital File Characteristics."""
    return {
        'file_type': utils.force_list(
            value.get('a')
        ),
        'file_size': utils.force_list(
            value.get('c')
        ),
        'encoding_format': utils.force_list(
            value.get('b')
        ),
        'regional_encoding': utils.force_list(
            value.get('e')
        ),
        'resolution': utils.force_list(
            value.get('d')
        ),
        'transmission_speed': utils.force_list(
            value.get('f')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^347..', 'digital_file_characteristics')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_file_characteristics(self, key, value):
    """Reverse - Digital File Characteristics."""
    return {
        'a': utils.reverse_force_list(value.get('file_type')),
        'c': utils.reverse_force_list(value.get('file_size')),
        'b': utils.reverse_force_list(value.get('encoding_format')),
        'e': utils.reverse_force_list(value.get('regional_encoding')),
        'd': utils.reverse_force_list(value.get('resolution')),
        'f': utils.reverse_force_list(value.get('transmission_speed')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    """Organization and Arrangement of Materials."""
    return {
        'organization': utils.force_list(
            value.get('a')
        ),
        'hierarchical_level': value.get('c'),
        'arrangement': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^351..', 'organization_and_arrangement_of_materials')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_organization_and_arrangement_of_materials(self, key, value):
    """Reverse - Organization and Arrangement of Materials."""
    return {
        'a': utils.reverse_force_list(value.get('organization')),
        'c': utils.reverse_force_list(value.get('hierarchical_level')),
        'b': utils.reverse_force_list(value.get('arrangement')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('digital_graphic_representation', '^352..')
@utils.for_each_value
@utils.filter_values
def digital_graphic_representation(self, key, value):
    """Digital Graphic Representation."""
    return {
        'direct_reference_method': value.get('a'),
        'object_count': utils.force_list(
            value.get('c')
        ),
        'object_type': utils.force_list(
            value.get('b')
        ),
        'column_count': value.get('e'),
        'row_count': value.get('d'),
        'vpf_topology_level': value.get('g'),
        'vertical_count': value.get('f'),
        'indirect_reference_description': value.get('i'),
        'format_of_the_digital_image': value.get('q'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^352..', 'digital_graphic_representation')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_digital_graphic_representation(self, key, value):
    """Reverse - Digital Graphic Representation."""
    return {
        'a': utils.reverse_force_list(value.get('direct_reference_method')),
        'c': utils.reverse_force_list(value.get('object_count')),
        'b': utils.reverse_force_list(value.get('object_type')),
        'e': utils.reverse_force_list(value.get('column_count')),
        'd': utils.reverse_force_list(value.get('row_count')),
        'g': utils.reverse_force_list(value.get('vpf_topology_level')),
        'f': utils.reverse_force_list(value.get('vertical_count')),
        'i': utils.reverse_force_list(value.get('indirect_reference_description')),
        'q': utils.reverse_force_list(value.get('format_of_the_digital_image')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('security_classification_control', '^355[1032548_].')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    """Security Classification Control."""
    indicator_map1 = {"0": "Document", "1": "Title", "2": "Abstract", "3": "Contents note", "4": "Author", "5": "Record", "8": "None of the above"}
    return {
        'security_classification': value.get('a'),
        'external_dissemination_information': utils.force_list(
            value.get('c')
        ),
        'handling_instructions': utils.force_list(
            value.get('b')
        ),
        'classification_system': value.get('e'),
        'downgrading_or_declassification_event': value.get('d'),
        'downgrading_date': value.get('g'),
        'country_of_origin_code': value.get('f'),
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


@tomarc21.over('^355[1032548_].', 'security_classification_control')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_security_classification_control(self, key, value):
    """Reverse - Security Classification Control."""
    indicator_map1 = {"Abstract": "2", "Author": "4", "Contents note": "3", "Document": "0", "None of the above": "8", "Record": "5", "Title": "1"}
    return {
        'a': utils.reverse_force_list(value.get('security_classification')),
        'c': utils.reverse_force_list(value.get('external_dissemination_information')),
        'b': utils.reverse_force_list(value.get('handling_instructions')),
        'e': utils.reverse_force_list(value.get('classification_system')),
        'd': utils.reverse_force_list(value.get('downgrading_or_declassification_event')),
        'g': utils.reverse_force_list(value.get('downgrading_date')),
        'f': utils.reverse_force_list(value.get('country_of_origin_code')),
        'h': utils.reverse_force_list(value.get('declassification_date')),
        'j': utils.reverse_force_list(value.get('authorization')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('controlled_element')),
    }


@marc21.over('originator_dissemination_control', '^357..')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    """Originator Dissemination Control."""
    return {
        'originator_control_term': value.get('a'),
        'authorized_recipients_of_material': utils.force_list(
            value.get('c')
        ),
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


@tomarc21.over('^357..', 'originator_dissemination_control')
@utils.filter_values
def reverse_originator_dissemination_control(self, key, value):
    """Reverse - Originator Dissemination Control."""
    return {
        'a': utils.reverse_force_list(value.get('originator_control_term')),
        'c': utils.reverse_force_list(value.get('authorized_recipients_of_material')),
        'b': utils.reverse_force_list(value.get('originating_agency')),
        'g': utils.reverse_force_list(value.get('other_restrictions')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('dates_of_publication_and_or_sequential_designation', '^362[10_].')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    """Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"0": "Formatted style", "1": "Unformatted note"}
    return {
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'format_of_date': indicator_map1.get(key[3]),
    }


@tomarc21.over('^362[10_].', 'dates_of_publication_and_or_sequential_designation')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dates_of_publication_and_or_sequential_designation(self, key, value):
    """Reverse - Dates of Publication and/or Sequential Designation."""
    indicator_map1 = {"Formatted style": "0", "Unformatted note": "1"}
    return {
        'a': utils.reverse_force_list(value.get('dates_of_publication_and_or_sequential_designation')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('source_of_information')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('format_of_date')),
    }


@marc21.over('normalized_date_and_sequential_designation', '^363[10_][10_]')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    """Normalized Date and Sequential Designation."""
    indicator_map1 = {"#": "No information provided", "0": "Starting information", "1": "Ending information"}
    indicator_map2 = {"#": "Not specified", "0": "Closed", "1": "Open"}
    return {
        'first_level_of_enumeration': value.get('a'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
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
        'public_note': utils.force_list(
            value.get('z')
        ),
        'first_level_of_chronology_issuance': value.get('v'),
        'start_end_designator': indicator_map1.get(key[3]),
        'state_of_issuance': indicator_map2.get(key[4]),
    }


@tomarc21.over('^363[10_][10_]', 'normalized_date_and_sequential_designation')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_normalized_date_and_sequential_designation(self, key, value):
    """Reverse - Normalized Date and Sequential Designation."""
    indicator_map1 = {"Ending information": "1", "No information provided": "#", "Starting information": "0"}
    indicator_map2 = {"Closed": "0", "Not specified": "#", "Open": "1"}
    return {
        'a': utils.reverse_force_list(value.get('first_level_of_enumeration')),
        'x': utils.reverse_force_list(value.get('nonpublic_note')),
        'c': utils.reverse_force_list(value.get('third_level_of_enumeration')),
        'b': utils.reverse_force_list(value.get('second_level_of_enumeration')),
        'e': utils.reverse_force_list(value.get('fifth_level_of_enumeration')),
        'd': utils.reverse_force_list(value.get('fourth_level_of_enumeration')),
        'g': utils.reverse_force_list(value.get('alternative_numbering_scheme_first_level_of_enumeration')),
        'f': utils.reverse_force_list(value.get('sixth_level_of_enumeration')),
        'i': utils.reverse_force_list(value.get('first_level_of_chronology')),
        'h': utils.reverse_force_list(value.get('alternative_numbering_scheme_second_level_of_enumeration')),
        'k': utils.reverse_force_list(value.get('third_level_of_chronology')),
        'j': utils.reverse_force_list(value.get('second_level_of_chronology')),
        'm': utils.reverse_force_list(value.get('alternative_numbering_scheme_chronology')),
        'l': utils.reverse_force_list(value.get('fourth_level_of_chronology')),
        'u': utils.reverse_force_list(value.get('first_level_textual_designation')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('public_note')),
        'v': utils.reverse_force_list(value.get('first_level_of_chronology_issuance')),
        '_indicator1': indicator_map1.get(value.get('start_end_designator')),
        '_indicator2': indicator_map2.get(value.get('state_of_issuance')),
    }


@marc21.over('trade_price', '^365..')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
    """Trade Price."""
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
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^365..', 'trade_price')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_price(self, key, value):
    """Reverse - Trade Price."""
    return {
        'a': utils.reverse_force_list(value.get('price_type_code')),
        'c': utils.reverse_force_list(value.get('currency_code')),
        'b': utils.reverse_force_list(value.get('price_amount')),
        'e': utils.reverse_force_list(value.get('price_note')),
        'd': utils.reverse_force_list(value.get('unit_of_pricing')),
        'g': utils.reverse_force_list(value.get('price_effective_until')),
        'f': utils.reverse_force_list(value.get('price_effective_from')),
        'i': utils.reverse_force_list(value.get('tax_rate_2')),
        'h': utils.reverse_force_list(value.get('tax_rate_1')),
        'k': utils.reverse_force_list(value.get('marc_country_code')),
        'j': utils.reverse_force_list(value.get('iso_country_code')),
        'm': utils.reverse_force_list(value.get('identification_of_pricing_entity')),
        '2': utils.reverse_force_list(value.get('source_of_price_type_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('trade_availability_information', '^366..')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
    """Trade Availability Information."""
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
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^366..', 'trade_availability_information')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_trade_availability_information(self, key, value):
    """Reverse - Trade Availability Information."""
    return {
        'a': utils.reverse_force_list(value.get('publishers_compressed_title_identification')),
        'c': utils.reverse_force_list(value.get('availability_status_code')),
        'b': utils.reverse_force_list(value.get('detailed_date_of_publication')),
        'e': utils.reverse_force_list(value.get('note')),
        'd': utils.reverse_force_list(value.get('expected_next_availability_date')),
        'g': utils.reverse_force_list(value.get('date_made_out_of_print')),
        'f': utils.reverse_force_list(value.get('publisher_s_discount_category')),
        'k': utils.reverse_force_list(value.get('marc_country_code')),
        'j': utils.reverse_force_list(value.get('iso_country_code')),
        'm': utils.reverse_force_list(value.get('identification_of_agency')),
        '2': utils.reverse_force_list(value.get('source_of_availability_status_code')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    """Associated Language."""
    return {
        'language_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'language_term': utils.force_list(
            value.get('l')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^377..', 'associated_language')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_associated_language(self, key, value):
    """Reverse - Associated Language."""
    return {
        'a': utils.reverse_force_list(value.get('language_code')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '2': utils.reverse_force_list(value.get('source')),
        'l': utils.reverse_force_list(value.get('language_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    """Form of Work."""
    return {
        'form_of_work': utils.force_list(
            value.get('a')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^380..', 'form_of_work')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_form_of_work(self, key, value):
    """Reverse - Form of Work."""
    return {
        'a': utils.reverse_force_list(value.get('form_of_work')),
        '0': utils.reverse_force_list(value.get('record_control_number')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Other Distinguishing Characteristics of Work or Expression."""
    return {
        'other_distinguishing_characteristic': utils.force_list(
            value.get('a')
        ),
        'source_of_information': utils.force_list(
            value.get('v')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^381..', 'other_distinguishing_characteristics_of_work_or_expression')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    """Reverse - Other Distinguishing Characteristics of Work or Expression."""
    return {
        'a': utils.reverse_force_list(value.get('other_distinguishing_characteristic')),
        'v': utils.reverse_force_list(value.get('source_of_information')),
        '0': utils.reverse_force_list(value.get('record_control_number')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('medium_of_performance', '^382[10_][10_]')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    """Medium of Performance."""
    indicator_map1 = {"#": "No information provided", "0": "Medium of performance", "1": "Partial medium of performance"}
    indicator_map2 = {"#": "No information provided", "0": "Not intended for access", "1": "Intended for access"}
    return {
        'medium_of_performance': utils.force_list(
            value.get('a')
        ),
        'soloist': utils.force_list(
            value.get('b')
        ),
        'doubling_instrument': utils.force_list(
            value.get('d')
        ),
        'alternative_medium_of_performance': utils.force_list(
            value.get('p')
        ),
        'note': utils.force_list(
            value.get('v')
        ),
        'number_of_performers_of_the_same_medium': utils.force_list(
            value.get('n')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'total_number_of_performers': utils.force_list(
            value.get('s')
        ),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
        'access_control': indicator_map2.get(key[4]),
    }


@tomarc21.over('^382[10_][10_]', 'medium_of_performance')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_medium_of_performance(self, key, value):
    """Reverse - Medium of Performance."""
    indicator_map1 = {"Medium of performance": "0", "No information provided": "#", "Partial medium of performance": "1"}
    indicator_map2 = {"Intended for access": "1", "No information provided": "#", "Not intended for access": "0"}
    return {
        'a': utils.reverse_force_list(value.get('medium_of_performance')),
        'b': utils.reverse_force_list(value.get('soloist')),
        'd': utils.reverse_force_list(value.get('doubling_instrument')),
        'p': utils.reverse_force_list(value.get('alternative_medium_of_performance')),
        'v': utils.reverse_force_list(value.get('note')),
        'n': utils.reverse_force_list(value.get('number_of_performers_of_the_same_medium')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        's': utils.reverse_force_list(value.get('total_number_of_performers')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
        '_indicator2': indicator_map2.get(value.get('access_control')),
    }


@marc21.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    """Numeric Designation of Musical Work."""
    return {
        'serial_number': utils.force_list(
            value.get('a')
        ),
        'thematic_index_number': utils.force_list(
            value.get('c')
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


@tomarc21.over('^383..', 'numeric_designation_of_musical_work')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numeric_designation_of_musical_work(self, key, value):
    """Reverse - Numeric Designation of Musical Work."""
    return {
        'a': utils.reverse_force_list(value.get('serial_number')),
        'c': utils.reverse_force_list(value.get('thematic_index_number')),
        'b': utils.reverse_force_list(value.get('opus_number')),
        'e': utils.reverse_force_list(value.get('publisher_associated_with_opus_number')),
        'd': utils.reverse_force_list(value.get('thematic_index_code')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('key', '^384[10_].')
@utils.filter_values
def key(self, key, value):
    """Key."""
    indicator_map1 = {"#": "Relationship to original unknown ", "0": "Original key ", "1": "Transposed key "}
    return {
        'key': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'key_type': indicator_map1.get(key[3]),
    }


@tomarc21.over('^384[10_].', 'key')
@utils.filter_values
def reverse_key(self, key, value):
    """Reverse - Key."""
    indicator_map1 = {"Original key ": "0", "Relationship to original unknown ": "#", "Transposed key ": "1"}
    return {
        'a': utils.reverse_force_list(value.get('key')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('key_type')),
    }


@marc21.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    """Audience Characteristics."""
    return {
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
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^385..', 'audience_characteristics')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_audience_characteristics(self, key, value):
    """Reverse - Audience Characteristics."""
    return {
        'a': utils.reverse_force_list(value.get('audience_term')),
        'b': utils.reverse_force_list(value.get('audience_code')),
        'm': utils.reverse_force_list(value.get('demographic_group_term')),
        'n': utils.reverse_force_list(value.get('demographic_group_code')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    """Creator/Contributor Characteristics."""
    return {
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
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^386..', 'creator_contributor_characteristics')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creator_contributor_characteristics(self, key, value):
    """Reverse - Creator/Contributor Characteristics."""
    return {
        'a': utils.reverse_force_list(value.get('creator_contributor_term')),
        'b': utils.reverse_force_list(value.get('creator_contributor_code')),
        'm': utils.reverse_force_list(value.get('demographic_group_term')),
        'n': utils.reverse_force_list(value.get('demographic_group_code')),
        '0': utils.reverse_force_list(value.get('authority_record_control_number_or_standard_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }
