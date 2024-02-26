import numpy as np

def degree(A, i):
    return sum(A[i])

A = [
     [0, 1, 1, 0],
     [1, 0, 1, 1],
     [1, 1, 0, 1],
     [0, 1, 1, 0]
]
i = int(input("De quel sommet voulez vous connaitre le degre : "))
print("le degré du sommet", i, "est :", degree(A, i))