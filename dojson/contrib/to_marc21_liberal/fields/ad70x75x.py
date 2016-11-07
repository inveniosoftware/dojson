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

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('700', '^established_heading_linking_entry_personal_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_personal_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'personal_name': 'a',
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'attribution_qualifier': 'j',
        'medium': 'h',
        'chronological_subdivision': 'y',
        'key_for_music': 'r',
        'relationship_information': 'i',
        'number_of_part_section_of_a_work': 'n',
        'title_of_a_work': 't',
        'institution_to_which_field_applies': '5',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance_for_music': 'm',
        'fuller_form_of_name': 'q',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'dates_associated_with_a_name': 'd',
        'numeration': 'b',
        'source_of_heading_or_term': '2',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'linkage': '6',
        'arranged_statement_for_music': 'o',
        'language_of_a_work': 'l',
        'version': 's',
        'titles_and_other_words_associated_with_a_name': 'c',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('personal_name'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'h': value.get('medium'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'r': value.get('key_for_music'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        't': value.get('title_of_a_work'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'q': value.get('fuller_form_of_name'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'b': value.get('numeration'),
        '2': value.get('source_of_heading_or_term'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        'o': value.get('arranged_statement_for_music'),
        'l': value.get('language_of_a_work'),
        's': value.get('version'),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), value.get('type_of_personal_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('710', '^established_heading_linking_entry_corporate_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_corporate_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Corporate Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'medium': 'h',
        'chronological_subdivision': 'y',
        'key_for_music': 'r',
        'relationship_information': 'i',
        'number_of_part_section_meeting': 'n',
        'title_of_a_work': 't',
        'institution_to_which_field_applies': '5',
        'relator_term': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'medium_of_performance_for_music': 'm',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'date_of_meeting_or_treaty_signing': 'd',
        'subordinate_unit': 'b',
        'source_of_heading_or_term': '2',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'language_of_a_work': 'l',
        'version': 's',
        'location_of_meeting': 'c',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'r': value.get('key_for_music'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        't': value.get('title_of_a_work'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '2': value.get('source_of_heading_or_term'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        'l': value.get('language_of_a_work'),
        's': value.get('version'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), value.get('type_of_corporate_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('711', '^established_heading_linking_entry_meeting_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_meeting_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Meeting Name."""
    indicator_map1 = {"Inverted name": "0", "Jurisdiction name": "1", "Name in direct order": "2"}
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'language_of_a_work': 'l',
        'relator_term': 'j',
        'medium': 'h',
        'linkage': '6',
        'chronological_subdivision': 'y',
        'number_of_part_section_meeting': 'n',
        'institution_to_which_field_applies': '5',
        'subordinate_unit': 'e',
        'authority_record_control_number_or_standard_number': '0',
        'form_subheading': 'k',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'date_of_meeting': 'd',
        'source_of_heading_or_term': '2',
        'relationship_information': 'i',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'title_of_a_work': 't',
        'version': 's',
        'location_of_meeting': 'c',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'l': value.get('language_of_a_work'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'h': value.get('medium'),
        '6': value.get('linkage'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'd': value.get('date_of_meeting'),
        '2': value.get('source_of_heading_or_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), value.get('type_of_meeting_name_entry_element', '_')),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('730', '^established_heading_linking_entry_uniform_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_uniform_title(self, key, value):
    """Reverse - Established Heading Linking Entry-Uniform Title."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'uniform_title': 'a',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'medium': 'h',
        'chronological_subdivision': 'y',
        'relationship_information': 'i',
        'number_of_part_section_of_a_work': 'n',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'key_for_music': 'r',
        'miscellaneous_information': 'g',
        'medium_of_performance_for_music': 'm',
        'date_of_treaty_signing': 'd',
        'source_of_heading_or_term': '2',
        'form_subheading': 'k',
        'date_of_a_work': 'f',
        'form_subdivision': 'v',
        'general_subdivision': 'x',
        'name_of_part_section_of_a_work': 'p',
        'arranged_statement_for_music': 'o',
        'title_of_a_work': 't',
        'version': 's',
        'relationship_code': '4',
        'language_of_a_work': 'l',
        'geographic_subdivision': 'z',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('uniform_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'h': value.get('medium'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'r': value.get('key_for_music'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        '2': value.get('source_of_heading_or_term'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'f': value.get('date_of_a_work'),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'o': value.get('arranged_statement_for_music'),
        't': value.get('title_of_a_work'),
        's': value.get('version'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'l': value.get('language_of_a_work'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('748', '^established_heading_linking_entry_chronological_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_chronological_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Chronological Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'chronological_term': 'a',
        'relationship_code': '4',
        'source_of_heading_or_term': '2',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('chronological_term'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '2': value.get('source_of_heading_or_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('750', '^established_heading_linking_entry_topical_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_topical_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Topical Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'topical_term_or_geographic_name_entry_element': 'a',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'topical_term_following_geographic_name_entry_element': 'b',
        'source_of_heading_or_term': '2',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        '2': value.get('source_of_heading_or_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('751', '^established_heading_linking_entry_geographic_name$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_geographic_name(self, key, value):
    """Reverse - Established Heading Linking Entry-Geographic Name."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'geographic_name': 'a',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'source_of_heading_or_term': '2',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('geographic_name'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('755', '^established_heading_linking_entry_genre_form_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_genre_form_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Genre/Form Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'control_subfield': 'w',
        'genre_form_term_as_entry_element': 'a',
        'relationship_code': '4',
        'source_of_heading_or_term': '2',
        'relationship_information': 'i',
        'chronological_subdivision': 'y',
        'general_subdivision': 'x',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_subdivision': 'z',
        'form_subdivision': 'v',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'w': value.get('control_subfield'),
        'a': value.get('genre_form_term_as_entry_element'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '2': value.get('source_of_heading_or_term'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
