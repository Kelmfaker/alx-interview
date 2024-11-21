#!/usr/bin/python3
"""
Function - Rotate 2D Matrix
"""


# Function to rotate the matrix by 90 degrees counterclockwise
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(n)]

    # Flip the matrix counterclockwise using nested loops
    for i in range(n):
        for j in range(n):
            res[n - j - 1][i] = matrix[i][j]

    # Update the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]
