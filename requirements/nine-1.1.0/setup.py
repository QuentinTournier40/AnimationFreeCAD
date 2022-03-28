#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://peak.telecommunity.com/DevCenter/setuptools#developer-s-guide
# from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

requires = []
# Python 2.6 does not have importlib, but a package exists for that
from sys import version_info
if version_info[:2] < (2, 7):
    requires.append('importlib')

setup(
    name="nine",
    version='1.1.0',
    description="Python 2 / 3 compatibility, like six, but favouring Python 3",
    long_description=long_description,
    url='https://github.com/nandoflorestan/nine',
    author='Nando Florestan',
    author_email="nandoflorestan@gmail.com",
    license='Public domain',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nine',
    install_requires=requires,
    keywords=[
        "python 2", 'python 3', 'python2', 'python3', 'migration',
        'compatibility', 'nine', 'six', '2to3', '3to2', 'future',
    ],
    classifiers=[  # http://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'License :: Public Domain',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
