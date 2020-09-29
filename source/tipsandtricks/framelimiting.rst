.. _framelimit:

Frame rate limiting
===================

Frame rate limiting or frame cap (it has many terms) means a technique to limit
rendering rate to something known. This has two advantages. It gives
computer time to process other tasks like running your operating system and you
as a programmer get a fixed period that your code runs for one single draw-cycle
on different computers.

Let's check the following code:

.. code-block:: python

    while True:
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        game_update()
        clear_screen()
        game_render()
        
        pygame.display.flip()

The above code runs as fast as it can and it can be hard to time actions so that
for example player character moves smoothly.

Pygame has a solution called ``pygame.time.Clock`` class. You can use it like the
following:

.. code-block:: python

    clock = pygame.time.Clock()

    while True:
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)  # 60 FPS
        game_update()
        clear_screen()
        game_render()
        
        pygame.display.flip()

The code above changes the working of the loop. Now every time program reaches
``clock.tick(60)`` it stops and waits until 1/60 seconds from the last call happened.
This gives a nice constant speed for your game.

However this the above code poses one problem - you need to lock your movement
to 1/60th second movements (~ 16.67 milliseconds).

There is a solution also for that. ``clock.tick(60)`` return number of milliseconds
since the last call. To get the number of seconds elapsed since the last call you just need to
divide value returned by a thousand as in the following code:

.. code-block:: python

    clock = pygame.time.Clock()

    while True:
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        dt = clock.tick(60) / 1000.0
        game_update(dt)
        clear_screen()
        game_render()
        
        pygame.display.flip()

In the above code ``dt`` is delta time, seconds since the last call to ``clock.tick(60)``.
It is very important to divide the returned value with ``1000.0`` not ``1000``.
The reason for that is that ``clock.tick(60)`` return milliseconds since last
call as an integer value. In Python dividing integer with integer results as an
integer division and in most cases ``dt`` would be zero.

Now you can pass ``dt`` to game update logic and for example do this:

.. code-block:: python

    SPEED = 5

    def game_update(dt):
        object.x += speed * dt

The above code causes speed being constant. You get easy to use 5 pixels per
second movement speed.
