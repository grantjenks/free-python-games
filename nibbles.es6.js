function* __jsnake_prog() {
    '\nNibbles the video game.\n\nCopyright (c) 2014 Grant Jenks\nhttp://www.grantjenks.com/\n\nExercises\n1. Change the colors.\n2. Increase the size of the playing area.\n3. Change the snake speed.\n4. Make the food jump randomly.\n5. Change the controls to (w, a, s, d)\n6. Add diagonals.\n7. Add high score.\n8. Make the game boundaries into walls.\n';
    sys = __jsnake_lib.sys;
    pygame = __jsnake_lib.pygame;
    randrange = __jsnake_lib.random.randrange;
    KEYDOWN = __jsnake_lib.pygame.locals.KEYDOWN;
    K_UP = __jsnake_lib.pygame.locals.K_UP;
    K_RIGHT = __jsnake_lib.pygame.locals.K_RIGHT;
    K_DOWN = __jsnake_lib.pygame.locals.K_DOWN;
    K_LEFT = __jsnake_lib.pygame.locals.K_LEFT;
    QUIT = __jsnake_lib.pygame.locals.QUIT;
    K_r = __jsnake_lib.pygame.locals.K_r;
    K_q = __jsnake_lib.pygame.locals.K_q;
    count = __jsnake_lib.itertools.count;
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
    var clock = pygame.time.Clock();
    var screen = pygame.display.set_mode(size);
    var font = pygame.font.Font(null, 14);
    __temp2 = [down, null, false];
    snake_dir = __temp2[0];
    food = __temp2[1];
    dead = __temp2[2];
    var snake = (function () { __temp3 = []; for (__temp4 = __jsnake_iter(range(20)); __temp4.has_next();) { value = __temp4.next(); __temp3.push(pygame.Rect(10, 10 + value * 10, 10, 10)); } return __temp3; })();
    __temp5 = [[255, 255, 255], [0, 0, 0]];
    foreground = __temp5[0];
    background = __temp5[1];
    for (var __temp6 = __jsnake_iter(count()); __temp6.has_next();) {
        yield;
        counter = __temp6.next();
        clock.tick(min(5 + len(snake) / 4, 30));
        var event = pygame.event.poll();
        if (__jsnake_cmp(event.type, QUIT, __jsnake_op.eq)) {
            pygame.quit();
            sys.exit();
        } else {
            if (__jsnake_cmp(event.type, KEYDOWN, __jsnake_op.eq)) {
                if ((__jsnake_cmp(event.key, K_UP, __jsnake_op.eq)) && (snake_dir != down)) {
                    var snake_dir = up;
                } else {
                    if ((__jsnake_cmp(event.key, K_RIGHT, __jsnake_op.eq)) && (snake_dir != left)) {
                        var snake_dir = right;
                    } else {
                        if ((__jsnake_cmp(event.key, K_DOWN, __jsnake_op.eq)) && (snake_dir != up)) {
                            var snake_dir = down;
                        } else {
                            if ((__jsnake_cmp(event.key, K_LEFT, __jsnake_op.eq)) && (snake_dir != right)) {
                                var snake_dir = left;
                            } else {
                                if (__jsnake_cmp(event.key, K_r, __jsnake_op.eq)) {
                                    __temp7 = [down, null, false];
                                    snake_dir = __temp7[0];
                                    food = __temp7[1];
                                    dead = __temp7[2];
                                    var snake = (function () { __temp8 = []; for (__temp9 = __jsnake_iter(range(20)); __temp9.has_next();) { value = __temp9.next(); __temp8.push(pygame.Rect(10, 10 + value * 10, 10, 10)); } return __temp8; })();
                                    __temp10 = [[255, 255, 255], [0, 0, 0]];
                                    foreground = __temp10[0];
                                    background = __temp10[1];
                                } else {
                                    if (__jsnake_cmp(event.key, K_q, __jsnake_op.eq)) {
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
        var next = snake[__jsnake_idx(snake, -1)].move(snake_dir);
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
        if (__jsnake_in(next, snake)) {
            var dead = true;
            __temp11 = [background, foreground];
            foreground = __temp11[0];
            background = __temp11[1];
        } else {
            snake.append(next);
            if (__jsnake_cmp(next, food, __jsnake_op.eq)) {
                var food = null;
            } else {
                snake.splice(0, 1);
            }
        }
        if ((food == null) && (__jsnake_cmp(counter % 50, 0, __jsnake_op.eq))) {
            var food = pygame.Rect(randrange(48) * 10, randrange(48) * 10, 10, 10);
        } else {
        }
        screen.fill(background);
        for (var __temp12 = __jsnake_iter(snake); __temp12.has_next();) {
            yield;
            rect = __temp12.next();
            pygame.draw.rect(screen, foreground, rect);
            yield;
        }
        if (food) {
            pygame.draw.rect(screen, foreground, food);
        } else {
        }
        var surface = font.render(str(len(snake)), true, foreground);
        screen.blit(surface, [0, 0]);
        pygame.display.flip();
        yield;
    }
}

