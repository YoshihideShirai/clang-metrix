from jinja2 import Environment, FileSystemLoader
import os

def generate_html_report(results, output_path="report.html"):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html.j2')
    html = template.render(results=results)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
