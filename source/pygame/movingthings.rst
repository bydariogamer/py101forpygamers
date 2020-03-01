.. _movingthings:

Moving Things
=============

In this part of the tutorial you will learn how to move things
around the screen.

At this point you should have the basic knowledge of how to make pygame
initialization, drawing simple graphics, showing (blitting) graphics on 
the screen and running your game within a game loop. If some of those terms
are not familiar to you, please revise the :ref:`pygameintroduction`
chapter.

A new notation
--------------

Before continuing further you will be introduced a new notation
for program changes. At each step you will see a simplified diff format:

.. code:: udiff

    @@ 123 @@
     print("First row that you should find")
    -print("Remove this row from program")
     # This line is unchanged
    +if add_this_line:
    +    print("Yes")

    @@ 767 @@
     print("Second block you need to find")
    -exit()


The above is read as:

#. Number between ``@@``-markers is the line number you need to locate from
   the source code.

#. First line after ``@@``-markers is locator helper line. It must match
   it should be on a same line as you located using line number or at
   least in very close to it.

#. Read lines in the order of appearance and make a note of the character in
   the first column. Character can be one of the following: minus, plus or
   a space.

    * If line starts with minus (``-``), remove the line
    * If line starts with plus (``+``), add the rest of the line 
    * If line starts with space, skip the line
    * Skip the first character when typing the line, it's not valid Python

#. Notation may have multiple ``@@ <lineno> @@`` markers. When you encounter
   a new marker locate the line number from your file. Note that the line
   number is based on the previous removals or additions.

Don't worry if notation feels strange initially. Full code is presented after
every section to help verify that you have done modifications to correct lines
and to get working code if you didn't manage to type code correctly.


Moving object theory
--------------------

Moving an object involves few things. First and most important is to keep
track of an object position on the screen. On the every time you loop through
the game loop you draw object at the tracked position. You already did this
when making your square to jump around the screen in the introduction chapter.

When object is moved to a new location and on a next game loop drawn
an object appears in a new position. There are several ways to achieve
actual movement and you will be introduced some of them. Movement can be
also controlled by computer. For example in platformer game there are enemies,
moving platforms or elevators.

.. _userinput:

User input
----------

Very common way to move object is based on user input. Here you learn three
different types to move object. By moving object using keyboard keys using 
common method called WASD movement or cursor keys. After that you will learn
to move object to mouse click position. Finally you will learn to follow 
the mouse.


Initial program
---------------

Here is the initial program from :ref:`pygameintroduction` chapter. You will
be changing it to achieve object movement.

.. literalinclude:: sourcecode/initial.py

Make sure that you have the same file in your editor and saved the file on disk.

Moving object with keys
-----------------------

In this section you will be using Pygame to move an object, the player, by
using WASD-movement. WASD-movement is one of the classical character movements
by moving objects left, right, up and down using letters W, A, S and D as they
resemble layout of the cursor keys.

Player movement could be done by checking ``pg.KEYDOWN`` events but it has one
problem. Player would need to press a button and then release it for next key
down even to happen. To address that Pygame provides ``pg.key.get_pressed()``
function to return all pressed down keys at the specific point of time.

.. note::

    ``pg.key.get_pressed()`` must be called only after all events are handled.
    Otherwise it might return invalid results since internal state of pressed
    keys are updated only after events are handled.

Because movement is time related object is moved a certain amount of units, 
a pixels, per time unit. In this tutorial you will be using time unit of one
frame at the speed of 30 frames per second. It can be translated to object
movement number of units (pixels) per ~33.33 milliseconds.

To limit number of frames per second, also known as frame cap or frame limit,
Pygame provides ``Clock`` class for that.

Edit your file as the following:

.. code-block:: udiff

    @@ 8 @@
     rect = square.get_rect()
    +clock = pg.time.Clock()
     while True:
    +    clock.tick(30)

This change doesn't seemingly affect program anyways but it changes internal
workings quite much. ``clock.tick(30)`` causes Pygame to wait until certain
time is passed since last call to ``clock.tick()`` and then lets program to
continue.

As a remainder how to interpret that new format, here is the full 
program you should have:

.. literalinclude:: sourcecode/keyboard_1.py

Now you can add keyboard handling which is straight forward. Pressing W will
make your rectangle to go up, pressing S will make it go down, pressing 
A makes it to go left and pressing D makes it go to right. Since you already
do have ``rect`` which you can manipulate - just like you manipulated it to
jump in :ref:`pygameintroduction` chapter.

Add the following lines:

.. code-block:: udiff

    @@ 17 @@
                 rect.y = random.randrange(0, 479)
    +    pressed = pg.key.get_pressed()
    +    if pressed[pg.K_w]:
    +        rect.y -= 1
    +    if pressed[pg.K_s]:
    +        rect.y += 1
    +    if pressed[pg.K_a]:
    +        rect.x -= 1
    +    if pressed[pg.K_d]:
    +        rect.x += 1
    
``pg.key.get_pressed()`` retrieves a Python dictionary with all possible keys
and sets their value as ``True`` or ``False`` depending is key pressed or not.
Manipulation of ``rect.x`` and ``rect.y`` provides convenient way to move object
around the screen.

Save your code and run it. Try pressing keys W, A, S and D to move object
around the screen. Try also pressing space to make object jump. Does object
still move correctly?

.. note::

    This addition doesn't restrict movement within visible screen area. It is
    possible move the object out of the screen and back. It is possible to
    cause overflow with the movement. With your implementation it would take
    approximately constantly pressing the button to single direction about
    2 years and 2 months.

Here is the full program you should now have:

.. literalinclude:: sourcecode/keyboard_2.py

Moving object with mouse click
------------------------------

Moving object to location where mouse is clicked involves more variables than
moving with the keys. First, you need to track direction where movement
happens, a speed which movement happens and finally yo need to track where
your movement should stop. There are multiple ways to achieve that. This time
you will be using vectors since they simplify required math and are provided
by Pygame. Movement could be done with basic trigonometry as well.

First you need to declare variables for speed, direction and position. 
Position is good to keep in vector since it's floating point value. Rect 
handles only integers. Quantizing to int would cause problems in moving, 
including that at low speeds object might not move at all. Speed isn't 
absolutely necessary it could be hard coded but it makes code more readable.

Add the following lines:

.. code-block:: udiff

    @@ 9 @@
     clock = pg.time.Clock()
    +position_vec = pg.Vector2(rect.topleft)
    +direction_vec = None
    +target_vec = None
    +speed = 1
     
In the event loop you need to add handler for mouse click:

.. code-block:: udiff

    @@ 21 @@
                 rect.y = random.randrange(0, 479)
    +        if event.type == pg.MOUSEBUTTONDOWN:
    +            target_vec = pg.Vector2(event.pos)
    +            direction_vec = target_vec - position_vec
    +            direction_vec.normalize_ip()

When ``event.type`` is ``pg.MOUSEBUTTONDOWN`` ``event`` contains new
attributes, ``event.button`` and ``event.pos``. ``button`` contains which
button is pressed and ``pos`` contains position where mouse button was pressed
down.

First thing is to set ``target_vec`` to point where you want the object move
to. ``direction_vec`` is a bit more complex. First position vector is 
substracted from target vector. This gives a vector that points to direction
of target position. But the problem is that length of the vector is actually
distance from current position to target position. To fix that vector is
normalized, made as length of one. Now you have nice vector that is length of
one and points to direction where object needs to move to reach target.

Next thing is to add actual movement code. Add the following to your program:

.. code-block:: udiff

    @@ 34 @@
             rect.x += 1
    +    if target_vec is not None:
    +        position_vec += direction_vec * speed
    +        rect.x = int(position_vec.x)
    +        rect.y = int(position_vec.y)
    +        if position_vec.distance_squared_to(target_vec) <= speed*speed:
    +            rect.x = int(target_vec.x)
    +            rect.y = int(target_vec.y)
    +            target_vec = None

First check is if target position is set. If ``target_vec`` is set it
means that your object must still move to reach the target. If movement should
still happen a direction vector is multiplied by direction vector which and
then added to position vector. This moves position vector to correct direction
at the given speed. Finally is tested if squared distance to target is less
than speed to power of two. You could use plain ``distance_to()`` but using
it involved square root which is relatively heavy calculation. If target
was reached object is moved to final place and ``target_vec`` set to None so
no movement happens. Save the program and try it.

Try changing speed value to bigger or smaller to see how it affects movement.

Here is the full program you should now have:

.. literalinclude:: sourcecode/mouse_1.py


Following the mouse
-------------------

Following the mouse doesn't change much of your program. Instead of reacting
to ``pg.MOUSEBUTTONDOWN`` event react to ``pg.MOUSEMOTION`` event.

So change your program as the following:

.. code-block:: udiff

    @@ 21 @@
                 rect.y = random.randrange(0, 479)
    -        if event.type == pg.MOUSEBUTTONDOWN:
    +        if event.type == pg.MOUSEMOTION:

Save and run the program. Now the object follows your mouse position.

Here is the full program you should now have:

.. literalinclude:: sourcecode/mouse_2.py


Vector math illustrated
-----------------------

In the image below you see all three vectors which are involved in moving
things towards mouse click point after click event was picked but no other
processing has taken a place. But image is not the whole truth. Because
vectors only have two attributes a length and a direction. This is usually
represented with two dimensional coordinates vector points to and the other
end is placed in `(0, 0)` (origin). 

.. image:: /_static/vectormath1.svg

So from vectors point of view those three vectors looks like actually
like the following when all starting points are pulled to origin (0,0):

.. image:: /_static/vectormath2.svg

As a final step  direction vector is normalized. It means that it's length is
adjusted to be exactly one. This allows using variable speed and arbitrary
directions easily. You see how how length is adjusted in the following
illustration:

.. image:: /_static/vectormath3.svg

Here you can see progression of ``position_vec`` when it get's applied (added
by vector math ``position_vec += direction_vec * speed`` where normalized
``direction_vec`` multiplied by speed (which is one in this case)

.. image:: /_static/vectormath4.svg

Summary
-------

Congratulations! In this section you have learned how to move objects in 
three different ways:

- By using keyboard
- By using mouse click
- By following mouse position constantly
