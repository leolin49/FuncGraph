import os.path
import sys

import util
from func_cpp import FuncCpp
from func_go import FuncGolang
from func_py import FuncPython


def print_help():
    print("Hello, the FCAV is a tool of source code function call relation analyze and visualize.")
    print(
        'Currently supported source file types:\tC++: ".cpp", Golang: ".go", Python: ".py"\n'
    )
    print("Usage:\n")
    print("\tpython {} [command] [arguments]\n".format(sys.argv[0]))
    print("The Commands are:\n")
    print("\thelp\tPrint the instructions and usage")
    print("\tgen\tGenerate function call relationships for a given source file")
    print("\t\te.g. python fcav.py gen testfiles/test.go")
    print("\tinput\tInput the code snippet of the specified type from console")
    print("\t\te.g. python fcav.py input cpp\t(Then input your cpp code and enter the Ctrl+Z to end)")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    cmd = sys.argv[1].lower()
    mode = 1
    f = None
    if cmd == "gen":
        file_path = sys.argv[2]
        if not os.path.exists(file_path):
            print("Source file not found: {}".format(file_path))
            return
        mode = 1
        file_type = util.get_file_type(file_path)
        if file_type == "cpp":
            f = FuncCpp(mode, file_path)
        elif file_type == "go":
            f = FuncGolang(mode, file_path)
        elif file_type == "py":
            f = FuncPython(mode, file_path)
        else:
            print('The type "{}" of source file is not supported'.format(file_type))
            return
        f.start()
    elif cmd == "input":
        input_type = sys.argv[2]
        inputs = []
        mode = 2
        for line in sys.stdin:
            inputs.append(line)
        if len(inputs) == 0:
            print('error: nothing input')
            return
        if input_type == "cpp":
            f = FuncCpp(mode, inputs)
        elif input_type == "go":
            f = FuncGolang(mode, inputs)
        elif input_type == "py":
            f = FuncPython(mode, inputs)
        else:
            print('The type "{}" of source code is not supported'.format(input_type))
            return
        f.start()
    elif cmd == "help":
        if len(sys.argv) < 3:
            print_help()
        else:
            c = sys.argv[2]
    else:
        print("{}: unknown command".format(sys.argv[1]))
        print("Run 'python fcav.py help' for usage.")


if __name__ == "__main__":
    main()
