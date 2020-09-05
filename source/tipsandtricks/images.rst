.. _loadingimages:

Loading images
==============

Loading images to pygame is rather straightforward:

The following code loads image relative to current file from subdirectory
called ``assets``:

.. code-block:: python

    import os
    import pygame

    pygame.init()

    image_path = os.path.join(os.path.dirname(__file__), "assets/image.png")
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
