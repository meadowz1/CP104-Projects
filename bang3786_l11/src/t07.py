"""
------------------------------------------------------------------------
Lab 11, Task 7
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "'2023-12-01'
------------------------------------------------------------------------
"""

from functions import find_position

matrix = []
s_loc, l_loc = find_position(matrix)
print(f"Smallest Location: {s_loc}, Largest Location: {l_loc}")

print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s_loc, l_loc = find_position(matrix)
print(f"Smallest Location: {s_loc}, Largest Location: {l_loc}")

print()

matrix = [
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5]
]
s_loc, l_loc = find_position(matrix)
print(f"Smallest Location: {s_loc}, Largest Location: {l_loc}")

print()

matrix = [
    [1, 2.5, 3],
    [4.5, 5, 6.5],
    [7, 8.5, 9]
]
s_loc, l_loc = find_position(matrix)
print(f"Smallest Location: {s_loc}, Largest Location: {l_loc}")
