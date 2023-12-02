"""
------------------------------------------------------------------------
Lab 11, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import generate_matrix_num

# Test Case 1: Generating a matrix of floats
matrix_float = generate_matrix_num(2, 3, 0.0, 1.0, 'float')
print("Matrix of floats:")
print(matrix_float)

# Test Case 2: Generating a matrix of integers
matrix_int = generate_matrix_num(3, 2, 5, 10, 'int')
print("\nMatrix of integers:")
print(matrix_int)

# Test Case 3: Generating a case that shouldn't work
matrix_int = generate_matrix_num(3, 2, 0, 10, 'idk')
print("\nMatrix of 'idk':")
print(matrix_int)