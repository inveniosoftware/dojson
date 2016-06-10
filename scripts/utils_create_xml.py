# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
"""Functions for creating MARCXML documents based on conversion files."""

import xml.etree.ElementTree as ET
import re
import random


def indent(elem, level=0):
    """Add indentation to Etree instance."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def tryint(str):
    """Return int if applicable, else return the input directly."""
    try:
        return int(str)
    except ValueError:
        return str


def create_xml_from_rules(filename):
    """Produce a MARCXML file with rules generated from MARC conversion file.

    Read the content of a marc21 conversion file and produce a MARCXML file
    containing all the datafields and their subfields.

    :param filename: String containing the path to a marc21 conversion
    file.
    """
    with open(filename, 'r') as pyfile:
        blob = pyfile.read()
    datafield_strings = blob.split("@to_marc")

    # Delete the first element containing imports etc
    del datafield_strings[0]

    # Start building the XML document
    collection = ET.Element(
        'collection', {'xmlns': 'http://www.loc.gov/MARC21/slim'})
    record = ET.SubElement(collection, 'record')
    for string in datafield_strings:
        datafield = extract_datafield(string)
        append_datafield(record, datafield)

    indent(collection)

    tree = ET.ElementTree(collection)
    xml_filename = filename.split(".")[0] + ".xml"
    tree.write(xml_filename, xml_declaration=True,
               encoding='utf-8', method="xml")


def append_datafield(record, df):
    """Append a datafield Etree with the provided subfields to an Etree.

    :param record: Etree instance
    :param df: Dictionary containing subfields
    """
    datafield = ET.SubElement(record, 'datafield', {
        'tag': df['tag'],
        'ind1': df['ind1'],
        'ind2': df['ind2'],
    })
    for k in sorted(df['subfields'].keys(), key=lambda e:
                    ({int: 1, float: 1, str: 0}.get(type(tryint(e)), 0), e)):
        subfield = ET.SubElement(datafield, 'subfield', {
            'code': k,
        })
        subfield.text = df['subfields'][k]


def extract_datafield(blob):
    """Extract subfields from marc21 conversion function.

    :param blob: String blob containing a marc21 conversion function defintion.
    :return: Dictionary containing subfields.
    """
    marc_elements = dict()
    blob = blob.replace("\n", '')
    marc_elements['tag'] = re.search("\d{3}", blob).group(0)

    # find indicators
    indicator_map1_str = re.findall("indicator_map1[^\.].*?}", blob)
    if indicator_map1_str:
        exec(indicator_map1_str[0])
    else:
        indicator_map1 = False

    indicator_map2_str = re.findall("indicator_map2[^\.].*?}", blob)
    if indicator_map2_str:
        exec(indicator_map2_str[0])
    else:
        indicator_map2 = False

    return_dict_str = re.findall("return {.*?}", blob)[0]
    return_dict_str = re.sub(
        r":.*?value\.get\(('.*?').*?  (['}])", r": \1, \2", return_dict_str)
    exec(return_dict_str.replace("return", "subfield_dict ="))
    subfield_dict.pop('$ind1', None)
    subfield_dict.pop('$ind2', None)
    marc_elements['subfields'] = subfield_dict
    marc_elements['ind1'] = random.choice(
        indicator_map1.values()) if indicator_map1 else " "
    marc_elements['ind2'] = random.choice(
        indicator_map2.values()) if indicator_map2 else " "
    return marc_elements
