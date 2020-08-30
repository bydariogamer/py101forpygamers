.. _inputbox:

Inputbox
========

Creating inputbox, a box where you can write text is relatively simple.

Just capture ``pygame.KEYDOWN`` event and it provides two handy attributes.
First one is ``event.key`` which returns which key was pressed down and second
is ``event.unicode``. ``event.unicode`` is set when value is printable unicode
charater. This provides easy way to filter visible characters and other
keys.

In the following program you can type text and remove chars with backspace.
You can print contents for text by hitting enter.

.. literalinclude:: sourcecode/inputbox.py

.. note:: 
    This program doesn't work with devices that uses on-screen keyboards
    or touch events.
