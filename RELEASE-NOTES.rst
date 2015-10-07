===========================
 DoJSON v0.2.0 is released
===========================

DoJSON v0.2.0 was released on October 7, 2015.

About
-----

DoJSON is a simple Pythonic JSON to JSON converter.

New features
------------

- Adds the posibility to use base DoJSON model so the rules are
  "inherited" from them.
- Adds new decorator `ignore_value` that remove the key in the
  resulting json for None value.

Improved features
-----------------

- Uses entry points instead of plain imports to load the creator
  rules.

Bug fixes
---------

- Removes calls to PluginManager consider_setuptools_entrypoints()
  removed in PyTest 2.8.0.

Installation
------------

   $ pip install dojson==0.2.0

Documentation
-------------

   http://dojson.readthedocs.org/en/v0.2.0

Happy hacking and thanks for flying DoJSON.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/dojson
|   URL: http://invenio-software.org
