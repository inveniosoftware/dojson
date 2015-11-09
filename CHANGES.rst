Changes
=======

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
