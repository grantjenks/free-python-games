
from turtle import *
from unittest import mock



@mock.patch('turtle.class')
class mockTurtle():
        
    state = {}
    events = []
    @mock.patch('turtle.__init__')
    def __init__(self, visible=True):
        pass
    
    @mock.patch('turtle.goto')
    def goto(self, x, y):
        pass
    
    @mock.patch('turtle.up')
    def up(self):
        pass
    
    @mock.patch('turtle.down')
    def down(self):
        pass

    @mock.patch('turtle.width')
    def width(self, size):
        pass
    
    @mock.patch('turtle.color')
    def color(self, fill, outline=None):
        pass

    @mock.patch('turtle.write')
    def write(self, text, font=None):
        pass
    
    @mock.patch('turtle.begin_fill')
    def begin_fill(self):
        pass

    @mock.patch('turtle.end_fill')
    def end_fill(self):
        pass

    @mock.patch('turtle.forward')
    def forward(self, steps):
        pass

    @mock.patch('turtle.back')
    def back(self, steps):
        pass

    @mock.patch('turtle.addshape')
    def addshape(self, reference):
        pass

    @mock.patch('turtle.shape')
    def shape(self, reference):
        pass

    @mock.patch('turtle.stamp')
    def stamp(self):
        pass

    @mock.patch('turtle.left')
    def left(self, degrees):
        pass

    @mock.patch('turtle.right')
    def right(self, degrees):
        pass

    @mock.patch('turtle.hideturtle')
    def hideturtle(self):
        pass

    @mock.patch('turtle.tracer')
    def tracer(self, state):
        pass

    @mock.patch('turtle.dot')
    def dot(self, size, color=None):
        pass

    @mock.patch('turtle.clear')
    def clear(self):
        pass

    @mock.patch('turtle.radius')
    def circle(self, radius):
        pass

    @mock.patch('turtle.bgcolor')
    def bgcolor(self, name):
        pass

    @mock.patch('turtle.update')
    def update(self):
        pass
    
    @mock.patch('turtle.undo')
    def undo(self):
        pass


_turtle = mockTurtle()
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
        



