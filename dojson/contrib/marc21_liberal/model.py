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

marc21_liberal = Overdo(entry_point_group='dojson.contrib.marc21_liberal')
"""MARC 21 Format for Bibliographic Data."""

marc21_liberal_authority = Overdo(entry_point_group='dojson.contrib.marc21_liberal_authority')
"""MARC 21 Format for Authority Data."""


@marc21_liberal.over('__order__', '__order__')
def order(self, key, value):
    """Preserve order of datafields."""
    order = []
    for field in value:
        name = marc21_liberal.index.query(field)
        if name:
            name = name[0]
        else:
            name = field
        order.append(name)

    return order


@marc21_liberal_authority.over('__order__', '__order__')
def order_ad(self, key, value):
    """Preserve order of datafields."""
    order = []
    for field in value:
        name = marc21_liberal_authority.index.query(field)
        if name:
            name = name[0]
        else:
            name = field
        order.append(name)

    return order

marc21_liberal_holdings = Overdo(entry_point_group='dojson.contrib.marc21_liberal_holdings')
"""MARC 21 Format for Holdings Data."""
