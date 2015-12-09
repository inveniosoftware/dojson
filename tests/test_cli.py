# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON."""

from click.testing import CliRunner

import json


def test_cli_do_marc21_from_xml():
    """Test MARC21 loading from XML."""
    from dojson import cli
    from dojson.utils import GroupableOrderedDict
    from test_core import RECORD_SIMPLE, RECORD_999_FIELD

    expected = {'main_entry_personal_name': {'personal_name': 'Donges, Jonathan F'}}
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('record.xml', 'wb') as f:
            f.write(RECORD_SIMPLE.encode('utf-8'))

        with open('record_999.xml', 'wb') as f:
            f.write(RECORD_999_FIELD.encode('utf-8'))

        result = runner.invoke(
            cli.missing_fields,
            ['-i', 'record.xml', '-l', 'marcxml', 'marc21']
        )
        assert result.output == ''
        assert result.exit_code == 0

        result = runner.invoke(
            cli.missing_fields,
            ['-i', 'record_999.xml', '-l', 'marcxml', 'marc21']
        )
        assert result.output == '999__\n'
        assert result.exit_code == 1

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record.xml', '-l', 'marcxml', 'marc21']
        )
        data = json.loads(result.output)
        assert GroupableOrderedDict(expected) == data[0]

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record_999.xml', '-l', 'marcxml', 'marc21']
        )
        data = json.loads(result.output)
        assert {} == data[0]
        assert result.exit_code == 0

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record.xml', '-l', 'marcxml', '--strict', 'marc21']
        )
        assert result.exit_code == -1


def test_cli_do_marc21_from_json():
    """Test MARC21 loading from XML."""
    from dojson import cli
    from dojson.utils import GroupableOrderedDict
    from dojson.contrib.marc21.utils import create_record
    from test_core import RECORD_SIMPLE

    expected = {'main_entry_personal_name': {'personal_name': 'Donges, Jonathan F'}}
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('record.json', 'wb') as fp:
            record = create_record(RECORD_SIMPLE)
            fp.write(json.dumps(record).encode('utf-8'))

        result = runner.invoke(
            cli.missing_fields,
            ['-i', 'record.json', 'marc21']
        )
        assert '' == result.output, result.exception
        assert 0 == result.exit_code

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record.json', 'marc21']
        )

        assert 0 == result.exit_code, result.exception

        data = json.loads(result.output)
        assert GroupableOrderedDict(expected) == data
