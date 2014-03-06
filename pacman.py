"""
Simplified Pacman.

# Getting Started

1. Open Google Chrome
2. Visit http://github.com/grantjenks/free_python_games
3. Click on pacman.py
4. Click on "Raw"
5. Ctrl-s to save the file.
6. Go Back twice.
7. Click on pacmang.jpg
8. Click on "Raw"
9. Ctrl-s to save the file.
10. Go Back twice.
11. Click on ghost.jpg
12. Click on "Raw"
13. Ctrl-s to save the file.
14. Open IDLE
15. In IDLE open pacman.py
16. Press F5

Written by Grant Jenks
http://www.grantjenks.com/

Copyright (c) 2012 Grant Jenks

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

Exercises
1. Change the pacman board.
2. Change the number of monsters.
3. Change the starting position of pacman.
4. Make the monsters faster/slower.
5. Make the monsters smarter.
"""

import sys
import pygame
import random
from pygame.locals import *

pygame.init()

font = pygame.font.Font(None, 24)
pacman_img = pygame.image.load('pacman.jpg')
ghost_img = pygame.image.load('ghost.jpg')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((340, 400))

class Game:
    """Track pacman game state."""
    def __init__(self):
        """Initialize game."""
        self.tiles_width = 17
        self.levels = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0,
             0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0,
             0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0,
             0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0,
             0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
             0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0,
             0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0,
             0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
             0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0,
             0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.reset()

    def reset(self):
        """Reset game to initial game state."""
        self.running = True
        self.score = 0
        self.level = 0
        self.next_dir = 0
        self.pacman = [pygame.Rect(160, 260, 20, 20), 0]
        self.ghosts = [[pygame.Rect(20, 20, 20, 20), 0],
                       [pygame.Rect(300, 20, 20, 20), 2],
                       [pygame.Rect(20, 340, 20, 20), 0],
                       [pygame.Rect(300, 340, 20, 20), 2]]

    def next_pos(self, next_dir, rect):
        """Advance rectangle by given direction."""
        if next_dir == 0: chng = (4, 0)
        if next_dir == 1: chng = (0, -4)
        if next_dir == 2: chng = (-4, 0)
        if next_dir == 3: chng = (0, 4)
        return rect.move(*chng)

    def rect_idx(self, rect):
        """Calculate tile index by rectangle."""
        return (rect.top / 20) * self.tiles_width + (rect.left / 20)

    def valid_pos(self, rect):
        """Return True iff character rectangle is valid on tiles."""
        prev_tile = self.levels[self.level][self.rect_idx(rect)]
        next_tile = self.levels[self.level][self.rect_idx(rect.move(19, 19))]
        on_track = rect.left % 20 == 0 or rect.top % 20 == 0
        return prev_tile != 0 and next_tile != 0 and on_track

    def move_rect(self, next_dir, curr_dir, rect):
        """
        Move character rectangle.
        Returns next character location and direction.
        """
        next_rect = self.next_pos(next_dir, rect)
        if self.valid_pos(next_rect):
            return (next_rect, next_dir)
        else:
            next_rect = self.next_pos(curr_dir, rect)
            if self.valid_pos(next_rect):
                return (next_rect, curr_dir)
        return (rect, curr_dir)

    def move_pacman(self):
        """Move pacman character."""
        rect, curr_dir = self.pacman
        tup = self.move_rect(self.next_dir, curr_dir, rect)
        self.pacman[0], self.pacman[1] = tup

    def move_ghosts(self):
        """Move ghost characters."""
        def dist_pacman(rect):
            return ((rect.top - self.pacman[0].top) ** 2
                    + (rect.left - self.pacman[0].left) ** 2) ** 0.5

        def test_dir(new_dir, curr_dir, rect):
            next_tup = self.move_rect(new_dir, curr_dir, rect)
            return dist_pacman(next_tup[0])

        for tup in self.ghosts:
            rect = tup[0]
            curr_dir = next_dir = tup[1]
            if rect.top % 20 == 0 and rect.left % 20 == 0:

                # Uncomment for Ghost AI
                #
                # dist = [(test_dir(val, curr_dir, rect), val)
                #         for val in (0, 1, 2, 3)]
                # min_dist = min(dist)
                # next_dir = min_dist[1]

                next_dir = (curr_dir + random.choice((1, 3))) % 4

            tup[0], tup[1] = self.move_rect(next_dir, curr_dir, rect)

    def update(self):
        """Update tiles, score and running based on pacman location."""
        self.next_dir = self.pacman[1]

        idx = self.rect_idx(self.pacman[0])
        if self.levels[self.level][idx] == 2:
            self.score += 1
            self.levels[self.level][idx] = 1

        has_food = any(val == 2 for val in self.levels[self.level])
        ghost_rects = [tup[0] for tup in self.ghosts]
        is_eaten = self.pacman[0].collidelist(ghost_rects) >= 0
        self.running = has_food and not is_eaten

    def draw(self):
        """Draw game on screen."""
        # Draw tiles

        for idx, val in enumerate(self.levels[self.level]):
            left = (idx % self.tiles_width) * 20
            top = (idx / self.tiles_width) * 20
            if val == 0:
                # Draws a blue square.
                color = (0, 0, 128)
                pygame.draw.rect(screen, color, (left, top, 20, 20))
            else:
                # Draw a black square.
                color = (0, 0, 0)
                pygame.draw.rect(screen, color, (left, top, 20, 20))
            if val == 2:
                # Draw a white dot.
                color = (255, 255, 255)
                pygame.draw.circle(screen, color, (left + 10, top + 10), 2)

        # Draw pacman.

        pacman_dir = pygame.transform.rotate(pacman_img, 90 * self.pacman[1])
        screen.blit(pacman_dir, self.pacman[0])

        # Draw ghosts.

        for val in self.ghosts:
            screen.blit(ghost_img, val[0])

        # Draw score.

        pygame.draw.rect(screen, (0, 0, 0), (0, 380, 100, 20))
        msg = 'Score: ' + str(self.score)
        text = font.render(msg , True, (255, 255, 255))
        screen.blit(text, (5, 382))

game = Game()

while True:

    event = pygame.event.poll()

    # Respond to key presses.

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            game.next_dir = 1
        elif event.key == K_RIGHT:
            game.next_dir = 0
        elif event.key == K_DOWN:
            game.next_dir = 3
        elif event.key == K_LEFT:
            game.next_dir = 2
        elif event.key == K_r:
            game.reset()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if game.running:
        game.move_pacman()
        game.move_ghosts()
        game.update()

    game.draw()

    # Display next frame.

    pygame.display.flip()
    clock.tick(12)
