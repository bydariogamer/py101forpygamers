.. _pygameintroduction:

Introduction to Pygame
======================

Now you should be comfortable with the Python and using the command-line. It
is time to start get hands dirty with the Pygame.

Creating workspace
------------------

Before you begin you should to create a workspace. Workspace means a place
where you put all files belonging to your project - in this case it's Pygame
tutorial. In the Python tutorial chapter you used your desktop as a workspace
but in the long run you don't want to put all your files on your desktop.

First you should create an umbrella directory under your home directory called
``pygame-projects``. Under that directory you will be creating other
directories (workspaces) to contain your Pygame projects, including this tutorial.

Creating workspace: Windows
---------------------------

Open up Windows Command Prompt and type:

.. code-block:: winbatch

    > cd %HomePath%
    > mkdir pygame-projects

No you created an umbrella directory. You only need to do this once.

Then you need to create the workspace for the project. You can call it
``pygame-tutorial``. Before you can do that, you need to step into
``pygame-projects`` and then you can create the workspace directory:

.. code-block:: winbatch

    > cd pygame-projects
    > mkdir pygame-tutorial

Now your directories and the workspace are ready for Pygame installation. Please,
keep your command-line open for further steps.

Pygame installation
-------------------

Time to install Pygame. In command-line you need to step into directory 
``pygame-tutorial``. If you have command-line open from previous step it is as
simple as:

.. code-block:: winbatch

    > cd pygame-tutorial

If you accidentally closed your command-line or you're returning to tutorial
you can type in the full path:

.. code-block:: winbatch

    > cd %HomePath%\pygame-projects\pygame-tutorial

Now you remember that in :ref:`firststeps` section one of the tools for
Python you installed was ``pipenv``? It is time to put it in the use.

Make sure that you are in the ``pygame-tutorial`` directory, type in the
following command:

.. code-block:: winbatch

    > pipenv install pygame==2.0.0dev6

The ``pipenv`` command does several things at once. At the first time it may
take a long time to run since it builds up some caches. So what happens when
you run the command? First pipenv creates a virtual environment. Then it
downloads and installs specific version of Pygame for you (2.0.0dev6 in this
case). As last it checks all the dependencies for Pygame and installs them
if necessary.

You should see the output similar to following:

.. code-block::

    Creating a virtualenv for this project…
    Pipfile: C:\Users\user\pygame-projects\pygame-tutorial\Pipfile
    Using c:\users\user\appdata\local\programs\python\python38\python.exe (3.8.0) to create virtualenv…
    [====] Creating virtual environment...Already using interpreter c:\users\user\appdata\local\programs\python\python38\python.exe
    Using base prefix 'c:\\users\\user\\appdata\\local\\programs\\python\\python38'
    New python executable in C:\Users\user\.virtualenvs\pygame-tutorial-5se6izmW\Scripts\python.exe
    Installing setuptools, pip, wheel...
    done.

    Successfully created virtual environment!
    Virtualenv location: C:\Users\user\.virtualenvs\pygame-tutorial-5se6izmW
    Creating a Pipfile for this project…
    Installing pygame==2.0.0dev6…
    Adding pygame to Pipfile's [packages]…
    Installation Succeeded
    Pipfile.lock not found, creating…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Success!
    Updated Pipfile.lock (14f5b3)!
    Installing dependencies from Pipfile.lock (14f5b3)…
    ================================ 1/1 - 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

Verification
------------

To verify that Pygame was installed successfully type the following:

.. code-block:: winbatch

    > pipenv run python -c "import pygame"
    pygame 2.0.0.dev6 (SDL 2.0.10, python 3.8.0)
    Hello from the pygame community. https://www.pygame.org/contribute.html

That indicates successful installation and you've verified the Pygame
installation.

.. note::

    In case of installation problems, for example if these instructions
    are outdated, please see https://www.pygame.org/wiki/GettingStarted.

Initialization and a gameloop
-----------------------------

Now open up the code editor and create a new file. Save the file as empty to
the workspace directory using name ``pygame_tutorial.py``. Make sure that
the filename ends with the ``.py`` extension.

You can verify that the file exists by typing the following:

.. code-block:: winbatch

    > dir /b

You should see output like the following:

.. code-block::

    Pipfile
    Pipfile.lock
    pygame_tutorial.py

For the Pygame to actually do anything useful you need write a few lines of code.

.. code-block:: python

    import pygame as pg

``import`` command tells Python that "find me a thing with a given name and
load it for use" (in reality it's much more complex process).

``as pg`` tells again to Python that instead of name ``pygame`` you will refer
it to as ``pg``. This saves some typing since instead of all the time writing
``pygame`` you can just need to type ``pg``.

.. note::

    Examples and source codes in the internet does Pygame import in the two 
    different ways. More common is just ``import pygame`` but that requires
    writing ``pygame`` all the time.

    In our case we want to save typing same few characters over and over again.

First thing after importing Pygame is to initialize it. As in simplest form
you can use:

.. code-block:: python

    pg.init()

That will initialize compelete Pygame as complete as possible.

As next you need to setup display. Setting up display is done by using Pygame
submodule ``display`` and it's function ``set_mode()``:

.. code-block:: python

    pg.display.set_mode([500, 500])

The first parameter for the ``set_mode()``  is a width and a height in a list.
Width and height units are pixels.

Now your file should look like this:

.. code-block:: python

    import pygame as pg
    pg.init()
    pg.display.set_mode([500, 500]

Save the file and run it:

.. code-block:: winbatch

    > pipenv run python pygame_tutorial.py
    pygame 2.0.0.dev6 (SDL 2.0.10, python 3.8.0)
    Hello from the pygame community. https://www.pygame.org/contribute.html

You might see the Pygame window popping up and then disappearing. Why is that
happening?

That happens because your code is missing the **gameloop**. A gameloop is 
a loop that runs as long as necessary to keep your game running. A minimalistic
gameloop looks like the following:

.. code-block:: python

    while True:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()

``while`` loop works almost like the ``for`` loop from the tutorial. ``while`` 
loop executes following intended lines as long as condition after ``while`` is
true. In the above code it means that ``while`` loop is run "forever".

``pg.event.poll()`` polls single event from Pygame event queue. Events and event
queue is explained later. The program stores polled event in the ``event`` variable.

Finally program checks if event type was ``pg.QUIT`` meaning that the Pygame
requests your game to stop running. You already used ``exit()`` command
to exit from Python console and the same function can be used to exit the program.

Now your file should look like the following:

.. code-block:: python

    import pygame as pg
    pg.init()
    pg.display.set_mode([500, 500]
    while True:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()

When you save the file and run it:

.. code-block:: winbatch

    > pipenv run python pygame_tutorial.py
    pygame 2.0.0.dev6 (SDL 2.0.10, python 3.8.0)
    Hello from the pygame community. https://www.pygame.org/contribute.html

You should see Pygame window appearing and staying visible. When you click 'X'
to close window application closes. Congratulations! You have done your first
Pygame application.

Events
------

In your first pygame application you polled events from event queue. Pygame has
an event queue which holds all kinds of events happening on the background. 
There are events like ``pg.QUIT`` but also events that handles keyboard, mouse,
joystick or game controller, video and few others. And there is also a way to
define user events as well.

When event happens it is actually placed in a list of events. The list, or 
actually queue, works so that when even it read, oldest one is returned to 
the event reader. New events are place at the other end of the list.

.. note::

    Event list (the queue) has maximum length. After list is full, no new
    events can be added to it.
    
    You need to make sure that you poll events fast enough not to cause event
    queue to fill up.

Events do have ``properties``. A property is readable and sometimes writable
attribute of some object. Event object has always at least one property called
``type``. In minimalistic gameloop only event type used was ``pg.QUIT``.


Common way to handle all events from the queue is to use ``for`` loop to
get events:

.. code-block::

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

As you see code is only slightly different than previous one. ``for`` loop uses
``pg.event.get()`` which returns a list of all events that has occurred since
last time ``for`` loop was executed.

How about handling a keyboard? Let's say that you want to set ``space`` key to
do jump for player. Code for that would look like the following:

.. code-block::

    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        print("Jump!")

``if`` in above code uses two ``properties``. First property is the common
``type`` and because now code tested key down event ``pg.KEYDOWN`` there exists
also second property the ``key``. The ``key`` contains integer value of key
which was pressed down. Unfortunately you don't have to remember values
because Pygame provides easily memorable ``constants``.

.. note::

    Full list of keys can be found at https://www.pygame.org/docs/ref/key.html#key-constants-label

Now the full program should look like the following:

.. code-block:: python

    import pygame as pg
    pg.init()
    pg.display.set_mode([500, 500]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print("Jump!")

Save the file and run it. Hit ``space``-key few times and you should see text
"jump" in the command-line.

.. code-block:: winbatch

    > pipenv run python pygame_tutorial.py
    pygame 2.0.0.dev6 (SDL 2.0.10, python 3.8.0)
    Hello from the pygame community. https://www.pygame.org/contribute.html
    Jump!
    Jump!

For the fun try to add other keys as well.

Summary
-------

You now have learned basics of the Pygame:

- How to install Pygame using pipenv
- How to initialize pygame with ``init()``
- Events and event queue
- How to read keypress
