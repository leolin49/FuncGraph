import sys

import util
from func_cpp import FuncCpp
from func_go import FuncGolang


def print_help():
    print("Source file function call relation visualize:")
    print("Currently supported source file types: \".cpp\", \".go\"")
    print("{} [command] [file path] [command options]".format(sys.argv[0]))
    print("Command: ")
    print("  gen      visualize the [file path] function's call relationship by graph")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    cmd = sys.argv[1].lower()
    if cmd == "gen":
        file_path = sys.argv[2]
        file_type = util.get_file_type(file_path)
        f = None
        if file_type == "cpp":
            f = FuncCpp(file_path)
        elif file_type == "go":
            f = FuncGolang(file_path)
        f.start()
    else:
        print_help()


if __name__ == '__main__':
    main()
