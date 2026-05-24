# SPDX-FileCopyrightText: 2015, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""MARC standards based on `www.loc.gov/marc/ <http://www.loc.gov/marc/>`_."""

from __future__ import absolute_import

from .model import marc21, marc21_authority, marc21_holdings

__all__ = ('marc21', 'marc21_authority', 'marc21_holdings')
