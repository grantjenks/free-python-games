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
        self.position = vector(-40, -80)#PACMAM

    def offset(self,point):
    "Return offset of point in tiles."
    "Retorne o deslocamento do ponto nos blocos."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

    def valid(self,point):
        "Return True if point is valid in tiles."
        "Retorne True se o ponto for válido em tiles."
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def move_pacma(self):
        "Move pacman and all ghosts."
        "Mova Pacman e todos os fantasmas."
        writer.undo() # desfaz o que foi feito anteriormente
        writer.write(state['score'])#update do score

        clear()
        # move-se se nao houver parede
        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)
        # verifica o caminho e move-se adiante 
        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, 'yellow')#desenha um circulo
            


class Ghosts:
    def __init__(self):
        self.position = [vector(-180, 160), vector(5, 0)]

    def move_ghosts(self):
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
        self.state = {'score': 0} #GAME
        self.path = Turtle(visible=False) #caminho
        self.writer = Turtle(visible=False)#estritor ?
        self.pacman = Pacman()
        self.ghosts = Ghosts()
    
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')

    tiles = [
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

    def world():
        "Draw world using path."
        "Desenhe o mundo usando o caminho."
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')
    def square(x, y):
        "Draw square using path at (x, y)."
        "Desenhe um quadrado usando o caminho em (x, y)."
        path.up()
        path.goto(x, y)#move o pincel ate a posição
        path.down()
        path.begin_fill()#chamado antes de desenhar uma forma 

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()
        update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)
    def change(x, y):
    "Change pacman aim if valid."
    "Mude o objetivo do pacman se for válido."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
def init():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    game = GamePacman()
    game.writer.goto(160, 160)
    game.writer.color('white')
    game.writer.write(state['score'])
    listen()
    game.world()
    #move()
    done()
    
if __name__ == '__main__':
    init()
