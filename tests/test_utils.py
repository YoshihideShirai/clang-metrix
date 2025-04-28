from analyzer.utils import is_c_file

def test_is_c_file_with_c_extension():
    assert is_c_file("example.c") is True

def test_is_c_file_with_h_extension():
    assert is_c_file("example.h") is True

def test_is_c_file_with_non_c_extension():
    assert is_c_file("example.txt") is False

def test_is_c_file_with_no_extension():
    assert is_c_file("example") is False

def test_is_c_file_with_uppercase_extension():
    assert is_c_file("example.C") is False
    assert is_c_file("example.H") is False

def test_is_c_file_with_mixed_case_extension():
    assert is_c_file("example.cH") is False
    assert is_c_file("example.hC") is False