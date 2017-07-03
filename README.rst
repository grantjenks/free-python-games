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

TODO

* Setup AppVeyor
* Add comment to bagels.py and crypto.py
* Describe how games work
* Confirm testimonials
* Curriculum page
* Improve module help docstring


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
- Developed on Python 3.4
- Tested on CPython 2.7, 3.4, 3.5, and 3.6
- Tested on Windows, Mac OS X, Raspbian (Raspberry Pi), and Linux
- Tested using Travis CI and AppVeyor CI

.. image:: https://api.travis-ci.org/grantjenks/free-python-games.svg?branch=master
    :target: http://www.grantjenks.com/docs/freegames/

.. image:: https://ci.appveyor.com/api/projects/status/github/grantjenks/free-python-games?branch=master&svg=true
    :target: http://www.grantjenks.com/docs/freegames/


Quickstart
----------

Installing Free Python Games is simple with
`pip <http://www.pip-installer.org/>`_::

  $ python3 -m pip install freegames
  $ python3 -m freegames --help

You can access documentation in the interpreter with Python's built-in help
function::

  >>> import freegames
  >>> help(freegames)


Free Games
----------

Paint
.....

Paint -- draw lines and shapes on the screen.

.. image:: http://www.grantjenks.com/docs/freegames/_static/paint.gif
   :alt: Paint Free Python Game

Snake
.....

Snake -- classic arcade game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/snake.gif
   :alt: Snake Free Python Game

Pacman
......

Pacman -- classic arcade game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/pacman.gif
   :alt: Pacman Free Python Game

Cannon
......

Cannon -- projectile motion.

.. image:: http://www.grantjenks.com/docs/freegames/_static/cannon.gif
   :alt: Cannon Free Python Game

Connect
.......

Connect -- Connect 4 game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/connect.gif
   :alt: Connect Free Python Game

Flappy
......

Flappy -- Flappy-bird inspired game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/flappy.gif
   :alt: Flappy Free Python Game

Memory
......

Memory -- puzzle game of number pairs.

.. image:: http://www.grantjenks.com/docs/freegames/_static/memory.gif
   :alt: Memory Free Python Game

Pong
....

Pong -- classic arcade game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/pong.gif
   :alt: Pong Free Python Game

Simon Says
..........

Simon Says -- classic memory puzzle game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/simonsays.gif
   :alt: Simonsays Free Python Game

Tic Tac Toe
...........

Tic Tac Toe -- classic game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/tictactoe.gif
   :alt: Tictactoe Free Python Game

Tiles
.....

Tiles -- puzzle game of sliding numbers into place.

.. image:: http://www.grantjenks.com/docs/freegames/_static/tiles.gif
   :alt: Tiles Free Python Game

Tron
....

Tron -- classic arcade game.

.. image:: http://www.grantjenks.com/docs/freegames/_static/tron.gif
   :alt: Tron Free Python Game

Fidget
......

Fidget -- fidget spinner inspired animation.

.. image:: http://www.grantjenks.com/docs/freegames/_static/fidget.gif
   :alt: Fidget Free Python Game


User Guide
----------

For those wanting more details, this part of the documentation describes
tutorial, API, and development.

* `Free Python Games Curriculum`_
* `Free Python Games API Reference`_
* `Free Python Games Development`_

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
