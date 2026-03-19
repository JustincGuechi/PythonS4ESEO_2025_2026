"""
Module core.graph
-----------------
Implémentation d'un graphe non orienté basé sur une liste d'adjacence.

Ce module doit être TOTALEMENT indépendant de l'UI.
Tous les tests du palier A doivent passer avec ce fichier.
"""

from typing import Any


class Graph:
    """
    Représente un graphe non orienté.
    
    Structure de données : liste d'adjacence (dictionnaire)
    - Clé : nom du nœud (str)
    - Valeur : liste des voisins (list[str])
    
    Exemple d'usage:
        >>> g = Graph()
        >>> g.add_node("A")
        >>> g.add_node("B")
        >>> g.add_edge("A", "B")
        >>> g.neighbors("A")
        ['B']
    """

    def __init__(self):
        """Initialise un graphe vide."""
        # TODO: initialiser la structure de données
        # Conseil : utiliser un dictionnaire
        self.graph = {}
    
    def add_node(self, node: str) -> None:
        """
        Ajoute un nœud au graphe.
        
        Si le nœud existe déjà, ne fait rien (pas d'erreur).
        
        Args:
            node: Identifiant unique du nœud (chaîne de caractères)
        
        Raises:
            TypeError: Si node n'est pas une chaîne de caractères
        
        Exemple:
            >>> g = Graph()
            >>> g.add_node("Paris")
            >>> g.has_node("Paris")
            True
        """
        # TODO: implémenter
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, a: str, b: str) -> None:
        """
        Ajoute une arête non orientée entre deux nœuds.
        
        Si l'arête existe déjà, ne fait rien.
        Si l'un des nœuds n'existe pas, il est créé automatiquement.
        
        Args:
            a: Premier nœud
            b: Deuxième nœud
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("Paris", "Lyon")
            >>> g.has_edge("Paris", "Lyon")
            True
            >>> g.has_edge("Lyon", "Paris")  # Non orienté !
            True
        """
        # TODO: implémenter
        # Attention : graphe NON ORIENTÉ → ajouter dans les deux sens
        self.add_node(a)
        self.add_node(b)

        if b not in self.graph[a]:
            self.graph[a].append(b)

        if a not in self.graph[b]:
            self.graph[b].append(a)
    
    def remove_node(self, node: str) -> None:
        """
        Supprime un nœud et toutes ses arêtes associées.
        
        Args:
            node: Nœud à supprimer
        
        Raises:
            ValueError: Si le nœud n'existe pas
        """
        # TODO: implémenter
        # Attention : supprimer aussi le nœud de toutes les listes de voisins
        if node not in self.graph.keys():
            raise ValueError("le noeud n'existe pas")
        
        neighborsList = self.graph[node]
        for neighbor in neighborsList:
            if node in self.graph[neighbor]:
                self.graph[neighbor].remove(node)

        del self.graph[node]
    
    def remove_edge(self, a: str, b: str) -> None:
        """
        Supprime une arête entre deux nœuds.
        
        Args:
            a: Premier nœud
            b: Deuxième nœud
        
        Raises:
            ValueError: Si l'arête n'existe pas
        """
        # TODO: implémenter
        # Attention : graphe NON ORIENTÉ → supprimer dans les deux sens
        if a not in self.graph[b] or b not in self.graph[a]:
            raise ValueError("l'arête n'existe pas")
        self.graph[a].remove(b)
        self.graph[b].remove(a)
    
    def neighbors(self, node: str) -> list[str]:
        """
        Retourne la liste des voisins d'un nœud.
        
        Args:
            node: Nœud dont on veut les voisins
        
        Returns:
            Liste triée des nœuds voisins (ordre alphabétique)
        
        Raises:
            ValueError: Si le nœud n'existe pas
        
        Note:
            ⚠️ CRITIQUE : Cette méthode DOIT retourner une liste TRIÉE !
            Les algorithmes DFS et BFS en dépendent pour être déterministes.
            Les tests vérifieront explicitement cet ordre alphabétique.
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("A", "Z")
            >>> g.add_edge("A", "B")
            >>> g.add_edge("A", "M")
            >>> g.neighbors("A")
            ['B', 'M', 'Z']  # Toujours en ordre alphabétique
        """
        
        #vérifie que le noeud existe
        if node not in self.graph:
            raise ValueError(f"Le nœud '{node}' n'existe pas")
        
        #renvoie liste triée des voisins       
        return sorted(self.graph[node])
    
    def has_node(self, node: str) -> bool:
        """Vérifie si un nœud existe dans le graphe."""
        # TODO: implémenter
        return node in self.graph.keys()
    
    def has_edge(self, a: str, b: str) -> bool:
        """Vérifie si une arête existe entre deux nœuds."""
        # TODO: implémenter
        if a not in self.graph or b not in self.graph:
            return False
        return b in self.graph[a]
    
    def nodes(self) -> list[str]:
        """
        Retourne la liste de tous les nœuds du graphe.
        
        Returns:
            Liste triée des nœuds (ordre alphabétique)
        """
        if len(self.graph) == 0 :
            return []
        return sorted(list(self.graph.keys()))
    
    def edges(self) -> list[tuple[str, str]]:
        """
        Retourne la liste de toutes les arêtes du graphe.
        
        Returns:
            Liste de tuples (a, b) où a < b (ordre alphabétique)
            Chaque arête n'apparaît qu'une seule fois.
        
        Exemple:
            >>> g = Graph()
            >>> g.add_edge("B", "A")
            >>> g.edges()
            [('A', 'B')]  # Ordre normalisé
        """
        # TODO: implémenter
        # Astuce : utiliser un set pour éviter les doublons
        if len(self.graph) == 0 :
            return []
        
        aretes = []
        for u in self.graph:
            for v in self.graph[u]:
                if u < v:
                    aretes.append((u, v))
        return sorted(aretes)
    
    def __len__(self) -> int:
        """Retourne le nombre de nœuds dans le graphe."""
        return len(self.graph)
    
    def __repr__(self) -> str:
        """Représentation lisible du graphe pour debug."""
        return f"Graph(nodes={len(self)}, edges={len(self.edges())})"
