"""
Module ui.controller
--------------------
Fait le lien entre l'interface graphique et le cœur algorithmique.

Ce module évite de mélanger la logique UI (Tkinter) et la logique métier (core).
"""

from ..core import Graph, dfs, bfs, shortest_path, is_connected


class GraphController:
    """
    Contrôleur pour gérer les interactions entre UI et Core.
    
    Pattern MVC (Model-View-Controller):
    - Model : Graph (core)
    - View : app.py, render.py (ui)
    - Controller : ce fichier
    """
    
    def __init__(self, graph: Graph):
        """
        Initialise le contrôleur avec un graphe.
        
        Args:
            graph: Le graphe à contrôler
        """
        self.graph = graph
    
    def execute_dfs(self, start: str) -> list[str]:
        """
        Exécute DFS et retourne l'ordre de visite.
        
        Args:
            start: Nœud de départ
        
        Returns:
            Liste des nœuds visités
        
        Raises:
            ValueError: Si le nœud n'existe pas ou si le graphe est vide
        """
        # TODO: implémenter
        # Validation + appel à core.algorithms.dfs()

        if not self.graph.nodes():
            raise ValueError("Le graphe est vide.")
            
        if start not in self.graph.nodes():
            raise ValueError(f"Noeud '{start}' n'existe pas.")
            
        try:
            ordre_visite = dfs(self.graph, start)
            return ordre_visite
            
        except Exception as e:
            raise ValueError(f"Erreur lors de l'exécution de la DFS : {e}")

    def execute_bfs(self, start: str) -> list[str]:
        """
        Exécute BFS et retourne l'ordre de visite.
        
        Args:
            start: Nœud de départ
        
        Returns:
            Liste des nœuds visités
        """
        # TODO: implémenter

        noeuds = self.graph.nodes()

        if not noeuds:
            raise ValueError("Le graphe est vide.")

        if start not in noeuds:
            raise ValueError(f"Noeud '{start}' n'existe pas.")

        try:
            ordre_visite = bfs(self.graph, start)
            return ordre_visite
            
        except Exception as e:
            raise ValueError(f"Erreur lors de l'exécution de la BFS : {e}")

    def find_shortest_path(self, start: str, goal: str) -> list[str] | None:
        """
        Trouve le plus court chemin entre deux nœuds.
        
        Args:
            start: Nœud de départ
            goal: Nœud d'arrivée
        
        Returns:
            Chemin ou None si aucun chemin
        """
        # TODO: implémenter

        noeuds = self.graph.nodes()
        
        if not noeuds:
            raise ValueError("Le graphe est vide.")

        if start not in noeuds:
            raise ValueError(f"Le nœud de départ '{start}' n'existe pas dans le graphe.")

        if goal not in noeuds:
            raise ValueError(f"Le nœud d'arrivée '{goal}' n'existe pas dans le graphe.")

        return shortest_path(self.graph, start, goal)
    
    def check_connectivity(self) -> bool:
        """
        Vérifie si le graphe est connexe.
        
        Returns:
            True si connexe, False sinon
        """
        # TODO: implémenter
        
        if not self.graph.nodes():
            return False

        return is_connected(self.graph)
    
    def get_graph_info(self) -> dict:
        """
        Retourne des informations sur le graphe.
        
        Returns:
            Dictionnaire avec des stats (nb nœuds, arêtes, connexité...)
        
        Exemple:
            {
                'nodes': 5,
                'edges': 7,
                'connected': True,
                'density': 0.7
            }
        """
        # TODO: implémenter
        # density = 2 * edges / (nodes * (nodes - 1)) pour graphe non orienté

        nodes = list(self.graph.nodes())
        nb_nodes = len(nodes)

        try:
            edges = list(self.graph.edges())
            nb_edges = len(edges)
        except AttributeError:
            nb_edges = 0

        connected = self.check_connectivity()
        
        if nb_nodes > 1:
            density = (2 * nb_edges) / (nb_nodes * (nb_nodes - 1))
        else:
            density = 0.0 
            
        return {
            'nodes': nb_nodes,
            'edges': nb_edges,
            'connected': connected,
            'density': round(density, 2) 
        }
