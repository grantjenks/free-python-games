"""Mock turtle module.
"""

state = {}
events = []


class Turtle:
    def __init__(self, visible=True):
        pass

    def goto(self, x, y):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def width(self, size):
        pass

    def color(self, fill, outline=None):
        pass

    def write(self, text, font=None):
        pass

    def begin_fill(self):
        pass

    def end_fill(self):
        pass

    def forward(self, steps):
        pass

    def back(self, steps):
        pass

    def addshape(self, reference):
        pass

    def shape(self, reference):
        pass

    def stamp(self):
        pass

    def left(self, degrees):
        pass

    def right(self, degrees):
        pass

    def hideturtle(self):
        pass

    def tracer(self, state):
        pass

    def dot(self, size, color=None):
        pass

    def clear(self):
        pass

    def circle(self, radius):
        pass

    def bgcolor(self, name):
        pass

    def update(self):
        pass

    def undo(self):
        pass


_turtle = Turtle()
goto = _turtle.goto
up = _turtle.up
down = _turtle.down
width = _turtle.width
color = _turtle.color
write = _turtle.write
begin_fill = _turtle.begin_fill
end_fill = _turtle.end_fill
forward = _turtle.forward
back = _turtle.back
addshape = _turtle.addshape
shape = _turtle.shape
stamp = _turtle.stamp
left = _turtle.left
right = _turtle.right
hideturtle = _turtle.hideturtle
tracer = _turtle.tracer
dot = _turtle.dot
clear = _turtle.clear
circle = _turtle.circle
bgcolor = _turtle.bgcolor
update = _turtle.update
undo = _turtle.undo


def setup(width, height, x, y):
    pass


def listen():
    pass


def onkey(function, key):
    state['key ' + key] = function


def ontimer(function, delay):
    state['timer'] = function
    state['delay'] = delay


def onscreenclick(function):
    state['click'] = function


def done():
    for event in events:
        name = event[0]

        try:
            function = state[name]
        except KeyError:
            if name == 'timer':
                if event[1:] and event[1]:
                    continue
            raise

        if name == 'timer':
            del state['timer']
            del state['delay']
            args = ()
        else:
            args = event[1:]

        function(*args)
