# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting to MARC21."""

from __future__ import unicode_literals

import pkg_resources

from lxml import etree
from lxml.builder import E


MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""

MARC21_NS = "http://www.loc.gov/MARC21/slim"
"""MARCXML XML Schema"""


def dumps(*records, **kwargs):
    """Dump records into a MarcXML file."""

    root = etree.Element('collection', nsmap={None: MARC21_NS})
    for record in records:
        rec = E.record()
        for df, subfields in record.items():
            if isinstance(subfields, list):
                controlfield = E.controlfield(subfields[0])
                print(df)
                controlfield.attrib['tag'] = df[0:3]
                rec.append(controlfield)
            else:
                df = df.replace('_', ' ')
                datafield = E.datafield()
                datafield.attrib['tag'] = df[0:3]
                datafield.attrib['ind1'] = df[3]
                datafield.attrib['ind2'] = df[4]

                for code, value in subfields.items(repeated=True):
                    if not isinstance(value, basestring):
                        for v in value:
                            datafield.append(E.subfield(v, code=code))
                    else:
                        datafield.append(E.subfield(value, code=code))

                rec.append(datafield)
        root.append(rec)

    return etree.tostring(root, **kwargs)
