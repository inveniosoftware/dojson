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

from ..model import marc21, tomarc21


@marc21.over('control_number', '^001')
def control_number(self, key, value):
    """Control Number."""
    return value[0]

@tomarc21.over('001', '^control_number$')
def reverse_control_number(self, key, value):
    """Reverse - Control Number."""
    return [value]


@marc21.over('control_number_identifier', '^003')
def control_number_identifier(self, key, value):
    """Control Number Identifier."""
    return value[0]

@tomarc21.over('003', '^control_number_identifier$')
def reverse_control_number_identifier(self, key, value):
    """Reverse - Control Number Identifier."""
    return [value]


@marc21.over('date_and_time_of_latest_transaction', '^005')
def date_and_time_of_latest_transaction(self, key, value):
    """Date and Time of Latest Transaction."""
    return value[0]

@tomarc21.over('005', '^date_and_time_of_latest_transaction$')
def reverse_date_and_time_of_latest_transaction(self, key, value):
    """Reverse - Date and Time of Latest Transaction."""
    return [value]


@marc21.over('fixed_length_data_elements_additional_material_characteristics', '^006')
def fixed_length_data_elements_additional_material_characteristics(self, key, value):
    """Fixed-Length Data Elements-Additional Material Characteristics."""
    return value[0]

@tomarc21.over('006', '^fixed_length_data_elements_additional_material_characteristics$')
def reverse_fixed_length_data_elements_additional_material_characteristics(self, key, value):
    """Reverse - Fixed-Length Data Elements-Additional Material Characteristics."""
    return [value]


@marc21.over('fixed_length_data_elements', '^008')
def fixed_length_data_elements(self, key, value):
    """Fixed-Length Data Elements."""
    return value[0]

@tomarc21.over('008', '^fixed_length_data_elements$')
def reverse_fixed_length_data_elements(self, key, value):
    """Reverse - Fixed-Length Data Elements."""
    return [value]
