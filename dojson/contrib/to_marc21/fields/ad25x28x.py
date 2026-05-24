# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_authority


@to_marc21_authority.over('260', '^complex_see_reference_subject$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_complex_see_reference_subject(self, key, value):
    """Reverse - Complex See Reference-Subject."""
    field_map = {
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
        'authority_record_control_number': '0',
        'linkage': '6',
        'field_link_and_sequence_number': '8',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': '_',
    }
