DoJSON
======

Simple pythonic JSON to JSON converter.

Example
-------

Simple example how to convert MARC XML to JSON.

.. code:: python

    from dojson.contrib.marc21.utils import create_record, split_blob
    from dojson.contrib.marc21 import marc21
    [marc21.do(create_record(data)) for data in split_blob(open('./data.xml', 'r').read())]
