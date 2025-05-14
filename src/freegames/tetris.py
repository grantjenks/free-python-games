import pygame
import random

# 定义常量
W = 15
H = 20
BLOCK_SIZE = 30
SIDE_WIDTH = 200  # 左侧区域宽度
GAME_AREA_X = SIDE_WIDTH  # 游戏区域X坐标起点
GAME_AREA_Y = 0  # 游戏区域Y坐标起点
GAME_AREA_WIDTH = W * BLOCK_SIZE
GAME_AREA_HEIGHT = H * BLOCK_SIZE
FPS = 30

# 颜色定义（新增边框颜色）
BORDER_COLOR = (100, 100, 100)  # 深灰色边框
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

COLORS = [CYAN, YELLOW, MAGENTA, GREEN, RED, BLUE, ORANGE]

# 方块形状
n = [
    [15, 0, 0, 0], [1, 1, 1, 1], [15, 0, 0, 0], [1, 1, 1, 1],
    [3, 3, 0, 0], [3, 3, 0, 0], [3, 3, 0, 0], [3, 3, 0, 0],
    [1, 7, 0, 0], [6, 2, 2, 0], [0, 7, 4, 0], [2, 2, 3, 0],
    [0, 7, 1, 0], [2, 2, 6, 0], [4, 7, 0, 0], [3, 2, 2, 0],
    [2, 7, 0, 0], [2, 6, 2, 0], [0, 7, 2, 0], [2, 3, 2, 0],
    [6, 3, 0, 0], [1, 3, 2, 0], [6, 3, 0, 0], [1, 3, 2, 0],
    [3, 6, 0, 0], [2, 3, 1, 0], [3, 6, 0, 0], [2, 3, 1, 0]
]

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode((W * BLOCK_SIZE + SIDE_WIDTH, H * BLOCK_SIZE))
pygame.display.set_caption("俄罗斯方块")
clock = pygame.time.Clock()

# 初始化地图和其他变量
m = [[0 for _ in range(W)] for __ in range(H)]
x = 1
y = 1
t = 0
next_t = random.randint(0, 27)  # 下一个方块的形状
tot = 0
score = 0


def draw_block(x, y, color):
    """绘制单个方块（调整坐标到游戏区域）"""
    x_pos = x * BLOCK_SIZE + GAME_AREA_X
    y_pos = y * BLOCK_SIZE + GAME_AREA_Y
    pygame.draw.rect(screen, color, (x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, BLACK, (x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_game_border():
    """绘制游戏区域边框"""
    pygame.draw.rect(screen, BORDER_COLOR,
                     (GAME_AREA_X, GAME_AREA_Y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT), 3)


def draw_next_block():
    """绘制下一个方块"""
    pygame.draw.rect(screen, GRAY, (10, 100, 180, 180), 2)
    font = pygame.font.Font(None, 36)
    text = font.render("Next Block:", True, WHITE)
    screen.blit(text, (20, 60))
    for i in range(4):
        for j in range(4):
            if n[next_t][i] >> j & 1:
                pygame.draw.rect(screen, COLORS[next_t // 4],
                                 (20 + j * BLOCK_SIZE, 120 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (20 + j * BLOCK_SIZE, 120 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_score():
    """绘制得分"""
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))


def draw_board():
    screen.fill(BLACK)

    # 绘制游戏区域边框
    draw_game_border()

    # 绘制地图方块和当前下落方块
    for i in range(H):
        for j in range(W):
            if m[i][j]:
                draw_block(j, i, GRAY)
    for i in range(4):
        for j in range(4):
            if n[t][i] >> j & 1:
                draw_block(x + j, y + i, COLORS[t // 4])

    draw_score()
    draw_next_block()


def is_collision(mode, value=None):
    global x, y, t
    check_x = x if mode != 'x' else value
    check_y = y if mode != 'y' else value
    check_t = t if mode != 't' else value
    for i in range(4):
        for j in range(4):
            if n[check_t][i] >> j & 1:
                block_x = check_x + j
                block_y = check_y + i
                if block_y < 0 or block_y >= H or block_x < 0 or block_x >= W:
                    return True
                if block_y >= 0 and m[block_y][block_x]:
                    return True
    return False


def move(variable, w):
    global x, y, t, m, score, next_t
    if variable == 'x':
        new_x = x + w
        if not is_collision('x', new_x):
            x = new_x
    elif variable == 'y':
        new_y = y + w
        if not is_collision('y', new_y):
            y = new_y
        else:
            for i in range(4):
                for j in range(4):
                    if n[t][i] >> j & 1:
                        m[y + i][x + j] = 1
            full_rows = [i for i, row in enumerate(m) if all(row)]
            for row in full_rows:
                del m[row]
                m.insert(0, [0] * W)
            score += len(full_rows) * 100
            x = 1
            y = 1
            t = next_t
            next_t = random.randint(0, 27)
            if any(m[0]):
                return False
    elif variable == 't':
        new_t = (t + w) % 28
        if not is_collision('t', new_t):
            t = new_t
    return True


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move('x', -1)
            elif event.key == pygame.K_RIGHT:
                move('x', 1)
            elif event.key == pygame.K_DOWN:
                if not move('y', 1):
                    running = False
            elif event.key == pygame.K_UP:
                move('t', 1 if t % 4 != 3 else -3)
            elif event.key == pygame.K_SPACE:
                while move('y', 1):
                    pass

    tot += 1
    if tot >= FPS // 2:
        if not move('y', 1):
            running = False
        tot = 0

    draw_board()
    pygame.display.flip()

pygame.quit()
print(f"Game Over，你的得分为 {score}")
#这个是我新加的，你的要求都完成了，你能看到吗，欧克，这个新增加了一个俄罗斯方块，你的任务指标都完成了，这个项目是游戏的整合，一个游戏是一个分支，新增游戏就相当与增加了一个功能吧
#software 可以 可以 欧克