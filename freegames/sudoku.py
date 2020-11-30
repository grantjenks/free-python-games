from random import *
from turtle import *
from freegames import floor, vector

# def sudoku_load 를 정의한다. -> 실행할 때마다 현재 sudoku 상태를 입력된 숫자를 base로 업데이트
# 입력된 것이 1~9가 아닐경우 에러 메세지를 출력한다.
# 입력된 것이 한줄 혹은 한 박스를 모두 채우면 색깔을 바꾼다?
# 입력된 숫자는 업데이트 할 수 있어야 한다.
# def sudoku_restart를 정의한다. -> 초기화 한다.
#######################################
# def game_start를 정의한다. -> game start 버튼을 생성한다. 난이도 선택 누르면 sudoku_load 한다.
tiles = {}
difficulty = 0
origin_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
board = [[0 for j in range(0, 9)] for i in range(0, 9)]
board_show = [[0 for j in range(0, 9)] for i in range(0, 9)]
row = [[0 for j in range(0, 10)] for i in range(0, 10)]
col = [[0 for j in range(0, 10)] for i in range(0, 10)]
diag = [[0 for j in range(0, 10)] for i in range(0, 10)]
terminate_flag = False
difficulty = -1
push = 1


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
                    if(board_show[i][j] != None):
                        board_show[i][j] = None
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
                    if(board_show[i][j] != None):
                        board_show[i][j] = None
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
                    if(board_show[i][j] != None):
                        board_show[i][j] = None
                        count += 1


def sudoku_load():
    "Load tiles"

    i = 0
    j = 0
    for y in range(-200, 250, 50):
        for x in range(-200, 250, 50):
            mark = vector(x, y)
            tiles[mark] = board_show[i][j]
            j = j + 1
            if(j == 9):
                j = 0
                i = i + 1
            if(i == 9):
                break


def square(mark, number):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)
    down()

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

    write(number, font=('Arial', 30, 'normal'))


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    coordinate = vector(x, y)
    print(coordinate)


def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark, tiles[mark])
    update()


def game_start():
    "draw game start button and select difficulty"
    print("Hello")
    s = textinput("", "please select your difficulty")


setup(1000, 1000, 370, 0)
hideturtle()
onscreenclick(tap)
tracer(False)
game_start()
board_init()
make_sudoku(0)
erase(difficulty)
sudoku_load()
draw()
done()
