import pytest
from analyzer.parser import extract_functions
from analyzer.metrics import compute_metrics

# テスト用のCコード
TEST_C_CODE = """
#include <stdio.h>

void simple() {
    // This is a simple function
    printf("Hello\\n");
}

void with_if(int x) {
    if (x > 0) {
        printf("Positive\\n");
    } else {
        printf("Non-positive\\n");
    }
}

void nested_loops(int n) {
    for (int i = 0; i < n; i++) {
        while (i < n/2) {
            if (i % 2 == 0) {
                printf("Even\\n");
            }
        }
    }
}
"""


@pytest.fixture(scope="module")
def parsed_functions(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("data")
    c_file = tmp_path / "test.c"
    c_file.write_text(TEST_C_CODE)

    # clang初期化
    functions = extract_functions(str(c_file))
    return {f.spelling: f for f in functions}


def test_simple(parsed_functions):
    metrics = compute_metrics(parsed_functions["simple"])
    assert metrics["cyclomatic"] == 1
    assert metrics["cognitive"] == 0
    assert metrics["loc"] == 3
    assert metrics["mi"] > 0


def test_with_if(parsed_functions):
    metrics = compute_metrics(parsed_functions["with_if"])
    assert metrics["cyclomatic"] == 3
    assert metrics["cognitive"] == 5
    assert metrics["loc"] == 7
    assert metrics["mi"] > 66
    assert metrics["mi"] < 67


def test_nested_loops(parsed_functions):
    metrics = compute_metrics(parsed_functions["nested_loops"])
    assert metrics["cyclomatic"] == 9
    assert metrics["cognitive"] == 41
    assert metrics["halstead"] > 0
    assert metrics["loc"] == 9
    assert metrics["mi"] > 61
    assert metrics["mi"] < 62
