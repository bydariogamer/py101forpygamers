Introduction to Python
======================

Now it's time to write some code!

This part is based on `Django Girls Tutorial <https://tutorial.djangogirls.org/en/python_introduction/>`_

Python prompt
-------------

To start playing with Python you need to open up a *command-line* on your
computer. You should already know how to do that - you learned that in the
:ref:`Introduction to command-line` chapter.

Once you're ready follow the instructions below.

You need to open up a Python console, so type in ``python`` in command-line and
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

Strings can be joined together. Try this:

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

You might wonder why you used dot (``.``) when you called ``upper()`` on
your name. When you use dot like in ``"Jani".upper()"`` you called a **method**.

A method is a is a sequence of instructions that Python has to execute on a
given object (``"Jani"``) when you call it. Methods always do belong to objects.
In this case object is a string. String has also other methods like ``lower()``
and ``title()``. You can try them out.

If you want to know the number of letters contained in your name, there is a
**function** for that.

.. code-block:: python

    >>> len("Jani")
    4

Now you put string within parenthesis without dot. That is called a **function**.

Functions are, like methods, sequence of instructions but they don't
belong to any specific object. 

You will learn to write your own functions at the end of this tutorial.

Summary
-------

So far you have learned following:

* the prompt - you know how to open Python prompt and type simple commands
* numbers and strings - numbers for math and strings for text objects
* operators - like + and * to combine values to produce new values
* methods and functions - to perform actions on objects

Now you know very basics of Python and probably want to learn more. Read on!

Errors
------

Now how about trying to find out length of number same ways as you did with
your name:

.. code-block:: python

    >>> len(37337)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

You got your first error! Making mistakes (even intentional ones like you did
here) is important part of learning process. It is also very important to be
able to read and interpret errors so you can fix your programs. Actual error
message is most of the time readable, plain text and tells quite well what 
is wrong.

In this case error says that objects type "int" (integers,
whole numbers) have no length. So how would you fix that? In previous part you
learned that strings do have length since you could ask length of your name.

Try following:

.. code-block:: python

    >>> len(str(37337))
    5

It works. So you called ``str`` function within ``len`` function. ``str()`` is
very useful function which converts many objects to a string representation.

You can also convert numeric strings to integers with ``int()`` function. Try
it out:

.. code-block:: python

    >>> int("37337")
    37337

What would happen if you do ``int`` for your name? Right, you get an error.

* The ``str`` function converts things into **strings**
* The ``int`` function converts things into **integers**

Variables
---------

An important concept in programming is variables. A variable is nothing more 
than a name for something so you can use it later. Programmers use these 
variables to store data, make their code more readable and so they don't have
to keep remembering what things are.

Let's say you want to create a new variable called ``name``:

.. code-block:: python

    >>> name = "Jani"

You type name equals Jani.

As you've noticed, your program didn't return anything like it did before.
So how do you know that the variable actually exists? Enter ``name`` and 
hit ``enter``:

.. code-block:: python

    >>> name
    'Jani'

Yippee! Your first variable! :) You can always change what it refers to:

.. code-block:: python
    
    >>> name = "Marci"
    >>> name
    'Marci'

You can use it in functions too:

.. code-block:: python

    >>> len(name)
    5

Awesome, right? Now, variables can be anything – numbers too! Try this:

.. code-block:: python

    >>> a = 4
    >>> b = 6
    >>> a * b
    24

But what if you used the wrong name? Can you guess what would happen? Let's try!

.. code-block:: python

    >>> city = "Joensuu"
    >>> ctiy
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ctiy' is not defined

An error! As you can see, Python has different types of errors and this one is
called a **NameError**. Python will give you this error if you try to use 
a variable that hasn't been defined yet. If you encounter this error later, 
check your code to see if you've mistyped any variable names.

Play with this for a while and see what you can do!

The print function
------------------

Try this:

.. code-block:: python

    >>> name = 'Maria'
    >>> name
    'Maria'
    >>> print(name)
    Maria

When you just type ``name``, the Python interpreter responds with the string
*representation* of the variable 'name', which is the letters M-a-r-i-a, 
surrounded by single quotes, ''. When you say ``print(name)``, Python will 
"print" the contents of the variable to the screen, without the quotes,
which is neater.

As you'll see later, ``print()`` is also useful when you want to print things
from inside functions, or when you want to print things on multiple lines.

Lists
-----

Beside strings and integers, Python has all sorts of different types of
objects. Now you're going to be introduced one called **list**. Lists are
exactly what you think they are: objects which are lists of other objects.

Go ahead and create a list:

.. code-block:: python
    
    >>> []
    []

Yes, this list is empty. Not very useful, right? Let's create a list of 
lottery numbers. You don't want to repeat yourself all the time, so you 
will put it in a variable, too:

.. code-block:: python

    >>> lottery = [3, 42, 12, 19, 30, 59]

All right, you have a list! What can you do with it? Let's see how many lottery
numbers there are in a list. Do you have any idea which function you should
use for that? You know this already!

.. code-block:: python

    >>> len(lottery)
    6

Yes! ``len()`` can give you a number of objects in a list. Handy, right? 
Maybe you will sort the list now:

.. code-block:: python

    >>> lottery.sort()

This doesn't return anything, it just changed the order in which the numbers
appear in the list. Let's print it out again and see what happened:

.. code-block:: python

    >>> print(lottery)
    [3, 12, 19, 30, 42, 59]

As you can see, the numbers in your list are now sorted from the lowest to
highest value. Congrats!

Maybe you want to reverse that order? Do that!

.. code-block:: python

    >>> lottery.reverse()
    >>> print(lottery)
    [59, 42, 30, 19, 12, 3]

If you want to add something to your list, you can do this by typing 
following command:

.. code-block:: python

>>> lottery.append(199)
>>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]

If you want to show only the first number, you can do this by using **indexes**.
An index is the number that says where in a list an item occurs. Programmers 
prefer to start counting at 0, so the first object in your list is at index 0, 
the next one is at 1, and so on. Try this:

.. code-block:: python
    >>> print(lottery[0])
    59
    >>> print(lottery[1])
    42

As you can see, you can access different objects in your list by using the 
list's name and the object's index inside of square brackets (``[]``).

To delete something from your list you will need to use **indexes** as you
learned above and the ``pop()`` method. Try an example and reinforce what you
learned previously; you will be deleting the first number of your list.

.. code-block:: python

    >>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]
    >>> print(lottery[0])
    59
    >>> lottery.pop(0)
    59
    >>> print(lottery)
    [42, 30, 19, 12, 3, 199]

That worked like a charm!

For extra fun, try some other indexes: 6, 7, 1000, -1, -6 or -1000. See if you
can predict the result before trying the command. Do the results make sense?

You can find a list of all available list methods in this chapter of the
Python documentation: https://docs.python.org/3/tutorial/datastructures.html

Dictionaries
------------

A dictionary is similar to a list, but you access values by looking up a key
instead of a numeric index. A key can be any string or number. The syntax to
define an empty dictionary is:

.. code-block:: python
    >>> {}
    {}

This shows that you just created an empty dictionary. Hurray!

Now, try writing the following command (try substituting your own information,
too):

.. code-block:: python

    >>> participant = {'name': 'Jani', 'country': 'Finland', 'favorite_numbers': [7, 42, 92]}

With this command, you just created a variable named ``participant`` with three
key–value pairs:

- The key ``name`` points to the value ``'Jani'`` (a ``string`` object),
- ``country`` points to ``'Finland'`` (another ``string``),
- and ``favorite_numbers`` points to ``[7, 42, 92]`` (a ``list`` with three numbers in it).

You can check the content of individual keys with following syntax:

.. code-block:: python

    >>> print(participant['name'])
    Jani

See, it's similar to a list. But you don't need to remember the index – just
the name of the key.

What happens if you ask Python the value of a key that doesn't exist? Can you
guess? Let's try it and see!

.. code-block:: python

    >>> participant['age']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'age'

Look, another error! This one is a **KeyError**. Python is helpful and tells
you that the key ``'age'`` doesn't exist in this dictionary.

When should you use a dictionary or a list? Well, that's a good point to
ponder. Think about the answer before looking at it in the next line.

- Do you just need an ordered sequence of items? Go for a list.
- Do you need to associate values with keys, so you can look them up
  efficiently (by key) later on? Use a dictionary.

Dictionaries, like lists, are *mutable*, meaning that they can be changed
after they are created. You can add new key–value pairs to a dictionary after
it is created, like this:

.. code-block:: python

    >>> participant['favorite_language'] = 'Python'

Like lists, using the ``len()`` method on the dictionaries returns the number of
key–value pairs in the dictionary. Go ahead and type in this command:

.. code-block:: python

    >>> len(participant)
    4

Hope it makes sense up to now. :) Ready for some more fun with dictionaries?
Read on for some amazing things.

You can use the ``pop()`` method to delete an item in the dictionary. Say, if
you want to delete the entry corresponding to the key ``'favorite_numbers'``,
type in the following command:

.. code-block:: python

    >>> participant.pop('favorite_numbers')
    [7, 42, 92]
    >>> participant
    {'country': 'Finland', 'favorite_language': 'Python', 'name': 'Jani'}

As you can see from the output, the key–value pair corresponding to the
'favorite_numbers' key has been deleted.

As well as this, you can also change a value associated with an already-created
key in the dictionary. Type this:

.. code-block:: python

    >>> participant['country'] = 'Germany'
    >>> participant
    {'country': 'Germany', 'favorite_language': 'Python', 'name': 'Jani'}

As you can see, the value of the key `'country'` has been altered from 
``'Finland'`` to `'Germany'`. :) Exciting? Hurrah! You just learned another
amazing thing.

Summary
-------

Awesome! You know a lot about programming now. In this last part you learned
about:

- **errors** – you now know how to read and understand errors that show up if
  Python doesn't understand a command you've given it.
- **variables** – names for objects that allow you to code more easily and 
  to make your code more readable.
- **lists** – lists of objects stored in a particular order.
- **dictionaries** – objects stored as key–value pairs.

Excited for the next part? :)

Comparing things
----------------

A big part of programming involves comparing things. What's the easiest thing
to compare? Numbers! Let's see how that works:

.. code-block:: python
    
    >>> 5 > 2
    True
    >>> 3 < 1
    False
    >>> 5 > 2 * 2
    True
    >>> 1 == 1
    True
    >>> 5 != 2
    True
    >>> len("Jani") == len("Marci")
    False

You gave Python some numbers to compare. As you can see, not only can Python
compare numbers, but it can also compare method results. Nice, huh?

You may wonder why you have put two equal signs ``==`` next to each other to
compare if numbers are equal? You use a single ``=`` for assigning values
to variables. You always, **always** need to put two of them – ``==`` – if you
want to check if things are equal to each other. It can be also stated that
things are unequal to each other. For that, you use the symbol ``!=``, as
shown in the example above.

Give Python two more tasks:

.. code-block:: python

    >>> 6 >= 12 / 2
    True
    >>> 3 <= 2
    False

You've seen ``>`` and ``<``, but what do ``>=`` and ``<=`` mean? Read them
like this (just like in normal mathematics):

- x ``>`` y means: x is greater than y
- x ``<`` y means: x is less than y
- x ``<=`` y means: x is less than or equal to y
- x ``>=`` y means: x is greater than or equal to y

Awesome! Wanna do one more? Try this:

.. code-block:: python

    >>> 6 > 2 and 2 < 3
    True
    >>> 3 > 2 and 2 < 1
    False
    >>> 3 > 2 or 2 < 1
    True

You can give Python as many numbers to compare as you want, and it will give
you an answer! Pretty smart, right?

- **and** – if you use the ``and`` operator, both comparisons have to be True
  in order for the whole command to be True.
- **or** – if you use the ``or`` operator, only one of the comparisons has to
  be True in order for the whole command to be True.

Have you heard of the expression "comparing apples to oranges"? Let's try the
Python equivalent of that expression:

.. code-block:: python

    >>> 1 > 'Jani'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: '>' not supported between instances of 'int' and 'str'

Here you see that just like in the expression, Python is not able to compare
a number (``int``) and a string (``str``).
Instead, it shows a **TypeError** and tells to you  the two types can't be
compared together.

Boolean
-------

Incidentally, you just learned about a new type of object in Python. 
It's called **Boolean**.

There are only two Boolean objects:
- True
- False

But for Python to understand this, you need to always write it as 'True' 
(first letter uppercase, with the rest of the letters lowercased). **true,**
**TRUE, and tRUE won't work – only True is correct.** (The same applies to
'False' as well.)

Booleans can be variables, too! See here:

.. code-block:: python

    >>> a = True
    >>> a
    True

You can also do it this way:

.. code-block:: python

    >>> a = 2 > 5
    >>> a
    False

Practice and have fun with Booleans by trying to run the following commands:

- ``True and True``
- ``False and True``
- ``True or 1 == 1``
- ``1 != 2``

Congrats! Booleans are one of the coolest features in programming, and you
just learned how to use them!

Save it!
--------

So far you've been writing all your python code in the interpreter, which
limits you to entering one line of code at a time. Normal programs are saved
in files and executed by programming language **interpreter** or **compiler**.
So far you've been running your programs one line at a time in the
Python **interpreter**. You're going to need more than one line of code
for the next few tasks, so you'll quickly need to:

- Exit the Python interpreter
- Open up your code editor of choice
- Save some code into a new python file
- Run it!

To exit from the Python interpreter that you've been using, type the ``exit()``
function.

.. code-block:: python

    >>> exit()
    $

This will put you back into the command prompt.

Earlier, you picked out a code editor from the :ref:`code-editor` section.
You'll need to open the editor now and write some code into a new file:

.. code-block:: python
    
    print('Hello, PyGamers!')

Obviously, you're a pretty seasoned Python developer now, so feel free to
write some code that you've learned today.

Now you need to save the file and give it a descriptive name. Let's call the
file **python_intro.py** and save it to your desktop. You can name the file
anything you want, but the important part here is to make sure the file
ends in **.py**. The **.py** extension tells your operating system that this
is a **Python executable file** and Python can run it.

.. note:: 

    You should notice one of the coolest thing about code editors: colors! 
    In the Python console, everything was the same color; now you should 
    see that the `print` function is a different color from the string.
    This is called "syntax highlighting", and it's a really useful feature
    when coding. The color of things will give you hints, such as unclosed
    strings or a typo in a keyword name (like the `def` in a function,
    which youe'll see below).
    
    This is one of the reasons for you use a code editor. :)

With the file saved, it's time to run it! Using the skills you've learned
in the command line section, use the terminal to **change directories** to
the desktop.

Changing directory: Windows
---------------------------

On Windows Command Prompt, it will be like this:

.. code-block:: winbatch

    > cd %HomePath%\Desktop

And on Windows Powershell, it will be like this:

.. code-block:: Powershell

    > cd $Home\Desktop


If you get stuck, ask for help.

Now use Python to execute the code in the file like this:

.. code-block::

    > python python_intro.py
    Hello, PyGamers!

.. note::
    On other platforms than Windows 'python' might refer to Python 2 rather
    than Python 3. You can check it easily with ``python --version`` command. 
    Instead, use you might need to use 'python3' to execute the file:

    .. code-block::
        
        $ python python_intro.py

Alright! You just ran your first Python program that was saved to a file.
Feel awesome?

You can now move on to an essential tool in programming:

If … elif … else
----------------

Lots of things in code should be executed only when given conditions are met.
That's why Python has language construct called **if statements**.

Replace the code in your **python_intro.py** file with this:

.. code-block::

    if 3 > 2:

If you were to save and run this, you'd see an error like this:

.. code-block:: python

    $ python3 python_intro.py
    File ".\python_intro.py", line 2
               ^
    SyntaxError: unexpected EOF while parsing

Python expects you to give further instructions to it which are executed if the
condition ``3 > 2`` turns out to be true (or ``True`` for that matter).
Try to make Python print “It works!”. Change your code in your 
**python_intro.py** file to this:

.. code-block:: python

    if 3 > 2:
        print('It works!')

Notice how second line of code is indented by 4 spaces? You need to do this
so Python knows what code to run if the result is true. You can do one
space, but nearly all Python programmers do 4 to make things look neat.
A single Tab will also count as 4 spaces as long as your text editor is
set to do so. When you made your choice, don't change it! If you already
indented with 4 spaces, make any future indentation with 4 spaces,
too - otherwise you may run into problems.

.. note::

    Many other programming languages uses some kind of block-characters.
    Most common block characters are curly braces (``{}``). For example:

    .. code-block:: c

        if (3 > 2) {
            print("It works!");
        }

    In those languages indentation doesn't matter at all.

Save the file and give it another run:

.. code-block::

    $ python python_intro.py
    It works!

What if a condition isn't True?
-------------------------------

In previous examples, code was executed only when the conditions were True.
But Python also has ``elif`` and ``else`` statements:

.. code-block:: python

    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')

When the file is saved and you runt the file this is run it will print out:

.. code-block::

    $ python python_intro.py
    5 is indeed greater than 2

Try now to change comparison to something that is not true, for example
``5 > 10`` (You might want to change number 2 to 10 as well). Save the file
and run the file again. You should see message from the ``else`` part.

Now let's see how `elif` works:

.. code-block:: python

    name = 'Marci'
    if name == 'Jani':
        print('Hey Jani!')
    elif name == 'Marci':
        print('Hey Marci!')
    else:
        print('Hey anonymous!')

and executed:

.. code-block:: python

    $ python3 python_intro.py
    Hey Marci!

See what happened there? ``elif`` lets you add extra conditions that run
if the previous conditions fail. Now try changing ``name`` contents, save
the file and run it. Observe how responses do change if you use values like
'Jani' or your own name.

You can add as many ``elif`` statements as you like after your initial ``if``
statement. For example:

.. code-block:: python

    volume = 57
    if volume < 20:
        print("It's kinda quiet.")
    elif 20 <= volume < 40:
        print("It's nice for background music")
    elif 40 <= volume < 60:
        print("Perfect, I can hear all the details")
    elif 60 <= volume < 80:
        print("Nice for parties")
    elif 80 <= volume < 100:
        print("A bit loud!")
    else:
        print("My ears are hurting! :(")

Python runs through each test in sequence and prints:

.. code-block::

    $ python python_intro.py
    Perfect, I can hear all the details

Comments
--------

Comments are lines beginning with ``#``. You can write whatever you want after
the ``#`` and Python will ignore it. Comments can make your code easier for
other people to understand.

Let's see how that looks:

.. code-block:: python

    # Change the volume if it's too loud or too quiet
    if volume < 20 or volume > 80:
        volume = 50
        print("That's better!")

You don't need to write a comment for every line of code, but they are useful
for explaining why your code is doing something, or providing a summary when
it's doing something complex.

Summary
-------

In the last few exercises you learned about:

- **comparing things** – in Python you can compare things by using ``>``, ``>=``,
  ``==``, ``<=``, ``<`` and the ``and``, ``or`` operators.
- **Boolean** – a type of object that can only have one of two values:
  ``True`` or ``False``.
- **Saving files** – storing code in files so you can execute larger programs.
- **if … elif … else** – statements that allow you to execute code only when
  certain conditions are met.
- **comments** - lines that Python won't run which let you document your code.

Time for the last part of this chapter!

Your own functions!
-------------------

Remember functions like ``len()`` that you can execute in Python? Well,
good news – you will learn how to write your own functions now!

A function is a sequence of instructions that Python should execute. Each
function in Python starts with the keyword ``def``, is given a name, and can
have some parameters. Let's give it a go.
Replace the code in **python_intro.py** with the following:

.. code-block:: python

    def hi():
        print('Hi there!')
        print('How are you?')

    hi()

Okay, your first function is ready!

You may wonder why there is the name of the function at the bottom of the file.
This is because Python reads the file and executes it from top to bottom.
So in order to use your function, you have to re-write it at the bottom.

Let's run this now and see what happens:

.. code-block::

    $ python3 python_intro.py
    Hi there!
    How are you?

.. note:: 
    If it didn't work, don't panic! The output will help you to figure why:

    - If you get a ``NameError``, that probably means you typed something
      wrong, so you should check that you used the same name when creating the
      function with ``def hi():`` and when calling it with ``hi()``.
    - If you get an ``IndentationError``, check that both of the ``print`` lines
      have the same whitespace at the start of a line: python wants all the
      code inside the function to be neatly aligned.
    - If there's no output at all, check that the last ``hi()`` *isn't* indented
      - if it is, that line will become part of the function too, and it will
      never get run.

Let's build your first function with parameters. You need change the previous
example – a function that says 'hi' to the person running it – with a name:

.. code-block:: python
    
    def hi(name):

As you can see, you now gave your function a parameter that is called ``name``:

.. code-block:: python

    def hi(name):
        if name == 'Jani':
            print('Hi Jani!')
        elif name == 'Marci':
            print('Hi Marci!')
        else:
            print('Hi anonymous!')

    hi()

Remember: The ``print`` function is indented four spaces within the ``if``
statement. This is because the function runs when the condition is met.
Let's see how it works now:

.. code-block::

    $ python python_intro.py
    Traceback (most recent call last):
    File ".\python_intro.py", line 9, in <module>
        hi()
    TypeError: hi() missing 1 required positional argument: 'name'

Oops, an error. Luckily, Python gives you a pretty useful error message.
It tells to you that the function ``hi()`` (the one you defined) has one 
required argument (called ``name``) and that you forgot to pass it when calling
the function. Fix it at the bottom of the file:

.. code-block:: python

    hi("Jani")

And run it again:

.. code-block::

    $ python python_intro.py
    Hi Jani!

And if you change the name?

.. code-block:: python

    hi("Marci")

And run it:

.. code-block::

    $ python3 python_intro.py
    Hi Marci!

Now, what do you think will happen if you write another name in there? (Not 
Jani or Marci.) Give it a try and see if you're right. It should print out this:

.. code-block::

    Hi anonymous!

This is awesome, right? This way you don't have to repeat yourself every time
you want to change the name of the person the function is supposed to greet.
And that's exactly why you need functions – you never want to repeat your code!

Time to do something smarter – there are more names than two, and writing
a condition for each would be hard, right? Replace the content of your file
with the following:

.. code-block:: python

    def hi(name):
        print('Hi ' + name + '!')

    hi("Rachel")

Let's run the program now:

.. code-block::

    $ python python_intro.py
    Hi Rachel!

Congratulations! You just learned how to write functions! :)

Loops
-----

This is the last part already. That was quick, right? :)

Programmers don't like to repeat themselves. Programming is all about
automating things, so you don't want to greet every person by their name
manually, right? That's where loops come in handy.

Still remember lists? Let's add a list of persons.

.. code-block:: python

    persons = ['Marci', 'Jani', 'Rachel', 'Phoebe', 'You']

You want to greet all of them by their name. For that you have written 
the ``hi`` function already to do that, so you can use it in a loop:

.. code-block:: python

    for name in persons:

The ``for`` statement behaves similarly to the ``if`` statement; code below
both of these need to be indented four spaces.

Here is the full code that will be in the file:

.. code-block:: python

    def hi(name):
        print('Hi ' + name + '!')

    persons = ['Marci', 'Jani', 'Rachel', 'Phoebe', 'You']
    for name in persons:
        hi(name)
        print('Next person')

And when you run it:

.. code-block::

    $ python python_intro.py
    Hi Marci!
    Next person
    Hi Jani!
    Next person
    Hi Rachel!
    Next person
    Hi Phoebe!
    Next person
    Hi You!
    Next person

As you can see, everything you put inside a ``for`` statement with an indent
will be repeated for every element of the list ``persons``.

When ``for`` loops over ``persons`` it picks item from the list one by one
and assigns picked item to variable ``name`` and then runs indented lines.

.. note::
    Sometimes you might see term *iterating* being used. It means the same
    thing: looping over list of items just like you did with ``persons``.

You can also use ``for`` on numbers using the ``range`` function:

.. code-block:: python

    for i in range(1, 6):
        print(i)

Which would print:

.. code-block::

    1
    2
    3
    4
    5

``range`` is a function that creates a list of numbers following one after
the other (these numbers are provided by you as parameters).

Note that the second of these two numbers is not included in the list that
is output by Python (meaning ``range(1, 6)`` counts from 1 to 5, but does not
include the number 6). That is because "range" is half-open, and that means it
includes the first value, but not the last.

Summary
-------

That's it. **You totally rock!** This was a tricky chapter, so you should feel
proud of yourself. 

I'm as an author of this definitely proud of you for making it this far!

For official and full python tutorial visit https://docs.python.org/3/tutorial/.
This will give you a more thorough and complete study of the language.

Now you're ready to start tackle PyGame itself.
