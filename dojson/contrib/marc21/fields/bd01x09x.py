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


@marc21.over('library_of_congress_control_number', '^010..')
@utils.filter_values
def library_of_congress_control_number(self, key, value):
    """Library of Congress Control Number."""
    return {
        'lc_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'nucmc_control_number': utils.force_list(
            value.get('b')
        ),
        'canceled_invalid_lc_control_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('patent_control_information', '^013..')
@utils.for_each_value
@utils.filter_values
def patent_control_information(self, key, value):
    """Patent Control Information."""
    return {
        'number': value.get('a'),
        'type_of_number': value.get('c'),
        'country': value.get('b'),
        'status': utils.force_list(
            value.get('e')
        ),
        'date': utils.force_list(
            value.get('d')
        ),
        'party_to_document': utils.force_list(
            value.get('f')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('national_bibliography_number', '^015..')
@utils.for_each_value
@utils.filter_values
def national_bibliography_number(self, key, value):
    """National Bibliography Number."""
    return {
        'national_bibliography_number': utils.force_list(
            value.get('a')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_national_bibliography_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('national_bibliographic_agency_control_number', '^016[_7].')
@utils.for_each_value
@utils.filter_values
def national_bibliographic_agency_control_number(self, key, value):
    """National Bibliographic Agency Control Number."""
    indicator_map1 = {
        "#": "Library and Archives Canada",
        "7": "Source specified in subfield $2"}
    return {
        'record_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'national_bibliographic_agency': indicator_map1.get(key[3]),
    }


@marc21.over('copyright_or_legal_deposit_number', '^017.[8_]')
@utils.for_each_value
@utils.filter_values
def copyright_or_legal_deposit_number(self, key, value):
    """Copyright or Legal Deposit Number."""
    indicator_map2 = {
        "#": "Copyright or legal deposit number",
        "8": "No display constant generated"}
    return {
        'copyright_or_legal_deposit_number': utils.force_list(
            value.get('a')
        ),
        'assigning_agency': value.get('b'),
        'date': value.get('d'),
        'display_text': value.get('i'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_copyright_or_legal_deposit_number': utils.force_list(
            value.get('z')
        ),
        'display_constant_controller': indicator_map2.get(key[4]),
    }


@marc21.over('copyright_article_fee_code', '^018..')
@utils.filter_values
def copyright_article_fee_code(self, key, value):
    """Copyright Article-Fee Code."""
    return {
        'copyright_article_fee_code_nr': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('international_standard_book_number', '^020..')
@utils.for_each_value
@utils.filter_values
def international_standard_book_number(self, key, value):
    """International Standard Book Number."""
    return {
        'international_standard_book_number': value.get('a'),
        'terms_of_availability': value.get('c'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_isbn': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('international_standard_serial_number', '^022[10_].')
@utils.for_each_value
@utils.filter_values
def international_standard_serial_number(self, key, value):
    """International Standard Serial Number."""
    indicator_map1 = {
        "#": "No level specified",
        "0": "Continuing resource of international interest",
        "1": "Continuing resource not of international interest"}
    return {
        'international_standard_serial_number': value.get('a'),
        'canceled_issn_l': utils.force_list(
            value.get('m')
        ),
        'issn_l': value.get('l'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'incorrect_issn': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_issn': utils.force_list(
            value.get('z')
        ),
        'level_of_international_interest': indicator_map1.get(key[3]),
    }


@marc21.over('other_standard_identifier', '^024[1032478_][10_]')
@utils.for_each_value
@utils.filter_values
def other_standard_identifier(self, key, value):
    """Other Standard Identifier."""
    indicator_map1 = {
        "0": "International Standard Recording Code",
        "1": "Universal Product Code",
        "2": "International Standard Music Number",
        "3": "International Article Number",
        "4": "Serial Item and Contribution Identifier",
        "7": "Source specified in subfield $2",
        "8": "Unspecified type of standard number or code"}
    indicator_map2 = {
        "#": "No information provided",
        "0": "No difference",
        "1": "Difference"}
    return {
        'standard_number_or_code': value.get('a'),
        'terms_of_availability': value.get('c'),
        'additional_codes_following_the_standard_number_or_code': value.get('d'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'source_of_number_or_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_standard_number_or_code': utils.force_list(
            value.get('z')
        ),
        'type_of_standard_number_or_code': indicator_map1.get(key[3]),
        'difference_indicator': indicator_map2.get(key[4]),
    }


@marc21.over('overseas_acquisition_number', '^025..')
@utils.for_each_value
@utils.filter_values
def overseas_acquisition_number(self, key, value):
    """Overseas Acquisition Number."""
    return {
        'overseas_acquisition_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('fingerprint_identifier', '^026..')
@utils.for_each_value
@utils.filter_values
def fingerprint_identifier(self, key, value):
    """Fingerprint Identifier."""
    return {
        'first_and_second_groups_of_characters': value.get('a'),
        'date': value.get('c'),
        'third_and_fourth_groups_of_characters': value.get('b'),
        'unparsed_fingerprint': value.get('e'),
        'number_of_volume_or_part': utils.force_list(
            value.get('d')
        ),
        'source': value.get('2'),
        'institution_to_which_field_applies': utils.force_list(
            value.get('5')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('standard_technical_report_number', '^027..')
@utils.for_each_value
@utils.filter_values
def standard_technical_report_number(self, key, value):
    """Standard Technical Report Number."""
    return {
        'standard_technical_report_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_number': utils.force_list(
            value.get('z')
        ),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('publisher_number', '^028[103254_][1032_]')
@utils.for_each_value
@utils.filter_values
def publisher_number(self, key, value):
    """Publisher Number."""
    indicator_map1 = {
        "0": "Issue number",
        "1": "Matrix number",
        "2": "Plate number",
        "3": "Other music number",
        "4": "Videorecording number",
        "5": "Other publisher number"}
    indicator_map2 = {
        "0": "No note, no added entry",
        "1": "Note, added entry",
        "2": "Note, no added entry",
        "3": "No note, added entry"}
    return {
        'publisher_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('b'),
        'qualifying_information': utils.force_list(
            value.get('q')
        ),
        'linkage': value.get('6'),
        'type_of_publisher_number': indicator_map1.get(key[3]),
        'note_added_entry_controller': indicator_map2.get(key[4]),
    }


@marc21.over('coden_designation', '^030..')
@utils.for_each_value
@utils.filter_values
def coden_designation(self, key, value):
    """CODEN Designation."""
    return {
        'coden': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_coden': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('musical_incipits_information', '^031..')
@utils.for_each_value
@utils.filter_values
def musical_incipits_information(self, key, value):
    """Musical Incipits Information."""
    return {
        'number_of_work': value.get('a'),
        'number_of_excerpt': value.get('c'),
        'number_of_movement': value.get('b'),
        'role': value.get('e'),
        'caption_or_heading': utils.force_list(
            value.get('d')
        ),
        'clef': value.get('g'),
        'public_note': utils.force_list(
            value.get('z')
        ),
        'voice_instrument': value.get('m'),
        'time_signature': value.get('o'),
        'key_signature': value.get('n'),
        'general_note': utils.force_list(
            value.get('q')
        ),
        'musical_notation': value.get('p'),
        'coded_validity_note': utils.force_list(
            value.get('s')
        ),
        'system_code': value.get('2'),
        'uniform_resource_identifier': utils.force_list(
            value.get('u')
        ),
        'text_incipit': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
        'link_text': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'key_or_mode': value.get('r'),
    }


@marc21.over('postal_registration_number', '^032..')
@utils.for_each_value
@utils.filter_values
def postal_registration_number(self, key, value):
    """Postal Registration Number."""
    return {
        'postal_registration_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('date_time_and_place_of_an_event', '^033[10_2][10_2]')
@utils.for_each_value
@utils.filter_values
def date_time_and_place_of_an_event(self, key, value):
    """Date/Time and Place of an Event."""
    indicator_map1 = {
        "#": "No date information ",
        "0": "Single date ",
        "1": "Multiple single dates ",
        "2": "Range of dates "}
    indicator_map2 = {
        "#": "No information provided ",
        "0": "Capture ",
        "1": "Broadcast ",
        "2": "Finding "}
    return {
        'formatted_date_time': utils.force_list(
            value.get('a')
        ),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('c')
        ),
        'geographic_classification_area_code': utils.force_list(
            value.get('b')
        ),
        'place_of_event': utils.force_list(
            value.get('p')
        ),
        'authority_record_control_number': utils.force_list(
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
        'type_of_date_in_subfield_a': indicator_map1.get(key[3]),
        'type_of_event': indicator_map2.get(key[4]),
    }


@marc21.over('coded_cartographic_mathematical_data', '^034[103_][10_]')
@utils.for_each_value
@utils.filter_values
def coded_cartographic_mathematical_data(self, key, value):
    """Coded Cartographic Mathematical Data."""
    indicator_map1 = {
        "0": "Scale indeterminable/No scale recorded",
        "1": "Single scale",
        "3": "Range of scales"}
    indicator_map2 = {
        "#": "Not applicable",
        "0": "Outer ring",
        "1": "Exclusion ring"}
    return {
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'materials_specified': value.get('3'),
        'source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'category_of_scale': value.get('a'),
        'constant_ratio_linear_vertical_scale': utils.force_list(
            value.get('c')
        ),
        'constant_ratio_linear_horizontal_scale': utils.force_list(
            value.get('b')
        ),
        'coordinates_easternmost_longitude': value.get('e'),
        'coordinates_westernmost_longitude': value.get('d'),
        'coordinates_southernmost_latitude': value.get('g'),
        'coordinates_northernmost_latitude': value.get('f'),
        'angular_scale': utils.force_list(
            value.get('h')
        ),
        'declination_southern_limit': value.get('k'),
        'declination_northern_limit': value.get('j'),
        'right_ascension_eastern_limit': value.get('m'),
        'right_ascension_western_limit': value.get('n'),
        'equinox': value.get('p'),
        'g_ring_latitude': utils.force_list(
            value.get('s')
        ),
        'distance_from_earth': value.get('r'),
        'g_ring_longitude': utils.force_list(
            value.get('t')
        ),
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
    """System Control Number."""
    return {
        'system_control_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_control_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('original_study_number_for_computer_data_files', '^036..')
@utils.filter_values
def original_study_number_for_computer_data_files(self, key, value):
    """Original Study Number for Computer Data Files."""
    return {
        'original_study_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_agency_assigning_number': value.get('b'),
        'linkage': value.get('6'),
    }


@marc21.over('source_of_acquisition', '^037..')
@utils.for_each_value
@utils.filter_values
def source_of_acquisition(self, key, value):
    """Source of Acquisition."""
    return {
        'stock_number': value.get('a'),
        'terms_of_availability': utils.force_list(
            value.get('c')
        ),
        'source_of_stock_number_acquisition': value.get('b'),
        'additional_format_characteristics': utils.force_list(
            value.get('g')
        ),
        'form_of_issue': utils.force_list(
            value.get('f')
        ),
        'note': utils.force_list(
            value.get('n')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('record_content_licensor', '^038..')
@utils.filter_values
def record_content_licensor(self, key, value):
    """Record Content Licensor."""
    return {
        'record_content_licensor': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('cataloging_source', '^040..')
@utils.filter_values
def cataloging_source(self, key, value):
    """Cataloging Source."""
    return {
        'original_cataloging_agency': value.get('a'),
        'transcribing_agency': value.get('c'),
        'language_of_cataloging': value.get('b'),
        'description_conventions': utils.force_list(
            value.get('e')
        ),
        'modifying_agency': utils.force_list(
            value.get('d')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('language_code', '^041[10_].')
@utils.for_each_value
@utils.filter_values
def language_code(self, key, value):
    """Language Code."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Item not a translation/does not include a\n                  \t\t\t\t\t\ttranslation",
        "1": "Item is or includes a translation"}
    return {
        'language_code_of_text_sound_track_or_separate_title': utils.force_list(
            value.get('a')
        ),
        'language_code_of_summary_or_abstract': utils.force_list(
            value.get('b')
        ),
        'language_code_of_librettos': utils.force_list(
            value.get('e')
        ),
        'language_code_of_sung_or_spoken_text': utils.force_list(
            value.get('d')
        ),
        'language_code_of_accompanying_material_other_than_librettos': utils.force_list(
            value.get('g')
        ),
        'language_code_of_table_of_contents': utils.force_list(
            value.get('f')
        ),
        'language_code_of_original': utils.force_list(
            value.get('h')
        ),
        'language_code_of_intermediate_translations': utils.force_list(
            value.get('k')
        ),
        'language_code_of_subtitles_or_captions': utils.force_list(
            value.get('j')
        ),
        'language_code_of_original_accompanying_materials_other_than_librettos': utils.force_list(
            value.get('m')
        ),
        'language_code_of_original_libretto': utils.force_list(
            value.get('n')
        ),
        'source_of_code': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'translation_indication': indicator_map1.get(key[3]),
    }


@marc21.over('authentication_code', '^042..')
@utils.filter_values
def authentication_code(self, key, value):
    """Authentication Code."""
    return {
        'authentication_code': utils.force_list(
            value.get('a')
        ),
    }


@marc21.over('geographic_area_code', '^043..')
@utils.filter_values
def geographic_area_code(self, key, value):
    """Geographic Area Code."""
    return {
        'geographic_area_code': utils.force_list(
            value.get('a')
        ),
        'iso_code': utils.force_list(
            value.get('c')
        ),
        'local_gac_code': utils.force_list(
            value.get('b')
        ),
        'authority_record_control_number_or_standard_number': utils.force_list(
            value.get('0')
        ),
        'source_of_local_code': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('country_of_publishing_producing_entity_code', '^044..')
@utils.filter_values
def country_of_publishing_producing_entity_code(self, key, value):
    """Country of Publishing/Producing Entity Code."""
    return {
        'marc_country_code': utils.force_list(
            value.get('a')
        ),
        'iso_country_code': utils.force_list(
            value.get('c')
        ),
        'local_subentity_code': utils.force_list(
            value.get('b')
        ),
        'source_of_local_subentity_code': utils.force_list(
            value.get('2')
        ),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('time_period_of_content', '^045[10_2].')
@utils.filter_values
def time_period_of_content(self, key, value):
    """Time Period of Content."""
    indicator_map1 = {
        "#": "Subfield $b or $c not present",
        "0": "Single date/time",
        "1": "Multiple single dates/times",
        "2": "Range of dates/times"}
    return {
        'time_period_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'formatted_pre_9999_bc_time_period': utils.force_list(
            value.get('c')
        ),
        'formatted_9999_bc_through_ce_time_period': utils.force_list(
            value.get('b')
        ),
        'linkage': value.get('6'),
        'type_of_time_period_in_subfield_b_or_c': indicator_map1.get(key[3]),
    }


@marc21.over('special_coded_dates', '^046..')
@utils.for_each_value
@utils.filter_values
def special_coded_dates(self, key, value):
    """Special Coded Dates."""
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
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('form_of_musical_composition_code', '^047..')
@utils.for_each_value
@utils.filter_values
def form_of_musical_composition_code(self, key, value):
    """Form of Musical Composition Code."""
    return {
        'form_of_musical_composition_code': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2'),
    }


@marc21.over('number_of_musical_instruments_or_voices_code', '^048..')
@utils.for_each_value
@utils.filter_values
def number_of_musical_instruments_or_voices_code(self, key, value):
    """Number of Musical Instruments or Voices Code."""
    return {
        'performer_or_ensemble': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_code': value.get('2'),
        'soloist': utils.force_list(
            value.get('b')
        ),
    }


@marc21.over('library_of_congress_call_number', '^050[10_][0_4]')
@utils.for_each_value
@utils.filter_values
def library_of_congress_call_number(self, key, value):
    """Library of Congress Call Number."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Item is in LC",
        "1": "Item is not in LC"}
    indicator_map2 = {
        "0": "Assigned by LC",
        "4": "Assigned by agency other than LC"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
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
    """Library of Congress Copy, Issue, Offprint Statement."""
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@marc21.over('geographic_classification', '^052..')
@utils.for_each_value
@utils.filter_values
def geographic_classification(self, key, value):
    """Geographic Classification."""
    return {
        'geographic_classification_area_code': value.get('a'),
        'geographic_classification_subarea_code': utils.force_list(
            value.get('b')
        ),
        'populated_place_name': utils.force_list(
            value.get('d')
        ),
        'code_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over(
    'classification_numbers_assigned_in_canada', '^055[10_][_1032547698]')
@utils.for_each_value
@utils.filter_values
def classification_numbers_assigned_in_canada(self, key, value):
    """Classification Numbers Assigned in Canada."""
    indicator_map1 = {
        "#": "Information not provided",
        "0": "Work held by LAC",
        "1": "Work not held by LAC"}
    indicator_map2 = {
        "0": "LC-based call number assigned by LAC",
        "1": "Complete LC class number assigned by LAC",
        "2": "Incomplete LC class number assigned by LAC",
        "3": "LC-based call number assigned by the contributing library",
        "4": "Complete LC class number assigned by the contributing library",
        "5": "Incomplete LC class number assigned by the contributing library",
        "6": "Other call number assigned by LAC",
        "7": "Other class number assigned by LAC",
        "8": "Other call number assigned by the contributing library",
        "9": "Other class number assigned by the contributing library"}
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source_of_call_class_number': value.get('2'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'existence_in_lac_collection': indicator_map1.get(key[3]),
        'type_completeness_source_of_class_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_call_number', '^060[10_][0_4]')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_call_number(self, key, value):
    """National Library of Medicine Call Number."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Item is in NLM",
        "1": "Item is not in NLM"}
    indicator_map2 = {
        "0": "Assigned by NLM",
        "4": "Assigned by agency other than NLM"}
    return {
        'classification_number_r': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'existence_in_nlm_collection': indicator_map1.get(key[3]),
        'source_of_call_number': indicator_map2.get(key[4]),
    }


@marc21.over('national_library_of_medicine_copy_statement', '^061..')
@utils.for_each_value
@utils.filter_values
def national_library_of_medicine_copy_statement(self, key, value):
    """National Library of Medicine Copy Statement."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': value.get('c'),
        'item_number': value.get('b'),
    }


@marc21.over('character_sets_present', '^066..')
@utils.filter_values
def character_sets_present(self, key, value):
    """Character Sets Present."""
    return {
        'primary_g0_character_set': value.get('a'),
        'alternate_g0_or_g1_character_set': utils.force_list(
            value.get('c')
        ),
        'primary_g1_character_set': value.get('b'),
    }


@marc21.over('national_agricultural_library_call_number', '^070[10_].')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_call_number(self, key, value):
    """National Agricultural Library Call Number."""
    indicator_map1 = {"0": "Item is in NAL", "1": "Item is not in NAL"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number_r': utils.force_list(
            value.get('8')
        ),
        'item_number': value.get('b'),
        'existence_in_nal_collection': indicator_map1.get(key[3]),
    }


@marc21.over('national_agricultural_library_copy_statement', '^071..')
@utils.for_each_value
@utils.filter_values
def national_agricultural_library_copy_statement(self, key, value):
    """National Agricultural Library Copy Statement."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'copy_information': utils.force_list(
            value.get('c')
        ),
        'item_number': value.get('b'),
    }


@marc21.over('subject_category_code', '^072..')
@utils.for_each_value
@utils.filter_values
def subject_category_code(self, key, value):
    """Subject Category Code."""
    return {
        'subject_category_code': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'source': value.get('2'),
        'subject_category_code_subdivision': utils.force_list(
            value.get('x')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('gpo_item_number', '^074..')
@utils.for_each_value
@utils.filter_values
def gpo_item_number(self, key, value):
    """GPO Item Number."""
    return {
        'gpo_item_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_gpo_item_number': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('universal_decimal_classification_number', '^080[10_].')
@utils.for_each_value
@utils.filter_values
def universal_decimal_classification_number(self, key, value):
    """Universal Decimal Classification Number."""
    indicator_map1 = {
        "#": "No information provided",
        "0": "Full",
        "1": "Abridged"}
    return {
        'universal_decimal_classification_number': value.get('a'),
        'item_number': value.get('b'),
        'linkage': value.get('6'),
        'edition_identifier': value.get('2'),
        'common_auxiliary_subdivision': utils.force_list(
            value.get('x')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('dewey_decimal_classification_number', '^082[10_7][0_4]')
@utils.for_each_value
@utils.filter_values
def dewey_decimal_classification_number(self, key, value):
    """Dewey Decimal Classification Number."""
    indicator_map1 = {
        "0": "Full edition",
        "1": "Abridged edition",
        "7": "Other edition specified in subfield $2"}
    indicator_map2 = {
        "#": "No information provided",
        "0": "Assigned by LC",
        "4": "Assigned by agency other than LC"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
        'source_of_classification_number': indicator_map2.get(key[4]),
    }


@marc21.over('additional_dewey_decimal_classification_number', '^083[10_7].')
@utils.for_each_value
@utils.filter_values
def additional_dewey_decimal_classification_number(self, key, value):
    """Additional Dewey Decimal Classification Number."""
    indicator_map1 = {
        "0": "Full edition",
        "1": "Abridged edition",
        "7": "Other edition specified in subfield $2"}
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'standard_or_optional_designation': value.get('m'),
        'assigning_agency': value.get('q'),
        'edition_number': value.get('2'),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
        'type_of_edition': indicator_map1.get(key[3]),
    }


@marc21.over('other_classification_number', '^084..')
@utils.for_each_value
@utils.filter_values
def other_classification_number(self, key, value):
    """Other Classification Number."""
    return {
        'classification_number': utils.force_list(
            value.get('a')
        ),
        'item_number': value.get('b'),
        'assigning_agency': value.get('q'),
        'number_source': value.get('2'),
        'linkage': value.get('6'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
    }


@marc21.over('synthesized_classification_number_components', '^085..')
@utils.for_each_value
@utils.filter_values
def synthesized_classification_number_components(self, key, value):
    """Synthesized Classification Number Components."""
    return {
        'number_where_instructions_are_found_single_number_or_beginning_number_of_span': utils.force_list(
            value.get('a')
        ),
        'classification_number_ending_number_of_span': utils.force_list(
            value.get('c')
        ),
        'base_number': utils.force_list(
            value.get('b')
        ),
        'facet_designator': utils.force_list(
            value.get('f')
        ),
        'number_in_internal_subarrangement_or_add_table_where_instructions_are_found': utils.force_list(
            value.get('v')
        ),
        'digits_added_from_classification_number_in_schedule_or_external_table': utils.force_list(
            value.get('s')
        ),
        'root_number': utils.force_list(
            value.get('r')
        ),
        'number_being_analyzed': utils.force_list(
            value.get('u')
        ),
        'digits_added_from_internal_subarrangement_or_add_table': utils.force_list(
            value.get('t')
        ),
        'table_identification_internal_subarrangement_or_add_table': utils.force_list(
            value.get('w')
        ),
        'linkage': value.get('6'),
        'table_sequence_number_for_internal_subarrangement_or_add_table': utils.force_list(
            value.get('y')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'table_identification': utils.force_list(
            value.get('z')
        ),
    }


@marc21.over('government_document_classification_number', '^086..')
@utils.for_each_value
@utils.filter_values
def government_document_classification_number(self, key, value):
    """Government Document Classification Number."""
    return {
        'classification_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'number_source': value.get('2'),
        'canceled_invalid_classification_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }


@marc21.over('report_number', '^088..')
@utils.for_each_value
@utils.filter_values
def report_number(self, key, value):
    """Report Number."""
    return {
        'report_number': value.get('a'),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'canceled_invalid_report_number': utils.force_list(
            value.get('z')
        ),
        'linkage': value.get('6'),
    }
