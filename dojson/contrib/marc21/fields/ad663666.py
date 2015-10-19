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

from ..model import marc21_authority


@marc21_authority.over('complex_see_also_reference_name', '^663..')
@utils.filter_values
def complex_see_also_reference_name(self, key, value):
    """Complex See Also Reference-Name."""
    return {
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('complex_see_reference_name', '^664..')
@utils.filter_values
def complex_see_reference_name(self, key, value):
    """Complex See Reference-Name."""
    return {
        'explanatory_text': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'heading_referred_to': utils.force_list(
            value.get('b')
        ),
        'title_referred_to': utils.force_list(
            value.get('t')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('history_reference', '^665..')
@utils.filter_values
def history_reference(self, key, value):
    """History Reference."""
    return {
        'history_reference': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }


@marc21_authority.over('general_explanatory_reference_name', '^666..')
@utils.filter_values
def general_explanatory_reference_name(self, key, value):
    """General Explanatory Reference-Name."""
    return {
        'general_explanatory_reference': utils.force_list(
            value.get('a')
        ),
        'field_link_and_sequence_number': utils.force_list(
            value.get('8')
        ),
        'linkage': value.get('6'),
    }
