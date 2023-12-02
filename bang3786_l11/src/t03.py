"""
------------------------------------------------------------------------
Labb 11, Task 3
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""
from functions import print_matrix_num

matrix = []
value_type = 'float'
print_matrix_num(matrix, value_type)

matrix = [
    [1.234, 2.345, 3.456],
    [4.567, 5.678, 6.789],
    [7.890, 8.901, 9.012]
]
value_type = 'float'
print_matrix_num(matrix, value_type)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
value_type = 'int'
print_matrix_num(matrix, value_type)