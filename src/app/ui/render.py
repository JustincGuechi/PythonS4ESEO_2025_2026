"""
Module ui.render
----------------
Fonctions pour dessiner un graphe sur un Canvas Tkinter.

Palier F - Séances 7-8.
"""
import tkinter as tk
from ..core import Graph

NODE_RADIUS = 20
NODE_COLOR = "#4A90E2"
NODE_COLOR_VISITED = "#50C878"
EDGE_COLOR = "#95A5A6"
EDGE_WIDTH = 2
TEXT_COLOR = "black"

def draw_graph(canvas: tk.Canvas, graph: Graph, positions: dict[str, tuple[int, int]], bg_image=None):
    """Dessine le graphe routier sur la carte."""
    canvas.delete("all")


    if bg_image:
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

    for u, v in graph.edges():
        if u in positions and v in positions:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            canvas.create_line(x1, y1, x2, y2, width=EDGE_WIDTH, fill=EDGE_COLOR)
        

    for node in graph.nodes():
        if node in positions:
            x, y = positions[node]
            r = NODE_RADIUS
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=NODE_COLOR, outline="black")
            canvas.create_text(x, y, text=str(node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))


def highlight_path(canvas: tk.Canvas, path: list[str], positions: dict[str, tuple[int, int]]):
    """Surligne l'itinéraire trouvé en vert."""
    if not path or len(path) == 0:
        return


    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        if u in positions and v in positions:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            canvas.create_line(x1, y1, x2, y2, width=EDGE_WIDTH + 3, fill=NODE_COLOR_VISITED)


    for node in path:
        if node in positions:
            x, y = positions[node]
            r = NODE_RADIUS
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=NODE_COLOR_VISITED, outline="black", width=2)
            canvas.create_text(x, y, text=str(node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))