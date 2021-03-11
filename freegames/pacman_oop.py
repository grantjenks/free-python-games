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
        self.direction = "WEST"
        self.position = vector(-40, -80)
        self.status = "ALIVE"

    def move(self,aim):
        "Change pacman aim if valid."
        self.position.move(aim)
class Ghost:
    def __init__(self):
        self.position = [vector(-180, 160), vector(5, 0)]

    def move(self):
        
        for point, course in ghosts:
            if valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y
            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

    update()

class GamePacman:
    def __init__(self):
        self.state = {'score': 0}
        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.pacman = Pacman()
        self.ghost = Ghost()
        self.aim = vector(5,0)
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

        onkey(lambda: self.change(5,0), 'Right')
        onkey(lambda: self.change(-5, 0), 'Left')
        onkey(lambda: self.change(0, 5), 'Up')
        onkey(lambda: self.change(0, -5), 'Down')
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
        self.pacman.move(self.pacman.aim)

        if self.tiles[index] == 0:
            return False

        index = self.offset(point + 19)

        if self.tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def change(self,x,y):
        if self.valid(self.pacman.position + vector(x, y)):
            self.pacman.aim.x = x
            self.pacman.aim.y = y

    
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
        

    
    def run(self):
        clear()
        if self.valid(self.pacman.position + self.aim):
            self.pacman.move(self.pacman.aim)
        index = self.offset(self.pacman.aim)

        if self.tiles[index] == 1:
            self.tiles[index] = 2
            self.state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            self.square(x, y)
        self.draw_world()
        self.draw_score()

        up()
        goto(self.pacman.aim.x + 10, self.pacman.aim.y + 10)
        dot(20,'yellow')

        
        update()
        ontimer(self.run, 100)
    
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


