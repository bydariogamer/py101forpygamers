.. _loadingimages:

Loading images
==============

Loading images to pygame is rather straightforward. The following code loads
image relative to current file from subdirectory called ``assets``. See
:ref:`paths` for more information.

.. code-block:: python

    import os
    import pygame

    pygame.init()

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_PATH, "assets/image.png")
    surface = pygame.image.load(image_path)

    fast_surface = surface.convert()
    fast_surface_per_pixel_alpha = surface.convert_alpha()

When looking above code you can notice two special surfaces ``fast_surface`` and
``fast_surface_per_pixel_alpha``.

``fast_surface`` is created by using ``convert()`` method on surface to convert
image to same pixel format as display. This guarantees fastest possible surface
for blitting. 

You can set one color as transparent. That is also called as blanket alpha. To
do that you use ``surface.set_colorkey(COLOR_HERE)``. For example 
``surface.set_colorkey((0, 255, 0))`` would set bright green as transparent color.

``fast_surface_per_pixel_alpha`` is created by using ``convert_alpha()`` method
on surface. It works similar way as ``convert()`` but additionally sets per 
pixel alpha. Per pixel alpha means then when you saved image in your image
editor tool and you saved the alpha channel with your image every pixel can
have their independent transparency (alpha) value set. This could be useful
in cases where your image has borders or holes that uses antialiasing on
transparent background or you do have images that are semi-transparent.

.. note::
    If image has alpha channel defined ``convert()`` will strip it.

    If you loaded image with alpha channel or used ``.convert_alpha()`` setting
    blanket alpha won't work.

Batch loading images
--------------------

When you do have multiple images it might come tedious to load images one by one.
To help that you can declare function that does loading for you.

The following code is just one way to do this. It's purpose is to give you 
ideas how to implement your own.

.. code-block:: python

    from pathlib import Path
    import pygame

    def load_images():
        # Make path relative to current file
        p = Path(__file__).absolute().parent.appendpath("images")
        d = {f.stem: pygame.image.load(f).convert() for f in p.glob("*.png")}
        return d

So what above code actually does?

First directory is determined being relative to Python file where function is
and appends "images" to a path and assignd it to variable ``p``. You can change
those values to come from the parameters.

Second is dict comprehension. Code generates a dictionary where image name
without extension is key and value is loaded image surface.

So when you call ``images = load_images()`` images will be a dictionary and
you can reference images like ``images["player"]``

To help you to understand above the following code would have same result:

.. code-block:: python

    images = {}
    images["player"] = pygame.image.load("images/player.png").convert()
    images["enemy1"] = pygame.image.load("images/enemy1.png").convert()
    images["enemy2"] = pygame.image.load("images/enemy2.png").convert()

.. note::
    Above code is missing proper relative path code due demonstration purposes.
