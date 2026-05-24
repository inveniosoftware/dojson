# SPDX-FileCopyrightText: 2015, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Define all DoJSON exceptions."""


class DoJSONException(Exception):
    """Parent for all DoJSON exceptions.

    .. versionadded:: 1.0.0
    """


class IgnoreKey(DoJSONException):
    """The corresponding key has been ignored.

    .. versionadded:: 0.2.0
    """


class IgnoreItem(DoJSONException):
    """The corresponding item from the current iterable has been ignored.

    .. versionadded:: 1.3.0
    """


class MissingRule(DoJSONException):
    """Raise when no matching rule was found.

    .. versionadded:: 1.0.0
    """
