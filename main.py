import sys

import util
from func_cpp import FuncCpp
from func_go import FuncGolang


def print_help():
    print("Source file function call relation visualize.")
    print('Currently supported source file types: ".cpp", ".go"\n')
    print("Usage:\n")
    print("\tpython {} [command] [arguments]\n".format(sys.argv[0]))
    print("The Commands are:\n")
    print("\thelp\tPrint the instructions and usage")
    print("\tgen\tGenerate function call relationships for a given source file")


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
    elif cmd == "help":
        print_help()
    else:
        print("{}: unknown command".format(sys.argv[1]))
        print("Run 'python main.py help' for usage.")


if __name__ == "__main__":
    main()
