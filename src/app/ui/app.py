"""
Module ui.app
-------------
Fenêtre principale de l'application Tkinter.

Palier F - Séances 6-8.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from ..core import Graph
from ..core import algorithms
from tkinter.colorchooser import askcolor
from tkinter import *
from tkinter import simpledialog
from . import render
from .controller import GraphController
import json

VILLES_FRANCE = [
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice", 
    "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Toulon", "Saint-Étienne", "Le Havre"
]

ROUTES_FRANCE = [
    ("Paris", "Lille"), ("Paris", "Le Havre"), ("Paris", "Rennes"),
    ("Paris", "Nantes"), ("Paris", "Bordeaux"), ("Paris", "Lyon"),
    ("Paris", "Reims"), ("Reims", "Strasbourg"), ("Rennes", "Nantes"),
    ("Nantes", "Bordeaux"), ("Bordeaux", "Toulouse"), ("Toulouse", "Montpellier"),
    ("Montpellier", "Marseille"), ("Lyon", "Saint-Étienne"), ("Lyon", "Marseille"),
    ("Marseille", "Toulon"), ("Toulon", "Nice"), ("Lyon", "Strasbourg"),
    ("Montpellier", "Toulouse")
]

POSITIONS_FRANCE = {
    "Paris": (400, 180), "Marseille": (580, 520), "Lyon": (520, 380),
    "Toulouse": (380, 510), "Nice": (680, 500), "Nantes": (220, 280),
    "Montpellier": (500, 510), "Strasbourg": (700, 200), "Bordeaux": (280, 420),
    "Lille": (420, 50), "Rennes": (220, 200), "Reims": (500, 150),
    "Toulon": (620, 540), "Saint-Étienne": (480, 400), "Le Havre": (300, 120)
}

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
        self.root.title("Calculateur d'itinéraire - France")
        self.root.geometry("1000x700")
        
        self.graph = Graph()
        self.controller = GraphController(self.graph)
        
        try:
            self.bg_image = tk.PhotoImage(file="carte_france.png") 
        except Exception:
            self.bg_image = None
            
        self._setup_ui()
        self.load_france_map()

    
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

        bottomFrame = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusVariable = tk.StringVar()
        tk.Label(bottomFrame, textvariable=self.statusVariable, anchor=tk.W).pack(side=tk.LEFT, padx=5, pady=2)

        leftFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        leftFrame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(leftFrame, text="Outils de Navigation", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Button(leftFrame, text="📍 Chercher un Itinéraire", command=self.run_shortest_path, bg="#9AD0E6", font=("Arial", 10, "bold"), height=2).pack(fill=tk.X, padx=5, pady=10)
        tk.Button(leftFrame, text="🔄 Réinitialiser la carte", command=self.load_france_map).pack(fill=tk.X, padx=5, pady=2)

        tk.Label(leftFrame, text="Villes disponibles :").pack(pady=(20, 0))
        self.node_listframe = tk.Listbox(leftFrame, height=20)
        self.node_listframe.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        rightFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        rightFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(rightFrame, bg="#9AD0E6") 
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_graph(self):
        """Dessine la carte sur le Canvas."""
        self.canvas.delete("all")
        render.draw_graph(self.canvas, self.graph, POSITIONS_FRANCE, self.bg_image)
        
    def load_france_map(self):
        """Génère la carte de France avec les villes et les routes."""
        self.graph = Graph()
        self.controller = GraphController(self.graph)
        self.node_listframe.delete(0, tk.END)

        for ville in VILLES_FRANCE:
            self.graph.add_node(ville)
            self.node_listframe.insert(tk.END, ville)
            
        for u, v in ROUTES_FRANCE:
            self.graph.add_edge(u, v)
            
        self.draw_graph()
        self.statusVariable.set("Carte prête. Prêt pour le calcul d'itinéraire.")

    def run_shortest_path(self):
        """Demande point A et B, et surligne l'itinéraire."""
        start = simpledialog.askstring("Itinéraire", "Ville de départ :", parent=self.root)
        if not start or not start.strip(): return
        
        goal = simpledialog.askstring("Itinéraire", "Ville d'arrivée :", parent=self.root)
        if not goal or not goal.strip(): return

        start, goal = start.strip().capitalize(), goal.strip().capitalize() 

        try:
            path = self.controller.find_shortest_path(start, goal)
            
            if path:
                self.draw_graph()
                render.highlight_path(self.canvas, path, POSITIONS_FRANCE)
                
                chemin_str = " -> ".join(path)
                messagebox.showinfo("Itinéraire trouvé !", f"Le plus court chemin est :\n\n{chemin_str}")
                self.statusVariable.set(f"Itinéraire affiché : {start} à {goal} ({len(path)-1} étapes)")
            else:
                messagebox.showwarning("Introuvable", "Aucune route n'existe entre ces deux villes.")
                
        except ValueError:
            messagebox.showerror("Erreur", f"L'une des villes n'est pas sur la carte.\nVérifiez l'orthographe (ex: '{start}' ou '{goal}').")

def main():
    root = tk.Tk()
    app = GraphExplorerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
