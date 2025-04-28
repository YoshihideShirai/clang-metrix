from clang.cindex import Config

# Clangのパスを設定（必要に応じて修正）
# Config.set_library_file('/path/to/libclang.so')
Config.set_library_file("/usr/lib/llvm-19/lib/libclang-19.so.1")

