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

from functions import generate_matrix_char

# Test Case 1: Generating a matrix with valid dimensions
rows = 2
cols = 3
char_matrix = generate_matrix_char(rows, cols)
print("Matrix with dimensions (2, 3):")
print(char_matrix)

# Test Case 2: Generating a matrix with different dimensions
rows = 3
cols = 2
char_matrix = generate_matrix_char(rows, cols)
print("\nMatrix with dimensions (3, 2):")
print(char_matrix)

# Test Case 3: Generating a matrix with larger dimensions
rows = 4
cols = 4
char_matrix = generate_matrix_char(rows, cols)
print("\nMatrix with dimensions (4, 4):")
print(char_matrix)

# Test Case 4: Generating a matrix with no dimensions
rows = 0
cols = 0
char_matrix = generate_matrix_char(rows, cols)
print("\nMatrix with dimensions (0, 0):")
print(char_matrix)