#! /usr/bin/env python

# $Id: test_class.py 8481 2020-01-31 08:17:24Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Tests for the 'class' directive.
"""
from __future__ import absolute_import

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport

def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['class'] = [
["""\
.. class:: class1  class2
""",
"""\
<document source="test data">
    <pending>
        .. internal attributes:
             .transform: docutils.transforms.misc.ClassAttribute
             .details:
               class: ['class1', 'class2']
               directive: 'class'
"""],
["""\
.. class:: class1  class2

   The classes are applied to this paragraph.

   And this one.
""",
"""\
<document source="test data">
    <paragraph classes="class1 class2">
        The classes are applied to this paragraph.
    <paragraph classes="class1 class2">
        And this one.
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
