"""
Nibbles the video game.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Change the colors.
2. Increase the size of the playing area.
3. Change the snake speed.
4. Make the food jump randomly.
5. Change the controls to (w, a, s, d)
6. Add diagonals.
7. Add high score.
8. Make the game boundaries into walls.
"""

import sys, pygame
from random import randrange
from pygame.locals import KEYDOWN, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_r, K_q
from itertools import count

size = width, height = 480, 480
up, right, down, left = (0, -10), (10, 0), (0, 10), (-10, 0)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 14)

snake_dir, food, dead = down, None, False
snake = [pygame.Rect(10, 10 + value * 10, 10, 10) for value in range(20)]
foreground, background = (255, 255, 255), (0, 0, 0)

for counter in count():
    clock.tick(min(5 + (len(snake) / 4), 30))

    event = pygame.event.poll()

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP and snake_dir != down:
            snake_dir = up
        elif event.key == K_RIGHT and snake_dir != left:
            snake_dir = right
        elif event.key == K_DOWN and snake_dir != up:
            snake_dir = down
        elif event.key == K_LEFT and snake_dir != right:
            snake_dir = left
        elif event.key == K_r:
            snake_dir, food, dead = down, None, False
            snake = [pygame.Rect(10, 10 + value * 10, 10, 10)
                     for value in range(20)]
            foreground, background = (255, 255, 255), (0, 0, 0)
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if dead:
        continue

    next = snake[-1].move(snake_dir)
    if next.left < 0: next.left = width - 10
    if next.left >= width: next.left = 0
    if next.top < 0: next.top = height - 10
    if next.top >= height: next.top = 0

    if next in snake:
        dead = True
        foreground, background = background, foreground
    else:
        snake.append(next)

        if next == food:
            food = None
        else:
            del snake[0]

    if food is None and counter % 50 == 0:
        food = pygame.Rect(randrange(48) * 10, randrange(48) * 10, 10, 10)

    screen.fill(background)
    for rect in snake:
        pygame.draw.rect(screen, foreground, rect)
    if food:
        pygame.draw.rect(screen, foreground, food)
    surface = font.render(str(len(snake)), True, foreground)
    screen.blit(surface, (0, 0))

    pygame.display.flip()
