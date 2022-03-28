#!/usr/bin/env python

# $Id: test_buildhtml.py 8500 2020-03-03 20:53:38Z milde $
# Author: engelbert gruber <grubert@users.sourceforge.net>
# Copyright: This module has been placed in the public domain.

"""
test buildhtml options, because ``--local`` is broken.

Build-HTML Options
------------------
--recurse               Recursively scan subdirectories for files to process.
                        This is the default.
--local                 Do not scan subdirectories for files to process.
--prune=<directory>     Do not process files in <directory>.  This option may
                        be used more than once to specify multiple
                        directories.
--ignore=<patterns>     Recursively ignore files or directories matching any
                        of the given wildcard (shell globbing) patterns
                        (separated by colons).  Default: ".svn:CVS"
--silent                Work silently (no progress messages).  Independent of
                        "--quiet".
"""

import unittest
import os
from subprocess import Popen, PIPE, STDOUT
import sys
import tempfile


buildhtml_path = os.path.abspath(os.path.join(
                    os.path.dirname(__file__) or os.curdir,
                    '..', 'buildhtml.py'))

def process_and_return_filelist(options):
    dirs = []
    files = []
    p = Popen([sys.executable, buildhtml_path] + options,
              stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    (cin, cout) = (p.stdin, p.stdout)
    while True:
        line = cout.readline()
        if not line:
            break
        # in Py 3x, cout.readline() returns `bytes` and the processing fails
        line = line.decode('ascii', 'replace')
        # BUG no colon in filename/path allowed
        item = line.split(": ")[-1].strip()
        if line.startswith(" "):
            files.append(item)
        else:
            dirs.append(item)
    cin.close()
    cout.close()
    p.wait()
    return (dirs, files)

class BuildHtmlTests(unittest.TestCase):
    tree = ( "_tmp_test_tree",
             "_tmp_test_tree/one.txt",
             "_tmp_test_tree/two.txt",
             "_tmp_test_tree/dir1",
             "_tmp_test_tree/dir1/one.txt",
             "_tmp_test_tree/dir1/two.txt",
             "_tmp_test_tree/dir2",
             "_tmp_test_tree/dir2/one.txt",
             "_tmp_test_tree/dir2/two.txt",
             "_tmp_test_tree/dir2/sub",
             "_tmp_test_tree/dir2/sub/one.txt",
             "_tmp_test_tree/dir2/sub/two.txt",
             )

    def setUp(self):
        self.root = tempfile.mkdtemp()

        for s in self.tree:
            s = os.path.join(self.root, s)
            if not "." in s:
                os.mkdir(s)
            else:
                fd_s = open(s, "w")
                fd_s.write("dummy")
                fd_s.close()

    def tearDown(self):
        for i in range(len(self.tree) - 1, -1, -1):
            s = os.path.join(self.root, self.tree[i])
            if not "." in s:
                os.rmdir(s)
            else:
                os.remove(s)
        os.rmdir(self.root)

    def test_1(self):
        opts = ["--dry-run", self.root]
        dirs, files = process_and_return_filelist( opts )
        self.assertEqual(files.count("one.txt"), 4)

    def test_local(self):
        opts = ["--dry-run", "--local", self.root]
        dirs, files = process_and_return_filelist( opts )
        self.assertEqual( len(dirs), 1)
        self.assertEqual( files, [])

if __name__ == '__main__':
    unittest.main()
