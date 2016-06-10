# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_authority


@to_marc21_authority.over('001', '^control_number$')
def reverse_control_number(self, key, value):
    """Reverse - Control Number."""
    return [value]


@to_marc21_authority.over('003', '^control_number_identifier$')
def reverse_control_number_identifier(self, key, value):
    """Reverse - Control Number Identifier."""
    return [value]


@to_marc21_authority.over('005', '^date_and_time_of_latest_transaction$')
def reverse_date_and_time_of_latest_transaction(self, key, value):
    """Reverse - Date and Time of Latest Transaction."""
    return [value]


@to_marc21_authority.over('008', '^fixed_length_data_elements$')
def reverse_fixed_length_data_elements(self, key, value):
    """Reverse - Fixed-Length Data Elements."""
    return [value]
