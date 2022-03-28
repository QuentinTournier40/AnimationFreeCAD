#! /usr/bin/env python

# $Id: test_unknown.py 8481 2020-01-31 08:17:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for unknown directives.
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

totest['unknown'] = [
["""\
.. reStructuredText-unknown-directive::

.. reStructuredText-unknown-directive:: argument

.. reStructuredText-unknown-directive::
   block
""",
"""\
<document source="test data">
    <system_message level="1" line="1" source="test data" type="INFO">
        <paragraph>
            No directive entry for "reStructuredText-unknown-directive" in module "docutils.parsers.rst.languages.en".
            Trying "reStructuredText-unknown-directive" as canonical directive name.
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive".
        <literal_block xml:space="preserve">
            .. reStructuredText-unknown-directive::
    <system_message level="1" line="3" source="test data" type="INFO">
        <paragraph>
            No directive entry for "reStructuredText-unknown-directive" in module "docutils.parsers.rst.languages.en".
            Trying "reStructuredText-unknown-directive" as canonical directive name.
    <system_message level="3" line="3" source="test data" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive".
        <literal_block xml:space="preserve">
            .. reStructuredText-unknown-directive:: argument
    <system_message level="1" line="5" source="test data" type="INFO">
        <paragraph>
            No directive entry for "reStructuredText-unknown-directive" in module "docutils.parsers.rst.languages.en".
            Trying "reStructuredText-unknown-directive" as canonical directive name.
    <system_message level="3" line="5" source="test data" type="ERROR">
        <paragraph>
            Unknown directive type "reStructuredText-unknown-directive".
        <literal_block xml:space="preserve">
            .. reStructuredText-unknown-directive::
               block
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
