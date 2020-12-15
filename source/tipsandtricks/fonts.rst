.. _fonts:

Fonts
=====

Pygame supports text rendering with TrueType fonts. 

Font rendering consists of two steps. First you need to load a font with correct
size. This is needed to be done only once per font and size combination. Note
that Pygame can't change font size dynamically. To change the font size you need
to load the font with the correct size.

.. note::
    I recommend to download a font file to your game assets and loading it from
    there. It guarantees that others will have your font as well without a need to
    install it into system fonts.

.. literalinclude:: sourcecode/fonts.py

In the example above ``sysfont`` is system font that Pygame tries to find for
you. ``custom_font`` is any TrueType font copied or downloaded from internet.

Note that font size when loading the font is given in points and not in pixels.
The following table lists some sizes. You can find similar tables from internet.

.. table::
    :align: left
    :column-dividers: none single

    ========  ======
    Points    Pixels
    ========  ======
    6pt        8px
    6.75pt     9px
    7.5pt     10px
    8.25pt    11px
    9pt       12px
    9.75pt    13px
    10.5pt    14px
    11.25pt   15px
    12pt      16px
    12.75pt   17px
    13.5pt    18px
    14.25pt   19px
    15pt      20px
    15.75pt   21px
    16.5pt    22px
    17.25pt   23px
    18pt      24px
    18.75pt   25px
    ========  ======
