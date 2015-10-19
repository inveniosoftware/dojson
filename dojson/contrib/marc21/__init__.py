# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC standards based on `www.loc.gov/marc/ <http://www.loc.gov/marc/>`_."""

from __future__ import absolute_import

from .model import marc21, marc21_authority, marc21_holdings

__all__ = ('marc21', 'marc21_authority', 'marc21_holdings')
