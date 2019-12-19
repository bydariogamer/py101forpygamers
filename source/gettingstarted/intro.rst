Introduction to Python
======================

Now it's time to write some code!

Python prompt
-------------

To start playing with Python you need to open up a *command-line* on your
computer. You should already know how to do that - you learned that in the
:ref:`Introduction to command-line` chapter.

Once you're ready follow the instructions below.

We want to open up a Python console, so type in ``python`` in command-line and
hit ``enter``

.. code-block::

    $ python
    Python 3.8.0 (...)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>                                                                              

Your very first Python command
------------------------------

After running the Python command, the prompt changed to ``>>>``. For you it
means that Python is ready for accepting Python language. You don't need to
type ``>>>`` in - Python will do that for you automatically.

If you want to exit Python console at any point, type ``exit()`` or use 
shortcut ``Ctrl + Z``. Then you won't see ``>>>`` any longer.

For now stay in Python console so you can learn more about it. Start by typing 
in some math, like ``1 + 2`` and hitting ``enter``.

.. code-block:: python
    
    >>> 1 + 2
    3

Nice. Python knows math! You can try some others as well:

* ``2 * 5``
* ``5 - 1``
* ``11 / 2``

Strings
-------

How about your name? Type your first name in quotes like this:

.. code-block:: python

    >>> "Jani"
    'Jani'

You have now created your first string. String is a sequence of characters
that can be processed by a computer. The string must begin and end with the
same character. This can be double (``"``) or single (``'``) quotes (there is
no difference). The quotes tell Python that what's inside quotes is a string.

Strings can be joined to gether. Try this:

.. code-block:: python

    >>> "Hi there " + "Jani"
    'Hi there Jani'

You can also multiply strings with a number:

.. code-block:: python
    
    >>> "Jani" * 3
    'JaniJaniJani'

Quotes and apostrophes
----------------------

If you need to put quote or apostrophe in your text
there are two ways to do that. Recommended way is as follows. Since Python
strings can be defined with either of quotes use other as string marker than
what you need to put in a string:

.. code-block:: python

    >>> "Ain't this cool?"
    "Ain't this cool?"
    
    >>> 'Word "magic"'
    'Word "Magic"'

Second way is to use escape character, which is backslash (``\``) in Python.

.. code-block:: python

    >>> 'Ain\'t this cool?'
    "Ain't this cool?"

    >>> "Word \"magic\""
    'Word "magic"'

How about making your name to uppercase?

.. code-block:: python

    >>> "Jani".upper()
    'JANI'

Now, what happened here? You used ``upper`` **method** on a string. A method
is a sequence of instructions that Python has to perform on a given object
(``"Jani"``) once you call it.

You might wonder why you used dot (``.``) when you called ``upper()`` on
your name. When you use dot like in ``"Jani".upper()"`` you called **method**. 

Method is a function that belongs to object. In this case object is a string.
String has also other methods like ``lower()`` and ``title()``.

If you want to know the number of letters contained in your name, there is a
**function** for that.

.. code-block:: python

    >>> len("Jani")
    4

Now you put string within parenthesis without dot. That is called **function**.
Functions don't belong to any object but they're standalone and doesn't require
any object to be used.

Recap
-----

So far you have learned following:

* the prompt - you know how to open Python prompt and type simple commands
* numbers and strings - numbers for math and strings for text objects
* operators - like + and * to combine values to produce new values
* methods and functions - to perform actions on objects

Now you know very basics of Python and probably want to learn more. Read on!
