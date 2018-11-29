Give the Gift of Python
=======================

*Talk given at SF Python Holiday Party on December 5, 2018.*

Who am I?
---------

1. Python programmer.
2. Hundreds of hours of classroom instruction.

What we need?
-------------

1. Interest!
2. Typing skills.
3. Math: Arithmetic, Algebra, Geometry

Quickstart
----------

1. Install Python, https://www.python.org/
2. Run IDLE, ``$ python -m idlelib.idle``
3. Write code.

Open the Turtle Window
......................

.. code-block:: python

   >>> from turtle import *
   >>> reset()

Commands
........

.. code-block:: python

   >>> forward(100)
   >>> right(90)
   >>> forward(100)
   >>> right(90)
   >>> forward(100)
   >>> right(90)
   >>> forward(100)
   >>> right(90)

Loops
.....

.. code-block:: python

   >>> reset()
   >>> for each in range(4):
           forward(100)
           right(90)

Shapes
......

.. code-block:: python

   >>> reset()
   >>> begin_fill()
   >>> for each in range(4):
           forward(100)
           right(90)
   >>> end_fill()

Dots
....

.. code-block:: python

   >>> reset()
   >>> dot(10)

Functions
.........

.. code-block:: python

   >>> def square():
           begin_fill()
           for each in range(4):
               forward(100)
               right(90)
           end_fill()
   >>> reset()
   >>> square()

Colors
......

.. code-block:: python

   >>> reset()
   >>> color('orange')
   >>> square()

Locations
.........

.. code-block:: python

   >>> reset()
   >>> up()
   >>> goto(-100, 100)
   >>> down()
   >>> square()

Inputs
......

- listen
- onclick
- onkey

Animation
.........

- ontimer
- hideturtle
- tracer
- clear
- update

.. code-block:: python

   >>> reset()
   >>> hideturtle()
   >>> tracer(False)
   >>> square()
   >>> clear()
   >>> square()
   >>> update()

Tips
----

1. help(...)
2. undo(...)
3. Embrace copy/paste
4. Close window/reset()

Activities
----------

1. Spell your name.
2. ``python -m pip install freegames``

Notes
-----

1. Start simple! Start easy! Start plain!
2. Focus on fun! No PEP8. No Pylint.
3. Make it readable! Say it aloud.
4. No special shells! No IPython.
5. Show them mistakes! Red is your favorite color!
6. No virtual environments!
7. If they're not ready, don't push them!
8. No dunder methods or attributes! No __name__ or __main__.
