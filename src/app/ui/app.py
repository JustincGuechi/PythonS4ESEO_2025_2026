"""
Module ui.app
-------------
Fenêtre principale de l'application Tkinter.

Palier F - Séances 6-8.
"""
import os
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
    "Rennes", "Reims", "Toulon", "Saint-Étienne", "Le Havre", "Dijon"
]

ROUTES_FRANCE = [
    ("Paris", "Lille", 225), ("Paris", "Le Havre", 195), ("Paris", "Rennes", 350),
    ("Paris", "Nantes", 385), ("Paris", "Bordeaux", 585), 
    ("Paris", "Reims", 145), ("Reims", "Strasbourg", 350), ("Rennes", "Nantes", 110),
    ("Nantes", "Bordeaux", 350), ("Bordeaux", "Toulouse", 245), 
    ("Toulouse", "Montpellier", 240), ("Montpellier", "Marseille", 170), 
    ("Lyon", "Saint-Étienne", 60), ("Lyon", "Marseille", 315),
    ("Marseille", "Toulon", 65), ("Toulon", "Nice", 150), 
    ("Lyon", "Strasbourg", 490), 
    ("Paris", "Dijon", 315), 
    ("Dijon", "Lyon", 195), 
    ("Dijon", "Strasbourg", 330)
]

POSITIONS_FRANCE = {
    "Paris": (400, 180), "Marseille": (580, 570), "Lyon": (520, 380),
    "Toulouse": (360, 580), "Nice": (660, 560), "Nantes": (220, 300),
    "Montpellier": (500, 540), "Strasbourg": (660, 180), "Bordeaux": (270, 480),
    "Lille": (440, 50), "Rennes": (220, 220), "Reims": (500, 150),
    "Toulon": (620, 590), "Saint-Étienne": (480, 400), "Le Havre": (300, 120), "Dijon": (500,300)
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
        self.root = root
        self.root.title("Calculateur d'itinéraire - France")
        self.root.geometry("1000x700")
        
        self.graph = Graph()
        self.controller = GraphController(self.graph)
        
        try:
            dossier_actuel = os.path.dirname(os.path.abspath(__file__))
            chemin_image = os.path.join(dossier_actuel, "carte_france.png")
            self.bg_image = tk.PhotoImage(file=chemin_image)
        except Exception as e:
            print(f"erreur image : {e}")
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
        
        tk.Button(leftFrame, text="Chercher un Itinéraire", command=self.run_shortest_path, bg="#9AD0E6", font=("Arial", 10, "bold"), height=2).pack(fill=tk.X, padx=5, pady=10)
        tk.Button(leftFrame, text="Réinitialiser la carte", command=self.load_france_map).pack(fill=tk.X, padx=5, pady=2)

        tk.Label(leftFrame, text="Villes disponibles :").pack(pady=(20, 0))
        self.node_listframe = tk.Listbox(leftFrame, height=20)
        self.node_listframe.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        rightFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        rightFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(rightFrame, bg="#FFFFFF") 
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
            
        for u, v, distance in ROUTES_FRANCE:
            self.graph.add_edge(u, v, weight=distance)
            
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
            path = self.controller.find_shortest_path(start, goal, POSITIONS_FRANCE)

            if path:
                self.draw_graph()
                render.highlight_path(self.canvas, path, POSITIONS_FRANCE)
                
                distance_totale = 0
                for i in range(len(path) - 1):
                    ville_a = path[i]
                    ville_b = path[i+1]

                    distance_totale += self.graph.weights.get((ville_a, ville_b), 0)

                chemin_str = " -> ".join(path)
                
                messagebox.showinfo(
                    "Itinéraire trouvé !", 
                    f"Le plus court chemin est :\n\n{chemin_str}\n\n Distance totale : {distance_totale} km"
                )
                
                
                self.statusVariable.set(f"Itinéraire affiché : {start} à {goal} ({distance_totale} km)")
                
            else:
                messagebox.showwarning("Introuvable", "Aucune route n'existe entre ces deux villes.")
                
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

def main():
    root = tk.Tk()
    app = GraphExplorerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
