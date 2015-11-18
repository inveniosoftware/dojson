# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON."""

import dojson
import pytest

RECORD = """<record>
  <controlfield tag="001">17575</controlfield>
  <controlfield tag="005">20150513165819.0</controlfield>
  <datafield tag="024" ind1="7" ind2=" ">
    <subfield code="2">DOI</subfield>
    <subfield code="a">10.5281/zenodo.17575</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">&lt;p>Model definitions and data...&lt;/p></subfield>
  </datafield>
  <datafield tag="540" ind1=" " ind2=" ">
    <subfield code="u"></subfield>
    <subfield code="a">Other (Open)</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="a">other-open</subfield>
    <subfield code="2">opendefinition.org</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">bphi: Initial release</subfield>
  </datafield>
  <datafield tag="542" ind1=" " ind2=" ">
    <subfield code="l">open</subfield>
  </datafield>
  <datafield tag="856" ind1="4" ind2=" ">
    <subfield code="s">272681</subfield>
    <subfield code="u">https://zenodo.org/record/17575/files/...</subfield>
    <subfield code="z">0</subfield>
  </datafield>
  <datafield tag="260" ind1=" " ind2=" ">
    <subfield code="c">2015-05-13</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Matthew Caldwell</subfield>
  </datafield>
  <datafield tag="773" ind1=" " ind2=" ">
    <subfield code="a">https://github.com/bcmd/bphi/tree/v1.0</subfield>
    <subfield code="i">isSupplementTo</subfield>
    <subfield code="n">url</subfield>
  </datafield>
</record>"""

RECORD_SIMPLE = """<record>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Donges, Jonathan F</subfield>
  </datafield>
</record>"""


def test_index_creation():
    """Test index creation."""
    overdo = dojson.Overdo()

    @overdo.over('247', '^247..')
    def match(self, key, value):
        return value

    @overdo.over('024', '^024..')
    def match(self, key, value):
        return value

    data = overdo.do({'0247_': '024', '247__': '247'})

    assert data['024'] == '024'
    assert data['247'] == '247'


def test_missing_fields():
    """Test missing fields."""
    overdo = dojson.Overdo()

    @overdo.over('247', '^247..')
    def match(self, key, value):
        return value

    assert '0247_' in overdo.missing({'0247_': '024', '247__': '247'})


def test_marc21_field_247_matching():
    """Test MARC21 0247/247 field matching."""
    from dojson.contrib.marc21 import marc21

    data = marc21.do({
        '0247_': [{'a': 'A'}],
        '247__': [{'a': 'B'}],
    })

    assert data['other_standard_identifier'][0]['standard_number_or_code'] \
        == 'A'
    assert data['former_title'][0]['title'] == 'B'
    assert len(data) == 2


def test_marc21_from_xml():
    """Test MARC21 loading from XML."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record

    blob = create_record(RECORD)

    data = marc21.do(blob)

    assert 'former_title' not in data


def test_simple_record_from_xml():
    """Test simple record loading from XML."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record

    blob = create_record(RECORD_SIMPLE)
    data = marc21.do(blob)
    expected = {'main_entry_personal_name': {'personal_name': 'Donges, Jonathan F'}}

    assert data == expected


def test_none_value():
    """Test none value."""
    overdo = dojson.Overdo()
    from dojson.utils import ignore_value

    @overdo.over('024', '^024..')
    @ignore_value
    def match(self, key, value):
        return None

    data = overdo.do({'0247_': 'this should not be added'})
    assert "024" not in data, "key with None value should not be added"


def test_no_none_value():
    """Test a valid value with the ignore_value decorator."""
    overdo = dojson.Overdo()
    from dojson.utils import ignore_value

    @overdo.over('024', '^024..')
    @ignore_value
    def match(self, key, value):
        return value

    data = overdo.do({'0247_': 'valid value'})
    assert data.get('024') == 'valid value'


def test_marc21_loader():
    """Test MARC21 loader."""
    from six import StringIO
    from dojson.contrib.marc21.utils import load

    COLLECTION = '<collection>{0}{1}</collection>'.format(
        RECORD, RECORD_SIMPLE
    )

    records = list(load(StringIO(COLLECTION)))
    assert len(records) == 2


def test_marc21_split_stream():
    """Test MARC21 split_stream()."""
    from six import StringIO, u
    from dojson.contrib.marc21.utils import split_stream

    # Testing regular situation
    COLLECTION = '<collection>{0}{1}</collection>'.format(
        RECORD, RECORD_SIMPLE
    )
    generator = split_stream(StringIO(COLLECTION))
    assert generator.next() == RECORD
    assert generator.next() == RECORD_SIMPLE

    # Testing records over single line
    records = StringIO(" <record>foo</record> <record>会意字</record> ")

    generator = split_stream(records)
    assert generator.next() == "<record>foo</record>"
    assert generator.next() == "<record>会意字</record>"


def test_simple_record_tomarc21():
    """Test simple record marc21 - json - marc21."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21 import to_marc21

    blob = create_record(RECORD_SIMPLE)
    data = marc21.do(blob)

    back_blob = to_marc21.do(data)

    assert blob == back_blob


def test_tomarc21_from_xml():
    """Test MARC21 loading and recreating from XML."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21 import to_marc21

    blob = create_record(RECORD)
    data = marc21.do(blob)

    back_blob = to_marc21.do(data)

    assert blob == back_blob


def test_marc21_856_indicators():
    """Test MARC21 856 field special indicator values."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21 import to_marc21

    RECORD_8564 = '''
    <datafield tag="856" ind1="4" ind2=" ">
        <subfield code="s">272681</subfield>
        <subfield code="u">https://zenodo.org/record/17575/files/...</subfield>
        <subfield code="z">0</subfield>
    </datafield>
    '''
    RECORD_8567 = '''
    <datafield tag="856" ind1="7" ind2=" ">
        <subfield code="s">272681</subfield>
        <subfield code="u">https://zenodo.org/record/17575/files/...</subfield>
        <subfield code="z">0</subfield>
        <subfield code="2">Awesome access method</subfield>
    </datafield>
    '''

    expected_8564 = {
        'electronic_location_and_access': [
            {'public_note': ['0'],
             'access_method': 'HTTP',
             'uniform_resource_identifier': [
                 'https://zenodo.org/record/17575/files/...'],
             'file_size': ['272681']}
        ]
    }
    expected_8567 = {
        'electronic_location_and_access': [
            {'public_note': ['0'],
             'access_method': 'Awesome access method',
             'uniform_resource_identifier': [
                 'https://zenodo.org/record/17575/files/...'],
             'file_size': ['272681']}
        ]
    }

    blob = create_record(RECORD_8564)
    data = marc21.do(blob)
    assert data == expected_8564
    back_blob = to_marc21.do(data)
    assert blob == back_blob

    blob = create_record(RECORD_8567)
    data = marc21.do(blob)
    assert data == expected_8567
    back_blob = to_marc21.do(data)
    assert blob == back_blob
