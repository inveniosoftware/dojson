# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting to MARC21."""

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
        for df, subfields in record.items(repeated=True):
            # Control fields
            if len(df) == 3:
                if isinstance(subfields, basestring):
                    controlfield = E.controlfield(subfields)
                    controlfield.attrib['tag'] = df[0:3]
                    rec.append(controlfield)
                elif isinstance(subfields, (list, tuple, set)):
                    for subfield in subfields:
                        controlfield = E.controlfield(subfield)
                        controlfield.attrib['tag'] = df[0:3]
                        rec.append(controlfield)
            else:
                if not isinstance(subfields, (list, tuple, set)):
                    subfields = (subfields,)

                df = df.replace('_', ' ')
                for subfield in subfields:
                    datafield = E.datafield()
                    datafield.attrib['tag'] = df[0:3]
                    datafield.attrib['ind1'] = df[3]
                    datafield.attrib['ind2'] = df[4]

                    for code, value in subfield.items(repeated=True):
                        if not isinstance(value, basestring):
                            for v in value:
                                datafield.append(E.subfield(v, code=code))
                        else:
                            datafield.append(E.subfield(value, code=code))

                    rec.append(datafield)
        root.append(rec)

    return etree.tostring(root, **kwargs)
