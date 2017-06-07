Free Python Games
=================

A collection (18) of free python games.

In the first half of 2012, I wrote ten games to teach a group of students some basics of programming. The goal was to have fun as much as it was to learn. Here you'll find simplified versions of several classics.

In 2013, I used these games again as part of a programming club for high school students at Downtown College Prep in San Jose, CA. At that time, I added a number of new games bringing the total up to eighteen and covering more advanced topics like projectile motion and encryption.

In 2014, I used these games as part of week-long programming club that met in the evenings at The River Church Community in San Jose, CA. Our demographic was middle and high school students.

Each game is entirely independent from the others and includes comments along with a list of exercises to work through with students. Creativity and flexibility is important. There's no right or wrong way to implement a new feature! You never know which games the students will find really interesting.

Screenshots
-----------

Nibbles
.......

Nibbles -- like Snake on the old Nokia phones.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/nibbles.png?raw=true
   :alt: Nibbles Free Computer Game

Memory
......

Memory -- match tile pairs of numbers to uncover the hidden image.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/memory.png?raw=true
   :alt: Memory Free Computer Game

Tiles
.....

Tiles -- shuffle image tiles to solve the puzzle.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/tiles.png?raw=true
   :alt: Tiles Free Computer Game

Pacman
......

Pacman -- simplified version of the classic.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/pacman.png?raw=true
   :alt: Pacman Free Computer Game

Maze
....

Maze -- solve a randomly generated maze.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/maze.png?raw=true
   :alt: Maze Free Computer Game

Tic Tac Toe
...........

Tic Tac Toe -- the classic.

.. image:: https://github.com/grantjenks/free_python_games/blob/master/screenshots/tictactoe.png?raw=true
   :alt: Tic Tac Toe Free Computer Game

Requirements
------------

These games were tested on a Win32 system running Python 2.7 with pygame installed.

Most games should work for Linux-type systems. Where needed (e.g. hangman.py), I tried to make the code cross-platform compatible.

For Python 3 compatibility, you'll need to run the 2to3 tool, change division (/) to integer division (//), and convert return values of filter(..), map(..), etc. calls to lists.

License
-------

MIT-licensed.

::
    
    Copyright (c) 2014 Grant Jenks
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.

Curriculum
----------

What follows are notes for a week-long curriculum with about 3 hours of classroom time each day.

Monday
......

- Interactive python interpreter
- nibbles.py
  - Commenting code
- guess.py
- paint.py
  - Getting help in the ipython interpreter

Tuesday
.......

- tron.py
- crypto.py
- memory.py

Wednesday
.........

- pacman.py
- bagels.py
- cannon.py
- cups.py

Thursday
........

- tictactoe.py
- hangman.py
- sonar.py
- simonsays.py

Friday
......

- pong.py
- connect.py
- maze.py
- tiles.py

Tags
----

- guess.py | text-based, puzzle
- hangman.py | text-based, two-player, puzzle
- crypto.py | text-based, topic:encryption
- bagels.py | text-based, puzzle

- connect.py | two-player, game
- tron.py | two-player, game
- pong.py | two-player, game

- maze.py | game, topic:maze
- cannon.py | game, topic:projectile-motion
- cups.py | game, topic:animation

- sonar.py | game, topic:distance
- nibbles.py | game
- pacman.py | game
- tictactoe.py | game, topic:artificial-intelligence

- memory.py | puzzle, image
- simonsays.py | game, puzzle
- tiles.py | puzzle, image

- paint.py | topic:drawing

- flappy.py | nyi


Quickstart
----------

Installing Free Python Games is simple with
`pip <http://www.pip-installer.org/>`_::

  $ pip install freegames

You can access documentation in the interpreter with Python's built-in help
function::

  >>> from freegames import snake
  >>> help(snake)

User Guide
----------

For those wanting more details, this part of the documentation describes
tutorial, API, and development.

* `Free Python Games Tutorial`_
* `Free Python Games API Reference`_
* `Free Python Games Development`_

.. _`Free Python Games Tutorial`: http://www.grantjenks.com/docs/freegames/tutorial.html
.. _`Free Python Games API Reference`: http://www.grantjenks.com/docs/freegames/api.html
.. _`Free Python Games Development`: http://www.grantjenks.com/docs/freegames/development.html

Reference and Indices
---------------------

* `Free Python Games Documentation`_
* `Free Python Games at PyPI`_
* `Free Python Games at GitHub`_
* `Free Python Games Issue Tracker`_

.. _`Free Python Games Documentation`: http://www.grantjenks.com/docs/freegames/
.. _`Free Python Games at PyPI`: https://pypi.python.org/pypi/freegames/
.. _`Free Python Games at GitHub`: https://github.com/grantjenks/free-python-games/
.. _`Free Python Games Issue Tracker`: https://github.com/grantjenks/free-python-games/issues/

Free Python Games License
-------------------------

Copyright 2017 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
