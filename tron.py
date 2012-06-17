"""
Tron, the video game.

Written by Grant Jenks
http://www.grantjenks.com/

DISCLAIMER
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE
LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY
SERVICING, REPAIR OR CORRECTION.

Copyright
This work is licensed under the
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-nd/3.0/
or send a letter to Creative Commons, 171 Second Street, Suite 300,
San Francisco, California, 94105, USA
"""

import sys, pygame
from pygame.locals import *

pygame.init()

black, red, blue, white = (0, 0, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)
up, right, down, left = (0, -2), (2, 0), (0, 2), (-2, 0)
width, height = size = 720, 720

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

class Player:
    def __init__(self, head, direction, color):
        self.direction = direction
        self.body = {}
        self.head = head
        self.color = color
        self.dead = False
    def move(self):
        next = self.head.move(self.direction)
        if next.left < 0: next.left = width - 10
        if next.left >= width: next.left = 0
        if next.top < 0: next.top = height - 10
        if next.top >= height: next.top = 0
        self.head = next
        self.body[tuple(self.head)] = self.head

player1 = Player(pygame.Rect(540, 360, 2, 2), left, red)
player2 = Player(pygame.Rect(180, 360, 2, 2), right, blue)

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP and player1.direction != down:
            player1.direction = up
        elif event.key == K_RIGHT and player1.direction != left:
            player1.direction = right
        elif event.key == K_DOWN and player1.direction != up:
            player1.direction = down
        elif event.key == K_LEFT and player1.direction != right:
            player1.direction = left
        elif event.key == K_w and player2.direction != down:
            player2.direction = up
        elif event.key == K_d and player2.direction != left:
            player2.direction = right
        elif event.key == K_s and player2.direction != up:
            player2.direction = down
        elif event.key == K_a and player2.direction != right:
            player2.direction = left
        elif event.key == K_r:
            player1 = Player(pygame.Rect(540, 360, 2, 2), left, red)
            player2 = Player(pygame.Rect(180, 360, 2, 2), right, blue)
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if player1.dead or player2.dead:
        continue

    player1.move()
    player2.move()

    if tuple(player1.head) in player2.body:
        player1.dead = True
    if tuple(player2.head) in player1.body:
        player2.dead = True

    if player1.dead == True or player2.dead == True:
        screen.fill(white)
    else:
        screen.fill(black)

    pygame.draw.rect(screen, player1.color, player1.head)
    pygame.draw.rect(screen, player2.color, player2.head)

    for rect in player1.body.itervalues():
        pygame.draw.rect(screen, player1.color, rect)
    for rect in player2.body.itervalues():
        pygame.draw.rect(screen, player2.color, rect)

    pygame.display.flip()
    clock.tick(24)
