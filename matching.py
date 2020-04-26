'''
exercise
1.Print the number of steps taken to complete the game
2.Try changing the symbols
3.change the size of GUI

'''


import time
from tkinter import Tk , Button , DISABLED
import random

def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()
    

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:#avoid pressing the same symbol twice 
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

win = Tk()
win.title('Matchmaker')
win.resizable(width=False , height=False)
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']
#unicode of symbols written twice in order to create two matches in the game

random.shuffle(symbols)
#shuffle the symbols everytime

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8)
        #If you press GUI nuton then only the unknown function lamda show symbol will execute
        button.grid(column = x , row = y)
        buttons[x,y] = button
        #store the button object in buttons dictionary 
        button_symbols[x,y] = symbols.pop()
        #pop will remove  the symbol from symbols list
win.mainloop()
