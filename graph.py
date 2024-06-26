import networkx as nx
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_edge(ratings,currency1):
    G = nx.Graph()
    G.add_nodes_from(ratings.columns)
    weights = ratings.iloc[0]
    for col1 in ratings.columns:
        if col1 != currency1:
                weight = weights[col1]
                if weight != 0:  # Exclude edges with zero weight
                    G.add_edge(currency1, col1, weight=weight)
    return G

def is_component(G,node):
    if ' - ' in node:
        node = node.split(' - ')[1]
    if " " in node:
        node = node.replace(" ", "\n")
    visited = set()
    component = set()
    dfs(node, G, visited, component)
    return component

def dfs(node, G, visited, component):
    visited.add(node)
    component.add(node)
    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            dfs(neighbor, G, visited, component)


def draw_graph(G,main_node,root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    fig = Figure(figsize=(11,10),dpi=50)
    a = fig.add_subplot(111)

    old_labels = {node: str(node) for node in G.nodes}

    for node, label in old_labels.items():
        if ' - ' in str(label):
            old_labels[node] = str(label).split(' - ')[1]
        if " " in old_labels[node]:
            old_labels[node] = str(old_labels[node]).replace(" ", "\n")

    G = nx.relabel_nodes(G, old_labels)

    # pos = nx.circular_layout(G)
    # nx.draw(G, pos,ax=a,with_labels=True,node_size=700)
    if ' - ' in main_node:
        main_node = main_node.split(' - ')[1]
    if " " in main_node:
        main_node = main_node.replace(" ", "\n")

    nodes_with_edges = is_component(G,main_node)
    subgraph = G.subgraph(nodes_with_edges)
    pos = nx.circular_layout(subgraph)
    pos[main_node] = np.array([0, 0])
    nx.draw(subgraph, pos, ax=a, with_labels=True, node_size=2000,node_color="yellow")

    edge = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge,ax=a,font_color='blue',font_size=18)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig
