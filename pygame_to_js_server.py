import requests
from pygame_to_js import PyGameToJSVisitor
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/pygame_to_js')
def pygame_to_js():
    uri = request.args.get('uri')
    resp = requests.get(uri)
    visitor = PyGameToJSVisitor()
    visitor.visit(ast.parse(resp.text))
    return Response(visitor.result(), mimetype='text/javascript')

@app.route('/pygame_to_js.js')
def pygame_to_js_js():
    with open('pygame_to_js.js') as fptr:
        return Response(fptr.read(), mimetype='text/javascript')

@app.route('/nibbles.html')
def nibbles_html():
    with open('nibbles.html') as fptr:
        return fptr.read()

if __name__ == '__main__':
    app.run(debug=True)
