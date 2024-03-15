# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : fcav.py

import os.path
import sys

import util
import config as cfg
import editor as edt
from func_cpp import FuncCpp
from func_go import FuncGolang
from func_py import FuncPython


def print_help():
    print(
        "Hello, the FCAV is a tool of source code function call relation analyze and visualize."
    )
    print('Current supported languages:\tC++: ".cpp", Golang: ".go", Python: ".py"\n')
    print("Usage:")
    print("\tpython {} [command] [arguments] [options]\n".format(sys.argv[0]))
    print("The Commands are:")
    # help
    print("\thelp\tPrint the instructions and usage")
    # gen
    print("\tgen\tGenerate function call relationships for a given source file")
    print("\t\te.g. python fcav.py gen testfiles/test.go -c")
    # input
    print("\tinput\tInput the code snippet of the specified type from console")
    print("\t\te.g. python fcav.py input cpp\t(Then input your cpp code and enter the Ctrl+Z to end)")
    # editor
    print("\teditor\tInput the code snippet on a new editor")
    print("\t\te.g. python fcav.py editor cpp\t(Then input your cpp code and click the 'Run' button to run FCAV)")
    print("The Options are:")
    print("\t-c\tTurn on the relevant compiler for syntax checkout")


def main():
    if len(sys.argv) < 3:
        print_help()
        return

    options = []
    if len(sys.argv) >= 4:
        options = sys.argv[3:]
    for option in options:
        if option == "-c":
            cfg.COMPILER_DETECT = True

    cmd = sys.argv[1].lower()
    f = None
    if cmd == "gen":
        mode = cfg.SUPPORT_MODE_FILE
        file_path = sys.argv[2]
        if not os.path.exists(file_path):
            print("Source file not found: {}".format(file_path))
            return
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
        mode = cfg.SUPPORT_MODE_TERM
        input_type = sys.argv[2]
        input_type = input_type.lower()
        inputs = []
        if input_type not in cfg.SUPPORT_LANG:
            print('The type "{}" of source code is not supported'.format(input_type))
            return
        print("input your code and enter Ctrl+Z for ending\n")
        for line in sys.stdin:
            inputs.append(line)
        if input_type == "cpp" or input_type == "c++":
            f = FuncCpp(mode, inputs)
        elif input_type == "go" or input_type == "golang":
            f = FuncGolang(mode, inputs)
        elif input_type == "py" or input_type == "python":
            f = FuncPython(mode, inputs)
        f.start()
    elif cmd == "editor":
        # mode = cfg.SUPPORT_MODE_EDIT
        input_type = sys.argv[2]
        input_type = input_type.lower()
        if input_type not in cfg.SUPPORT_LANG:
            print('The type "{}" of source code is not supported'.format(input_type))
            return
        ed = edt.Editor(input_type)
        ed.run()
    elif cmd == "help":
        print_help()
    else:
        print("{}: unknown command".format(sys.argv[1]))
        print("Run 'python fcav.py help' for usage.")


if __name__ == "__main__":
    main()
