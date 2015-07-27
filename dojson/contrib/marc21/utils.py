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

from lxml import etree
from six import StringIO, iteritems

split_marc = re.compile('<record.*?>.*?</record>', re.DOTALL)

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""


def create_record(marcxml, correct=False, keep_singletons=True):
    """Create a record object using the LXML parser.

    If correct == 1, then perform DTD validation
    If correct == 0, then do not perform DTD validation
    """
    parser = etree.XMLParser(dtd_validation=correct, recover=True)

    if correct:
        marcxml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<!DOCTYPE collection SYSTEM "file://{0}">\n'
                   '<collection>\n{1}\n</collection>'.format(
                       MARC21_DTD, marcxml))

    tree = etree.parse(StringIO(marcxml), parser)
    record = {}
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

    class SaveDict(dict):
        __getitem__ = dict.get

    def dict_extend_helper(d, key, value):
        """Helper function.
        If the key is present inside the dictionary it creates a list (if
        not present) and extends it with the new value.
        Almost as in `list.extend`
        """
        if key in d:
            current_value = d.get(key)
            if not isinstance(current_value, list):
                current_value = [current_value]
            current_value.append(value)
            value = current_value
        d[key] = value

    rec_tree = SaveDict()

    for key, values in iteritems(record):
        if key < '010' and key.isdigit():
            rec_tree[key] = [value[3] for value in values]
        else:
            for value in values:
                field = SaveDict()
                for subfield in value[0]:
                    dict_extend_helper(field, subfield[0], subfield[1])
                dict_extend_helper(
                    rec_tree,
                    (key + value[1] + value[2]).replace(' ', '_'), field)

    return rec_tree


def split_blob(blob):
    """Split the blob using <record.*?>.*?</record> as pattern."""
    for match in split_marc.finditer(blob):
        yield match.group()
    raise StopIteration()
