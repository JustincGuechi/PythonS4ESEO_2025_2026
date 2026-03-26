"""
Module ui.render
----------------
Fonctions pour dessiner un graphe sur un Canvas Tkinter.

Palier F - Séances 7-8.
"""

import tkinter as tk
from ..core import Graph
from math import *

# Constantes pour le rendu
NODE_RADIUS = 20
NODE_COLOR = "#4A90E2"
NODE_COLOR_VISITED = "#50C878"
NODE_COLOR_CURRENT = "#FF6B6B"
EDGE_COLOR = "#95A5A6"
EDGE_WIDTH = 2
TEXT_COLOR = "white"


def draw_graph(canvas: tk.Canvas, graph: Graph, positions: dict[str, tuple[int, int]]):
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
    pass


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
    pass


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

    
    pass
