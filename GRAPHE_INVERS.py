import numpy as np


g = {0: {1}, 1: {2, 3, 4}, 2: {3, 0}, 3: {}, 4: {3}}

inverse_g = {sommet: set() for sommet in g}

# Parcours des sommets et des voisins du graphe pour calculer l'inverse
for sommet, voisins in g.items():
    for voisin in voisins:
        inverse_g[voisin].add(sommet)

inverse_liste = []
for sommet, voisins in inverse_g.items():
    inverse_liste.append(f"{sommet}: {voisins}")
print("\nInverse de g :")
print(inverse_liste)