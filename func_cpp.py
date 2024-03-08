import re

import util
from func import Func
from networkx import DiGraph
import config as cfg


class FuncCpp:
    def __init__(self, file_path: str):
        """
        func_id:    Unique ID of the function (begin with index 0)
        file_path:  Source code "cpp" file path to be analyzed
        file_lines: The content of the source file is stored by line
        func_list:  Func object list
        line_func:  A dict, key = func_line, val = func_id
        edges:      A directed graph storing function call relationships
        """
        self.graph = DiGraph()
        self.func_id = 0
        self.file_path = file_path
        self.file_lines = []
        self.func_list = []
        self.line_func = dict()
        self.edges = []
        self.log = util.get_logger(cfg.LOG_PATH_CPP, cfg.LOG_NAME_CPP)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                self.file_lines.append(line)

    def __get_all_func(self) -> None:
        """
        cpp function line format: return_type function_name(parameter list) {
        example: vector<string> split(char seq, int max_split) {
        """
        for lineno, s in enumerate(self.file_lines):
            if len(s) >= 2 and (s[:2] == "//" or s[:2] == "/*"):
                # commentary line
                continue
            funcs = re.findall(cfg.FUNC_PATTERN_CPP, s)
            if len(funcs) == 0:
                # not match
                continue
            f_ret, f_name, f_param = funcs[0][0], funcs[0][1], funcs[0][2]
            if f_ret == "return":
                continue
            if f_name in cfg.KEYWORD_SET_CPP or f_name in cfg.KEYWORD_SET_CPP or f_name[0].isdigit():
                # invalid function name
                self.log.error("Invalid function name: {}".format(f_name))
                continue
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

    def draw(self) -> None:
        g = self.graph
        n = self.func_id
        fl = self.func_list
        g.add_nodes_from(obj.name for obj in self.func_list)
        [g.add_edge(fl[i].name, fl[j].name) for i in range(n) for j in self.edges[i]]
        util.show_graph(g)

    def start(self) -> None:
        self.__get_all_func()
        cur_id = -1
        for lineno, s in enumerate(self.file_lines):
            if lineno + 1 in self.line_func:
                cur_id = self.line_func[lineno + 1]
                continue
            for obj in self.func_list:
                if re.search('.*?'+obj.name+'\s*\(', s) is not None:
                    self.edges[cur_id].append(obj.id)
        self.draw()