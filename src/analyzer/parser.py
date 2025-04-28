import clang.cindex
from clang.cindex import CursorKind

def extract_functions(file_path):
    index = clang.cindex.Index.create()
    tu = index.parse(file_path, args=['-std=c11'])

    functions = []

    for cursor in tu.cursor.get_children():
        if cursor.kind == CursorKind.FUNCTION_DECL and cursor.is_definition():
            functions.append(cursor)

    return functions
