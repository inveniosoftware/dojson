# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting to MARC21."""

import pkg_resources
from lxml import etree
from lxml.builder import ElementMaker

from dojson._compat import iteritems, string_types
from dojson.utils import GroupableOrderedDict

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""

MARC21_NS = "http://www.loc.gov/MARC21/slim"
"""MARCXML XML Schema"""


def dumps_etree(records, xslt_filename=None, prefix=None):
    """Dump records into a etree."""
    E = ElementMaker(namespace=MARC21_NS, nsmap={prefix: MARC21_NS})

    def dump_record(record):
        """Dump a single record."""
        rec = E.record()

        leader = record.get('leader')
        if leader:
            rec.append(E.leader(leader))

        if isinstance(record, GroupableOrderedDict):
            items = record.iteritems(with_order=False, repeated=True)
        else:
            items = iteritems(record)

        for df, subfields in items:
            # Control fields
            if len(df) == 3:
                if isinstance(subfields, string_types):
                    controlfield = E.controlfield(subfields)
                    controlfield.attrib['tag'] = df[0:3]
                    rec.append(controlfield)
                elif isinstance(subfields, (list, tuple, set)):
                    for subfield in subfields:
                        controlfield = E.controlfield(subfield)
                        controlfield.attrib['tag'] = df[0:3]
                        rec.append(controlfield)
            else:
                # Skip leader.
                if df == 'leader':
                    continue

                if not isinstance(subfields, (list, tuple, set)):
                    subfields = (subfields,)

                df = df.replace('_', ' ')
                for subfield in subfields:
                    if not isinstance(subfield, (list, tuple, set)):
                        subfield = [subfield]

                    for s in subfield:
                        datafield = E.datafield()
                        datafield.attrib['tag'] = df[0:3]
                        datafield.attrib['ind1'] = df[3]
                        datafield.attrib['ind2'] = df[4]

                        if isinstance(s, GroupableOrderedDict):
                            items = s.iteritems(with_order=False, repeated=True)
                        elif isinstance(s, dict):
                            items = iteritems(s)
                        else:
                            datafield.append(E.subfield(s))

                            items = tuple()

                        for code, value in items:
                            if not isinstance(value, string_types):
                                for v in value:
                                    datafield.append(E.subfield(v, code=code))
                            else:
                                datafield.append(E.subfield(value, code=code))

                        rec.append(datafield)
        return rec

    if isinstance(records, dict):
        root = dump_record(records)
    else:
        root = E.collection()
        for record in records:
            root.append(dump_record(record))

    if xslt_filename is not None:
        xslt_root = etree.parse(open(xslt_filename))
        transform = etree.XSLT(xslt_root)
        root = transform(root).getroot()

    return root


def dumps(records, xslt_filename=None, **kwargs):
    """Dump records into a MarcXML file."""
    root = dumps_etree(records=records, xslt_filename=xslt_filename)
    return etree.tostring(
        root,
        pretty_print=True,
        xml_declaration=True,
        encoding='UTF-8',
        **kwargs
    )
