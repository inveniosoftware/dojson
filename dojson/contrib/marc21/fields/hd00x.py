# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""MARC 21 model definition."""

from dojson import utils

from ..model import marc21_holdings


@marc21_holdings.over('control_number', '^001')
def control_number(self, key, value):
    """Control Number."""
    return value


@marc21_holdings.over('control_number_identifier', '^003')
def control_number_identifier(self, key, value):
    """Control Number Identifier."""
    return value


@marc21_holdings.over('date_and_time_of_latest_transaction', '^005')
def date_and_time_of_latest_transaction(self, key, value):
    """Date and Time of Latest Transaction."""
    return value
