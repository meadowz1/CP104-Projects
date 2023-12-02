"""
------------------------------------------------------------------------
Lab 11, Task 9
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import count_frequency

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
char = "e"
count = count_frequency(matrix, char)
print(f"Frequency of '{char}' in the matrix: {count}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
char = "z"
count = count_frequency(matrix, char)
print(f"Frequency of '{char}' in the matrix: {count}")

print()

matrix = []
char = "a"
count = count_frequency(matrix, char)
print(f"Frequency of '{char}' in the matrix: {count}")
