# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : util.py

import logging
import networkx as nx
import matplotlib.pyplot as plt


def get_logger(log_file_path: str, name="Unknown log name"):
    """
    get logger
    :param log_file_path: log file path
    :param name: log name
    :return: logging object by default config
    """
    logger = logging.getLogger(name)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s-%(name)s-%(lineno)s-%(levelname)s - %(message)s",
        filename=log_file_path,
        filemode="a",  # append at the end of log file
        # filemode="w",  # rewrite the log file
    )
    return logger


def show_graph(dig: nx.DiGraph, node_color: str, edge_color="black"):
    pos = nx.spring_layout(dig, k=1)
    # pos = nx.arf_layout(dig)
    nx.draw(dig, pos, with_labels=True)
    # draw nodes
    nodes = [node for node in dig.nodes]
    nx.draw_networkx_nodes(
        dig,
        pos,
        nodelist=nodes,
        node_size=2000,
        node_color=node_color,
    )
    # draw edges
    edges = [(u, v) for (u, v) in dig.edges]
    nx.draw_networkx_edges(
        dig,
        pos,
        edgelist=edges,
        arrows=True,
        arrowsize=40,
        arrowstyle="-|>",
        edge_color=edge_color
    )
    plt.show()


def get_file_type(filename: str) -> str:
    return filename.split(".")[-1]
