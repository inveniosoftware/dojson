# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON."""

import json

from click.testing import CliRunner

from dojson import cli
from dojson.contrib.marc21.utils import create_record
from test_core import RECORD_SIMPLE, RECORD_999_FIELD


def test_cli_do_marc21_from_xml():
    """Test MARC21 loading from XML."""
    expected = [{
        'main_entry_personal_name': {
            'personal_name': 'Donges, Jonathan F'
        }
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
        assert -1 == result.exit_code


def test_cli_do_marc21_from_xml_unknown_fieds():
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
        assert {} == data[0]
        assert 0 == result.exit_code


def test_cli_do_marc21_from_json():
    """Test MARC21 loading from XML."""
    expected = [{
        '$schema': '/schema.json',
        'main_entry_personal_name': {
            'personal_name': 'Donges, Jonathan F'
        }
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
