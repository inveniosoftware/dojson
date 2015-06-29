#!/bin/sh
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

pep257 --match-dir='dojson' dojson && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
