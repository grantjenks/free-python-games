"""
# Convert PyGame Apps to Javascript

# Library Support

library.pygame
"""

import ast
from itertools import count

counter = count()

class PyGameToJSVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(PyGameToJSVisitor, self).__init__(*args, **kwargs)
        self._indent = 0
        self._parts = []
        self._counter = counter

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

    visit_Module = ast.NodeVisitor.generic_visit
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
            self.append('for ({0} = __iter('.format(loop_temp))
            self.visit(generator.iter)
            self.append('); {0}.has_next();) {{ '.format(loop_temp))
            self.visit(generator.target)
            self.append(' = {0}.next(); '.format(loop_temp))
        self.append('{0}.append('.format(temp))
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
            self.append('__in(')
            self.visit(node.left)
            self.append(', ')
            self.visit(node.comparators[0])
            self.append(')')
        else:
            self.generic_visit(node)

    def visit_Subscript(self, node):
        self.visit(node.value)
        self.append('[__index(')
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
        self.statement('for ({0} = __iter('.format(temp))
        self.visit(node.iter)
        self.append('); {0}.has_next();) {{\n'.format(temp))
        self._indent += 4
        self.indent()
        self.visit(node.target)
        self.append(' = {0}.next();\n'.format(temp))
        for stmt in node.body:
            self.visit(stmt)
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
            self.statement('{0} = library.{0};\n'.format(alias.name))
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # todo:
        # from pygame.locals import *
        for alias in node.names:
            name = alias.name if alias.asname is None else alias.asname
            self.statement('{0} = library.{1}.{2};\n'.format(name, node.module, alias.name))

if __name__ == '__main__':
    with open('nibbles.py') as fptr:
        module = ast.parse(fptr.read())

    visitor = PyGameToJSVisitor()

    visitor.visit(module)

    print visitor.result()
