pygame_to_js = {
    start: function (canvas_id, script_name) {
        var worker = new Worker('http://127.0.0.1:5000/pygame_to_js?uri=' + script_name);
    }
}
