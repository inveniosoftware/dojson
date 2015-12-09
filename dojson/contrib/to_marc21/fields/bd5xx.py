# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('500', '^general_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_general_note(self, key, value):
    """Reverse - General Note."""
    return {
        'a': value.get('general_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('501', '^with_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_with_note(self, key, value):
    """Reverse - With Note."""
    return {
        'a': value.get('with_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('502', '^dissertation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_dissertation_note(self, key, value):
    """Reverse - Dissertation Note."""
    return {
        'a': value.get('dissertation_note'),
        'c': value.get('name_of_granting_institution'),
        'b': value.get('degree_type'),
        'd': value.get('year_degree_granted'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'o': utils.reverse_force_list(
            value.get('dissertation_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('504', '^bibliography_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_bibliography_note(self, key, value):
    """Reverse - Bibliography, Etc. Note."""
    return {
        'a': value.get('bibliography_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('number_of_references'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('505', '^formatted_contents_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_formatted_contents_note(self, key, value):
    """Reverse - Formatted Contents Note."""
    indicator_map1 = {
        "Contents": "0",
        "Incomplete contents": "1",
        "No display constant generated": "8",
        "Partial contents": "2"}
    indicator_map2 = {"Basic": "_", "Enhanced": "0"}
    return {
        'a': value.get('formatted_contents_note'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'r': utils.reverse_force_list(
            value.get('statement_of_responsibility')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        't': utils.reverse_force_list(
            value.get('title')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('display_constant_controller'), '_'),
        '$ind2': indicator_map2.get(value.get('level_of_content_designation'), '_'),
    }


@to_marc21.over('506', '^restrictions_on_access_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_restrictions_on_access_note(self, key, value):
    """Reverse - Restrictions on Access Note."""
    indicator_map1 = {
        "No information provided": "_",
        "No restrictions": "0",
        "Restrictions apply": "1"}
    return {
        'a': value.get('terms_governing_access'),
        'c': utils.reverse_force_list(
            value.get('physical_access_provisions')
        ),
        'b': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'e': utils.reverse_force_list(
            value.get('authorization')
        ),
        'd': utils.reverse_force_list(
            value.get('authorized_users')
        ),
        'f': utils.reverse_force_list(
            value.get('standardized_terminology_for_access_restriction')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('restriction'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('507', '^scale_note_for_graphic_material$')
@utils.filter_values
def reverse_scale_note_for_graphic_material(self, key, value):
    """Reverse - Scale Note for Graphic Material."""
    return {
        'a': value.get('representative_fraction_of_scale_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('remainder_of_scale_note'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('508', '^creation_production_credits_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_creation_production_credits_note(self, key, value):
    """Reverse - Creation/Production Credits Note."""
    return {
        'a': value.get('creation_production_credits_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('510', '^citation_references_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_citation_references_note(self, key, value):
    """Reverse - Citation/References Note."""
    indicator_map1 = {
        "Coverage complete": "1",
        "Coverage is selective": "2",
        "Coverage unknown": "0",
        "Location in source given": "4",
        "Location in source not given": "3"}
    return {
        'a': value.get('name_of_source'),
        'x': value.get('international_standard_serial_number'),
        'c': value.get('location_within_source'),
        'b': value.get('coverage_of_source'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('coverage_location_in_source'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('511', '^participant_or_performer_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_participant_or_performer_note(self, key, value):
    """Reverse - Participant or Performer Note."""
    indicator_map1 = {"Cast": "1", "No display constant generated": "0"}
    return {
        'a': value.get('participant_or_performer_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('513', '^type_of_report_and_period_covered_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_report_and_period_covered_note(self, key, value):
    """Reverse - Type of Report and Period Covered Note."""
    return {
        'a': value.get('type_of_report'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('period_covered'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('514', '^data_quality_note$')
@utils.filter_values
def reverse_data_quality_note(self, key, value):
    """Reverse - Data Quality Note."""
    return {
        'a': value.get('attribute_accuracy_report'),
        'c': utils.reverse_force_list(
            value.get('attribute_accuracy_explanation')
        ),
        'b': utils.reverse_force_list(
            value.get('attribute_accuracy_value')
        ),
        'e': value.get('completeness_report'),
        'd': value.get('logical_consistency_report'),
        'g': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_value')
        ),
        'f': value.get('horizontal_position_accuracy_report'),
        'i': value.get('vertical_positional_accuracy_report'),
        'h': utils.reverse_force_list(
            value.get('horizontal_position_accuracy_explanation')
        ),
        'k': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_explanation')
        ),
        'j': utils.reverse_force_list(
            value.get('vertical_positional_accuracy_value')
        ),
        'm': value.get('cloud_cover'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('515', '^numbering_peculiarities_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_numbering_peculiarities_note(self, key, value):
    """Reverse - Numbering Peculiarities Note."""
    return {
        'a': value.get('numbering_peculiarities_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('516', '^type_of_computer_file_or_data_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_type_of_computer_file_or_data_note(self, key, value):
    """Reverse - Type of Computer File or Data Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Type of file": "_"}
    return {
        'a': value.get('type_of_computer_file_or_data_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('518', '^date_time_and_place_of_an_event_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_date_time_and_place_of_an_event_note(self, key, value):
    """Reverse - Date/Time and Place of an Event Note."""
    return {
        'a': value.get('date_time_and_place_of_an_event_note'),
        'd': utils.reverse_force_list(
            value.get('date_of_event')
        ),
        'p': utils.reverse_force_list(
            value.get('place_of_event')
        ),
        'o': utils.reverse_force_list(
            value.get('other_event_information')
        ),
        '0': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': utils.reverse_force_list(
            value.get('source_of_term')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('520', '^summary$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_summary(self, key, value):
    """Reverse - Summary, Etc.."""
    indicator_map1 = {
        "Abstract": "3",
        "Content advice": "4",
        "No display constant generated": "8",
        "Review": "1",
        "Scope and content": "2",
        "Subject": "0",
        "Summary": "_"}
    return {
        'a': value.get('summary'),
        'c': value.get('assigning_source'),
        'b': value.get('expansion_of_summary_note'),
        '3': value.get('materials_specified'),
        '2': value.get('source'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('521', '^target_audience_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_target_audience_note(self, key, value):
    """Reverse - Target Audience Note."""
    indicator_map1 = {
        "Audience": "_",
        "Interest age level": "1",
        "Interest grade level": "2",
        "Motivation/interest level": "4",
        "No display constant generated": "8",
        "Reading grade level": "0",
        "Special audience characteristics": "3"}
    return {
        'a': utils.reverse_force_list(
            value.get('target_audience_note')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '3': value.get('materials_specified'),
        'b': value.get('source'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('522', '^geographic_coverage_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_geographic_coverage_note(self, key, value):
    """Reverse - Geographic Coverage Note."""
    indicator_map1 = {
        "Geographic coverage": "_",
        "No display constant generated": "8"}
    return {
        'a': value.get('geographic_coverage_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('524', '^preferred_citation_of_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preferred_citation_of_described_materials_note(self, key, value):
    """Reverse - Preferred Citation of Described Materials Note."""
    indicator_map1 = {"Cite as": "_", "No display constant generated": "8"}
    return {
        'a': value.get('preferred_citation_of_described_materials_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_schema_used'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('525', '^supplement_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_note(self, key, value):
    """Reverse - Supplement Note."""
    return {
        'a': value.get('supplement_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('526', '^study_program_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_study_program_information_note(self, key, value):
    """Reverse - Study Program Information Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Reading program": "0"}
    return {
        'a': value.get('program_name'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')),
        'c': value.get('reading_level'),
        'b': value.get('interest_level'),
        'd': value.get('title_point_value'),
        'i': value.get('display_text'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(
            value.get('public_note')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('530', '^additional_physical_form_available_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_available_note(self, key, value):
    """Reverse - Additional Physical Form Available Note."""
    return {
        'a': value.get('additional_physical_form_available_note'),
        'c': value.get('availability_conditions'),
        'b': value.get('availability_source'),
        'd': value.get('order_number'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('533', '^reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_reproduction_note(self, key, value):
    """Reverse - Reproduction Note."""
    return {
        'a': value.get('type_of_reproduction'),
        'c': utils.reverse_force_list(
            value.get('agency_responsible_for_reproduction')
        ),
        'b': utils.reverse_force_list(
            value.get('place_of_reproduction')
        ),
        'e': value.get('physical_description_of_reproduction'),
        'd': value.get('date_of_reproduction'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_reproduction')
        ),
        'm': utils.reverse_force_list(
            value.get('dates_and_or_sequential_designation_of_issues_reproduced')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_reproduction')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '7': value.get('fixed_length_data_elements_of_reproduction'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('534', '^original_version_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_version_note(self, key, value):
    """Reverse - Original Version Note."""
    return {
        'a': value.get('main_entry_of_original'),
        'x': utils.reverse_force_list(
            value.get('international_standard_serial_number')
        ),
        'c': value.get('publication_distribution_of_original'),
        'b': value.get('edition_statement_of_original'),
        'e': value.get('physical_description_of_original'),
        'f': utils.reverse_force_list(
            value.get('series_statement_of_original')
        ),
        'k': utils.reverse_force_list(
            value.get('key_title_of_original')
        ),
        'm': value.get('material_specific_details'),
        'l': value.get('location_of_original'),
        'o': utils.reverse_force_list(
            value.get('other_resource_identifier')
        ),
        'n': utils.reverse_force_list(
            value.get('note_about_original')
        ),
        'p': value.get('introductory_phrase'),
        '3': value.get('materials_specified'),
        't': value.get('title_statement_of_original'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('535', '^location_of_originals_duplicates_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_originals_duplicates_note(self, key, value):
    """Reverse - Location of Originals/Duplicates Note."""
    indicator_map1 = {"Holder of duplicates": "2", "Holder of originals": "1"}
    return {
        'a': value.get('custodian'),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'b': utils.reverse_force_list(
            value.get('postal_address')
        ),
        'd': utils.reverse_force_list(
            value.get('telecommunications_address')
        ),
        'g': value.get('repository_location_code'),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('custodial_role'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('536', '^funding_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_funding_information_note(self, key, value):
    """Reverse - Funding Information Note."""
    return {
        'a': value.get('text_of_note'),
        'c': utils.reverse_force_list(
            value.get('grant_number')
        ),
        'b': utils.reverse_force_list(
            value.get('contract_number')
        ),
        'e': utils.reverse_force_list(
            value.get('program_element_number')
        ),
        'd': utils.reverse_force_list(
            value.get('undifferentiated_number')
        ),
        'g': utils.reverse_force_list(
            value.get('task_number')
        ),
        'f': utils.reverse_force_list(
            value.get('project_number')
        ),
        'h': utils.reverse_force_list(
            value.get('work_unit_number')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('538', '^system_details_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_system_details_note(self, key, value):
    """Reverse - System Details Note."""
    return {
        'a': value.get('system_details_note'),
        'i': value.get('display_text'),
        '3': value.get('materials_specified'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('540', '^terms_governing_use_and_reproduction_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_terms_governing_use_and_reproduction_note(self, key, value):
    """Reverse - Terms Governing Use and Reproduction Note."""
    field_map = {
        'terms_governing_use_and_reproduction': 'a',
        'authorization': 'c',
        'jurisdiction': 'b',
        'authorized_users': 'd',
        'materials_specified': '3',
        'institution_to_which_field_applies': '5',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'uniform_resource_identifier': 'u',
    }
    return {
        'a': value.get('terms_governing_use_and_reproduction'),
        'c': value.get('authorization'),
        'b': value.get('jurisdiction'),
        'd': value.get('authorized_users'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': '_',
        '$ind2': '_',
        '__order__': tuple([field_map[k] for k in value['__order__']]) if '__order__' in value else None,
    }


@to_marc21.over('541', '^immediate_source_of_acquisition_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_immediate_source_of_acquisition_note(self, key, value):
    """Reverse - Immediate Source of Acquisition Note."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    return {
        'a': value.get('source_of_acquisition'),
        'c': value.get('method_of_acquisition'),
        'b': value.get('address'),
        'e': value.get('accession_number'),
        'd': value.get('date_of_acquisition'),
        'f': value.get('owner'),
        'h': value.get('purchase_price'),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('542', '^information_relating_to_copyright_status$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_relating_to_copyright_status(self, key, value):
    """Reverse - Information Relating to Copyright Status."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    return {
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('personal_creator'),
        'c': value.get('corporate_creator'),
        'b': value.get('personal_creator_death_date'),
        'e': utils.reverse_force_list(
            value.get('copyright_holder_contact_information')
        ),
        'd': utils.reverse_force_list(
            value.get('copyright_holder')
        ),
        'g': value.get('copyright_date'),
        'f': utils.reverse_force_list(
            value.get('copyright_statement')
        ),
        'i': value.get('publication_date'),
        'h': utils.reverse_force_list(
            value.get('copyright_renewal_date')
        ),
        'k': utils.reverse_force_list(
            value.get('publisher')
        ),
        'j': value.get('creation_date'),
        'm': value.get('publication_status'),
        'l': value.get('copyright_status'),
        'o': value.get('research_date'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'q': value.get('supplying_agency'),
        'p': utils.reverse_force_list(
            value.get('country_of_publication_or_creation')
        ),
        's': value.get('source_of_information'),
        'r': value.get('jurisdiction_of_copyright_assessment'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('544', '^location_of_other_archival_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_location_of_other_archival_materials_note(self, key, value):
    """Reverse - Location of Other Archival Materials Note."""
    indicator_map1 = {
        "Associated materials": "0",
        "No information provided": "_",
        "Related materials": "1"}
    return {
        'a': utils.reverse_force_list(
            value.get('custodian')
        ),
        'c': utils.reverse_force_list(
            value.get('country')
        ),
        'b': utils.reverse_force_list(
            value.get('address')
        ),
        'e': utils.reverse_force_list(
            value.get('provenance')
        ),
        'd': utils.reverse_force_list(
            value.get('title')
        ),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('relationship'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('545', '^biographical_or_historical_data$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_biographical_or_historical_data(self, key, value):
    """Reverse - Biographical or Historical Data."""
    indicator_map1 = {
        "Administrative history": "1",
        "Biographical sketch": "0",
        "No information provided": "_"}
    return {
        'a': value.get('biographical_or_historical_data'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('expansion'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('type_of_data'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('546', '^language_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_language_note(self, key, value):
    """Reverse - Language Note."""
    return {
        'a': value.get('language_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        'b': utils.reverse_force_list(
            value.get('information_code_or_alphabet')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('547', '^former_title_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title_complexity_note(self, key, value):
    """Reverse - Former Title Complexity Note."""
    return {
        'a': value.get('former_title_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('550', '^issuing_body_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issuing_body_note(self, key, value):
    """Reverse - Issuing Body Note."""
    return {
        'a': value.get('issuing_body_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('552', '^entity_and_attribute_information_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_entity_and_attribute_information_note(self, key, value):
    """Reverse - Entity and Attribute Information Note."""
    return {
        'a': value.get('entity_type_label'),
        'c': value.get('attribute_label'),
        'b': value.get('entity_type_definition_and_source'),
        'e': utils.reverse_force_list(
            value.get('enumerated_domain_value')
        ),
        'd': value.get('attribute_definition_and_source'),
        'g': value.get('range_domain_minimum_and_maximum'),
        'f': utils.reverse_force_list(
            value.get('enumerated_domain_value_definition_and_source')
        ),
        'i': value.get('unrepresentable_domain'),
        'h': value.get('codeset_name_and_source'),
        'k': value.get('beginning_and_ending_date_of_attribute_values'),
        'j': value.get('attribute_units_of_measurement_and_resolution'),
        'm': value.get('attribute_value_accuracy_explanation'),
        'l': value.get('attribute_value_accuracy'),
        'o': utils.reverse_force_list(
            value.get('entity_and_attribute_overview')
        ),
        'n': value.get('attribute_measurement_frequency'),
        'p': utils.reverse_force_list(
            value.get('entity_and_attribute_detail_citation')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('display_note')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('555', '^cumulative_index_finding_aids_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_cumulative_index_finding_aids_note(self, key, value):
    """Reverse - Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        "Finding aids": "0",
        "Indexes": "_",
        "No display constant generated": "8"}
    return {
        'a': value.get('cumulative_index_finding_aids_note'),
        'c': value.get('degree_of_control'),
        'b': utils.reverse_force_list(
            value.get('availability_source')),
        'd': value.get('bibliographic_reference'),
        '3': value.get('materials_specified'),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('556', '^information_about_documentation_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_information_about_documentation_note(self, key, value):
    """Reverse - Information About Documentation Note."""
    indicator_map1 = {
        "Documentation": "_",
        "No display constant generated": "8"}
    return {
        'a': value.get('information_about_documentation_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('561', '^ownership_and_custodial_history$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_ownership_and_custodial_history(self, key, value):
    """Reverse - Ownership and Custodial History."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    return {
        'a': value.get('history'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('562', '^copy_and_version_identification_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_copy_and_version_identification_note(self, key, value):
    """Reverse - Copy and Version Identification Note."""
    return {
        'a': utils.reverse_force_list(
            value.get('identifying_markings')
        ),
        'c': utils.reverse_force_list(
            value.get('version_identification')
        ),
        'b': utils.reverse_force_list(
            value.get('copy_identification')
        ),
        'e': utils.reverse_force_list(
            value.get('number_of_copies')
        ),
        'd': utils.reverse_force_list(
            value.get('presentation_format')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('563', '^binding_information$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_binding_information(self, key, value):
    """Reverse - Binding Information."""
    return {
        'a': value.get('binding_note'),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('565', '^case_file_characteristics_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_case_file_characteristics_note(self, key, value):
    """Reverse - Case File Characteristics Note."""
    indicator_map1 = {
        "Case file characteristics": "0",
        "File size": "_",
        "No display constant generated": "8"}
    return {
        'a': value.get('number_of_cases_variables'),
        'c': utils.reverse_force_list(
            value.get('unit_of_analysis')),
        'b': utils.reverse_force_list(
            value.get('name_of_variable')),
        'e': utils.reverse_force_list(
            value.get('filing_scheme_or_code')),
        'd': utils.reverse_force_list(
            value.get('universe_of_data')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('567', '^methodology_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_methodology_note(self, key, value):
    """Reverse - Methodology Note."""
    indicator_map1 = {"Methodology": "_", "No display constant generated": "8"}
    return {
        'a': value.get('methodology_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('580', '^linking_entry_complexity_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_linking_entry_complexity_note(self, key, value):
    """Reverse - Linking Entry Complexity Note."""
    return {
        'a': value.get('linking_entry_complexity_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('581', '^publications_about_described_materials_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_publications_about_described_materials_note(self, key, value):
    """Reverse - Publications About Described Materials Note."""
    indicator_map1 = {
        "No display constant generated": "8",
        "Publications": "_"}
    return {
        'a': value.get('publications_about_described_materials_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '3': value.get('materials_specified'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('583', '^action_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_action_note(self, key, value):
    """Reverse - Action Note."""
    indicator_map1 = {
        "No information provided": "_",
        "Not private": "1",
        "Private": "0"}
    return {
        'a': value.get('action'),
        'x': utils.reverse_force_list(
            value.get('nonpublic_note')
        ),
        'c': utils.reverse_force_list(
            value.get('time_date_of_action')
        ),
        'b': utils.reverse_force_list(
            value.get('action_identification')
        ),
        'e': utils.reverse_force_list(
            value.get('contingency_for_action')
        ),
        'd': utils.reverse_force_list(
            value.get('action_interval')
        ),
        'f': utils.reverse_force_list(
            value.get('authorization')
        ),
        'i': utils.reverse_force_list(
            value.get('method_of_action')
        ),
        'h': utils.reverse_force_list(
            value.get('jurisdiction')
        ),
        'k': utils.reverse_force_list(
            value.get('action_agent')
        ),
        'j': utils.reverse_force_list(
            value.get('site_of_action')
        ),
        'l': utils.reverse_force_list(
            value.get('status')
        ),
        'o': utils.reverse_force_list(
            value.get('type_of_unit')
        ),
        'n': utils.reverse_force_list(
            value.get('extent')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('public_note')
        ),
        'u': utils.reverse_force_list(
            value.get('uniform_resource_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('privacy'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('584', '^accumulation_and_frequency_of_use_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_accumulation_and_frequency_of_use_note(self, key, value):
    """Reverse - Accumulation and Frequency of Use Note."""
    return {
        'a': utils.reverse_force_list(
            value.get('accumulation')
        ),
        'b': utils.reverse_force_list(
            value.get('frequency_of_use')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('585', '^exhibitions_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_exhibitions_note(self, key, value):
    """Reverse - Exhibitions Note."""
    return {
        'a': value.get('exhibitions_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '3': value.get('materials_specified'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('586', '^awards_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_awards_note(self, key, value):
    """Reverse - Awards Note."""
    indicator_map1 = {"Awards": "_", "No display constant generated": "8"}
    return {
        'a': value.get('awards_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '3': value.get('materials_specified'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(
            value.get('display_constant_controller'),
            '_'),
        '$ind2': '_',
    }


@to_marc21.over('588', '^source_of_description_note$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_source_of_description_note(self, key, value):
    """Reverse - Source of Description Note."""
    return {
        'a': value.get('source_of_description_note'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }
