'\nNibbles the video game.\n\nCopyright (c) 2014 Grant Jenks\nhttp://www.grantjenks.com/\n\nExercises\n1. Change the colors.\n2. Increase the size of the playing area.\n3. Change the snake speed.\n4. Make the food jump randomly.\n5. Change the controls to (w, a, s, d)\n6. Add diagonals.\n7. Add high score.\n8. Make the game boundaries into walls.\n';
sys = library.sys;
pygame = library.pygame;
randrange = library.random.randrange;
* = library.pygame.locals.*;
count = library.itertools.count;
__temp0 = [480, 480];
width = __temp0[0];
height = __temp0[1];
size = __temp0;
__temp1 = [[0, -10], [10, 0], [0, 10], [-10, 0]];
up = __temp1[0];
right = __temp1[1];
down = __temp1[2];
left = __temp1[3];
pygame.init();
clock = pygame.time.Clock();
screen = pygame.display.set_mode(size);
font = pygame.font.Font(null, 14);
__temp2 = [down, null, false];
snake_dir = __temp2[0];
food = __temp2[1];
dead = __temp2[2];
snake = (function () { __temp3 = []; for (__temp4 = __iter(range(20)); __temp4.has_next();) { value = __temp4.next(); __temp3.append(pygame.Rect(10, 10 + value * 10, 10, 10)); } return __temp3; })();
__temp5 = [[255, 255, 255], [0, 0, 0]];
foreground = __temp5[0];
background = __temp5[1];
for (__temp6 = __iter(count()); __temp6.has_next();) {
    counter = __temp6.next();
    clock.tick(min(5 + len(snake) / 4, 30));
    event = pygame.event.poll();
    if (event.type == pygame.QUIT) {
        pygame.quit();
        sys.exit();
    } else {
        if (event.type == KEYDOWN) {
            if ((event.key == K_UP) && (snake_dir != down)) {
                snake_dir = up;
            } else {
                if ((event.key == K_RIGHT) && (snake_dir != left)) {
                    snake_dir = right;
                } else {
                    if ((event.key == K_DOWN) && (snake_dir != up)) {
                        snake_dir = down;
                    } else {
                        if ((event.key == K_LEFT) && (snake_dir != right)) {
                            snake_dir = left;
                        } else {
                            if (event.key == K_r) {
                                __temp7 = [down, null, false];
                                snake_dir = __temp7[0];
                                food = __temp7[1];
                                dead = __temp7[2];
                                snake = (function () { __temp8 = []; for (__temp9 = __iter(range(20)); __temp9.has_next();) { value = __temp9.next(); __temp8.append(pygame.Rect(10, 10 + value * 10, 10, 10)); } return __temp8; })();
                                __temp10 = [[255, 255, 255], [0, 0, 0]];
                                foreground = __temp10[0];
                                background = __temp10[1];
                            } else {
                                if (event.key == K_q) {
                                    pygame.event.post(pygame.event.Event(QUIT));
                                } else {
                                }
                            }
                        }
                    }
                }
            }
        } else {
        }
    }
    if (dead) {
        continue;
    } else {
    }
    next = snake[__index(snake, -1)].move(snake_dir);
    if (next.left < 0) {
        next.left = width - 10;
    } else {
    }
    if (next.left >= width) {
        next.left = 0;
    } else {
    }
    if (next.top < 0) {
        next.top = height - 10;
    } else {
    }
    if (next.top >= height) {
        next.top = 0;
    } else {
    }
    if (__in(next, snake)) {
        dead = true;
        __temp11 = [background, foreground];
        foreground = __temp11[0];
        background = __temp11[1];
    } else {
        snake.append(next);
        if (next == food) {
            food = null;
        } else {
            snake.splice(0, 1);
        }
    }
    if ((food == null) && (counter % 50 == 0)) {
        food = pygame.Rect(randrange(48) * 10, randrange(48) * 10, 10, 10);
    } else {
    }
    screen.fill(background);
    for (__temp12 = __iter(snake); __temp12.has_next();) {
        rect = __temp12.next();
        pygame.draw.rect(screen, foreground, rect);
    }
    if (food) {
        pygame.draw.rect(screen, foreground, food);
    } else {
    }
    surface = font.render(str(len(snake)), true, foreground);
    screen.blit(surface, [0, 0]);
    pygame.display.flip();
}

