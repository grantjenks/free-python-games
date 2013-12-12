"""
Tron Server

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

import asynchat, asyncore, random, socket, threading, time

# Handler management.

handno = 0
handlers = {}

# Tron game globals.

tiles, width = 120, 4
dirs = (up, right, down, left) = (-tiles, 1, tiles, -1)
black = (0, 0, 0)
board = [black] * (tiles * tiles)

# Handler and server for Tron.

class TronHandler(asynchat.async_chat):
    def __init__(self, sock):
        global handno

        asynchat.async_chat.__init__(self, sock=sock)

        self.set_terminator('\n')
        self.buffer = []

        self.color = tuple(int(random.random() * 255) for rpt in xrange(3))
        self.init_player()

        self.handno = handno
        handlers[self.handno] = self
        handno += 1

    def init_player(self):
        self.direction = random.choice(dirs)
        self.position = int(random.random() * tiles * tiles)
        self.dead = False

    def handle_close(self):
        try:
            del handlers[self.handno]
        except KeyError:
            pass
        asynchat.async_chat.handle_close(self)

    def collect_incoming_data(self, data):
        self.buffer.append(data)

    def found_terminator(self):
        global board

        cmd = int(''.join(self.buffer))

        if cmd < 4:
            self.direction = dirs[cmd]
        elif cmd == 4:
            board = [black] * (tiles * tiles)
            for handler in handlers.values():
                try:
                    handler.init_player()
                    handler.send('0\n')
                except:
                    pass

        self.buffer = []

class TronServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = TronHandler(sock)

# Connect server.

ip_addr = socket.gethostbyname(socket.gethostname())
print 'Listening at', ip_addr, 8080
server = TronServer(ip_addr, 8080)

# Launch server in separate thread.

comm = threading.Thread(target=asyncore.loop)
comm.daemon = True
comm.start()

# Game Logic.

def move(player):
    global board
    curr = player.position

    curr_x = curr % tiles
    curr_y = curr / tiles

    if player.direction == left:
        curr_x -= 1
    elif player.direction == right:
        curr_x += 1
    elif player.direction == up:
        curr_y -= 1
    elif player.direction == down:
        curr_y += 1

    curr_x %= tiles
    curr_y %= tiles

    next = curr_x + tiles * curr_y

    if board[next] != black:
        # player.dead = True
        pass
    else:
        board[next] = player.color

    player.position = next

# Game loop.

while True:
    # Try to show 36 frames per second.

    time.sleep(1.0/36)

    if any(handler.dead for handler in handlers.values()):
        continue

    # Move all the players.

    for player in handlers.values():
        move(player)

    # Create the message that updates every player's position.

    msgs = []
    for player in handlers.values():
        data = (1, player.position, player.direction) + player.color
        msgs.append(' '.join(map(str, data)))

    msgs.append('')
    msg = '\n'.join(msgs)

    # Communicate new player positions.

    for handler in handlers.values():
        try:
            handler.send(msg)
        except:
            pass
