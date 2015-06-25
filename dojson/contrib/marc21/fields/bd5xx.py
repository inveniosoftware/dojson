# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from dojson import utils

from ..model import marc21

@marc21.over('general_note', '^500..')
@utils.for_each_value
@utils.filter_values
def general_note(self, key, value):
    return {
        'general_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }

@marc21.over('with_note', '^501..')
@utils.for_each_value
@utils.filter_values
def with_note(self, key, value):
    return {
        'with_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }

@marc21.over('dissertation_note', '^502..')
@utils.for_each_value
@utils.filter_values
def dissertation_note(self, key, value):
    return {
        'dissertation_note': value.get('a'),
        'name_of_granting_institution': value.get('c'),
        'degree_type': value.get('b'),
        'year_degree_granted': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'dissertation_identifier': value.get('o'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('bibliography_note', '^504..')
@utils.for_each_value
@utils.filter_values
def bibliography_note(self, key, value):
    return {
        'bibliography_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'number_of_references': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('formatted_contents_note', '^505[1028][0.]')
@utils.for_each_value
@utils.filter_values
def formatted_contents_note(self, key, value):
    indicator_map1 = {u'1': u'Incomplete contents', u'0': u'Contents', u'2': u'Partial contents', u'8': u'No display constant generated'}
    indicator_map2 = {u'0': u'Enhanced', u'#': u'Basic'}
    return {
        'formatted_contents_note': value.get('a'),
        'miscellaneous_information': value.get('g'),
        'statement_of_responsibility': value.get('r'),
        'uniform_resource_identifier': value.get('u'),
        'title': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
        'level_of_content_designation': indicator_map2.get(key[4]),
    }

@marc21.over('restrictions_on_access_note', '^506[10.].')
@utils.for_each_value
@utils.filter_values
def restrictions_on_access_note(self, key, value):
    indicator_map1 = {u'1': u'Restrictions apply', u'0': u'No restrictions', u'#': u'No information provided'}
    return {
        'terms_governing_access': value.get('a'),
        'physical_access_provisions': value.get('c'),
        'jurisdiction': value.get('b'),
        'authorization': value.get('e'),
        'authorized_users': value.get('d'),
        'standardized_terminology_for_access_restriction': value.get('f'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_resource_identifier': value.get('u'),
        'restriction': indicator_map1.get(key[3]),
    }

@marc21.over('scale_note_for_graphic_material', '^507..')
@utils.filter_values
def scale_note_for_graphic_material(self, key, value):
    return {
        'representative_fraction_of_scale_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'remainder_of_scale_note': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('creation_production_credits_note', '^508..')
@utils.for_each_value
@utils.filter_values
def creation_production_credits_note(self, key, value):
    return {
        'creation_production_credits_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('citation_references_note', '^510[10324].')
@utils.for_each_value
@utils.filter_values
def citation_references_note(self, key, value):
    indicator_map1 = {u'1': u'Coverage complete', u'0': u'Coverage unknown', u'3': u'Location in source not given', u'2': u'Coverage is selective', u'4': u'Location in source given'}
    return {
        'name_of_source': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_within_source': value.get('c'),
        'coverage_of_source': value.get('b'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'coverage_location_in_source': indicator_map1.get(key[3]),
    }

@marc21.over('participant_or_performer_note', '^511[10].')
@utils.for_each_value
@utils.filter_values
def participant_or_performer_note(self, key, value):
    indicator_map1 = {u'1': u'Cast', u'0': u'No display constant generated'}
    return {
        'participant_or_performer_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('type_of_report_and_period_covered_note', '^513..')
@utils.for_each_value
@utils.filter_values
def type_of_report_and_period_covered_note(self, key, value):
    return {
        'type_of_report': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'period_covered': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('data_quality_note', '^514..')
@utils.filter_values
def data_quality_note(self, key, value):
    return {
        'attribute_accuracy_report': value.get('a'),
        'attribute_accuracy_explanation': value.get('c'),
        'attribute_accuracy_value': value.get('b'),
        'completeness_report': value.get('e'),
        'logical_consistency_report': value.get('d'),
        'horizontal_position_accuracy_value': value.get('g'),
        'horizontal_position_accuracy_report': value.get('f'),
        'vertical_positional_accuracy_report': value.get('i'),
        'horizontal_position_accuracy_explanation': value.get('h'),
        'vertical_positional_accuracy_explanation': value.get('k'),
        'vertical_positional_accuracy_value': value.get('j'),
        'cloud_cover': value.get('m'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_note': value.get('z'),
    }

@marc21.over('numbering_peculiarities_note', '^515..')
@utils.for_each_value
@utils.filter_values
def numbering_peculiarities_note(self, key, value):
    return {
        'numbering_peculiarities_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('type_of_computer_file_or_data_note', '^516[8.].')
@utils.for_each_value
@utils.filter_values
def type_of_computer_file_or_data_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Type of file'}
    return {
        'type_of_computer_file_or_data_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('date_time_and_place_of_an_event_note', '^518..')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event_note(self, key, value):
    return {
        'date_time_and_place_of_an_event_note': value.get('a'),
        'date_of_event': value.get('d'),
        'place_of_event': value.get('p'),
        'other_event_information': value.get('o'),
        'record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('summary', '^520[.103248].')
@utils.for_each_value
@utils.filter_values
def summary(self, key, value):
    indicator_map1 = {u'#': u'Summary', u'1': u'Review', u'0': u'Subject', u'3': u'Abstract', u'2': u'Scope and content', u'4': u'Content advice', u'8': u'No display constant generated'}
    return {
        'summary': value.get('a'),
        'assigning_source': value.get('c'),
        'expansion_of_summary_note': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('target_audience_note', '^521[.103248].')
@utils.for_each_value
@utils.filter_values
def target_audience_note(self, key, value):
    indicator_map1 = {u'#': u'Audience', u'1': u'Interest age level', u'0': u'Reading grade level', u'3': u'Special audience characteristics', u'2': u'Interest grade level', u'4': u'Motivation/interest level', u'8': u'No display constant generated'}
    return {
        'target_audience_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'source': value.get('b'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('geographic_coverage_note', '^522[8.].')
@utils.for_each_value
@utils.filter_values
def geographic_coverage_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Geographic coverage'}
    return {
        'geographic_coverage_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('preferred_citation_of_described_materials_note', '^524[8.].')
@utils.for_each_value
@utils.filter_values
def preferred_citation_of_described_materials_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Cite as'}
    return {
        'preferred_citation_of_described_materials_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'source_of_schema_used': value.get('2'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('supplement_note', '^525..')
@utils.for_each_value
@utils.filter_values
def supplement_note(self, key, value):
    return {
        'supplement_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('study_program_information_note', '^526[08].')
@utils.for_each_value
@utils.filter_values
def study_program_information_note(self, key, value):
    indicator_map1 = {u'0': u'Reading program', u'8': u'No display constant generated'}
    return {
        'program_name': value.get('a'),
        'nonpublic_note': value.get('x'),
        'reading_level': value.get('c'),
        'interest_level': value.get('b'),
        'title_point_value': value.get('d'),
        'display_text': value.get('i'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'public_note': value.get('z'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('additional_physical_form_available_note', '^530..')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_available_note(self, key, value):
    return {
        'additional_physical_form_available_note': value.get('a'),
        'availability_conditions': value.get('c'),
        'availability_source': value.get('b'),
        'order_number': value.get('d'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('reproduction_note', '^533..')
@utils.for_each_value
@utils.filter_values
def reproduction_note(self, key, value):
    return {
        'type_of_reproduction': value.get('a'),
        'agency_responsible_for_reproduction': value.get('c'),
        'place_of_reproduction': value.get('b'),
        'physical_description_of_reproduction': value.get('e'),
        'date_of_reproduction': value.get('d'),
        'series_statement_of_reproduction': value.get('f'),
        'dates_and_or_sequential_designation_of_issues_reproduced': value.get('m'),
        'note_about_reproduction': value.get('n'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'fixed_length_data_elements_of_reproduction': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('original_version_note', '^534..')
@utils.for_each_value
@utils.filter_values
def original_version_note(self, key, value):
    return {
        'main_entry_of_original': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'publication_distribution_of_original': value.get('c'),
        'edition_statement_of_original': value.get('b'),
        'physical_description_of_original': value.get('e'),
        'series_statement_of_original': value.get('f'),
        'key_title_of_original': value.get('k'),
        'material_specific_details': value.get('m'),
        'location_of_original': value.get('l'),
        'other_resource_identifier': value.get('o'),
        'note_about_original': value.get('n'),
        'introductory_phrase': value.get('p'),
        'materials_specified': value.get('3'),
        'title_statement_of_original': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'international_standard_book_number': value.get('z'),
    }

@marc21.over('location_of_originals_duplicates_note', '^535[12].')
@utils.for_each_value
@utils.filter_values
def location_of_originals_duplicates_note(self, key, value):
    indicator_map1 = {u'1': u'Holder of originals', u'2': u'Holder of duplicates'}
    return {
        'custodian': value.get('a'),
        'country': value.get('c'),
        'postal_address': value.get('b'),
        'telecommunications_address': value.get('d'),
        'repository_location_code': value.get('g'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'custodial_role': indicator_map1.get(key[3]),
    }

@marc21.over('funding_information_note', '^536..')
@utils.for_each_value
@utils.filter_values
def funding_information_note(self, key, value):
    return {
        'text_of_note': value.get('a'),
        'grant_number': value.get('c'),
        'contract_number': value.get('b'),
        'program_element_number': value.get('e'),
        'undifferentiated_number': value.get('d'),
        'task_number': value.get('g'),
        'project_number': value.get('f'),
        'work_unit_number': value.get('h'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('system_details_note', '^538..')
@utils.for_each_value
@utils.filter_values
def system_details_note(self, key, value):
    return {
        'system_details_note': value.get('a'),
        'display_text': value.get('i'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_resource_identifier': value.get('u'),
    }

@marc21.over('terms_governing_use_and_reproduction_note', '^540..')
@utils.for_each_value
@utils.filter_values
def terms_governing_use_and_reproduction_note(self, key, value):
    return {
        'terms_governing_use_and_reproduction': value.get('a'),
        'authorization': value.get('c'),
        'jurisdiction': value.get('b'),
        'authorized_users': value.get('d'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_resource_identifier': value.get('u'),
    }

@marc21.over('immediate_source_of_acquisition_note', '^541[10.].')
@utils.for_each_value
@utils.filter_values
def immediate_source_of_acquisition_note(self, key, value):
    indicator_map1 = {u'1': u'Not private', u'0': u'Private', u'#': u'No information provided'}
    return {
        'source_of_acquisition': value.get('a'),
        'method_of_acquisition': value.get('c'),
        'address': value.get('b'),
        'accession_number': value.get('e'),
        'date_of_acquisition': value.get('d'),
        'owner': value.get('f'),
        'purchase_price': value.get('h'),
        'type_of_unit': value.get('o'),
        'extent': value.get('n'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'privacy': indicator_map1.get(key[3]),
    }

@marc21.over('information_relating_to_copyright_status', '^542[10.].')
@utils.for_each_value
@utils.filter_values
def information_relating_to_copyright_status(self, key, value):
    indicator_map1 = {u'1': u'Not private', u'0': u'Private', u'#': u'No information provided'}
    return {
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'personal_creator': value.get('a'),
        'corporate_creator': value.get('c'),
        'personal_creator_death_date': value.get('b'),
        'copyright_holder_contact_information': value.get('e'),
        'copyright_holder': value.get('d'),
        'copyright_date': value.get('g'),
        'copyright_statement': value.get('f'),
        'publication_date': value.get('i'),
        'copyright_renewal_date': value.get('h'),
        'publisher': value.get('k'),
        'creation_date': value.get('j'),
        'publication_status': value.get('m'),
        'copyright_status': value.get('l'),
        'research_date': value.get('o'),
        'note': value.get('n'),
        'supplying_agency': value.get('q'),
        'country_of_publication_or_creation': value.get('p'),
        'source_of_information': value.get('s'),
        'jurisdiction_of_copyright_assessment': value.get('r'),
        'uniform_resource_identifier': value.get('u'),
        'privacy': indicator_map1.get(key[3]),
    }

@marc21.over('location_of_other_archival_materials_note', '^544[10.].')
@utils.for_each_value
@utils.filter_values
def location_of_other_archival_materials_note(self, key, value):
    indicator_map1 = {u'1': u'Related materials', u'0': u'Associated materials', u'#': u'No information provided'}
    return {
        'custodian': value.get('a'),
        'country': value.get('c'),
        'address': value.get('b'),
        'provenance': value.get('e'),
        'title': value.get('d'),
        'note': value.get('n'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'relationship': indicator_map1.get(key[3]),
    }

@marc21.over('biographical_or_historical_data', '^545[10.].')
@utils.for_each_value
@utils.filter_values
def biographical_or_historical_data(self, key, value):
    indicator_map1 = {u'1': u'Administrative history', u'0': u'Biographical sketch', u'#': u'No information provided'}
    return {
        'biographical_or_historical_data': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'expansion': value.get('b'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'type_of_data': indicator_map1.get(key[3]),
    }

@marc21.over('language_note', '^546..')
@utils.for_each_value
@utils.filter_values
def language_note(self, key, value):
    return {
        'language_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'information_code_or_alphabet': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('former_title_complexity_note', '^547..')
@utils.for_each_value
@utils.filter_values
def former_title_complexity_note(self, key, value):
    return {
        'former_title_complexity_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('issuing_body_note', '^550..')
@utils.for_each_value
@utils.filter_values
def issuing_body_note(self, key, value):
    return {
        'issuing_body_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('entity_and_attribute_information_note', '^552..')
@utils.for_each_value
@utils.filter_values
def entity_and_attribute_information_note(self, key, value):
    return {
        'entity_type_label': value.get('a'),
        'attribute_label': value.get('c'),
        'entity_type_definition_and_source': value.get('b'),
        'enumerated_domain_value': value.get('e'),
        'attribute_definition_and_source': value.get('d'),
        'range_domain_minimum_and_maximum': value.get('g'),
        'enumerated_domain_value_definition_and_source': value.get('f'),
        'unrepresentable_domain': value.get('i'),
        'codeset_name_and_source': value.get('h'),
        'beginning_and_ending_date_of_attribute_values': value.get('k'),
        'attribute_units_of_measurement_and_resolution': value.get('j'),
        'attribute_value_accuracy_explanation': value.get('m'),
        'attribute_value_accuracy': value.get('l'),
        'entity_and_attribute_overview': value.get('o'),
        'attribute_measurement_frequency': value.get('n'),
        'entity_and_attribute_detail_citation': value.get('p'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_note': value.get('z'),
    }

@marc21.over('cumulative_index_finding_aids_note', '^555[0.8].')
@utils.for_each_value
@utils.filter_values
def cumulative_index_finding_aids_note(self, key, value):
    indicator_map1 = {u'0': u'Finding aids', u'#': u'Indexes', u'8': u'No display constant generated'}
    return {
        'cumulative_index_finding_aids_note': value.get('a'),
        'degree_of_control': value.get('c'),
        'availability_source': value.get('b'),
        'bibliographic_reference': value.get('d'),
        'materials_specified': value.get('3'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('information_about_documentation_note', '^556[8.].')
@utils.for_each_value
@utils.filter_values
def information_about_documentation_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Documentation'}
    return {
        'information_about_documentation_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'international_standard_book_number': value.get('z'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('ownership_and_custodial_history', '^561[10.].')
@utils.for_each_value
@utils.filter_values
def ownership_and_custodial_history(self, key, value):
    indicator_map1 = {u'1': u'Not private', u'0': u'Private', u'#': u'No information provided'}
    return {
        'history': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_resource_identifier': value.get('u'),
        'privacy': indicator_map1.get(key[3]),
    }

@marc21.over('copy_and_version_identification_note', '^562..')
@utils.for_each_value
@utils.filter_values
def copy_and_version_identification_note(self, key, value):
    return {
        'identifying_markings': value.get('a'),
        'version_identification': value.get('c'),
        'copy_identification': value.get('b'),
        'number_of_copies': value.get('e'),
        'presentation_format': value.get('d'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('binding_information', '^563..')
@utils.for_each_value
@utils.filter_values
def binding_information(self, key, value):
    return {
        'binding_note': value.get('a'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_resource_identifier': value.get('u'),
    }

@marc21.over('case_file_characteristics_note', '^565[0.8].')
@utils.for_each_value
@utils.filter_values
def case_file_characteristics_note(self, key, value):
    indicator_map1 = {u'0': u'Case file characteristics', u'#': u'File size', u'8': u'No display constant generated'}
    return {
        'number_of_cases_variables': value.get('a'),
        'unit_of_analysis': value.get('c'),
        'name_of_variable': value.get('b'),
        'filing_scheme_or_code': value.get('e'),
        'universe_of_data': value.get('d'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('methodology_note', '^567[8.].')
@utils.for_each_value
@utils.filter_values
def methodology_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Methodology'}
    return {
        'methodology_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('linking_entry_complexity_note', '^580..')
@utils.for_each_value
@utils.filter_values
def linking_entry_complexity_note(self, key, value):
    return {
        'linking_entry_complexity_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('publications_about_described_materials_note', '^581[8.].')
@utils.for_each_value
@utils.filter_values
def publications_about_described_materials_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Publications'}
    return {
        'publications_about_described_materials_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'international_standard_book_number': value.get('z'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('action_note', '^583[10.].')
@utils.for_each_value
@utils.filter_values
def action_note(self, key, value):
    indicator_map1 = {u'1': u'Not private', u'0': u'Private', u'#': u'No information provided'}
    return {
        'action': value.get('a'),
        'nonpublic_note': value.get('x'),
        'time_date_of_action': value.get('c'),
        'action_identification': value.get('b'),
        'contingency_for_action': value.get('e'),
        'action_interval': value.get('d'),
        'authorization': value.get('f'),
        'method_of_action': value.get('i'),
        'jurisdiction': value.get('h'),
        'action_agent': value.get('k'),
        'site_of_action': value.get('j'),
        'status': value.get('l'),
        'type_of_unit': value.get('o'),
        'extent': value.get('n'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'public_note': value.get('z'),
        'uniform_resource_identifier': value.get('u'),
        'privacy': indicator_map1.get(key[3]),
    }

@marc21.over('accumulation_and_frequency_of_use_note', '^584..')
@utils.for_each_value
@utils.filter_values
def accumulation_and_frequency_of_use_note(self, key, value):
    return {
        'accumulation': value.get('a'),
        'frequency_of_use': value.get('b'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('exhibitions_note', '^585..')
@utils.for_each_value
@utils.filter_values
def exhibitions_note(self, key, value):
    return {
        'exhibitions_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }

@marc21.over('awards_note', '^586[8.].')
@utils.for_each_value
@utils.filter_values
def awards_note(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Awards'}
    return {
        'awards_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('source_of_description_note', '^588..')
@utils.for_each_value
@utils.filter_values
def source_of_description_note(self, key, value):
    return {
        'source_of_description_note': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
    }
