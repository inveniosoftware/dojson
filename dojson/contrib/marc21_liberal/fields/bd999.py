from dojson import utils
from dojson.errors import IgnoreKey
from dojson.contrib.marc21 import marc21

@marc21.over('9XX', '^9....')
@marc21.over('X9X', '^.9...')
@marc21.over('XX9', '^..9..')
def local(self, key, values):
    """Local."""
    def assert_and_append(value):
        assert isinstance(value, (dict, utils.GroupableOrderedDict)), value

        value = utils.GroupableOrderedDict(
            list(value.items(with_order=False)) + [('$ind1', key[3]), ('$ind2', key[4])]
        )
        self[field].append(value)

    field = key[:3]
    self.setdefault(field, list())

    if isinstance(values, (list, tuple, set)):
        for value in values:
            assert_and_append(value)
    else:
        assert_and_append(values)

    raise IgnoreKey
