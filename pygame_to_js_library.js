var library = {
    pygame: {
        init: function () {},
        display: {
            set_mode: function (size) {},
        },
        font: {
            Font: function (name, size) {},
        },
        Rect: function (left, top, width, height) {},
        event: {
            poll: function () {}
        },
        draw: {},
        event: {
            poll: function () {
                if (in_queue.length == 0) {
                    return library.pygame.event.Event(null, null);
                } else {
                    var event = in_queue[0];
                    in_queue.slice(0, 1);
                    return event;
                }
            },
            Event: function (kind, key) {
                return {
                    type: kind,
                    key: key
                }
            },
            post: function (event) {
                out_queue.append(event);
            }
        },
        quit: function () { }

    },
    itertools: {
        count: function () {
            var curr = 0;
            return {
                has_next: function () { return true; },
                next: function () {
                    var temp = curr;
                    curr += 1;
                    return temp;
                }
            }
        }
    }
}


function len(arr) {
    return arr.length;
}

function min(left, right) {
    return (left < right ? left : right);
}

function range(value) {
    var curr = 0;
    return {
        next: function() {
            var temp = curr;
            curr += 1;
            return temp;
        },
        has_next: function() {
            return (curr < value);
        }
    }
}

function __iter(item) {
    return item;
}

function __in(val, arr) {
    return (arr.index(val) >= 0);
}

function __index(arr, val) {
    return (val >= 0 ? val : val + arr.length);
}
