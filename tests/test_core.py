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
from lxml import etree


RECORD = """<record>
  <controlfield tag="001">17575</controlfield>
  <controlfield tag="005">20150513165819.0</controlfield>
  <datafield tag="024" ind1="7" ind2=" ">
    <subfield code="2">DOI</subfield>
    <subfield code="a">10.5281/zenodo.17575</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">&lt;p&gt;Model definitions and data...&lt;/p&gt;</subfield>
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

# http://www.loc.gov/marc/umb/um07to10.html
RECORD_THEATER = """<record>
  <datafield tag="650" ind1=" " ind2=" ">
    <subfield code="a">Theater</subfield>
    <subfield code="z">United States</subfield>
    <subfield code="v">Biography</subfield>
    <subfield code="v">Dictionaries.</subfield>
  </datafield>
</record>"""

# Requires a liberal MARC
RECORD_AUDUB = """<record>
    <datafield tag="852" ind1="8" ind2=" ">
        <subfield code="i">M 314</subfield>
        <subfield code="h">339</subfield>
        <subfield code="b">Library Reading Room</subfield>
        <subfield code="9">10</subfield>
    </datafield>
</record>"""

# http://www.loc.gov/marc/bibliographic/bd245.html
#
# 245 00 $a Deutsche Bibliographie.
#        $p Wöchentliches Verzeichnis.
#        $n Reihe B,
#        $p Beilage, Erscheinungen ausserhalb des Verlagsbuchhandels :
#        $b Amtsblatt der Deutschen Bibliothek.
RECORD_DEUTSCHE_BIBLIO = """<record>
    <datafield tag="245" ind1="0" ind2="0">
        <subfield code="a">Deutsche Bibliographie.</subfield>
        <subfield code="p">Wöchentliches Verzeichnis.</subfield>
        <subfield code="n">Reihe B,</subfield>
        <subfield code="p">Beilage, Erscheinungen ausserhalb des Verlagsbuchhandels :</subfield>
        <subfield code="b">Amtsblatt der Deutschen Bibliothek.</subfield>
    </datafield>
</record>"""

RECORDS = {
    "base": RECORD,
    "simple": RECORD_SIMPLE,
    "theater": RECORD_THEATER,
    "deutsche biblio": RECORD_DEUTSCHE_BIBLIO
}


def test_index_creation():
    """Test index creation."""
    overdo = dojson.Overdo()

    @overdo.over('247', '^247..')
    def match_247(self, key, value):
        return key, value

    @overdo.over('024', '^024..')
    def match_024(self, key, value):
        return key, value

    data = overdo.do({'0247_': '024', '247__': '247'})

    assert ('0247_', '024') == data['024']
    assert ('247__', '247') == data['247']


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
    from six import BytesIO
    from dojson.contrib.marc21.utils import load

    COLLECTION = '<collection>{0}{1}</collection>'.format(
        RECORD, RECORD_SIMPLE
    )

    records = list(load(BytesIO(COLLECTION.encode('utf-8'))))
    assert len(records) == 2


def test_marc21_split_stream():
    """Test MARC21 split_stream()."""
    from six import StringIO
    from dojson.contrib.marc21.utils import split_stream

    COLLECTION = '<collection>{0}{1}</collection>'.format(
        RECORD, RECORD_SIMPLE
    )
    generator = split_stream(StringIO(COLLECTION.encode('utf-8')))
    assert etree.tostring(generator.next(), method='html') == RECORD
    assert etree.tostring(generator.next(), method='html') == RECORD_SIMPLE


def test_marc21_records_over_single_line():
    """Test records over single line."""
    from six import StringIO, u
    from dojson.contrib.marc21.utils import split_stream

    records = (u('<record>foo</record>'),
               u('<record>会意字</record>'),
               u('<record>&gt;&amp;&lt;</record>'))
    collection = u('<collection>{0}</collection>').format(u('').join(records))

    generator = split_stream(StringIO(collection.encode('utf-8')))
    for record in records:
        result = etree.tostring(generator.next(),
                                encoding='utf-8',
                                method='xml')
        assert record.encode('utf-8') == result


def test_records_marc21_tojson_tomarc21():
    """Test records marc21 - json - marc21."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21 import to_marc21

    for name, record in RECORDS.items():
        blob = create_record(record)
        data = marc21.do(blob)

        back_blob = to_marc21.do(data)

        assert blob == back_blob, name


def test_tomarc21_from_xml():
    """Test MARC21 loading and recreating from XML."""
    from dojson.contrib.marc21 import marc21
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21 import to_marc21

    for name, record in RECORDS.items():
        blob = create_record(record)
        data = marc21.do(blob)

        back_blob = to_marc21.do(data)

        assert blob == back_blob, name


def test_toxml_from_xml():
    """Test MARC21 loading from XML and recreating to XML."""
    from dojson.contrib.marc21.utils import create_record
    from dojson.contrib.to_marc21.utils import dumps
    from lxml import etree, objectify

    for name, record in RECORDS.items():
        blob = create_record(record)
        xml = dumps(blob)

        options = {'xml_declaration': True,
                   'encoding': 'utf8',
                   'pretty_print': True}

        recordxml = ('<collection xmlns="http://www.loc.gov/MARC21/slim">' +
                     record +
                     '</collection>')

        expected = etree.tostring(objectify.fromstring(recordxml), **options)
        actual = etree.tostring(objectify.fromstring(xml), **options)

        assert expected == actual


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
