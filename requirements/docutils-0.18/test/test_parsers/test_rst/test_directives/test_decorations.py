#! /usr/bin/env python

# $Id: test_decorations.py 8481 2020-01-31 08:17:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the "header" & "footer" directives.
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

totest['headers'] = [
["""\
.. header:: a paragraph for the header
""",
"""\
<document source="test data">
    <decoration>
        <header>
            <paragraph>
                a paragraph for the header
"""],
["""\
.. header::
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Content block expected for the "header" directive; none found.
        <literal_block xml:space="preserve">
            .. header::
"""],
["""\
.. header:: first part of the header
.. header:: second part of the header
""",
"""\
<document source="test data">
    <decoration>
        <header>
            <paragraph>
                first part of the header
            <paragraph>
                second part of the header
"""],
]

totest['footers'] = [
["""\
.. footer:: a paragraph for the footer
""",
"""\
<document source="test data">
    <decoration>
        <footer>
            <paragraph>
                a paragraph for the footer
"""],
["""\
.. footer:: even if a footer is declared first
.. header:: the header appears first
""",
"""\
<document source="test data">
    <decoration>
        <header>
            <paragraph>
                the header appears first
        <footer>
            <paragraph>
                even if a footer is declared first
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
