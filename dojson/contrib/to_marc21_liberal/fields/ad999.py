from dojson import utils
from dojson.errors import IgnoreKey
from dojson.contrib.to_marc21 import to_marc21_authority

@to_marc21_authority.over('9XX', '^9..$')
@to_marc21_authority.over('X9X', '^.9.$')
@to_marc21_authority.over('XX9', '^..9$')
def reverse_local(self, key, values):
    """Reverse Local."""
    for value in values:
        value = dict(value.items())
        field = '{0}{1}{2}'.format(
            key,
            value.pop('$ind1', '_'),
            value.pop('$ind2', '_')
        )
        if '__order__' in value:
            value['__order__'] = list(value['__order__'])
            if '$ind1' in value['__order__']:
                value['__order__'].remove('$ind1')
            if '$ind2' in value['__order__']:
                value['__order__'].remove('$ind2')

            value = utils.GroupableOrderedDict(value)
        self.append((field, value))
    raise IgnoreKey
