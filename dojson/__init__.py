# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""DoJSON is a simple Pythonic JSON to JSON converter.

The main goal of this package is to help with managing a set of rules
for manipulation of Python dictionaries with focus on JSON serialization.
Each rule is associated with regular expression and key. The regular expression
has to match a key in the source mapping and produces a new value that is added
to the output mapping under the new key.

Initialization
--------------
First create an `Overdo` object that is holding the index with rules.

>>> import dojson
>>> simple = dojson.Overdo()

Next step is to create rules that will manupulate a source object.

>>> @simple.over('first', '^.*st$')
... def first(self, key, value):
...     return value + 1
>>> @simple.over('second', '^.*nd$')
... def second(self, key, value):
...     return value + 2

And now we can try to match the source object and produce new data.

>>> data = simple.do({'1st': 1, '2nd': 2})
>>> assert 2 == data['first']
>>> assert 4 == data['second']
"""

from .overdo import Overdo
from .version import __version__

__all__ = (
    'Overdo',
    '__version__',
)
