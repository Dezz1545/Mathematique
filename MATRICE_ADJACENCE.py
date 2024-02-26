import numpy as np

# Fonction pour calculer la matrice d'adjacence d'un graphe
def MATRICE_ADJACENCE(graphe):
    n = len(graphe)
    matrice = [[0] * n for _ in range(n)]  # Initialisation d'une matrice n x n remplie de zéros
    
    # Parcours des sommets et de leurs voisins pour mettre à jour la matrice
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            matrice[sommet][voisin] = 1
    
    return matrice


g = {0: {1}, 1: {2, 3, 4}, 2: {3, 0}, 3: {}, 4: {3}}

matrice_g = MATRICE_ADJACENCE(g)
print("Matrice d'adjacence de g :")
for ligne in matrice_g:
    print(ligne)

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