"""
Module ui.app
-------------
Fenêtre principale de l'application Tkinter.

Palier F - Séances 6-8.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from ..core import Graph
from tkinter.colorchooser import askcolor
from tkinter import *

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

        #self.bg_image = tk.PhotoImage(file="C:/Users/coudryni/Documents/licensed-image.png")
        #background_label = tk.Label(self.root, image=self.bg_image)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)

        topFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        topFrame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        
        tk.Button(topFrame, text="Nouveau", command=self.new_graph).pack(side=tk.LEFT, padx=5)
        tk.Button(topFrame, text="CHARGER! CHARGER! CHARGER! CHARGER! BRRRRRRRRRRRRR", command=self.load_graph).pack(side=tk.LEFT, padx=5)
        tk.Button(topFrame, text= "Sauvegarder", command=self.save_graph).pack(side=tk.LEFT, padx=5)
        
        bottomFrame = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.statusVariable = tk.StringVar()
        self.statusVariable.set("Statut : Prêt. En attente de création d'un graphe.")
        tk.Label(bottomFrame, textvariable=self.statusVariable, anchor=tk.W).pack(side=tk.LEFT, padx=5, pady=2)

        leftFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        leftFrame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(leftFrame, text="Outils & Nœuds", font=("Arial", 10, "bold")).pack(pady=5)
        
        tk.Button(leftFrame, text="+ Ajouter Nœud", command=self.add_node).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(leftFrame, text="+ Ajouter Arête", command=self.add_edge).pack(fill=tk.X, padx=5, pady=2)
        tk.Button(leftFrame, text="Lancer DFS", command=self.run_dfs).pack(fill=tk.X, padx=5, pady=10)
        tk.Button(leftFrame, text="Lancer BFS", command=self.run_bfs).pack(fill=tk.X, padx=5, pady=2)
        
        tk.Label(leftFrame, text="Liste des Nœuds :").pack(pady=(10, 0))
        self.node_listframe = tk.Listbox(leftFrame, height=15)
        self.node_listframe.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        rightFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        rightFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(rightFrame, bg="white", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        tk.Button(rightFrame, text="Effacer le dessin", command=self.clear_canvas).pack(side=tk.BOTTOM, pady=5)

        bottomFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)

        self.canvas.config(bg='#9AD0E6')

    def new_graph(self):
        """Crée un nouveau graphe vide."""
        # TODO: implémenter
        self.graph = Graph()
        self.clear_canvas()
        
    def load_graph(self):
        """Charge un graphe depuis un fichier JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.askopenfilename()
        chemin_fichier = filedialog.askopenfilename(
        title="Sélectionner le fichier du graph",
        filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")])
    
        if not chemin_fichier:
            return None
    
    def save_graph(self):
        """Sauvegarde le graphe actuel en JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.asksaveasfilename()
        if self.current_file_path:

            import os
            initial_name = os.path.basename(self.current_file_path).split('.')[0] + "_modifie.png"

    
        file_path = filedialog.asksaveasfilename(
            initialfile=initial_name,
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("PDF Document", "*.pdf"), ("Tous les fichiers", "*.*")]
        )
        
        if file_path:
            try:
                self.fig.savefig(file_path)
                self.current_file_path = file_path
                messagebox.showinfo("Succès", f"Fichier enregistré :\n{file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde : {e}")
    
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
