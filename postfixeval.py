from stack import *

def postfixEval(expr):
    s = Stack()
    operators = '+-*/%'
    operands = '0123456789'
    for c in expr:
        if c in operators:
            try:
                a = s.pop()
                b = s.pop()
            except Exception as e:
                return 'Malformed Postfix Expression'
            r = eval(b, a, c)
            s.push(r)
        elif c in operands:
            s.push(int(c))
    
    if len(s) != 1:
        return 'Malformed Postfix Expression'
    return s.pop()

def eval(op1, op2, oper):
    if oper == '+':
        return op1 + op2
    elif oper == '-':
        return op1 - op2
    elif oper == '*':
        return op1 * op2
    elif oper == '/':
        return op1 / op2
    elif oper == '%':
        return op1 % op2
