"""
------------------------------------------------------------------------
Lab 11, Task 12
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import find_word_diagonal

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "aei"
found = find_word_diagonal(matrix, word)
print(f"Word '{word}' on diagonal: {found}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "abc"
found = find_word_diagonal(matrix, word)
print(f"Word '{word}' on diagonal: {found}")

print()

matrix = []
word = "xyz"
found = find_word_diagonal(matrix, word)
print(f"Word '{word}' on diagonal: {found}")
