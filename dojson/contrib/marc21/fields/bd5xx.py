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


@marc21.over('general_note', '^500..')
@utils.for_each_value
@utils.filter_values
def general_note(self, key, value):
    """General Note."""
    return {
        'general_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^500..', 'general_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_general_note(self, key, value):
    """Reverse - General Note."""
    return {
        'a': utils.reverse_force_list(value.get('general_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('with_note', '^501..')
@utils.for_each_value
@utils.filter_values
def with_note(self, key, value):
    """With Note."""
    return {
        'with_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^501..', 'with_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_with_note(self, key, value):
    """Reverse - With Note."""
    return {
        'a': utils.reverse_force_list(value.get('with_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('dissertation_note', '^502..')
@utils.for_each_value
@utils.filter_values
def dissertation_note(self, key, value):
    """Dissertation Note."""
    return {
        'dissertation_note': value.get('a'),
        'name_of_granting_institution': value.get('c'),
        'degree_type': value.get('b'),
        'year_degree_granted': value.get('d'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'dissertation_identifier': utils.force_list(
            value.get('o')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^502..', 'dissertation_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dissertation_note(self, key, value):
    """Reverse - Dissertation Note."""
    return {
        'a': utils.reverse_force_list(value.get('dissertation_note')),
        'c': utils.reverse_force_list(value.get('name_of_granting_institution')),
        'b': utils.reverse_force_list(value.get('degree_type')),
        'd': utils.reverse_force_list(value.get('year_degree_granted')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'o': utils.reverse_force_list(value.get('dissertation_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('bibliography_note', '^504..')
@utils.for_each_value
@utils.filter_values
def bibliography_note(self, key, value):
    """Bibliography, Etc. Note."""
    return {
        'bibliography_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_of_references': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^504..', 'bibliography_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_bibliography_note(self, key, value):
    """Reverse - Bibliography, Etc. Note."""
    return {
        'a': utils.reverse_force_list(value.get('bibliography_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('number_of_references')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('formatted_contents_note', '^505[10_28][0_]')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    """Formatted Contents Note."""
    indicator_map1 = {"0": "Contents", "1": "Incomplete contents", "2": "Partial contents", "8": "No display constant generated"}
    indicator_map2 = {"#": "Basic", "0": "Enhanced"}
    return {
        'formatted_contents_note': value.get('a'),
        'miscellaneous_information': utils.force_list(
            value.get('g')
        ),
        'statement_of_responsibility': utils.force_list(
            value.get('r')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'title': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
        'level_of_content_designation': indicator_map2.get(key[4]),
    }


@tomarc21.over('^505[10_28][0_]', 'formatted_contents_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_formatted_contents_note(self, key, value):
    """Reverse - Formatted Contents Note."""
    indicator_map1 = {"Contents": "0", "Incomplete contents": "1", "No display constant generated": "8", "Partial contents": "2"}
    indicator_map2 = {"Basic": "#", "Enhanced": "0"}
    return {
        'a': utils.reverse_force_list(value.get('formatted_contents_note')),
        'g': utils.reverse_force_list(value.get('miscellaneous_information')),
        'r': utils.reverse_force_list(value.get('statement_of_responsibility')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        't': utils.reverse_force_list(value.get('title')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
        '_indicator2': indicator_map2.get(value.get('level_of_content_designation')),
    }


@marc21.over('restrictions_on_access_note', '^506[10_].')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    indicator_map1 = {"#": "No information provided", "0": "No restrictions", "1": "Restrictions apply"}
    return {
        'terms_governing_access': value.get('a'),
        'physical_access_provisions': utils.force_list(
            value.get('c')
        ),
        'jurisdiction': utils.force_list(
            value.get('b')
        ),
        'authorization': utils.force_list(
            value.get('e')
        ),
        'authorized_users': utils.force_list(
            value.get('d')
        ),
        'standardized_terminology_for_access_restriction': utils.force_list(
            value.get('f')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'restriction': indicator_map1.get(key[3]),
    }


@tomarc21.over('^506[10_].', 'restrictions_on_access_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_restrictions_on_access_note(self, key, value):
    """Reverse - Restrictions on Access Note."""
    indicator_map1 = {"No information provided": "#", "No restrictions": "0", "Restrictions apply": "1"}
    return {
        'a': utils.reverse_force_list(value.get('terms_governing_access')),
        'c': utils.reverse_force_list(value.get('physical_access_provisions')),
        'b': utils.reverse_force_list(value.get('jurisdiction')),
        'e': utils.reverse_force_list(value.get('authorization')),
        'd': utils.reverse_force_list(value.get('authorized_users')),
        'f': utils.reverse_force_list(value.get('standardized_terminology_for_access_restriction')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '_indicator1': indicator_map1.get(value.get('restriction')),
    }


@marc21.over('scale_note_for_graphic_material', '^507..')
@utils.filter_values
def scale_note_for_graphic_material(self, key, value):
    """Scale Note for Graphic Material."""
    return {
        'representative_fraction_of_scale_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'remainder_of_scale_note': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^507..', 'scale_note_for_graphic_material')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    return {
        'a': utils.reverse_force_list(value.get('representative_fraction_of_scale_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('remainder_of_scale_note')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('creation_production_credits_note', '^508..')
@utils.for_each_value
@utils.filter_values
def creation_production_credits_note(self, key, value):
    """Creation/Production Credits Note."""
    return {
        'creation_production_credits_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^508..', 'creation_production_credits_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creation_production_credits_note(self, key, value):
    """Reverse - Creation/Production Credits Note."""
    return {
        'a': utils.reverse_force_list(value.get('creation_production_credits_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('citation_references_note', '^510[10324_].')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    """Citation/References Note."""
    indicator_map1 = {"0": "Coverage unknown", "1": "Coverage complete", "2": "Coverage is selective", "3": "Location in source not given", "4": "Location in source given"}
    return {
        'name_of_source': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_within_source': value.get('c'),
        'coverage_of_source': value.get('b'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'coverage_location_in_source': indicator_map1.get(key[3]),
    }


@tomarc21.over('^510[10324_].', 'citation_references_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_citation_references_note(self, key, value):
    """Reverse - Citation/References Note."""
    indicator_map1 = {"Coverage complete": "1", "Coverage is selective": "2", "Coverage unknown": "0", "Location in source given": "4", "Location in source not given": "3"}
    return {
        'a': utils.reverse_force_list(value.get('name_of_source')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('location_within_source')),
        'b': utils.reverse_force_list(value.get('coverage_of_source')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('coverage_location_in_source')),
    }


@marc21.over('participant_or_performer_note', '^511[10_].')
@utils.for_each_value
@utils.filter_values
def participant_or_performer_note(self, key, value):
    """Participant or Performer Note."""
    indicator_map1 = {"0": "No display constant generated", "1": "Cast"}
    return {
        'participant_or_performer_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^511[10_].', 'participant_or_performer_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_participant_or_performer_note(self, key, value):
    """Reverse - Participant or Performer Note."""
    indicator_map1 = {"Cast": "1", "No display constant generated": "0"}
    return {
        'a': utils.reverse_force_list(value.get('participant_or_performer_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('type_of_report_and_period_covered_note', '^513..')
@utils.for_each_value
@utils.filter_values
def type_of_report_and_period_covered_note(self, key, value):
    """Type of Report and Period Covered Note."""
    return {
        'type_of_report': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'period_covered': value.get('b'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^513..', 'type_of_report_and_period_covered_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    return {
        'a': utils.reverse_force_list(value.get('type_of_report')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('period_covered')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('data_quality_note', '^514..')
@utils.filter_values
def data_quality_note(self, key, value):
    """Data Quality Note."""
    return {
        'attribute_accuracy_report': value.get('a'),
        'attribute_accuracy_explanation': utils.force_list(
            value.get('c')
        ),
        'attribute_accuracy_value': utils.force_list(
            value.get('b')
        ),
        'completeness_report': value.get('e'),
        'logical_consistency_report': value.get('d'),
        'horizontal_position_accuracy_value': utils.force_list(
            value.get('g')
        ),
        'horizontal_position_accuracy_report': value.get('f'),
        'vertical_positional_accuracy_report': value.get('i'),
        'horizontal_position_accuracy_explanation': utils.force_list(
            value.get('h')
        ),
        'vertical_positional_accuracy_explanation': utils.force_list(
            value.get('k')
        ),
        'vertical_positional_accuracy_value': utils.force_list(
            value.get('j')
        ),
        'cloud_cover': value.get('m'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_note': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('^514..', 'data_quality_note')
@utils.filter_values
def reverse_data_quality_note(self, key, value):
    """Reverse - Data Quality Note."""
    return {
        'a': utils.reverse_force_list(value.get('attribute_accuracy_report')),
        'c': utils.reverse_force_list(value.get('attribute_accuracy_explanation')),
        'b': utils.reverse_force_list(value.get('attribute_accuracy_value')),
        'e': utils.reverse_force_list(value.get('completeness_report')),
        'd': utils.reverse_force_list(value.get('logical_consistency_report')),
        'g': utils.reverse_force_list(value.get('horizontal_position_accuracy_value')),
        'f': utils.reverse_force_list(value.get('horizontal_position_accuracy_report')),
        'i': utils.reverse_force_list(value.get('vertical_positional_accuracy_report')),
        'h': utils.reverse_force_list(value.get('horizontal_position_accuracy_explanation')),
        'k': utils.reverse_force_list(value.get('vertical_positional_accuracy_explanation')),
        'j': utils.reverse_force_list(value.get('vertical_positional_accuracy_value')),
        'm': utils.reverse_force_list(value.get('cloud_cover')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('display_note')),
    }


@marc21.over('numbering_peculiarities_note', '^515..')
@utils.for_each_value
@utils.filter_values
def numbering_peculiarities_note(self, key, value):
    """Numbering Peculiarities Note."""
    return {
        'numbering_peculiarities_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^515..', 'numbering_peculiarities_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numbering_peculiarities_note(self, key, value):
    """Reverse - Numbering Peculiarities Note."""
    return {
        'a': utils.reverse_force_list(value.get('numbering_peculiarities_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('type_of_computer_file_or_data_note', '^516[8_].')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    """Type of Computer File or Data Note."""
    indicator_map1 = {"#": "Type of file", "8": "No display constant generated"}
    return {
        'type_of_computer_file_or_data_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^516[8_].', 'type_of_computer_file_or_data_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_computer_file_or_data_note(self, key, value):
    """Reverse - Type of Computer File or Data Note."""
    indicator_map1 = {"No display constant generated": "8", "Type of file": "#"}
    return {
        'a': utils.reverse_force_list(value.get('type_of_computer_file_or_data_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('date_time_and_place_of_an_event_note', '^518..')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event_note(self, key, value):
    """Date/Time and Place of an Event Note."""
    return {
        'date_time_and_place_of_an_event_note': value.get('a'),
        'date_of_event': utils.force_list(
            value.get('d')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'other_event_information': utils.force_list(
            value.get('o')
        ),
        'record_control_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^518..', 'date_time_and_place_of_an_event_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    return {
        'a': utils.reverse_force_list(value.get('date_time_and_place_of_an_event_note')),
        'd': utils.reverse_force_list(value.get('date_of_event')),
        'p': utils.reverse_force_list(value.get('place_of_event')),
        'o': utils.reverse_force_list(value.get('other_event_information')),
        '0': utils.reverse_force_list(value.get('record_control_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('summary', '^520[10_2483].')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    """Summary, Etc.."""
    indicator_map1 = {"#": "Summary", "0": "Subject", "1": "Review", "2": "Scope and content", "3": "Abstract", "4": "Content advice", "8": "No display constant generated"}
    return {
        'summary': value.get('a'),
        'assigning_source': value.get('c'),
        'expansion_of_summary_note': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^520[10_2483].', 'summary')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {"Abstract": "3", "Content advice": "4", "No display constant generated": "8", "Review": "1", "Scope and content": "2", "Subject": "0", "Summary": "#"}
    return {
        'a': utils.reverse_force_list(value.get('summary')),
        'c': utils.reverse_force_list(value.get('assigning_source')),
        'b': utils.reverse_force_list(value.get('expansion_of_summary_note')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('target_audience_note', '^521[10_2483].')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    """Target Audience Note."""
    indicator_map1 = {"#": "Audience", "0": "Reading grade level", "1": "Interest age level", "2": "Interest grade level", "3": "Special audience characteristics", "4": "Motivation/interest level", "8": "No display constant generated"}
    return {
        'target_audience_note': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('b'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^521[10_2483].', 'target_audience_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {"Audience": "#", "Interest age level": "1", "Interest grade level": "2", "Motivation/interest level": "4", "No display constant generated": "8", "Reading grade level": "0", "Special audience characteristics": "3"}
    return {
        'a': utils.reverse_force_list(value.get('target_audience_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'b': utils.reverse_force_list(value.get('source')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('geographic_coverage_note', '^522[8_].')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    """Geographic Coverage Note."""
    indicator_map1 = {"#": "Geographic coverage", "8": "No display constant generated"}
    return {
        'geographic_coverage_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^522[8_].', 'geographic_coverage_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {"Geographic coverage": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('geographic_coverage_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('preferred_citation_of_described_materials_note', '^524[8_].')
@utils.for_each_value
@utils.filter_values
def preferred_citation_of_described_materials_note(self, key, value):
    """Preferred Citation of Described Materials Note."""
    indicator_map1 = {"#": "Cite as", "8": "No display constant generated"}
    return {
        'preferred_citation_of_described_materials_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'source_of_schema_used': value.get('2'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^524[8_].', 'preferred_citation_of_described_materials_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preferred_citation_of_described_materials_note(self, key, value):
    """Reverse - Preferred Citation of Described Materials Note."""
    indicator_map1 = {"Cite as": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('preferred_citation_of_described_materials_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_schema_used')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('supplement_note', '^525..')
@utils.for_each_value
@utils.filter_values
def supplement_note(self, key, value):
    """Supplement Note."""
    return {
        'supplement_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^525..', 'supplement_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    return {
        'a': utils.reverse_force_list(value.get('supplement_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('study_program_information_note', '^526[0_8].')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    """Study Program Information Note."""
    indicator_map1 = {"0": "Reading program", "8": "No display constant generated"}
    return {
        'program_name': value.get('a'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'reading_level': value.get('c'),
        'interest_level': value.get('b'),
        'title_point_value': value.get('d'),
        'display_text': value.get('i'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^526[0_8].', 'study_program_information_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_study_program_information_note(self, key, value):
    """Reverse - Study Program Information Note."""
    indicator_map1 = {"No display constant generated": "8", "Reading program": "0"}
    return {
        'a': utils.reverse_force_list(value.get('program_name')),
        'x': utils.reverse_force_list(value.get('nonpublic_note')),
        'c': utils.reverse_force_list(value.get('reading_level')),
        'b': utils.reverse_force_list(value.get('interest_level')),
        'd': utils.reverse_force_list(value.get('title_point_value')),
        'i': utils.reverse_force_list(value.get('display_text')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('public_note')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('additional_physical_form_available_note', '^530..')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_available_note(self, key, value):
    """Additional Physical Form Available Note."""
    return {
        'additional_physical_form_available_note': value.get('a'),
        'availability_conditions': value.get('c'),
        'availability_source': value.get('b'),
        'order_number': value.get('d'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^530..', 'additional_physical_form_available_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    return {
        'a': utils.reverse_force_list(value.get('additional_physical_form_available_note')),
        'c': utils.reverse_force_list(value.get('availability_conditions')),
        'b': utils.reverse_force_list(value.get('availability_source')),
        'd': utils.reverse_force_list(value.get('order_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('reproduction_note', '^533..')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    """Reproduction Note."""
    return {
        'type_of_reproduction': value.get('a'),
        'agency_responsible_for_reproduction': utils.force_list(
            value.get('c')
        ),
        'place_of_reproduction': utils.force_list(
            value.get('b')
        ),
        'physical_description_of_reproduction': value.get('e'),
        'date_of_reproduction': value.get('d'),
        'series_statement_of_reproduction': utils.force_list(
            value.get('f')
        ),
        'dates_and_or_sequential_designation_of_issues_reproduced': utils.force_list(
            value.get('m')
        ),
        'note_about_reproduction': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^533..', 'reproduction_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_reproduction_note(self, key, value):
    """Reverse - Reproduction Note."""
    return {
        'a': utils.reverse_force_list(value.get('type_of_reproduction')),
        'c': utils.reverse_force_list(value.get('agency_responsible_for_reproduction')),
        'b': utils.reverse_force_list(value.get('place_of_reproduction')),
        'e': utils.reverse_force_list(value.get('physical_description_of_reproduction')),
        'd': utils.reverse_force_list(value.get('date_of_reproduction')),
        'f': utils.reverse_force_list(value.get('series_statement_of_reproduction')),
        'm': utils.reverse_force_list(value.get('dates_and_or_sequential_designation_of_issues_reproduced')),
        'n': utils.reverse_force_list(value.get('note_about_reproduction')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '7': utils.reverse_force_list(value.get('fixed_length_data_elements_of_reproduction')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('original_version_note', '^534..')
@utils.for_each_value
@utils.filter_values
def original_version_note(self, key, value):
    """Original Version Note."""
    return {
        'main_entry_of_original': value.get('a'),
        'international_standard_serial_number': utils.force_list(
            value.get('x')
        ),
        'publication_distribution_of_original': value.get('c'),
        'edition_statement_of_original': value.get('b'),
        'physical_description_of_original': value.get('e'),
        'series_statement_of_original': utils.force_list(
            value.get('f')
        ),
        'key_title_of_original': utils.force_list(
            value.get('k')
        ),
        'material_specific_details': value.get('m'),
        'location_of_original': value.get('l'),
        'other_resource_identifier': utils.force_list(
            value.get('o')
        ),
        'note_about_original': utils.force_list(
            value.get('n')
        ),
        'introductory_phrase': value.get('p'),
        'materials_specified': value.get('3'),
        'title_statement_of_original': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('^534..', 'original_version_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_version_note(self, key, value):
    """Reverse - Original Version Note."""
    return {
        'a': utils.reverse_force_list(value.get('main_entry_of_original')),
        'x': utils.reverse_force_list(value.get('international_standard_serial_number')),
        'c': utils.reverse_force_list(value.get('publication_distribution_of_original')),
        'b': utils.reverse_force_list(value.get('edition_statement_of_original')),
        'e': utils.reverse_force_list(value.get('physical_description_of_original')),
        'f': utils.reverse_force_list(value.get('series_statement_of_original')),
        'k': utils.reverse_force_list(value.get('key_title_of_original')),
        'm': utils.reverse_force_list(value.get('material_specific_details')),
        'l': utils.reverse_force_list(value.get('location_of_original')),
        'o': utils.reverse_force_list(value.get('other_resource_identifier')),
        'n': utils.reverse_force_list(value.get('note_about_original')),
        'p': utils.reverse_force_list(value.get('introductory_phrase')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        't': utils.reverse_force_list(value.get('title_statement_of_original')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
    }


@marc21.over('location_of_originals_duplicates_note', '^535[1_2].')
@utils.for_each_value
@utils.filter_values
def location_of_originals_duplicates_note(self, key, value):
    """Location of Originals/Duplicates Note."""
    indicator_map1 = {"1": "Holder of originals", "2": "Holder of duplicates"}
    return {
        'custodian': value.get('a'),
        'country': utils.force_list(
            value.get('c')
        ),
        'postal_address': utils.force_list(
            value.get('b')
        ),
        'telecommunications_address': utils.force_list(
            value.get('d')
        ),
        'repository_location_code': value.get('g'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'custodial_role': indicator_map1.get(key[3]),
    }


@tomarc21.over('^535[1_2].', 'location_of_originals_duplicates_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_originals_duplicates_note(self, key, value):
    """Reverse - Location of Originals/Duplicates Note."""
    indicator_map1 = {"Holder of duplicates": "2", "Holder of originals": "1"}
    return {
        'a': utils.reverse_force_list(value.get('custodian')),
        'c': utils.reverse_force_list(value.get('country')),
        'b': utils.reverse_force_list(value.get('postal_address')),
        'd': utils.reverse_force_list(value.get('telecommunications_address')),
        'g': utils.reverse_force_list(value.get('repository_location_code')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('custodial_role')),
    }


@marc21.over('funding_information_note', '^536..')
@utils.for_each_value
@utils.filter_values
def funding_information_note(self, key, value):
    """Funding Information Note."""
    return {
        'text_of_note': value.get('a'),
        'grant_number': utils.force_list(
            value.get('c')
        ),
        'contract_number': utils.force_list(
            value.get('b')
        ),
        'program_element_number': utils.force_list(
            value.get('e')
        ),
        'undifferentiated_number': utils.force_list(
            value.get('d')
        ),
        'task_number': utils.force_list(
            value.get('g')
        ),
        'project_number': utils.force_list(
            value.get('f')
        ),
        'work_unit_number': utils.force_list(
            value.get('h')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^536..', 'funding_information_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_funding_information_note(self, key, value):
    """Reverse - Funding Information Note."""
    return {
        'a': utils.reverse_force_list(value.get('text_of_note')),
        'c': utils.reverse_force_list(value.get('grant_number')),
        'b': utils.reverse_force_list(value.get('contract_number')),
        'e': utils.reverse_force_list(value.get('program_element_number')),
        'd': utils.reverse_force_list(value.get('undifferentiated_number')),
        'g': utils.reverse_force_list(value.get('task_number')),
        'f': utils.reverse_force_list(value.get('project_number')),
        'h': utils.reverse_force_list(value.get('work_unit_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('system_details_note', '^538..')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    """System Details Note."""
    return {
        'system_details_note': value.get('a'),
        'display_text': value.get('i'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@tomarc21.over('^538..', 'system_details_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_note(self, key, value):
    """Reverse - System Details Note."""
    return {
        'a': utils.reverse_force_list(value.get('system_details_note')),
        'i': utils.reverse_force_list(value.get('display_text')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
    }


@marc21.over('terms_governing_use_and_reproduction_note', '^540..')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    return {
        'terms_governing_use_and_reproduction': value.get('a'),
        'authorization': value.get('c'),
        'jurisdiction': value.get('b'),
        'authorized_users': value.get('d'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@tomarc21.over('^540..', 'terms_governing_use_and_reproduction_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_terms_governing_use_and_reproduction_note(self, key, value):
    """Reverse - Terms Governing Use and Reproduction Note."""
    return {
        'a': utils.reverse_force_list(value.get('terms_governing_use_and_reproduction')),
        'c': utils.reverse_force_list(value.get('authorization')),
        'b': utils.reverse_force_list(value.get('jurisdiction')),
        'd': utils.reverse_force_list(value.get('authorized_users')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
    }


@marc21.over('immediate_source_of_acquisition_note', '^541[10_].')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    indicator_map1 = {"#": "No information provided", "0": "Private", "1": "Not private"}
    return {
        'source_of_acquisition': value.get('a'),
        'method_of_acquisition': value.get('c'),
        'address': value.get('b'),
        'accession_number': value.get('e'),
        'date_of_acquisition': value.get('d'),
        'owner': value.get('f'),
        'purchase_price': value.get('h'),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@tomarc21.over('^541[10_].', 'immediate_source_of_acquisition_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_immediate_source_of_acquisition_note(self, key, value):
    """Reverse - Immediate Source of Acquisition Note."""
    indicator_map1 = {"No information provided": "#", "Not private": "1", "Private": "0"}
    return {
        'a': utils.reverse_force_list(value.get('source_of_acquisition')),
        'c': utils.reverse_force_list(value.get('method_of_acquisition')),
        'b': utils.reverse_force_list(value.get('address')),
        'e': utils.reverse_force_list(value.get('accession_number')),
        'd': utils.reverse_force_list(value.get('date_of_acquisition')),
        'f': utils.reverse_force_list(value.get('owner')),
        'h': utils.reverse_force_list(value.get('purchase_price')),
        'o': utils.reverse_force_list(value.get('type_of_unit')),
        'n': utils.reverse_force_list(value.get('extent')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('privacy')),
    }


@marc21.over('information_relating_to_copyright_status', '^542[10_].')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    """Information Relating to Copyright Status."""
    indicator_map1 = {"#": "No information provided", "0": "Private", "1": "Not private"}
    return {
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'personal_creator': value.get('a'),
        'corporate_creator': value.get('c'),
        'personal_creator_death_date': value.get('b'),
        'copyright_holder_contact_information': utils.force_list(
            value.get('e')
        ),
        'copyright_holder': utils.force_list(
            value.get('d')
        ),
        'copyright_date': value.get('g'),
        'copyright_statement': utils.force_list(
            value.get('f')
        ),
        'publication_date': value.get('i'),
        'copyright_renewal_date': utils.force_list(
            value.get('h')
        ),
        'publisher': utils.force_list(
            value.get('k')
        ),
        'creation_date': value.get('j'),
        'publication_status': value.get('m'),
        'copyright_status': value.get('l'),
        'research_date': value.get('o'),
        'note': utils.force_list(
            value.get('n')
        ),
        'supplying_agency': value.get('q'),
        'country_of_publication_or_creation': utils.force_list(
            value.get('p')
        ),
        'source_of_information': value.get('s'),
        'jurisdiction_of_copyright_assessment': value.get('r'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@tomarc21.over('^542[10_].', 'information_relating_to_copyright_status')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_relating_to_copyright_status(self, key, value):
    """Reverse - Information Relating to Copyright Status."""
    indicator_map1 = {"No information provided": "#", "Not private": "1", "Private": "0"}
    return {
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'a': utils.reverse_force_list(value.get('personal_creator')),
        'c': utils.reverse_force_list(value.get('corporate_creator')),
        'b': utils.reverse_force_list(value.get('personal_creator_death_date')),
        'e': utils.reverse_force_list(value.get('copyright_holder_contact_information')),
        'd': utils.reverse_force_list(value.get('copyright_holder')),
        'g': utils.reverse_force_list(value.get('copyright_date')),
        'f': utils.reverse_force_list(value.get('copyright_statement')),
        'i': utils.reverse_force_list(value.get('publication_date')),
        'h': utils.reverse_force_list(value.get('copyright_renewal_date')),
        'k': utils.reverse_force_list(value.get('publisher')),
        'j': utils.reverse_force_list(value.get('creation_date')),
        'm': utils.reverse_force_list(value.get('publication_status')),
        'l': utils.reverse_force_list(value.get('copyright_status')),
        'o': utils.reverse_force_list(value.get('research_date')),
        'n': utils.reverse_force_list(value.get('note')),
        'q': utils.reverse_force_list(value.get('supplying_agency')),
        'p': utils.reverse_force_list(value.get('country_of_publication_or_creation')),
        's': utils.reverse_force_list(value.get('source_of_information')),
        'r': utils.reverse_force_list(value.get('jurisdiction_of_copyright_assessment')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '_indicator1': indicator_map1.get(value.get('privacy')),
    }


@marc21.over('location_of_other_archival_materials_note', '^544[10_].')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    """Location of Other Archival Materials Note."""
    indicator_map1 = {"#": "No information provided", "0": "Associated materials", "1": "Related materials"}
    return {
        'custodian': utils.force_list(
            value.get('a')
        ),
        'country': utils.force_list(
            value.get('c')
        ),
        'address': utils.force_list(
            value.get('b')
        ),
        'provenance': utils.force_list(
            value.get('e')
        ),
        'title': utils.force_list(
            value.get('d')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'relationship': indicator_map1.get(key[3]),
    }


@tomarc21.over('^544[10_].', 'location_of_other_archival_materials_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {"Associated materials": "0", "No information provided": "#", "Related materials": "1"}
    return {
        'a': utils.reverse_force_list(value.get('custodian')),
        'c': utils.reverse_force_list(value.get('country')),
        'b': utils.reverse_force_list(value.get('address')),
        'e': utils.reverse_force_list(value.get('provenance')),
        'd': utils.reverse_force_list(value.get('title')),
        'n': utils.reverse_force_list(value.get('note')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('relationship')),
    }


@marc21.over('biographical_or_historical_data', '^545[10_].')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {"#": "No information provided", "0": "Biographical sketch", "1": "Administrative history"}
    return {
        'biographical_or_historical_data': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'expansion': value.get('b'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'type_of_data': indicator_map1.get(key[3]),
    }


@tomarc21.over('^545[10_].', 'biographical_or_historical_data')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {"Administrative history": "1", "Biographical sketch": "0", "No information provided": "#"}
    return {
        'a': utils.reverse_force_list(value.get('biographical_or_historical_data')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'b': utils.reverse_force_list(value.get('expansion')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('type_of_data')),
    }


@marc21.over('language_note', '^546..')
@utils.for_each_value
@utils.filter_values
def language_note(self, key, value):
    """Language Note."""
    return {
        'language_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'information_code_or_alphabet': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^546..', 'language_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_note(self, key, value):
    """Reverse - Language Note."""
    return {
        'a': utils.reverse_force_list(value.get('language_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'b': utils.reverse_force_list(value.get('information_code_or_alphabet')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('former_title_complexity_note', '^547..')
@utils.for_each_value
@utils.filter_values
def former_title_complexity_note(self, key, value):
    """Former Title Complexity Note."""
    return {
        'former_title_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^547..', 'former_title_complexity_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title_complexity_note(self, key, value):
    """Reverse - Former Title Complexity Note."""
    return {
        'a': utils.reverse_force_list(value.get('former_title_complexity_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('issuing_body_note', '^550..')
@utils.for_each_value
@utils.filter_values
def issuing_body_note(self, key, value):
    """Issuing Body Note."""
    return {
        'issuing_body_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^550..', 'issuing_body_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issuing_body_note(self, key, value):
    """Reverse - Issuing Body Note."""
    return {
        'a': utils.reverse_force_list(value.get('issuing_body_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('entity_and_attribute_information_note', '^552..')
@utils.for_each_value
@utils.filter_values
def entity_and_attribute_information_note(self, key, value):
    """Entity and Attribute Information Note."""
    return {
        'entity_type_label': value.get('a'),
        'attribute_label': value.get('c'),
        'entity_type_definition_and_source': value.get('b'),
        'enumerated_domain_value': utils.force_list(
            value.get('e')
        ),
        'attribute_definition_and_source': value.get('d'),
        'range_domain_minimum_and_maximum': value.get('g'),
        'enumerated_domain_value_definition_and_source': utils.force_list(
            value.get('f')
        ),
        'unrepresentable_domain': value.get('i'),
        'codeset_name_and_source': value.get('h'),
        'beginning_and_ending_date_of_attribute_values': value.get('k'),
        'attribute_units_of_measurement_and_resolution': value.get('j'),
        'attribute_value_accuracy_explanation': value.get('m'),
        'attribute_value_accuracy': value.get('l'),
        'entity_and_attribute_overview': utils.force_list(
            value.get('o')
        ),
        'attribute_measurement_frequency': value.get('n'),
        'entity_and_attribute_detail_citation': utils.force_list(
            value.get('p')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_note': utils.force_list(
            value.get('z')
        ),
    }


@tomarc21.over('^552..', 'entity_and_attribute_information_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_entity_and_attribute_information_note(self, key, value):
    """Reverse - Entity and Attribute Information Note."""
    return {
        'a': utils.reverse_force_list(value.get('entity_type_label')),
        'c': utils.reverse_force_list(value.get('attribute_label')),
        'b': utils.reverse_force_list(value.get('entity_type_definition_and_source')),
        'e': utils.reverse_force_list(value.get('enumerated_domain_value')),
        'd': utils.reverse_force_list(value.get('attribute_definition_and_source')),
        'g': utils.reverse_force_list(value.get('range_domain_minimum_and_maximum')),
        'f': utils.reverse_force_list(value.get('enumerated_domain_value_definition_and_source')),
        'i': utils.reverse_force_list(value.get('unrepresentable_domain')),
        'h': utils.reverse_force_list(value.get('codeset_name_and_source')),
        'k': utils.reverse_force_list(value.get('beginning_and_ending_date_of_attribute_values')),
        'j': utils.reverse_force_list(value.get('attribute_units_of_measurement_and_resolution')),
        'm': utils.reverse_force_list(value.get('attribute_value_accuracy_explanation')),
        'l': utils.reverse_force_list(value.get('attribute_value_accuracy')),
        'o': utils.reverse_force_list(value.get('entity_and_attribute_overview')),
        'n': utils.reverse_force_list(value.get('attribute_measurement_frequency')),
        'p': utils.reverse_force_list(value.get('entity_and_attribute_detail_citation')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('display_note')),
    }


@marc21.over('cumulative_index_finding_aids_note', '^555[0_8].')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    """Cumulative Index/Finding Aids Note."""
    indicator_map1 = {"#": "Indexes", "0": "Finding aids", "8": "No display constant generated"}
    return {
        'cumulative_index_finding_aids_note': value.get('a'),
        'degree_of_control': value.get('c'),
        'availability_source': utils.force_list(
            value.get('b')
        ),
        'bibliographic_reference': value.get('d'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^555[0_8].', 'cumulative_index_finding_aids_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {"Finding aids": "0", "Indexes": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('cumulative_index_finding_aids_note')),
        'c': utils.reverse_force_list(value.get('degree_of_control')),
        'b': utils.reverse_force_list(value.get('availability_source')),
        'd': utils.reverse_force_list(value.get('bibliographic_reference')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('information_about_documentation_note', '^556[8_].')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    """Information About Documentation Note."""
    indicator_map1 = {"#": "Documentation", "8": "No display constant generated"}
    return {
        'information_about_documentation_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^556[8_].', 'information_about_documentation_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {"Documentation": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('information_about_documentation_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('ownership_and_custodial_history', '^561[10_].')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {"#": "No information provided", "0": "Private", "1": "Not private"}
    return {
        'history': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@tomarc21.over('^561[10_].', 'ownership_and_custodial_history')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {"No information provided": "#", "Not private": "1", "Private": "0"}
    return {
        'a': utils.reverse_force_list(value.get('history')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '_indicator1': indicator_map1.get(value.get('privacy')),
    }


@marc21.over('copy_and_version_identification_note', '^562..')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    """Copy and Version Identification Note."""
    return {
        'identifying_markings': utils.force_list(
            value.get('a')
        ),
        'version_identification': utils.force_list(
            value.get('c')
        ),
        'copy_identification': utils.force_list(
            value.get('b')
        ),
        'number_of_copies': utils.force_list(
            value.get('e')
        ),
        'presentation_format': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^562..', 'copy_and_version_identification_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copy_and_version_identification_note(self, key, value):
    """Reverse - Copy and Version Identification Note."""
    return {
        'a': utils.reverse_force_list(value.get('identifying_markings')),
        'c': utils.reverse_force_list(value.get('version_identification')),
        'b': utils.reverse_force_list(value.get('copy_identification')),
        'e': utils.reverse_force_list(value.get('number_of_copies')),
        'd': utils.reverse_force_list(value.get('presentation_format')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('binding_information', '^563..')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    """Binding Information."""
    return {
        'binding_note': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
    }


@tomarc21.over('^563..', 'binding_information')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_binding_information(self, key, value):
    """Reverse - Binding Information."""
    return {
        'a': utils.reverse_force_list(value.get('binding_note')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
    }


@marc21.over('case_file_characteristics_note', '^565[0_8].')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    """Case File Characteristics Note."""
    indicator_map1 = {"#": "File size", "0": "Case file characteristics", "8": "No display constant generated"}
    return {
        'number_of_cases_variables': value.get('a'),
        'unit_of_analysis': utils.force_list(
            value.get('c')
        ),
        'name_of_variable': utils.force_list(
            value.get('b')
        ),
        'filing_scheme_or_code': utils.force_list(
            value.get('e')
        ),
        'universe_of_data': utils.force_list(
            value.get('d')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^565[0_8].', 'case_file_characteristics_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_case_file_characteristics_note(self, key, value):
    """Reverse - Case File Characteristics Note."""
    indicator_map1 = {"Case file characteristics": "0", "File size": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('number_of_cases_variables')),
        'c': utils.reverse_force_list(value.get('unit_of_analysis')),
        'b': utils.reverse_force_list(value.get('name_of_variable')),
        'e': utils.reverse_force_list(value.get('filing_scheme_or_code')),
        'd': utils.reverse_force_list(value.get('universe_of_data')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('methodology_note', '^567[8_].')
@utils.for_each_value
@utils.filter_values
def methodology_note(self, key, value):
    """Methodology Note."""
    indicator_map1 = {"#": "Methodology", "8": "No display constant generated"}
    return {
        'methodology_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^567[8_].', 'methodology_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_methodology_note(self, key, value):
    """Reverse - Methodology Note."""
    indicator_map1 = {"Methodology": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('methodology_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('linking_entry_complexity_note', '^580..')
@utils.for_each_value
@utils.filter_values
def linking_entry_complexity_note(self, key, value):
    """Linking Entry Complexity Note."""
    return {
        'linking_entry_complexity_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@tomarc21.over('^580..', 'linking_entry_complexity_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    return {
        'a': utils.reverse_force_list(value.get('linking_entry_complexity_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('publications_about_described_materials_note', '^581[8_].')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    """Publications About Described Materials Note."""
    indicator_map1 = {"#": "Publications", "8": "No display constant generated"}
    return {
        'publications_about_described_materials_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'international_standard_book_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^581[8_].', 'publications_about_described_materials_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publications_about_described_materials_note(self, key, value):
    """Reverse - Publications About Described Materials Note."""
    indicator_map1 = {"No display constant generated": "8", "Publications": "#"}
    return {
        'a': utils.reverse_force_list(value.get('publications_about_described_materials_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        'z': utils.reverse_force_list(value.get('international_standard_book_number')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('action_note', '^583[10_].')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    indicator_map1 = {"#": "No information provided", "0": "Private", "1": "Not private"}
    return {
        'action': value.get('a'),
        'nonpublic_note': utils.force_list(
            value.get('x')
        ),
        'time_date_of_action': utils.force_list(
            value.get('c')
        ),
        'action_identification': utils.force_list(
            value.get('b')
        ),
        'contingency_for_action': utils.force_list(
            value.get('e')
        ),
        'action_interval': utils.force_list(
            value.get('d')
        ),
        'authorization': utils.force_list(
            value.get('f')
        ),
        'method_of_action': utils.force_list(
            value.get('i')
        ),
        'jurisdiction': utils.force_list(
            value.get('h')
        ),
        'action_agent': utils.force_list(
            value.get('k')
        ),
        'site_of_action': utils.force_list(
            value.get('j')
        ),
        'status': utils.force_list(
            value.get('l')
        ),
        'type_of_unit': utils.force_list(
            value.get('o')
        ),
        'extent': utils.force_list(
            value.get('n')
        ),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'privacy': indicator_map1.get(key[3]),
    }


@tomarc21.over('^583[10_].', 'action_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {"No information provided": "#", "Not private": "1", "Private": "0"}
    return {
        'a': utils.reverse_force_list(value.get('action')),
        'x': utils.reverse_force_list(value.get('nonpublic_note')),
        'c': utils.reverse_force_list(value.get('time_date_of_action')),
        'b': utils.reverse_force_list(value.get('action_identification')),
        'e': utils.reverse_force_list(value.get('contingency_for_action')),
        'd': utils.reverse_force_list(value.get('action_interval')),
        'f': utils.reverse_force_list(value.get('authorization')),
        'i': utils.reverse_force_list(value.get('method_of_action')),
        'h': utils.reverse_force_list(value.get('jurisdiction')),
        'k': utils.reverse_force_list(value.get('action_agent')),
        'j': utils.reverse_force_list(value.get('site_of_action')),
        'l': utils.reverse_force_list(value.get('status')),
        'o': utils.reverse_force_list(value.get('type_of_unit')),
        'n': utils.reverse_force_list(value.get('extent')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '2': utils.reverse_force_list(value.get('source_of_term')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(value.get('public_note')),
        'u': utils.reverse_force_list(value.get('uniform_resource_identifier')),
        '_indicator1': indicator_map1.get(value.get('privacy')),
    }


@marc21.over('accumulation_and_frequency_of_use_note', '^584..')
@utils.for_each_value
@utils.filter_values
def accumulation_and_frequency_of_use_note(self, key, value):
    """Accumulation and Frequency of Use Note."""
    return {
        'accumulation': utils.force_list(
            value.get('a')
        ),
        'frequency_of_use': utils.force_list(
            value.get('b')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@tomarc21.over('^584..', 'accumulation_and_frequency_of_use_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_accumulation_and_frequency_of_use_note(self, key, value):
    """Reverse - Accumulation and Frequency of Use Note."""
    return {
        'a': utils.reverse_force_list(value.get('accumulation')),
        'b': utils.reverse_force_list(value.get('frequency_of_use')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
    }


@marc21.over('exhibitions_note', '^585..')
@utils.for_each_value
@utils.filter_values
def exhibitions_note(self, key, value):
    """Exhibitions Note."""
    return {
        'exhibitions_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^585..', 'exhibitions_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_exhibitions_note(self, key, value):
    """Reverse - Exhibitions Note."""
    return {
        'a': utils.reverse_force_list(value.get('exhibitions_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }


@marc21.over('awards_note', '^586[8_].')
@utils.for_each_value
@utils.filter_values
def awards_note(self, key, value):
    """Awards Note."""
    indicator_map1 = {"#": "Awards", "8": "No display constant generated"}
    return {
        'awards_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }


@tomarc21.over('^586[8_].', 'awards_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_awards_note(self, key, value):
    """Reverse - Awards Note."""
    indicator_map1 = {"Awards": "#", "No display constant generated": "8"}
    return {
        'a': utils.reverse_force_list(value.get('awards_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '3': utils.reverse_force_list(value.get('materials_specified')),
        '6': utils.reverse_force_list(value.get('linkage')),
        '_indicator1': indicator_map1.get(value.get('display_constant_controller')),
    }


@marc21.over('source_of_description_note', '^588..')
@utils.for_each_value
@utils.filter_values
def source_of_description_note(self, key, value):
    """Source of Description Note."""
    return {
        'source_of_description_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }


@tomarc21.over('^588..', 'source_of_description_note')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    return {
        'a': utils.reverse_force_list(value.get('source_of_description_note')),
        '8': utils.reverse_force_list(value.get('field_link_and_sequence_number')),
        '5': utils.reverse_force_list(value.get('institution_to_which_field_applies')),
        '6': utils.reverse_force_list(value.get('linkage')),
    }
