# clang-metrix

**clang-metrix** is a code analysis tool that uses Clang and Python to evaluate the complexity and maintainability of C functions.

It computes the following metrics:

- ✅ Cyclomatic Complexity  
- ✅ Cognitive Complexity  
- ✅ Halstead Volume  
- ✅ Maintainability Index  
- ✅ Lines of Code (excluding comments)  
- ✅ Report output in HTML or JSON (GitHub-style with sortable tables)

---

## 🚀 Usage

```bash
docker run --rm -v "$PWD:/data" yoshihideshirai/clang-metrix --format html --output /data/report.html /data/examples/example.c
```

### 🔧 Options

| Option               | Description                                        |
|----------------------|----------------------------------------------------|
| `--format html\|json`| Output format (`html` by default)                 |
| `--output FILE`      | Output file name (`report.html` or `report.json`) |

Example:
```bash
docker run --rm -v "$PWD:/data" yoshihideshirai/clang-metrix /data/example.c --format json --output /data/report.json
```

---

## 🧪 Testing

Run unit tests using `pytest`:

```bash
pytest
```

---

## 📝 License

MIT License

---

## 🙋 Contributions

Feel free to open issues or submit pull requests to improve this project!
