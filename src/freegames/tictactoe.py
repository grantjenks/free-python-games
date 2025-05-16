from turtle import *

from freegames import line

# ——— 全局状态 ———
state = {
    'player': 0,                   # 0 = X（人），1 = O（电脑）
    'board': [[None]*3 for _ in range(3)],
    'game_over': False,
}

# 绘制格子
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line( 67, 200,  67, -200)
    line(-200, -67, 200, -67)
    line(-200,  67, 200,  67)

# 画 X
def drawx(x, y):
    """Draw X player in blue, width=4."""
    color('blue')
    width(4)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

# 画 O
def drawo(x, y):
    """Draw O player in red, width=4."""
    up()
    goto(x + 67, y + 5)
    down()
    color('red')
    width(4)
    circle(62)

# 将点击坐标归整到格子左下角
def floor(value):
    return ((value + 200) // 133) * 133 - 200

# 检测胜利
def check_win():
    b = state['board']
    # 行、列检测
    for i in range(3):
        if b[i][0] is not None and b[i][0] == b[i][1] == b[i][2]:
            return b[i][0]
        if b[0][i] is not None and b[0][i] == b[1][i] == b[2][i]:
            return b[0][i]
    # 对角线
    if b[0][0] is not None and b[0][0] == b[1][1] == b[2][2]:
        return b[0][0]
    if b[0][2] is not None and b[0][2] == b[1][1] == b[2][0]:
        return b[0][2]
    # 平局
    if all(all(cell is not None for cell in row) for row in b):
        return -1
    return None

def evaluate():
    """胜利时得分：电脑 O 赢 +1，人 X 赢 -1，平局或未结束 0"""
    winner = check_win()
    if winner == 1:   # O (电脑)
        return +1
    if winner == 0:   # X (人)
        return -1
    return 0          # 平局 or 未结束

def minimax(is_maximizing):
    """Minimax 递归，返回 (最佳分值, (row, col) 最佳落子)"""
    score = evaluate()
    if score != 0 or all(all(cell is not None for cell in row) for row in state['board']):
        # 终止：有人赢或满盘
        return score, None

    if is_maximizing:
        best = (-2, None)  # 初始化为比最小值还低
        for r in range(3):
            for c in range(3):
                if state['board'][r][c] is None:
                    state['board'][r][c] = 1  # 电脑落 O
                    val, _ = minimax(False)
                    state['board'][r][c] = None
                    if val > best[0]:
                        best = (val, (r, c))
        return best
    else:
        worst = (2, None)   # 初始化为比最大值还高
        for r in range(3):
            for c in range(3):
                if state['board'][r][c] is None:
                    state['board'][r][c] = 0  # 玩家落 X
                    val, _ = minimax(True)
                    state['board'][r][c] = None
                    if val < worst[0]:
                        worst = (val, (r, c))
        return worst

# 落子回调
def tap(x, y):
    if state['game_over']:
        return

    # 计算格子索引
    fx = floor(x)
    fy = floor(y)
    col = int((fx + 200) // 133)
    row = int((fy + 200) // 133)

    # 已有落子则忽略
    if state['board'][row][col] is not None:
        return

    # 当前玩家落子
    player = state['player']
    draw = drawx if player == 0 else drawo
    draw(fx, fy)
    update()
    state['board'][row][col] = player

    # 检查胜利
    result = check_win()
    if result is not None:
        state['game_over'] = True
        penup()
        goto(0, 0)
        color('green')
        if result == 0:
            write("You Win!", align='center', font=('Arial', 24, 'bold'))
        elif result == 1:
            write("Computer Wins!", align='center', font=('Arial', 24, 'bold'))
        else:
            write("Draw!", align='center', font=('Arial', 24, 'bold'))
        return

    # 切换玩家
    state['player'] = 1 - player

    # 如果轮到电脑，就随机落子
    if state['player'] == 1:
        _, move = minimax(True)       # True 表示电脑层 (maximizing)
        r, c = move
        # 计算该格左下角坐标
        fx_ai = c*133 - 200
        fy_ai = r*133 - 200
        # 延迟一点，看起来更自然
        ontimer(lambda: tap(fx_ai + 1, fy_ai + 1), 200)

# 主流程
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()