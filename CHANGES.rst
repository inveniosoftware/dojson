Changes
=======

Version 1.3.0 (released 2017-02-14):
------------------------------------

New features
~~~~~~~~~~~~

- Adds the possibility to skip individual items when using the
  `for_each_value` decorator by raising the `IgnoreElement` exception.
- Adds `@flatten` decorator that joins iterable results. (#147)
- Adds to_marc21 conversion functions.

Improved features
~~~~~~~~~~~~~~~~~

- Updates MARC21 schema and conversion functions to the latest
  Library of Congress standard.
- Clarifies in its docstring that `force_list` may returns a tuple,
  not a list.  (#154)
- Adds order to existing marc21 conversion functions.
- Updates authority schema with new fields and corrects some existing
  ones.

Bug fixes
~~~~~~~~~

- Addresses issues with STDIN encoding on Python 3.
- Removes `@utils.for_each_value decorator` from conversion function
  for MARC21 field 044, which is not repeatable. (#181)
- Adds `tuples` to recogines types in `reverse_force_list` so it
  behaves correctly as an inverse fuction to `force_list`.
- Adds missing default argument to `__deepcopy__` method on
  GroupableOrderedDict.  (#167)
- Implements GroupableOrderedDict.__repr__() so that `eval(repr(god))
  == god`. (#162)
- Removes invalid check for length of yielded value causing exception
  when value is dictionary with one item.  (#150)
- Removes list definition from `main_entry_uniform_title` as according
  to Library of Congress is a non repeatable field.
- Removes invalid subfield from `data/test_7.xml`.

Version 1.2.1 (released 2016-05-02):
------------------------------------

Improved features
~~~~~~~~~~~~~~~~~

- Improves support for `leader` field conversion to and from
  MARC21 and adds JSON Schema for this field.  (#133)
- Adds conversion support for `leader` field in authority
  records, as well as schema support.
- Adds support for dashes in keys.  (#139)

Bug fixes
~~~~~~~~~

- Fixes bug in string formatting, and pads integer fields with
  zeros (as per MARC standard).
- Removes list definition from `main_entry_personal_name` as
  according to Library of Congress is a non repeatable field.

Version 1.2.0 (released 2016-03-21):
------------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Removes automatic wrapping to `<collection/>` for single record
  passed to `dumps_etree`.

Improved features
~~~~~~~~~~~~~~~~~

- Adds new argument to specify namespace prefix in generated MARCXML.

Version 1.1.1 (released 2016-03-15):
------------------------------------

Bug fixes
~~~~~~~~~

- Adds missing schemas for fields bd388, bd370, bd348, bd884.

Version 1.1.0 (released 2016-03-10):
------------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Moves `--load` and `--dump` options to global group.

New features
~~~~~~~~~~~~

- Adds `schema` command to enhance JSON with '$schema' field. (#73)
- Adds rules and schemas for MARC 21 Format for Authority Data. (#7)
- Adds rules and schemas for MARC 21 Format for Holdings Data. (#21)
- Adds support for parsing `<leader/>` tag in MARCXML.
- Adds new parameter `exception_handlers` to dojson.Overdo.do and
  dojson.contrib.to_marc21.model.Underdo.do. It can be given to the
  translation process to deal with non-standard fields in a custom way
  (#26).
- Adds new utility `map_order` function to ease renaming of
  subfields.

Improved features
~~~~~~~~~~~~~~~~~

- Adds more detailed usage examples.  (#117)
- Refactors CLI to allow commands chaining.
- Adds support preserving the order of subfields.

Bug fixes
~~~~~~~~~

- Fixes support for Python 3.5.1.

Version 1.0.0 (released 2016-01-14):
------------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Removes support for single key matching multiple rules. Please make
  your rules mutually exclusive!
- controlfields 00x are expected to be the element or a list of
  multiple elements.

New features
~~~~~~~~~~~~

- Adds new keyword argument `ignore_missing` to `Overdo.do` method to
  specify if method should raise `MissingRule` exception when there is
  no matching rule for a key.
- Adds new CLI option `--strict` to the `do` command that sets the
  `ignore_missing` argument to `False`.  (#51)
- MARC XML serialization from to_marc21.

Improved features
~~~~~~~~~~~~~~~~~

- Adds support for Python 3+.
- Uses an OrderedDict to let the external tools working on `dict`
  (like json) behave correctly.
- All results from rules using `for_each_value` decorator are being
  automatically extended. This is useful for repeatable MARC21 fields
  with different indicators.  (#53)
- Record are stored in an immutable sorted structure which enables to
  keep the intended order while offering easy ways to access, index
  and manipulate.
- Adds two records to be tested.
- Reorders some of the assertion: `expected == actual`.

Version 0.4.0 (released 2015-11-18):
------------------------------------

New features
~~~~~~~~~~~~

- Improves dojson.contrib.marc2.utils.load() to read the input by
  iterating of the open stream, rather than loading it all in memory
  in one go.  (#45) (#46)
- Renames OverUndo to Underdo following same name convention as for
  Overdo.

Bug fixes
~~~~~~~~~

- Fixes indicator extraction from value in `Underdo` model.

Version 0.3.0 (released 2015-11-09):
------------------------------------

New features
~~~~~~~~~~~~

- Adds **experimental** rules for converting human readable JSON into
  a JSON representation of the MARC21 Format.
- Adds `do` and `missing` commands for `dojson` command line interface
  (see `dojson --help` for more information).

Improved features
~~~~~~~~~~~~~~~~~

- Adds missing mapping for the first indicator of field 856.

Version 0.2.0 (released 2015-10-07):
------------------------------------

New features
~~~~~~~~~~~~

- Adds the posibility to use base DoJSON model so the rules are
  "inherited" from them.
- Adds new decorator `ignore_value` that remove the key in the
  resulting json for None value.

Improved features
~~~~~~~~~~~~~~~~~

- Uses entry points instead of plain imports to load the creator
  rules.

Bug fixes
~~~~~~~~~

- Removes calls to PluginManager consider_setuptools_entrypoints()
  removed in PyTest 2.8.0.

Version 0.1.1 (released 2015-07-27):
------------------------------------

- Sorts and removes duplicated enum values.
- Swaps wrongly defined repeatable and non-repeatable subfields. (#23)
- Addresses issue when allowed indicators where defined as a range.
  (#22)

Version 0.1.0 (released 2015-07-03):
------------------------------------

- Initial public release.
