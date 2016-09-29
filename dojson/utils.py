# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utility functions."""

import codecs
import functools
import itertools
import warnings
from collections import Counter, OrderedDict

import simplejson as json

from ._compat import iteritems
from .errors import IgnoreItem, IgnoreKey


def int_with_default(value, default):
    """Parse and integer from a string and return default if it fails."""
    try:
        return int(value)
    except ValueError:
        return default


def ignore_value(f):
    """Remove key for None value.

    .. versionadded:: 0.2.0
    """
    @functools.wraps(f)
    def wrapper(self, key, value, **kwargs):
        result = f(self, key, value, **kwargs)
        if result is None:
            raise IgnoreKey(key)
        return result
    return wrapper


def filter_values(f):
    """Remove None values from dictionary."""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        out = f(*args, **kwargs)
        return dict((k, v) for k, v in iteritems(out) if v is not None)
    return wrapper


def flatten(f):
    """Flatten list of iterables.

    .. versionadded:: 1.3.0
    """
    @functools.wraps(f)
    def wrapper(self, key, values, **kwargs):
        return list(itertools.chain.from_iterable(
            f(self, key, values, **kwargs)
        ))
    return wrapper


def for_each_value(f):
    """Apply function to each item."""
    # Extends values under same name in output.  This should be possible
    # because we are alredy expecting list.
    setattr(f, '__extend__', True)

    @functools.wraps(f)
    def wrapper(self, key, values, **kwargs):
        parsed_values = []

        if not isinstance(values, (list, tuple, set)):
            values = [values]

        for value in values:
            try:
                parsed_values.append(f(self, key, value, **kwargs))
            except IgnoreItem:
                continue

        return parsed_values
    return wrapper


def reverse_for_each_value(f):
    """Undo what `for_each_value` does."""
    @functools.wraps(f)
    def wrapper(self, key, values, **kwargs):
        if isinstance(values, (list, tuple, set)):
            if len(values) == 1:
                return f(self, key, values[0], **kwargs)
            return [f(self, key, value, **kwargs) for value in values]

        return [f(self, key, values, **kwargs)]

    return wrapper


def force_list(data):
    """Wrap data in a tuple.

    Wraps its argument in a tuple so that it can be iterated over, unless
    it was a list, a tuple, or a set (therefore already iterable).

    Note that if ``data`` is ``None`` this method will return ``None``, which
    is not iterable.
    """
    if data is not None and not isinstance(data, (list, tuple, set)):
        return (data,)
    return data


def reverse_force_list(data):
    """Unwrap data from list if its length is == 1."""
    if isinstance(data, (list, tuple, set)) and len(data) == 1:
        return data[0]
    return data


def load(stream):
    """Load JSON from bytestream."""
    reader = codecs.getreader("utf-8")
    return json.load(reader(stream))


def dump(iterator):
    """Dump JSON from iteraror."""
    return json.dumps(list(iterator))


def deprecated(explanation):
    """Decorate as deprecated."""
    def decorator(f):
        @functools.wraps(f)
        def wrapper(self, key, values, **kwargs):
            warnings.warn('{0}: {1}'.format(key, explanation),
                          DeprecationWarning)
            return f(self, key, values, **kwargs)

    return decorator


def map_order(field_map, value):
    """Ordered list of fields to be able to pass the order along.

    .. note:: It returns a list as you may want to alter it based on the
       indicators. The final structure should use a tuple for immutability.

    Returns an empty list if no `__order__' is found in the value.

    .. versionadded:: 1.1.0
    """
    if '__order__'in value:
        order = value['__order__']
    else:
        order = value.keys()

    return [field_map[k] for k in order if field_map.get(k) is not None]


class GroupableOrderedDict(OrderedDict):
    """Immutable list that can group values pretending to be a dict."""

    def __new__(cls, *args):
        """Create a new immutable GroupableOrderedDict."""
        new = OrderedDict.__new__(cls)
        OrderedDict.__init__(new)

        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got {}'
                            .format(len(args)))

        ordering = []
        values = args[0]

        if values:
            if isinstance(values, GroupableOrderedDict):
                values = values.iteritems(with_order=False, repeated=True)
            elif isinstance(values, dict):
                if '__order__' in values:
                    order = values.pop('__order__')

                    tmp = []
                    c = Counter()
                    for key in order:
                        v = values[key]
                        if not isinstance(v, (tuple, list)):
                            if c[key] == 0:
                                tmp.append((key, v))
                            else:
                                raise Exception("Order and values don't match "
                                                "on key {0} at position {1}"
                                                .format(key, c[key]))
                        else:
                            tmp.append((key, v[c[key]]))
                        c[key] += 1
                    values = tmp
                else:
                    values = iteritems(values)

            for key, value in values:
                if key not in new:
                    OrderedDict.__setitem__(new, key, [])
                v = []
                if isinstance(value, (tuple, list)):
                    for item in value:
                        v.append(item)
                        ordering.append(key)
                elif isinstance(value, dict):
                    if '__order__' in value:
                        value = GroupableOrderedDict(value)
                    v.append(value)
                    ordering.append(key)
                else:
                    v.append(value)
                    ordering.append(key)

                OrderedDict.__getitem__(new, key).extend(v)

        # Immutable...
        for key, value in dict.items(new):
            OrderedDict.__setitem__(new, key, tuple(value))

        OrderedDict.__setitem__(new, '__order__', tuple(ordering))
        return new

    def __repr__(self):
        """Output the representation of the GroupableOrderedDict."""
        out = ("({!r}, {!r})".format(k, v)
               for k, v in self.iteritems(repeated=True)
               if k != '__order__')
        return 'GroupableOrderedDict(({out}))'.format(out=', '.join(out))

    __str__ = __repr__

    def __init__(self, *args, **kwargs):
        """Initialize the GroupableOrderedDict.

        It's done in __new__ so the instance cannot be modified through it.
        """

    def __copy__(self):
        """A copy of D."""
        return GroupableOrderedDict(self)

    def __deepcopy__(self, memo=None):
        """A copy of D."""
        return self.__copy__()

    def __reduce__(self):
        """Helper for pickle."""
        return GroupableOrderedDict, (dict(self.items()), )

    def __eq__(self, other):
        """Comparison help."""
        if other is None:
            return False
        if isinstance(other, tuple):
            return False

        if (len(self.keys()) != len(other.keys()) and
                '__order__' not in other and
                len(self.keys()) - 1 == len(other.keys())):

            return False

        for k, vs in self.iteritems():
            if k == '__order__':
                if k in other and vs != other[k]:
                    return False
                else:
                    continue

            if k not in other:
                return False

            if isinstance(vs, (list, tuple, set)):
                # repeatable fields...
                if isinstance(other[k], (list, tuple, set)):
                    for i, v in enumerate(vs):
                        if v != other[k][i]:
                            return False

                elif len(vs) == 1 and vs[0] != other[k][0]:
                    return False

                for i, v in enumerate(vs):
                    if v != other[k][i]:
                        return False
            else:
                # repeatable fields...
                if isinstance(other[k], (list, tuple, set)):
                    if len(other[k]) == 1 and vs != other[k][0]:
                        return False
                    else:
                        continue

                if vs != other[k] and (vs,) != other[k] and [vs] != other[k]:
                    return False
        return True

    def __ne__(self, other):
        """Not equals."""
        return not self.__eq__(other)

    def get(self, key, default=None):
        """D[k] if k in D, else d. d defaults to None."""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, key):
        """D[key].

        It will return a list or an element depending on the quantity present.
        """
        item = OrderedDict.__getitem__(self, key)
        if len(item) == 1 and key != '__order__':
            return item[0]
        return item

    def __setitem__(self, *args, **kwargs):
        """Item assigment is not supported."""
        raise TypeError('{} object does not support item assignment'
                        .format(self.__class__.__name__))

    def __delitem__(self, *args, **kwargs):
        """Item deletion is not supported."""
        raise TypeError('{} object does not support item deletion'
                        .format(self.__class__.__name__))

    def __iter__(self):
        """Iterator."""
        occurences = Counter()
        order = self['__order__']
        yield '__order__'
        for o in order:
            if occurences[o] == 0:
                yield o
            occurences[o] += 1

    def values(self, expand=False):
        """List of D's values grouped by key.

        :param expand: If set to True it will return the raw values in
                       the initial order.
        """
        values = []
        if expand:
            occurences = Counter()
            order = self['__order__']
            for key in order:
                values.append(dict.__getitem__(self, key)[occurences[key]])
                occurences[key] += 1
        else:
            for key, value in OrderedDict.items(self):
                if key == '__order__':
                    continue
                if len(value) == 1:
                    values.append(value[0])
                else:
                    values.append(value)
        return values

    def keys(self, repeated=False):
        """List of D's keys.

        :param repeated: If set to True it will return the ordering of the
                         values rather than the keys. It may contain
                         repetitions.
        """
        if not repeated:
            keys = list(OrderedDict.keys(self))
            keys.remove('__order__')
            return keys
        else:
            return list(self['__order__'])

    def items(self, with_order=True, repeated=False):
        """List of D's (key, value) pairs, as 2-tuples.

        :param with_order: If set to True it will also return a
                           ``(__order__, keys)`` tuples with the ordering.
                           It is usefull to be able to reconstruct this
                           structure later on.
        :param repeated: If set to True it will not group by key and respect
                         the initial ordering.
        """
        return tuple(self.iteritems(with_order, repeated))

    def iteritems(self, with_order=True, repeated=False):
        """Just like D.items() but as an iterator."""
        if not repeated:
            if with_order:
                yield '__order__', dict.__getitem__(self, '__order__')
            occurences = {
                k: len(list(v))
                for k, v in itertools.groupby(sorted(self.keys()))
            }
            for key, value in OrderedDict.items(self):
                if key == '__order__':
                    continue
                if isinstance(value, (list, tuple)) and \
                        len(value) == 1 and \
                        occurences[key] == 1:
                    yield key, value[0]
                else:
                    yield key, value
        else:
            occurences = Counter()
            order = self['__order__']
            if with_order:
                yield '__order__', order
            for key in order:
                yield key, OrderedDict.__getitem__(self, key)[occurences[key]]
                occurences[key] += 1
