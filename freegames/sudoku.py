from random import *
from turtle import *
from freegames import floor, vector, square
from tkinter import messagebox
import tkinter.messagebox
tiles = {}
# using in board_init(), no need to modify
origin_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
board = [[0 for j in range(0, 9)]
         for i in range(0, 9)]  # answerboard before erase(), a.k.a answer
board_show = [[0 for j in range(0, 9)]
              for i in range(0, 9)]  # Board to deal with in game, a.k.a masked board
board_tofill = [[0 for j in range(0, 9)]
                for i in range(0, 9)]  # Board to deal with in game, a.k.a masked board with user input
# using in board_init(), not using
row = [[0 for j in range(0, 10)] for i in range(0, 10)]
col = [[0 for j in range(0, 10)] for i in range(0, 10)]
diag = [[0 for j in range(0, 10)] for i in range(0, 10)]
# using in board_init(), no need to modify
terminate_flag = False
difficulty = -1  # default value
coordinate = vector(0, 0)

# board_init function, no need to modify, no need of use


def board_init():
    seq_diag = [0, 4, 8]
    for offset in range(0, 9, 3):
        seq = [i for i in range(1, 10)]
        shuffle(seq)
        for idx in range(0, 9):
            i, j = idx//3, idx % 3
            row[offset+i][seq[idx]] = 1
            col[offset+j][seq[idx]] = 1
            k = seq_diag[offset//3]
            diag[k][seq[idx]] = 1
            origin_board[offset+i][offset+j] = seq[idx]


# generate random number according to sudoku rule, no need to modify, no need of use
def make_sudoku(k):

    global terminate_flag
    global board
    global board_show

    if terminate_flag == True:
        return True

    if k > 80:
        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = origin_board[i][j]
                board_show[i][j] = origin_board[i][j]
                board_tofill[i][j] = origin_board[i][j]
        terminate_flag = True
        return True

    i, j = k//9, k % 9
    start_num = randint(1, 9)

    if origin_board[i][j] != 0:
        make_sudoku(k+1)

    for m in range(1, 10):
        m = 1 + (m + start_num) % 9
        d = (i//3)*3 + (j//3)
        if row[i][m] == 0 and col[j][m] == 0 and diag[d][m] == 0:
            row[i][m], col[j][m], diag[d][m] = 1, 1, 1
            origin_board[i][j] = m
            make_sudoku(k+1)
            row[i][m], col[j][m], diag[d][m] = 0, 0, 0
            origin_board[i][j] = 0


# masking function, no need to modify, no need of use
def erase(diff):
    global board_show

    if(diff == 0):
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                count = 0
                for z in range(99):
                    i = randrange(x, x + 3)
                    j = randrange(y, y + 3)
                    if(count == 3):
                        continue
                    if(board_show[i][j] is not None):
                        board_show[i][j] = None
                        board_tofill[i][j] = None
                        count += 1

    if(diff == 1):
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                count = 0
                for z in range(99):
                    i = randrange(x, x + 3)
                    j = randrange(y, y + 3)
                    if(count == 4):
                        continue
                    if(board_show[i][j] is not None):
                        board_show[i][j] = None
                        board_tofill[i][j] = None
                        count += 1

    if(diff == 2):
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                count = 0
                for z in range(99):
                    i = randrange(x, x + 3)
                    j = randrange(y, y + 3)
                    if(count == 5):
                        continue
                    if(board_show[i][j] is not None):
                        board_show[i][j] = None
                        board_tofill[i][j] = None
                        count += 1


# loading data function, no need to modify, no need of use
def sudoku_load():
    "Load tiles"

    i = 0
    j = 0
    for y in range(-325, 125, 50):
        for x in range(-225, 225, 50):
            mark = vector(x, y)
            tiles[mark] = board_tofill[i][j]
            j = j + 1
            if(j == 9):
                j = 0
                i = i + 1
            if(i == 9):
                break

# writing data function, no need to modify, no need of use


def square_given(mark, number):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)
    down()

    if -225 < mark.y < -25 and (mark.x < -75 or mark.x > 25):
        color('black', 'skyblue')
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()
    elif -125 < mark.x < 75 and (mark.y < -175 or mark.y > -75):
        color('black', 'skyblue')
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()
    else:
        color('black', 'white')
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()

    if number is None:
        return
    elif number < 10:
        forward(20)

    if board_show[int((mark.y + 325)/50)][int((mark.x + 225)/50)] is None:
        pencolor('blue')
        write(number, font=('Arial', 30, 'normal'))
    else:
        pencolor('black')
        write(number, font=('Arial', 30, 'normal'))

# restart the game & go to the page for selecting difficulty

def restart():
    global origin_board, board, board_show, board_tofill, row, col, dialog, terminate_flag, difficulty, coordinate

    tiles = {}
    origin_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
    board = [[0 for j in range(0, 9)] for i in range(0, 9)]
    board_show = [[0 for j in range(0, 9)] for i in range(0, 9)]
    board_tofill = [[0 for j in range(0, 9)] for i in range(0, 9)]
    row = [[0 for j in range(0, 10)] for i in range(0, 10)]
    col = [[0 for j in range(0, 10)] for i in range(0, 10)]
    diag = [[0 for j in range(0, 10)] for i in range(0, 10)]

    terminate_flag = False
    difficulty = -1
    coordinate = vector(0, 0)

    game_start()

# return how many cells are left to fill in

def num_of_last_tofills():
    global board_tofill
    toret = 0  # return value

    for x in range(0, 9):
        for y in range(0, 9):
            if(board_tofill[x][y] is None):
                toret += 1
    return toret

# check whether the user's board is correct or not

def Is_all_num_right():
    global board
    global board_tofill
    for x in range(0, 9):
        for y in range(0, 9):
            if(board_tofill[x][y] is not board[x][y]):               
                return 0
    return 1


# convert clicked coordinate to particular array


def tap_ingame(x, y):
    global terminate_flag
    global difficulty
    global coordinate
    result = change_pixel_index_to_button_index(x, y)
    if(result == 5):
        restart()

    elif(result != 5):
        array_x = int((x + 225)//50)
        array_y = int((y + 325)//50)
        # if click coordinate is out of box, change coordinate -1, -1
        if(array_x < 0 or array_x > 8 or array_y < 0 or array_y > 8):
            array_x = -1
            array_y = -1
            print("Out of range! Please click on the board.")
            return

        print(array_y, array_x)
        print(board_show[array_y][array_x])
        if(board_show[array_y][array_x] is None):
            temp = numinput("num input", "plz enter an integer",
                            None, minval=1, maxval=9)
            if temp is not int:
                tkinter.messagebox.showinfo("Warning!","입력하신 수는 정수가 아닙니다!")
            if temp is not None:
                board_tofill[array_y][array_x] = int(temp)
            
            sudoku_load()
            draw()

            # check whether the completed board is correct or not

            if(num_of_last_tofills() == 0):
                judgement = Is_all_num_right()
                if(judgement == 1):
                    print("Correct answer!")
                    if messagebox.askyesno("Congratulations!", "You won! New Game?") == True:
                        restart()
                    else:
                        print("Bye!")
                        exit()
                else:
                    print("Not a correct board")
                    messagebox.showerror("Wrong answer!", "Not a correct board. Try again!")
                    

def change_pixel_index_to_button_index(x, y):
    if(x >= 200 and x <= 280 and y <= 330 and y >= 280):
        return 5
    elif(x >= 60 and x <= 140 and y <= 0 and y >= -80):
        return 3
    elif(x >= - 40 and x <= 40 and y <= 0 and y >= -80):
        return 2
    elif(x >= - 140 and x <= -60 and y <= 0 and y >= -80):
        return 1
    else:
        return 0

# print title


def print_title():
    up()
    goto(0, 250)
    down()
    write("SUDOKU", move=False, align="center", font=("Arial", 30, "bold"))

# print difficulty level


def print_difficulty():
    global difficulty

    up()
    goto(0, 200)
    down()
    if difficulty == 0:
        write("Easy", move=False, align="center",
              font=("Arial", 20, "underline"))
    if difficulty == 1:
        write("Normal", move=False, align="center",
              font=("Arial", 20, "underline"))
    if difficulty == 2:
        write("Hard", move=False, align="center",
              font=("Arial", 20, "underline"))

# drawing square


def draw():
    up()
    "Draw all tiles."
    for mark in tiles:
        square_given(mark, tiles[mark])
    update()
    down()

# recognize which button is clicked


def tap_button(x, y):
    global difficulty
    result = change_pixel_index_to_button_index(x, y)
    if(result == 1):
        difficulty = 0
    elif(result == 2):
        difficulty = 1
    elif(result == 3):
        difficulty = 2

    if(difficulty != -1):
        clear()
        board_init()
        make_sudoku(0)
        erase(difficulty)
        ingame()
        reloadbutton()

# create page to choose difficulty


def game_start():
    clear()
    print_title()
    square(-140, -80, 80, 'gray')
    up()
    goto(-100, -50)
    down()
    color('black')
    write("Easy", move=True, align="center", font=("Arial", 15, "bold"))
    square(-40, -80, 80, 'gray')
    up()
    goto(0, -50)
    down()
    color('black')
    write("Normal", move=True, align="center", font=("맑은고딕", 15, "bold"))
    square(60, -80, 80, 'gray')
    up()
    goto(100, -50)
    down()
    color('black')
    write("Hard", move=True, align="center", font=("맑은고딕", 15, "bold"))
    up()
    goto(0, 100)
    down()
    color('black')
    write("Please select the difficulty level", move=True,
          align="center", font=("맑은고딕", 18, "bold"))
    onscreenclick(tap_button)

# manage game function


def ingame():
    print_title()
    print_difficulty()
    sudoku_load()
    draw()
    onscreenclick(None)
    onscreenclick(tap_ingame)  # bind tap_ingame


def reloadbutton():
    up()
    goto(250, 300)
    down()
    color('black')
    write("HOME", move=True, align="center", font=("Arial", 15, "bold"))


setup(600, 800, 370, 0)
hideturtle()
speed(0)
tracer(False)
game_start()
done()
