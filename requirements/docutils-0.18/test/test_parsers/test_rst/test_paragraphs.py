#! /usr/bin/env python

# $Id: test_paragraphs.py 8481 2020-01-31 08:17:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for states.py.
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

totest['paragraphs'] = [
["""\
A paragraph.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph.
"""],
["""\
Paragraph 1.

Paragraph 2.
""",
"""\
<document source="test data">
    <paragraph>
        Paragraph 1.
    <paragraph>
        Paragraph 2.
"""],
["""\
Line 1.
Line 2.
Line 3.
""",
"""\
<document source="test data">
    <paragraph>
        Line 1.
        Line 2.
        Line 3.
"""],
["""\
Paragraph 1, Line 1.
Line 2.
Line 3.

Paragraph 2, Line 1.
Line 2.
Line 3.
""",
"""\
<document source="test data">
    <paragraph>
        Paragraph 1, Line 1.
        Line 2.
        Line 3.
    <paragraph>
        Paragraph 2, Line 1.
        Line 2.
        Line 3.
"""],
["""\
A. Einstein was a really
smart dude.
""",
"""\
<document source="test data">
    <paragraph>
        A. Einstein was a really
        smart dude.
"""],
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
