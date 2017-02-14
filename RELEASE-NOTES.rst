===============
 DoJSON v1.3.0
===============

DoJSON v1.3.0 was released on February 14, 2017.

About
-----

DoJSON is a simple Pythonic JSON to JSON converter.

New features
------------

- Adds the possibility to skip individual items when using the
  `for_each_value` decorator by raising the `IgnoreElement` exception.
- Adds `@flatten` decorator that joins iterable results. (#147)
- Adds to_marc21 conversion functions.

Improved features
-----------------

- Updates MARC21 schema and conversion functions to the latest
  Library of Congress standard.
- Clarifies in its docstring that `force_list` may returns a tuple,
  not a list.  (#154)
- Adds order to existing marc21 conversion functions.
- Updates authority schema with new fields and corrects some existing
  ones.

Bug fixes
---------

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

Installation
------------

   $ pip install dojson==1.3.0

Documentation
-------------

   http://dojson.readthedocs.io/en/v1.3.0

Happy hacking and thanks for flying DoJSON.

| Invenio Development Team
|   Email: info@inveniosoftware.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/dojson
|   URL: http://inveniosoftware.org
