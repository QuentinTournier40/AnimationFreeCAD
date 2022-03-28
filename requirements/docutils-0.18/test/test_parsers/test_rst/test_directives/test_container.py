#! /usr/bin/env python

# $Id: test_container.py 8765 2021-06-17 09:59:43Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the 'container' directive from body.py.
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

totest['container'] = [
["""\
.. container::

   "container" is a generic element, an extension mechanism for
   users & applications.

   Containers may contain arbitrary body elements.
""",
"""\
<document source="test data">
    <container>
        <paragraph>
            "container" is a generic element, an extension mechanism for
            users & applications.
        <paragraph>
            Containers may contain arbitrary body elements.
"""],
["""\
.. container:: custom

   Some text.
""",
"""\
<document source="test data">
    <container classes="custom">
        <paragraph>
            Some text.
"""],
["""\
.. container:: one two three
   four

   Multiple classes.

   Multi-line argument.

   Multiple paragraphs in the container.
""",
"""\
<document source="test data">
    <container classes="one two three four">
        <paragraph>
            Multiple classes.
        <paragraph>
            Multi-line argument.
        <paragraph>
            Multiple paragraphs in the container.
"""],
["""\
.. container::
   :name: my name

   The name argument allows hyperlinks to `my name`_.
""",
"""\
<document source="test data">
    <container ids="my-name" names="my\\ name">
        <paragraph>
            The name argument allows hyperlinks to \n\
            <reference name="my name" refname="my name">
                my name
            .
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
