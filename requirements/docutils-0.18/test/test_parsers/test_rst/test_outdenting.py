#! /usr/bin/env python

# $Id: test_outdenting.py 8481 2020-01-31 08:17:24Z milde $
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

totest['outdenting'] = [
["""\
Anywhere a paragraph would have an effect on the current
indentation level, a comment or list item should also.

+ bullet

This paragraph ends the bullet list item before a block quote.

  Block quote.
""",
"""\
<document source="test data">
    <paragraph>
        Anywhere a paragraph would have an effect on the current
        indentation level, a comment or list item should also.
    <bullet_list bullet="+">
        <list_item>
            <paragraph>
                bullet
    <paragraph>
        This paragraph ends the bullet list item before a block quote.
    <block_quote>
        <paragraph>
            Block quote.
"""],
["""\
+ bullet

.. Comments swallow up all indented text following.

  (Therefore this is not a) block quote.

- bullet

  If we want a block quote after this bullet list item,
  we need to use an empty comment:

..

  Block quote.
""",
"""\
<document source="test data">
    <bullet_list bullet="+">
        <list_item>
            <paragraph>
                bullet
    <comment xml:space="preserve">
        Comments swallow up all indented text following.
        \n\
        (Therefore this is not a) block quote.
    <bullet_list bullet="-">
        <list_item>
            <paragraph>
                bullet
            <paragraph>
                If we want a block quote after this bullet list item,
                we need to use an empty comment:
    <comment xml:space="preserve">
    <block_quote>
        <paragraph>
            Block quote.
"""],
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
