import re

import util
import config as cfg
from func import Func
from networkx import DiGraph


class FuncGolang:
    def __init__(self, mode: int, input_info=None):
        """
        func_id:    Unique ID of the function (begin with index 0)
        file_lines: The content of the source file is stored by line
        func_list:  Func object list
        line_func:  A dict, key = func_line, val = func_id
        edges:      A directed graph storing function call relationships
        :param mode: Work mode, mode=1(from file) mode=2(from console)
        :param input_info: Source code "cpp" file path to be analyzed
        """
        self.graph = DiGraph()
        self.func_id = 0
        self.func_list = []
        self.line_func = dict()
        self.edges = []
        self.log = util.get_logger(cfg.LOG_PATH_CPP, cfg.LOG_NAME_CPP)
        self.file_lines = []
        if input_info is None:
            self.log.error("no input from mode {}".format(mode))
            exit(1)
        if mode == 1:
            with open(input_info, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    self.file_lines.append(line)
        elif mode == 2:
            self.file_lines = input_info
        else:
            self.log.error("unknown work mode {}".format(mode))
            exit(1)

    def __get_all_func(self) -> None:
        """
        golang function line format: func function_name(parameter list) (return list) {
        example: func split(seq rune, max_split uint32) ([]string) {
        """
        for lineno, s in enumerate(self.file_lines):
            funcs = re.findall(
                r"\s*func\s+([A-Za-z_]+\w*)\s*\((.*?)\)\s*\(*(.*?)\)*\s*{", s
            )
            if len(funcs) == 0:
                continue
            f_name, f_param, f_ret = funcs[0][0], funcs[0][1], funcs[0][2]
            if f_name in cfg.KEYWORD_SET_GOLANG or f_name[0].isdigit():
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
        g = self.graph
        n = self.func_id
        fl = self.func_list
        g.add_nodes_from(obj.name for obj in self.func_list)
        for i in range(n):
            for j in self.edges[i]:
                g.add_edge(fl[i].name, fl[j].name)
        util.show_graph(g, cfg.NODE_COLOR_GOLANG, cfg.EDGE_COLOR_GOLANG)

    def start(self) -> None:
        self.__get_all_func()
        cur_id = -1
        for lineno, s in enumerate(self.file_lines):
            if lineno + 1 in self.line_func:
                cur_id = self.line_func[lineno + 1]
                continue
            for obj in self.func_list:
                if re.search(".*?{}\s*\(".format(obj.name), s) is not None:
                    self.log.info(
                        "Find a function call: line: {}, relation: {} -> {}".format(
                            lineno + 1, self.func_list[cur_id].name, obj.name
                        )
                    )
                    self.edges[cur_id].append(obj.id)
        self.__draw()
