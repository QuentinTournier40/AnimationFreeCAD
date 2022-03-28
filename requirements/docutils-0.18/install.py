#!/usr/bin/env python
# $Id: install.py 8346 2019-08-26 12:11:32Z milde $
# Copyright: This file has been placed in the public domain.

"""
This is a quick & dirty installation shortcut. It is equivalent to the
command::

    python setup.py install

However, the shortcut lacks error checking and command-line option
processing.  If you need any kind of customization or help, please use
one of::

    python setup.py install --help
    python setup.py --help
"""
from __future__ import print_function

from distutils import core
from setup import do_setup

if __name__ == '__main__':
    print(__doc__)
    core._setup_stop_after = 'config'
    dist = do_setup()
    dist.commands = ['install']
    dist.run_commands()
