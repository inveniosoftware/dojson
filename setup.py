# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""DoJSON is a simple Pythonic JSON to JSON converter."""

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    """PyTest test runner.

    See: http://pytest.org/latest/goodpractises.html?highlight=setuptools
    """

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        """Initialise test options."""
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        """Finalise test options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Rest tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# Get the version string.  Cannot be done with import!
with open(os.path.join('dojson', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

tests_require = [
    'pytest-cache>=1.0',
    'pytest-cov>=2.1.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
    'coverage>=4.0.0',
    'mock',
]

setup(
    name='dojson',
    version=version,
    url='http://github.com/inveniosoftware/dojson/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description=__doc__,
    long_description=open('README.rst').read(),
    packages=['dojson'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'esmre',
        'lxml',
        'six',
    ],
    extras_require={
        'docs': ['sphinx_rtd_theme'],
        'tests': tests_require,
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ],
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    entry_points={
        'dojson.contrib.marc21': [
            'bd00x = dojson.contrib.marc21.fields.bd00x',
            'bd01x09x = dojson.contrib.marc21.fields.bd01x09x',
            'bd1xx = dojson.contrib.marc21.fields.bd1xx',
            'bd20x24x = dojson.contrib.marc21.fields.bd20x24x',
            'bd25x28x = dojson.contrib.marc21.fields.bd25x28x',
            'bd3xx = dojson.contrib.marc21.fields.bd3xx',
            'bd4xx = dojson.contrib.marc21.fields.bd4xx',
            'bd5xx = dojson.contrib.marc21.fields.bd5xx',
            'bd6xx = dojson.contrib.marc21.fields.bd6xx',
            'bd70x75x = dojson.contrib.marc21.fields.bd70x75x',
            'bd76x78x = dojson.contrib.marc21.fields.bd76x78x',
            'bd80x83x = dojson.contrib.marc21.fields.bd80x83x',
            'bd84188x = dojson.contrib.marc21.fields.bd84188x',
        ]
    }
)
