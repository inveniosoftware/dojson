# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting MARC21 liberal."""

from dojson.contrib.marc21.utils import load as marc21_load, create_record \
    as marc21_create_record, split_blob as marc21_split_blob, split_stream \
    as marc21_split_stream

load = marc21_load
create_record = marc21_create_record
split_blob = marc21_split_blob
split_stream = marc21_split_stream
