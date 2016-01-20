# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON to_marc21."""

import os

import pkg_resources

import pytest
from click.testing import CliRunner
from dojson.contrib.marc21.utils import load
from dojson.contrib.to_marc21.utils import dumps
from test_core import RECORD_SIMPLE


def test_xslt_not_found():
    """Test xslt not found."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('record.xml', 'wb') as f:
            f.write(RECORD_SIMPLE.encode('utf-8'))
        data = list(load('record.xml'))
        pytest.raises(IOError, dumps, data, xslt_filename='file_not_exist')


def test_xslt_dump():
    """Test xslt dump."""
    path = os.path.dirname(__file__)
    with open("{0}/demo_marc21_to_dc.converted.xml".format(path)) as myfile:
        expect = myfile.read().replace('\n', '')
    data = list(load('{0}/demo_marc21_to_dc.xml'.format(path)))
    output = dumps(
        data,
        xslt_filename='{0}/demo_marc21_to_dc.xslt'.format(path)
    )
    assert output.decode('utf-8') == expect


def test_entry_points():
    """Test entry points."""
    dump = list(pkg_resources.iter_entry_points(
        'dojson.cli.dump', 'marcxml'
    ))[0].load()
    path = os.path.dirname(__file__)
    with open("{0}/demo_marc21_to_dc.converted.xml".format(path)) as myfile:
        expect = myfile.read().replace('\n', '')
    data = list(load('{0}/demo_marc21_to_dc.xml'.format(path)))
    output = dump(data,
                  xslt_filename='{0}/demo_marc21_to_dc.xslt'.format(path))
    assert output.decode('utf-8') == expect
