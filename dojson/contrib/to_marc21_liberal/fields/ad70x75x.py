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
        'form_subdivision': 'v',
        'personal_name': 'a',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
        'language_of_a_work': 'l',
        'general_subdivision': 'x',
        'title_of_a_work': 't',
        'source_of_heading_or_term': '2',
        'attribution_qualifier': 'j',
        'control_subfield': 'w',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'version': 's',
        'date_of_a_work': 'f',
        'fuller_form_of_name': 'q',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'name_of_part_section_of_a_work': 'p',
        'titles_and_other_words_associated_with_a_name': 'c',
        'chronological_subdivision': 'y',
        'medium': 'h',
        'geographic_subdivision': 'z',
        'number_of_part_section_of_a_work': 'n',
        'form_subheading': 'k',
        'authority_record_control_number_or_standard_number': '0',
        'arranged_statement_for_music': 'o',
        'dates_associated_with_a_name': 'd',
        'numeration': 'b',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_personal_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('personal_name'),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
        'l': value.get('language_of_a_work'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        't': value.get('title_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        's': value.get('version'),
        'f': value.get('date_of_a_work'),
        'q': value.get('fuller_form_of_name'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'c': utils.reverse_force_list(
            value.get('titles_and_other_words_associated_with_a_name')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': value.get('dates_associated_with_a_name'),
        'b': value.get('numeration'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'corporate_name_or_jurisdiction_name_as_entry_element': 'a',
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'key_for_music': 'r',
        'language_of_a_work': 'l',
        'general_subdivision': 'x',
        'title_of_a_work': 't',
        'source_of_heading_or_term': '2',
        'version': 's',
        'control_subfield': 'w',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'date_of_a_work': 'f',
        'relator_term': 'e',
        'medium_of_performance_for_music': 'm',
        'miscellaneous_information': 'g',
        'location_of_meeting': 'c',
        'chronological_subdivision': 'y',
        'medium': 'h',
        'geographic_subdivision': 'z',
        'number_of_part_section_meeting': 'n',
        'form_subheading': 'k',
        'authority_record_control_number_or_standard_number': '0',
        'arranged_statement_for_music': 'o',
        'date_of_meeting_or_treaty_signing': 'd',
        'subordinate_unit': 'b',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_corporate_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'r': value.get('key_for_music'),
        'l': value.get('language_of_a_work'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        't': value.get('title_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        's': value.get('version'),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'f': value.get('date_of_a_work'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'general_subdivision': 'x',
        'title_of_a_work': 't',
        'source_of_heading_or_term': '2',
        'version': 's',
        'control_subfield': 'w',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'date_of_a_work': 'f',
        'name_of_meeting_following_jurisdiction_name_entry_element': 'q',
        'subordinate_unit': 'e',
        'miscellaneous_information': 'g',
        'location_of_meeting': 'c',
        'chronological_subdivision': 'y',
        'medium': 'h',
        'geographic_subdivision': 'z',
        'number_of_part_section_meeting': 'n',
        'form_subheading': 'k',
        'authority_record_control_number_or_standard_number': '0',
        'meeting_name_or_jurisdiction_name_as_entry_element': 'a',
        'date_of_meeting': 'd',
        'relator_term': 'j',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['type_of_meeting_name_entry_element', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        't': value.get('title_of_a_work'),
        '2': value.get('source_of_heading_or_term'),
        's': value.get('version'),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'f': value.get('date_of_a_work'),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        'c': utils.reverse_force_list(
            value.get('location_of_meeting')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'd': value.get('date_of_meeting'),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'name_of_part_section_of_a_work': 'p',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'language_of_a_work': 'l',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'control_subfield': 'w',
        'relationship_code': '4',
        'institution_to_which_field_applies': '5',
        'uniform_title': 'a',
        'date_of_a_work': 'f',
        'medium_of_performance_for_music': 'm',
        'key_for_music': 'r',
        'title_of_a_work': 't',
        'chronological_subdivision': 'y',
        'medium': 'h',
        'geographic_subdivision': 'z',
        'number_of_part_section_of_a_work': 'n',
        'form_subheading': 'k',
        'authority_record_control_number_or_standard_number': '0',
        'arranged_statement_for_music': 'o',
        'date_of_treaty_signing': 'd',
        'version': 's',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'l': value.get('language_of_a_work'),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        'w': value.get('control_subfield'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'a': value.get('uniform_title'),
        'f': value.get('date_of_a_work'),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'h': value.get('medium'),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'o': value.get('arranged_statement_for_music'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        's': value.get('version'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'chronological_term': 'a',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('chronological_term'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'institution_to_which_field_applies': '5',
        'control_subfield': 'w',
        'authority_record_control_number_or_standard_number': '0',
        'topical_term_or_geographic_name_entry_element': 'a',
        'topical_term_following_geographic_name_entry_element': 'b',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'w': value.get('control_subfield'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('topical_term_or_geographic_name_entry_element'),
        'b': value.get('topical_term_following_geographic_name_entry_element'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'relationship_code': '4',
        'miscellaneous_information': 'g',
        'field_link_and_sequence_number': '8',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'geographic_name': 'a',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'g': utils.reverse_force_list(
            value.get('miscellaneous_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('geographic_name'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
        'form_subdivision': 'v',
        'relationship_code': '4',
        'field_link_and_sequence_number': '8',
        'chronological_subdivision': 'y',
        'geographic_subdivision': 'z',
        'general_subdivision': 'x',
        'source_of_heading_or_term': '2',
        'institution_to_which_field_applies': '5',
        'authority_record_control_number_or_standard_number': '0',
        'genre_form_term_as_entry_element': 'a',
        'control_subfield': 'w',
        'relationship_information': 'i',
        'linkage': '6',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    if not value.get('$ind1') and '$ind1' in order:
        order.remove('$ind1')

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'a': value.get('genre_form_term_as_entry_element'),
        'w': value.get('control_subfield'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '6': value.get('linkage'),
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
