import numpy as np


def nombre_aretes(graph):
    edges = 0
    
    for node in graph:
        edges += len(graph[node])

    return edges // 2


def nombre_aretes_orientees(graph):
    edges = 0
    
    for node in graph:
        edges += len(graph[node])
    
    return edges

# Exemple d'utilisation avec un graphe représenté par une liste d'adjacence
graph_exemple = {'A': ['B','D','F'], 
                 'B': ['A', 'C', 'F'], 
                 'C': ['B', 'D','E'], 
                 'D': ['A','C','E'],
                 'E': ['B','C'],
                 'F': ['A','B']
                 }


resultat = nombre_aretes(graph_exemple)
resultat_oriente = nombre_aretes_orientees(graph_exemple)

print(f"Le nombre d'arêtes dans le graphe est : {resultat}")
print(f"Le nombre d'arêtes dans le graphe orienté est : {resultat_oriente}")