# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""DoJSON API."""

from .overdo import Overdo
from .version import __version__

__all__ = (
    'Overdo',
    '__version__',
)
