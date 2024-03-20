# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : func_py.py

import re
import keyword

import util
import config as cfg
from func import Func
from func_base import FuncBase
from config_graph import GraphConfig


class FuncPython(FuncBase):
    def __init__(self, mode: int, input_info=None):
        """
        :param mode: Work mode,
        mode=1(from file)
        mode=2(from console)
        mode=3(from editor)
        :param input_info: Source code "python" to be analyzed
        """
        super(FuncPython, self).__init__()
        self.log = util.get_logger(cfg.LOG_PATH_CPP, cfg.LOG_NAME_CPP)
        if input_info is None:
            exit(1)
        if mode == cfg.SUPPORT_MODE_FILE or mode == cfg.SUPPORT_MODE_EDIT:
            if cfg.COMPILER_DETECT:
                ok, err = util.check_file_syntax(input_info)
                if not ok:
                    self.compile_ok = False
                    print("python syntax check failed:" + err)
                    return
                self.compile_ok = True
                print("python syntax check success")
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
        python function line format: def function_name(param: param_type) -> return_type:
        example: def search(self: List[str], string: str, pos: int) -> List[str]:
        """
        for lineno, s in enumerate(self.file_lines):
            if re.search(r"\s*#.*?", s) is not None:
                # commentary line
                continue
            funcs = re.findall(
                r"\s*def\s+([A-Za-z_]+\w*)\s*\((.*?)\)\s*[->]*\s*\(*(.*?)\)*\s*:", s
            )
            if len(funcs) == 0:
                continue
            f_name, f_param, f_ret = funcs[0][0], funcs[0][1], funcs[0][2]
            if keyword.iskeyword(f_name) or f_name[0].isdigit():
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
        util.show_graph(
            self.graph,
            GraphConfig(cfg.NODE_COLOR_PYTHON, cfg.EDGE_COLOR_PYTHON, 2000, 40, "-|>"),
        )

    def start(self) -> None:
        self.__get_all_func()
        super().run()
        self.__draw()
