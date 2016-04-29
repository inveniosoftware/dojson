===============
 DoJSON v1.2.1
===============

DoJSON v1.2.1 was released on May 02, 2016.

About
-----

DoJSON is a simple Pythonic JSON to JSON converter.

Improved features
-----------------

- Improves support for `leader` field conversion to and from
  MARC21 and adds JSON Schema for this field.  (#133)
- Adds conversion support for `leader` field in authority
  records, as well as schema support.
- Adds support for dashes in keys.  (#139)

Bug fixes
---------

- Fixes bug in string formatting, and pads integer fields with
  zeros (as per MARC standard).
- Removes list definition from `main_entry_personal_name` as
  according to Library of Congress is a non repeatable field.

Installation
------------

   $ pip install dojson==1.2.1

Documentation
-------------

   http://dojson.readthedocs.org/en/v1.2.1

Happy hacking and thanks for flying DoJSON.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/dojson
|   URL: http://invenio-software.org
