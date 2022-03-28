# -*- coding: utf-8 -*-

'''*nine* is about Python 2 and 3 compatibility, but I have taken the
liberty of including something else in it. The *reify* decorator is
so useful that it should come with Python, in the standard library.
While it doesn't, the next best thing is for it to be included in a
"base" package. And *nine* is a base package!

The *reify* decorator comes from Pyramid_ source code. This is fair use
because it is only one function out of hundreds.

.. _Pyramid: https://pypi.python.org/pypi/pyramid
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


class reify(object):
    """ Use as a class method decorator.  It operates almost exactly like the
    Python ``@property`` decorator, but it puts the result of the method it
    decorates into the instance dict after the first call, effectively
    replacing the function it decorates with an instance variable.  It is, in
    Python parlance, a non-data descriptor.  An example:

    .. code-block:: python

       class Foo(object):
           @reify
           def jammy(self):
               print 'jammy called'
               return 1

    And usage of Foo:

    .. code-block:: text

       >>> f = Foo()
       >>> v = f.jammy
       'jammy called'
       >>> print v
       1
       >>> f.jammy
       1
       >>> # jammy func not called the second time; it replaced itself with 1
    """

    def __init__(self, wrapped):
        self.wrapped = wrapped
        try:
            self.__doc__ = wrapped.__doc__
        except:  # pragma: no cover
            pass

    def __get__(self, inst, objtype=None):
        if inst is None:
            return self
        val = self.wrapped(inst)
        setattr(inst, self.wrapped.__name__, val)
        return val
