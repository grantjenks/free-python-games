import unittest
import random
from mockturtle import mockTurtle
import runpy


class testDrive(unittest.TestCase):
    def testTurtle(self):
        _turtle = mockTurtle()
        _turtle.down
        _turtle.left

    def testSnake(self):
        mockTurtle.events[:] = (
            [('timer',), ('key Left',), ('timer',), ('key Up',)]
        + [('timer', True)] * 300
        )
        runpy.run_module('snake')
        
if __name__ == '__main__':
    unittest.main()


