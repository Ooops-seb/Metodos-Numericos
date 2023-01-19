import ast

def check_syntax(funcion_str):
    try:
        ast.parse(funcion_str)
        return True
    except SyntaxError:
        return False