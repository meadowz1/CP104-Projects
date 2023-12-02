"""
------------------------------------------------------------------------
Lab 11, Task 14
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import matrix_transpose, print_matrix_num

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = matrix_transpose(matrix)
print_matrix_num(transposed, 'int')

print()

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = matrix_transpose(matrix)
print_matrix_num(transposed, 'int')

print()

matrix = []
transposed = matrix_transpose(matrix)
print_matrix_num(transposed, 'int')
