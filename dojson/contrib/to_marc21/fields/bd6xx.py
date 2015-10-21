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


@to_marc21.over('600', '^subject_added_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_personal_name(self, key, value):
    """Reverse - Subject Added Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('personal_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'b': value.get('numeration'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('610', '^subject_added_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_corporate_name(self, key, value):
    """Reverse - Subject Added Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('611', '^subject_added_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_meeting_name(self, key, value):
    """Reverse - Subject Added Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'u': value.get('affiliation'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('630', '^subject_added_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_uniform_title(self, key, value):
    """Reverse - Subject Added Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'a': value.get('uniform_title'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('648', '^subject_added_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_chronological_term(self, key, value):
    """Reverse - Subject Added Entry-Chronological Term."""
    indicator_map1 = {
        "Date or time period covered or depicted": "0",
        "Date or time period of creation or origin": "1",
        "No information provided": "_"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00c3\u00a9pertoire de vedettes-mati\u00c3\u00a8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        'a': value.get('chronological_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')),
        '$ind1': indicator_map1.get(
            value.get('type_of_date_or_time_period'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('thesaurus'),
            '_'),
    }


@to_marc21.over('650', '^subject_added_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_topical_term(self, key, value):
    """Reverse - Subject Added Entry-Topical Term."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': value.get('location_of_event'),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('active_dates'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('651', '^subject_added_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_geographic_name(self, key, value):
    """Reverse - Subject Added Entry-Geographic Name."""
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        'a': value.get('geographic_name'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('653', '^index_term_uncontrolled$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_uncontrolled(self, key, value):
    """Reverse - Index Term-Uncontrolled."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    indicator_map2 = {
        "Chronological term": "4",
        "Corporate name": "2",
        "Genre/form term": "6",
        "Geographic name": "5",
        "Meeting name": "3",
        "No information provided": "_",
        "Personal name": "1",
        "Topical term": "0"}
    return {
        'a': utils.reverse_force_list(
            value.get('uncontrolled_term')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('level_of_index_term'), '_'),
        '$ind2': indicator_map2.get(value.get('type_of_term_or_name'), '_'),
    }


@to_marc21.over('654', '^subject_added_entry_faceted_topical_terms$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_faceted_topical_terms(self, key, value):
    """Reverse - Subject Added Entry-Faceted Topical Terms."""
    indicator_map1 = {
        "No information provided": "_",
        "No level specified": "0",
        "Primary": "1",
        "Secondary": "2"}
    return {
        'a': utils.reverse_force_list(
            value.get('focus_term')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('level_of_subject'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('655', '^index_term_genre_form$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_genre_form(self, key, value):
    """Reverse - Index Term-Genre/Form."""
    indicator_map1 = {"Basic": "_", "Faceted": "0"}
    indicator_map2 = {
        "Canadian Subject Headings": "5",
        "LC subject headings for children\u0027s literature": "1",
        "Library of Congress Subject Headings": "0",
        "Medical Subject Headings": "2",
        "National Agricultural Library subject authority file": "3",
        "R\u00e9pertoire de vedettes-mati\u00e8re": "6",
        "Source not specified": "4",
        "Source specified in subfield $2": "7"}
    return {
        'a': value.get('genre_form_data_or_focus_term'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'c': utils.reverse_force_list(
            value.get('facet_hierarchy_designation')
        ),
        'b': utils.reverse_force_list(
            value.get('non_focus_term')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_heading'), '_'),
        '$ind2': indicator_map2.get(value.get('thesaurus'), '_'),
    }


@to_marc21.over('656', '^index_term_occupation$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_occupation(self, key, value):
    """Reverse - Index Term-Occupation."""
    return {
        'a': value.get('occupation'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'k': value.get('form'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('657', '^index_term_function$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_function(self, key, value):
    """Reverse - Index Term-Function."""
    return {
        'a': value.get('function'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '3': value.get('materials_specified'),
        '2': value.get('source_of_term'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('658', '^index_term_curriculum_objective$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_index_term_curriculum_objective(self, key, value):
    """Reverse - Index Term-Curriculum Objective."""
    return {
        'a': value.get('main_curriculum_objective'),
        'c': value.get('curriculum_code'),
        'b': utils.reverse_force_list(
            value.get('subordinate_curriculum_objective')
        ),
        'd': value.get('correlation_factor'),
        '2': value.get('source_of_term_or_code'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }


@to_marc21.over('662', '^subject_added_entry_hierarchical_place_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subject_added_entry_hierarchical_place_name(self, key, value):
    """Reverse - Subject Added Entry-Hierarchical Place Name."""
    return {
        'a': utils.reverse_force_list(
            value.get('country_or_larger_entity')
        ),
        'c': utils.reverse_force_list(
            value.get('intermediate_political_jurisdiction')
        ),
        'b': value.get('first_order_political_jurisdiction'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('city'),
        'g': utils.reverse_force_list(
            value.get('other_nonjurisdictional_geographic_region_and_feature')
        ),
        'f': utils.reverse_force_list(
            value.get('city_subsection')
        ),
        'h': utils.reverse_force_list(
            value.get('extraterrestrial_area')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': '_',
        '$ind2': '_',
    }
