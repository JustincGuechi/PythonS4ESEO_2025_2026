"""
Module ui.render
----------------
Fonctions pour dessiner un graphe sur un Canvas Tkinter.

Palier F - Séances 7-8.
"""

import tkinter as tk
from ..core import Graph
import math

# Constantes pour le rendu
NODE_RADIUS = 20
NODE_COLOR = "#4A90E2"
NODE_COLOR_VISITED = "#50C878"
NODE_COLOR_CURRENT = "#FF6B6B"
EDGE_COLOR = "#95A5A6"
EDGE_WIDTH = 2
TEXT_COLOR = "white"


def draw_graph(canvas: tk.Canvas, graph: Graph, positions: dict[str, tuple[int, int]], bg_image=None):
    """
    Dessine un graphe sur un Canvas Tkinter.

    Args:
        canvas: Canvas Tkinter où dessiner
        graph: Le graphe à dessiner
        positions: Dictionnaire {nœud: (x, y)} pour la position de chaque nœud
    
    Exemple:
        >>> canvas = tk.Canvas(root, width=800, height=600)
        >>> positions = {"A": (100, 100), "B": (200, 100)}
        >>> draw_graph(canvas, my_graph, positions)
    """
    # TODO: implémenter
    # Algorithme:
    # 1. Effacer le canvas
    # 2. Dessiner toutes les arêtes (lignes)
    # 3. Dessiner tous les nœuds (cercles + texte)
    
    # Astuce pour dessiner un cercle:
    # canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
    
    # Astuce pour dessiner une ligne:
    # canvas.create_line(x1, y1, x2, y2, width=width, fill=color)
    
    # Astuce pour dessiner du texte:
    # canvas.create_text(x, y, text=label, fill=color)
    
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
    """
    Surligne un chemin dans le graphe.
    
    Args:
        canvas: Canvas Tkinter
        path: Liste des nœuds du chemin
        positions: Positions des nœuds
    
    Note:
        Cette fonction redessine les nœuds du chemin en couleur différente.
    """
    # TODO: implémenter
    # Astuce : redessiner les nœuds du chemin avec NODE_COLOR_VISITED

    if not path or len(path) == 0:
        return

    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        if u in positions and v in positions:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            canvas.create_line(x1, y1, x2, y2, width=EDGE_WIDTH + 2, fill=NODE_COLOR_VISITED)

    for node in path:
        if node in positions:
            x, y = positions[node]
            r = NODE_RADIUS
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=NODE_COLOR_VISITED, outline="black", width=2)
            canvas.create_text(x, y, text=str(node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))



def animate_traversal(canvas: tk.Canvas, order: list[str], positions: dict[str, tuple[int, int]], delay_ms: int = 500):
    """
    Anime un parcours DFS/BFS nœud par nœud.
    
    Args:
        canvas: Canvas Tkinter
        order: Ordre de visite des nœuds
        positions: Positions des nœuds
        delay_ms: Délai entre chaque étape (millisecondes)
    
    Note:
        Utilise canvas.after() pour créer une animation.
        Fonction avancée, optionnelle pour les étudiants.
    """
    # TODO: implémenter (BONUS)
    # Astuce : utiliser canvas.after(delay, callback)
    
    def step(index):
        if index < len(order):
            node = order[index]
            if node in positions:
                x, y = positions[node]
                r = NODE_RADIUS

                canvas.create_oval(x-r, y-r, x+r, y+r, fill=NODE_COLOR_CURRENT, outline="black")
                canvas.create_text(x, y, text=str(node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))
                
                if index > 0:
                    prev_node = order[index-1]
                    if prev_node in positions:
                        px, py = positions[prev_node]
                        canvas.create_oval(px-r, py-r, px+r, py+r, fill=NODE_COLOR_VISITED, outline="black")
                        canvas.create_text(px, py, text=str(prev_node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))
            
            canvas.after(delay_ms, step, index + 1)
            
        elif len(order) > 0:
            last_node = order[-1]
            if last_node in positions:
                x, y = positions[last_node]
                r = NODE_RADIUS
                canvas.create_oval(x-r, y-r, x+r, y+r, fill=NODE_COLOR_VISITED, outline="black")
                canvas.create_text(x, y, text=str(last_node), fill=TEXT_COLOR, font=("Arial", 10, "bold"))
    step(0)


def auto_layout(graph: Graph, width: int = 800, height: int = 600) -> dict[str, tuple[int, int]]:
    """
    Génère automatiquement des positions pour les nœuds.
    
    Args:
        graph: Le graphe
        width: Largeur du canvas (défaut: 800)
        height: Hauteur du canvas (défaut: 600)
    
    Returns:
        Dictionnaire {nœud: (x, y)}
    
    Note:
        Implémentation simple : disposition circulaire.
        
        ⚠️ IMPORTANT : Assure les dimensions minimales !
        Si width < 400 ou height < 300 (par ex. Canvas non encore affiché),
        utilise les valeurs par défaut pour éviter un positionnement invalide.
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> g.add_edge("B", "C")
        >>> positions = auto_layout(g, width=800, height=600)
        >>> positions["A"]
        (600, 200)  # Environ au centre, sur un cercle
    
    Algorithme (disposition en cercle):
        1. Calculer le rayon du cercle (40% de la plus petite dimension)
        2. Pour chaque nœud i (sur N nœuds):
           - Calculer l'angle : 2π * i / N
           - Calculer position : (center_x + radius*cos(angle), center_y + radius*sin(angle))
    """
    # TODO: implémenter
    # Astuce : assurer les dimensions minimales

    positions = {}
    nodes = list(graph.nodes())
    n = len(nodes)
    
    if n == 0:
        return positions
        
    if width < 400: width = 800
    if height < 300: height = 600
    
    center_x = width / 2
    center_y = height / 2
    
    radius = min(width, height) * 0.40
    
    for i, node in enumerate(nodes):
        angle = i * (2 * math.pi / n)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        positions[node] = (int(x), int(y))
        
    return positions
