
import xml.etree.ElementTree as ET
import re
import random


def add_order_to_fields(filename, suffix='', to_marc=False):
    """Reads the content of a marc21 conversion file and produces an
    indentical file, but with order added.

    :param filename: String containing the path to a marc21 conversion
    file.
    :param suffix: Optional suffix for the new file. If none is provided,
    the original file will be overwritten.
    :param to_marc: Bool denoting what type of conversion file is provided.
    """
    with open(filename, 'r') as file:
        blob = file.read()

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
    """Returns int if applicable, else it returns the input directly"""
    try:
        return int(str)
    except ValueError:
        return str


def add_order(df_string, to_marc=False):
    """Takes a text blob containing a datafield function defintion.
    Dissects it and collects information before writing the order information
    to the return string

    Returns the same blob, but with field_map and `__order__` added.
    If ` __order__` already exists, it returns the input directly.

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
        for key in sorted(fields.keys(), key=lambda e: ({int: 1, float: 1, str: 0}.get(type(tryint(fields[e])), 0), fields[e])):
            field_map_str += "        '{0}': '{1}',\n".format(key, fields[key])
    else:
        for key in sorted(fields.keys(), key=lambda e: ({int: 1, float: 1, str: 0}.get(tryint(type(e)), 0), tryint(e))):
            field_map_str += "        '{0}': '{1}',\n".format(key, fields[key])
    field_map_str += "    }\n    order = utils.map_order(field_map, value)\n"

    returnstr = returnstr.split("\n", 1)[1]
    returnstr = "return {\n        '__order__': tuple(order) if len(order) else None,\n" + \
        returnstr

    new_function_str = parts[0] + '"""\n' + \
        field_map_str + '\n' + nl_or_ind + returnstr

    return new_function_str
