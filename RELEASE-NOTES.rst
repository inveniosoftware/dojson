===============
 DoJSON v1.1.0
===============

DoJSON v1.1.0 was released on March 10, 2016.

About
-----

DoJSON is a simple Pythonic JSON to JSON converter.

Incompatible changes
--------------------

- Moves `--load` and `--dump` options to global group.

New features
------------

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
-----------------

- Adds more detailed usage examples.  (#117)
- Refactors CLI to allow commands chaining.
- Adds support preserving the order of subfields.

Bug fixes
---------

- Fixes support for Python 3.5.1.

Installation
------------

   $ pip install dojson==1.1.0

Documentation
-------------

   http://dojson.readthedocs.org/en/v1.1.0

Happy hacking and thanks for flying DoJSON.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/dojson
|   URL: http://invenio-software.org
