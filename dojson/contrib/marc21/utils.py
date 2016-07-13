# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting MARC21."""

import re
from collections import Counter, OrderedDict

import pkg_resources
from lxml import etree

from dojson._compat import StringIO, binary_type, iteritems, text_type
from dojson.utils import GroupableOrderedDict

split_marc = re.compile('<record.*?>.*?</record>', re.DOTALL)

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""


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

    leader_iterator = tree.iter(tag='{*}leader')
    for leader in leader_iterator:
        text = leader.text or ''
        record.append(('leader', text))

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
        if ind1 in ('', '#'):
            ind1 = '_'
        if ind2 in ('', '#'):
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
