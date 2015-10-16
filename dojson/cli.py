# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
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

**Extensions**

New extensions with loaders, dumpers, or rules can be provided via entry points.

- ``dojson.cli.load`` functions expecting a stream and returning Python dict or
  iterator;
- ``dojson.cli.dump`` functions expecting a Python object and returning
  ``str``;
- ``dojson.cli.rule`` instances of :class:`dojson.Overdo` with loaded rules.
"""

import json
import pkg_resources
import sys

import click


@click.group()
def cli():
    """Command line interface."""


def open_entry_point(group_name):
    """Open entry point."""
    def loader(ctx, param, value):
        """Load entry point from group name based on given value."""
        entry_points = list(pkg_resources.iter_entry_points(
            group_name, value
        ))
        assert len(entry_points) == 1
        return entry_points[0].load()
    return loader


@cli.command(name='do')
@click.option('-i', '--input', 'source', type=click.File('rb'),
              default=sys.stdin)
@click.option('-l', '--load', callback=open_entry_point('dojson.cli.load'),
              default='json')
@click.option('-d', '--dump', callback=open_entry_point('dojson.cli.dump'),
              default='json')
@click.argument('rule', callback=open_entry_point('dojson.cli.rule'))
def apply_rule(source, load, dump, rule):
    """Create JSON using given rule."""
    data = load(source)

    if isinstance(data, dict):
        click.echo(dump(rule.do(data)))
    else:
        click.echo(dump([
            rule.do(item) for item in data
        ]))


@cli.command(name='missing')
@click.option('-i', '--input', 'source', type=click.File('rb'),
              default=sys.stdin)
@click.option('-l', '--load', callback=open_entry_point('dojson.cli.load'),
              default='json')
@click.argument('rule', callback=open_entry_point('dojson.cli.rule'))
def missing_fields(source, load, rule):
    """List fields with missing rules."""
    data = load(source)
    missing = set()

    if isinstance(data, dict):
        missing |= set(rule.missing(data))
    else:
        for item in data:
            missing |= set(rule.missing(item))

    if missing:
        click.echo(', '.join(missing))
        sys.exit(1)
