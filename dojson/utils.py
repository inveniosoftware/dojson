# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utility functions."""

import functools
import six


def filter_values(f):
    """Remove None values from dictionary."""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        out = f(*args, **kwargs)
        return dict((k, v) for k, v in six.iteritems(out) if v is not None)
    return wrapper


def for_each_value(f):
    """Apply function to each item."""
    @functools.wraps(f)
    def wrapper(self, key, values, **kwargs):
        if isinstance(values, list):
            return [f(self, key, value, **kwargs) for value in values]
        return [f(self, key, values, **kwargs)]
    return wrapper


def force_list(data):
    """Wrap data in list."""
    if data is not None and not isinstance(data, (list, set)):
        return [data]
    return data
