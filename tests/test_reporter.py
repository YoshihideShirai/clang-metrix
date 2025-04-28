import pytest
from analyzer.reporter import generate_html_report
from jinja2 import FileSystemLoader

@pytest.fixture
def dummy_results():
    return [
        {
            "name": "func1",
            "loc": 10,
            "cyclomatic": 3,
            "cognitive": 2,
            "halstead": 45.3,
            "mi": 76.2
        },
        {
            "name": "func2",
            "loc": 20,
            "cyclomatic": 5,
            "cognitive": 4,
            "halstead": 120.0,
            "mi": 55.5
        }
    ]

@pytest.fixture
def template_dir(tmp_path):
    templates_path = tmp_path / "templates"
    templates_path.mkdir()
    template_file = templates_path / "report.html.j2"
    template_file.write_text("""
    <html>
    <body>
        <table>
        {% for r in results %}
            <tr><td>{{ r.name }}</td><td>{{ r.mi }}</td></tr>
        {% endfor %}
        </table>
    </body>
    </html>
    """)
    return templates_path

def test_generate_html_report(tmp_path, dummy_results, template_dir, monkeypatch):
    output_file = tmp_path / "output.html"

    # monkeypatch templates/ に置き換える
    monkeypatch.setattr("analyzer.reporter.FileSystemLoader", lambda _: FileSystemLoader(str(template_dir)))


    # 実行
    generate_html_report(dummy_results, output_path=output_file)

    # 検証: 出力ファイルが存在し、内容に関数名とMIが入っている
    assert output_file.exists()
    content = output_file.read_text()
    assert "func1" in content
    assert "76.2" in content
    assert "func2" in content
    assert "55.5" in content
