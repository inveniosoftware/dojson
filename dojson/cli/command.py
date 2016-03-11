# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Define chainable commands for processing loaded data."""

import json
import os
import sys

import click

from .utils import open_entry_point


@click.command('do')
@click.argument('rule', callback=open_entry_point('dojson.cli.rule'))
@click.option('--strict', is_flag=True, default=False,
              help='Raise when there is not matching rule for a key.')
def process_do(rule, strict):
    """Process data using given rule."""
    def processor(iterator):
        for item in iterator:
            yield rule.do(item, ignore_missing=not strict)
    return processor


@click.command('missing')
@click.argument('rule', callback=open_entry_point('dojson.cli.rule'))
def process_missing(rule):
    """List fields with missing rules."""
    def processor(iterator):
        missing = set()
        for item in iterator:
            missing |= set(rule.missing(item))
        missing.discard('__order__')

        if missing:
            click.echo(', '.join(missing), nl=False)
            sys.exit(1)

        click.echo('', nl=False)
        sys.exit(0)

    return processor


@click.command('schema')
@click.argument('schema')
def process_schema(schema):
    """Add $schema to an item."""
    def processor(iterator):
        for item in iterator:
            assert '$schema' not in item
            item['$schema'] = schema
            yield item

    return processor


@click.command('validate')
@click.argument('schema')
def process_validate(schema):
    """Validate data using given JSON schema."""
    import jsonschema

    schema_dir = os.path.dirname(os.path.abspath(schema))
    schema_name = os.path.basename(schema)

    with open(schema) as f:
        schema_json = json.load(f)

    resolver = jsonschema.RefResolver(
        'file://' + '/'.join(os.path.split(schema_dir)) + '/', schema_name
    )
    validator = jsonschema.Draft4Validator(
        schema_json, resolver=resolver, types=(('array', (list, tuple)), )
    )

    def processor(iterator):
        for item in iterator:
            validator.validate(item)
            yield item

    return processor

__all__ = (
    'process_do',
    'process_missing',
    'process_schema',
    'process_validate',
)
