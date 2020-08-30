.. _nestedeventloops:

Nested event loops
==================

Nested event loops are useful if you want to delegate event handling to
separate functions or class methods.

The following is artificial example.

.. literalinclude:: sourcecode/nestedloops_wrong.py

This unfortunately doesn't work. The second loop is run after first loop has
been processed and thus it doesn't contain events from first loop. Only events
that were added to event queue after loop started are present in second loop.

So in most cases ``keyboard_handler`` function doesn't get any events.

The fix is simple:

.. literalinclude:: sourcecode/nestedloops_right.py

Change here is that before processing events you take all current events
and assign them to a variable. ``events`` in above code. Now you can pass and
iterate over that events set as many times you wish.
