Changes
=======

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
