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

        bottomFrame = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusVariable = tk.StringVar()
        tk.Label(bottomFrame, textvariable=self.statusVariable, anchor=tk.W).pack(side=tk.LEFT, padx=5, pady=2)

        # --- Frame Gauche (Contrôles) ---
        leftFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        leftFrame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(leftFrame, text="Outils de Navigation", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Button(leftFrame, text="📍 Chercher un Itinéraire", command=self.run_shortest_path, bg="#9AD0E6", font=("Arial", 10, "bold"), height=2).pack(fill=tk.X, padx=5, pady=10)
        tk.Button(leftFrame, text="🔄 Réinitialiser la carte", command=self.load_france_map).pack(fill=tk.X, padx=5, pady=2)

        tk.Label(leftFrame, text="Villes disponibles :").pack(pady=(20, 0))
        self.node_listframe = tk.Listbox(leftFrame, height=20)
        self.node_listframe.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # --- Frame Droite (Canvas) ---
        rightFrame = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        rightFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(rightFrame, bg="#9AD0E6") # Bleu clair pour la mer si l'image ne couvre pas tout
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_graph(self):
        """Dessine le graphe sur le Canvas via le module render."""
        self.canvas.delete("all")
        if len(self.graph.nodes()) > 0:
            if not self.current_positions:
                self.current_positions = render.auto_layout(self.graph, self.canvas.winfo_width(), self.canvas.winfo_height())

            render.draw_graph(self.canvas, self.graph, self.current_positions, self.bg_image)
        
    def new_graph(self):
        """Crée un nouveau graphe vide."""
        # TODO: implémenter
        self.graph = Graph()
        self.controller = GraphController(self.graph) 
        self.current_positions = {}                   
        
        self.canvas.delete("all")
        self.node_listframe.delete(0, tk.END)
        
        self.statusVariable.set("Nouveau graphe créé")
        
    def load_graph(self):
        """Charge un graphe depuis un fichier JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.askopenfilename()
        chemin_fichier = filedialog.askopenfilename(
        title="Sélectionner le fichier du graph",
        filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")])
    
        if not chemin_fichier:
            return

        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
            self.clear_canvas()
            if "nodes" in data:
                for node in data["nodes"]:
                    self.graph.add_node(node)
                    self.node_listframe.insert(tk.END, node)
            if "edges" in data:
                for edge in data["edges"]:
                    if len(edge) >= 2:
                        self.graph.add_edge(edge[0], edge[1])
            self.draw_graph()
            self.statusVariable.set(f"Graphe chargé depuis '{chemin_fichier}'")
            messagebox.showinfo("Succès", "Graphe chargé avec succès !")
            
        except Exception as e:
            messagebox.showerror("Erreur de chargement", f"Impossible de lire le fichier :\n{e}")
    
    def save_graph(self):
        """Sauvegarde le graphe actuel en JSON."""
        # TODO: implémenter
        # Astuce : utiliser filedialog.asksaveasfilename()

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )
        
        if not file_path:
            return 
            
        try:
            edges_list = list(self.graph.edges()) if hasattr(self.graph, 'edges') else []
            
            donnees_graphe = {
                "nodes": list(self.graph.nodes()),
                "edges": edges_list
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(donnees_graphe, f, indent=4)
            self.statusVariable.set("Graphe sauvegardé avec succès.")
            messagebox.showinfo("Succès", f"Graphe enregistré dans :\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Erreur de sauvegarde", f"Impossible d'enregistrer le graphe :\n{e}")
    
    def add_node(self):
        """Ajoute un nœud au graphe (via dialogue)."""
        # TODO: implémenter

        nom_noeud = simpledialog.askstring("Ajouter un noeud", "Noeud à ajouter", parent=self.root)
        
        if nom_noeud and nom_noeud.strip():
            nom_noeud = nom_noeud.strip()
            if nom_noeud not in self.graph.nodes():
                self.graph.add_node(nom_noeud)
                self.node_listframe.insert(tk.END, nom_noeud)
                self.statusVariable.set(f"Nœud '{nom_noeud}' ajouté avec succès.")
                self.draw_graph()
            else:
                messagebox.showwarning("Attention", f"Le noeud '{nom_noeud}' existe déjà !")
    
    def add_edge(self):
        """Ajoute une arête au graphe (via dialogue)."""
        # TODO: implémenter
        u = simpledialog.askstring("Arête", "Nœud de départ :", parent=self.root)
        if not u or not u.strip(): return 
        u = u.strip()
        
        v = simpledialog.askstring("Arête", f"Relier '{u}' à quel nœud d'arrivée ? :", parent=self.root)
        if not v or not v.strip(): return 
        v = v.strip()

        if u in self.graph.nodes() and v in self.graph.nodes():
            try:
                self.graph.add_edge(u, v)
                self.statusVariable.set(f"Arête ajoutée avec succès : {u} -> {v}")

                self.draw_graph()
            except Exception as e:
                messagebox.showerror("Erreur d'ajout", f"Impossible de créer l'arête :\n{e}")
        else:
            messagebox.showerror("Erreur", "L'un des nœuds (ou les deux) n'existe pas. Créez-les d'abord !")

    def run_dfs(self):
        """Lance DFS et visualise le résultat."""
        # TODO: implémenter
        # Astuce : appeler core.algorithms.dfs()
        # puis render.py pour visualiser
        start_node = simpledialog.askstring("DFS", "Entrez le nœud de départ:")
        if not start_node or not start_node.strip():
            return
        start_node = start_node.strip()
    
        try:
            visited_nodes = self.controller.execute_dfs(start_node)
            positions = render.auto_layout(self.graph, self.canvas.winfo_width(), self.canvas.winfo_height())
            render.draw_graph(self.canvas, self.graph, positions)
            render.animate_traversal(self.canvas, visited_nodes, positions, delay_ms=500)
            chemin_str = " -> ".join([str(n) for n in visited_nodes])
            messagebox.showinfo("Résultat DFS", f"Chemin :\n{chemin_str}")
            
        except ValueError as e:
            messagebox.showwarning("Erreur", str(e))
    
    def run_bfs(self):
        """Lance BFS et visualise le résultat."""
        # TODO: implémenter

        start_node=simpledialog.askstring("DFS","Entrez le nœud de départ: ")

        if not start_node or not start_node.strip():
            return
        start_node = start_node.strip()

        try :
            visited_nodes = self.controller.execute_bfs(start_node)
            positions = render.auto_layout(self.graph, self.canvas.winfo_width(), self.canvas.winfo_height())
            render.draw_graph(self.canvas, self.graph, positions)
            render.animate_traversal(self.canvas, visited_nodes, positions, delay_ms=500)
            chemin_str = " -> ".join([str(n) for n in visited_nodes])
            messagebox.showinfo("Résultat BFS", f"Chemin (Largeur) :\n{chemin_str}")
            self.statusVariable.set(f"BFS depuis '{start_node}' terminé.")

        except ValueError as e:
            messagebox.showwarning("Erreur", str(e))
        except Exception as e:
            messagebox.showerror("Erreur inattendue", f"Impossible d'exécuter le BFS :\n{e}")

    def clear_canvas(self):
        """Efface le canvas."""
        # TODO: implémenter
        
        self.canvas.delete("all")
        self.statusVariable.set("Canvas effacé")
        
    def show_info(self):
        """Affiche des infos sur le graphe actuel."""
        # TODO: implémenter
        # Exemple : nombre de nœuds, arêtes, connexité...
        
        stats = self.controller.get_graph_info()

        if stats['nodes'] == 0:
            message = "Le graphe est actuellement complètement vide.\nCommencez par ajouter des nœuds !"
        else:
            message = "Statistiques de votre graphe :\n\n"
            message += f"Nombre de nœuds : {stats['nodes']}\n"
            message += f"Nombre d'arêtes : {stats['edges']}\n"
            texte_connexe = "Oui" if stats['connected'] else "Non"
            message += f"Graphe connexe : {texte_connexe}\n"
            
            message += f"Densité : {stats['density']}\n\n"

            nodes = list(self.graph.nodes())
            if stats['nodes'] <= 20:
                nodes_list = ", ".join([str(n) for n in nodes])
                message += f"Liste des nœuds :\n{nodes_list}"
            else:
                message += "Liste des nœuds : (Trop nombreux pour l'affichage)"

        messagebox.showinfo("Informations du Graphe", message)

    def load_france_map(self):
        """Génère la carte de France avec les 15 grandes villes."""
        self.new_graph() # Nettoie tout
        
        # Ajoute les nœuds
        for ville in VILLES_FRANCE:
            self.graph.add_node(ville)
            self.node_listframe.insert(tk.END, ville)
            
        # Ajoute les routes
        for u, v in ROUTES_FRANCE:
            self.graph.add_edge(u, v)
            
        # Applique les positions fixes
        self.current_positions = POSITIONS_FRANCE
        
        self.draw_graph()
        self.statusVariable.set("Carte de France chargée avec les axes principaux.")

    def run_shortest_path(self):
        """Demande point A et B, et surligne l'itinéraire."""
        start = simpledialog.askstring("Itinéraire", "Ville de départ :", parent=self.root)
        if not start or not start.strip(): return
        
        goal = simpledialog.askstring("Itinéraire", "Ville d'arrivée :", parent=self.root)
        if not goal or not goal.strip(): return

        start, goal = start.strip(), goal.strip()

        try:
            # On utilise le contrôleur que tu as brillamment codé !
            path = self.controller.find_shortest_path(start, goal)
            
            if path:
                self.draw_graph() # Nettoie les anciens dessins
                render.highlight_path(self.canvas, path, self.current_positions)
                
                chemin_str = " -> ".join(path)
                messagebox.showinfo("Itinéraire trouvé !", f"Le plus court chemin est :\n\n{chemin_str}")
                self.statusVariable.set(f"Itinéraire affiché : {start} à {goal} ({len(path)-1} étapes)")
            else:
                messagebox.showwarning("Introuvable", "Aucune route n'existe entre ces deux villes.")
                
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

def main():
    """Point d'entrée de l'application."""
    root = tk.Tk()
    app = GraphExplorerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
