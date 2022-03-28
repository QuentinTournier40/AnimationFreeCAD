# -*- coding: utf-8 -*-

"""For documentation and usage, please see the file README.rst.

This module is donated to the public domain.
"""

import sys

# Test for Python 2, not 3; don't get bitten when Python 4 appears:
IS_PYTHON2 = (sys.version_info[0] == 2)
IS_PYPY = hasattr(sys, 'pypy_translation_info')
from importlib import import_module

if IS_PYTHON2:  # Rename Python 2 builtins so they become like Python 3
    native_str = bytes
    str = unicode
    basestring = basestring
    byte_chr = chr  # does not seem to have an equivalent in Python 3.
    chr = unichr  # takes an int and returns the corresponding unicode char
    integer_types = (int, long)
    long = long
    from types import ClassType
    class_types = (type, ClassType)
    del ClassType
    range_list = range
    range = xrange
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
    from itertools import ifilter as filter, imap as map, izip as zip
    # In Python 2, *input* was equivalent to eval(raw_input(prompt)):
    input = raw_input
else:  # For Python 3, declare these variables so they can be chain imported:
    basestring = native_str = str = str
    chr = chr  # No need to do the same to ord()
    integer_types = (int,)
    long = int
    class_types = type
    range = range
    range_list = lambda *a: list(range(*a))
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())
    filter = filter
    map = map
    zip = zip
    input = input

if IS_PYTHON2:
    # Turn code into string to avoid SyntaxError on Python 3:
    exec('def reraise(tp, value, tb=None):\n  raise tp, value, tb')
else:
    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

# ===== Class decorators =====
if IS_PYTHON2:
    def implements_to_string(cls):
        """Class decorator that converts __str__() and __bytes__.

        You define __str__() and it is moved to __unicode__() on Python 2.

        Additionally, if you define __bytes__(), it becomes __str__() on
        Python 2. If __bytes__() is not defined, __str__() executes
        __unicode__() and encodes the result to utf-8.
        """
        cls.__unicode__ = cls.__str__
        cls.__str__ = cls.__bytes__ if hasattr(cls, '__bytes__') \
            else lambda x: x.__unicode__().encode('utf-8')
        return cls

    def implements_iterator(cls):
        """Class decorator. next() has been renamed to __next__()."""
        cls.next = cls.__next__
        del cls.__next__
        return cls

    def implements_repr(cls):
        """Class decorator that wraps __repr__() in Python 2.

        You implement __repr__() returning a unicode string,
        and in Python 2, I encode it to utf-8 for you.
        """
        cls.__repr_unicode__ = cls.__repr__

        def wrapper(self):
            return self.__repr_unicode__().encode('utf-8')
        cls.__repr__ = wrapper
        return cls

    def nine(cls):
        """Class decorator for Python 2 and 3 compatibility of magic methods.

        You define the magic methods with their Python 3 names and,
        on Python 2, they get their corresponding names. You may write:

        * __next__(). Use the next(iterator) function to iterate.
        * __str__(): must return a unicode string.
        * __repr__(): must return a unicode string.
        * __bytes__(): must return a bytes object.

        (*nine* is all the above class decorators in one.)
        """
        if hasattr(cls, '__str__'):
            cls = implements_to_string(cls)
        if hasattr(cls, '__next__'):
            cls = implements_iterator(cls)
        if hasattr(cls, '__repr__'):
            cls = implements_repr(cls)
        return cls
else:  # On Python 3, these class decorators do nothing:
    implements_to_string = implements_iterator = implements_repr = nine = \
        lambda cls: cls


# http://docs.pythonsprints.com/python3_porting/py-porting.html
_moved = {  # Mapping from Python 3 to Python 2 location. May need improvement.
    'builtins': '__builtin__',
    'configparser': 'ConfigParser',
    'copyreg': 'copy_reg',
    '_markupbase': 'markupbase',
    'pickle': 'cPickle',
    'queue': 'Queue',
    'reprlib': 'repr',
    'socketserver': 'SocketServer',
    '_thread': 'thread',
    'tkinter': 'Tkinter',
    'http.client':    'httplib',
    'http.cookiejar': 'cookielib',
    'http.cookies':   'Cookie',
    'html.entities':                'htmlentitydefs',
    'html.entities:entitydefs':     'htmlentitydefs:entitydefs',
    'html.entities:name2codepoint': 'htmlentitydefs:name2codepoint',
    'html.entities:codepoint2name': 'htmlentitydefs:codepoint2name',
    'html:escape': 'cgi:escape',
    'html.parser:HTMLParser': 'htmllib:HTMLParser',
    'urllib.robotparser': 'robotparser',
    'urllib.error:ContentTooShortError': 'urllib:ContentTooShortError',
    'urllib.parse':              'urlparse',
    'urllib.parse:quote':        'urllib:quote',
    'urllib.parse:quote_plus':   'urllib:quote_plus',
    'urllib.parse:unquote':      'urllib:unquote',
    'urllib.parse:unquote_plus': 'urllib:unquote_plus',
    'urllib.parse:urlencode':    'urllib:urlencode',
    'urllib.request:getproxies':     'urllib:getproxies',
    'urllib.request:pathname2url':   'urllib:pathname2url',
    'urllib.request:url2pathname':   'urllib:url2pathname',
    'urllib.request:urlcleanup':     'urllib:urlcleanup',
    'urllib.request:urlretrieve':    'urllib:urlretrieve',
    'urllib.request:URLopener':      'urllib:URLopener',
    'urllib.request:FancyURLopener': 'urllib:FancyURLopener',
    'urllib.request:urlopen':                'urllib2:urlopen',
    'urllib.request:install_opener':         'urllib2:install_opener',
    'urllib.request:build_opener':           'urllib2:build_opener',
    'urllib.error:URLError':                 'urllib2:URLError',
    'urllib.error:HTTPError':                'urllib2:HTTPError',
    'urllib.request:Request':                'urllib2:Request',
    'urllib.request:OpenerDirector':         'urllib2:OpenerDirector',
    'urllib.request:BaseHandler':            'urllib2:BaseHandler',
    'urllib.request:HTTPDefaultErrorHandler':
    'urllib2:HTTPDefaultErrorHandler',
    'urllib.request:HTTPRedirectHandler':    'urllib2:HTTPRedirectHandler',
    'urllib.request:HTTPCookieProcessor':    'urllib2:HTTPCookieProcessor',
    'urllib.request:ProxyHandler':           'urllib2:ProxyHandler',
    'urllib.request:HTTPPasswordMgr':        'urllib2:HTTPPasswordMgr',
    'urllib.request:HTTPPasswordMgrWithDefaultRealm':
    'urllib2:HTTPPasswordMgrWithDefaultRealm',
    'urllib.request:AbstractBasicAuthHandler':
    'urllib2:AbstractBasicAuthHandler',
    'urllib.request:HTTPBasicAuthHandler':   'urllib2:HTTPBasicAuthHandler',
    'urllib.request:ProxyBasicAuthHandler':  'urllib2:ProxyBasicAuthHandler',
    'urllib.request:AbstractDigestAuthHandler':
    'urllib2:AbstractDigestAuthHandler',
    'urllib.request:HTTPDigestAuthHandler':  'urllib2:HTTPDigestAuthHandler',
    'urllib.request:ProxyDigestAuthHandler': 'urllib2:ProxyDigestAuthHandler',
    'urllib.request:HTTPHandler':            'urllib2:HTTPHandler',
    'urllib.request:HTTPSHandler':           'urllib2:HTTPSHandler',
    'urllib.request:FileHandler':            'urllib2:FileHandler',
    'urllib.request:FTPHandler':             'urllib2:FTPHandler',
    'urllib.request:CacheFTPHandler':        'urllib2:CacheFTPHandler',
    'urllib.request:UnknownHandler':         'urllib2:UnknownHandler',
}
if sys.version_info < (3, 9):
    # dummy_thread has been removed from Python 3.9
    # https://bugs.python.org/issue37312
    _moved['_dummy_thread'] = 'dummy_thread'


def nimport(spec):
    """Given a Python 3 resource spec, imports and returns it.

    Example usage::

        join = nimport('os.path:join')

    The ":" indicates "join" is a variable in the module "os.path".

    The spec should provide the **new** location of the module or variable.
    *nine* is supposed to know the corresponding, old Python 2 location.
    Bug reports and pull requests are welcome.
    """
    assert spec
    if IS_PYTHON2:  # Get the Python 2 location of the name, first.
        spec = _moved.get(spec, spec)
    alist = spec.split(':')
    if len(alist) > 2:
        raise ValueError(
            'The argument *spec* cannot have more than '
            '2 colon-separated parts: "{}"'.format(spec))
    elif len(alist) == 2:
        module, name = alist
    elif len(alist) == 1:
        module = alist[0]
        name = None
    module = import_module(module)
    return getattr(module, name) if name else module

# don't export nine.six
del sys
