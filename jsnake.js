////////////////////////////////////////////////////////////////////////////////
// JSnake Library
////////////////////////////////////////////////////////////////////////////////

var __jsnake_consume = [];
var __jsnake_produce = [];

var __jsnake_lib = {
    print: function (values) {
        _(values).each(function (value) {
            __jsnake_term.write(value.toString());
        });
    },
    math: {
        sqrt: function* (value) {
            yield Math.sqrt(value);
        }
    },
    pygame: {
        init: function* () {
            __jsnake_div = document.getElementById('jsnake');
        },
        display: {
            set_mode: function* (size) {
                var screen = document.createElement('canvas');
                screen.width = size[0];
                screen.height = size[1];
                screen.setAttribute('tabindex', 1);
                __jsnake_div.appendChild(screen);
                setTimeout(function () {
                    $('#jsnake > canvas').css('outline', 'none').focus();
                }, 100);
                yield* __jsnake_lib.pygame.Surface(size, screen);
            },
            flip: function* () {
                __jsnake_flip = true;
                yield;
            }
        },
        font: {
            Font: function* (name, size) {
                yield {
                    render: function* (text, antialias, color) {
                        yield {
                            kind: 'text',
                            text: text,
                            size: size,
                            name: name,
                            antialias: antialias,
                            color: color
                        }
                    }
                };
            },
        },
        Surface: function* (size, canvas) {
            yield {
                width: size[0],
                height: size[1],
                canvas: canvas,
                fill: function* (color) {
                    var ctx = canvas.getContext("2d");
                    ctx.fillStyle = __jsnake_rgb_to_hex(color);
                    ctx.fillRect(0, 0, size[0], size[1]);
                },
                blit: function* (surface, pos) {
                    if (surface.kind == 'text') {
                        var ctx = canvas.getContext("2d");
                        ctx.font = surface.size + "px Monospace";
                        ctx.fillStyle = __jsnake_rgb_to_hex(surface.color);
                        ctx.fillText(surface.text, pos[0], pos[1] + surface.size);
                    } else {
                        throw new Error('unrecognized surface in blit: ' + surface.kind);
                    }
                }
            };
        },
        Rect: function* (left, top, width, height) {
            yield {
                left: left,
                top: top,
                width: width,
                height: height,
                move: function* (direction) {
                    yield* __jsnake_lib.pygame.Rect(
                        this.left + direction[0],
                        this.top + direction[1],
                        this.width,
                        this.height
                    );
                }
            };
        },
        draw: {
            rect: function* (surface, color, rect) {
                var ctx = surface.canvas.getContext("2d");
                ctx.fillStyle = __jsnake_rgb_to_hex(color);
                ctx.fillRect(rect.left, rect.top, rect.width, rect.height);
            }
        },
        event: {
            poll: function* () {
                if (__jsnake_consume.length == 0) {
                    yield* __jsnake_lib.pygame.event.Event(null, null);
                } else {
                    var event = __jsnake_consume[0];
                    __jsnake_consume.splice(0, 1);
                    yield event;
                }
            },
            Event: function* (kind, key) {
                yield {
                    type: kind,
                    key: key
                }
            },
            post: function* (event) {
                __jsnake_produce.push(event);
            }
        },
        locals: {
            KEYDOWN: 2,
            QUIT: 12,
            K_q: 113,
            K_r: 114,
            K_UP: 273,
            K_DOWN: 274,
            K_RIGHT: 275,
            K_LEFT: 276
        },
        time: {
            Clock: function* () {
                yield {
                    tick: function* (fps) {
                        if (__jsnake_tick) {
                            __jsnake_flip = true;
                        }
                        __jsnake_fps = fps;
                        __jsnake_tick = true;
                    }
                }
            }
        },
        quit: function* () {
            __jsnake_quit = true;
        }
    },
    random: {
        randrange: function* (value) {
            yield Math.floor(Math.random() * value);
        }
    },
    itertools: {
        count: function* () {
            for (var value = 0; true; value += 1) {
                yield value;
            }
        }
    },
    sys: {
        exit: function* () {
            // todo
        }
    }
}

////////////////////////////////////////////////////////////////////////////////
// Python Built-ins
////////////////////////////////////////////////////////////////////////////////

function* str(obj) {
    yield obj.toString();
}

function* len(arr) {
    yield arr.length;
}

function* min(left, right) {
    yield (left < right ? left : right);
}

function* range(limit) {
    for (var value = 0; value < limit; value += 1) {
        yield value;
    }
}        

function* input(text) {
    __jsnake_term.write(text);
    while (__jsnake_term_buffer.substr(-1) != '\n') {
        __jsnake_flip = true;
        yield;
    }
    yield eval(__jsnake_term_read());
}

function* raw_input(text) {
    __jsnake_term.write(text);
    while (__jsnake_term_buffer.substr(-1) != '\n') {
        __jsnake_flip = true;
        yield;
    }
    yield __jsnake_term_read().slice(0, -1);
}

////////////////////////////////////////////////////////////////////////////////
// JSnake Helpers
////////////////////////////////////////////////////////////////////////////////

__jsnake_op = {
    eq: function (lhs, rhs) {
        if (_.isPlainObject(lhs) && _.isPlainObject(rhs)) {
            return _.isEqual(lhs, rhs, function (alpha, beta) {
                if (_.isFunction(alpha) && _.isFunction(beta)) {
                    return true;
                } else {
                    return undefined;
                }
            });
        } else {
            return _.isEqual(lhs, rhs);
        }
    },
    ne: null,
    gt: null,
    ge: null,
    lt: null,
    le: null
}

function __jsnake_cmp(lhs, rhs, op) {
    return op(lhs, rhs);
}

function __jsnake_in(val, arr) {
    for (var pos = 0; pos < arr.length; pos += 1) {
        if (__jsnake_cmp(val, arr[pos], __jsnake_op.eq)) {
            return true;
        }
    }
    return false;
}

function __jsnake_idx(arr, val) {
    return (val >= 0 ? val : val + arr.length);
}

function __jsnake_rgb_to_hex(rgb) {
    function toHex(val) {
        var hex = val.toString(16);
        return (hex.length == 1 ? '0' + hex : hex);
    }
    return '#' + toHex(rgb[0]) + toHex(rgb[1]) + toHex(rgb[2]);
}

Array.prototype.append = function* (value) {
    this.push(value);
}

////////////////////////////////////////////////////////////////////////////////
// JSnake event handlers
////////////////////////////////////////////////////////////////////////////////

$('#jsnake').on('keydown', function (event) {
    var key = 0;
    var pygame = __jsnake_lib.pygame;
    var locals = pygame.locals;

    switch (event.which) {
    case 37:
        key = locals.K_LEFT;
        break;
    case 38:
        key = locals.K_UP;
        break;
    case 39:
        key = locals.K_RIGHT;
        break;
    case 40:
        key = locals.K_DOWN;
        break;
    case 81:
        key = locals.K_q;
        break;
    case 82:
        key = locals.K_r;
        break;
    default:
        console.log('key error: ' + event.which);
    }

    __jsnake_consume.push(pygame.event.Event(locals.KEYDOWN, key).next().value);
});

////////////////////////////////////////////////////////////////////////////////
// JSnake Terminal
////////////////////////////////////////////////////////////////////////////////

__jsnake_term = new Terminal({
    cols: 80,
    rows: 24,
    useStyle: true,
    screenKeys: true,
    cursorBlink: false
});

__jsnake_term.open(document.body);

__jsnake_term.on('data', function(data) {
    console.log('data: ' + data);
    if (data === '\r') {
        __jsnake_term.write('\r');
        __jsnake_term.write('\n');
        __jsnake_term_buffer += '\n';
    } else if (data.charCodeAt() == 127) { // backspace
        __jsnake_term_buffer = __jsnake_term_buffer.substr(
            0,
            __jsnake_term_buffer.length - 1
        );
        __jsnake_term.write('\x1b[D');
        __jsnake_term.write(' ');
        __jsnake_term.write('\x1b[D');
    } else {
        __jsnake_term.write(data);
        __jsnake_term_buffer += data;
    }
});

__jsnake_term_buffer = '';

__jsnake_term_read = function () {
    temp = __jsnake_term_buffer;
    __jsnake_term_buffer = '';
    return temp;
}

////////////////////////////////////////////////////////////////////////////////
// JSnake game loop
////////////////////////////////////////////////////////////////////////////////

__jsnake_inst = __jsnake_prog();
__jsnake_fps = 12;
__jsnake_yield = (new Date()).getTime();
__jsnake_sleep = 0;
__jsnake_result = undefined;
__jsnake_flip = false;
__jsnake_quit = false;
__jsnake_tick = false;

function __jsnake_clear() {
    var result = __jsnake_result;
    __jsnake_result = undefined;
    return result;
}

function __jsnake_run() {
    var start = (new Date()).getTime();
    var frame = 1000 / __jsnake_fps;

    // Handle incoming event queue.

    if (__jsnake_produce.length > 0) {
        var event = __jsnake_produce[0];
        __jsnake_produce.splice(0, 1);

        switch (event.type) {
        case pygame.locals.QUIT:
            __jsnake_quit = true;
            break;
        default:
            console.log('event error: ' + event.kind);
        }
    }

    // Advance instance generator.

    while (!__jsnake_flip && !__jsnake_quit) {
        __jsnake_result = __jsnake_inst.next().value;

        frame = 1000 / __jsnake_fps;
        var now = (new Date()).getTime();

        if ((now - start) > frame) {
            console.log('frame drop');
            break;
        }
    }

    if (__jsnake_quit) {
        return;
    }

    __jsnake_flip = false;
    __jsnake_tick = false;

    frame = 1000 / __jsnake_fps;
    var next = __jsnake_yield + frame;
    var now = (new Date()).getTime();

    __jsnake_sleep = Math.min(frame, Math.max(next - now + __jsnake_sleep, 0));
    __jsnake_yield = (new Date()).getTime();

    setTimeout(__jsnake_run, __jsnake_sleep);
}

__jsnake_run();
