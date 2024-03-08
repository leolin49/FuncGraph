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
        # filemode='a', # append at the end of log file
        filemode="w",  # rewrite the log file
    )
    return logger


def show_graph(dig: nx.DiGraph, node_color: str):
    # pos = nx.spring_layout(dig, k=1)
    pos = nx.arf_layout(dig)
    nx.draw(dig, pos, with_labels=True, font_weight="bold", font_color="black")
    # draw nodes
    nodes = [node for node in dig.nodes]
    nx.draw_networkx_nodes(
        dig,
        pos,
        nodelist=nodes,
        node_size=1000,
        node_color=node_color,
        alpha=0.618,
        node_shape='o'
    )
    # draw edges
    edges = [(u, v) for (u, v) in dig.edges]
    nx.draw_networkx_edges(
        dig,
        pos,
        edgelist=edges,
        arrows=True,
        arrowsize=20,
        arrowstyle="-|>",
        style="dashed"
    )
    plt.show()


def get_file_type(filename: str) -> str:
    return filename.split(".")[-1]
