#!/usr/bin/env python

# $Id: test_odt.py 8481 2020-01-31 08:17:24Z milde $
# Author: Dave Kuhlman <dkuhlman@rexx.com>
# Copyright: This module has been placed in the public domain.

"""
Tests for docutils odtwriter.

Instructions for adding a new test:

1. Add a new method to class DocutilsOdtTestCase (below) named
   test_odt_xxxx, where xxxx describes your new feature.  See
   test_odt_basic for an example.

2. Add a new input reST (.txt) file in test/functional/input. This
   file should contain the smallest amount of reST that tests your
   new feature.  Name this file odt_xxxx.txt.

3. Convert your input reST (.txt) file to an ODF (.odt) file using
   rst2odt.py.  Place this ODF (.odt) file in
   test/functional/expected.  Name this file odt_xxxx.odt.
   You can also pass parameter save_output_name='filename' to method
   process_test() in order to produce expected output.
   See and modify variable TEMP_FILE_PATH for destination.

4. Run your test.  Your new test should pass.

5. If any other tests fail, that's a possible regression.

"""
from __future__ import absolute_import

import os
import zipfile
import xml.etree.ElementTree as etree
from io import BytesIO

if __name__ == '__main__':
    import __init__
from test_writers import DocutilsTestSupport
import docutils
import docutils.core

#
# Globals
TEMP_FILE_PATH = 'functional/output/'
INPUT_PATH = 'functional/input/'
EXPECTED_PATH = 'functional/expected/'


class DocutilsOdtTestCase(DocutilsTestSupport.StandardTestCase):

    def process_test(self, input_filename, expected_filename, 
            save_output_name=None, settings_overrides=None):
        # Test that xmlcharrefreplace is the default output encoding
        # error handler.
        input_file = open(INPUT_PATH + input_filename, 'rb')
        expected_file = open(EXPECTED_PATH + expected_filename, 'rb')
        input = input_file.read()
        expected = expected_file.read()
        input_file.close()
        expected_file.close()
        if settings_overrides is None:
            settings_overrides={}
            settings_overrides['_disable_config'] = True
            settings_overrides['language_code'] = 'en-US'

        result = docutils.core.publish_string(
            source=input,
            reader_name='standalone',
            writer_name='odf_odt',
            settings_overrides=settings_overrides)
##         msg = 'file length not equal: expected length: %d  actual length: %d' % (
##             len(expected), len(result), )
##         self.assertEqual(str(len(result)), str(len(expected)))
        if save_output_name:
            filename = '%s%s%s' % (TEMP_FILE_PATH, os.sep, save_output_name,)
            outfile = open(filename, 'wb')
            outfile.write(result)
            outfile.close()
        content1 = self.extract_file(result, 'content.xml')
        content2 = self.extract_file(expected, 'content.xml')
        msg = 'content.xml not equal: expected len: %d  actual len: %d' % (
            len(content2), len(content1), )
        self.assertEqual(content1, content2, msg)

    def reorder_attributes(self, root):
        """
        Make attribute order independent of python version. 
        python3.8 is different to previous.
        """
        for el in root.iter():
            attrib = el.attrib
            if len(attrib) > 1:
                # adjust attribute order, e.g. by sorting
                attribs = sorted(attrib.items())
                attrib.clear()
                attrib.update(attribs)

    def extract_file(self, payload, filename):
        payloadfile = BytesIO()
        payloadfile.write(payload)
        payloadfile.seek(0)
        zfile = zipfile.ZipFile(payloadfile, 'r')
        content1 = zfile.read(filename)
        doc = etree.fromstring(content1)
        self.reorder_attributes(doc)
        #content2 = doc.toprettyxml(indent='  ')
        content2 = etree.tostring(doc)
        return content2

    def assertEqual(self, first, second, msg=None):
        if msg is None:
            msg2 = msg
        else:
            sep = '+' * 60
            msg1 = '\n%s\nresult:\n%s\n%s\nexpected:\n%s\n%s' % (
                sep, first, sep, second, sep, )
            #msg2 = '%s\n%s' % (msg1, msg, )
            msg2 = '%s' % (msg, )
        DocutilsTestSupport.StandardTestCase.assertEqual(self,
            first, second, msg2)

    #
    # Unit test methods
    #
    # All test methods should be named "test_odt_xxxx", where
    #     xxxx is replaced with a name for the new test.
    # See instructions above in module doc-string.
    #

    def test_odt_basic(self):
        self.process_test('odt_basic.txt', 'odt_basic.odt',
            save_output_name='odt_basic.odt'
            )

    def test_odt_nested_class(self):
        self.process_test('odt_nested_class.txt',
                          'odt_nested_class.odt',
                          save_output_name='odt_nested_class.odt'
        )
        self.process_test('odt_unnested_class.txt',
                          'odt_unnested_class.odt',
                          save_output_name='odt_unnested_class.odt'
        )
        self.process_test('odt_no_class.txt',
                          'odt_no_class.odt',
                          save_output_name='odt_no_class.odt'
        )

    def test_odt_tables1(self):
        self.process_test('odt_tables1.txt', 'odt_tables1.odt',
            save_output_name='odt_tables1.odt'
            )

    def test_odt_custom_headfoot(self):
        settings_overrides = {
            'custom_header': 'Page %p% of %P%',
            'custom_footer': 'Title: %t%  Date: %d3%  Time: %t4%',
            'language_code': 'en-US',
            }
        self.process_test('odt_custom_headfoot.txt', 'odt_custom_headfoot.odt',
            settings_overrides=settings_overrides,
            save_output_name='odt_custom_headfoot.odt'
            )

    def test_odt_header_footer(self):
        self.process_test('odt_header_footer.txt', 'odt_header_footer.odt',
            save_output_name='odt_header_footer.odt'
            )

    def test_odt_literal_block(self):
        self.process_test('odt_literal_block.txt', 'odt_literal_block.odt')

    def test_odt_contents(self):
        self.process_test('odt_contents.txt', 'odt_contents.odt')

    def test_odt_classifier(self):
        self.process_test('odt_classifier.txt', 'odt_classifier.odt')

    def test_odt_footnotes(self):
        self.process_test('odt_footnotes.txt', 'odt_footnotes.odt',
            save_output_name='odt_footnotes.odt'
            )
    def test_odt_raw(self):
        self.process_test('odt_raw.txt', 'odt_raw.odt',
            save_output_name='odt_raw.odt'
            )

    #
    # Template for new tests.
    # Also add functional/input/odt_xxxx.txt and
    #   functional/expected/odt_xxxx.odt
    # Replace all xxxx with name of your test.
    #
##     def test_odt_xxxx(self):
##         self.process_test('odt_xxxx.txt', 'odt_xxxx.odt')


# -----------------------------------------------------------------


if __name__ == '__main__':
    import unittest
    unittest.main()
