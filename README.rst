Free Python Games
=================

`Free Python Games`_ is an Apache2 licensed collection of free Python games
intended for education and fun. The games are written in simple Python code and
designed for experimentation and changes. Simplified versions of several
classic arcade games are included.

Python is one of the top-five most popular programming languages in the world
and available for free from `Python.org <https://www.python.org/>`_. Python
includes an extensive Standard Library distributed with your installation. The
Standard Library has a module called Turtle which is a popular way to introduce
programming to kids. Turtle was part of the original Logo programming language
developed by Wally Feurzig and Seymour Papert in 1966. All of the games in
`Free Python Games`_ are implemented using Python and its Turtle module.

Starting in 2012, `Free Python Games`_ began as an after school program to
teach programming to inner-city youth. The goal was to have fun as much as it
was to learn. Since then the games have been improved and used in a variety of
settings ranging from classrooms to summer day-camps.

The games run anywhere Python can be installed which includes desktop computers
running Windows, Mac OS, or Linux and older or low-power hardware such as the
Raspberry Pi. Kids across the United States in grades 6th-12th have enjoyed
learning about topics such as encryption and projectile motion through games.

Each game is entirely independent from the others and includes comments along
with a list of exercises to work through with students. Creativity and
flexibility is important. There is no right or wrong way to implement a new
feature or behavior! You never know which games students will engage with best.

.. _`Free Python Games`: http://www.grantjenks.com/docs/freegames/


Testimonials
------------

*"I love Free Python Games because the games are fun and they're easy to
understand and change. I like making my own games now."*

-- Luke Martin, Student

*"Free Python Games inspired and introduced a new hobby to our son. Thank you so
much for exposing him to coding. He is having so much fun!"*

-- Mary Lai, Parent

*"Free Python Games are great because they really engage students and let them
learn at their own pace."*

-- Rick Schertle, Teacher, Steindorf STEAM School

*"Free Python Games combines play and learning in a flexible environment that
reduces the stress of a difficult topic like programming."*

-- Brett Bymaster, Youth Pastor, The River Church Community

*"Free Python Games is great for students, is highly organized and flexible,
and seeks to unleash inquiry and understanding."*

-- Terri Furton, Principal, Downtown College Prep


Features
--------

- Fun to play!
- Simple Python code
- Easy to install
- Designed for education
- Depends only on the Python Standard Library
- Used in hundreds of hours of classroom instruction
- Fully Documented
- 100% Test Coverage
- Developed on Python 3.10
- Tested on CPython 3.6, 3.7, 3.8, 3.9, 3.10
- Tested on Linux, Mac OS X, and Windows
- Tested using GitHub Actions

.. image:: https://github.com/grantjenks/free-python-games/workflows/integration/badge.svg
   :target: http://www.grantjenks.com/docs/freegames/


Quickstart
----------

Installing Free Python Games is simple with `pip
<https://pypi.python.org/pypi/pip>`_::

  $ python3 -m pip install freegames

Free Python Games supports a command-line interface (CLI). Help for the CLI is
available using::

  $ python3 -m freegames --help

The CLI supports three commands: list, copy, and show. For a list of all games
run::

  $ python3 -m freegames list

Any of the listed games may be played by executing the Python module from the
command-line. To reference the Python module, combine "freegames" with the name
of the game. For example, to play the "snake" game run::

  $ python3 -m freegames.snake

Games can be modified by copying their source code. The copy command will
create a Python file in your local directory which you can edit. For example,
to copy and play the "snake" game run::

  $ python3 -m freegames copy snake
  $ python3 snake.py

Python includes a built-in text editor named IDLE which can also execute Python
code. To launch the editor and make changes to the "snake" game run::

  $ python3 -m idlelib.idle snake.py

You can also access documentation in the interpreter with Python's built-in
help function::

  >>> import freegames
  >>> help(freegames)


Free Games
----------

Paint
.....

`Paint`_ -- draw lines and shapes on the screen. Click to mark the start of a
shape and click again to mark its end. Different shapes and colors can be
selected using the keyboard.

.. image:: http://www.grantjenks.com/docs/freegames/_static/paint.gif
   :alt: Paint Free Python Game

.. _`Paint`: http://www.grantjenks.com/docs/freegames/paint.html

Snake
.....

`Snake`_ -- classic arcade game. Use the arrow keys to navigate and eat the
green food. Each time the food is consumed, the snake grows one segment
longer. Avoid eating yourself or going out of bounds!

.. image:: http://www.grantjenks.com/docs/freegames/_static/snake.gif
   :alt: Snake Free Python Game

.. _`Snake`: http://www.grantjenks.com/docs/freegames/snake.html

Pacman
......

`Pacman`_ -- classic arcade game. Use the arrow keys to navigate and eat all
the white food. Watch out for red ghosts that roam the maze.

.. image:: http://www.grantjenks.com/docs/freegames/_static/pacman.gif
   :alt: Pacman Free Python Game

.. _`Pacman`: http://www.grantjenks.com/docs/freegames/pacman.html

Cannon
......

`Cannon`_ -- projectile motion. Click the screen to fire your cannnonball. The
cannonball pops blue balloons in its path. Pop all the balloons before they can
cross the screen.

.. image:: http://www.grantjenks.com/docs/freegames/_static/cannon.gif
   :alt: Cannon Free Python Game

.. _`Cannon`: http://www.grantjenks.com/docs/freegames/cannon.html

Connect
.......

`Connect`_ -- Connect 4 game. Click a row to drop a disc. The first player to
connect four discs vertically, horizontally, or diagonally wins!

.. image:: http://www.grantjenks.com/docs/freegames/_static/connect.gif
   :alt: Connect 4 Free Python Game

.. _`Connect`: http://www.grantjenks.com/docs/freegames/connect.html

Flappy
......

`Flappy`_ -- Flappy-bird inspired game. Click the screen to flap your
wings. Watch out for black ravens as you fly across the screen.

.. image:: http://www.grantjenks.com/docs/freegames/_static/flappy.gif
   :alt: Flappy Bird Free Python Game

.. _`Flappy`: http://www.grantjenks.com/docs/freegames/flappy.html

Memory
......

`Memory`_ -- puzzle game of number pairs. Click a tile to reveal a
number. Match two numbers and the tiles will disappear to reveal an image.

.. image:: http://www.grantjenks.com/docs/freegames/_static/memory.gif
   :alt: Memory Free Python Game

.. _`Memory`: http://www.grantjenks.com/docs/freegames/memory.html

Pong
....

`Pong`_ -- classic arcade game. Use the keyboard to move your paddle up and
down. The first player to miss the ball loses.

.. image:: http://www.grantjenks.com/docs/freegames/_static/pong.gif
   :alt: Pong Free Python Game

.. _`Pong`: http://www.grantjenks.com/docs/freegames/pong.html

Simon Says
..........

`Simon Says`_ -- classic memory puzzle game. Click the screen to start. Watch
the pattern and then click the tiles in the same order. Each time you get the
sequence right the pattern gets one step longer.

.. image:: http://www.grantjenks.com/docs/freegames/_static/simonsays.gif
   :alt: Simon Says Free Python Game

.. _`Simon Says`: http://www.grantjenks.com/docs/freegames/simonsays.html

Tic Tac Toe
...........

`Tic Tac Toe`_ -- classic game. Click the screen to place an X or O. Connect
three in a row and you win!

.. image:: http://www.grantjenks.com/docs/freegames/_static/tictactoe.gif
   :alt: Tic Tac Toe Free Python Game

.. _`Tic Tac Toe`: http://www.grantjenks.com/docs/freegames/tictactoe.html

Tiles
.....

`Tiles`_ -- puzzle game of sliding numbers into place. Click a tile adjacent to
the empty square to swap positions. Can you make the tiles count one to fifteen
from left to right and bottom to top?

.. image:: http://www.grantjenks.com/docs/freegames/_static/tiles.gif
   :alt: Tiles Free Python Game

.. _`Tiles`: http://www.grantjenks.com/docs/freegames/tiles.html

Tron
....

`Tron`_ -- classic arcade game. Use the keyboard to change the direction of
your Tron player. Avoid touching the line drawn by your opponent.

.. image:: http://www.grantjenks.com/docs/freegames/_static/tron.gif
   :alt: Tron Free Python Game

.. _`Tron`: http://www.grantjenks.com/docs/freegames/tron.html

Life
....

`Life`_ -- Conway's Game of Life. The classic, zero-player, cellular automation
created in 1970 by John Conway.

.. image:: http://www.grantjenks.com/docs/freegames/_static/life.gif
   :alt: Game of Life Free Python Game

.. _`Life`: http://www.grantjenks.com/docs/freegames/life.html

Maze
....

`Maze`_ -- move from one side to another. Inspired by `A Universe in One Line
of Code with 10 PRINT`_. Tap the screen to trace a path from one side to
another.

.. image:: http://www.grantjenks.com/docs/freegames/_static/maze.gif
   :alt: Maze Free Python Game

.. _`Maze`: http://www.grantjenks.com/docs/freegames/maze.html
.. _`A Universe in One Line of Code with 10 PRINT`: https://www.makeartwithpython.com/blog/10-print-in-python/

Fidget
......

`Fidget`_ -- fidget spinner inspired animation. Click the screen to accelerate
the fidget spinner.

.. image:: http://www.grantjenks.com/docs/freegames/_static/fidget.gif
   :alt: Fidget Spinner Free Python Game

.. _`Fidget`: http://www.grantjenks.com/docs/freegames/fidget.html


User Guide
----------

For those wanting more details, this part of the documentation describes
curriculum, API, and development.

* `Talk: Give the Gift of Python`_
* `Free Python Games Curriculum`_
* `Free Python Games API Reference`_
* `Free Python Games Development`_

.. _`Talk: Give the Gift of Python`: http://www.grantjenks.com/docs/freegames/give-gift-python.html
.. _`Free Python Games Curriculum`: http://www.grantjenks.com/docs/freegames/curriculum.html
.. _`Free Python Games API Reference`: http://www.grantjenks.com/docs/freegames/api.html
.. _`Free Python Games Development`: http://www.grantjenks.com/docs/freegames/development.html


References
----------

* `Free Python Games Documentation`_
* `Free Python Games at PyPI`_
* `Free Python Games at GitHub`_
* `Free Python Games Issue Tracker`_

.. _`Free Python Games Documentation`: http://www.grantjenks.com/docs/freegames/
.. _`Free Python Games at PyPI`: https://pypi.python.org/pypi/freegames
.. _`Free Python Games at GitHub`: https://github.com/grantjenks/free-python-games
.. _`Free Python Games Issue Tracker`: https://github.com/grantjenks/free-python-games/issues


Free Python Games License
-------------------------

Copyright 2017-2022 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
