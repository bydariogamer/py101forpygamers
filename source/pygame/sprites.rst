.. _sprites:

Sprites
=======

Sprites in many 2D games are considered to be graphical objects that you can
draw on display, move and maybe check collisions with other sprites or other
background graphics or objects.

Pygame as not being game engine doesn't have true concept of sprites in that
traditional sense. Pygame though provides a few helper classes to deal with
sprites.

In this chapter you will first learn how to handle sprites without any classes.
Finally there are two ways to handle sprites, first with custom class, second
with using Pygame helper classes.

This chapter requires knowledge of Python classes and a basic knowledge
about object oriented programming. Neither of them are not covered in this
book.

`Python tutorial of classes <https://docs.python.org/3/tutorial/classes.html>`__


Sprites without classes
-----------------------

You actually did this method already in previous :ref:`movingthings` chapter.

This is the program you wrote:

.. literalinclude:: sourcecode/keyboard_2.py

Here the ``square`` represents image of the sprite and ``rect`` for it's
position. Also if you remember from :ref:`collisions` chapter the ``Rect``
objects can handle collisions for you. If these three properties are put 
together you get the sprite - an image, a position and the collision  handling.

This will work when you have only very limited number of objects to handle but
when sprite count grows this becomes hard to maintain.

Sprites with classes
--------------------

Common approach is to use classes to build sprites. So let's start with
a simple spesifications: you want to have a sprite class which can hold your
image and rect to control it's position and to help with collision detection.

The initial class definition:

.. code-block:: python

    class MySprite:
        def __init__(self, image, initial_pos):
            self.image = image
            self.rect = image.get_rect(topleft=initial_pos)

That is a very minimal implementation of the sprite with possibility to give
the sprite image and initial top left position.

Let's add two more methods to class to make class useful and reusable.
First method is ``move`` which will move sprite relatively from current
position. So for example doing ``.move(2, -2)`` would move sprite 2 pixels
right and two up. Second method to add is ``draw`` which just draws sprite
on given position on given surface - usually display surface.

The following is the full code for the class:

.. code-block:: python

    class MySprite:
        def __init__(self, image, initial_pos):
            self.image = image
            self.rect = image.get_rect(topleft=initial_pos)

        def move(self, x, y):
            self.rect.x += x
            self.rect.y += y

        def draw(self, surface):
            self.image.blit(surface, self.rect)

Since you already have a proper application where this class can be tested
with, modify it to use ``MySprite`` class instead of separate variables.

Here is the full program with the changes:

.. literalinclude:: sourcecode/sprites_1.py


Collisions
~~~~~~~~~~

How about adding collisions to sprite class? Since ``Rect`` object can detect
collisions and ``MySprite`` class has the rect it is easy to add collision
checking:

.. code-block:: python

        def collide(self, other):
            return self.rect.colliderect(other.rect)

Now put that in a use. Add a second sprite that your player character 
can try to collide with and when colliding throw it back to top left
corner of the display.

Here is the full code:

.. literalinclude:: sourcecode/sprites_2.py

Now when the white sprite which is movable collides with the green sprite it is
respawned on top left corner.


Sprites with ``pygame.sprite``
------------------------------

Pygame provides set of classes to work with sprites. You can find the
documentation here: `pygame.sprite <https://www.pygame.org/docs/ref/sprite.html>`__

This is merely example how to use ``pygame.sprite`` classes.

.. literalinclude:: sourcecode/sprites_3.py

   
Most of the code is the same as in your custom version of sprite with classes.
Major difference is the declaration of the ``MySprite`` class and it's 
``__init__`` method. In pygame sprite you have to remember to call parent
class ``__init__`` before anything else. That is achieved by using 
``super().__init__()`` call as a first line in your own sprite ``__init__``
method.

Movement of player is done modifying player sprite directly. It could be done
also via group methods but it would be quite complex.

You may notice also collision detection has been changed. Pygame sprite module
has function ``groupcollide(groupa, groupb, killa, killb)``. This does two
things. First function checks if sprite collisions between sprites in 
``groupa`` and ``groupb``. Then if ``killa`` is ``True`` all colliding sprites
from ``groupa`` are removed. If ``killb`` is ``True`` all colliding sprites
from ``groupb`` are removed. Try it out and modify collision so that ``killb``
value is set ``True``.


Summary
-------

Congratulations! In this section you have learned how to use sprites in
Pygame:

- Without classes using variables
- With own custom class
- With Pygame own sprites
