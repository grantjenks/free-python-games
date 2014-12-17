# Written by Christopher Fong.
# Copyright 2014
# Minor edits (for JSnake) made by Grant Jenks.

"""
Copyright(c)2014 China Instruments
http://www.engrish.com/engrish
Model no: 1308
No License. (figures huh? Given our sketchy name.)
"""
import math
print 'Copyright(c)2014 China Instruments'
print 'Ti-Sketchy 1308'
print '__________________________'
print 'password required'

name = raw_input('Enter password:')
print ''
print ' "Eh...Close Enough" '
print '--------------------------'
while True:
    num1 = input("Enter first number: ")
    operation = raw_input("Enter operation(+,-,x,/,sqrt): ")
    if operation == "sqrt" or operation == "Sqrt":
        print math.sqrt(num1)
    else:
        num2 = input("Enter second number: ")
        if operation == "+":
            print "Answer:", num1+num2
        elif operation == "-":
            print "Answer:", num1-num2
        elif operation == "*" or operation == "x" or operation == "X":
            print "Answer:", num1*num2
        elif operation == "/":
            print "Answer:", num1/num2
        else:
            print "Syntax error"
