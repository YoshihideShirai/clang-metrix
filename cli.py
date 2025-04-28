import argparse
import os
import json
from src.analyzer.parser import extract_functions
from src.analyzer.metrics import compute_metrics
from src.analyzer.reporter import generate_html_report

def main():
    parser = argparse.ArgumentParser(description="C Complexity Analyzer")
    parser.add_argument("file", help="C source file path")
    parser.add_argument("--format", "-f", choices=["html", "json"], default="html", help="Output format (html or json)")
    parser.add_argument("--output", "-o", help="Output file path (auto-set by format if omitted)")

    args = parser.parse_args()

    # 出力パスの自動補完
    if args.output:
        output_path = args.output
    else:
        ext = "html" if args.format == "html" else "json"
        output_path = f"report.{ext}"

    # 入力ファイル存在チェック
    if not os.path.isfile(args.file):
        print(f"❌ Error: file not found: {args.file}")
        return

    # 複雑度計算
    results = []
    for func in extract_functions(args.file):
        metrics = compute_metrics(func)
        results.append(metrics)

    # 出力形式に応じた処理
    if args.format == "html":
        generate_html_report(results, output_path=output_path)
        print(f"✔ HTML report saved to: {output_path}")
    elif args.format == "json":
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"✔ JSON report saved to: {output_path}")

if __name__ == "__main__":
    main()
