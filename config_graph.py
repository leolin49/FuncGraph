# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/19 14:28
# Author  : linyf49@qq.com
# File    : config_graph.py
class GraphConfig:
    def __init__(
        self,
        node_color="red",
        edge_color="black",
        node_size="2000",
        arrow_size="40",
        arrow_style="-|>",
    ):
        self.node_color = node_color
        self.edge_color = edge_color
        self.node_size = node_size
        self.arrow_size = arrow_size
        self.arrow_style = arrow_style
