"""
------------------------------------------------------------------------
Lab 11, Task 13
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import matrix_scalar_multiply, print_matrix_num

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
num = 2
matrix_scalar_multiply(matrix, num)
print_matrix_num(matrix, 'int')

print()

matrix = [
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5]
]
num = 0.5
matrix_scalar_multiply(matrix, num)
print_matrix_num(matrix, 'float')

print()

matrix = []
num = 3
matrix_scalar_multiply(matrix, num)
print_matrix_num(matrix, 'int')
