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


@marc21.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    return {
        'lc_control_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'nucmc_control_number': value.get('b'),
        'canceled_invalid_lc_control_number': value.get('z'),
    }


@marc21.over('patent_control_information', '^013..')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    return {
        'number': value.get('a'),
        'type_of_number': value.get('c'),
        'country': value.get('b'),
        'status': value.get('e'),
        'date': value.get('d'),
        'party_to_document': value.get('f'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('national_bibliography_number', '^015..')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    return {
        'national_bibliography_number': value.get('a'),
        'qualifying_information': value.get('q'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_national_bibliography_number': value.get('z'),
    }


@marc21.over('national_bibliographic_agency_control_number', '^016[_7].')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    indicator_map1 = {u'#': u'Library and Archives Canada',
                      u'7': u'Source specified in subfield $2'}
    return {
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'canceled_invalid_control_number': value.get('z'),
        'national_bibliographic_agency': indicator_map1.get(key[3]),
    }


@marc21.over('copyright_or_legal_deposit_number', '^017.[8_]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    indicator_map2 = {u'8': u'No display constant generated',
                      u'#': u'Copyright or legal deposit number'}
    return {
        'copyright_or_legal_deposit_number': value.get('a'),
        'assigning_agency': value.get('b'),
        'date': value.get('d'),
        'display_text': value.get('i'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_copyright_or_legal_deposit_number': value.get('z'),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('copyright_article_fee_code', '^018..')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    return {
        'copyright_article_fee_code_nr': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }


@marc21.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    return {
        'international_standard_book_number': value.get('a'),
        'terms_of_availability': value.get('c'),
        'qualifying_information': value.get('q'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_isbn': value.get('z'),
    }


@marc21.over('international_standard_serial_number', '^022[10_].')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    indicator_map1 = {u'1': u'Continuing resource not of international interest',
                      u'0': u'Continuing resource of international interest', u'#': u'No level specified'}
    return {
        'international_standard_serial_number': value.get('a'),
        'canceled_issn_l': value.get('m'),
        'issn_l': value.get('l'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'incorrect_issn': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_issn': value.get('z'),
        'level_of_international_interest': indicator_map1.get(key[3]),
    }


@marc21.over('other_standard_identifier', '^024[1032478_][10_]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    indicator_map1 = {u'1': u'Universal Product Code', u'0': u'International Standard Recording Code', u'3': u'International Article Number', u'2': u'International Standard Music Number',
                      u'4': u'Serial Item and Contribution Identifier', u'7': u'Source specified in subfield $2', u'8': u'Unspecified type of standard number or code'}
    indicator_map2 = {
        u'1': u'Difference', u'0': u'No difference', u'#': u'No information provided'}
    return {
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'qualifying_information': value.get('q'),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_standard_number_or_code': value.get('z'),
        'type_of_standard_number_or_code': indicator_map1.get(key[3]),
        'difference_indicator': indicator_map2.get(key[4]),
    }


@marc21.over('overseas_acquisition_number', '^025..')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    return {
        'overseas_acquisition_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('fingerprint_identifier', '^026..')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    return {
        'first_and_second_groups_of_characters': value.get('a'),
        'date': value.get('c'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'unparsed_fingerprint': value.get('e'),
        'number_of_volume_or_part': value.get('d'),
        'source': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    return {
        'standard_technical_report_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_number': value.get('z'),
        'qualifying_information': value.get('q'),
        'linkage': value.get('6'),
    }


@marc21.over('publisher_number', '^028[103254_][1032_]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    indicator_map1 = {u'1': u'Matrix number', u'0': u'Issue number', u'3': u'Other music number',
                      u'2': u'Plate number', u'5': u'Other publisher number', u'4': u'Videorecording number'}
    indicator_map2 = {u'1': u'Note, added entry', u'0': u'No note, no added entry',
                      u'3': u'No note, added entry', u'2': u'Note, no added entry'}
    return {
        'publisher_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('b'),
        'qualifying_information': value.get('q'),
        'linkage': value.get('6'),
        'type_of_publisher_number': indicator_map1.get(key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4]),
    }


@marc21.over('coden_designation', '^030..')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    return {
        'coden': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_coden': value.get('z'),
        'linkage': value.get('6'),
    }


@marc21.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    return {
        'number_of_work': value.get('a'),
        'number_of_excerpt': value.get('c'),
        'number_of_movement': value.get('b'),
        'role': value.get('e'),
        'caption_or_heading': value.get('d'),
        'clef': value.get('g'),
        'public_note': value.get('z'),
        'voice_instrument': value.get('m'),
        'time_signature': value.get('o'),
        'key_signature': value.get('n'),
        'general_note': value.get('q'),
        'musical_notation': value.get('p'),
        'coded_validity_note': value.get('s'),
        'system_code': value.get('2'),
        'uniform_resource_identifier': value.get('u'),
        'text_incipit': value.get('t'),
        'linkage': value.get('6'),
        'link_text': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'key_or_mode': value.get('r'),
    }


@marc21.over('postal_registration_number', '^032..')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    return {
        'postal_registration_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('date_time_and_place_of_an_event', '^033[10_2][10_2]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    indicator_map1 = {u'1': u'Multiple single dates ', u'0': u'Single date ',
                      u'#': u'No date information ', u'2': u'Range of dates '}
    indicator_map2 = {u'1': u'Broadcast ', u'0': u'Capture ',
                      u'#': u'No information provided ', u'2': u'Finding '}
    return {
        'formatted_date_time': value.get('a'),
        'geographic_classification_subarea_code': value.get('c'),
        'geographic_classification_area_code': value.get('b'),
        'place_of_event': value.get('p'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'type_of_date_in_subfield_a': indicator_map1.get(key[3]),
        'type_of_event': indicator_map2.get(key[4]),
    }


@marc21.over('coded_cartographic_mathematical_data', '^034[103_][10_]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    indicator_map1 = {u'1': u'Single scale', u'0':
                      u'Scale indeterminable/No scale recorded', u'3': u'Range of scales'}
    indicator_map2 = {
        u'1': u'Exclusion ring', u'0': u'Outer ring', u'#': u'Not applicable'}
    return {
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'category_of_scale': value.get('a'),
        'constant_ratio_linear_vertical_scale': value.get('c'),
        'constant_ratio_linear_horizontal_scale': value.get('b'),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_southernmost_latitude': value.get('g'),
        'coordinates_northernmost_latitude': value.get('f'),
        'angular_scale': value.get('h'),
        'declination_southern_limit': value.get('k'),
        'declination_northern_limit': value.get('j'),
        'right_ascension_eastern_limit': value.get('m'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'g_ring_latitude': value.get('s'),
        'distance_from_earth': value.get('r'),
        'g_ring_longitude': value.get('t'),
        'ending_date': value.get('y'),
        'beginning_date': value.get('x'),
        'name_of_extraterrestrial_body': value.get('z'),
        'type_of_scale': indicator_map1.get(key[3]),
        'type_of_ring': indicator_map2.get(key[4]),
    }


@marc21.over('system_control_number', '^035..')
@utils.for_each_value
@utils.filter_values
def system_control_number(self, key, value):
    return {
        'system_control_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_control_number': value.get('z'),
        'linkage': value.get('6'),
    }


@marc21.over('original_study_number_for_computer_data_files', '^036..')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    return {
        'original_study_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('source_of_acquisition', '^037..')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    return {
        'stock_number': value.get('a'),
        'terms_of_availability': value.get('c'),
        'source_of_stock_number_acquisition': value.get('b'),
        'additional_format_characteristics': value.get('g'),
        'form_of_issue': value.get('f'),
        'note': value.get('n'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('record_content_licensor', '^038..')
@utils.filter_values
def record_content_licensor(self, key, value):
    return {
        'record_content_licensor': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }


@marc21.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    return {
        'original_cataloging_agency': value.get('a'),
        'transcribing_agency': value.get('c'),
        'language_of_cataloging': value.get('b'),
        'description_conventions': value.get('e'),
        'modifying_agency': value.get('d'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('language_code', '^041[10_].')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    indicator_map1 = {u'1': u'Item is or includes a translation', u'0':
                      u'Item not a translation/does not include a\n                  \t\t\t\t\t\ttranslation', u'#': u'No information provided'}
    return {
        'language_code_of_text_sound_track_or_separate_title': value.get('a'),
        'language_code_of_summary_or_abstract': value.get('b'),
        'language_code_of_librettos': value.get('e'),
        'language_code_of_sung_or_spoken_text': value.get('d'),
        'language_code_of_accompanying_material_other_than_librettos': value.get('g'),
        'language_code_of_table_of_contents': value.get('f'),
        'language_code_of_original': value.get('h'),
        'language_code_of_intermediate_translations': value.get('k'),
        'language_code_of_subtitles_or_captions': value.get('j'),
        'language_code_of_original_accompanying_materials_other_than_librettos': value.get('m'),
        'language_code_of_original_libretto': value.get('n'),
        'source_of_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'translation_indication': indicator_map1.get(key[3]),
    }


@marc21.over('authentication_code', '^042..')
@utils.filter_values
def authentication_code(self, key, value):
    return {
        'authentication_code': value.get('a'),
    }


@marc21.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    return {
        'geographic_area_code': value.get('a'),
        'iso_code': value.get('c'),
        'local_gac_code': value.get('b'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'source_of_local_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('country_of_publishing_producing_entity_code', '^044..')
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    return {
        'marc_country_code': value.get('a'),
        'iso_country_code': value.get('c'),
        'local_subentity_code': value.get('b'),
        'source_of_local_subentity_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('time_period_of_content', '^045[10_2].')
@utils.filter_values
def time_period_of_content(self, key, value):
    indicator_map1 = {u'1': u'Multiple single dates/times', u'0': u'Single date/time',
                      u'#': u'Subfield $b or $c not present', u'2': u'Range of dates/times'}
    return {
        'time_period_code': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'formatted_pre_9999_bc_time_period': value.get('c'),
        'formatted_9999_bc_through_ce_time_period': value.get('b'),
        'linkage': value.get('6'),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3]),
    }


@marc21.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    return {
        'type_of_date_code': value.get('a'),
        'date_1_ce_date': value.get('c'),
        'date_1_bc_date': value.get('b'),
        'date_2_ce_date': value.get('e'),
        'date_2_bc_date': value.get('d'),
        'beginning_or_single_date_created': value.get('k'),
        'date_resource_modified': value.get('j'),
        'beginning_of_date_valid': value.get('m'),
        'ending_date_created': value.get('l'),
        'single_or_starting_date_for_aggregated_content': value.get('o'),
        'end_of_date_valid': value.get('n'),
        'ending_date_for_aggregated_content': value.get('p'),
        'source_of_date': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('form_of_musical_composition_code', '^047..')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    return {
        'form_of_musical_composition_code': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_code': value.get('2'),
    }


@marc21.over('number_of_musical_instruments_or_voices_code', '^048..')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    return {
        'performer_or_ensemble': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_code': value.get('2'),
        'soloist': value.get('b'),
    }


@marc21.over('library_of_congress_call_number', '^050[10_][04_]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    indicator_map1 = {u'1': u'Item is not in LC',
                      u'0': u'Item is in LC', u'#': u'No information provided'}
    indicator_map2 = {
        u'0': u'Assigned by LC', u'4': u'Assigned by agency other than LC'}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lc_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('library_of_congress_copy_issue_offprint_statement', '^051..')
@utils.for_each_value
@utils.filter_values
def library_of_congress_copy_issue_offprint_statement(self, key, value):
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@marc21.over('geographic_classification', '^052..')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    return {
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': value.get('b'),
        'populated_place_name': value.get('d'),
        'code_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('classification_numbers_assigned_in_canada', '^055[10_][1032547698_]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    indicator_map1 = {u'1': u'Work not held by LAC', u'0':
                      u'Work held by LAC', u'#': u'Information not provided'}
    indicator_map2 = {u'1': u'Complete LC class number assigned by LAC', u'0': u'LC-based call number assigned by LAC', u'3': u'LC-based call number assigned by the contributing library', u'2': u'Incomplete LC class number assigned by LAC', u'5': u'Incomplete LC class number assigned by the contributing library',
                      u'4': u'Complete LC class number assigned by the contributing library', u'7': u'Other class number assigned by LAC', u'6': u'Other call number assigned by LAC', u'9': u'Other class number assigned by the contributing library', u'8': u'Other call number assigned by the contributing library'}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_call_class_number': value.get('2'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_call_number', '^060[10_][04_]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    indicator_map1 = {u'1': u'Item is not in NLM',
                      u'0': u'Item is in NLM', u'#': u'No information provided'}
    indicator_map2 = {
        u'0': u'Assigned by NLM', u'4': u'Assigned by agency other than NLM'}
    return {
        'classification_number_r': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'item_number': value.get('b'),
        'existence_in_nlm_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_copy_statement', '^061..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@marc21.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    return {
        'primary_g0_character_set': value.get('a'),
        'alternate_g0_or_g1_character_set': value.get('c'),
        'primary_g1_character_set': value.get('b'),
    }


@marc21.over('national_agricultural_library_call_number', '^070[10_].')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    indicator_map1 = {u'1': u'Item is not in NAL', u'0': u'Item is in NAL'}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number_r': value.get('8'),
        'item_number': value.get('b'),
        'existence_in_nal_collection': indicator_map1.get(key[3]),
    }


@marc21.over('national_agricultural_library_copy_statement', '^071..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@marc21.over('subject_category_code', '^072..')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    return {
        'subject_category_code': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'subject_category_code_subdivision': value.get('x'),
        'linkage': value.get('6'),
    }


@marc21.over('gpo_item_number', '^074..')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    return {
        'gpo_item_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_gpo_item_number': value.get('z'),
    }


@marc21.over('universal_decimal_classification_number', '^080[10_].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    indicator_map1 = {
        u'1': u'Abridged', u'0': u'Full', u'#': u'No information provided'}
    return {
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'edition_identifier': value.get('2'),
        'common_auxiliary_subdivision': value.get('x'),
        'field_link_and_sequence_number': value.get('8'),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('dewey_decimal_classification_number', '^082[107_][0_4]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    indicator_map1 = {u'1': u'Abridged edition', u'0': u'Full edition',
                      u'7': u'Other edition specified in subfield $2'}
    indicator_map2 = {u'0': u'Assigned by LC', u'#':
                      u'No information provided', u'4': u'Assigned by agency other than LC'}
    return {
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'type_of_edition': indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21.over('additional_dewey_decimal_classification_number', '^083[107_].')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    indicator_map1 = {u'1': u'Abridged edition', u'0': u'Full edition',
                      u'7': u'Other edition specified in subfield $2'}
    return {
        'classification_number': value.get('a'),
        'classification_number_ending_number_of_span': value.get('c'),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'table_identification': value.get('z'),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('other_classification_number', '^084..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    return {
        'classification_number': value.get('a'),
        'item_number': value.get('b'),
        'assigning_agency': value.get('q'),
        'number_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }


@marc21.over('synthesized_classification_number_components', '^085..')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    return {
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': value.get('a'),
        'classification_number_ending_number_of_span': value.get('c'),
        'base_number': value.get('b'),
        'facet_designator': value.get('f'),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': value.get('v'),
        'digits_added_from_classification_number_in_schedule_or_external_table': value.get('s'),
        'root_number': value.get('r'),
        'number_being_analyzed': value.get('u'),
        'digits_added_from_internal_subarrangement_or_add_table': value.get('t'),
        'table_identification_internal_subarrangement_or_add_table': value.get('w'),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'table_identification': value.get('z'),
    }


@marc21.over('government_document_classification_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'number_source': value.get('2'),
        'canceled_invalid_classification_number': value.get('z'),
        'linkage': value.get('6'),
    }


@marc21.over('report_number', '^088..')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    return {
        'report_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'canceled_invalid_report_number': value.get('z'),
        'linkage': value.get('6'),
    }
