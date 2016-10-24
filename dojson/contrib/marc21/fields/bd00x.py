# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21


@marc21.over('control_number', '^001')
def control_number(self, key, value):
    """Control Number."""
    return value


@marc21.over('control_number_identifier', '^003')
def control_number_identifier(self, key, value):
    """Control Number Identifier."""
    return value


@marc21.over('date_and_time_of_latest_transaction', '^005')
def date_and_time_of_latest_transaction(self, key, value):
    """Date and Time of Latest Transaction."""
    return value


@marc21.over(
    'fixed_length_data_elements_additional_material_characteristics', '^006')
def fixed_length_data_elements_additional_material_characteristics(
        self, key, value):
    """Fixed-Length Data Elements-Additional Material Characteristics."""
    return value


@marc21.over('physical_description_fixed_field_general_information', '^007')
def physical_description_fixed_field_general_information(self, key, value):
    """Physical Description Fixed Field-General Information."""
    return value


@marc21.over('fixed_length_data_elements', '^008')
def fixed_length_data_elements(self, key, value):
    """Fixed-Length Data Elements."""
    return value
