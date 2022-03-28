#! /usr/bin/env python

# $Id: test_block_quotes.py 8481 2020-01-31 08:17:24Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Tests for the block quote directives "epigraph", "highlights", and
"pull-quote".
"""
from __future__ import absolute_import

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport

def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

generic_tests = [
["""\
.. %(type)s::

   This is a block quote.

   -- Attribution

   This is another block quote.

   -- Another Attribution,
      Second Line
""",
"""\
<document source="test data">
    <block_quote classes="%(type)s">
        <paragraph>
            This is a block quote.
        <attribution>
            Attribution
    <block_quote classes="%(type)s">
        <paragraph>
            This is another block quote.
        <attribution>
            Another Attribution,
            Second Line
"""],
# TODO: Add class option.
["""\
.. %(type)s::
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Content block expected for the "%(type)s" directive; none found.
        <literal_block xml:space="preserve">
            .. %(type)s::
"""],
]

totest = {}
for block_quote_type in ('epigraph', 'highlights', 'pull-quote'):
   totest[block_quote_type] = [
       [text % {'type': block_quote_type} for text in pair]
       for pair in generic_tests]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
