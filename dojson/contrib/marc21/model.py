# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""MARC 21 model definition."""

from dojson import Overdo, utils

marc21 = Overdo(entry_point_group='dojson.contrib.marc21')
"""MARC 21 Format for Bibliographic Data."""

marc21_authority = Overdo(entry_point_group='dojson.contrib.marc21_authority')
"""MARC 21 Format for Authority Data."""


@marc21.over('__order__', '__order__')
def order(self, key, value):
    """Preserve order of datafields."""
    order = []
    for field in value:
        name = marc21.index.query(field)
        if name:
            name = name[0]
        else:
            name = field
        order.append(name)

    return order


@marc21_authority.over('__order__', '__order__')
def order_ad(self, key, value):
    """Preserve order of datafields."""
    order = []
    for field in value:
        name = marc21_authority.index.query(field)
        if name:
            name = name[0]
        else:
            name = field
        order.append(name)

    return order

marc21_holdings = Overdo(entry_point_group='dojson.contrib.marc21_holdings')
"""MARC 21 Format for Holdings Data."""
