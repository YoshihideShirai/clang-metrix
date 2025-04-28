from analyzer.parser import extract_functions

def test_extract_functions(tmp_path):
    # Create a temporary C file
    c_file_content = """
    #include <stdio.h>

    void hello() {
        printf("Hello, World!\\n");
    }

    int add(int a, int b) {
        return a + b;
    }
    """
    c_file_path = tmp_path / "test.c"
    c_file_path.write_text(c_file_content)

    # Call the function to test
    functions = extract_functions(str(c_file_path))

    # Assert the results
    assert len(functions) == 2
    assert functions[0].spelling == "hello"
    assert functions[1].spelling == "add"
