"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector

# 蛇身体列表，初始有一节 / Snake body list, starts with one segment
snake = [vector(10, 0)]

# 移动方向 / Movement direction
aim = vector(0, -10)

# 普通食物位置 / Regular food position
food = vector(0, 0)

# 超级食物位置（None 表示不存在）/ Super food position (None = not on map)
super_food = None

# 超级食物是否可见（用于闪烁）/ Whether the super food is visible (flashing effect)
super_food_active = False

# 超级食物倒计时（单位：10ms）/ Countdown for super food (in units of 100ms)
super_food_timer = 0

# 已吃普通食物数量（每5个触发超级食物）/ Normal food count (trigger super food every 5)
normal_food_count = 0

# 闪烁状态控制 / Flashing toggle
flash_state = True


def change(x, y):
    """改变蛇的移动方向 / Change snake movement direction"""
    aim.x = x
    aim.y = y


def inside(head):
    """判断是否在游戏边界内 / Check if the head is within bounds"""
    return -200 < head.x < 190 and -200 < head.y < 190


def place_food_randomly():
    """生成新的食物位置 / Place food at random position"""
    return vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)


def draw():
    """绘制蛇、普通食物、超级食物 / Draw snake, food, and super food"""
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')

    # 如果有超级食物并且当前处于激活状态则绘制 / Draw super food if active
    if super_food and super_food_active:
        color = 'gold' if flash_state else 'orange'
        square(super_food.x, super_food.y, 9, color)

    update()


def move():
    """控制蛇移动、吃食物和碰撞检测 / Handle snake movement, food eating and collision"""
    global food, super_food, normal_food_count
    global super_food_timer, super_food_active

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('普通食物 +1 / Normal food +1')
        food = place_food_randomly()
        normal_food_count += 1

        # 每吃5个生成一个超级食物 / Spawn super food every 5 normal foods
        if normal_food_count % 5 == 0:
            super_food = place_food_randomly()
            super_food_active = True
            super_food_timer = 50  # 5秒 = 50 * 100ms
    elif super_food and head == super_food:
        print('超级食物 +2！/ Super food +2!')
        snake.append(snake[-1].copy())  # 额外加一节 / One extra segment
        super_food = None
        super_food_active = False
    else:
        snake.pop()

    draw()
    ontimer(move, 100)


def tick_super_food():
    """定时器函数：控制超级食物闪烁和超时消失 / Super food flash and timeout control"""
    global flash_state, super_food_timer, super_food, super_food_active

    if super_food_active:
        flash_state = not flash_state  # 颜色闪烁 / Toggle color

        super_food_timer -= 1
        if super_food_timer <= 0:
            print('超级食物消失 / Super food expired')
            super_food = None
            super_food_active = False

    draw()
    ontimer(tick_super_food, 100)


# 初始化窗口和控制 / Game window and controls
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# 启动主循环 / Start main game loop
move()
tick_super_food()
done()