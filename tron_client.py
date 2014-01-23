"""
Tron Client

Written by Grant Jenks
http://www.grantjenks.com/

Copyright (c) 2013 Grant Jenks

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
"""

import asynchat, asyncore, pygame, Queue, socket, sys, threading
from pygame.locals import *

# Networking handler.

class TronClient(asynchat.async_chat):

    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        self.set_terminator('\n')
        self.buffer = []

    def collect_incoming_data(self, data):
        self.buffer.append(data)

    def found_terminator(self):
        msg = ''.join(self.buffer)
        if msg == '0':
            restart()
        elif msg.startswith('1 '):
            data = map(int, msg.split(' '))
            queue.put(data)
        self.buffer = []

# Initialize communication queue.

queue = Queue.Queue()

# Initialize pygame.

black = (0, 0, 0)
tiles, width = 120, 4
dirs = (up, right, down, left) = (-tiles, 1, tiles, -1)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((tiles * width, tiles * width))

# Setup connection.

if len(sys.argv) > 1:
    ip_addr = sys.argv[1]
else:
    ip_addr = socket.gethostbyname(socket.gethostname())
print 'Connecting to', ip_addr, 8080
client = TronClient(ip_addr, 8080)

# Start listening to the server.

comm = threading.Thread(target=asyncore.loop)
comm.daemon = True
comm.start()

# Drawing functions.

def restart():
    screen.fill(black)
    pygame.display.flip()

# Game loop.

direction = left

while True:
    clock.tick(36)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP and direction != down:
            direction = up
            client.send('{0}\n'.format(dirs.index(direction)))
        elif event.key == K_RIGHT and direction != left:
            direction = right
            client.send('{0}\n'.format(dirs.index(direction)))
        elif event.key == K_DOWN and direction != up:
            direction = down
            client.send('{0}\n'.format(dirs.index(direction)))
        elif event.key == K_LEFT and direction != right:
            direction = left
            client.send('{0}\n'.format(dirs.index(direction)))
        if event.key == K_r:
            client.send('4\n')
            restart()
            queue = Queue.Queue()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    while True:
        try:
            data = queue.get(False)
            direction = data[2]
            rect = ((4 * (data[1] % tiles)), (4 * (data[1] / tiles)), 4, 4)
            pygame.draw.rect(screen, data[-3:], rect)
            pygame.display.update(rect)
        except Queue.Empty:
            break
