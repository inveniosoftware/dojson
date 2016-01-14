===============
 DoJSON v1.0.0
===============

DoJSON v1.0.0 was released on January 14, 2016.

About
-----

DoJSON is a simple Pythonic JSON to JSON converter.

Incompatible changes
--------------------

- Removes support for single key matching multiple rules. Please make
  your rules mutually exclusive!
- controlfields 00x are expected to be the element or a list of
  multiple elements.

New features
------------

- Adds new keyword argument `ignore_missing` to `Overdo.do` method to
  specify if method should raise `MissingRule` exception when there is
  no matching rule for a key.
- Adds new CLI option `--strict` to the `do` command that sets the
  `ignore_missing` argument to `False`.  (#51)
- MARC XML serialization from to_marc21.

Improved features
-----------------

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

Installation
------------

   $ pip install dojson==1.0.0

Documentation
-------------

   http://dojson.readthedocs.org/en/v1.0.0

Happy hacking and thanks for flying DoJSON.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/dojson
|   URL: http://invenio-software.org
