"""
Module core.io
--------------
Import/Export de graphes au format JSON.

Palier E.
"""

import json
from pathlib import Path
from .graph import Graph


# ============================================================================
# PALIER E : Import/Export
# ============================================================================

def save_graph(graph: Graph, filepath: str | Path) -> None:
    """
    Sauvegarde un graphe au format JSON.
    
    Format JSON:
    {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    
    Args:
        graph: Le graphe à sauvegarder
        filepath: Chemin du fichier de sortie
    
    Raises:
        IOError: Si l'écriture échoue
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> save_graph(g, "my_graph.json")
    """
    # TODO: implémenter
    # Astuce : utiliser graph.nodes() et graph.edges()
    # Convertir les edges en liste de listes pour JSON
    data = graph_to_dict(graph)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise IOError(f"Erreur lors de l'écriture du fichier : {e}")


def load_graph(filepath: str | Path) -> Graph:
    """
    Charge un graphe depuis un fichier JSON.
    
    Format JSON attendu:
    {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    
    Args:
        filepath: Chemin du fichier à charger
    
    Returns:
        Le graphe chargé
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si le format JSON est invalide
        KeyError: Si les clés "nodes" ou "edges" sont absentes
    
    Exemple:
        >>> g = load_graph("my_graph.json")
        >>> g.has_node("A")
        True
    """
    # TODO: implémenter
    # Astuce :
    # 1. Ouvrir et parser le JSON
    # 2. Créer un graphe vide
    # 3. Ajouter les nœuds
    # 4. Ajouter les arêtes
    # 5. Gérer les exceptions proprement
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {filepath} n'existe pas.")
    except json.JSONDecodeError:
        raise ValueError("Le fichier n'est pas un JSON valide.")
    return dict_to_graph(data)


def graph_to_dict(graph: Graph) -> dict:
    """
    Convertit un graphe en dictionnaire (utile pour serialization).
    
    Args:
        graph: Le graphe à convertir
    
    Returns:
        Dictionnaire avec clés "nodes" et "edges"
    
    Exemple:
        >>> g = Graph()
        >>> g.add_edge("A", "B")
        >>> graph_to_dict(g)
        {'nodes': ['A', 'B'], 'edges': [['A', 'B']]}
    """
    # TODO: implémenter
    
    nodes_list = list(graph.nodes())
    
    edges_list = [list(edge) for edge in graph.edges()]
    
    return {
        "nodes": nodes_list,
        "edges": edges_list
    }


def dict_to_graph(data: dict) -> Graph:
    """
    Crée un graphe depuis un dictionnaire.
    
    Args:
        data: Dictionnaire avec clés "nodes" et "edges"
              - "nodes": liste de chaînes ["A", "B", "C"]
              - "edges": liste de paires [["A", "B"], ["B", "C"]]
                         (ou tuples : [("A", "B"), ("B", "C")])
    
    Returns:
        Le graphe créé
    
    Raises:
        KeyError: Si les clés requises sont absentes
        ValueError: Si le format est invalide (ex: arête invalide)
    
    Validation:
        - Clés "nodes" et "edges" doivent exister
        - "nodes" : liste de chaînes
        - "edges" : liste de paires [a, b] ou (a, b)
        - Chaque arête doit référencer des nœuds existants
    
    Exemple:
        >>> data = {'nodes': ['A', 'B'], 'edges': [['A', 'B']]}
        >>> g = dict_to_graph(data)
        >>> g.has_edge("A", "B")
        True
    """
    # TODO: implémenter
    # Validation requise :
    # 1. Vérifier que "nodes" et "edges" existent
    # 2. Créer un graphe vide
    # 3. Ajouter tous les nœuds
    # 4. Pour chaque arête :
    #    - Vérifier format (liste/tuple de 2 éléments)
    #    - Vérifier que a et b existent dans nodes
    #    - Ajouter l'arête
    # 5. Gérer les exceptions proprement
    pass
