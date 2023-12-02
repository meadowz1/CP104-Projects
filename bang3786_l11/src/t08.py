"""
------------------------------------------------------------------------
Lab 11, Task 8
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import find_less

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = 7
loc = find_less(matrix, n)
print(f"Location of the first value smaller than {n}: {loc}")

print()

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
n = 5
loc = find_less(matrix, n)
print(f"Location of the first value smaller than {n}: {loc}")

print()

matrix = []
n = 5
loc = find_less(matrix, n)
print(f"Location of the first value smaller than {n}: {loc}")

