# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
"""Functions for adding order to existing conversion files."""

import xml.etree.ElementTree as ET
import re
import random


def add_order_to_fields(filename, suffix='', to_marc=False):
    """Add order to all functions withing a provided marc21 conversion file.

    Read the content of a marc21 conversion file and produce an
    indentical file, but with order added to each function.

    :param filename: String containing the path to a marc21 conversion
    file.
    :param suffix: Optional suffix for the new file. If none is provided,
    the original file will be overwritten.
    :param to_marc: Bool denoting what type of conversion file is provided.
    """
    with open(filename, 'r') as pyfile:
        blob = pyfile.read()

    splitkey = "@to_marc21" if to_marc else "@marc21"
    datafield_strings = blob.split(splitkey)

    file_string = datafield_strings.pop(0)
    for datafield in datafield_strings:
        ordered_datafield = add_order(datafield, to_marc)
        file_string += splitkey + ordered_datafield

    new_filename = filename.split(".")[0] + (suffix or '') + ".py"

    with open(new_filename, "w") as new_file:
        new_file.write(file_string)


def tryint(str):
    """Return int if applicable, else return the input directly."""
    try:
        return int(str)
    except ValueError:
        return str


def add_order(df_string, to_marc=False):
    u"""Add order to text blob containing a datafield function defintion.

    Add order to text blob containing a datafield function defintion. Dissect
    it and collects information before writing the order information to the
    return string.

    Return the same blob, but with field_map and `__order__` added.
    If ` __order__` already exists, return the input directly.

    :param df_string: String containing the datafield function definition.
    :param to_marc: Bool denoting what type of conversion file is provided.
    """
    parts = df_string.split('"""\n')

    # Already have a field map. Abort
    if "field_map" in parts[1]:
        return df_string

    nl_or_ind, returnstr = parts[1].split("return")

    elems = returnstr.split(",")
    fields = dict()
    for i, elem in enumerate(elems):
        elem_parts = elem.split("'")
        if len(elem_parts) >= 4:
            if '$ind' in elem_parts[1]:
                continue
            fields[elem_parts[3]] = elem_parts[1]

    field_map_str = "    field_map = {\n"

    if to_marc:
        for key in sorted(fields.keys(), key=lambda e:
                          ({int: 1, float: 1, str: 0}.
                          get(type(tryint(fields[e])), 0), fields[e])):
            field_map_str += "        '{0}': '{1}',\n".format(key, fields[key])
    else:
        for key in sorted(fields.keys(), key=lambda e:
                          ({int: 1, float: 1, str: 0}.
                          get(tryint(type(e)), 0), tryint(e))):
            field_map_str += "        '{0}': '{1}',\n".format(key, fields[key])
    field_map_str += "    }\n    order = utils.map_order(field_map, value)\n"

    returnstr = returnstr.split("\n", 1)[1]
    returnstr = "return {\n        '__order__': tuple(order) if len(order) else None,\n" + \
        returnstr

    new_function_str = parts[0] + '"""\n' + \
        field_map_str + '\n' + nl_or_ind + returnstr

    return new_function_str
