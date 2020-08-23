.. _collisions:
.. index:: Collisions

Collisions
==========

Pygame, unlike game engines like Unity or Godot, doesn't have concept of game
objects. Images are handled through concept of surface, a set of pixels. To
position surfaces on screen you already have used ``Rect`` objects. Besides
ability to position objects on a screen ``Rect`` also provides methods
to check various collisions.

Here you will be presented two most common types of check for collision. A
collision between ``Rect`` and a point and collision between two ``Rect``
objects.

.. index:: Point collision

Point collision
---------------

First collision type is to check does a point collide with a rect. This is
useful when you want to check for example was mouse clicked within an 
on object on a screen. Next you will learn how to detect mouse click
within a very simple button.

Type in the following initial program and save it to the file:

.. literalinclude:: sourcecode/collision_1.py

When you run the program you see that when ever you click a mouse button color
of button changes from green to red. But color changes when clicking anywhere.
To change that so that color changes only when you click on the button you
need to do very minimal change to the code:

.. code-block:: udiff

    @@ 21 @@
         if pg.mouse.get_pressed()[0]:
    -        draw_button = pressed_button
    +        if button_rect.collidepoint(pg.mouse.get_pos()):
    +            draw_button = pressed_button

And that's it. ``collidepoint`` method on a ``Rect`` object checks if the given
point is within the rect.

.. note:: Right edge and bottom edge are not considered to be inside the rect.

The following is the full code:

.. literalinclude:: sourcecode/collision_2.py

.. index:: Rect collision

Colliding to another rect
-------------------------

Second collision type is to check does two ``Rect`` objects collide to each
other. This is very useful for all kind of checks for example to check if
player collided with an enemy.

This is the initial code. Type it in and save to a file:

.. literalinclude:: sourcecode/collision_3.py

In this example you can move around by using classical WASD-keys movement. On
screen you see two objects smaller blue rectangle at upper left corner and
big red rectangle at middle of the screen. Blue is you - the player and red is
"danger zone" which you're not supposed to move on to. Initially you can move
freely  around the screen and when you go over red area nothing happens.

Now change the program to react red area in the screen and reset player position
back to top left corner if player touches the red area. To achieve that do the
following changes to your code:

.. code-block:: udiff

    @@ 34 @@
            player_rect.left += 3
    +
    +    if player_rect.colliderect(dangerzone_rect):
    +        player_rect.topleft = (10, 10)


The ``colliderect`` method on ``Rect`` object checks if those two rects
overlap. If they do it returns ``True`` and ``False`` if they don't. This is
useful to check collisions between any objects.

.. note:: 
    
    This is very simple check and doesn't take into account shapes that
    are complex. 

The following is the full code:

.. literalinclude:: sourcecode/collision_4.py

Summary
-------

Congratulations! In this section you have learned how to detect collisions
in two ways:

 - Point within a rect
 - Rect overlapping an another rect
