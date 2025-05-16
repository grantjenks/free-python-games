Tic Tac Toe
===========

A single-player vs computer Tic Tac Toe game with the following features:

- **Colored and styled pieces**:
  X in blue, O in red, with thicker lines for clarity.
- **Move validation**:
  Prevents placing a piece on an occupied square.
- **Win and draw detection**:
  Automatically detects and displays a result message when someone
  wins or when the board is full (draw).
- **Smart AI opponent**:
  Uses the Minimax algorithm for optimal play, ensuring a
  challenging game.

Gameplay
--------

1. **Starting the game**:

   .. code-block:: python

      python tictactoe.py

2. **Player moves**:
   The human player uses X (blue) and always moves first. Click on
   any empty square in the 3×3 grid to place your X.

3. **Computer response**:
   After your move, the computer (O in red) will calculate its optimal
   move and place an O after a brief delay.

4. **Winning**:
   The first player to align three of their own pieces in a row
   (horizontal, vertical, or diagonal) wins.

5. **Draw**:
   If all nine squares are filled without a winner, the game ends
   in a draw.

.. literalinclude:: ../src/freegames/tictactoe.py
   :language: python
   :linenos: