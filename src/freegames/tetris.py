import tkinter as tk
import random

CELL_SIZE = 30
COLUMNS = 10
ROWS = 20
ANIMATION_SPEED = 500


SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
]
COLORS = ['cyan', 'yellow', 'purple', 'green', 'red', 'blue', 'orange']

class Tetris(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.canvas = tk.Canvas(self, width=CELL_SIZE*COLUMNS, height=CELL_SIZE*ROWS)
        self.canvas.pack()
        self.init_game()
        self.pack()
        self.master.bind('<Key>', self.key_pressed)
        self.after(ANIMATION_SPEED, self.game_loop)

    def init_game(self):
        self.grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.score = 0
        self.new_piece()

    def new_piece(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0
        if self.collision(self.x, self.y):
            self.game_over()

    def rotate_shape(self):
        rotated = [list(row) for row in zip(*self.shape[::-1])]
        if not self.collision(self.x, self.y, rotated):
            self.shape = rotated

    def collision(self, x, y, shape=None):
        shape = shape or self.shape
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    if (i+y >= ROWS or j+x < 0 or j+x >= COLUMNS or self.grid[i+y][j+x]):
                        return True
        return False

    def freeze(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.y+i][self.x+j] = self.color
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared = ROWS - len(new_grid)
        for _ in range(cleared):
            new_grid.insert(0, [0 for _ in range(COLUMNS)])
        self.grid = new_grid
        self.score += cleared

    def game_loop(self):
        if not self.move(0, 1):
            self.freeze()
        self.draw()
        self.after(ANIMATION_SPEED, self.game_loop)

    def move(self, dx, dy):
        if not self.collision(self.x+dx, self.y+dy):
            self.x += dx
            self.y += dy
            return True
        return False

    def key_pressed(self, event):
        key = event.keysym
        if key == 'Left':
            self.move(-1, 0)
        elif key == 'Right':
            self.move(1, 0)
        elif key == 'Down':
            self.move(0, 1)
        elif key == 'Up':
            self.rotate_shape()
        elif key == 'space':
            while self.move(0, 1):
                pass
            self.freeze()
        self.draw()

    def draw(self):
        self.canvas.delete('all')
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell:
                    self.draw_cell(j, i, cell)
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.draw_cell(self.x+j, self.y+i, self.color)
        self.master.title(f'Tetris - Score: {self.score}')

    def draw_cell(self, x, y, color):
        x1, y1 = x*CELL_SIZE, y*CELL_SIZE
        x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def game_over(self):
        self.canvas.create_text(CELL_SIZE*COLUMNS//2, CELL_SIZE*ROWS//2,
            text='GAME OVER', fill='red', font=('Helvetica', 24))
        self.master.unbind('<Key>')

if __name__ == '__main__':
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()