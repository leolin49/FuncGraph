# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : func_cpp.py

import re
import subprocess
import time

import util
from func import Func
from func_base import FuncBase
import config as cfg


class FuncCpp(FuncBase):
    def __init__(self, mode: int, input_info=None):
        """
        :param mode: Work mode,
        mode=1(from file)
        mode=2(from console)
        mode=3(from editor)
        :param input_info: Source code "cpp" to be analyzed
        """
        super(FuncCpp, self).__init__()
        self.log = util.get_logger(cfg.LOG_PATH_CPP, cfg.LOG_NAME_CPP)
        if input_info is None:
            exit(1)
        if mode == cfg.SUPPORT_MODE_FILE or mode == cfg.SUPPORT_MODE_EDIT:
            if cfg.COMPILER_DETECT:
                result = subprocess.run(
                    [
                        "g++",
                        "-c",
                        input_info,
                        "-o",
                        "./tmp/{}.o".format(int(time.time())),
                    ],
                    capture_output=True,
                )
                if result.returncode == 0:
                    print("g++ compile successfully!\n")
                else:
                    print("g++ compile failed!\n")
                    print(result.stderr.decode())
                    exit(0)
            with open(input_info, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    self.file_lines.append(line)
        elif mode == cfg.SUPPORT_MODE_TERM:
            self.file_lines = input_info
        else:
            print("unknown work mode {}".format(mode))
            exit(0)

    def __get_all_func(self) -> None:
        """
        cpp function line format: return_type function_name(parameter list) {
        example: vector<string> split(char seq, int max_split) {
        """
        for lineno, s in enumerate(self.file_lines):
            if re.search(r"\s*/[/*].*?", s) is not None:
                # commentary line
                continue
            funcs = re.findall(r"\s*([A-Za-z_]+\w*)\s+(\w+[()]*)\s*\((.*?)\)\s*{*", s)
            if len(funcs) == 0:
                # not match
                continue
            f_ret, f_name, f_param = funcs[0][0], funcs[0][1], funcs[0][2]
            if f_ret == "return" or f_name == "operator()":
                # some special cases
                continue
            if f_name in cfg.KEYWORD_SET_CPP or f_name[0].isdigit():
                # invalid function name (keyword or begin with digit)
                error_info = "invalid function name: {} in line {}".format(
                    f_name, lineno + 1
                )
                self.log.error(error_info)
                print(error_info)
                exit(1)
            f_lineno = lineno + 1
            self.log.info(
                "Get function {}: line:{}, name:{}, parameters:{}, return_type:{}".format(
                    self.func_id, f_lineno, f_name, f_param, f_ret
                )
            )
            self.func_list.append(Func(self.func_id, f_name, f_param, f_ret, f_lineno))
            self.line_func[f_lineno] = self.func_id
            self.func_id += 1
        self.edges = [[] for _ in range(self.func_id)]

    def __draw(self) -> None:
        super().draw()
        util.show_graph(self.graph, cfg.NODE_COLOR_CPP, cfg.EDGE_COLOR_CPP)

    def start(self) -> None:
        self.__get_all_func()
        super().run()
        self.__draw()
