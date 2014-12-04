// PyGame to Javascript Worker Library

var in_queue = [];
var out_queue = [];

onmessage = function (evt) {
    in_queue.append(JSON.parse(evt.data));
}

function process_queue() {
    for (var pos = 0; pos < out_queue.length; pos += 1) {
        var msg = out_queue[pos];
        postMessage(JSON.stringify(msg));
    }
    out_queue.slice(0);
    setTimeout(process_queue, 0);
}

process_queue()
