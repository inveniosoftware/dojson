..
  This file is part of DoJSON
  Copyright (C) 2015 CERN.

  DoJSON is free software; you can redistribute it and/or
  modify it under the terms of the Revised BSD License; see LICENSE
  file for more details.

========
 DoJSON
========
.. currentmodule:: dojson

.. raw:: html

    <p style="height:22px; margin:0 0 0 2em; float:right">
        <a href="https://travis-ci.org/inveniosoftware/dojson">
            <img src="https://travis-ci.org/inveniosoftware/dojson.png?branch=master"
                 alt="travis-ci badge"/>
        </a>
        <a href="https://coveralls.io/r/inveniosoftware/dojson">
            <img src="https://coveralls.io/repos/inveniosoftware/dojson/badge.png?branch=master"
                 alt="coveralls.io badge"/>
        </a>
    </p>

DoJSON is a simple Pythonic JSON to JSON converter.

Installation
============

DoJSON is on PyPI so all you need is:

.. code-block:: console

    $ pip install dojson

Example
=======

A simple example on how to convert MARCXML to JSON:

.. code:: python

    from dojson.contrib.marc21.utils import create_record, split_blob
    from dojson.contrib.marc21 import marc21
    [marc21.do(create_record(data)) for data in split_blob(open('/tmp/data.xml', 'r').read())]


API
===

.. automodule:: dojson
    :members:

.. automodule:: dojson.contrib.marc21
    :members:

.. include:: ../CHANGES.rst

.. include:: ../CONTRIBUTING.rst

.. include:: ../AUTHORS.rst

License
=======

.. include:: ../LICENSE
