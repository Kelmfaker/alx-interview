#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Retourne une liste de listes
    d'entiers représentant le triangle de Pascal pour n.

    Renvoie une liste vide si n <= 0.
    On peut supposer que n sera toujours un entier.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
