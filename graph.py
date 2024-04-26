import networkx as nx
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

def is_component(G):
    component_edges = {}
    for component in nx.connected_components(G):
        subgraph = G.subgraph(component)
        edge_weights = nx.get_edge_attributes(subgraph, 'weight')
        component_edges.update(edge_weights)
    return component_edges

def draw_graph(G,root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    fig = Figure(figsize=(10,8),dpi=50)
    a = fig.add_subplot(111)

    pos = nx.circular_layout(G)
    edge = nx.get_edge_attributes(G, 'weight')
    #components
    # edge = is_component(G)
    nx.draw(G, pos,ax=a)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge,ax=a,font_color='blue',font_size=18)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig
