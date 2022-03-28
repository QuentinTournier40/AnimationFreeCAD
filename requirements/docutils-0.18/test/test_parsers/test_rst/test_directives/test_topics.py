#! /usr/bin/env python

# $Id: test_topics.py 8481 2020-01-31 08:17:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the "topic" directive.
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

totest['topics'] = [
["""\
.. topic::
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Error in "topic" directive:
            1 argument(s) required, 0 supplied.
        <literal_block xml:space="preserve">
            .. topic::
"""],
["""\
.. topic:: Title
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Content block expected for the "topic" directive; none found.
        <literal_block xml:space="preserve">
            .. topic:: Title
"""],
["""\
.. topic:: Title

   Body.
""",
"""\
<document source="test data">
    <topic>
        <title>
            Title
        <paragraph>
            Body.
"""],
["""\
.. topic:: With Options
   :class: custom
   :name: my point

   Body.
""",
"""\
<document source="test data">
    <topic classes="custom" ids="my-point" names="my\\ point">
        <title>
            With Options
        <paragraph>
            Body.
"""],
["""\
.. topic::

   Title

   Body.
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Error in "topic" directive:
            1 argument(s) required, 0 supplied.
        <literal_block xml:space="preserve">
            .. topic::
            \n\
               Title
            \n\
               Body.
"""],
["""\
.. topic:: Title
   Body.
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Content block expected for the "topic" directive; none found.
        <literal_block xml:space="preserve">
            .. topic:: Title
               Body.
"""],
["""\
.. topic::

   Title
   Body.
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Error in "topic" directive:
            1 argument(s) required, 0 supplied.
        <literal_block xml:space="preserve">
            .. topic::
            \n\
               Title
               Body.
"""],
["""\
.. topic:: Title

   .. topic:: Nested

      Body.
""",
"""\
<document source="test data">
    <topic>
        <title>
            Title
        <system_message level="3" line="3" source="test data" type="ERROR">
            <paragraph>
                The "topic" directive may not be used within topics or body elements.
            <literal_block xml:space="preserve">
                .. topic:: Nested
                \n\
                   Body.
"""],
["""\
.. topic:: Title

   .. topic:: Nested

      Body.
   More.
""",
"""\
<document source="test data">
    <topic>
        <title>
            Title
        <system_message level="3" line="3" source="test data" type="ERROR">
            <paragraph>
                The "topic" directive may not be used within topics or body elements.
            <literal_block xml:space="preserve">
                .. topic:: Nested
                \n\
                   Body.
        <system_message level="2" line="6" source="test data" type="WARNING">
            <paragraph>
                Explicit markup ends without a blank line; unexpected unindent.
        <paragraph>
            More.
"""],
["""\
.. topic:: Title

   .. topic:: Nested

      Body.

   More.

More.
""",
"""\
<document source="test data">
    <topic>
        <title>
            Title
        <system_message level="3" line="3" source="test data" type="ERROR">
            <paragraph>
                The "topic" directive may not be used within topics or body elements.
            <literal_block xml:space="preserve">
                .. topic:: Nested
                \n\
                   Body.
        <paragraph>
            More.
    <paragraph>
        More.
"""],
["""\
.. topic:: First

   Body

.. topic:: Second

   Body.
""",
"""\
<document source="test data">
    <topic>
        <title>
            First
        <paragraph>
            Body
    <topic>
        <title>
            Second
        <paragraph>
            Body.
"""],
["""\
.. sidebar:: Title
   :subtitle: Outer

   .. topic:: Nested

      Body.

   More.

More.
""",
"""\
<document source="test data">
    <sidebar>
        <title>
            Title
        <subtitle>
            Outer
        <topic>
            <title>
                Nested
            <paragraph>
                Body.
        <paragraph>
            More.
    <paragraph>
        More.
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
