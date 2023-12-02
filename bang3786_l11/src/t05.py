"""
------------------------------------------------------------------------
Lab 11, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import words_to_matrix, print_matrix_char

word_list = []
matrix = words_to_matrix(word_list)
print_matrix_char(matrix)

print()

word_list = ["apple", "orange", "banana"]
matrix = words_to_matrix(word_list)
print_matrix_char(matrix)

print()

word_list = ["cat", "dog", "elephant"]
matrix = words_to_matrix(word_list)
print_matrix_char(matrix)

print()

word_list = ["", "", ""]
matrix = words_to_matrix(word_list)
print_matrix_char(matrix)

