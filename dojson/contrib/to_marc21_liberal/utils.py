# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting to MARC21 liberal."""
from dojson.contrib.to_marc21.utils import dumps_etree as marc21_dumps_etree, \
    dumps as marc21_dumps

dumps_etree = marc21_dumps_etree
dumps = marc21_dumps
