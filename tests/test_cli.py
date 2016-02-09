# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON."""

import codecs
import os

import pytest
import simplejson as json
from click.testing import CliRunner

from dojson import cli
from dojson.contrib.marc21.utils import create_record
from test_core import RECORD_999_FIELD, RECORD_SIMPLE


@pytest.mark.parametrize('file_name', [
    'test_1.xml',
    'test_2.xml',
    'test_3.xml',
    'test_4.xml',
    'test_5.xml',
    'test_6.xml',
    'test_7.xml',
    'test_8.xml',
    'test_9.xml',
    'test_11.xml',
    'test_12.xml',
    'test_13.xml',
    'test_14.xml',
    'test_15.xml',
    'test_16.xml',
])
def test_xml_to_marc21_to_xml(file_name):
    """Test xslt dump."""
    path = os.path.dirname(__file__)
    # Open explicitly as UTF-8 for Python 2.7 compatibility
    with codecs.open(
            '{0}/data/{1}'.format(path, file_name),
            'r',
            'utf-8') as myfile:
        expect = myfile.read()

    runner = CliRunner()
    result = runner.invoke(
        cli.cli, [
            '-i', '{0}/data/{1}'.format(path, file_name),
            '-l', 'marcxml',
            '-d', 'marcxml',
            'do', 'marc21',
            'do', 'to_marc21',
        ]
    )

    assert expect.strip('\n') == result.output.strip('\n')
    assert result.exit_code == 0


def test_cli_do_marc21_from_xml():
    """Test MARC21 loading from XML."""
    expected = [{
        '__order__': ['main_entry_personal_name'],
        'main_entry_personal_name': [
            {
                '__order__': ['personal_name'],
                'personal_name': 'Donges, Jonathan F',
            }
        ],
    }]

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('record.xml', 'wb') as f:
            f.write(RECORD_SIMPLE.encode('utf-8'))

        result = runner.invoke(
            cli.cli,
            ['-i', 'record.xml', '-l', 'marcxml', 'missing', 'marc21']
        )
        assert '' == result.output
        assert 0 == result.exit_code

        result = runner.invoke(
            cli.cli,
            ['-i', 'record.xml', '-l', 'marcxml', 'do', 'marc21']
        )

        try:
            data = json.loads(result.output)
            assert expected == data
        except ValueError:
            assert False, result.output

        result = runner.invoke(
            cli.cli,
            ['-i', 'record.xml', '-l', 'marcxml', 'do', '--strict', 'marc21']
        )
        assert 0 == result.exit_code


def test_cli_do_marc21_from_xml_unknown_fields():
    """Test MARC21 loading from XML containing unknown fields."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('record_999.xml', 'wb') as f:
            f.write(RECORD_999_FIELD.encode('utf-8'))

        result = runner.invoke(
            cli.cli,
            ['-i', 'record_999.xml', '-l', 'marcxml', 'missing', 'marc21']
        )
        assert "999__" == result.output.strip()
        assert 1 == result.exit_code
        result = runner.invoke(
            cli.cli,
            ['-i', 'record_999.xml', '-l', 'marcxml', 'do', 'marc21']
        )

        data = json.loads(result.output)
        assert {'__order__': []} == data[0]
        assert 0 == result.exit_code


def test_cli_do_marc21_from_json():
    """Test MARC21 loading from XML."""
    expected = [{
        '$schema': '/schema.json',
        '__order__': ['main_entry_personal_name'],
        'main_entry_personal_name': [
            {
                '__order__': ['personal_name'],
                'personal_name': 'Donges, Jonathan F',
            }
        ],
    }]

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('record.json', 'wb') as fp:
            record = create_record(RECORD_SIMPLE)
            fp.write(json.dumps(record).encode('utf-8'))

        result = runner.invoke(
            cli.cli,
            ['-i', 'record.json', 'missing', 'marc21']
        )
        assert '' == result.output, result.exception
        assert 0 == result.exit_code

        result = runner.invoke(
            cli.cli,
            ['-i', 'record.json', 'do', 'marc21', 'schema', '/schema.json']
        )

        assert 0 == result.exit_code, result.exception

        try:
            data = json.loads(result.output)
            assert expected == data
        except ValueError:
            assert False, result.output
