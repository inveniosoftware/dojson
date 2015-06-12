"""MARC 21 model definition."""

from dojson import Overdo
from dojson import utils

marc21 = Overdo()

@marc21.over('control_number', '^001')
def control_number(self, key, value):
    return value[0]

@marc21.over('control_number_identifier', '^003')
def control_number_identifier(self, key, value):
    return value[0]

@marc21.over('date_and_time_of_latest_transaction', '^005')
def date_and_time_of_latest_transaction(self, key, value):
    return value[0]

@marc21.over('fixed_length_data_elements_additional_material_characteristics', '^006')
def fixed_length_data_elements_additional_material_characteristics(self, key, value):
    return value[0]

@marc21.over('fixed_length_data_elements', '^008')
def fixed_length_data_elements(self, key, value):
    return value[0]

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

@marc21.over('national_bibliographic_agency_control_number', '^016[.7].')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    indicator_map1 = {u'#': u'Library and Archives Canada', u'7': u'Source specified in subfield $2'}
    return {
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'canceled_invalid_control_number': value.get('z'),
        'national_bibliographic_agency': indicator_map1.get(key[3]),
    }

@marc21.over('copyright_or_legal_deposit_number', '^017.[8.]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Copyright or legal deposit number'}
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

@marc21.over('international_standard_serial_number', '^022[10.].')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    indicator_map1 = {u'1': u'Continuing resource not of international interest', u'0': u'Continuing resource of international interest', u'#': u'No level specified'}
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

@marc21.over('other_standard_identifier', '^024[1032478][10.]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    indicator_map1 = {u'1': u'Universal Product Code', u'0': u'International Standard Recording Code', u'3': u'International Article Number', u'2': u'International Standard Music Number', u'4': u'Serial Item and Contribution Identifier', u'7': u'Source specified in subfield $2', u'8': u'Unspecified type of standard number or code'}
    indicator_map2 = {u'1': u'Difference', u'0': u'No difference', u'#': u'No information provided'}
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

@marc21.over('publisher_number', '^028[103254][1032]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    indicator_map1 = {u'1': u'Matrix number', u'0': u'Issue number', u'3': u'Other music number', u'2': u'Plate number', u'5': u'Other publisher number', u'4': u'Videorecording number'}
    indicator_map2 = {u'1': u'Note, added entry', u'0': u'No note, no added entry', u'3': u'No note, added entry', u'2': u'Note, no added entry'}
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

@marc21.over('date_time_and_place_of_an_event', '^033[10.2][10.2]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    indicator_map1 = {u'1': u'Multiple single dates ', u'0': u'Single date ', u'#': u'No date information ', u'2': u'Range of dates '}
    indicator_map2 = {u'1': u'Broadcast ', u'0': u'Capture ', u'#': u'No information provided ', u'2': u'Finding '}
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

@marc21.over('coded_cartographic_mathematical_data', '^034[103][10.]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    indicator_map1 = {u'1': u'Single scale', u'0': u'Scale indeterminable/No scale recorded', u'3': u'Range of scales'}
    indicator_map2 = {u'1': u'Exclusion ring', u'0': u'Outer ring', u'#': u'Not applicable'}
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

@marc21.over('language_code', '^041[10.].')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    indicator_map1 = {u'1': u'Item is or includes a translation', u'0': u'Item not a translation/does not include a\n                  \t\t\t\t\t\ttranslation', u'#': u'No information provided'}
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

@marc21.over('time_period_of_content', '^045[10.2].')
@utils.filter_values
def time_period_of_content(self, key, value):
    indicator_map1 = {u'1': u'Multiple single dates/times', u'0': u'Single date/time', u'#': u'Subfield $b or $c not present', u'2': u'Range of dates/times'}
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

@marc21.over('library_of_congress_call_number', '^050[10.][04]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    indicator_map1 = {u'1': u'Item is not in LC', u'0': u'Item is in LC', u'#': u'No information provided'}
    indicator_map2 = {u'0': u'Assigned by LC', u'4': u'Assigned by agency other than LC'}
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

@marc21.over('classification_numbers_assigned_in_canada', '^055[10.][1032547698]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    indicator_map1 = {u'1': u'Work not held by LAC', u'0': u'Work held by LAC', u'#': u'Information not provided'}
    indicator_map2 = {u'1': u'Complete LC class number assigned by LAC', u'0': u'LC-based call number assigned by LAC', u'3': u'LC-based call number assigned by the contributing library', u'2': u'Incomplete LC class number assigned by LAC', u'5': u'Incomplete LC class number assigned by the contributing library', u'4': u'Complete LC class number assigned by the contributing library', u'7': u'Other class number assigned by LAC', u'6': u'Other call number assigned by LAC', u'9': u'Other class number assigned by the contributing library', u'8': u'Other call number assigned by the contributing library'}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_call_class_number': value.get('2'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4]),
    }

@marc21.over('national_library_of_medicine_call_number', '^060[10.][04]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    indicator_map1 = {u'1': u'Item is not in NLM', u'0': u'Item is in NLM', u'#': u'No information provided'}
    indicator_map2 = {u'0': u'Assigned by NLM', u'4': u'Assigned by agency other than NLM'}
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

@marc21.over('national_agricultural_library_call_number', '^070[10].')
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

@marc21.over('universal_decimal_classification_number', '^080[10.].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    indicator_map1 = {u'1': u'Abridged', u'0': u'Full', u'#': u'No information provided'}
    return {
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'edition_identifier': value.get('2'),
        'common_auxiliary_subdivision': value.get('x'),
        'field_link_and_sequence_number': value.get('8'),
        'type_of_edition': indicator_map1.get(key[3]),
    }

@marc21.over('dewey_decimal_classification_number', '^082[107][0.4]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    indicator_map1 = {u'1': u'Abridged edition', u'0': u'Full edition', u'7': u'Other edition specified in subfield $2'}
    indicator_map2 = {u'0': u'Assigned by LC', u'#': u'No information provided', u'4': u'Assigned by agency other than LC'}
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

@marc21.over('additional_dewey_decimal_classification_number', '^083[107].')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    indicator_map1 = {u'1': u'Abridged edition', u'0': u'Full edition', u'7': u'Other edition specified in subfield $2'}
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

@marc21.over('main_entry_personal_name', '^100[103].')
@utils.filter_values
def main_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    return {
        'personal_name': value.get('a'),
        'titles_and_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'attribution_qualifier': value.get('j'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_of_a_work': value.get('n'),
        'fuller_form_of_name': value.get('q'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
    }

@marc21.over('main_entry_corporate_name', '^110[102].')
@utils.filter_values
def main_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_meeting': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number_r': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
    }

@marc21.over('main_entry_meeting_name', '^111[102].')
@utils.filter_values
def main_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'relator_term': value.get('j'),
        'language_of_a_work': value.get('l'),
        'name_of_part_section_of_a_work': value.get('p'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'authority_record_control_number': value.get('0'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
    }

@marc21.over('main_entry_uniform_title', '^130..')
@utils.filter_values
def main_entry_uniform_title(self, key, value):
    return {
        'uniform_title': value.get('a'),
        'name_of_part_section_of_a_work': value.get('p'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('abbreviated_title', '^210[10][0.]')
@utils.for_each_value
@utils.filter_values
def abbreviated_title(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'Other abbreviated title', u'#': u'Abbreviated key title'}
    return {
        'abbreviated_title': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'title_added_entry': indicator_map1.get(key[3]),
        'type': indicator_map2.get(key[4]),
    }

@marc21.over('key_title', '^222.[0]')
@utils.for_each_value
@utils.filter_values
def key_title(self, key, value):
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'key_title': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'qualifying_information': value.get('b'),
        'linkage': value.get('6'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('uniform_title', '^240[10].')
@utils.filter_values
def uniform_title(self, key, value):
    indicator_map1 = {u'1': u'Printed or displayed', u'0': u'Not printed or displayed'}
    return {
        'uniform_title': value.get('a'),
        'name_of_part_section_of_a_work': value.get('p'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
    }

@marc21.over('translation_of_title_by_cataloging_agency', '^242[10][0]')
@utils.for_each_value
@utils.filter_values
def translation_of_title_by_cataloging_agency(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'statement_of_responsibility_': value.get('c'),
        'remainder_of_title': value.get('b'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'linkage': value.get('6'),
        'language_code_of_translated_title': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('collective_uniform_title', '^243[10].')
@utils.filter_values
def collective_uniform_title(self, key, value):
    indicator_map1 = {u'1': u'Printed or displayed', u'0': u'Not printed or displayed'}
    return {
        'uniform_title': value.get('a'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title_printed_or_displayed': indicator_map1.get(key[3]),
    }

@marc21.over('title_statement', '^245[10][0]')
@utils.filter_values
def title_statement(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'statement_of_responsibility_': value.get('c'),
        'remainder_of_title': value.get('b'),
        'bulk_dates': value.get('g'),
        'inclusive_dates': value.get('f'),
        'medium': value.get('h'),
        'form': value.get('k'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('varying_form_of_title', '^246[1032][.103254768]')
@utils.for_each_value
@utils.filter_values
def varying_form_of_title(self, key, value):
    indicator_map1 = {u'1': u'Note, added entry', u'0': u'Note, no added entry', u'3': u'No note, added entry', u'2': u'No note, no added entry'}
    indicator_map2 = {u'#': u'No type specified', u'1': u'Parallel title', u'0': u'Portion of title', u'3': u'Other title', u'2': u'Distinctive title', u'5': u'Added title page title', u'4': u'Cover title', u'7': u'Running title', u'6': u'Caption title', u'8': u'Spine title'}
    return {
        'title_proper_short_title': value.get('a'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'display_text': value.get('i'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'note_added_entry_controller': indicator_map1.get(key[3]),
        'type_of_title': indicator_map2.get(key[4]),
    }

@marc21.over('former_title', '^247[10][10]')
@utils.for_each_value
@utils.filter_values
def former_title(self, key, value):
    indicator_map1 = {u'1': u'Added entry', u'0': u'No added entry'}
    indicator_map2 = {u'1': u'Do not display note', u'0': u'Display note'}
    return {
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'remainder_of_title': value.get('b'),
        'miscellaneous_information': value.get('g'),
        'date_or_sequential_designation': value.get('f'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_added_entry': indicator_map1.get(key[3]),
        'note_controller': indicator_map2.get(key[4]),
    }

@marc21.over('edition_statement', '^250..')
@utils.for_each_value
@utils.filter_values
def edition_statement(self, key, value):
    return {
        'edition_statement': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'materials_specified': value.get('3'),
        'remainder_of_edition_statement': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('musical_presentation_statement', '^254..')
@utils.filter_values
def musical_presentation_statement(self, key, value):
    return {
        'musical_presentation_statement': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('cartographic_mathematical_data', '^255..')
@utils.for_each_value
@utils.filter_values
def cartographic_mathematical_data(self, key, value):
    return {
        'statement_of_scale': value.get('a'),
        'statement_of_coordinates': value.get('c'),
        'statement_of_projection': value.get('b'),
        'statement_of_equinox': value.get('e'),
        'statement_of_zone': value.get('d'),
        'exclusion_g_ring_coordinate_pairs': value.get('g'),
        'outer_g_ring_coordinate_pairs': value.get('f'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('computer_file_characteristics', '^256..')
@utils.filter_values
def computer_file_characteristics(self, key, value):
    return {
        'computer_file_characteristics': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('country_of_producing_entity', '^257..')
@utils.for_each_value
@utils.filter_values
def country_of_producing_entity(self, key, value):
    return {
        'country_of_producing_entity': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'linkage': value.get('6'),
    }

@marc21.over('philatelic_issue_data', '^258..')
@utils.for_each_value
@utils.filter_values
def philatelic_issue_data(self, key, value):
    return {
        'issuing_jurisdiction': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'denomination': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('publication_distribution__imprint', '^260[.23].')
@utils.for_each_value
@utils.filter_values
def publication_distribution__imprint(self, key, value):
    indicator_map1 = {u'#': u'Not applicable/No information provided/Earliest available publisher', u'2': u'Intervening publisher', u'3': u'Current/latest publisher'}
    return {
        'place_of_publication_distribution_': value.get('a'),
        'date_of_publication_distribution_': value.get('c'),
        'name_of_publisher_distributor_': value.get('b'),
        'place_of_manufacture': value.get('e'),
        'date_of_manufacture': value.get('g'),
        'manufacturer': value.get('f'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'sequence_of_publishing_statements': indicator_map1.get(key[3]),
    }

@marc21.over('imprint_statement_for_films_pre_aacr_1_revised', '^261..')
@utils.filter_values
def imprint_statement_for_films_pre_aacr_1_revised(self, key, value):
    return {
        'producing_company': value.get('a'),
        'releasing_company': value.get('b'),
        'contractual_producer': value.get('e'),
        'date_of_production_release_': value.get('d'),
        'place_of_production_release_': value.get('f'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('imprint_statement_for_sound_recordings_pre_aacr_1', '^262..')
@utils.filter_values
def imprint_statement_for_sound_recordings_pre_aacr_1(self, key, value):
    return {
        'place_of_production_release_': value.get('a'),
        'date_of_production_release_': value.get('c'),
        'publisher_or_trade_name': value.get('b'),
        'serial_identification': value.get('k'),
        'matrix_and_or_take_number': value.get('l'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('projected_publication_date', '^263..')
@utils.filter_values
def projected_publication_date(self, key, value):
    return {
        'projected_publication_date': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('production_publication_distribution_manufacture_and_copyright_notice', '^264[.23][10324]')
@utils.for_each_value
@utils.filter_values
def production_publication_distribution_manufacture_and_copyright_notice(self, key, value):
    indicator_map1 = {u'#': u'Not applicable/No information provided/Earliest', u'2': u'Intervening', u'3': u'Current/latest'}
    indicator_map2 = {u'1': u'Publication', u'0': u'Production', u'3': u'Manufacture', u'2': u'Distribution', u'4': u'Copyright notice date'}
    return {
        'place_of_production_publication_distribution_manufacture': value.get('a'),
        'date_of_production_publication_distribution_manufacture_or_copyright_notice': value.get('c'),
        'name_of_producer_publisher_distributor_manufacturer': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'sequence_of_statements': indicator_map1.get(key[3]),
        'function_of_entity': indicator_map2.get(key[4]),
    }

@marc21.over('address', '^270[1.2].')
@utils.for_each_value
@utils.filter_values
def address(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'#': u'No level specified', u'2': u'Secondary'}
    return {
        'address': value.get('a'),
        'state_or_province': value.get('c'),
        'city': value.get('b'),
        'postal_code': value.get('e'),
        'country': value.get('d'),
        'attention_name': value.get('g'),
        'terms_preceding_attention_name': value.get('f'),
        'type_of_address': value.get('i'),
        'attention_position': value.get('h'),
        'telephone_number': value.get('k'),
        'specialized_telephone_number': value.get('j'),
        'electronic_mail_address': value.get('m'),
        'fax_number': value.get('l'),
        'tdd_or_tty_number': value.get('n'),
        'title_of_contact_person': value.get('q'),
        'contact_person': value.get('p'),
        'hours': value.get('r'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'public_note': value.get('z'),
        'level': indicator_map1.get(key[3]),
    }

@marc21.over('physical_description', '^300..')
@utils.for_each_value
@utils.filter_values
def physical_description(self, key, value):
    return {
        'extent': value.get('a'),
        'dimensions': value.get('c'),
        'other_physical_details': value.get('b'),
        'accompanying_material': value.get('e'),
        'size_of_unit': value.get('g'),
        'type_of_unit': value.get('f'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('playing_time', '^306..')
@utils.filter_values
def playing_time(self, key, value):
    return {
        'playing_time': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('hours_', '^307[8.].')
@utils.for_each_value
@utils.filter_values
def hours_(self, key, value):
    indicator_map1 = {u'8': u'No display constant generated', u'#': u'Hours'}
    return {
        'hours': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'additional_information': value.get('b'),
        'linkage': value.get('6'),
        'display_constant_controller': indicator_map1.get(key[3]),
    }

@marc21.over('current_publication_frequency', '^310..')
@utils.filter_values
def current_publication_frequency(self, key, value):
    return {
        'current_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'date_of_current_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('former_publication_frequency', '^321..')
@utils.for_each_value
@utils.filter_values
def former_publication_frequency(self, key, value):
    return {
        'former_publication_frequency': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'dates_of_former_publication_frequency': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('content_type', '^336..')
@utils.for_each_value
@utils.filter_values
def content_type(self, key, value):
    return {
        'content_type_term': value.get('a'),
        'content_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('media_type', '^337..')
@utils.for_each_value
@utils.filter_values
def media_type(self, key, value):
    return {
        'media_type_term': value.get('a'),
        'media_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('carrier_type', '^338..')
@utils.for_each_value
@utils.filter_values
def carrier_type(self, key, value):
    return {
        'carrier_type_term': value.get('a'),
        'carrier_type_code': value.get('b'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('physical_medium', '^340..')
@utils.for_each_value
@utils.filter_values
def physical_medium(self, key, value):
    return {
        'material_base_and_configuration': value.get('a'),
        'materials_applied_to_surface': value.get('c'),
        'dimensions': value.get('b'),
        'support': value.get('e'),
        'information_recording_technique': value.get('d'),
        'production_rate_ratio': value.get('f'),
        'technical_specifications_of_medium': value.get('i'),
        'location_within_medium': value.get('h'),
        'layout': value.get('k'),
        'generation': value.get('j'),
        'book_format': value.get('m'),
        'polarity': value.get('o'),
        'font_size': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('geospatial_reference_data', '^342[10][103254768]')
@utils.for_each_value
@utils.filter_values
def geospatial_reference_data(self, key, value):
    indicator_map1 = {u'1': u'Vertical coordinate system', u'0': u'Horizontal coordinate system'}
    indicator_map2 = {u'1': u'Map projection', u'0': u'Geographic', u'3': u'Local planar', u'2': u'Grid coordinate system', u'5': u'Geodetic model', u'4': u'Local', u'7': u'Method specified in $2', u'6': u'Altitude', u'8': u'Depth'}
    return {
        'reference_method_used': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'name': value.get('a'),
        'latitude_resolution': value.get('c'),
        'coordinate_units_or_distance_units': value.get('b'),
        'standard_parallel_or_oblique_line_latitude': value.get('e'),
        'longitude_resolution': value.get('d'),
        'longitude_of_central_meridian_or_projection_center': value.get('g'),
        'oblique_line_longitude': value.get('f'),
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

@marc21.over('planar_coordinate_data', '^343..')
@utils.for_each_value
@utils.filter_values
def planar_coordinate_data(self, key, value):
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
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('sound_characteristics', '^344..')
@utils.for_each_value
@utils.filter_values
def sound_characteristics(self, key, value):
    return {
        'type_of_recording': value.get('a'),
        'playing_speed': value.get('c'),
        'recording_medium': value.get('b'),
        'track_configuration': value.get('e'),
        'groove_characteristic': value.get('d'),
        'configuration_of_playback_channels': value.get('g'),
        'tape_configuration': value.get('f'),
        'special_playback_characteristics': value.get('h'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('projection_characteristics_of_moving_image', '^345..')
@utils.for_each_value
@utils.filter_values
def projection_characteristics_of_moving_image(self, key, value):
    return {
        'presentation_format': value.get('a'),
        'projection_speed': value.get('b'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('video_characteristics', '^346..')
@utils.for_each_value
@utils.filter_values
def video_characteristics(self, key, value):
    return {
        'video_format': value.get('a'),
        'broadcast_standard': value.get('b'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('digital_file_characteristics', '^347..')
@utils.for_each_value
@utils.filter_values
def digital_file_characteristics(self, key, value):
    return {
        'file_type': value.get('a'),
        'file_size': value.get('c'),
        'encoding_format': value.get('b'),
        'regional_encoding': value.get('e'),
        'resolution': value.get('d'),
        'transmission_speed': value.get('f'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('organization_and_arrangement_of_materials', '^351..')
@utils.for_each_value
@utils.filter_values
def organization_and_arrangement_of_materials(self, key, value):
    return {
        'organization': value.get('a'),
        'hierarchical_level': value.get('c'),
        'arrangement': value.get('b'),
        'materials_specified': value.get('3'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('digital_graphic_representation', '^352..')
@utils.for_each_value
@utils.filter_values
def digital_graphic_representation(self, key, value):
    return {
        'direct_reference_method': value.get('a'),
        'object_count': value.get('c'),
        'object_type': value.get('b'),
        'column_count': value.get('e'),
        'row_count': value.get('d'),
        'vpf_topology_level': value.get('g'),
        'vertical_count': value.get('f'),
        'indirect_reference_description': value.get('i'),
        'format_of_the_digital_image': value.get('q'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('security_classification_control', '^355[1032548].')
@utils.for_each_value
@utils.filter_values
def security_classification_control(self, key, value):
    indicator_map1 = {u'1': u'Title', u'0': u'Document', u'3': u'Contents note', u'2': u'Abstract', u'5': u'Record', u'4': u'Author', u'8': u'None of the above'}
    return {
        'security_classification': value.get('a'),
        'external_dissemination_information': value.get('c'),
        'handling_instructions': value.get('b'),
        'classification_system': value.get('e'),
        'downgrading_or_declassification_event': value.get('d'),
        'downgrading_date': value.get('g'),
        'country_of_origin_code': value.get('f'),
        'declassification_date': value.get('h'),
        'authorization': value.get('j'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'controlled_element': indicator_map1.get(key[3]),
    }

@marc21.over('originator_dissemination_control', '^357..')
@utils.filter_values
def originator_dissemination_control(self, key, value):
    return {
        'originator_control_term': value.get('a'),
        'authorized_recipients_of_material': value.get('c'),
        'originating_agency': value.get('b'),
        'other_restrictions': value.get('g'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('dates_of_publication_and_or_sequential_designation', '^362[10].')
@utils.for_each_value
@utils.filter_values
def dates_of_publication_and_or_sequential_designation(self, key, value):
    indicator_map1 = {u'1': u'Unformatted note', u'0': u'Formatted style'}
    return {
        'dates_of_publication_and_or_sequential_designation': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source_of_information': value.get('z'),
        'linkage': value.get('6'),
        'format_of_date': indicator_map1.get(key[3]),
    }

@marc21.over('normalized_date_and_sequential_designation', '^363[10.][10.]')
@utils.for_each_value
@utils.filter_values
def normalized_date_and_sequential_designation(self, key, value):
    indicator_map1 = {u'1': u'Ending information', u'0': u'Starting information', u'#': u'No information provided'}
    indicator_map2 = {u'1': u'Open', u'0': u'Closed', u'#': u'Not specified'}
    return {
        'first_level_of_enumeration': value.get('a'),
        'nonpublic_note': value.get('x'),
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
        'public_note': value.get('z'),
        'first_level_of_chronology_issuance': value.get('v'),
        'start_end_designator': indicator_map1.get(key[3]),
        'state_of_issuance': indicator_map2.get(key[4]),
    }

@marc21.over('trade_price', '^365..')
@utils.for_each_value
@utils.filter_values
def trade_price(self, key, value):
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
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('trade_availability_information', '^366..')
@utils.for_each_value
@utils.filter_values
def trade_availability_information(self, key, value):
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
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('associated_language', '^377..')
@utils.for_each_value
@utils.filter_values
def associated_language(self, key, value):
    return {
        'language_code': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'source': value.get('2'),
        'language_term': value.get('l'),
        'linkage': value.get('6'),
    }

@marc21.over('form_of_work', '^380..')
@utils.for_each_value
@utils.filter_values
def form_of_work(self, key, value):
    return {
        'form_of_work': value.get('a'),
        'record_control_number': value.get('0'),
        'source_of_term': value.get('2'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
    }

@marc21.over('other_distinguishing_characteristics_of_work_or_expression', '^381..')
@utils.for_each_value
@utils.filter_values
def other_distinguishing_characteristics_of_work_or_expression(self, key, value):
    return {
        'other_distinguishing_characteristic': value.get('a'),
        'source_of_information': value.get('v'),
        'record_control_number': value.get('0'),
        'source_of_term': value.get('2'),
        'uniform_resource_identifier': value.get('u'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('medium_of_performance', '^382[10.][10.]')
@utils.for_each_value
@utils.filter_values
def medium_of_performance(self, key, value):
    indicator_map1 = {u'1': u'Partial medium of performance', u'0': u'Medium of performance', u'#': u'No information provided'}
    indicator_map2 = {u'1': u'Intended for access', u'0': u'Not intended for access', u'#': u'No information provided'}
    return {
        'medium_of_performance': value.get('a'),
        'soloist': value.get('b'),
        'doubling_instrument': value.get('d'),
        'alternative_medium_of_performance': value.get('p'),
        'note': value.get('v'),
        'number_of_performers_of_the_same_medium': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'total_number_of_performers': value.get('s'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'display_constant_controller': indicator_map1.get(key[3]),
        'access_control': indicator_map2.get(key[4]),
    }

@marc21.over('numeric_designation_of_musical_work', '^383..')
@utils.for_each_value
@utils.filter_values
def numeric_designation_of_musical_work(self, key, value):
    return {
        'serial_number': value.get('a'),
        'thematic_index_number': value.get('c'),
        'opus_number': value.get('b'),
        'publisher_associated_with_opus_number': value.get('e'),
        'thematic_index_code': value.get('d'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('key', '^384[10.].')
@utils.filter_values
def key(self, key, value):
    indicator_map1 = {u'1': u'Transposed key ', u'0': u'Original key ', u'#': u'Relationship to original unknown '}
    return {
        'key': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'key_type': indicator_map1.get(key[3]),
    }

@marc21.over('audience_characteristics', '^385..')
@utils.for_each_value
@utils.filter_values
def audience_characteristics(self, key, value):
    return {
        'audience_term': value.get('a'),
        'audience_code': value.get('b'),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('creator_contributor_characteristics', '^386..')
@utils.for_each_value
@utils.filter_values
def creator_contributor_characteristics(self, key, value):
    return {
        'creator_contributor_term': value.get('a'),
        'creator_contributor_code': value.get('b'),
        'demographic_group_term': value.get('m'),
        'demographic_group_code': value.get('n'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('series_statement_added_entry_personal_name', '^400[103][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'personal_name': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'titles_and_other_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_corporate_name', '^410[102][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_meeting_name', '^411[102][10]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u'Main entry represented by pronoun', u'0': u'Main entry not represented by pronoun'}
    return {
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'form_subheading': value.get('k'),
        'volume_sequential_designation': value.get('v'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'affiliation': value.get('u'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'title_of_a_work': value.get('t'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'pronoun_represents_main_entry': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement_added_entry_title', '^440.[0]')
@utils.for_each_value
@utils.filter_values
def series_statement_added_entry_title(self, key, value):
    indicator_map2 = {u'0': u'No nonfiling characters'}
    return {
        'title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': value.get('p'),
        'volume_sequential_designation': value.get('v'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'bibliographic_record_control_number': value.get('w'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'nonfiling_characters': indicator_map2.get(key[4]),
    }

@marc21.over('series_statement', '^490[10].')
@utils.for_each_value
@utils.filter_values
def series_statement(self, key, value):
    indicator_map1 = {u'1': u'Series traced', u'0': u'Series not traced'}
    return {
        'series_statement': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'linkage': value.get('6'),
        'library_of_congress_call_number': value.get('l'),
        'materials_specified': value.get('3'),
        'volume_sequential_designation': value.get('v'),
        'field_link_and_sequence_number': value.get('8'),
        'series_tracing_policy': indicator_map1.get(key[3]),
    }

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

@marc21.over('bibliography__note', '^504..')
@utils.for_each_value
@utils.filter_values
def bibliography__note(self, key, value):
    return {
        'bibliography__note': value.get('a'),
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

@marc21.over('summary_', '^520[.103248].')
@utils.for_each_value
@utils.filter_values
def summary_(self, key, value):
    indicator_map1 = {u'#': u'Summary', u'1': u'Review', u'0': u'Subject', u'3': u'Abstract', u'2': u'Scope and content', u'4': u'Content advice', u'8': u'No display constant generated'}
    return {
        'summary_': value.get('a'),
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
        'publication_distribution__of_original': value.get('c'),
        'edition_statement_of_original': value.get('b'),
        'physical_description__of_original': value.get('e'),
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

@marc21.over('subject_added_entry_personal_name', '^600[103][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'attribution_qualifier': value.get('j'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_corporate_name', '^610[102][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_meeting_name', '^611[102][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'relator_term': value.get('j'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_uniform_title', '^630.[10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_uniform_title(self, key, value):
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'uniform_title': value.get('a'),
        'relator_term': value.get('e'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'title_of_a_work': value.get('t'),
        'form_subdivision': value.get('v'),
        'chronological_subdivision': value.get('y'),
        'general_subdivision': value.get('x'),
        'geographic_subdivision': value.get('z'),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_chronological_term', '^648[10.][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_chronological_term(self, key, value):
    indicator_map1 = {u'1': u'Date or time period of creation or origin', u'0': u'Date or time period covered or depicted', u'#': u'No information provided'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xc3\xa9pertoire de vedettes-mati\xc3\xa8re'}
    return {
        'chronological_term': value.get('a'),
        'general_subdivision': value.get('x'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number_or_standard_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'type_of_date_or_time_period': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_topical_term', '^650[10.2][10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_topical_term(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'topical_term_or_geographic_name_entry_element': value.get('a'),
        'general_subdivision': value.get('x'),
        'location_of_event': value.get('c'),
        'topical_term_following_geographic_name_entry_element': value.get('b'),
        'relator_term': value.get('e'),
        'active_dates': value.get('d'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'level_of_subject': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_geographic_name', '^651.[10325476]')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_geographic_name(self, key, value):
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'geographic_name': value.get('a'),
        'general_subdivision': value.get('x'),
        'relator_term': value.get('e'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('index_term_uncontrolled', '^653[10.2][.1032546]')
@utils.for_each_value
@utils.filter_values
def index_term_uncontrolled(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    indicator_map2 = {u'#': u'No information provided', u'1': u'Personal name', u'0': u'Topical term', u'3': u'Meeting name', u'2': u'Corporate name', u'5': u'Geographic name', u'4': u'Chronological term', u'6': u'Genre/form term'}
    return {
        'uncontrolled_term': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'linkage': value.get('6'),
        'level_of_index_term': indicator_map1.get(key[3]),
        'type_of_term_or_name': indicator_map2.get(key[4]),
    }

@marc21.over('subject_added_entry_faceted_topical_terms', '^654[10.2].')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_faceted_topical_terms(self, key, value):
    indicator_map1 = {u'1': u'Primary', u'0': u'No level specified', u'#': u'No information provided', u'2': u'Secondary'}
    return {
        'focus_term': value.get('a'),
        'facet_hierarchy_designation': value.get('c'),
        'non_focus_term': value.get('b'),
        'relator_term': value.get('e'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'level_of_subject': indicator_map1.get(key[3]),
    }

@marc21.over('index_term_genre_form', '^655[0.][10325476]')
@utils.for_each_value
@utils.filter_values
def index_term_genre_form(self, key, value):
    indicator_map1 = {u'0': u'Faceted', u'#': u'Basic'}
    indicator_map2 = {u'1': u"LC subject headings for children's literature", u'0': u'Library of Congress Subject Headings', u'3': u'National Agricultural Library subject authority file', u'2': u'Medical Subject Headings', u'5': u'Canadian Subject Headings', u'4': u'Source not specified', u'7': u'Source specified in subfield $2', u'6': u'R\xe9pertoire de vedettes-mati\xe8re'}
    return {
        'genre_form_data_or_focus_term': value.get('a'),
        'general_subdivision': value.get('x'),
        'facet_hierarchy_designation': value.get('c'),
        'non_focus_term': value.get('b'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
        'type_of_heading': indicator_map1.get(key[3]),
        'thesaurus': indicator_map2.get(key[4]),
    }

@marc21.over('index_term_occupation', '^656..')
@utils.for_each_value
@utils.filter_values
def index_term_occupation(self, key, value):
    return {
        'occupation': value.get('a'),
        'general_subdivision': value.get('x'),
        'form': value.get('k'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
    }

@marc21.over('index_term_function', '^657..')
@utils.for_each_value
@utils.filter_values
def index_term_function(self, key, value):
    return {
        'function': value.get('a'),
        'general_subdivision': value.get('x'),
        'form_subdivision': value.get('v'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_term': value.get('2'),
        'linkage': value.get('6'),
        'chronological_subdivision': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'geographic_subdivision': value.get('z'),
    }

@marc21.over('index_term_curriculum_objective', '^658..')
@utils.for_each_value
@utils.filter_values
def index_term_curriculum_objective(self, key, value):
    return {
        'main_curriculum_objective': value.get('a'),
        'curriculum_code': value.get('c'),
        'subordinate_curriculum_objective': value.get('b'),
        'correlation_factor': value.get('d'),
        'source_of_term_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('subject_added_entry_hierarchical_place_name', '^662..')
@utils.for_each_value
@utils.filter_values
def subject_added_entry_hierarchical_place_name(self, key, value):
    return {
        'country_or_larger_entity': value.get('a'),
        'intermediate_political_jurisdiction': value.get('c'),
        'first_order_political_jurisdiction': value.get('b'),
        'relator_term': value.get('e'),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': value.get('g'),
        'city_subsection': value.get('f'),
        'extraterrestrial_area': value.get('h'),
        'authority_record_control_number': value.get('0'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('added_entry_personal_name', '^700[103][.2]')
@utils.for_each_value
@utils.filter_values
def added_entry_personal_name(self, key, value):
    indicator_map1 = {u'1': u'Surname', u'0': u'Forename', u'3': u'Family name'}
    indicator_map2 = {u'#': u'No information provided', u'2': u'Analytical entry'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'personal_name': value.get('a'),
        'titles_and_other_words_associated_with_a_name': value.get('c'),
        'numeration': value.get('b'),
        'relator_term': value.get('e'),
        'dates_associated_with_a_name': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': value.get('i'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'attribution_qualifier': value.get('j'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'fuller_form_of_name': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_personal_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }

@marc21.over('added_entry_corporate_name', '^710[102][.2]')
@utils.for_each_value
@utils.filter_values
def added_entry_corporate_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'#': u'No information provided', u'2': u'Analytical entry'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'corporate_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('b'),
        'relator_term': value.get('e'),
        'date_of_meeting_or_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': value.get('i'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'key_for_music': value.get('r'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_corporate_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }

@marc21.over('added_entry_meeting_name', '^711[102][.2]')
@utils.for_each_value
@utils.filter_values
def added_entry_meeting_name(self, key, value):
    indicator_map1 = {u'1': u'Jurisdiction name', u'0': u'Inverted name', u'2': u'Name in direct order'}
    indicator_map2 = {u'#': u'No information provided', u'2': u'Analytical entry'}
    return {
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'institution_to_which_field_applies': value.get('5'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'meeting_name_or_jurisdiction_name_as_entry_element': value.get('a'),
        'location_of_meeting': value.get('c'),
        'subordinate_unit': value.get('e'),
        'date_of_meeting': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': value.get('i'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'relator_term': value.get('j'),
        'language_of_a_work': value.get('l'),
        'number_of_part_section_meeting': value.get('n'),
        'name_of_meeting_following_jurisdiction_name_entry_element': value.get('q'),
        'name_of_part_section_of_a_work': value.get('p'),
        'version': value.get('s'),
        'affiliation': value.get('u'),
        'title_of_a_work': value.get('t'),
        'international_standard_serial_number': value.get('x'),
        'type_of_meeting_name_entry_element': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }

@marc21.over('added_entry_uncontrolled_name', '^720[1.2].')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_name(self, key, value):
    indicator_map1 = {u'1': u'Personal', u'#': u'Not specified', u'2': u'Other'}
    return {
        'name': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'relator_term': value.get('e'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'type_of_name': indicator_map1.get(key[3]),
    }

@marc21.over('added_entry_uniform_title', '^730.[.2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uniform_title(self, key, value):
    indicator_map2 = {u'#': u'No information provided', u'2': u'Analytical entry'}
    return {
        'uniform_title': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'name_of_part_section_of_a_work': value.get('p'),
        'date_of_treaty_signing': value.get('d'),
        'miscellaneous_information': value.get('g'),
        'date_of_a_work': value.get('f'),
        'relationship_information': value.get('i'),
        'medium': value.get('h'),
        'form_subheading': value.get('k'),
        'medium_of_performance_for_music': value.get('m'),
        'language_of_a_work': value.get('l'),
        'arranged_statement_for_music': value.get('o'),
        'number_of_part_section_of_a_work': value.get('n'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'key_for_music': value.get('r'),
        'institution_to_which_field_applies': value.get('5'),
        'title_of_a_work': value.get('t'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'version': value.get('s'),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }

@marc21.over('added_entry_uncontrolled_related_analytical_title', '^740[0][.2]')
@utils.for_each_value
@utils.filter_values
def added_entry_uncontrolled_related_analytical_title(self, key, value):
    indicator_map1 = {u'0': u'No nonfiling characters'}
    indicator_map2 = {u'#': u'No information provided', u'2': u'Analytical entry'}
    return {
        'uncontrolled_related_analytical_title': value.get('a'),
        'medium': value.get('h'),
        'number_of_part_section_of_a_work': value.get('n'),
        'name_of_part_section_of_a_work': value.get('p'),
        'institution_to_which_field_applies': value.get('5'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'nonfiling_characters': indicator_map1.get(key[3]),
        'type_of_added_entry': indicator_map2.get(key[4]),
    }

@marc21.over('added_entry_geographic_name', '^751..')
@utils.for_each_value
@utils.filter_values
def added_entry_geographic_name(self, key, value):
    return {
        'geographic_name': value.get('a'),
        'relator_term': value.get('e'),
        'authority_record_control_number': value.get('0'),
        'materials_specified': value.get('3'),
        'source_of_heading_or_term': value.get('2'),
        'relator_code': value.get('4'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('added_entry_hierarchical_place_name', '^752..')
@utils.for_each_value
@utils.filter_values
def added_entry_hierarchical_place_name(self, key, value):
    return {
        'country_or_larger_entity': value.get('a'),
        'intermediate_political_jurisdiction': value.get('c'),
        'first_order_political_jurisdiction': value.get('b'),
        'city': value.get('d'),
        'other_nonjurisdictional_geographic_region_and_feature': value.get('g'),
        'city_subsection': value.get('f'),
        'extraterrestrial_area': value.get('h'),
        'authority_record_control_number': value.get('0'),
        'source_of_heading_or_term': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
    }

@marc21.over('system_details_access_to_computer_files', '^753..')
@utils.for_each_value
@utils.filter_values
def system_details_access_to_computer_files(self, key, value):
    return {
        'make_and_model_of_machine': value.get('a'),
        'field_link_and_sequence_number': value.get('8'),
        'operating_system': value.get('c'),
        'programming_language': value.get('b'),
        'linkage': value.get('6'),
    }

@marc21.over('added_entry_taxonomic_identification', '^754..')
@utils.for_each_value
@utils.filter_values
def added_entry_taxonomic_identification(self, key, value):
    return {
        'taxonomic_name': value.get('a'),
        'non_public_note': value.get('x'),
        'taxonomic_category': value.get('c'),
        'common_or_alternative_name': value.get('d'),
        'authority_record_control_number': value.get('0'),
        'source_of_taxonomic_identification': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'public_note': value.get('z'),
    }

@marc21.over('main_series_entry', '^760[10][8.]')
@utils.for_each_value
@utils.filter_values
def main_series_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Main series'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('subseries_entry', '^762[10][8.]')
@utils.for_each_value
@utils.filter_values
def subseries_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Has subseries'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('original_language_entry', '^765[10][8.]')
@utils.for_each_value
@utils.filter_values
def original_language_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Translation of'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('translation_entry', '^767[10][8.]')
@utils.for_each_value
@utils.filter_values
def translation_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Translated as'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('supplement_special_issue_entry', '^770[10][8.]')
@utils.for_each_value
@utils.filter_values
def supplement_special_issue_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Has supplement'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('supplement_parent_entry', '^772[10][0.8]')
@utils.for_each_value
@utils.filter_values
def supplement_parent_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'0': u'Parent', u'#': u'Supplement to', u'8': u'No display constant generated'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('host_item_entry', '^773[10][8.]')
@utils.for_each_value
@utils.filter_values
def host_item_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'In'}
    return {
        'materials_specified': value.get('3'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'enumeration_and_first_page': value.get('q'),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('constituent_unit_entry', '^774[10][8.]')
@utils.for_each_value
@utils.filter_values
def constituent_unit_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Constituent unit'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('other_edition_entry', '^775[10][8.]')
@utils.for_each_value
@utils.filter_values
def other_edition_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Other edition available'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'language_code': value.get('e'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'country_code': value.get('f'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('additional_physical_form_entry', '^776[10][8.]')
@utils.for_each_value
@utils.filter_values
def additional_physical_form_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Available in another form'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('issued_with_entry', '^777[10][8.]')
@utils.for_each_value
@utils.filter_values
def issued_with_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Issued with'}
    return {
        'main_entry_heading': value.get('a'),
        'international_standard_serial_number': value.get('x'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'record_control_number': value.get('w'),
        'uniform_title': value.get('s'),
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'coden_designation': value.get('y'),
        'field_link_and_sequence_number': value.get('8'),
        'title': value.get('t'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('preceding_entry', '^780[10][10325476]')
@utils.for_each_value
@utils.filter_values
def preceding_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'1': u'Continues in part', u'0': u'Continues', u'3': u'Supersedes in part', u'2': u'Supersedes', u'5': u'Absorbed', u'4': u'Formed by the union of ... and ...', u'7': u'Separated from', u'6': u'Absorbed in part'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }

@marc21.over('succeeding_entry', '^785[10][103254768]')
@utils.for_each_value
@utils.filter_values
def succeeding_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'1': u'Continued in part by', u'0': u'Continued by', u'3': u'Superseded in part by', u'2': u'Superseded by', u'5': u'Absorbed in part by', u'4': u'Absorbed by', u'7': u'Merged with ... to form ...', u'6': u'Split into ... and ...', u'8': u'Changed back to'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'type_of_relationship': indicator_map2.get(key[4]),
    }

@marc21.over('data_source_entry', '^786[10][8.]')
@utils.for_each_value
@utils.filter_values
def data_source_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Data source'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'period_of_content': value.get('j'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'abbreviated_title': value.get('p'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'source_contribution': value.get('v'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }

@marc21.over('other_relationship_entry', '^787[10][8.]')
@utils.for_each_value
@utils.filter_values
def other_relationship_entry(self, key, value):
    indicator_map1 = {u'1': u'Do not display note', u'0': u'Display note'}
    indicator_map2 = {u'8': u'No display constant generated', u'#': u'Related item'}
    return {
        'relationship_code': value.get('4'),
        'control_subfield': value.get('7'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': value.get('8'),
        'main_entry_heading': value.get('a'),
        'qualifying_information': value.get('c'),
        'edition': value.get('b'),
        'place_publisher_and_date_of_publication': value.get('d'),
        'related_parts': value.get('g'),
        'relationship_information': value.get('i'),
        'physical_description': value.get('h'),
        'series_data_for_related_item': value.get('k'),
        'material_specific_details': value.get('m'),
        'other_item_identifier': value.get('o'),
        'note': value.get('n'),
        'uniform_title': value.get('s'),
        'report_number': value.get('r'),
        'standard_technical_report_number': value.get('u'),
        'title': value.get('t'),
        'record_control_number': value.get('w'),
        'coden_designation': value.get('y'),
        'international_standard_serial_number': value.get('x'),
        'international_standard_book_number': value.get('z'),
        'note_controller': indicator_map1.get(key[3]),
        'display_constant_controller': indicator_map2.get(key[4]),
    }
