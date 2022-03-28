# -*- coding: utf-8 -*-

'''This module is donated to the public domain.'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import unittest


class TestNine(unittest.TestCase):

    def test_import(self):
        from nine import (
            IS_PYTHON2, str, basestring, native_str,
            integer_types, class_types, range, range_list, reraise,
            iterkeys, itervalues, iteritems, map, zip, filter, input,
            implements_iterator, implements_to_string, implements_repr, nine,
            nimport, _moved)
        for key in _moved:
            if key == 'tkinter':
                continue  # travis does not have tk installed :p
            assert nimport(key)
