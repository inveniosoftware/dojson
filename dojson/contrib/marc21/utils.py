# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting MARC21."""

import re
from collections import Counter, OrderedDict

import pkg_resources
from lxml import etree
from six import StringIO, binary_type, iteritems, text_type

split_marc = re.compile('<record.*?>.*?</record>', re.DOTALL)

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""


class GroupableOrderedDict(OrderedDict):
    """Immutable list that can group values pretending to be a dict."""

    def __new__(cls, *args):
        """Create a new immutable GroupableOrderedDict."""
        new = OrderedDict.__new__(cls)
        OrderedDict.__init__(new)

        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got {}'
                            .format(len(args)))

        ordering = []
        values = args[0]

        if values:
            if isinstance(values, GroupableOrderedDict):
                values = values.iteritems(with_order=False, repeated=True)
            elif isinstance(values, dict):
                if '__order__' in values:
                    order = values.pop('__order__')

                    tmp = []
                    c = Counter()
                    for key in order:
                        v = values[key]
                        if not isinstance(v, (tuple, list)):
                            if c[key] == 0:
                                tmp.append((key, v))
                            else:
                                raise Exception("Order and values don't match"
                                                "on key {0} at position {1}"
                                                .format(key, c[key]))
                        else:
                            tmp.append((key, v[c[key]]))
                        c[key] += 1
                    values = tmp
                else:
                    values = iteritems(values)

            for key, value in values:
                if key not in new:
                    OrderedDict.__setitem__(new, key, [])
                v = []
                if isinstance(value, (tuple, list)):
                    for item in value:
                        v.append(item)
                        ordering.append(key)
                else:
                    v.append(value)
                    ordering.append(key)

                OrderedDict.__getitem__(new, key).extend(v)

        # Immutable...
        for key, value in dict.items(new):
            OrderedDict.__setitem__(new, key, tuple(value))

        OrderedDict.__setitem__(new, '__order__', tuple(ordering))
        return new

    def __init__(self, *args, **kwargs):
        """
        Init the GroupableOrderedDict.

        It's done in __new__ so the instance cannot be modified through it.
        """

    def __copy__(self):
        return GroupableOrderedDict(self)

    def __deepcopy__(self):
        return self.__copy__()

    def __reduce__(self):
        return GroupableOrderedDict, (dict(self.items()), )

    def __eq__(self, other):
        if (len(self.keys()) != len(other.keys()) and
                '__order__' not in other and
                len(self.keys()) - 1 == len(other.keys())):

            return False

        for k, vs in self.iteritems():
            if k == '__order__':
                if k in other and other[k] != vs:
                    return False
                else:
                    continue

            if k not in other:
                return False

            if isinstance(vs, (list, tuple, set)):
                if len(vs) == 1 and vs[0] != other[k] and vs != other[k]:
                    return False

                for i, v in enumerate(vs):
                    if v != other[k][i]:
                        return False
            else:
                # repeatable fields...
                if isinstance(other[k], (list, tuple, set)):
                    if len(other[k]) == 1 and vs != other[k][0]:
                        return False
                    else:
                        continue

                if vs != other[k] and (vs,) != other[k] and [vs] != other[k]:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def get(self, key, default=None):
        """D[k] if k in D, else d. d defaults to None."""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, key):
        item = OrderedDict.__getitem__(self, key)
        if len(item) == 1 and key != '__order__':
            return item[0]
        return item

    def __setitem__(self, *args, **kwargs):
        raise TypeError('{} object does not suppoert item assignment'
                        .format(self.__class__.__name__))

    def __delitem__(self, key):
        self.__data = [(k, v) for k, v in self.__data if k != key]
        self.__keys.remove(key)

    def __iter__(self):
        occurences = Counter()
        order = self['__order__']
        yield '__order__'
        for o in order:
            if occurences[o] == 0:
                yield o
            occurences[o] += 1

    def values(self, expand=False):
        """
        list of D's values grouped by key.

        expand=True will return the raw values in the initial order.
        """
        values = []
        if expand:
            occurences = Counter()
            order = self['__order__']
            for key in order:
                values.append(dict.__getitem__(self, key)[occurences[key]])
                occurences[key] += 1
        else:
            for key, value in OrderedDict.items(self):
                if key == '__order__':
                    continue
                if len(value) == 1:
                    values.append(value[0])
                else:
                    values.append(value)
        return values

    def keys(self, repeated=False):
        """
        list of D's keys.

        repeated=True will return the ordering of the values rather than the
        keys. It may contain repetitions.
        """
        if not repeated:
            keys = list(OrderedDict.keys(self))
            keys.remove('__order__')
            return keys
        else:
            return list(self['__order__'])

    def items(self, with_order=True, repeated=False):
        """
        list of D's (key, value) pairs, as 2-tuples.

        with_order=True will also return a (__order__, keys) tuples with the
        ordering. Usefull to be able to reconstruct this structure later on.

        repeated=True will not group by key and respect the initial ordering.
        """
        return tuple(self.iteritems(with_order, repeated))

    def iteritems(self, with_order=True, repeated=False):
        """Just like D.items() but as an iterator."""
        if not repeated:
            if with_order:
                yield '__order__', self['__order__']
            for key, value in OrderedDict.items(self):
                if key != '__order__':
                    if len(value) == 1:
                        yield key, value[0]
                    else:
                        yield key, value
        else:
            occurences = Counter()
            order = self['__order__']
            if with_order:
                yield '__order__', order
            for key in order:
                yield key, OrderedDict.__getitem__(self, key)[occurences[key]]
                occurences[key] += 1


def create_record(marcxml, correct=False, keep_singletons=True):
    """Create a record object using the LXML parser.

    If correct == 1, then perform DTD validation
    If correct == 0, then do not perform DTD validation
    """
    if isinstance(marcxml, binary_type):
        marcxml = marcxml.decode('utf-8')

    if isinstance(marcxml, text_type):
        parser = etree.XMLParser(dtd_validation=correct, recover=True)

        if correct:
            marcxml = (u'<?xml version="1.0" encoding="UTF-8"?>\n'
                       u'<!DOCTYPE collection SYSTEM "file://{0}">\n'
                       u'<collection>\n{1}\n</collection>'.format(
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
