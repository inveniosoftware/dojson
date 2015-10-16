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
import pytest


def test_cli_do_marc21_from_xml():
    """Test MARC21 loading from XML."""
    from dojson import cli
    from test_core import RECORD_SIMPLE

    expected = [{'main_entry_personal_name': {'personal_name': 'Donges, Jonathan F'}}]
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('record.xml', 'wb') as f:
            f.write(RECORD_SIMPLE)

        result = runner.invoke(
            cli.missing_fields,
            ['-i', 'record.xml', '-l', 'marcxml', 'marc21']
        )
        assert result.output == ''
        assert result.exit_code == 0

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record.xml', '-l', 'marcxml', 'marc21']
        )
        data = json.loads(result.output)
        assert data == expected


def test_cli_do_marc21_from_json():
    """Test MARC21 loading from XML."""
    from dojson import cli
    from dojson.contrib.marc21.utils import create_record
    from test_core import RECORD_SIMPLE

    expected = {'main_entry_personal_name': {'personal_name': 'Donges, Jonathan F'}}
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('record.json', 'wb') as f:
            f.write(json.dumps(create_record(RECORD_SIMPLE)))

        result = runner.invoke(
            cli.missing_fields,
            ['-i', 'record.json', 'marc21']
        )
        assert result.output == ''
        assert result.exit_code == 0

        result = runner.invoke(
            cli.apply_rule,
            ['-i', 'record.json', 'marc21']
        )
        data = json.loads(result.output)
        assert data == expected
