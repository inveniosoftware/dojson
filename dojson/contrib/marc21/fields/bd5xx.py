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

from ..model import marc21


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


@marc21.over('formatted_contents_note', '^505[10_28][0_]')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    """Formatted Contents Note."""
    indicator_map1 = {
        "0": "Contents",
        "1": "Incomplete contents",
        "2": "Partial contents",
        "8": "No display constant generated"}
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


@marc21.over('restrictions_on_access_note', '^506[10_].')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    """Restrictions on Access Note."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "No restrictions",
        "1": "Restrictions apply"}
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


@marc21.over('citation_references_note', '^510[10324_].')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    """Citation/References Note."""
    indicator_map1 = {
        "0": "Coverage unknown",
        "1": "Coverage complete",
        "2": "Coverage is selective",
        "3": "Location in source not given",
        "4": "Location in source given"}
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


@marc21.over('type_of_computer_file_or_data_note', '^516[8_].')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    """Type of Computer File or Data Note."""
    indicator_map1 = {
        "#": "Type of file",
        "8": "No display constant generated"}
    return {
        'type_of_computer_file_or_data_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
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


@marc21.over('summary', '^520[10_2483].')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    """Summary, Etc.."""
    indicator_map1 = {
        "#": "Summary",
        "0": "Subject",
        "1": "Review",
        "2": "Scope and content",
        "3": "Abstract",
        "4": "Content advice",
        "8": "No display constant generated"}
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


@marc21.over('target_audience_note', '^521[10_2483].')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    """Target Audience Note."""
    indicator_map1 = {
        "#": "Audience",
        "0": "Reading grade level",
        "1": "Interest age level",
        "2": "Interest grade level",
        "3": "Special audience characteristics",
        "4": "Motivation/interest level",
        "8": "No display constant generated"}
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


@marc21.over('geographic_coverage_note', '^522[8_].')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    """Geographic Coverage Note."""
    indicator_map1 = {
        "#": "Geographic coverage",
        "8": "No display constant generated"}
    return {
        'geographic_coverage_note': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
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


@marc21.over('study_program_information_note', '^526[0_8].')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    """Study Program Information Note."""
    indicator_map1 = {
        "0": "Reading program",
        "8": "No display constant generated"}
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


@marc21.over('immediate_source_of_acquisition_note', '^541[10_].')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    """Immediate Source of Acquisition Note."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Private",
        "1": "Not private"}
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


@marc21.over('information_relating_to_copyright_status', '^542[10_].')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    """Information Relating to Copyright Status."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Private",
        "1": "Not private"}
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


@marc21.over('location_of_other_archival_materials_note', '^544[10_].')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    """Location of Other Archival Materials Note."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Associated materials",
        "1": "Related materials"}
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


@marc21.over('biographical_or_historical_data', '^545[10_].')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    """Biographical or Historical Data."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Biographical sketch",
        "1": "Administrative history"}
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


@marc21.over('cumulative_index_finding_aids_note', '^555[0_8].')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    """Cumulative Index/Finding Aids Note."""
    indicator_map1 = {
        "#": "Indexes",
        "0": "Finding aids",
        "8": "No display constant generated"}
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


@marc21.over('information_about_documentation_note', '^556[8_].')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    """Information About Documentation Note."""
    indicator_map1 = {
        "#": "Documentation",
        "8": "No display constant generated"}
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


@marc21.over('ownership_and_custodial_history', '^561[10_].')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    """Ownership and Custodial History."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Private",
        "1": "Not private"}
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


@marc21.over('case_file_characteristics_note', '^565[0_8].')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    """Case File Characteristics Note."""
    indicator_map1 = {
        "#": "File size",
        "0": "Case file characteristics",
        "8": "No display constant generated"}
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


@marc21.over('publications_about_described_materials_note', '^581[8_].')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    """Publications About Described Materials Note."""
    indicator_map1 = {
        "#": "Publications",
        "8": "No display constant generated"}
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


@marc21.over('action_note', '^583[10_].')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    """Action Note."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Private",
        "1": "Not private"}
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
