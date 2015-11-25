# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting MARC21."""

from __future__ import unicode_literals

import pkg_resources
import re

from collections import MutableMapping, OrderedDict
from lxml import etree
from six import StringIO, string_types

split_marc = re.compile('<record.*?>.*?</record>', re.DOTALL)

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""


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
    record = OrderedDict()
    field_position_global = 0

    controlfield_iterator = tree.iter(tag='{*}controlfield')
    for controlfield in controlfield_iterator:
        tag = controlfield.attrib.get('tag', '!')  # .encode("UTF-8")
        ind1 = ' '
        ind2 = ' '
        text = controlfield.text
        if text is None:
            text = ''
        else:
            text = text  # .encode("UTF-8")
        subfields = []
        if text or keep_singletons:
            field_position_global += 1
            record.setdefault(tag, []).append((subfields, ind1, ind2, text,
                                               field_position_global))

    datafield_iterator = tree.iter(tag='{*}datafield')
    for datafield in datafield_iterator:
        tag = datafield.attrib.get('tag', '!')  # .encode("UTF-8")
        ind1 = datafield.attrib.get('ind1', '!')  # .encode("UTF-8")
        ind2 = datafield.attrib.get('ind2', '!')  # .encode("UTF-8")
        # ind1, ind2 = _wash_indicators(ind1, ind2)
        if ind1 in ('', '_'):
            ind1 = ' '
        if ind2 in ('', '_'):
            ind2 = ' '
        subfields = []
        subfield_iterator = datafield.iter(tag='{*}subfield')
        for subfield in subfield_iterator:
            code = subfield.attrib.get('code', '!')  # .encode("UTF-8")
            text = subfield.text
            if text is None:
                text = ''
            else:
                text = text  # .encode("UTF-8")
            if text or keep_singletons:
                subfields.append((code, text))
        if subfields or keep_singletons:
            text = ''
            field_position_global += 1
            record.setdefault(tag, []).append((subfields, ind1, ind2, text,
                                               field_position_global))

    rec_tree = OrderedDict()

    for key, values in record.items():
        if key < '010' and key.isdigit():
            rec_tree[key] = [value[3] for value in values]
        else:
            for value in values:
                k = (key + value[1] + value[2]).replace(' ', '_')
                fields = GroupableOrderedDict()
                for subfield in value[0]:
                    fields[subfield[0]] = subfield[1]
                rec_tree[k] = fields

    return rec_tree


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


class GroupableOrderedDict(MutableMapping):
    """List that can group values pretending to be a dict."""

    def __init__(self, values=None):
        super(MutableMapping, self).__init__()

        self._data = []
        self._keys = []
        if values:
            for k, v in values:
                self[k] = v

    def get(self, key):
        if key in self._keys:
            return self.__getitem__(key)
        else:
            return None

    def __getitem__(self, key):
        if key in self._keys:
            output = [v for k, v in self._data if k == key]
            if len(output) == 1:
                return output[0]
            else:
                return output
        raise KeyError(key)

    def __setitem__(self, key, value):
        self._data.append((key, value))
        if key not in self._keys:
            self._keys.append(key)

    def __delitem__(self, key):
        self._data = [(k, v) for k, v in self._data if k != key]
        self._keys.remove(key)

    def __len__(self):
        return len(self.keys)

    def values(self, **kw):
        r = []
        if not kw.get('expand', False):
            for key in self._keys:
                r.append(self[key])
        else:
            for _, v in self._data:
                r.append(v)
        return r

    def keys(self, **kw):
        if not kw.get('repeated', False):
            return list(self._keys)
        else:
            return [k for k, v in self._data]

    def items(self, **kw):
        return list(self.iteritems(**kw))

    def iteritems(self, **kw):
        if not kw.get('repeated', False):
            for key in self._keys:
                yield key, self[key]
        else:
            for item in self._data:
                yield item

    def __iter__(self, **kw):
        for key in self._keys:
            yield key

    def __repr__(self):
        return repr(dict(self.iteritems()))
