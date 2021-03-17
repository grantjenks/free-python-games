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
        self.status = "DIE"
    
    def alive(self):
        return self.status != "DIE"
    
    def next_position(self, aim=None):
        if aim != None :
            new_position = self.position + aim
        else:
            new_position = self.position + self.aim
        return new_position

    turn_to_left = {'NORTH': ('WEST', vector(-5, 0)),
                'WEST' : ('SOUTH', vector(0, -5)),
                'SOUTH': ('EAST', vector(5, 0)),
                'EAST' : ('NORTH', vector(0, 5))}

    turn_to_right = {'NORTH': ('EAST', vector(5, 0)),
                'EAST' : ('SOUTH', vector(0, -5)),
                'SOUTH': ('WEST', vector(-5, 0)),
                'WEST' : ('NORTH', vector(0, 5))}

    turn_to_go_back = {'NORTH': ('SOUTH', vector(0, -5)),
                'SOUTH' : ('NORTH', vector(0, 5)),
                'WEST': ('EAST', vector(5, 0)),
                'EAST' : ('WEST', vector(-5, 0))}

    def left(self):
        self.direction, new_aim = self.turn_to_left[self.direction]
        self.aim.x = new_aim.x
        self.aim.y = new_aim.y

    def right(self):
        self.direction, new_aim = self.turn_to_right[self.direction]
        self.aim.x = new_aim.x
        self.aim.y = new_aim.y
    
    def u_turn(self):
        self.direction, new_aim = self.turn_to_go_back[self.direction]
        self.aim.x = new_aim.x
        self.aim.y = new_aim.y
  
class Ghost:
    def __init__(self,position_x,position_y,aim_x,aim_y):
        self.position = vector(position_x,position_y) 
        self.aim = vector(aim_x, aim_y)

    def move(self):
        self.position.move(self.aim)
    
    def change_direction(self):
        options = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5),
        ]
        self.aim = choice(options)

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
        if self.valid(self.pacman.next_position(vector(5,0))):
            if self.pacman.direction == 'NORTH':
                self.pacman.right()
            elif self.pacman.direction == "SOUTH":
                self.pacman.left()
            elif self.pacman.direction == "WEST":
                self.pacman.u_turn()
    
    def on_leftkeypressed(self):
        if self.valid(self.pacman.next_position (vector(-5,0))):
            if self.pacman.direction == 'NORTH':
                self.pacman.left()
            elif self.pacman.direction == "SOUTH":
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.u_turn()


    def on_upkeypressed(self):
        if self.valid(self.pacman.next_position(vector(0,5))):
            if self.pacman.direction == 'WEST':
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.left()
            elif self.pacman.direction == "SOUTH":
                self.pacman.u_turn()

    def  on_downkeypressed (self):
        if self.valid(self.pacman.next_position(vector(0,-5))):
            if self.pacman.direction == 'WEST':
                self.pacman.left()
            elif self.pacman.direction == "EAST":
                self.pacman.right()
            elif self.pacman.direction == "NORTH":
                self.pacman.u_turn()

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

    def move_and_draw_pacman(self):
        if self.valid(self.pacman.next_position()):
            self.pacman.move()

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

        self.move_and_draw_pacman()

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