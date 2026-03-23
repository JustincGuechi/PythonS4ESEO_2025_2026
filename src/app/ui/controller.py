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
        pass
    
    def execute_bfs(self, start: str) -> list[str]:
        """
        Exécute BFS et retourne l'ordre de visite.
        
        Args:
            start: Nœud de départ
        
        Returns:
            Liste des nœuds visités
        """
        # TODO: implémenter
        pass
    
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
        pass
    
    def check_connectivity(self) -> bool:
        """
        Vérifie si le graphe est connexe.
        
        Returns:
            True si connexe, False sinon
        """
        # TODO: implémenter
        pass
    
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
        pass
