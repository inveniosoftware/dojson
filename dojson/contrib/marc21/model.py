# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import Overdo, utils

marc21 = Overdo(entry_point_group='dojson.contrib.marc21')
"""MARC 21 Format for Bibliographic Data."""

marc21_holdings = Overdo(entry_point_group='dojson.contrib.marc21_holdings')
"""MARC 21 Format for Holdings Data."""
