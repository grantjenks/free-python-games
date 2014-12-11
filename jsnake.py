"""
# JSnake - Convert Python to Javascript as JSnake

# Todo

* Draw fonts
* Use Google's Traceur compiler for ES6 to ES5 cross-compilation.
  * Example in repos/traceur-compiler/out
  * Commands:
    ../traceur --out nibbles.js --script nibbles.es6.js
    python -m SimpleHTTPServer
    # open http://127.0.0.1:8000/jsnake.html
* Create source maps to help with debugging!
  * https://github.com/mozilla/source-map
"""

import sys
import ast
import argparse
from itertools import count
from flask import Flask, request, Response

parser = argparse.ArgumentParser(description='jsnake to javascript translator')
parser.add_argument('--translate')

Counter = count()

class JSnakeVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(JSnakeVisitor, self).__init__(*args, **kwargs)
        self._indent = 0
        self._parts = []
        self._counter = Counter

    def result(self):
        return ''.join(self._parts)

    def append(self, value):
        self._parts.append(value)

    def temp(self):
        return '__temp{0}'.format(next(self._counter))

    def indent(self):
        self._parts.append(' ' * self._indent)

    def statement(self, value):
        self.indent()
        self._parts.append(value);

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node)

    def visit_Module(self, node):
        self.statement('function* __jsnake_prog() {\n')
        self._indent += 4
        self.generic_visit(node)
        self._indent -= 4
        self.statement('}\n')

    visit_alias = ast.NodeVisitor.generic_visit
    visit_BinOp = ast.NodeVisitor.generic_visit
    visit_Index = ast.NodeVisitor.generic_visit

    def visit_Delete(self, node):
        self.indent()
        subscript = node.targets[0]
        self.visit(subscript.value)
        self.append('.splice(')
        self.visit(subscript.slice)
        self.append(', 1);\n')

    def visit_Expr(self, node):
        self.indent()
        self.generic_visit(node)
        self.append(';\n')

    def visit_ListComp(self, node):
        temp = self.temp()
        self.append('(function () {{ {0} = []; '.format(temp))
        for generator in node.generators:
            loop_temp = self.temp()
            self.append('for ({0} = __jsnake_iter('.format(loop_temp))
            self.visit(generator.iter)
            self.append('); {0}.has_next();) {{ '.format(loop_temp))
            self.visit(generator.target)
            self.append(' = {0}.next(); '.format(loop_temp))
        self.append('{0}.push('.format(temp))
        self.visit(node.elt)
        self.append('); ')
        for generator in node.generators:
            self.append('}')
        self.append(' return {0}; }})()'.format(temp))

    def visit_Add(self, node): self.append(' + ')
    def visit_Sub(self, node): self.append(' - ')
    def visit_Mult(self, node): self.append(' * ')
    def visit_Div(self, node): self.append(' / ')
    def visit_Mod(self, node): self.append(' % ')

    def visit_Eq(self, node): self.append(' == ')
    def visit_NotEq(self, node): self.append(' != ')
    def visit_Lt(self, node): self.append(' < ')
    def visit_LtE(self, node): self.append(' <= ')
    def visit_Gt(self, node): self.append(' > ')
    def visit_GtE(self, node): self.append(' >= ')
    def visit_Is(self, node): self.append(' == ')

    def visit_And(self, node): self.append(' && ')
    def visit_Or(self, node): self.append(' || ')

    def visit_Continue(self, node): self.statement('continue;\n')

    def visit_Compare(self, node):
        if isinstance(node.ops[0], ast.In):
            self.append('__jsnake_in(')
            self.visit(node.left)
            self.append(', ')
            self.visit(node.comparators[0])
            self.append(')')
        elif isinstance(node.ops[0], ast.Eq):
            self.append('__jsnake_cmp(')
            self.visit(node.left)
            self.append(', ')
            self.visit(node.comparators[0])
            self.append(', ')
            self.append('__jsnake_op.eq')
            self.append(')')
        else:
            self.generic_visit(node)

    def visit_Subscript(self, node):
        self.visit(node.value)
        self.append('[__jsnake_idx(')
        self.visit(node.value)
        self.append(', ')
        self.visit(node.slice)
        self.append(')]')

    def visit_BoolOp(self, node):
        for idx, value in enumerate(node.values):
            self.append('(')
            self.visit(value)
            self.append(')')
            if idx < len(node.values) - 1:
                self.visit(node.op)

    def visit_Assign(self, node):
        if len(node.targets) == 1 and not isinstance(node.targets[0], ast.Tuple):
            self.indent()
            if isinstance(node.targets[0], ast.Name):
                self.append('var ')
            self.visit(node.targets[0])
            self.append(' = ')
            self.visit(node.value)
            self.append(';\n')
            return

        temp = self.temp()
        self.indent()
        self.append('{0} = '.format(temp))
        self.visit(node.value)
        self.append(';\n')
        for target in reversed(node.targets):
            if isinstance(target, ast.Tuple):
                for idx, name in enumerate(target.elts):
                    self.statement('{0} = {1}[{2}];\n'.format(name.id, temp, idx))
            elif isinstance(target, ast.Name):
                self.statement('{0} = {1};\n'.format(target.id, temp))

    def visit_Num(self, node):
        self.append('{0}'.format(node.n))
        self.generic_visit(node)

    def visit_Call(self, node):
        self.visit(node.func)
        self.append('(')
        for idx, arg in enumerate(node.args):
            self.visit(arg)
            if idx < len(node.args) - 1:
                self.append(', ')
        self.append(')')

    def visit_Attribute(self, node):
        self.visit(node.value)
        self.append('.')
        self.append(node.attr)

    def visit_Name(self, node):
        consts = {
            'None': 'null',
            'False': 'false',
            'True': 'true'
        }
        self.append(consts.get(node.id, node.id))

    def visit_For(self, node):
        temp = self.temp()
        self.statement('for (var {0} = __jsnake_iter('.format(temp))
        self.visit(node.iter)
        self.append('); {0}.has_next();) {{\n'.format(temp))
        self._indent += 4
        self.statement('yield;\n');
        self.indent()
        self.visit(node.target)
        self.append(' = {0}.next();\n'.format(temp))
        for stmt in node.body:
            self.visit(stmt)
        self.statement('yield;\n')
        self._indent -= 4
        self.statement('}\n')

    def visit_If(self, node):
        self.statement('if (')
        self.visit(node.test)
        self.append(') {\n')
        self._indent += 4
        for stmt in node.body:
            self.visit(stmt)
        self._indent -= 4
        self.statement('} else {\n')
        self._indent += 4
        for stmt in node.orelse:
            self.visit(stmt)
        self._indent -= 4
        self.statement('}\n')

    def visit_Tuple(self, node):
        self.append('[')
        for idx, child in enumerate(node.elts):
            self.visit(child)
            if idx < len(node.elts) - 1:
                self.append(', ')
        self.append(']')

    def visit_Str(self, node):
        self.append(repr(node.s))
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.statement('{0} = __jsnake_lib.{0};\n'.format(alias.name))
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # todo:
        # from pygame.locals import *
        for alias in node.names:
            name = alias.name if alias.asname is None else alias.asname
            self.statement('{0} = __jsnake_lib.{1}.{2};\n'.format(name, node.module, alias.name))

args = parser.parse_args()

if args.translate:
    with open(args.translate) as fptr:
        module = ast.parse(fptr.read())

    visitor = JSnakeVisitor()

    visitor.visit(module)

    print visitor.result()

    sys.exit(0)

app = Flask(__name__)

@app.route('/jsnake')
def jsnake():
    uri = request.args.get('file')
    with open(uri) as fptr:
        module = ast.parse(fptr.read())
    visitor = JSnakeVisitor()
    visitor.visit(module)
    return Response(visitor.result(), mimetype='text/javascript')

@app.route('/jsnake.js')
def jsnake_js():
    with open('jsnake.js') as fptr:
        return Response(fptr.read(), mimetype='text/javascript')

@app.route('/jsnake.html')
def nibbles_html():
    with open('jsnake.html') as fptr:
        return fptr.read()

if __name__ == '__main__':
    app.run(debug=True)
