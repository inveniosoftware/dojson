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
from six import iteritems, string_types

from dojson.utils import GroupableOrderedDict


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
                            items = s.items(repeated=True)
                        elif isinstance(s, dict):
                            items = s.items()
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
        root.append(rec)

    return etree.tostring(root, **kwargs)
