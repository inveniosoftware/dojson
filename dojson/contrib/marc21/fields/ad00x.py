# SPDX-FileCopyrightText: 2015, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_authority


@marc21_authority.over('control_number', '^001')
def control_number(self, key, value):
    """Control Number."""
    return value


@marc21_authority.over('control_number_identifier', '^003')
def control_number_identifier(self, key, value):
    """Control Number Identifier."""
    return value


@marc21_authority.over('date_and_time_of_latest_transaction', '^005')
def date_and_time_of_latest_transaction(self, key, value):
    """Date and Time of Latest Transaction."""
    return value


@marc21_authority.over('fixed_length_data_elements', '^008')
def fixed_length_data_elements(self, key, value):
    """Fixed-Length Data Elements."""
    return value
