.. _paths:

Paths
=====

With Pygame and Python there are two concepts of paths that are in use. Working
directory and relative directory to python file. Many times both are the same
but it's not guaranteed and this is known to create issues where to place
your game assets like music and images.

Relative to working directory
-----------------------------

Working directory is the directory which you started up your python application.
It might be the same directory where your application is located or it might
be something else depending on how you started your application.

The most important thing is that your working directory is not guaranteed to
be anything specific.

If you load your assets using the following code:

.. code-block:: python

    surface = pygame.image.load("image/foo.png")

This is relative path to your working directory which might not be the same
directory where that particular python file is.

Relative to program code file
-----------------------------

Given the problematic situation with working directory Python offers way to 
use relative paths correctly.

.. code-block:: python

    import os

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_PATH, "assets/image.png")

In the above code ``BASE_PATH`` is set to a same path as your .py file is.
Python special ``__file__`` attribute is used to get the directory where .py file
is located. Since ``__file__`` can be a relative path ``os.path.abspath`` function 
converts relative path to a absolute path. ``os.path.dirname`` strips last
component from path which is filename in this case and we don't want to have
that with ``BASE_PATH``. Finally absolute base path is joined to
relative image path with ``os.path.join`` function to join paths correctly.

This now will guarantee that your image is loaded from correct path regardless
of working directory.

Pathlib
-------

Python has modern object oriented library for paths called ``pathlib``.

.. code-block:: python

    from pathlib import Path

    BASE_PATH = Path(__file__).absolute().parent
    image_path = BASE_PATH.joinpath("assets/image.png")
    image_path2 = BASE_PATH / "assets" / "image.png"

The above is equivalent to code in previous section where ``os.path`` was used.

``image_path2`` is equivalent to ``image_path`` which is using division operator
to join paths instead of ``joinpath`` method.

.. note::
    Prior Pygame 2.0.1 there was no support for Path objects. Pygame 2.0.1 has
    full support to Path objects. 
    
    To overcome this issue in older Pygame than 2.0.1 you have to cast Path to
    string: ``pygame.image.load(str(image_path))``
