import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx

import tkinter as tk
import sys


def destroy(e): sys.exit()


root = tk.Tk()
root.wm_title("Embedding in TK")
# root.bind("<Destroy>", destroy)


f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)

G = nx.Graph()
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)
pos=nx.spring_layout(G)
nx.draw(G,pos,ax=a)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()