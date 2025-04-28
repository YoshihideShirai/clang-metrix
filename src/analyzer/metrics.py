import math
from clang.cindex import CursorKind, TokenKind

def compute_metrics(func_cursor):
    cyclomatic = 1
    cognitive = 0
    operators = set()
    operands = set()
    loc = 0
    comments = 0

    tokens = list(func_cursor.get_tokens())
    for token in tokens:
        if token.kind == TokenKind.COMMENT:
            comments += 1
        elif token.kind == TokenKind.KEYWORD or token.kind == TokenKind.PUNCTUATION:
            operators.add(token.spelling)
        elif token.kind == TokenKind.IDENTIFIER or token.kind == TokenKind.LITERAL:
            operands.add(token.spelling)

    loc = func_cursor.extent.end.line - func_cursor.extent.start.line + 1
    loc -= comments

    def walk(node, depth=0):
        nonlocal cyclomatic, cognitive
        for child in node.get_children():
            kind = child.kind
            if kind in (
                CursorKind.IF_STMT,
                CursorKind.FOR_STMT,
                CursorKind.WHILE_STMT,
                CursorKind.CASE_STMT,
                CursorKind.DEFAULT_STMT,
                CursorKind.CXX_TRY_STMT,
                CursorKind.CXX_CATCH_STMT,
                CursorKind.CONDITIONAL_OPERATOR,
                CursorKind.BINARY_OPERATOR,
                CursorKind.DO_STMT,
                CursorKind.SWITCH_STMT,
            ):
                cyclomatic += 1
                cognitive += 1 + depth
            walk(child, depth + 1)

    walk(func_cursor)

    n1 = len(operators)
    n2 = len(operands)
    N1 = sum(1 for t in tokens if t.spelling in operators)
    N2 = sum(1 for t in tokens if t.spelling in operands)
    halstead = (N1 + N2) * math.log2((n1 + n2) or 1)

    try:
        mi = max(0, (171 - 5.2 * math.log(halstead or 1)
                     - 0.23 * cyclomatic - 16.2 * math.log(loc or 1)) * 100 / 171)
    except:
        mi = 0

    return {
        "name": func_cursor.spelling,
        "loc": loc,
        "cyclomatic": cyclomatic,
        "cognitive": cognitive,
        "halstead": halstead,
        "mi": mi
    }
