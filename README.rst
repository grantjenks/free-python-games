Free Python Games
=================

A collection (10) of free python games.

In the first half of 2012, I used these games to teach a group of students some basics of programming. The goal was to have fun as much as it was to learn. Here you'll find simplified versions of several classics.

Each game is entirely independent from the others and includes comments along with a list of exercises to work through with students. In order of difficulty:

* Guess the Number
* Hangman
* Connect 4
* Nibbles
* Tron
* Tiles
* Memory
* Pacman
* Maze
* Tic Tac Toe

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
