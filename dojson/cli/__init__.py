# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

r"""Command line interface script is installed as ``dojson``.

The easiest way to get started by applying already registered rule to a JSON
data.

.. code-block:: text

   {"245__": {"a": "Test title"}}

DoJSON comes with set of rules for processing MARC21 fields.

.. code-block:: console

    $ echo '{"245__": {"a": "Test title"}}' | dojson do marc21
    {"title_statement": {"title": "Test title"}}

Sometimes one can get input with fields that does not match any rule.
To get such a list of fields one can use the ``missing`` command.

.. code-block:: console

    $ echo '{"999__": {"a": "Test title"}}' | dojson missing marc21
    999__

The usual problem comes with reading different file formats such as XML.

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <collection xmlns="http://www.loc.gov/MARC21/slim">
      <record>
        <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">Test title</subfield>
        </datafield>
      </record>
    </collection>

You can specify regitered loader using ``-l <NAME>`` argument. Save the above
example as ``example.xml`` and check following command.

.. code-block:: console

    $ dojson -i example.xml -l marcxml do marc21
    {"title_statement": {"title": "Test title"}}

In similar way it is possible to specify different output serializer (``-d``).

.. code-block:: console

    $ echo '{"title_statement": {"title": "Test title"}}' | \
      dojson -d marcxml do marc21
    <?xml version='1.0' encoding='UTF-8'?>
    <collection xmlns="http://www.loc.gov/MARC21/slim">
      <record>
        <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">Test title</subfield>
        </datafield>
      </record>
    </collection>

Command chaining
----------------

This makes JSON manipulation even easier. For first example see ``schema``
command that accept string argument containing URL of JSON-Schema that
should be added to ``$schema`` field.

.. code-block:: console

    $ dojson -i example.xml -l marcxml do marc21 \
      schema http://example.org/schema/marc21.json
    ..."schema": "http://example.org/schema/marc21.json"...

Second example shows easy verification that rules produce an identity function.

.. code-block:: console

    $ dojson -l marcxml -d marcxml do marc21 do to_marc21 < example.xml | \
      diff - example.xml

Extensibility
-------------

New commands, loaders, dumpers, or rules can be provided via entry points.

- ``dojson.cli`` commands that return a processor acception an iterator;
- ``dojson.cli.load`` functions expecting a stream and returning Python dict or
  iterator;
- ``dojson.cli.dump`` functions expecting a Python object and returning
  ``str``;
- ``dojson.cli.rule`` instances of :class:`dojson.overdo.Overdo` with loaded
  rules.
"""

import sys

import click

from .._compat import stdin
from .utils import open_entry_point, with_plugins


@with_plugins('dojson.cli')
@click.group(chain=True, invoke_without_command=True)
@click.option('-i', '--input', 'source', type=click.File('rb'),
              default=stdin)
@click.option('-l', '--load', callback=open_entry_point('dojson.cli.load'),
              default='json')
@click.option('-d', '--dump', callback=open_entry_point('dojson.cli.dump'),
              default='json')
def cli(**kwargs):
    """Command line interface."""


@cli.resultcallback()
def process_pipeline(processors, source, load, dump):
    """Call data processors."""
    def loader(iterator):
        data = load(iterator)
        if isinstance(data, dict):
            yield data
        else:
            for item in data:
                yield item

    source = loader(source)

    for processor in processors:
        source = processor(source)

    click.echo(dump(source))
