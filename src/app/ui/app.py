"""
Module ui.app
-------------
Fenêtre principale de l'application Tkinter.

Palier F - Séances 6-8.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from ..core import Graph


class GraphExplorerApp:
    """
    Application principale avec interface Tkinter.
    
    Fonctionnalités:
    - Créer/charger un graphe
    - Visualiser le graphe
    - Lancer DFS/BFS avec animation
    - Sauvegarder le graphe
    """
    
    def __init__(self, root: tk.Tk):
        """
        Initialise l'application.
        
        Args:
            root: Fenêtre racine Tkinter
        """
        self.root = root
        self.root.title("Explorateur de Graphes - ESEO S4")
        self.root.geometry("1000x700")
        
        # Graphe actuel
        self.graph = Graph()
        
        # Configuration de l'interface
        self._setup_ui()
    
    def _setup_ui(self):
        """Configure tous les widgets de l'interface."""
        # TODO: implémenter l'interface
        # Suggestions de structure:
        # 1. Frame haut : boutons de contrôle
        # 2. Frame gauche : liste des nœuds
        # 3. Frame centre : Canvas pour dessiner le graphe
        # 4. Frame bas : zone de status/log
        
        # Exemple de structure de base:
        # top_frame = tk.Frame(self.root)
        # top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        # 
        # tk.Button(top_frame, text="Nouveau", command=self.new_graph).pack(side=tk.LEFT)
        # tk.Button(top_frame, text="Charger", command=self.load_graph).pack(side=tk.LEFT)
        # tk.Button(top_frame, text="Sauver", command=self.save_graph).pack(side=tk.LEFT)
        # ...

        top_frame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        tk.Button(top_frame, text="Nouveau", command=self.new_graph).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Charger", command=self.load_graph).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Sauver", command=self.save_graph).pack(side=tk.LEFT, padx=5)
        
        tk.Button(top_frame, text="Lancer DFS", command=self.run_dfs).pack(side=tk.LEFT, padx=20)
        tk.Button(top_frame, text="Lancer BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=5)

        bottom_frame = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_label = tk.Label(bottom_frame, text="Prêt - En attente d'un graphe...")
        self.status_label.pack(side=tk.LEFT, padx=5, pady=2)

        left_frame = tk.Frame(self.root, width=200, bg="lightgray")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(left_frame, text="Liste des Nœuds", bg="lightgray").pack(pady=5)
        
        self.node_listbox = tk.Listbox(left_frame)
        self.node_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        center_frame = tk.Frame(self.root)
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(center_frame, bg="white", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def new_graph(self):
        """Crée un nouveau graphe vide."""
        # TODO: implémenter
        pass
    
    def load_graph(self):
        """Charge un graphe depuis un fichier JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.askopenfilename()
        pass
    
    def save_graph(self):
        """Sauvegarde le graphe actuel en JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.asksaveasfilename()
        pass
    
    def add_node(self):
        """Ajoute un nœud au graphe (via dialogue)."""
        # TODO: implémenter
        # Astuce : utiliser tk.simpledialog.askstring()
        pass
    
    def add_edge(self):
        """Ajoute une arête au graphe (via dialogue)."""
        # TODO: implémenter
        pass
    
    def run_dfs(self):
        """Lance DFS et visualise le résultat."""
        # TODO: implémenter
        # Astuce : appeler core.algorithms.dfs()
        # puis render.py pour visualiser
        pass
    
    def run_bfs(self):
        """Lance BFS et visualise le résultat."""
        # TODO: implémenter
        pass
    
    def clear_canvas(self):
        """Efface le canvas."""
        # TODO: implémenter
        pass
    
    def show_info(self):
        """Affiche des infos sur le graphe actuel."""
        # TODO: implémenter
        # Exemple : nombre de nœuds, arêtes, connexité...
        pass


def main():
    """Point d'entrée de l'application."""
    root = tk.Tk()
    app = GraphExplorerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
