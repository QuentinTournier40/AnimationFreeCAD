#! /usr/bin/env python

# $Id: test_default_role.py 8481 2020-01-31 08:17:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for misc.py "default-role" directive.
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

totest['default-role'] = [
["""\
.. default-role:: subscript

This is a `subscript`.
""",
"""\
<document source="test data">
    <paragraph>
        This is a \n\
        <subscript>
            subscript
        .
"""],
["""\
Must define a custom role before using it.

.. default-role:: custom
""",
"""\
<document source="test data">
    <paragraph>
        Must define a custom role before using it.
    <system_message level="1" line="3" source="test data" type="INFO">
        <paragraph>
            No role entry for "custom" in module "docutils.parsers.rst.languages.en".
            Trying "custom" as canonical role name.
    <system_message level="3" line="3" source="test data" type="ERROR">
        <paragraph>
            Unknown interpreted text role "custom".
        <literal_block xml:space="preserve">
            .. default-role:: custom
"""],
["""\
.. role:: custom
.. default-role:: custom

This text uses the `default role`.

.. default-role::

Returned the `default role` to its standard default.
""",
"""\
<document source="test data">
    <paragraph>
        This text uses the \n\
        <inline classes="custom">
            default role
        .
    <paragraph>
        Returned the \n\
        <title_reference>
            default role
         to its standard default.
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
