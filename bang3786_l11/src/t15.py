"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2020-04-20"
------------------------------------------------------------------------
"""

from functions import matrix_equal

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
equal = matrix_equal(matrix1, matrix2)
print(f"Matrices are equal: {equal}")

print()

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
]
equal = matrix_equal(matrix1, matrix2)
print(f"Matrices are equal: {equal}")

print()

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2],
    [4, 5],
    [7, 8]
]
equal = matrix_equal(matrix1, matrix2)
print(f"Matrices are equal: {equal}")

print()

matrix1 = []
matrix2 = []
equal = matrix_equal(matrix1, matrix2)
print(f"Matrices are equal: {equal}")
