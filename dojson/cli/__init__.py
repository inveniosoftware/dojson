# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""DoJSON command line interface.

This script is installed using the magic ``console_script`` section in
``entry_points`` parameters thanks to ``setuptools``. In order to get help from
console one can run:

.. code-block:: console

    $ dojson --help

Commands are loaded from entry point ``dojson.cli`` and they are chainable.
This makes JSON manipulation even easier.

Usage
~~~~~

For first example see ``schema``command that accept string argument containing
URL of JSON-Schema that should be added to ``$schema`` field.

.. code-block:: console

   $ dojson -l marcxml do marc21 schema http://example.org/schema/marc21.json

Second example shows easy verification that rules produce an identity function.

.. code-block:: console

    $ dojson -l marcxml -d marcxml do marc21 do to_marc21 < tests/data/test_1.xml > output.xml
    $ xmllint --format output.xml | diff - tests/data/test_1.xml

To get a list of fields that are missing mappings use the ``missing`` command:

.. code:: console

    $ dojson -i tests/data/handcrafted/text_incorrect_marc21.xml -l marcxml \
      missing marc21
    049__, 2452_, 999__


Entry Points
~~~~~~~~~~~~

New commands, loaders, dumpers, or rules can be provided via entry points.

- ``dojson.cli`` commands that return a processor acception an iterator;
- ``dojson.cli.load`` functions expecting a stream and returning Python dict or
  iterator;
- ``dojson.cli.dump`` functions expecting a Python object and returning
  ``str``;
- ``dojson.cli.rule`` instances of :class:`dojson.Overdo` with loaded rules.
"""

import sys

import click

from .utils import open_entry_point, with_plugins


@with_plugins('dojson.cli')
@click.group(chain=True, invoke_without_command=True)
@click.option('-i', '--input', 'source', type=click.File('rb'),
              default=sys.stdin)
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
