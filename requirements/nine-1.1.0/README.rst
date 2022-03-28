Let's write Python 3 right now!
===============================

When the best Python 2/Python 3 compatibility modules -- especially the famous
`*six* library invented by Benjamin Peterson <https://pypi.python.org/pypi/six>`_
-- were created, they were written from the point of view of a Python 2
programmer starting to grok Python 3.  If you use *six*,
your code is compatible, but stuck in Python 2 idioms.

**nine** turns **six** upside down. You write your code using Python 3 idioms
-- as much as possible --, and it is the Python 2 "version" that is patched.
Needless to say, this approach is more future-proof.

When thou writeth Python, thou shalt write Python 3 and,
just for a little longer, ensure that the thing worketh on Python 2.7.

*nine* facilitates this point of view. You can write code
that is as 3ish as possible while still supporting 2.6.

For instance, you don't type ``unicode`` anymore, you type ``str``, and *nine*
makes ``str`` point to ``unicode`` on Python 2 (if you use our boilerplate).
Also, ``map``, ``zip`` and ``filter`` have Python 3 behaviour, on Python 2,
meaning they return iterators, not lists.

Honestly you should not spend one thought on Python 2.6 anymore, it is
`no longer supported <https://mail.python.org/pipermail/python-dev/2013-September/128287.html>`_
since its final release (2.6.9) in October 2013. Nobody uses 3.0 or 3.1 either.

Python 2.7 has finally met its demise on the first day of 2020.

*nine* is extremely stable and unlikely to change since it solves an old
problem that never changes.  Nobody should be surprised if *nine* isn't
updated for months or even years.

The author(s) of *nine* donate this module to the public domain.

To understand most of the intricacies involved in achieving 2&3 compatibility
in a single codebase, I recommend reading this:
http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/


Using nine
==========

In each of your modules, start by declaring a text encoding and
importing Python 3 behaviours from __future__.
Then import variables from *nine*, as per this boilerplate::

    # -*- coding: utf-8 -*-
    from __future__ import (absolute_import, division, print_function,
                            unicode_literals)
    from nine import (IS_PYTHON2, str, basestring, native_str, chr, long,
        integer_types, class_types, range, range_list, reraise,
        iterkeys, itervalues, iteritems, map, zip, filter, input,
        implements_iterator, implements_to_string, implements_repr, nine,
        nimport)

I know that is ugly. What did you expect? *nine* is 3 squared.
OK, in many cases you can get away with less::

    # -*- coding: utf-8 -*-

    from __future__ import (absolute_import, division, print_function,
                            unicode_literals)
    from nine import IS_PYTHON2, nimport, nine, range, str, basestring

But in the second case you need to remember to import the missing stuff when
you use it, and it is not realistic to expect that you will remember, is it?


Unicode
=======

Because of the ``unicode_literals`` import, **all string literals in the module
become unicode objects**. No need to add a "u" prefix to each string literal.
This is the saner approach since in Python 3 strings are unicode objects
by default, and you can then indicate ``b"this is a byte string literal"``.
The literals that actually need to be byte strings are very rare.
But you wouldn't believe how many developers are irrationally afraid
of taking this simple step...

If you don't know much about Unicode, just read
`The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!) <http://www.joelonsoftware.com/articles/Unicode.html>`_


Importing moved stuff
=====================

Many standard library modules were renamed in Python 3, but nine can
help. The ``nimport`` function gets the new Python 3 name, but knows to
import the old name if running in Python 2.
For instance, instead of writing this to import pickle::

    # Bad:
    try:
        import cPickle as pickle  # Python 2.x
    except ImportError:
        import pickle  # Python 3 automatically uses the C version.

...you can write this::

    # Good:
    pickle = nimport('pickle')

For variables that have been moved: In the argument, please separate the module
from the variable with a colon::

    name2codepoint = nimport('html.entities:name2codepoint')

Want StringIO? I recommend you build lists instead. But if you really need it::

    # Good:
    if IS_PYTHON2:
        from cStringIO import StringIO as BytesIO, StringIO
        NativeStringIO = BytesIO
    else:
        from io import BytesIO, StringIO
        NativeStringIO = StringIO

Our coverage of Python version differences probably isn't exhaustive,
but contributions are welcome.

When in doubt,
`use the source <https://github.com/nandoflorestan/nine/blob/master/nine/__init__.py>`_!

See the
`project page at GitHub <https://github.com/nandoflorestan/nine>`_!
We also have
`continuous integration at Travis-CI <https://travis-ci.org/nandoflorestan/nine>`_.


The *nine* class decorator
==========================

We provide a class decorator for Python 2 and 3 compatibility of magic methods.
Magic methods are those that start and end with two underlines.

You define the magic methods with their Python 3 names and,
on Python 2, they get their corresponding names. You may write:

* ``__next__()``. Use the ``next(iterator)`` function to iterate.
* ``__str__()``: must return a unicode string.  In Python 2, we implement
  ``__unicode__()`` and ``__bytes__()`` for you, based on your ``__str__()``.
* ``__repr__()``: must return a unicode string.
* ``__bytes__()``: must return a bytes object.

Example::

    @nine
    class MyClass(object):

        def __str__(self):
            return "MyClass"  # a unicode string


Porting steps
=============

When you are starting to apply *nine* on Python 2 code to achieve Python 3
compatibility, you can start by following this list of tasks. It isn't
exhaustive, just a good start. You can upgrade one ``.py`` module at a time:

* Add our header as mentioned above.
* Replace ocurrences of the print statement with the print function
  (this roughly means, add parentheses).
* Replace ``str()``, usually with nine's ``native_str()`` or with ``bytes()``.
* Replace ``unicode()`` with ``str()`` and ``from nine import str``
* Replace ``__unicode__()`` methods with ``__str__()`` methods;
  apply the ``@nine`` decorator on the class.
* Also apply the ``@nine`` decorator on classes that define ``__repr__()``.
* Search for ``range`` and replace with nine's ``range`` or ``range_list``
* Some dict methods return different things in Python 3. Only if you need
  exactly the same behavior in both versions, replace:

  * ``d.keys()`` or ``d.iterkeys()`` with nine's ``iterkeys(d)``;
  * ``d.values()`` or ``d.itervalues()`` with nine's ``itervalues(d)``; and
  * ``d.items()`` or ``d.iteritems()`` with nine's ``iteritems(d)``.

* Notice that ``map()``, ``zip()`` and ``filter()``, in nine's versions,
  always return iterators independently of Python version.

If you had been using *six* or another compatibility library before:

* Replace ``string_types`` with nine's ``basestring``

Then run your tests in all the Python versions you wish to support.

If I forgot to mention anything, could you
`make a pull request <https://github.com/nandoflorestan/nine>`_, for the
benefit of other developers?
