"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.

"""

from random import choice
from turtle import bgcolor, clear, up, down, goto, Turtle, dot, update, ontimer, setup, hideturtle, tracer, listen, onkey, done
from freegames import floor, vector

class Pacman:
    def __init__(self):
        self.aim = vector(5, 0)
        self.direction = "EAST"
        self.position = vector(-40, -80)
        self.status = "ALIVE"

    def move(self):
        self.position.move(self.aim)
    
    def dead(self):
        self.status = "DEAD"
    
    def alive(self):
        return self.status != "DEAD"

    def left(self):
        if self.direction == "NORTH" :
            self.aim.x = -5
            self.aim.y = 0

        elif self.direction == "SOUTH":
            self.aim.x = 5
            self.aim.y = 0

        elif self.direction == "WEST" :
            self.aim.x = 0
            self.aim.y = -5

        elif self.direction == "EAST":
            self.aim.x = 0
            self.aim.y = 5

    def right(self):
        if self.direction == "NORTH" :
            self.aim.x = 5
            self.aim.y = 0

        elif self.direction == "SOUTH":
            self.aim.x = -5
            self.aim.y = 0

        elif self.direction == "WEST" :
            self.aim.x = 0
            self.aim.y = 5

        elif self.direction == "EAST":
            self.aim.x = 0
            self.aim.y = -5  
    
    def u_turn(self):
        if self.direction == "NORTH" :
            self.aim.x = 0
            self.aim.y = -5
            
        elif self.direction == "SOUTH":
            self.aim.x = 0
            self.aim.y = 5
            
        elif self.direction == "WEST" :
            self.aim.x = 5
            self.aim.y = 0
            
        elif self.direction == "EAST":
            self.aim.x = -5
            self.aim.y = 0
            
class Ghost:
    def __init__(self,x,y,w,z):
        self.position = vector(x,y) 
        self.aim = vector(w, z)
        self.color = "red"
    def move(self):
        self.position.move(self.aim)
    
    def change_direction(self):
        options = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5),
        ]
        plan = choice(options)
        self.aim.x = plan.x
        self.aim.y = plan.y

class GamePacman:
    def __init__(self):
        self.state = {'score': 0}
        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.pacman = Pacman()
        self.ghosts = [Ghost(-180,160,5,0),
                    Ghost(-180,-160,0,5),
                    Ghost(100,160,0,-5),
                    Ghost(100,-160,-5,0)]
        self.tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.draw_world()

        onkey(lambda: self.on_rightkeypressed() , 'Right')
        onkey(lambda: self.on_leftkeypressed(), 'Left')
        onkey(lambda: self.on_upkeypressed(), 'Up')
        onkey(lambda: self.on_downkeypressed(), 'Down')

    def on_rightkeypressed(self):
        if self.pacman_next_position(5,0):
            if self.pacman.direction == 'NORTH':
                self.pacman.right()
            elif self.pacman.direction == "SOUTH":
                self.pacman.left()
            elif self.pacman.direction == "WEST":
                self.pacman.u_turn()
            self.pacman.direction = "EAST"
    
    def on_leftkeypressed(self):
        if self.pacman_next_position(-5,0):
            if self.pacman.direction == 'NORTH':
                self.pacman.left()
            elif self.pacman.direction == "SOUTH":
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.u_turn()
            self.pacman.direction = "WEST"

    def on_upkeypressed(self):
        if self.pacman_next_position(0,5):
            if self.pacman.direction == 'WEST':
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.left()
            if self.pacman.direction == "SOUTH":
                self.pacman.u_turn()
            self.pacman.direction = "NORTH"

    def  on_downkeypressed (self):
        if self.pacman_next_position(0,-5):
            if self.pacman.direction == 'WEST':
                self.pacman.left()
            elif self.pacman.direction == "EAST":
                self.pacman.right()
            elif self.pacman.direction == "NORTH":
                self.pacman.u_turn()
            self.pacman.direction = "SOUTH"

    def square(self,x,y):
        self.path.up()
        self.path.goto(x,y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)
        
        self.path.end_fill()
    
    def offset(self,point):
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(self,point):
        "Return True if point is valid in tiles."
        index = self.offset(point)

        if self.tiles[index] == 0:
            return False

        index = self.offset(point + 19)

        if self.tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0
    
    def pacman_next_position(self, x=None, y=None):
        if x != None and y != None:
            if self.valid(self.pacman.position + vector(x, y)):
                return True
            else:
                return False
        else:
            if self.valid(self.pacman.position + self.pacman.aim):
                return True
            else:
                return False
            
    def draw_world(self):
        bgcolor('black')
        self.path.color('blue')

        for index in range(len(self.tiles)):
            tile = self.tiles[index]
            if tile> 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.square(x,y)

                if tile == 1:
                    self.path.up()
                    self.path.goto(x + 10, y + 10)
                    self.path.dot(2, 'white')
        
    def draw_score(self):
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.state['score'])

        index = self.offset(self.pacman.position)
        if self.tiles[index] == 1:
            self.tiles[index] = 2
            self.state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            self.square(x, y)

    def move_pacman(self):
        self.pacman.move()

    def draw_pacman(self):
        up()
        goto(self.pacman.position.x +10 , self.pacman.position.y + 10)
        dot(20,'yellow')

    def move_and_draw_ghost(self):
        for ghost in self.ghosts:
            if self.valid(ghost.position + ghost.aim):
                ghost.move()
            else:
                ghost.change_direction()

            up()
            goto(ghost.position.x + 10, ghost.position.y + 10)
            dot(20, 'red')

    def check_collision(self):
        for ghost in self.ghosts:
            if abs(self.pacman.position - ghost.position) < 20:
                self.pacman.dead()

    def run(self):

        self.writer.undo()
        self.draw_score()
        clear()
        
        if self.pacman_next_position():
            self.move_pacman()
            self.draw_pacman()
        else:
            self.draw_pacman()

        self.move_and_draw_ghost()

        self.check_collision()

        if self.pacman.alive():
            ontimer(self.run, 100)
        else:
            return

        update()

def init():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()

    game = GamePacman()
    game.run()
    done()

if __name__ == '__main__':
    init()