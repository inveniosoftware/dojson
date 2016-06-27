Contributing
============

Bug reports, feature requests, and other contributions are welcome.
If you find a demonstrable problem that is caused by the code of this
library, please:

1. Search for `already reported problems
   <https://github.com/inveniosoftware/dojson/issues>`_.
2. Check if the issue has been fixed or is still reproducible on the
   latest `master` branch.
3. Create an issue with **a test case**.

If you create a feature branch, you can run the tests to ensure everything is
operating correctly:

.. code-block:: console

    $ python setup.py test

    ...

    ====== 31 passed, 23 skipped in 1.37 seconds ======

You can also test your feature branch using Docker::

  $ docker-compose build
  $ docker-compose run web python setup.py test
  $ docker-compose run web python setup.py build_sphinx
  $ docker-compose run web pydocstyle --match-dir='dojson'
