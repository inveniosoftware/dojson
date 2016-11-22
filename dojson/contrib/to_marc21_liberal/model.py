# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 liberal model definition."""

from dojson.contrib.to_marc21.model import Underdo
from dojson.errors import MissingRule

from .utils import to_marc21_liberal_handler

to_marc21_liberal = Underdo(
    entry_point_group='dojson.contrib.to_marc21_liberal',
    exception_handlers={MissingRule: to_marc21_liberal_handler})

to_marc21_liberal_authority = Underdo(
    entry_point_group='dojson.contrib.to_marc21_liberal_authority',
    exception_handlers={MissingRule: to_marc21_liberal_handler})
