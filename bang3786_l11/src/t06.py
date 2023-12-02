"""
------------------------------------------------------------------------
Lab 11, Task 6
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import matrix_stats

matrix = []
smallest, largest, total, average = matrix_stats(matrix)
print(f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}")

print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
smallest, largest, total, average = matrix_stats(matrix)
print(f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}")

print()

matrix = [
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5]
]
smallest, largest, total, average = matrix_stats(matrix)
print(f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}")

print()

matrix = [
    [1, 2.5, 3],
    [4.5, 5, 6.5],
    [7, 8.5, 9]
]
smallest, largest, total, average = matrix_stats(matrix)
print(f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}")

print()