# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting MARC21."""

import pkg_resources
import re

from collections import Counter
from lxml import etree
from six import StringIO, string_types

split_marc = re.compile('<record.*?>.*?</record>', re.DOTALL)

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""


class GroupableOrderedDict(dict):
    """Immutable list that can group values pretending to be a dict."""

    def __new__(cls, values=None):
        new = dict.__new__(cls)
        dict.__init__(new)

        data = []
        keys = []
        ordering = []

        if values:
            if isinstance(values, GroupableOrderedDict):
                values = values.items(repeated=True)
            if isinstance(values, dict):
                if "__order__" not in values:
                    raise AttributeError("Can only be recreated from an "
                                         "ordered dict.")

                ordering = values["__order__"]
                occurences = Counter(ordering)
                counter = Counter()
                for key in ordering:
                    if key not in keys:
                        keys.append(key)
                    if occurences[key] > 1:
                        value = values[key][counter[key]]
                    else:
                        value = values[key]
                    data.append((key, value))
                    counter[key] += 1
            else:
                for key, value in values:
                    if key not in keys:
                        keys.append(key)
                    data.append((key, value))
                    ordering.append(key)

        # immutable, all the things
        new.__data = tuple(data)
        new.__keys = tuple(keys)
        new.__order__ = tuple(ordering)
        return new

    def __init__(self, *args):
        pass

    def __copy__(self):
        return GroupableOrderedDict(self.items(repeated=True))

    def __deepcopy__(self):
        return self.__copy__()

    def __reduce__(self):
        return GroupableOrderedDict, (dict(self.items()), )

    def __eq__(self, other):
        if len(other) != len(self.__keys):
            return False

        for k, v in self.iteritems(with_order=False):
            if not isinstance(v, (list, tuple)):
                if isinstance(other[k], (list, tuple)):
                    if len(other[k]) != 1:
                        return False
                    if v != other[k][0]:
                        return False
                elif v != other[k]:
                    return False
            else:
                if len(v) != len(other[k]):
                    return False

                for i, value in enumerate(v):
                    if other[k][i] != value:
                        return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def get(self, key, default=None):
        """D.get(k,[,d]) -> D[k] if k in D, else d. d defaults to None."""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, key):
        if key == "___keys__":
            return self.___keys__
        if key in self.__keys:
            item = tuple([v for k, v in self.__data if k == key])
            if len(item) == 1:
                return item[0]
            return item
        raise KeyError(key)

    def __setitem__(self, *args, **kwargs):
        raise TypeError('{} object does not suppoert item assignment'
                        .format(self.__class__.__name__))

    def __delitem__(self, key):
        self.__data = [(k, v) for k, v in self.__data if k != key]
        self.__keys.remove(key)

    def __len__(self):
        return len(self.__keys)

    def values(self, expand=False):
        """
        D.values() -> list of D's values grouped by key

        expand=True will return the raw values in the initial order.
        """
        r = []
        if not expand:
            for key in self.__keys:
                r.append(self[key])
        else:
            for _, v in self.__data:
                r.append(v)
        return r

    def keys(self, repeated=False):
        """
        D.keys() -> list of D's keys

        repeated=True will return the ordering of the values rather than the
        keys. It may contain repeatitions.
        """
        if not repeated:
            return self.__keys
        else:
            return tuple(k for k, v in self.__data)

    def items(self, with_order=False, repeated=False):
        """
        D.items() -> list of D's (key, value) pairs, as 2-tuples

        with_order=True will also return a (__order__, keys) tuples with the
        ordering. Usefull to be able to reconstruct this structure later on.

        repeated=True will not group by key and respect the initial ordering.
        """
        return tuple(self.iteritems(with_order, repeated))

    def iteritems(self, with_order=True, repeated=False):
        """Just like D.items() but as an iterator"""
        if with_order:
            yield "__order__", self.__order__
        if not repeated:
            for key in self.__keys:
                yield key, self[key]
        else:
            for item in self.__data:
                yield item

    def __iter__(self):
        for k in self.__keys:
            yield k

    def __repr__(self):
        return repr(dict(self.iteritems()))

    def __bool__(self):
        return bool(self.__keys)


def create_record(marcxml, correct=False, keep_singletons=True):
    """Create a record object using the LXML parser.

    If correct == 1, then perform DTD validation
    If correct == 0, then do not perform DTD validation
    """
    if isinstance(marcxml, string_types):
        parser = etree.XMLParser(dtd_validation=correct, recover=True)

        if correct:
            marcxml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                       '<!DOCTYPE collection SYSTEM "file://{0}">\n'
                       '<collection>\n{1}\n</collection>'.format(
                           MARC21_DTD, marcxml))

        tree = etree.parse(StringIO(marcxml), parser)
    else:
        tree = marcxml
    record = []

    controlfield_iterator = tree.iter(tag='{*}controlfield')
    for controlfield in controlfield_iterator:
        tag = controlfield.attrib.get('tag', '!')
        text = controlfield.text or ''
        if text or keep_singletons:
            record.append((tag, text))

    datafield_iterator = tree.iter(tag='{*}datafield')
    for datafield in datafield_iterator:
        tag = datafield.attrib.get('tag', '!')
        ind1 = datafield.attrib.get('ind1', '!')
        ind2 = datafield.attrib.get('ind2', '!')
        if ind1 in ('', ):
            ind1 = '_'
        if ind2 in ('', ):
            ind2 = '_'
        ind1 = ind1.replace(' ', '_')
        ind2 = ind2.replace(' ', '_')

        fields = []
        subfield_iterator = datafield.iter(tag='{*}subfield')
        for subfield in subfield_iterator:
            code = subfield.attrib.get('code', '!')  # .encode("UTF-8")
            text = subfield.text or ''
            if text or keep_singletons:
                fields.append((code, text))

        if fields or keep_singletons:
            key = '{0}{1}{2}'.format(tag, ind1, ind2)
            record.append((key, GroupableOrderedDict(fields)))

    return GroupableOrderedDict(record)


def split_blob(blob):
    """Split the blob using <record.*?>.*?</record> as pattern."""
    for match in split_marc.finditer(blob):
        yield match.group()
    raise StopIteration()


def split_stream(stream):
    """Yield record elements from given stream."""
    for _, element in etree.iterparse(stream, tag='{*}record'):
        yield element


def load(source):
    """Load MARC XML and return Python dict."""
    for data in split_stream(source):
        yield create_record(data)
