# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test suite for DoJSON contrib MARC21 module."""

import copy
import json
import pytest

from dojson.contrib.marc21.utils import GroupableOrderedDict


@pytest.fixture
def god():
    """Create a GroupableOrderedDict for testing."""
    return GroupableOrderedDict([('a', 'dojson'), ('b', 2), ('c', 'invenio'),
                                 ('a', 4), ('b', 5)])


def test_groupable_ordered_dict_is_immutable(god):
    """Test that a GroupableOrderedDict is immutable indeed."""
    with pytest.raises(TypeError):
        god['a'] = [1, 2]

    with pytest.raises(AttributeError):
        god['a'].append(1)

    god.values().append(('spam', 'ham'))
    with pytest.raises(KeyError):
        god['spam']


def test_groupable_ordered_dict_keys(god):
    """Test that a GroupableOrderedDict has keys like a dict, but more."""
    assert ('a', 'b', 'c') == god.keys()
    assert ('a', 'b', 'c', 'a', 'b') == god.keys(repeated=True)


def test_groupable_ordered_dict_items(god):
    """Test that a GroupableOrderedDict has items like a dict, but more."""
    assert (('a', ('dojson', 4)), ('b', (2, 5)), ('c', 'invenio')) == god.items()
    assert (('__order__', ('a', 'b', 'c', 'a', 'b')),
            ('a', ('dojson', 4)),
            ('b', (2, 5)),
            ('c', 'invenio')) == god.items(with_order=True)


def test_groupable_ordered_dict_get(god):
    """Test that a GroupableOrderedDict has get like a dict."""
    assert ('dojson', 4) == god.get('a')
    assert 'spam' == god.get('d', 'spam')


def test_groupable_ordered_dict_values(god):
    """Test that a GroupableOrderedDict has values like a dict, but more."""
    assert ['dojson', 2, 'invenio', 4, 5] == god.values(expand=True)
    assert [('dojson', 4), (2, 5), 'invenio'] == god.values()


def test_groupable_ordered_dict_eq(god):
    """Test that a GroupableOrderedDict can be compared with ==."""
    expected = {'a': ('dojson', 4), 'b': (2, 5), 'c': 'invenio'}

    assert expected == god
    assert not(expected != god)


def test_groupable_ordered_dict_copy(god):
    """Test that a GroupableOrderedDict can be copied."""
    god2 = copy.copy(god)

    assert god == god2


def test_groupable_ordered_dict_new(god):
    """Test that a GroupableOrderedDict can be created from a same element."""
    god2 = GroupableOrderedDict(god)

    assert god == god2


def test_groupable_ordered_dict_to_json(god):
    """Test that a GroupableOrderedDict can be serialized to JSON."""
    expected = json.dumps({'__order__': ('a', 'b', 'c', 'a', 'b'),
                           'a': ['dojson', 4],
                           'b': [2, 5],
                           'c': 'invenio'},
                          sort_keys=True,
                          indent=4)

    assert expected == json.dumps(god, indent=4)


def test_groupable_ordered_dict_iterable(god):
    """Test that a GroupableOrderedDict is iterable like a dict."""
    iterator = iter(god)

    assert 'a' == iterator.next()
    assert 'b' == iterator.next()
    assert 'c' == iterator.next()
    with pytest.raises(StopIteration):
        iterator.next()


def test_groupable_ordered_dict_recreate(god):
    """Test that a GroupableOrderedDict can be recreated from a dict."""
    god2 = GroupableOrderedDict({'__order__': ('a', 'b', 'c', 'a', 'b'),
                                 'a': ['dojson', 4],
                                 'b': [2, 5],
                                 'c': 'invenio'})

    assert god2 == god
