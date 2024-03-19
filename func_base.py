# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/19 11:58
# Author  : linyf49@qq.com
# File    : func.py
import re

from typing import List, Dict
from networkx import DiGraph

from func import Func


class FuncBase:
    """
    func_id:    Unique ID of the function (begin with index 0)
    file_lines: The content of the source file is stored by line
    func_list:  Func object list
    line_func:  A dict, key = func_line, val = func_id
    edges:      A directed graph storing function call relationships
    """

    graph: DiGraph
    func_id: int = 0
    file_lines: List[str]
    func_list: List[Func]
    line_func: Dict[int, int]
    edges: List[List[int]]
    log: None

    def __init__(self):
        self.graph = DiGraph()
        self.file_lines = []
        self.func_list = []
        self.line_func = dict()
        self.edges = []

    def __get_all_func(self) -> None:
        pass

    def draw(self) -> None:
        g = self.graph
        n = self.func_id
        fl = self.func_list
        g.add_nodes_from(obj.name for obj in self.func_list)
        [g.add_edge(fl[i].name, fl[j].name) for i in range(n) for j in self.edges[i]]

    def run(self):
        cur_id = -1
        for lineno, s in enumerate(self.file_lines):
            if lineno + 1 in self.line_func:
                cur_id = self.line_func[lineno + 1]
                continue
            for obj in self.func_list:
                if re.search(r".*?{}\s*\(".format(obj.name), s) is not None:
                    self.log.info(
                        "Find a function call: line: {}, relation: {} -> {}".format(
                            lineno + 1, self.func_list[cur_id].name, obj.name
                        )
                    )
                    self.edges[cur_id].append(obj.id)
